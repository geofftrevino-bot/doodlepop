# Fix-It Farm — REBUILD WORKFLOW

> **Tool:** `tools/mix_short.py` · **Spec:** `docs/spec-format.md`
> **Worked examples:** Short 4 (`short04_spec.json`), Short 14 (`short14_spec.json`)

One Short at a time. Every paid step gets a cost estimate and the user's OK
first. All `mix_short.py` steps are local and free.

---

## FAST PATH (from Short 3 on)

Fewer generations, fewer waits, and the timing and lip-sync gains kept. One
paid picture step and one paid lip-sync step per Short.

| # | Step | Command / tool | Cost |
|---|---|---|---|
| 1 | **Record each line separately with Eleven v3** and audio tags (`[excited]`, `[happy]`, `[curious]`…), 2 variations per line, all lines in parallel. v3 ignores `<break>`, which no longer matters. A bad line is redone alone | ElevenLabs speech | ~1¢ per line |
| 2 | Join the picked lines into the take and write the cut points | `assemble-take <spec> l1.mp3 l2.mp3 …` | free |
| 3 | Place lines on the story beats (the bloom, the reveal), not on mouths, and check | `retime`, `check` | free |
| 4 | **Picture:** reuse the existing clip if its staging works; otherwise one 8s Veo clip for staging. Chain 4s shots only when a gag needs a beat Veo won't hit in 8s (Short 3's bloom). End with a 4s tail for the sign-off | ElevenLabs video | $0.40–$1.60 |
| 4b | **Check every cut before paying for lip sync.** Fix any seam that jumps (see *Smooth handoffs* below) | `seams <spec> --out …` | free |
| 5 | Join everything into one silent picture and build one voice track (lines + sign-off) | `picture <spec>`, `lipsync-track <spec> --full` | free |
| 6 | **One lip-sync pass over the whole Short** (`sync-lipsync-v3`, `cut_off`). It fixes every line and the sign-off at once, so no 6fps face grids or per-line mouth matching | ElevenLabs video | ~$0.13/s (~$1.36 for 10s) |
| 7 | Set the synced picture as `clip` (drop `shots`/`tail`), mix, review, approve | `mix <spec>` | free |

**Before step 6, confirm shared assets are right** (each sign-off and catchphrase is in its own
character's voice). Short 5's `signoff_nugget.mp3` turned out to be Sprocket, and fixing
it after the pass meant re-syncing and splicing the ending.

### Smooth handoffs between sections

What made Short 5's cuts rough (seen with `seams`), and what to do instead:

| Problem | Fix |
|---|---|
| **Backgrounds don't match.** Each close-up was generated on a different set (shelves, pegboard, wagon wheel), so every cut jumped rooms | Make every shot of a Short from stills built on the **same location plate** (`refs/locations/`) and camera height. Or chain shots from cut frames (Short 3's chain was seamless) |
| **Shot scale jumps** close-up → wide → close-up | Use the wide shot once (open or button), and keep dialogue at one scale. One-character close-ups for lip sync, but matched framing |
| **Cutting mid-blink or mid-gesture** | Pick cut points on a settled pose; check both sides with `seams`, move `from`/`use` by a few frames |
| **Hard cut between separately generated clips** | Add `"xfade": 0.15`–`0.2` on the incoming shot (a short dissolve). Keep hard cuts for chained shots, where the frames already match. Each dissolve shortens the Short by its length, so re-place lines after |
| **Patching part of a synced picture** | Get every voice right first so the single lip-sync pass is final |

**Typical Short on the fast path:** ~$1.80–$3.00 and about 4 waits instead of 8–10.

What the docs say (ElevenLabs model guide, lip-sync family): the audio track
drives the result, so keep it clean (voice only, no music or SFX); the models
work best on clear, front-facing faces; `sync_mode` is the only setting. So:
stage speaking moments face-to-camera and give the pass a voice-only track.

---

## THE LOOP

| # | Step | Command / tool | Cost |
|---|---|---|---|
| 1 | Record the take with **Multilingual v2**, text and breaks from `docs/vo-retake-guide.md`. 2 variations | ElevenLabs speech | ~2¢ |
| 2 | Check the breaks rendered and pick the take that splits cleanly | `pauses <take>` | free |
| 3 | Write the spec: lines (cut points from step 2), planned beats, sign-off, SFX | edit `shortNN_spec.json` | free |
| 4 | Validate | `check <spec>` | free |
| 5 | **Grid the existing clip first.** If its action already matches the lines, skip to step 8 with it (Short 11 needed no new video). Otherwise generate the Veo prompt | `sheet <spec> --out …`, then `prompt <spec>` | free |
| 6 | **Estimate, get OK**, then generate the clip from `start_frame` | ElevenLabs video, `estimate_only` first | ~$0.80 |
| 7 | Download it as `shortNN_clip_vN.mp4` and make the frame grid | `sheet <spec> --clip … --out …` | free |
| 8 | Grid the face to see exactly when the mouth opens and closes. Update `beats` to what's on screen, then start each line when the mouth opens | `sheet <spec> --crop W:H:X:Y --fps 6 --to T --out …`, then `retime <spec> N=AT …` | free |
| 9 | Build the voice-only track and commit it, so ElevenLabs can fetch it by URL | `lipsync-track <spec>` | free |
| 10 | Optional: if the mouth still doesn't match after re-timing, **estimate, get OK**, then run the lip-sync pass: the **raw clip** + the track into `sync-lipsync-v3`, `sync_mode: cut_off` | ElevenLabs video | ~$1.06 |
| 11 | Download it as `shortNN_clip_vN_lipsync.mp4` and set it as `clip` in the spec | — | free |
| 11b | Optional: if the sign-off would play over a frozen frame, grab the clip's last frame, generate a **4s** Veo tail from it (Sprocket faces camera and speaks, then grins), save it as `shortNN_clip_tail.mp4`, and add a `tail` to the spec with `use` set to just past the sign-off. Set `signoff.at` to when the mouth starts moving in the tail | `ffmpeg -sseof`, ElevenLabs video | ~$0.40 |
| 12 | Mix | `mix <spec>` → `shortNN_final_test.mp4` | free |
| 13 | User watches and listens. Fix timing with `retime` and re-mix; don't regenerate unless the picture itself is wrong | — | free |
| 14 | On approval, rename to `shortNN_final.mp4` (replacing the old one) and delete the test | `git mv` | free |

**Typical Short:** 2¢ to about $2.30. Take ~2¢ always; clip ~$0.80 only if the existing picture doesn't fit; lip-sync ~$1.06 only if re-timing isn't enough; tail ~$0.40 only if the sign-off would freeze.

---

## WHAT WE LEARNED (Shorts 4, 14, 11, 10, 2, 3, 5 and 7)

- **Eleven v4 and v3 ignore `<break>` tags.** The pauses come out at ~0.4s, the
  same as pauses between sentences, so the lines can't be split. Use Multilingual v2.
- **Mix in stages, never one filter graph.** A single graph dropped the end of
  Short 4's last line ("Told you"). `mix` renders every stage to its own file.
- **Veo runs early and simplifies.** Both clips hit their beats about a second
  early, skipped a small beat, and moved the camera despite the prompt. So:
  4–6 big beats, mouth open/closed per beat, a locked-camera line, then re-time
  the voice to the picture rather than paying to regenerate.
- **Lip-sync with the voice only.** No music or SFX, the lines at their real
  positions, silence elsewhere. Leave the sign-off out if the face is off-screen by then.
- **ElevenLabs downloads work from the session.** Finished generations go
  straight into the repo; no manual download and upload needed.
- **Peak headroom.** Master to −1.5 dBTP so AAC encoding stays under −1 dB.
- **Re-time before paying.** Short 11's existing clip fit once the first line
  started when Rocco's beak opened (0.85s instead of the plan's 1.72s).
  Read mouth onset off a face-cropped `sheet`; plan anchors can be a beat late.
- **A line started late reads as bad lip sync.** A mouth moving with no voice
  is the most noticeable mismatch. Start lines on mouth onset, not after it.
- **Duck SFX under voice by hand.** Only the music is ducked automatically. An
  SFX that overlaps a line needs its own lower `gain_db` (−14 under voice, −8 alone).
- **Always record 2 variations.** One of the two Short 11 takes rendered no
  pause at all, even on Multilingual v2.
- **Rocco's sign-off is ~2s**, so his Shorts run ~9.5s with a longer held frame.
- **A tail beats a frozen frame.** Short 10's sign-off sat on a 1.7s freeze.
  A 4s Veo tail started from the last frame joins seamlessly; Veo's own mouth
  movement on a short catchphrase was close enough without a lip-sync pass.
  Use only as much of the tail as the sign-off needs, to keep Shorts ~10s.
- **Crops drift when the camera zooms.** On Short 10 a fixed face crop slid off
  the mouth; grid larger full frames instead.
- **The tails lip-synced almost perfectly without a lip-sync pass** (Shorts 10
  and 2). What they had that the 8s clips didn't:
  1. **The audio existed first.** The speaking window was sized to the actual
     sign-off (Rocco's 2.1s → a 0.4–2.6s SPEAKING beat), not to a plan guess.
  2. **One line per clip.** One speaking window, a closed beat before and after.
  3. **Face to camera the whole time**, no walking, turning or business with props.
  4. **Short clips (4s).** Veo holds timing far better over 4s than over 8s.
  5. **The audio went where the mouth actually opened** (read off a 6fps face grid).
- **Next Short to try it on: build the picture as a chain of 4s shots, one per
  line,** each started from the previous shot's last frame, with its SPEAKING
  window sized to that line's real length from the take. Trim each shot to its
  line plus the gap and join them. About $0.40 per line, so a 3-line Short plus
  sign-off tail is ~$1.60, less than an 8s clip + lip-sync pass (~$1.86), and
  it should sync better.
- **Chained 4s shots fix staging, not lip sync** (Short 3). Each shot joined
  seamlessly and the bloom landed, but Veo kept the talking to ~0.5–1s per shot
  however long the SPEAKING window was, and quoting the words in the prompt
  didn't change that. Only the ~1.3–2s sign-off tails line up on their own.
  Lines over ~1s need the lip-sync pass.
- **Veo starts the mouth at once and walks off at the end.** Put SPEAKING at
  0s, and cut a shot before the character turns away (Short 3 shot C at 3.3s).
- **Eleven v3 + tags for energy.** Multilingual v2 read Clover flat. v3 with
  `[excited]`/`[happy]` and a capitalised key word ("I GROW things!", "And LOOK
  what happens!") is livelier. Record line by line so v3's lack of `<break>`
  doesn't matter.
- **Watch for repeated words across a cut.** Short 3's "…and… look" read as an
  extra "and" between shots; script lines so each starts cleanly.
- **The fast path works with no new video** (Short 5: ~$1.85). Close-ups cut from
  existing clips, one character per shot, one lip-sync pass. But cutting between
  independently generated clips is where it shows its seams; see *Smooth handoffs*.
- **Match voice energy to the script's direction note with v3 tags.** Each line's
  note in `docs/vo-retake-guide.md` maps straight onto tags: "breathless, all-caps
  energy" → `[excited] [breathless]` + CAPS; "dry and fond" → `[warmly] [chuckles]`.
- **Stretch a clip with an inserted shot whose first and last frames are cut
  from the clip itself** (Short 7). The lines ran ~3s longer than the action
  before the carrot. A 4s Veo shot generated from the clip's frame at 5.4s to its
  frame at 5.5s slots between them with no visible join, and 1.1× `tempo` took
  up the rest.
- **Read the tail before setting `use`.** Short 7's tail walked off at ~3.4s, so
  the cut is at 2.9s (mouth onset 0.45s + 2.06s sign-off + a short grin).
- **The lip-sync pass often changes nothing on our cartoon faces** (found after
  Short 8). `sync-check` against the input shows Shorts 2, 5 (main picture), 6
  and 8 came back pixel-identical: the model found no face to sync, so the lip
  sync seen there was Veo's own mouth movement plus where we placed the lines.
  Only Short 5's sign-off, 7, 10 and 14 were edited at all. Wide shots with two
  characters and small rabbit or chick mouths fail most. **Run `sync-check`
  after every pass**, and don't pay for one on wide two-character shots.
