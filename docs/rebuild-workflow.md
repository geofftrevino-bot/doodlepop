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
| 5 | Generate the Veo prompt | `prompt <spec>` | free |
| 6 | **Estimate, get OK**, then generate the clip from `start_frame` | ElevenLabs video, `estimate_only` first | ~$0.80 |
| 7 | Download it as `shortNN_clip_vN.mp4` and make the frame grid | `sheet <spec> --clip … --out …` | free |
| 8 | Update `beats` to what Veo actually did, then move the lines to fit | `retime <spec> N=AT …` (re-runs `check`) | free |
| 9 | Build the voice-only track and commit it, so ElevenLabs can fetch it by URL | `lipsync-track <spec>` | free |
| 10 | **Estimate, get OK**, then run the lip-sync pass: the **raw clip** + the track into `sync-lipsync-v3`, `sync_mode: cut_off` | ElevenLabs video | ~$1.06 |
| 11 | Download it as `shortNN_clip_vN_lipsync.mp4` and set it as `clip` in the spec | — | free |
| 12 | Mix | `mix <spec>` → `shortNN_final_test.mp4` | free |
| 13 | User watches and listens. Fix timing with `retime` and re-mix; don't regenerate unless the picture itself is wrong | — | free |
| 14 | On approval, rename to `shortNN_final.mp4` (replacing the old one) and delete the test | `git mv` | free |

**Typical Short:** about $1.90 (take ~2¢ + clip ~$0.80 + lip-sync ~$1.06).

---

## WHAT WE LEARNED (Shorts 4 and 14)

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
