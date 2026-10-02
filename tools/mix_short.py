#!/usr/bin/env python3
"""Build a Fix-It Farm Short from its spec file (shorts/shortNN_<slug>/shortNN_spec.json).

The spec is the single source of timing: the Veo prompt, the lip-sync track
and the mix are all generated from it, so they can't disagree. See
docs/rebuild-workflow.md for the full loop and docs/spec-format.md for the
fields.

  pauses TAKE                 silences in a take, to pick each line's cut points
  assemble-take SPEC L1 L2 …  trim separately recorded lines, join them into the take
                              with even gaps, and write each line's cut points
  check SPEC                  validate timing (overlaps, voice over mouth-closed beats)
  prompt SPEC                 print the Veo prompt, negative prompt and settings
  sheet SPEC [--clip C] [--crop W:H:X:Y] [--to T] [--fps F] --out IMG
                              timestamped frame grid of the clip, beats listed;
                              crop to the face at --fps 6 to see when the mouth moves
  retime SPEC N=AT [N=AT ...] move line N (1-based) to play at AT seconds; saves the spec
  seams SPEC --out IMG        frames either side of every cut, to catch rough handoffs
  picture SPEC [--out]        join shots/clip/tail into one silent picture (for one lip-sync pass);
                              a shot's "xfade" dissolves into it instead of hard-cutting
  lipsync-track SPEC [--tail|--full] [--out]
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
            tp = ln.get("tempo", 1.0)
            out.append((ln["text"], s, e, ln["at"], ln["at"] + (f - s) / tp, ln["at"] + (l - s) / tp))
        return out

    def tempos(self):
        return [ln.get("tempo", 1.0) for ln in self.d["lines"]]

    def segments(self):
        """[(clip path, seconds used, start in clip)] in order: shots (or the clip), then the tail.
        A shot's optional "from" starts it partway into its clip, so one clip can supply several cuts."""
        segs = []
        if self.d.get("shots"):
            for sh in self.d["shots"]:
                c, f = self.res(sh["clip"]), sh.get("from", 0.0)
                segs.append((c, min(duration(c) - f, sh.get("use", 1e9)), f, sh.get("xfade", 0.0)))
        else:
            c = self.res(self.d["clip"])
            segs.append((c, duration(c), 0.0, 0.0))
        t = self.d.get("tail", {})
        if t.get("clip"):
            c = self.res(t["clip"])
            segs.append((c, min(duration(c), t.get("use", 1e9)), 0.0, t.get("xfade", 0.0)))
        return segs

    def picture(self):
        """(main clip, tail clip or None, total picture length)."""
        if self.d.get("shots"):
            segs = self.segments()
            return None, None, sum(u for _, u, _, _ in segs) - sum(x for _, _, _, x in segs[1:])
        clip = self.res(self.d["clip"])
        t = self.d.get("tail", {})
        tail = self.res(t["clip"]) if t.get("clip") else None
        tail_len = min(duration(tail), t.get("use", 1e9)) if tail else 0
        return clip, tail, duration(clip) + tail_len

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
    try:
        pic = sp.picture()[2] if (sp.d.get("clip") or sp.d.get("shots")) else None
    except SystemExit:
        pic = None
        print("picture not complete yet (some shot clips missing)")
    if pic is not None:
        hold = total - pic
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
    beats, secs, start = sp.d.get("beats", []), 8, v.get("start_frame")
    if a.shot:
        sh = sp.d["shots"][a.shot - 1]
        beats, secs, start = sh["beats"], 4, sh.get("start_frame", start)
    out = [
        "Vertical 9:16 bright 3D cartoon for preschoolers. ONE continuous shot. "
        "LOCKED-OFF CAMERA: the camera never pans, zooms, pushes in or cuts; the framing of the "
        f"provided first frame is kept for all {secs} seconds.",
        "Start exactly on the provided frame and keep every character, prop and the set exactly on-model. "
        + v["description"],
        "Mouths move ONLY in the beats marked SPEAKING. In every other beat the mouth stays closed.",
    ]
    for b in beats:
        tag = "SPEAKING" if b.get("mouth") == "open" else "mouth closed"
        out.append(f"{b['from']:g} to {b['to']:g} seconds ({tag}): {b['action']}")
    print("PROMPT:\n" + "\n".join(out))
    neg = ["camera movement", "pan", "zoom", "push-in", "cuts", "scene change", "text", "captions",
           "logos", "extra characters"] + v.get("negative", [])
    print("\nNEGATIVE:\n" + ", ".join(neg))
    print(f"\nSETTINGS: model {v.get('model', 'veo-3.1-fast-generate-001')}, {secs}s, 9:16, 1080p, "
          f"generate_audio false, start frame {start}")


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
    for k, ((_, s, e, at, *_r), tp) in enumerate(zip(lines, sp.tempos())):
        speed = f",atempo={tp}" if tp != 1.0 else ""  # pitch-preserving speed-up for a tight picture
        parts.append(f"[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS{speed},adelay={int(at * 1000)}:all=1[l{k}]")
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


def cmd_assemble_take(a):
    """Trim each separately recorded line, join with even gaps into the take, set the cut points."""
    sp = Spec(a.spec)
    if len(a.files) != len(sp.d["lines"]):
        raise SystemExit(f"{len(a.files)} files for {len(sp.d['lines'])} lines")
    trim = ("silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
            "silenceremove=start_periods=1:start_threshold=-45dB,areverse,aresample=44100")
    out = os.path.join(sp.dir, sp.d["take"])
    with tempfile.TemporaryDirectory() as t:
        parts, pos = [], 0.0
        run("-f", "lavfi", "-t", str(a.gap), "-i", "anullsrc=r=44100:cl=mono", os.path.join(t, "gap.wav"))
        for k, f in enumerate(a.files):
            w = os.path.join(t, f"l{k}.wav")
            run("-i", f, "-af", trim, "-ac", "1", w)
            d = duration(w)
            # cut 0.05s into the gap on each side so no consonant is clipped
            sp.d["lines"][k]["take"] = [round(max(0, pos - 0.05), 2),
                                        round(pos + d + 0.05, 2) if k < len(a.files) - 1 else None]
            parts += [w] + ([os.path.join(t, "gap.wav")] if k < len(a.files) - 1 else [])
            pos += d + a.gap
        ins = sum((["-i", w] for w in parts), [])
        run(*ins, "-filter_complex", f"concat=n={len(parts)}:v=0:a=1", "-b:a", "192k", out)
    sp.save()
    for k, ln in enumerate(sp.d["lines"], 1):
        print(f"line {k}: take {ln['take']}  {ln['text']}")
    print(f"wrote {out}; place the lines with retime, then check")


NORM = "fps=24,scale=1080:1920,setsar=1,format=yuv420p"


def video_join(segs, first=0):
    """Inputs and filter joining segments into [vj]. A segment's xfade (seconds) dissolves
    into it from the previous one instead of hard-cutting, which smooths handoffs between
    separately generated clips; each dissolve shortens the picture by its length."""
    ins = sum((["-i", c] for c, _, _, _ in segs), [])
    parts = [f"[{k + first}:v]trim={f}:{f + u},setpts=PTS-STARTPTS,{NORM}[s{k}]"
             for k, (_, u, f, _) in enumerate(segs)]
    cur, cum = "[s0]", segs[0][1]
    for k in range(1, len(segs)):
        u, x = segs[k][1], segs[k][3]
        out = f"[j{k}]"
        if x > 0:
            parts.append(f"{cur}[s{k}]xfade=transition=fade:duration={x}:offset={cum - x:.3f}{out}")
            cum += u - x
        else:
            parts.append(f"{cur}[s{k}]concat=n=2:v=1:a=0{out}")
            cum += u
        cur = out
    parts.append(f"{cur}null[vj]")
    return ins, ";".join(parts)


def cmd_seams(a):
    """Last frame before and first frame after every cut, side by side, to catch jumps
    (pose, framing, lighting) before paying for a lip-sync pass."""
    sp = Spec(a.spec)
    segs = sp.segments()
    with tempfile.TemporaryDirectory() as t:
        tiles = []
        for k in range(1, len(segs)):
            (c0, u0, f0, _), (c1, _, f1, x) = segs[k - 1], segs[k]
            a0, a1 = os.path.join(t, f"{k}a.png"), os.path.join(t, f"{k}b.png")
            run("-ss", f"{max(0, f0 + u0 - 0.05):.3f}", "-i", c0, "-frames:v", "1", "-vf", "scale=180:-1", a0)
            run("-ss", f"{f1:.3f}", "-i", c1, "-frames:v", "1", "-vf", "scale=180:-1", a1)
            pair = os.path.join(t, f"{k}.png")
            run("-i", a0, "-i", a1, "-filter_complex",
                f"hstack=2,drawtext=fontfile={FONT}:text='cut {k}{' xfade ' + str(x) if x else ''}':"
                "x=4:y=4:fontsize=13:fontcolor=white:box=1:boxcolor=black@0.6", pair)
            tiles.append(pair)
        ins = sum((["-i", p] for p in tiles), [])
        run(*ins, "-filter_complex", f"vstack={len(tiles)}" if len(tiles) > 1 else "null", a.out)
    print(f"wrote {a.out}: {len(segs) - 1} cuts (left = outgoing, right = incoming)")


def cmd_picture(a):
    """Join shots/clip/tail into one silent picture, e.g. for a single lip-sync pass."""
    sp = Spec(a.spec)
    segs = sp.segments()
    ins, vf = video_join(segs)
    out = a.out or os.path.join(sp.dir, f"{sp.name}_clip_joined.mp4")
    run(*ins, "-filter_complex", vf, "-map", "[vj]", "-c:v", "libx264", "-crf", "16",
        "-pix_fmt", "yuv420p", "-an", out)
    print(f"wrote {out} ({duration(out):.2f}s from {len(segs)} segments)")


def cmd_lipsync_track(a):
    sp = Spec(a.spec)
    if a.tail:
        return lipsync_tail_track(sp, a.out)
    if a.full:
        total = round(sp.picture()[2], 3)
        out = a.out or os.path.join(sp.dir, f"{sp.name}_vo_lipsync_track.mp3")
        with tempfile.TemporaryDirectory() as t:
            voice_bus(sp, sp.lines(), os.path.join(t, "bus.wav"), total, with_signoff=True, channels=1)
            run("-i", os.path.join(t, "bus.wav"), "-ar", "44100", "-b:a", "192k", out)
        print(f"wrote {out} ({total}s: all lines + sign-off, for the joined picture)")
        return
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
    pic_len = sp.picture()[2]
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
        ins, vf = video_join(sp.segments(), first=1)
        vf += f";[vj]tpad=stop_mode=clone:stop_duration={hold}[v]"
        run("-i", p("master.wav"), *ins, "-filter_complex", vf, "-map", "[v]", "-map", "0:a",
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
    sub.add_parser("check").add_argument("spec")
    pp = sub.add_parser("prompt")
    pp.add_argument("spec")
    pp.add_argument("--shot", type=int, help="prompt for chained shot N (1-based), 4s")
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
    at = sub.add_parser("assemble-take")
    at.add_argument("spec")
    at.add_argument("files", nargs="+", help="one audio file per line, in order")
    at.add_argument("--gap", type=float, default=1.0)
    sm = sub.add_parser("seams")
    sm.add_argument("spec")
    sm.add_argument("--out", required=True)
    pc = sub.add_parser("picture")
    pc.add_argument("spec")
    pc.add_argument("--out")
    for c in ("lipsync-track", "mix"):
        p = sub.add_parser(c)
        p.add_argument("spec")
        p.add_argument("--out")
        if c == "lipsync-track":
            p.add_argument("--tail", action="store_true", help="sign-off track for the tail clip")
            p.add_argument("--full", action="store_true",
                           help="lines + sign-off over the whole joined picture (shots + tail)")
    a = ap.parse_args()
    fn = {"pauses": cmd_pauses, "check": cmd_check, "prompt": cmd_prompt, "sheet": cmd_sheet,
          "retime": cmd_retime, "lipsync-track": cmd_lipsync_track, "mix": cmd_mix,
          "picture": cmd_picture, "assemble-take": cmd_assemble_take,
          "seams": cmd_seams}[a.cmd]
    return fn(a)


if __name__ == "__main__":
    sys.exit(main())
