# Fix-It Farm — REBUILD WORKFLOW

> **Tool:** `tools/mix_short.py` · **Spec:** `docs/spec-format.md`
> **Worked examples:** Short 4 (`short04_spec.json`), Short 14 (`short14_spec.json`)

One Short at a time. Every paid step gets a cost estimate and the user's OK
first. All `mix_short.py` steps are local and free.

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

## WHAT WE LEARNED (Shorts 4, 14, 11 and 10)

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
