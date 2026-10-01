# DoodlePop Kids — AUDIO BIBLE
### Sound is the brand. Preschoolers recognize a show by its audio before they can read the title.

Picture is solved: composite-first image-to-video keeps characters on-model.
Those clips come back **silent**, so every soundtrack is built in post. That's
not a workaround — it's how the consistency problem gets solved, because
anything assembled by hand can be identical in every upload.

> **Channel:** DoodlePop Kids  ·  **Show:** Fix-It Farm
---

## ⚠️ THE CONSTRAINT THAT SHAPES EVERYTHING

`Runvid:generate_audio` accepts **only a text prompt**. No voice ID, no seed,
no voice selection. There is no way to ask for the same voice twice.

That's the same failure mode as text-to-video: fine for one clip, fatal across
a series. Nugget sounding different in every episode breaks the character more
than any visual drift would, because a four-year-old tracks voice first.

**Use it for:** scratch tracks, timing tests, previewing a line read.
**Don't use it for:** anything you publish.

---

## THE THREE LAYERS

Every DoodlePop video is exactly three stacked layers. Never more.

| Layer | Source | Consistency method |
|---|---|---|
| **1. Voice** | Locked TTS voice IDs, or real VO | Same voice ID / same actor, forever |
| **2. Music** | Licensed library + your own theme | Same theme, same key, same tempo |
| **3. SFX** | Licensed library, curated once | A fixed cue sheet — same sound, same event |

---

## LAYER 1 — VOICE

### Options, best to worst for a series

**A. Real voice actors.** Four actors, or one or two doing multiple parts. Most
expensive, most consistent, best performance. Worth it once the channel earns.

**B. A TTS platform with locked voice IDs.** ElevenLabs, PlayHT, and similar let
you pick a specific voice and reuse that exact voice ID indefinitely — some let
you clone and save a custom one. **This is the current approach** — the four
voices are locked in the table below.

**C. Runvid `generate_audio`.** Scratch only, per the constraint above.

### Character voice specs — VOICES LOCKED

| Character | Voice | Direction | Pitch | Pace |
|---|---|---|---|---|
| **ROCCO** | **Callum — Husky Trickster** | Warm, big, theatrical. A proud friendly foreman who means well. Never stern. | Low-mid, resonant | Measured, lands his lines |
| **CLOVER** | **Laura — Enthusiast** | Soft, patient, sing-songy. The calm one. Gentle but not sleepy. | Mid, light | Unhurried, even |
| **SPROCKET** | **Bill — Wise** | Bright, busy, chatty. Thinks out loud while working. | Mid-high, energetic | Quick, overlapping |
| **NUGGET** | **Bella — Professional** | Tiny, breathy, eager. Short sentences. Pure enthusiasm. | High, small, squeaky | Fast, excitable bursts |

**These four are now canon.** Record the exact voice ID string from your TTS
platform next to each name the first time you use it — display names can change
or duplicate across a library, but the ID is permanent. Never swap a voice
between episodes; a character who changes voice reads as a different character.

**Settings to lock too.** Whatever platform you use, the stability /
similarity / style sliders affect the read as much as the voice choice does.
Write down the values you settle on and reuse them for every line. Same voice
at different settings will not match.

**Rule:** any two characters in a scene must be clearly distinguishable with
eyes closed. If Sprocket and Nugget read too similarly, adjust pitch on
Sprocket — never reassign a voice.

---

## LAYER 2 — MUSIC

### The theme is the single most valuable audio asset you own

It opens every episode and appears in most Shorts. Get it right once and it
carries the whole channel.

**Lock these and never vary them:**

- **Key:** pick one (C or G major — bright, easy to sing, sits well for kids)
- **Tempo:** 120–130 BPM. Fast enough to feel happy, slow enough to follow.
- **Instrumentation:** banjo, handclaps, light percussion, ukulele, glockenspiel.
  This palette is the sonic signature. Every cue uses it.
- **Length:** a 30s full version, a 10s Shorts sting, and a 5s logo tag.

**Where to get it:** Epidemic Sound, Artlist, Soundstripe (subscription,
YouTube-safe), or commission a musician once for a custom theme. Commissioned
is strongly preferable — a library theme can appear on someone else's channel.

### The cue library

Build these once and reuse forever:

| Cue | Use | Length |
|---|---|---|
| `THEME_full` | Episode open | 30s |
| `THEME_sting` | Shorts open/close | 10s |
| `THEME_tag` | Logo button | 5s |
| `WORK_montage` | Everyone doing their jobs | 60s loop |
| `TROUBLE` | Something's gone wrong; thinner, minor-ish, still gentle | 45s loop |
| `DISCOVERY` | Nugget's hero beat; rising, magical | 20s |
| `TRIUMPH` | The fix works, the reveal | 30s |
| `WARM_outro` | Golden hour, the emotional beat | 30s |

Every cue in the same key and palette as the theme, so they can cross-fade.

---

## LAYER 3 — SFX

### The cue sheet — same event, same sound, every time

This is what makes a world feel real to a small child. Consistency here is
more important than quality.

**Character signatures**
- `rocco_crow` — his crow. Used in nearly every open. Pick ONE take.
- `clover_sparkle` — soft rising chimes when something grows
- `sprocket_fix` — a short wrench-clank into a satisfied "ta-da" ding
- `nugget_toddle` — tiny rapid footsteps (his entrance sound)
- `nugget_womp` — the soft confused "womp" when he gets it wrong

**World sounds**
- `windmill_turn`, `tractor_putt`, `barn_door`, `box_tumble`, `birdsong_bed`

**Comedy punctuation**
- `woodblock`, `kazoo_flourish`, `deflate_trumpet`, `magic_ding`, `record_scratch`

**Never use:** sharp impacts, sudden loud stings, anything startling. Preschool
audio should never make a child flinch. The box avalanche is a soft bouncy
cascade, not a crash.

---

## TECHNICAL SPECS

- **Loudness:** −14 LUFS integrated. YouTube normalizes to roughly this; master
  louder and it gets turned down, and your dynamics get squashed for nothing.
- **True peak:** −1 dBTP maximum.
- **Dynamic range:** keep it narrow. Kids watch on phone speakers and tablets at
  low volume — a whispered line will vanish.
- **Mix balance:** voice always on top. Music sits about 12–15 dB under dialogue,
  SFX about 6–10 dB under.
- **Format:** 48 kHz, stereo, AAC 320 kbps on export.

---

## ASSEMBLY WORKFLOW

1. **Generate picture** — composite still → image-to-video → silent clip
2. **Record/generate voice** — one file per line, named `ep01_s55_rocco.wav`
3. **Lay the music bed** — pick the cue from the library, don't invent a new one
4. **Drop SFX from the cue sheet** — same sound for the same event
5. **Mix** — voice on top, duck music under dialogue
6. **Master to −14 LUFS**, export

**Tools:** CapCut (free, fast, fine for Shorts), DaVinci Resolve (free, real
audio mixing via Fairlight), Premiere, or Audition for the mix.

**File naming, so nothing gets lost:**
```
ep01_s55_rocco_line.wav
ep01_music_TRIUMPH.wav
sfx_nugget_womp.wav
```

---

## SONG PRODUCTION

Episode 1 has three songs written. Lyrics exist; melodies don't.

**Recommended:** commission a musician for the theme and the two episode songs
as a package. Preschool songs are short, simple, and repetitive — this is
cheaper than it sounds, and owning the master means no licensing questions
ever.

**If generating instead:** Suno or Udio can produce them from the lyrics, but
the same consistency warning applies — the theme will sound different every
time you regenerate it. Generate once, save the file, reuse that exact file
forever. Never regenerate a locked asset.

---

## THE ONE RULE

**Generate once, save, reuse.** Every audio asset that appears more than once —
the theme, the crow, Nugget's womp — gets created a single time and stored as a
file. The moment you regenerate something instead of reusing it, consistency is
gone. That applies to voices, music, and SFX equally.
