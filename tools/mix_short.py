#!/usr/bin/env python3
"""Mix a Fix-It Farm Short: silent clip + single VO take + sign-off + music.

Each stage is rendered to its own WAV so nothing gets dropped between filters
(a single filter graph lost the end of Short 4's last line).

  python3 tools/mix_short.py pauses TAKE
      Print the take's silences, to pick each line's cut points.

  python3 tools/mix_short.py mix --clip CLIP --take TAKE \\
      --line 0:2.20@0.15 --line 3.37:5.48@2.40 --line 7.27:@6.15 \\
      --signoff audio/signoffs/signoff_sprocket.mp3 [--signoff-at 7.98] \\
      [--sfx PATH@4.0[:-8]] [--music audio/theme/theme_sting.mp3] \\
      --out shorts/shortNN_slug/shortNN_final.mp4

--line is TAKE_START:TAKE_END@PLACE_AT in seconds (empty END = to the end of
the take). Without --signoff-at the sign-off goes 0.72s after the last line
ends. Runtime is the sign-off end + 0.25s; if that's longer than the clip,
the last frame is held. Master: voice -16 LUFS, music -22 ducked under the
voice, final -14 LUFS / -1.5 dBTP (two-pass, leaves room for AAC).
"""
import argparse, json, os, re, subprocess, sys, tempfile

SR = 48000


def run(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout)


def speech_end(path, start, end):
    """Time (in the take) where speech last stops inside [start, end]."""
    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af",
                          "silencedetect=noise=-40dB:d=0.05", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
    inside = [s for s in starts if start < s <= end]
    return inside[-1] if inside else end


def pauses(take):
    d = duration(take)
    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", take, "-af",
                          "silencedetect=noise=-40dB:d=0.3", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    s = re.findall(r"silence_start: ([\d.]+)", log)
    e = re.findall(r"silence_end: ([\d.]+)", log)
    print(f"{take}: {d:.2f}s")
    for a, b in zip(s, e + [f"{d}"]):
        print(f"  silence {float(a):6.2f} -> {float(b):6.2f}  ({float(b) - float(a):.2f}s)")


def loudnorm_2pass(src, dst, i, tp):
    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", src, "-af",
                          f"loudnorm=I={i}:TP={tp}:print_format=json", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    m = json.loads(log[log.rindex("{"):log.rindex("}") + 1])
    run("-i", src, "-af",
        f"loudnorm=I={i}:TP={tp}:linear=true:measured_I={m['input_i']}:"
        f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
        f"measured_thresh={m['input_thresh']}:offset={m['target_offset']},aresample={SR}",
        "-ac", "2", dst)


def mix(a):
    take_len = duration(a.take)
    lines = []
    for spec in a.line:
        rng, at = spec.split("@")
        s, e = rng.split(":")
        s, e, at = float(s), float(e) if e else take_len, float(at)
        lines.append((s, e, at))
    last_s, last_e, last_at = lines[-1]
    last_end = last_at + speech_end(a.take, last_s, last_e) - last_s
    so_at = a.signoff_at if a.signoff_at is not None else round(last_end + 0.72, 2)
    total = round(max(duration(a.clip), so_at + duration(a.signoff) + 0.25), 2)
    hold = max(0.0, total - duration(a.clip))
    print(f"last line ends {last_end:.2f}s, sign-off at {so_at:.2f}s, runtime {total:.2f}s"
          + (f", last frame held {hold:.2f}s" if hold else ""))

    with tempfile.TemporaryDirectory() as t:
        p = lambda n: os.path.join(t, n)
        # 1. voice bus: each line trimmed from the take and placed, plus sign-off
        parts, inputs = [], ["-i", a.take, "-i", a.signoff]
        for k, (s, e, at) in enumerate(lines):
            parts.append(f"[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,"
                         f"adelay={int(at * 1000)}:all=1[l{k}]")
        parts.append(f"[1:a]adelay={int(so_at * 1000)}:all=1[so]")
        labels = "".join(f"[l{k}]" for k in range(len(lines))) + "[so]"
        parts.append(f"{labels}amix=inputs={len(lines) + 1}:normalize=0:duration=longest,"
                     f"aresample={SR},apad=whole_dur={total},atrim=0:{total}")
        run(*inputs, "-filter_complex", ";".join(parts), "-ac", "2", p("bus.wav"))
        loudnorm_2pass(p("bus.wav"), p("vo.wav"), -16, -2)
        stems = [p("vo.wav")]

        # 2. sound effects
        for k, spec in enumerate(a.sfx or []):
            path, rest = spec.split("@")
            at, _, gain = rest.partition(":")
            run("-i", path, "-af", f"aresample={SR},adelay={int(float(at) * 1000)}:all=1,"
                f"volume={gain or -8}dB,apad=whole_dur={total},atrim=0:{total}",
                "-ac", "2", p(f"sfx{k}.wav"))
            stems.append(p(f"sfx{k}.wav"))

        # 3. music, levelled, faded, ducked under the voice
        if a.music:
            run("-i", a.music, "-af", f"aresample={SR},atrim=0:{total},loudnorm=I=-22,"
                f"aresample={SR},afade=t=out:st={max(0, total - 1.2)}:d=1.2,"
                f"apad=whole_dur={total},atrim=0:{total}", "-ac", "2", p("mus.wav"))
            run("-i", p("mus.wav"), "-i", p("vo.wav"), "-filter_complex",
                "[0:a][1:a]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300",
                p("duck.wav"))
            stems.append(p("duck.wav"))

        # 4. sum, 5. master
        ins = sum((["-i", s] for s in stems), [])
        run(*ins, "-filter_complex", f"amix=inputs={len(stems)}:normalize=0:duration=longest,"
            f"atrim=0:{total}", p("sum.wav"))
        loudnorm_2pass(p("sum.wav"), p("master.wav"), -14, -1.5)

        # 6. picture
        run("-i", a.clip, "-i", p("master.wav"), "-filter_complex",
            f"[0:v]tpad=stop_mode=clone:stop_duration={hold}[v]", "-map", "[v]", "-map", "1:a",
            "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", str(SR), "-t", str(total), a.out)

    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", a.out, "-af", "ebur128=peak=true",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", log)[-1]
    pk = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", log)[-1]
    print(f"wrote {a.out}: {total:.2f}s, {i} LUFS, peak {pk} dBFS")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("pauses")
    sp.add_argument("take")
    mp = sub.add_parser("mix")
    mp.add_argument("--clip", required=True)
    mp.add_argument("--take", required=True)
    mp.add_argument("--line", action="append", required=True)
    mp.add_argument("--signoff", required=True)
    mp.add_argument("--signoff-at", type=float)
    mp.add_argument("--sfx", action="append")
    mp.add_argument("--music", default="audio/theme/theme_sting.mp3")
    mp.add_argument("--out", required=True)
    a = ap.parse_args()
    pauses(a.take) if a.cmd == "pauses" else mix(a)


if __name__ == "__main__":
    sys.exit(main())
