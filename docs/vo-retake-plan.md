# Fix-It Farm — VO RE-TAKE PLAN (Shorts 2–14 → single-take format)

> **Channel:** DoodlePop Kids · **Show:** Fix-It Farm
> **Supersedes:** the "RECORDING NOTES" section of the original Shorts VO scripts
> (one-line-per-file) and every per-short `Files:` line listing `_01…_05` VO files.
> **Governed by:** `docs/audio-bible.md`, the single-take VO delivery standard

---

## THE ONE THING THAT'S DIFFERENT FOR THESE THIRTEEN

For new Shorts the recording is the master clock and the video is written to it.
These thirteen already exist, so **the picture is the master clock**: every
mouth move and story beat is baked into the video. A new take can't add a pause
the picture doesn't have.

So each re-take works like this:

1. **Record one take** with standard breaks (≥1.0s) so every line is delivered
   relaxed and separates cleanly at a silence.
2. **Split at the silences** and seat each line on its **existing mouth anchor**
   (the "Starts at" column below — same anchors the rev2 mixes use).
3. **Where the picture's gap is shorter than the recorded break,** the mix
   closes the break down to the picture gap. Where the picture gap is longer,
   the recorded break plays whole.
4. **Sign-off is not in the take.** It's the existing reusable
   `audio/signoffs/signoff_<character>.mp3`, placed at `max(tag beat, last line end + 0.72s)`.

What this buys: one consistent performance per Short (same energy, same
intonation line to line), the new sign-off everywhere, and a clean master take
for each Short in the repo.

What it doesn't buy: wider pauses in Shorts whose pictures were cut to the old
fast reads. Ten of the thirteen have at least one picture gap under the 1.0s
standard (marked **tight** below). Getting real 1.0s+ pauses in those means
regenerating the picture to the new take — an 8s Veo clip is $0.88 per Short
(~$8.80 for all ten), only if you want it after hearing the re-takes.

---

## RECORDING SETTINGS (every take)

- Custom voice named for the character (`Rocco`, `Clover`, `Sprocket`, `Nugget`)
  — look up the ID with `creative_list_voices`, never from memory.
- Identical stability/style settings across all takes (record them in the audio
  bible's Voice ID table on the first run).
- Speed 1.0, **except Shorts 7 and 9** (see notes there).
- Paste the block exactly — break tags included, nothing outside the quotes.
- ElevenLabs tends to render a tag slightly short. That's fine here: the mix
  sets every gap to the picture anyway.
- **File name:** `shortNN_vo_<character>_take.mp3` in the Short's own folder (`shorts/shortNN_<slug>/`) (Short 5 has two).

Measured line lengths below are from the current repo VO files, trimmed of
silence. "Picture gap" = next anchor − (this anchor + line length).

---

## SHORT 2 — "This Is Rocco" · `short02_vo_rocco_take.mp3`

```
I'm Rocco. I run this farm. <break time="1.0s" /> And I have a plan for everything. <break time="1.1s" /> …EVERY. <break time="0.3s" /> THING.
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | I'm Rocco. I run this farm. | 0.27 | 1.81 | 0.69 **tight** |
| 2 | And I have a plan for everything. | 2.77 | 1.80 | 1.06 |
| 3 | …EVERY. THING. | 5.63 | ~1.5 (accentuated; was 1.00) | → sign-off |

Delivery: line 3 is the punchline. Slow and stressed, EVERY… THING, savoring it. The pause before it sets it up.
The stretched read runs about 0.5s past the beak movement baked into the picture (5.63–6.63). The sign-off shifts later to keep its 0.72s gap, so runtime goes from 9.6s to about 10.1s. If the overrun reads wrong, the beak window can be extended with a $0.44 Veo continuation.

---

## SHORT 3 — "This Is Clover" · `short03_vo_clover_take.mp3`

```
Hi! I'm Clover. I grow things. <break time="1.0s" /> A little water, a little sunshine… <break time="1.0s" /> …and look what happens!
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | Hi! I'm Clover. I grow things. | 0.30 | 1.71 | 0.34 **tight** |
| 2 | A little water, a little sunshine… | 2.35 | 1.89 | 0.46 **tight** |
| 3 | …and look what happens! | 4.70 | 1.08 | → sign-off |

Line 3 must land on the bloom. If anything moves, move the line, not the picture.

---

## SHORT 4 — "This Is Sprocket" (rebuild) · `short04_vo_sprocket_take.mp3`

```
Sprocket here. If it's broken, I fix it. <break time="1.0s" /> This old tractor just needed one little part. <break time="1.7s" /> Ha! Told you.
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | Sprocket here. If it's broken, I fix it. | 0.30 | 2.18 | 0.73 **tight** |
| 2 | This old tractor just needed one little part. | 3.21 | 2.05 | 1.69 (engine 5.30–6.95) |
| 3 | Ha! Told you. | 6.95 | 0.89 | → sign-off |

Anchors are for the rebuilt video (`short4_sprocket_rebuild_silent.mp4`). The
1.7s break is the engine window — it must stay clear of voice.

---

## SHORT 5 — "This Is Nugget" (two speakers → two takes)

`short05_vo_nugget_take.mp3`
```
I'm Nugget! I help with EVERYTHING! <break time="1.9s" /> Wrench!
```

`short05_vo_sprocket_take.mp3`
```
Wrench, please. <break time="2.4s" /> …Close.
```

| # | Speaker | Line | Starts at | Length |
|---|---|---|---|---|
| 1 | Nugget | I'm Nugget! I help with EVERYTHING! | 0.30 | 2.01 |
| 2 | Sprocket | Wrench, please. | 2.85 | 0.79 |
| 3 | Nugget | Wrench! | 4.20 | 0.52 |
| 4 | Sprocket | …Close. | 6.05 | 0.33 |

Each take's break equals the gap between that character's own lines, so both
takes drop onto the cut almost unedited. Sprocket is fond, never annoyed.
Sign-off: Nugget.

---

## SHORT 6 — "Mystery Tool" · `short06_vo_sprocket_take.mp3`

```
What do you think this does? <break time="1.0s" /> A back scratcher? Nope! <break time="1.0s" /> It tightens bolts! Always ask a grown-up first.
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | What do you think this does? | 0.40 | 1.17 | 0.73 **tight** |
| 2 | A back scratcher? Nope! | 2.30 | 1.43 | 0.57 **tight** |
| 3 | It tightens bolts! Always ask a grown-up first. | 4.30 | 2.42 | → sign-off |

---

## SHORT 7 — "Nugget Sorts the Toolbox" · `short07_vo_nugget_take.mp3`

```
Sorting time! Big bolts here… <break time="1.0s" /> …and little bolts here! <break time="1.0s" /> Silver ones, gold ones — I did it! <break time="1.0s" /> And THIS goes right here.
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | Sorting time! Big bolts here… | 0.08 | 1.78 | −0.03 **overlaps** |
| 2 | …and little bolts here! | 1.83 | 1.97 | −0.07 **overlaps** |
| 3 | Silver ones, gold ones — I did it! | 3.73 | 1.93 | 0.12 **tight** |
| 4 | And THIS goes right here. | 5.78 | 1.13 | → sign-off |

**At natural speed the lines don't fit this picture** — the rev2 mix only works
because of the 12% tempo lift. Record this take at **speed 1.10** (cleaner than
stretching afterwards). If you'd rather keep natural pace, the fix is the
picture, not the audio: regenerate to the take ($0.88), or cut line 3 to
"Gold ones!" per the Short 7 doc.

---

## SHORT 8 — "Grow Test" · `short08_vo_clover_take.mp3`

```
Seeds need three things to grow. <break time="1.0s" /> Soil… water… and sunshine! <break time="1.0s" /> Now we watch them grow!
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | Seeds need three things to grow. | 0.25 | 1.74 | 0.36 **tight** |
| 2 | Soil… water… and sunshine! | 2.35 | 2.40 | 0.25 **tight** |
| 3 | Now we watch them grow! | 5.00 | 1.13 | → sign-off |

The ellipses in line 2 are micro-beats inside the line, not breaks — keep them.

---

## SHORT 9 — "Morning Checklist" · `short09_vo_rocco_take.mp3`

```
Three jobs today! <break time="1.0s" /> First — water the garden. <break time="1.0s" /> Then — fix the tractor. <break time="1.0s" /> Last — tidy the barn!
```

| # | Line | Starts at | Cut at | Length | Picture gap after |
|---|---|---|---|---|---|
| 1 | Three jobs today! | 0.10 | 0.00 | 1.41 | −0.03 **overlaps** |
| 2 | First — water the garden. | 1.48 | 1.42 | 1.86 | −0.07 **overlaps** |
| 3 | Then — fix the tractor. | 3.27 | 3.21 | 1.56 | −0.06 **overlaps** |
| 4 | Last — tidy the barn! | 4.77 | 4.71 | 1.73 | → sign-off |

Same problem as Short 7, but this one is VO over four cuts, so the **cuts can
move for free** if the source shots have spare frames. Recommended: record at
natural speed, then re-cut the four shots to the take (each shot starts 0.06s
before its line). Runtime grows to roughly 10.5s with Rocco's sign-off — inside
what a Short can be, a bit past our 8–10s habit. Fallback: speed 1.10 and the
current cuts.

---

## SHORT 10 — "Which One Doesn't Belong?" · `short10_vo_sprocket_take.mp3`

```
Wrench. Hammer. Screwdriver. Carrot. <break time="1.0s" /> Which one doesn't belong? <break time="2.2s" /> Thanks, Clover!
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | Wrench. Hammer. Screwdriver. Carrot. | 0.25 | 2.05 | 0.30 **tight** |
| 2 | Which one doesn't belong? | 2.60 | 1.00 | 2.15 (thinking pause, Clover's look) |
| 3 | Thanks, Clover! | 5.75 | 0.66 | → sign-off |

The 2.2s break is the viewer's answer window. Never fill it.

---

## SHORT 11 — "What Sound Is That?" · `short11_vo_rocco_take.mp3`

```
Listen! What's that sound? <break time="1.7s" /> It's the tractor!
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | Listen! What's that sound? | 1.72 | 1.89 | 1.69 (second engine SFX at 3.50) |
| 2 | It's the tractor! | 5.30 | 1.56 | → sign-off |

Take starts at 1.72 — the opening engine SFX (0.10) plays alone first. Already
fits the picture; mix keeps the three-layer duck (voice + SFX).

---

## SHORT 12 — "Nugget Counts Everything" · `short12_vo_nugget_take.mp3`

```
One… two… three carrots! <break time="1.0s" /> And… four! <break time="1.2s" /> …Oh! One, two, three!
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | One… two… three carrots! | 0.65 | 1.58 | 0.72 **tight** |
| 2 | And… four! | 2.95 | 0.95 | 1.15 |
| 3 | …Oh! One, two, three! | 5.05 | 1.69 | → sign-off |

Counts in line 1 land on the carrot taps — the "…" spacing inside the line has
to match the taps, so check line 1 against picture before the full mix.

---

## SHORT 13 — "Clover's Colour Garden" · `short13_vo_clover_take.mp3`

```
Red apples. Yellow sunflowers. <break time="1.0s" /> Orange carrots. Green lettuce!
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | Red apples. Yellow sunflowers. | 0.40 | 2.41 | 0.34 **tight** |
| 2 | Orange carrots. Green lettuce! | 3.15 | 1.45 | 1.15 (Nugget enters) |
| 3 | …And Nugget. | 5.75 | ~0.90 | → sign-off |

**Line 3 is not re-recorded.** You asked to keep that ending exactly as
recorded, so it stays `c03_andnugget.wav`. Only lines 1–2 are in the new take.
Same voice and settings, so the join should be invisible; if it isn't, we
re-record line 3 too — your call after a listen.

---

## SHORT 14 — "Before You Fix It" · `short14_vo_sprocket_take.mp3`

```
Ooh! It's broken. <break time="1.2s" /> Wait. First, we look! <break time="2.1s" /> Aha! A loose bolt.
```

| # | Line | Starts at | Length | Picture gap after |
|---|---|---|---|---|
| 1 | Ooh! It's broken. | 0.30 | 0.80 | 1.15 |
| 2 | Wait. First, we look! | 2.25 | 0.93 | 2.12 (inspection 3.14–5.30) |
| 3 | Aha! A loose bolt. | 5.30 | 1.00 | → sign-off |

Already fits the picture. This is the model the others should have looked like.

---

## AT A GLANCE

| Short | Takes | Fits picture as-is | Needs a decision |
|---|---|---|---|
| 2 Rocco | 1 | mostly (one tight gap) | — |
| 3 Clover | 1 | tight | — |
| 4 Sprocket | 1 | mostly | — |
| 5 Nugget | 2 | ✅ | — |
| 6 Mystery Tool | 1 | tight | — |
| 7 Nugget Sorts | 1 | ❌ overlaps | speed 1.10 vs regenerate |
| 8 Grow Test | 1 | tight | — |
| 9 Checklist | 1 | ❌ overlaps | re-cut shots (free) vs speed 1.10 |
| 10 Doesn't Belong | 1 | mostly | — |
| 11 What Sound | 1 | ✅ | — |
| 12 Counts | 1 | mostly | — |
| 13 Colour Garden | 1 (lines 1–2) | tight | keep original line 3 |
| 14 Before You Fix It | 1 | ✅ | — |

**14 takes total**, all short — a few cents of ElevenLabs credit each.

---

## RUN ORDER

1. Generate all 14 takes in one session, one flow, same settings.
2. Commit takes to the repo as `shortNN_vo_<character>_take.mp3` in the Short's own folder (`shorts/shortNN_<slug>/`).
3. Split each at its silences; seat lines on the anchors above.
4. Place the reusable sign-off; mix with the standard chain (VO −16 LUFS, music
   sting −22 with sidechain duck, master −14 LUFS / −1 dBTP).
5. Splice the pending continuation tails (Shorts 2, 4–14) where runtime passes 8.0s.
6. Export as `shortNN_final.mp4` replacing the current one; git keeps the previous version.
7. Listen pass. Any Short still feeling rushed goes on the regenerate list.

Language check: all spoken lines pass `kidsafe_check.py --spoken`
("broken" in Shorts 4 and 14 is a CAUTION word, fine in context — something to
fix, not something sad).
