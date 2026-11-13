# Fix-It Farm — REBUILD WORKFLOW

> **Tool:** `tools/mix_short.py` · **Spec:** `docs/spec-format.md`
> **Worked examples:** Short 6 (`short06_spec.json`), Short 7 (`short07_spec.json`), Short 5 for two speakers

One Short at a time. All `mix_short.py` steps are local and free. **Start with
*THE PLAYBOOK* below**; the older paths further down are kept for reference.

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

## THE PLAYBOOK (Shorts 4–7 rebuilds) — use this

Veo's standard model speaks the lines on camera, the voice changer turns that
speech into the character's voice without moving a syllable, and a 4s tail clip
gives the sign-off a moving mouth. The sign-off's audio is always the shared
recording in `audio/signoffs/`, never a voice-changed tail. Every step below
comes from a fix in *What we learned*.

### CREDIT RULES (audit 2026-11-12 — read before any paid step)

October–November used about a month of ElevenLabs credits (~$76) on four
Shorts plus the reference stills. Where it went: **reference stills ~$50
(two-thirds)** — 128 image options bought to keep 26 — and Shorts 18–20 plus the
shelved Rattly Tractor ~$26. Rules that would have halved it:

| # | Rule | Saves |
|---|---|---|
| C1 | **Never let an image node run 4 options when you need 1–2.** `run_flow_nodes` always makes 4. For stills and any reference work use `creative_generate_in_flow` with `generations_count: 2` (1 for a small, safe change). The refs were run as 4 × 26 nodes. | ~50% of every image step |
| C2 | **Tails without audio: `generate_audio: false`.** Priced 2026-11-12: 4s standard = **$0.80** silent vs $1.60 with audio. The sign-off audio is always the shared recording, so the tail's own audio is only used to find the mouth onset — read that off a 6–8 fps face grid instead (free). | $0.80 / Short |
| C3 | **Price the main clip on `veo-3.1-lite-generate-001` first.** 8s 1080p with audio = **$0.64** vs $3.20 standard (resolution doesn't change the price; 720p = 1080p). Lite is untested on our cartoons: try it on the next Short and run the usual checks (eyes, wings, props, who speaks). If it holds, it's the default; if not, record why here and stay on standard. Fast (`veo-3.1-fast`, $1.20/8s) already failed on eyes, wings and mouths. | up to $2.56 / Short |
| C4 | **Skip the still** whenever the opening fits a scene ref as-is (step 3). | $1.61–$2.01 |
| C5 | **Duplicate check before scripting** (step 0). | a whole Short |
| C6 | **Estimate every run and tell the user the exact cost first**; never re-run a video to "see if it's better" — fix by cutting, re-timing or splicing audio (pennies). | — |
| C7 | **One generation per audio step** (steps 11–12); transcribe only the voice-changed main and, once, the final mix. | pennies, but adds up |

**Target per Short:** standard main $3.20 + silent tail $0.80 + audio ~$0.10 =
**~$4.10** with no still; **~$1.55** if lite passes. Old typical was ~$6.50.

**Story**
0. **Run the duplicate check in `docs/shorts-catalog.md` before scripting —
   every new Short, no exceptions.** Same lead + same problem, fix, lesson or
   hero prop (two or more) = a repeat; also skip anything on the *Retired* list.
   In the plan shown to the user, name the closest existing Short and why this
   one is different. The shelved "Rattly Tractor" repeated Short 14 (Sprocket,
   tractor, loose bolt) and wasted ~$4.90 because this check didn't exist.

**Setup**
1. Fast-forward the branch to `main` (start fresh once a PR has merged) and open
   a draft PR for the Short.
2. Move the old version to `archive/shorts/shortNN/v1_<problem>/`; keep
   `shortNN_final.mp4` in place until the new one is approved.

**Start still**
3. **Start from the character's scene reference** (`refs/scenes/<character>_<set>.png`,
   see *Scene references* in `docs/location-bible.md`) when one fits the story:
   - Neutral standing start, no props in hand → use the scene ref itself as the
     Veo start frame and skip the still (saves ~$1.61).
   - Otherwise `gemini-3-pro-image` **via `creative_generate_in_flow` with
     `generations_count: 2`** (rule C1; `run_flow_nodes` would make 4), 9:16 / 2K
     set on the node: image 1 = the
     scene ref, image 2 = a pose ref from `refs/characters/poses/` (wave, point,
     thinking, proud), image 3 = the character's ref. "Keep the set, framing and
     size of image 1; the pose of image 2; on-model to image 3; add `<props>`."
     The set and framing stay fixed, so only the props and pose need checking.
   No scene ref for that character or set yet → the old way: the character's ref
   from `refs/characters/` as image 1 (never an old still), a location plate as
   image 2 for the setting only. Hero Nugget gets his cream chest patch.
4. Put every prop the story needs in the frame from the start, placed where the
   action will use it. Nothing may appear later.
   **Keep faces, props and the action out of the bottom 30% of the frame** —
   YouTube's title, handle and buttons cover it (`docs/intro-shorts-pack.md`
   rule 3; Short 1's Nugget "went missing" there). The scene refs leave open
   ground in front of the character, and that ground *is* the bottom 30%: put
   story props at chest height or beside the character (on a bench, crate,
   fence rail, the tractor), never on the ground in front of them.
   **Sprocket never uses a tool from his belt.** The red screwdriver, small
   silver tool and blue-handled tool are costume (`docs/prop-rules.md`), and Veo
   refills the pouch the moment he takes one out, so the tool appears twice
   (the shelved "Rattly Tractor": a red screwdriver in his hoof *and* in the pouch). The tool he
   uses is a separate prop: the silver wrench (never also in the belt), or
   something that isn't a belt tool (Short 4's gear from the pouch). It sits
   in the scene or in his hoof from frame one. In the main prompt say "the
   tools in his belt stay in his belt the whole time; he never takes one out."
5. The run returns 2 options (C1). **Check every one before picking** — fixing a still
   afterwards costs an edit batch (Short 18: $1.51 to remove a second wrench when
   a clean option was already in the batch):
   - **One of each prop.** Look for a second copy in a belt, pouch, pocket or the
     background.
   - **Counted props match the line** ("one, two, three carrots" = exactly three).
   - **The right character variant for the role**: hero Nugget (cream chest patch,
     leads) vs sidekick Nugget; Sprocket without goggles; and so on.
   - Closest to the ref.
   Pick a clean one. If none is clean, re-run the still rather than editing: the
   edit tool returns 16:9 at 1K whatever the input, so an edit needs the node set
   to 9:16 / 2K and run again (2 more). Commit and push the pick, then attach it
   to the flow by its `raw.githubusercontent.com/<owner>/<repo>/<sha>/…` URL
   (asset uploads are blocked).

**Main clip** — `veo-3.1-generate-001`, 8s, ~$3.20 (or lite, $0.64, once it passes — rule C3)
6. Prompt:
   - **Hook in the first 0.8s** (`docs/intro-shorts-pack.md` rule 1): the
     character is already moving or speaking by 0.4s; no slow open.
   - **Sprocket:** "the tools in his belt stay in his belt the whole time"
     (step 4), and the tool he uses named as the only one of its kind.
   - The bible's description line and "keep exactly on-model".
   - "The camera is LOCKED OFF… never pushes in"; crates/props "stay fully in frame".
   - Timed segments, each line in quotes, in plain lowercase (all caps gets spelled
     out) plus "He speaks in ordinary words, never spelling anything out".
   - **End the last line by ~7s, then a mouth-closed, eyes-open hold to 8s** facing
     camera. The tail starts from a frame in that hold, so there must be one after
     the last word (Short 18's "All fixed!" ran to 7.8s and the clip ended on a
     blink, so the tail started from an earlier frame and the cut jumped back).
   - **Only ONE line before the silent action beat.** Veo pushes a second
     pre-action line past the action (Shorts 17, 19, 20: "One more big pull" came
     after the carrot was out). Script: one line, the silent action, then one or
     two lines reacting to it.
   - Wings/hooves "SOLID, OPAQUE… never see-through, even when he moves them";
     give any free hoof a job; "only ONE <prop>… no new objects appear".
   - Two speakers: tag lines by species ("THE PIG says") and say whose mouth stays shut.
   - "Audio: only <character>'s voice and <quiet ambience>. No music."
   - Negative: see-through wings, camera push-in, spelling out letters, objects
     appearing, second <prop>, music, cuts, text.
7. New nodes default to 16:9 / 720p (images 1K). Set 9:16 and 1080p, read the
   node back, then run. The standard model is worth it: the fast one drifted eye
   colours, smeared wings and gave lines to the wrong mouth.
8. Check: a 4fps frame grid (staging, props, camera), full-size crops of anything
   that could smear, and a transcript of the clip's audio. Two speakers: grid both
   faces through every line.

**Tail** — same model, **4s**, $1.60 (picture only)
9. Grid the main clip's last second. Cut on a frame **in the hold after the last
   line**: eyes open, mouth closed, props held the way they should stay, before
   Veo's late camera push-in (usually the last ~0.7s). Never on a blink. Save it
   as `shortNN_tailstart.png`; **the main clip ends at this exact frame** (main
   `use` = its time), so there's no jump back at the cut.
10. **Size the sign-off's SPEAKING window to the shared recording's real length**
    (trim its silence and measure it): Rocco 2.09s, Nugget ~2.0s, Sprocket 1.18s,
    Clover 1.10s. Mouth closed 0–0.3s, SPEAKING 0.3s to 0.3s + that length,
    mouth closed after; only the sign-off in quotes; face to camera, no walking.
    This is what made the Short 10, 2 and 19 tails sync with no lip-sync pass
    (Short 19: a 2.1s window for Rocco's 2.09s line gave a 2.08s mouth).
    **But Veo won't mouth "we can fix anything!" in under ~1.7s**, whatever the
    window: Short 18 (2s window, Sprocket) gave 1.78s and Short 20 (1.1s window,
    Clover) gave 1.72s. So Sprocket's and Clover's short recordings never fill the
    mouth: slow them at most 15% (`atempo` 0.87), put the first word on the mouth
    onset, and accept ~0.4s of mouth after the audio — or re-record those two
    shared sign-offs at ~1.8s once. **Run the tail silent (`generate_audio:
    false`, $0.80 — rule C2)** and read the mouth span off a 6–8 fps face grid
    of the tail (first and last frame with the mouth open). Grid it and cut before the push-in, walk-off, or any extra
    unscripted word ("Huh?", "Ha.") Veo adds after the line.

**Voice** — pennies
11. **Main clip only.** Extract its audio, commit and attach it, then
    `audio_isolation` → `eleven_multilingual_sts_v2` with the character's voice id.
    `run_flow_nodes` on a node made by `creative_add_flow_node` makes 4
    variations and you use 1, so (confirmed on Short 19):
    - **Isolation:** `creative_generate_in_flow`, `connect_from` the audio node,
      **`generations_count: 1`** → 1 generation.
    - **Voice changer:** `creative_generate_in_flow` with `generations_count: 1`
      (its `voice_id` doesn't attach, so it fails free with "Select a voice"),
      then `creative_update_node` with the voice id on that same node, then
      `run_flow_nodes` it → 1 generation, because the node keeps its count of 1.
    Never voice-change raw audio (ambience makes it invent words); isolation
    needs ≥4.6s of audio, so pad shorter audio with silence.
12. Transcribe the converted main once. Fix a bad word by splicing it from an
    `eleven_multilingual_v2` read in the same voice (word cut from the loudness
    envelope, `atempo` 0.75–0.85 to fill the mouth span, no gain boost). Covers
    stretched ("beeolts"), shouted ("aah!nything") and garbled words. Don't try
    to turn a shout down; replace the word.
13. `silencedetect=n=-38dB:d=0.2` on the converted main gives each line's span.

**Assemble**
14. Take = the main clip's converted voice. **Sign-off = the shared
    `audio/signoffs/signoff_<character>.mp3`**, silence trimmed, at natural speed
    (or `atempo` 0.9–1.1 at most), saved as `shortNN_vo_<character>_signoff.mp3`.
    Never voice-change the tail: on short clips the voice changer garbles words
    ("anythang", "Let him fix for me the lineman") and makes the first word
    halting. Check the shared file is in the right character's voice first
    (Short 5's `signoff_nugget.mp3` was once Sprocket). No transcript needed.
15. Spec: `lines` with `take` = [span start, end] and `at` = span start (plays each
    line where it was spoken, on the mouth); `signoff.at` = cut point + the tail's
    mouth onset (from the tail's face grid); `shots` (main
    `use` = cut point, tail `use` = ~0.5s past the sign-off), `cast`, beats. Then
    `check`, `seams`, `refcheck`, `mix`.
16. Commit, attach the mix's audio, transcribe it, and compare word for word.

**Approval**
17. Send `shortNN_v2_test.mp4`. Fix what the user flags (usually one word or one
    prop) and re-send.
18. On approval: test → `shortNN_final.mp4`, delete the test files, add the
    lessons below, update the PR description and mark it ready.

**Typical Short (from 2026-11-12, see *Credit rules*):** ~$4.10 — no still,
standard main $3.20, silent 4s tail $0.80, voice and transcripts ~$0.10; add
~$1.00 for a still at 2 options. Before: ~$6.50 (4 stills $1.60, tail with
audio $1.60). Short 18 cost ~$8.10, of which $1.51 was a still edit and
$0.13 unused audio variations. Don't pay for a lip-sync pass: it usually leaves
our cartoon faces unchanged (see *What we learned*).

Still valid from the older paths: prefer the user's own recorded take when one
exists (row 4c below), and record voice-over shots (character off screen) with
Eleven v3 + tags.

---

## NATIVE-DIALOGUE PATH (from Short 8 v2, fast model; superseded by *THE PLAYBOOK*)

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
- **When the fast model keeps giving a line to the wrong mouth, switch to
  `veo-3.1-generate-001`** (Short 5 v2 sign-off). Three fast tails in a row had
  Sprocket mouthing Nugget's "We can fix anything!" (with audio, re-sequenced,
  and silent); the first standard-model try kept the pig's mouth shut. A
  gesture such as a thumbs-up also draws Veo to animate that character's mouth,
  so cut before it or give the gesture after the line.
- **Start a tail from a frame where the prop is held the way you want it kept,
  and say so** (Short 6 v2). Tail v2 started as Sprocket swung the wrench to the
  floor; Veo dropped it and the floor wrench smeared under the sign-off. Cutting
  0.4s earlier (wrench upright) and prompting "holds it UPRIGHT in his right hoof
  for the WHOLE clip… never drops it… the floor stays empty" held it.
- **Fix one garbled word by splicing, not regenerating** (Short 6 v2). Veo
  stretched "BOLTS" to "beeolts". Keeping its "It tightens" and splicing "bolts"
  from an `eleven_multilingual_v2` read in the same voice (word cut from the
  envelope, `atempo` 0.78 to fill the mouth span) cost $0.003 and transcribed
  clean.
- **Short 6 eyes: the fast model gave Sprocket brown, then blue irises** in three
  tries; the standard model kept them black (now stated in the character bible).
- **Never write a short word in ALL CAPS in a Veo line** (Short 7 v2). Veo read
  "BIG" and "DID" as letters ("B-I-G bolts", "I D-I-D it"). Plain lowercase plus
  "He speaks in ordinary words, never spelling anything out" fixed it.
- **Nugget's wings: describe them as solid, opaque fluff "even when he moves
  them"** (Short 7 v2). With that in the prompt and "transparent / see-through /
  motion-blurred wings" in the negative, the standard model kept them solid
  through a hop with wings out and a wing wave; v1 (fast model) smeared them
  see-through.
- **Veo creeps the camera in during the last ~0.7s even when told it's locked.**
  Grid the last second and cut before it (Short 7: 7.32s main, 6.3s tail).
- **A shouted syllable can't be turned down into a normal one; replace the word**
  (Short 7 v2 sign-off). Veo's "aah!nything" peaked ~15 dB over the line; a 5 dB
  dip with a low-pass still read as a scream. Splicing "anything" from an
  `eleven_multilingual_v2` read in Nugget's voice (`atempo` 0.82 to fill the beak
  span, no gain boost) fixed it.

### Shorts 16–18 (Nov 2026)

- **A word Veo cuts the clip on starts clipped** (Short 16 tail "Look"): the
  audio starts at full volume with no consonant attack, and the voice changer
  can't restore it. Splice that word from an `eleven_multilingual_v2` read in the
  character's voice. Better: start every speaking window after a short
  mouth-closed beat.
- **Veo can front-load an 8s clip** (Short 17): all three lines landed in the
  first 3.3s with ~0.3s gaps. It was still usable once the gag was reframed
  around the delivery (an over-confident "Ta-da!" before the flop), so read the
  clip before re-rolling.
- **Never voice-change a short tail** (Short 17): the 4s tail's raw audio came
  back as "Let him fix for me the lineman". Padding it past 4.6s and isolating
  first fixed the words, but the shared sign-off recording would have skipped
  all of it. That is now step 14.
- **Size the tail's SPEAKING window to the sign-off recording** (Short 18): a 2s
  window for Sprocket's 1.18s recording gave a 1.78s drawled mouth; slowing the
  recording 20% to fit sounded sluggish. Step 10.
- **Plan an eyes-open hold after the last line** (Short 18): the main clip ended
  on a blink right after "All fixed!", so the tail started from an earlier frame
  and the cut jumped back. Step 6 and step 9.
- **Pick a clean still; don't edit a flawed one** (Short 18): a wrench in the hoof
  plus one in the belt. The edit tool returned 16:9 at 1K, the re-run at 9:16 2K
  cost another 4 variations, $1.51 in all, while a clean option was in the first
  batch. Step 5.
- **`run_flow_nodes` makes 4 variations of every image and audio node**; video
  nodes make 1. Use `creative_generate_in_flow` / `creative_edit_image` with
  `generations_count` where you only need one.
- **Short 18 (8s main + 4s tail) came back with well-spaced lines** (0.48 / 2.52 /
  6.74s and a ~3s silent fix beat) when each segment had one line and the silent
  beat was the longest one. Plan beats that way.
- **Short 19 confirmed the tail rules** (~$6.47, no rework). A 0.3–2.4s SPEAKING
  window for Rocco's 2.09s sign-off gave a 2.08s mouth, so the shared recording
  played at natural speed. Cutting the main at 7.40s on an eyes-open frame and
  starting the tail from that same frame made the cut invisible. Veo added an
  unscripted "Huh?" after the sign-off with the beak moving; set the tail `use`
  just before it.
- **Veo may still reorder lines in the main clip** (Short 19): it said "Ah… mm"
  while pointing and moved the pointing line to after the action. Read the
  transcript against the beats before accepting; a reordered clip can still play.
- **A misplaced line can be replaced instead of re-rolling** (Short 20, a few
  cents): read a line that fits the moment in the character's voice with
  `eleven_v3` + an `[excited]` tag (2 takes), trim it, `atempo` within 0.85–1.15
  to the mouth span, mute the voice-changed original there and mix the new read
  in at the span (the take becomes a composite). Transcribe the composite once.
- **Short 16's settled-ear still keeps Clover's ears stable** (Short 20): pass
  `shorts/short16_droopy_sunflower/short16_still_v2.png` as image 2 "for her ear
  length only" and her ears held all 8s. Use `clover_noprop_ref.png` when a carrot
  is the story prop, so her pocket carrot isn't a second one.
- **Veo can drop a held prop in the last ~0.4s** (Short 20: the carrot vanished
  at 7.66s). Grid the end and cut the main before it; the tail prompt should say
  the prop "never disappears".
