# Fix-It Farm — VO Re-take Guide

> **Channel:** DoodlePop Kids · **Show:** Fix-It Farm
> **Goes in the repo as:** `docs/vo-retake-guide.md`
> **Timing anchors and the reasoning behind each break:** `docs/vo-retake-plan.md`

This guide covers recording the 14 single-take voice files for Shorts 2–14 in
ElevenLabs, saving them to one folder, and having Claude Code open a pull
request that puts each one in the right Short folder.

---

## PART 1 — RECORDING IN ELEVENLABS

### Before you start

| Setting | Value |
|---|---|
| Tool | Text to Speech |
| Model | **Eleven Multilingual v2.** Eleven v3 doesn't support `<break>` tags, so don't use it for these. |
| Voice | The custom voice named for the character: `Rocco`, `Clover`, `Sprocket` or `Nugget` |
| Stability / Similarity / Style | **The same values you used for the sign-off files.** Write them into the Voice ID table in `docs/audio-bible.md` if they're not there yet. |
| Speed | **1.0** for every take **except Short 7, which uses 1.10** |
| Output | MP3, 44.1 kHz (the default is fine) |

### How to record each one

1. Pick the voice.
2. Paste the text block exactly as written, break tags included. Don't add
   quotation marks or the sign-off.
3. Generate, then listen once. Check that:
   - every line is there, in order, with nothing added;
   - the pauses are audible gaps rather than rushed through;
   - the tone matches the delivery note.
4. If a read is off, regenerate. Keep only the take you like.
5. Download it and **rename it to the exact filename shown**.
6. Save it to one folder on your computer, e.g. `~/Downloads/vo_takes/`.

The sign-off ("We can fix anything!") is **not** part of any take. It already
exists as `audio/signoffs/signoff_<character>.mp3` and gets added at the mix.

---

## THE 14 TAKES

### 1 · `short02_vo_rocco_take.mp3` — Voice: Rocco
```
I'm Rocco. I run this farm. <break time="1.0s" /> And I have a plan for everything. <break time="1.1s" /> …EVERY. <break time="0.3s" /> THING.
```
Chest out, proud. The second "everything" is **the** punchline: slow, two big stressed halves — EVERY… THING — savoring it, a grin you can hear. Bigger than the first, not smaller.
If the split sounds robotic, regenerate with this fallback text for the last line: `…EVERYTHING!` and pick the read that leans on it hardest.

### 2 · `short03_vo_clover_take.mp3` — Voice: Clover
```
Hi! I'm Clover. I grow things. <break time="1.0s" /> A little water, a little sunshine… <break time="1.0s" /> …and look what happens!
```
Soft and bright, sing-songy in the middle, a delighted lift on the last line.

### 3 · `short04_vo_sprocket_take.mp3` — Voice: Sprocket
```
Sprocket here. If it's broken, I fix it. <break time="1.0s" /> This old tractor just needed one little part. <break time="1.7s" /> Ha! Told you.
```
Busy, casual, like it was nothing. Grinning on "Ha! Told you."

### 4 · `short05_vo_nugget_take.mp3` — Voice: Nugget
```
I'm Nugget! I help with EVERYTHING! <break time="1.9s" /> Wrench!
```
Tiny, breathless, all-caps energy. "Wrench!" is triumphant.

### 5 · `short05_vo_sprocket_take.mp3` — Voice: Sprocket
```
Wrench, please. <break time="2.4s" /> …Close.
```
Flat and not looking for the first line. "…Close." is dry and fond. He's **never** annoyed.

### 6 · `short06_vo_sprocket_take.mp3` — Voice: Sprocket
```
What do you think this does? <break time="1.0s" /> A back scratcher? Nope! <break time="1.0s" /> It tightens bolts! Always ask a grown-up first.
```
Playful quiz-show teasing, then warm and clear on the safety line.

### 7 · `short07_vo_nugget_take.mp3` — Voice: Nugget — **Speed 1.10**
```
Sorting time! Big bolts here… <break time="1.0s" /> …and little bolts here! <break time="1.0s" /> Silver ones, gold ones — I did it! <break time="1.0s" /> And THIS goes right here.
```
Bustling and important, sing-song on "little", total confidence on the last line.

### 8 · `short08_vo_clover_take.mp3` — Voice: Clover
```
Seeds need three things to grow. <break time="1.0s" /> Soil… water… and sunshine! <break time="1.0s" /> Now we watch them grow!
```
A gentle teacher. The "…" in line 2 are small counting beats, not long stops.

### 9 · `short09_vo_rocco_take.mp3` — Voice: Rocco
```
Three jobs today! <break time="1.0s" /> First — water the garden. <break time="1.0s" /> Then — fix the tractor. <break time="1.0s" /> Last — tidy the barn!
```
A foreman reading the day's list. Each line is its own little announcement.

### 10 · `short10_vo_sprocket_take.mp3` — Voice: Sprocket
```
Wrench. Hammer. Screwdriver. Carrot. <break time="1.0s" /> Which one doesn't belong? <break time="2.2s" /> Thanks, Clover!
```
Counting off items, with a beat of surprise on "Carrot." He asks the question to the viewer. "Thanks, Clover!" is cheerful.

### 11 · `short11_vo_rocco_take.mp3` — Voice: Rocco
```
Listen! What's that sound? <break time="1.7s" /> It's the tractor!
```
Hushed and curious, leaning in, then a big happy reveal.

### 12 · `short12_vo_nugget_take.mp3` — Voice: Nugget
```
One… two… three carrots! <break time="1.0s" /> And… four! <break time="1.2s" /> …Oh! One, two, three!
```
Careful counting. "four" is proud. "…Oh!" is a happy realisation, not embarrassment.

### 13 · `short13_vo_clover_take.mp3` — Voice: Clover
```
Red apples. Yellow sunflowers. <break time="1.0s" /> Orange carrots. Green lettuce!
```
Two lines only. **"…And Nugget." is not re-recorded**; the original ending stays.

### 14 · `short14_vo_sprocket_take.mp3` — Voice: Sprocket
```
Ooh! It's broken. <break time="1.2s" /> Wait. First, we look! <break time="2.1s" /> Aha! A loose bolt.
```
Eager, then catching himself and becoming patient, then a satisfied find.

---

### Checklist — your folder should hold exactly these 14 files

```
short02_vo_rocco_take.mp3
short03_vo_clover_take.mp3
short04_vo_sprocket_take.mp3
short05_vo_nugget_take.mp3
short05_vo_sprocket_take.mp3
short06_vo_sprocket_take.mp3
short07_vo_nugget_take.mp3
short08_vo_clover_take.mp3
short09_vo_rocco_take.mp3
short10_vo_sprocket_take.mp3
short11_vo_rocco_take.mp3
short12_vo_nugget_take.mp3
short13_vo_clover_take.mp3
short14_vo_sprocket_take.mp3
```

---

## PART 2 — PULL REQUEST WITH CLAUDE CODE

Open Claude Code in your local clone of `doodlepop`, with both guide files
(`vo-retake-guide.md` and `vo-retake-plan.md`) in the same folder as the takes.
Then paste the prompt below, changing the folder path if yours is different.

### Prompt to paste

````
Read docs/vo-retake-guide.md if it exists, otherwise read
~/Downloads/vo_takes/vo-retake-guide.md. Then follow its
"INSTRUCTIONS FOR CLAUDE CODE" section exactly, using
~/Downloads/vo_takes/ as the source folder. Stop and tell me before
doing anything the instructions don't cover.
````

---

## INSTRUCTIONS FOR CLAUDE CODE

You're adding 14 newly recorded single-take voice files to this repo and
opening one pull request. Work only inside this repo and the source folder
the user gave you. Don't delete any existing file.

### 1. Prepare

- `git checkout main && git pull`, then create the branch `vo/single-take-retakes`.
- Confirm `ffmpeg` and `ffprobe` are installed. If they're missing, tell the user
  and stop; don't install system packages without asking.

### 2. Check the source folder against this manifest

| File | Destination folder | Lines expected |
|---|---|---|
| `short02_vo_rocco_take.mp3` | `shorts/short02_rocco_intro/` | 3 |
| `short03_vo_clover_take.mp3` | `shorts/short03_clover_intro/` | 3 |
| `short04_vo_sprocket_take.mp3` | `shorts/short04_sprocket_intro/` | 3 |
| `short05_vo_nugget_take.mp3` | `shorts/short05_nugget_intro/` | 2 |
| `short05_vo_sprocket_take.mp3` | `shorts/short05_nugget_intro/` | 2 |
| `short06_vo_sprocket_take.mp3` | `shorts/short06_mystery_tool/` | 3 |
| `short07_vo_nugget_take.mp3` | `shorts/short07_nugget_sorts/` | 4 |
| `short08_vo_clover_take.mp3` | `shorts/short08_grow_test/` | 3 |
| `short09_vo_rocco_take.mp3` | `shorts/short09_morning_checklist/` | 4 |
| `short10_vo_sprocket_take.mp3` | `shorts/short10_doesnt_belong/` | 3 |
| `short11_vo_rocco_take.mp3` | `shorts/short11_what_sound/` | 2 |
| `short12_vo_nugget_take.mp3` | `shorts/short12_nugget_counts/` | 3 |
| `short13_vo_clover_take.mp3` | `shorts/short13_color_garden/` | 2 |
| `short14_vo_sprocket_take.mp3` | `shorts/short14_before_you_fix_it/` | 3 |

- Match names case-insensitively. If a file is close but not exact (e.g.
  `short2_rocco_take.mp3`, a ` (1)` suffix, `.MP3`), list the proposed rename
  and ask before applying it.
- If any file is missing, report which ones and ask whether to continue with
  the rest.
- Ignore other files in the source folder, apart from the two guide docs.

### 3. Validate each file (report only — never edit the audio)

For each take:

- `ffprobe` must read it as audio, with a duration between 2 and 15 seconds.
- Count the spoken lines by counting silences of at least 0.75s between speech:
  ```
  ffmpeg -hide_banner -i FILE -af silencedetect=noise=-40dB:d=0.75 -f null - 2>&1 | grep -c silence_start
  ```
  Don't count a silence that starts at 0.0s or runs to the end of the file.
  Lines found = internal silences + 1.
- Print one table with the columns file · duration · lines found · lines
  expected · OK/CHECK.
- A **CHECK** row is a warning, not a failure. The likely causes are a
  rushed break (too few lines) or a pause inside a line (too many). Put the
  table in the PR description and continue.

### 4. Copy the files in

- Copy (don't move) each take into its destination folder under the exact
  manifest name.
- **Leave the existing per-line `shortNN_vo_*_NN.mp3` files where they are.**
  They're still needed until each Short is rebuilt and approved. They get
  archived in a later PR, not this one.

### 5. Add the docs

- Copy `vo-retake-guide.md` → `docs/vo-retake-guide.md`
- Copy `vo-retake-plan.md` → `docs/vo-retake-plan.md`
- If either already exists in `docs/`, replace it in place.

### 6. Update README.md

In the naming-convention table, add these two rows directly after the
"Voice line" row:

```
| Voice take (whole Short, one file) | `shortNN_vo_<character>_take.mp3` | `short07_vo_nugget_take.mp3` |
| Continuation tail clip | `shortNN_clip_tail.mp4` | `short06_clip_tail.mp4` |
```

In the `docs/` block of the Layout section, add:

```
  vo-retake-guide.md        recording + PR steps for single-take VO
  vo-retake-plan.md         timing anchors for re-timing takes to picture
```

### 7. Fix Short 9's voice-file names (separate commit)

All five Short 9 voice files are Rocco speaking. They were named after the
character in each shot, which reads as if Clover, Sprocket and Nugget were
speaking. Rename them with `git mv`:

| From | To |
|---|---|
| `short09_vo_a_rocco.mp3` | `short09_vo_rocco_01.mp3` |
| `short09_vo_b_clover.mp3` | `short09_vo_rocco_02.mp3` |
| `short09_vo_c_sprocket.mp3` | `short09_vo_rocco_03.mp3` |
| `short09_vo_d_nugget.mp3` | `short09_vo_rocco_04.mp3` |
| `short09_vo_a_rocco_tag.mp3` | `short09_vo_rocco_tag.mp3` |

Add these five rows to the bottom of `docs/file-renames.md`, using the old
repo path → new path.

### 8. Commit, push, open the PR

Three commits, in this order:

1. `Add single-take VO for Shorts 2–14` (the 14 audio files)
2. `Add VO re-take guide and plan; document take naming` (docs + README)
3. `Rename Short 9 VO files to match speaker` (renames + file-renames.md)

Push the branch and open a PR to `main` titled
**"Single-take VO re-takes for Shorts 2–14"**. The description should contain:

- the validation table from step 3;
- a note that the old per-line VO files are deliberately kept until rebuilds are approved;
- a note that Short 13's original "…And Nugget." ending is intentionally not re-recorded;
- a note that Short 7 was recorded at speed 1.10.

Then give the user the PR link and the validation table. **Don't merge it.**
