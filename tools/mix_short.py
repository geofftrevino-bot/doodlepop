#!/usr/bin/env python3
"""Build a Fix-It Farm Short from its spec file (shorts/shortNN_<slug>/shortNN_spec.json).

The spec is the single source of timing: the Veo prompt, the lip-sync track
and the mix are all generated from it, so they can't disagree. See
docs/rebuild-workflow.md for the full loop and docs/spec-format.md for the
fields.

  pauses TAKE                 silences in a take, to pick each line's cut points
  check SPEC                  validate timing (overlaps, voice over mouth-closed beats)
  prompt SPEC                 print the Veo prompt, negative prompt and settings
  sheet SPEC [--clip C] [--crop W:H:X:Y] [--to T] [--fps F] --out IMG
                              timestamped frame grid of the clip, beats listed;
                              crop to the face at --fps 6 to see when the mouth moves
  retime SPEC N=AT [N=AT ...] move line N (1-based) to play at AT seconds; saves the spec
  lipsync-track SPEC [--tail] [--out]
                              voice-only lines at their positions, padded to the clip;
                              --tail: the sign-off, placed inside the tail clip
  mix SPEC [--out]            mastered Short (default: shortNN_final_test.mp4)

Paths in the spec resolve against the Short's folder first, then the repo root.
Each mix stage is rendered to its own WAV: a single filter graph dropped the
end of Short 4's last line. Master: voice -16 LUFS, music -22 ducked under the
voice, final -14 LUFS / -1.5 dBTP (two-pass, leaves room for AAC).
"""
import argparse, json, os, re, subprocess, sys, tempfile

SR = 48000
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
SIGNOFF_GAP = 0.72


# ---------- helpers ----------

def run(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def ffmpeg_log(*args):
    return subprocess.run(["ffmpeg", "-hide_banner", *args], capture_output=True, text=True).stderr


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout)


def silences(path, min_len):
    log = ffmpeg_log("-i", path, "-af", f"silencedetect=noise=-40dB:d={min_len}", "-f", "null", "-")
    s = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
    e = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    return list(zip(s, e + [duration(path)] * (len(s) - len(e))))


def speech_span(take, start, end):
    """(first, last) moment of speech inside [start, end] of the take."""
    first, last = start, end
    for s, e in silences(take, 0.05):
        if s <= start < e:
            first = min(e, end)
        if start < s <= end:
            last = s
    return first, max(first, last)


class Spec:
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.dir = os.path.dirname(self.path)
        with open(self.path) as f:
            self.d = json.load(f)

    def res(self, p):
        for base in (self.dir, REPO):
            if os.path.exists(os.path.join(base, p)):
                return os.path.join(base, p)
        raise SystemExit(f"{self.path}: can't find {p}")

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.d, f, indent=2, ensure_ascii=False)
            f.write("\n")

    @property
    def name(self):
        return os.path.basename(self.dir).split("_")[0]

    def take(self):
        return self.res(self.d["take"])

    def lines(self):
        """[(text, take_start, take_end, at, speech_from, speech_to)] on the Short's timeline."""
        take, tlen = self.take(), duration(self.take())
        out = []
        for ln in self.d["lines"]:
            s, e = ln["take"][0], ln["take"][1] if ln["take"][1] is not None else tlen
            f, l = speech_span(take, s, e)
            out.append((ln["text"], s, e, ln["at"], ln["at"] + f - s, ln["at"] + l - s))
        return out

    def picture(self):
        """(main clip, tail clip or None, total picture length)."""
        clip = self.res(self.d["clip"])
        tail = self.d.get("tail", {}).get("clip")
        tail = self.res(tail) if tail else None
        return clip, tail, duration(clip) + (duration(tail) if tail else 0)

    def signoff(self, lines):
        so = self.d["signoff"]
        at = so.get("at")
        if at is None:
            at = round(lines[-1][5] + SIGNOFF_GAP, 2)
        return self.res(so["file"]), at


# ---------- commands ----------

def cmd_pauses(a):
    d = duration(a.take)
    print(f"{a.take}: {d:.2f}s")
    for s, e in silences(a.take, 0.3):
        print(f"  silence {s:6.2f} -> {e:6.2f}  ({e - s:.2f}s)")


def cmd_check(a):
    sp = Spec(a.spec)
    lines = sp.lines()
    problems = []
    for i, (t, *_ , f, l) in enumerate(lines, 1):
        print(f"line {i}: {f:5.2f}-{l:5.2f}s  {t}")
    for i in range(1, len(lines)):
        if lines[i][4] < lines[i - 1][5] + 0.1:
            problems.append(f"line {i} and line {i + 1} overlap or touch")
    for b in sp.d.get("beats", []):
        if b.get("mouth") != "closed":
            continue
        for i, (t, *_, f, l) in enumerate(lines, 1):
            if f < b["to"] and l > b["from"]:
                problems.append(f"line {i} ({f:.2f}-{l:.2f}s) is spoken during a mouth-closed beat "
                                f"{b['from']}-{b['to']}s: {b['action']}")
    so_file, so_at = sp.signoff(lines)
    if so_at < lines[-1][5] + 0.3:
        problems.append(f"sign-off at {so_at}s starts too close to the last line")
    total = so_at + duration(so_file) + 0.25
    if sp.d.get("clip"):
        hold = total - sp.picture()[2]
        print(f"sign-off {so_at:.2f}s, runtime {total:.2f}s" + (f", last frame held {hold:.2f}s" if hold > 0 else ""))
    beats = sp.d.get("beats", [])
    if len(beats) > 6:
        problems.append(f"{len(beats)} beats; Veo follows 4-6 big beats far better than many small ones")
    for b in beats:
        if b["to"] - b["from"] < 0.75:
            problems.append(f"beat {b['from']}-{b['to']}s is under 0.75s; Veo tends to skip beats this short")
    print("\n".join(f"CHECK: {p}" for p in problems) or "OK")
    return 1 if problems else 0


def cmd_prompt(a):
    sp = Spec(a.spec)
    v = sp.d["video"]
    out = [
        "Vertical 9:16 bright 3D cartoon for preschoolers. ONE continuous shot. "
        "LOCKED-OFF CAMERA: the camera never pans, zooms, pushes in or cuts; the framing of the "
        "provided first frame is kept for all 8 seconds.",
        "Start exactly on the provided frame and keep every character, prop and the set exactly on-model. "
        + v["description"],
        "Mouths move ONLY in the beats marked SPEAKING. In every other beat the mouth stays closed.",
    ]
    for b in sp.d["beats"]:
        tag = "SPEAKING" if b.get("mouth") == "open" else "mouth closed"
        out.append(f"{b['from']:g} to {b['to']:g} seconds ({tag}): {b['action']}")
    print("PROMPT:\n" + "\n".join(out))
    neg = ["camera movement", "pan", "zoom", "push-in", "cuts", "scene change", "text", "captions",
           "logos", "extra characters"] + v.get("negative", [])
    print("\nNEGATIVE:\n" + ", ".join(neg))
    print(f"\nSETTINGS: model {v.get('model', 'veo-3.1-fast-generate-001')}, 8s, 9:16, 1080p, "
          f"generate_audio false, start frame {v['start_frame']}")


def cmd_sheet(a):
    sp = Spec(a.spec)
    clip = sp.res(a.clip or sp.d["clip"])
    fps, cols = a.fps, 8
    length = min(duration(clip), a.to or 1e9)
    n = int(length * fps)
    rows = (n + cols - 1) // cols
    crop = f"crop={a.crop}," if a.crop else ""
    run("-i", clip, "-vf",
        f"trim=0:{length},fps={fps},{crop}scale=160:-1,drawtext=fontfile={FONT}:text='%{{pts\\:flt}}':x=4:y=4:"
        f"fontsize=14:fontcolor=white:box=1:boxcolor=black@0.6,tile={cols}x{rows}",
        "-frames:v", "1", a.out)
    print(f"wrote {a.out} ({n} frames, every {1 / fps:g}s). Planned beats:")
    for b in sp.d.get("beats", []):
        print(f"  {b['from']:5.2f}-{b['to']:5.2f}s  [{b.get('mouth', 'closed')}] {b['action']}")


def cmd_retime(a):
    sp = Spec(a.spec)
    for m in a.moves:
        n, at = m.split("=")
        sp.d["lines"][int(n) - 1]["at"] = float(at)
    sp.save()
    print(f"saved {sp.path}")
    return cmd_check(a)


def voice_bus(sp, lines, out, total, with_signoff, channels=2):
    take = sp.take()
    parts, inputs = [], ["-i", take]
    for k, (_, s, e, at, *_r) in enumerate(lines):
        parts.append(f"[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,adelay={int(at * 1000)}:all=1[l{k}]")
    labels = "".join(f"[l{k}]" for k in range(len(lines)))
    n = len(lines)
    if with_signoff:
        so_file, so_at = sp.signoff(lines)
        inputs += ["-i", so_file]
        parts.append(f"[1:a]adelay={int(so_at * 1000)}:all=1[so]")
        labels += "[so]"
        n += 1
    parts.append(f"{labels}amix=inputs={n}:normalize=0:duration=longest,"
                 f"aresample={SR},apad=whole_dur={total},atrim=0:{total}")
    run(*inputs, "-filter_complex", ";".join(parts), "-ac", str(channels), out)


def cmd_lipsync_track(a):
    sp = Spec(a.spec)
    if a.tail:
        return lipsync_tail_track(sp, a.out)
    clip = sp.res(sp.d["video"].get("raw_clip") or sp.d["clip"])
    total = round(duration(clip), 3)
    out = a.out or os.path.join(sp.dir, f"{sp.name}_vo_lipsync_track.mp3")
    with tempfile.TemporaryDirectory() as t:
        voice_bus(sp, sp.lines(), os.path.join(t, "bus.wav"), total, with_signoff=False, channels=1)
        run("-i", os.path.join(t, "bus.wav"), "-ar", "44100", "-b:a", "192k", out)
    print(f"wrote {out} ({total}s, matches {os.path.basename(clip)})")


def lipsync_tail_track(sp, out):
    """Sign-off only, placed where it falls inside the tail clip."""
    t = sp.d["tail"]
    raw = sp.res(t.get("raw_clip") or t["clip"])
    so_file, so_at = sp.signoff(sp.lines())
    start = duration(sp.res(sp.d["clip"]))
    at = max(0.0, so_at - start)
    total = round(duration(raw), 3)
    out = out or os.path.join(sp.dir, f"{sp.name}_vo_lipsync_track_tail.mp3")
    run("-i", so_file, "-af", f"aresample=44100,adelay={int(at * 1000)}:all=1,"
        f"apad=whole_dur={total},atrim=0:{total}", "-ac", "1", "-b:a", "192k", out)
    print(f"wrote {out} ({total}s, sign-off at {at:.2f}s into {os.path.basename(raw)})")


def loudnorm_2pass(src, dst, i, tp):
    log = ffmpeg_log("-i", src, "-af", f"loudnorm=I={i}:TP={tp}:print_format=json", "-f", "null", "-")
    m = json.loads(log[log.rindex("{"):log.rindex("}") + 1])
    run("-i", src, "-af",
        f"loudnorm=I={i}:TP={tp}:linear=true:measured_I={m['input_i']}:"
        f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
        f"measured_thresh={m['input_thresh']}:offset={m['target_offset']},aresample={SR}",
        "-ac", "2", dst)


def cmd_mix(a):
    sp = Spec(a.spec)
    clip, tail, pic_len = sp.picture()
    lines = sp.lines()
    so_file, so_at = sp.signoff(lines)
    total = round(max(pic_len, so_at + duration(so_file) + 0.25), 2)
    hold = max(0.0, round(total - pic_len, 2))
    out = a.out or os.path.join(sp.dir, f"{sp.name}_final_test.mp4")
    print(f"last line ends {lines[-1][5]:.2f}s, sign-off at {so_at:.2f}s, runtime {total:.2f}s"
          + (f", last frame held {hold:.2f}s" if hold else ""))

    with tempfile.TemporaryDirectory() as t:
        p = lambda n: os.path.join(t, n)
        voice_bus(sp, lines, p("bus.wav"), total, with_signoff=True)
        loudnorm_2pass(p("bus.wav"), p("vo.wav"), -16, -2)
        stems = [p("vo.wav")]
        for k, fx in enumerate(sp.d.get("sfx", [])):
            run("-i", sp.res(fx["file"]), "-af",
                f"aresample={SR},adelay={int(fx['at'] * 1000)}:all=1,volume={fx.get('gain_db', -8)}dB,"
                f"apad=whole_dur={total},atrim=0:{total}", "-ac", "2", p(f"sfx{k}.wav"))
            stems.append(p(f"sfx{k}.wav"))
        music = sp.d.get("music")
        if music:
            run("-i", sp.res(music), "-af", f"aresample={SR},atrim=0:{total},loudnorm=I=-22,"
                f"aresample={SR},afade=t=out:st={max(0, total - 1.2)}:d=1.2,"
                f"apad=whole_dur={total},atrim=0:{total}", "-ac", "2", p("mus.wav"))
            run("-i", p("mus.wav"), "-i", p("vo.wav"), "-filter_complex",
                "[0:a][1:a]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300", p("duck.wav"))
            stems.append(p("duck.wav"))
        ins = sum((["-i", s] for s in stems), [])
        run(*ins, "-filter_complex",
            f"amix=inputs={len(stems)}:normalize=0:duration=longest,atrim=0:{total}", p("sum.wav"))
        loudnorm_2pass(p("sum.wav"), p("master.wav"), -14, -1.5)
        norm = "fps=24,scale=1080:1920,setsar=1,format=yuv420p"
        if tail:
            vin, vf = ["-i", clip, "-i", p("master.wav"), "-i", tail], (
                f"[0:v]{norm}[a];[2:v]{norm}[b];[a][b]concat=n=2:v=1:a=0,"
                f"tpad=stop_mode=clone:stop_duration={hold}[v]")
        else:
            vin, vf = ["-i", clip, "-i", p("master.wav")], (
                f"[0:v]{norm},tpad=stop_mode=clone:stop_duration={hold}[v]")
        run(*vin, "-filter_complex", vf, "-map", "[v]", "-map", "1:a",
            "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", str(SR), "-t", str(total), out)

    log = ffmpeg_log("-i", out, "-af", "ebur128=peak=true", "-f", "null", "-")
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", log)[-1]
    pk = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", log)[-1]
    print(f"wrote {out}: {total:.2f}s, {i} LUFS, peak {pk} dBFS")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("pauses").add_argument("take")
    for c in ("check", "prompt"):
        sub.add_parser(c).add_argument("spec")
    s = sub.add_parser("sheet")
    s.add_argument("spec")
    s.add_argument("--clip")
    s.add_argument("--fps", type=float, default=4)
    s.add_argument("--crop", metavar="W:H:X:Y", help="crop before tiling, e.g. the face, to read mouth movement")
    s.add_argument("--to", type=float, help="only the first N seconds")
    s.add_argument("--out", required=True)
    r = sub.add_parser("retime")
    r.add_argument("spec")
    r.add_argument("moves", nargs="+", metavar="N=AT")
    for c in ("lipsync-track", "mix"):
        p = sub.add_parser(c)
        p.add_argument("spec")
        p.add_argument("--out")
        if c == "lipsync-track":
            p.add_argument("--tail", action="store_true", help="sign-off track for the tail clip")
    a = ap.parse_args()
    fn = {"pauses": cmd_pauses, "check": cmd_check, "prompt": cmd_prompt, "sheet": cmd_sheet,
          "retime": cmd_retime, "lipsync-track": cmd_lipsync_track, "mix": cmd_mix}[a.cmd]
    return fn(a)


if __name__ == "__main__":
    sys.exit(main())
