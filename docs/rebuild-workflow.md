# Fix-It Farm — REBUILD WORKFLOW

> **Tool:** `tools/mix_short.py` · **Spec:** `docs/spec-format.md`
> **Worked examples:** Short 4 (`short04_spec.json`), Short 14 (`short14_spec.json`)

One Short at a time. Every paid step gets a cost estimate and the user's OK
first. All `mix_short.py` steps are local and free.

---

## CHARACTER CONSISTENCY (from Short 2 v2 on) — every new picture

The official look of each character is its reference in `refs/characters/`
(`rocco_ref.png` is the v2 look from Short 15). Veo copies whatever its start
frame shows, so the start frame decides whether a character is on model.

1. **Start frames come from the ref, never from an older Short's still or clip.**
   Make each new still with `gemini-3-pro-image`: the character's ref as image 1,
   the old still or a location plate as image 2 for the setting only, 9:16, 2K.
   Crop to 1080x1920.
2. **Paste the character bible's description into every Veo prompt** (the
   `> **NAME:**` line), plus "keep every character exactly on-model".
3. **List everyone on screen in the spec's `cast`** (e.g. `["rocco", "nugget"]`).
4. **Run `refcheck` on every new still and clip before any voice work:**
   `mix_short.py refcheck <spec> --out check.png` puts each cast member's ref beside
   frames from every shot. Off model → regenerate the still, not the voice.
5. **A tail starts from a frame of the clip it follows**, which is already on model.
6. **Changing a character's look** = a new ref in `refs/characters/`, the old one in
   `archive/refs/`, the bible updated, and the Shorts that show the old look listed
   in the bible until they're rebuilt.

## NATIVE-DIALOGUE PATH (from Short 8 v2 on) — use this

The lip-sync pass doesn't work on our cartoon faces (see *What we learned*), so
the mouth and the words have to come from the same generation. Veo animates the
mouth to speech it generates itself; the voice changer then turns that speech
into the character's voice without moving a syllable.

| # | Step | Tool | Cost |
|---|---|---|---|
| 1 | **Speaking shots:** Veo with `generate_audio: true`, the exact line in quotes, the character facing camera, timed segments for the action, and "Audio: only <character>'s voice and <quiet ambience>" + `music` in the negative prompt | `veo-3.1-fast-generate-001` | $0.60 / 4s, $1.20 / 8s |
| 2 | Check the words: transcribe the clip's audio (Veo sometimes paraphrases) | `eleven_scribe_v1` | <1¢ |
| 3 | Strip ambience: voice isolator (needs ≥4.6s; pad shorter audio with silence) | `audio_isolation` | ~2¢ |
| 4 | Re-voice as the character: voice changer with their voice id, 2 variations. Timing stays within ~0.03s of Veo's | `eleven_multilingual_sts_v2` | ~2¢ |
| 4c | **Prefer the user's own recorded take when one exists** (Short 2 v3, approved over the voice-changed version). Split it at its natural pauses into phrases and fit each to Veo's mouth span: `at` = the span's onset minus the cut's lead-in, `tempo` = take phrase length / span length, kept within 0.85–1.15. Fit the shared sign-off the same way (pre-rendered with `atempo`). Transcribe the voice-only track (`lipsync-track --full`) to confirm no word was clipped | `mix_short.py` | free |
| 5 | **Voice-over shots** (character off screen): keep recording with Eleven v3 + tags, no lip sync needed | `eleven_v3` | ~1¢ / line |
| 4b | **Listen to / transcribe the re-voiced audio too.** The voice changer can garble a word (Short 12: "anything" → "anythang"). Fix a garbled line by fitting a v3 recording of it to Veo's speaking span (`atempo` to the span's length, placed at its onset); for the sign-off, use the shared `audio/signoffs/` file the same way | — | free |
| 6 | The sign-off is spoken in the last speaking shot the same way, so it matches the mouth; save it as `shortNN_vo_<character>_signoff.mp3` | — | — |
| 7 | Spec: `take` = the re-voiced audio, lines at their real positions, `shots` = the speaking clips + reused cutaways; `check`, `seams`, `mix` | `mix_short.py` | free |

Trade-off: Veo chooses the delivery, so v3 tags don't apply to speaking shots;
direct the read in the prompt ("says brightly and confidently"). No paid
lip-sync pass. Typical Short: ~$1.30–$2.

---

## FAST PATH (Shorts 3–8, superseded)

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
- **The voice changer garbles short phrases** (Shorts 12–13). "Anything" came out
  as "anythang", and a 1s "…And Nugget." came out as "And magic" on both takes.
  Longer passages convert cleanly. Prefer the line as Veo spoke it inside a longer
  stretch (it's already on the mouth), and transcribe every re-voiced file.
- **Check every reused recording's voice, not just its file name.**
  `short13_vo_clover_tag.mp3` was Nugget's voice, like Short 5's sign-off.
  Short 5's `short05_vo_nugget_01/02` were Sprocket too (renamed `_SPROCKET_VOICE`).
- **Keep the action behind the speaker, not between lines** (Short 11). Prompting
  "a tractor rolls in" made Rocco stop and wait for it. Write the lines on a
  continuous timeline and put the event in the background while he talks.
- **Split a take only at word boundaries the transcript confirms** (Short 11).
  Splitting "trac-tor" at a dip in loudness read back as "the track"; Veo's long
  pauses inside a phrase are better matched with whole words ("It's the" /
  "tractor!").
- **Keep the smallest character out of the bottom 30% in group shots** (Short 1).
  Nugget at Sprocket's feet sat under YouTube's title and buttons and read as
  missing. Perch him on a shoulder or head instead. To move one character, edit
  the on-model still (it as image 1 + his ref) rather than re-rendering: a fresh
  five-reference render drifted Rocco off model.
- **Pull a shot's dialogue through to the end of the clip** (Short 1). Cutting
  the extract at Veo's last measured word clipped the tail of "…anything!".
  Trim silence afterwards, never before re-voicing.
- **Never start a tail from a blink** (Short 3). The main clip's last frame had
  Clover's eyes shut, so Veo invented her eyes and gave her blue, then brown
  irises (two fast tries and one standard try). Grid the last second, pick a
  frame with the eyes open, cut the main clip there and start the tail from it.
- **Props come from somewhere** (Short 3). Anything the action needs (a soil
  patch, a seed packet) is either in the start frame or pulled from a pocket on
  camera; otherwise Veo pops it in from nowhere.
- **Check a new node's settings before running it** (Short 5 v2). New image and
  Veo nodes default to 16:9 (images also to 1K, Veo to 720p) whatever the prompt
  says, and a 16:9 still cost a wasted pair of renders. Create with
  `estimate_only`, read the node, set `aspect_ratio: 9:16` and `2K` / `1080p`, then run.
- **Two speakers in one Veo clip: check who says each line** (Short 5 v2). With
  "SPROCKET says… / NUGGET says…" Veo gave "Wrench, please" to Nugget's beak and
  added a "Ha!" and a second "Wrench" for Sprocket; the full transcript still
  read almost right. Tag every line by species ("THE PIG says", "THE CHICK
  says"), say whose mouth stays closed, and transcribe each speaker's span on
  its own before re-voicing. A two-shot tail can also invent a second prop in
  the free hoof: say "only ONE carrot… his other hoof stays empty".
- **Grid both faces through every line, not just the speaker's** (Short 5 v2). Veo
  kept Nugget's audio running to 2.7s but only moved his beak to 1.1s; Sprocket's
  mouth moved over the rest. The fix was an insert shot generated between the
  clip's own frames (start 1.1s, end 2.8s), used only until the other character
  starts talking, then a 0.2s dissolve back. `mix` needed `settb` for a dissolve
  after a hard cut (fixed in `NORM`).
- **End an insert on a frame where nobody is talking, and cut where Veo actually
  lands on it** (Short 5 v2). An end frame with Sprocket's mouth open made Veo
  have him talk through the insert, and the dissolve needed to skip that ghosted.
  With a mouth-closed end frame, Veo reached it at 3.67s of 4s; a PSNR search
  (`ffmpeg -lavfi psnr`) found the matching main-clip frame (3.72s) for a hard cut.
- **Tails with a free hoof: give it a job.** Twice Veo filled Sprocket's empty
  hoof (a second carrot, then a wrench); an explicit empty-hoofed thumbs-up held.
