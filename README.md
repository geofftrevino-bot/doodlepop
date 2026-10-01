# DoodlePop Kids — Fix-It Farm

Production repo for the **Fix-It Farm** show on the DoodlePop Kids channel:
show bibles, reference art, shared audio, and every asset for each Short.

Any file can be attached to a generation by URL:

```
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/<path>
```

## Layout

```
docs/                     show bibles and production notes
  character-bible.md        locked character descriptions (current: v3)
  location-bible.md         sets and plates
  prop-rules.md             with-prop / no-prop reference rules
  audio-bible.md            voices, theme, catchphrases (current: v2)
  asset-pipeline.md         how assets move between the repo and ElevenLabs
  intro-shorts-pack.md      the first five Shorts and the repeatable formats
  file-renames.md           old root-level filename -> new path
  vo-retake-guide.md        recording + PR steps for single-take VO
  vo-retake-plan.md         timing anchors for re-timing takes to picture
episodes/
  ep01/                     "Welcome to Fix-It Farm": script.md, shot-list.md
refs/
  characters/               approved character reference renders
  locations/                approved location plates
audio/
  theme/                    theme_full.mp3, theme_sting.mp3
  catchphrases/             catch_<character>.mp3
  signoffs/                 signoff_<character>.mp3
shorts/
  shortNN_<slug>/           everything for one Short (see below)
archive/                  superseded takes, old doc versions, exact duplicates
```

## Shorts

| # | Folder | Lead |
|---|---|---|
| 1 | `short01_farm_intro` | ensemble |
| 2 | `short02_rocco_intro` | Rocco |
| 3 | `short03_clover_intro` | Clover |
| 4 | `short04_sprocket_intro` | Sprocket |
| 5 | `short05_nugget_intro` | Nugget (+ Sprocket shots b/c) |
| 6 | `short06_mystery_tool` | Sprocket |
| 7 | `short07_nugget_sorts` | Nugget |
| 8 | `short08_grow_test` | Clover |
| 9 | `short09_morning_checklist` | ensemble (shots a–d) |
| 10 | `short10_doesnt_belong` | Sprocket |
| 11 | `short11_what_sound` | Rocco |
| 12 | `short12_nugget_counts` | Nugget |
| 13 | `short13_color_garden` | Clover |
| 14 | `short14_before_you_fix_it` | Sprocket |
| 15 | `short15_stop_look_listen` | Rocco |

## Naming convention

All lowercase, words separated by `_`, Short numbers zero-padded to two digits.
Every file in a Short's folder starts with its `shortNN_` prefix, so a file
still makes sense on its own once it's downloaded or uploaded somewhere else.

| What | Pattern | Example |
|---|---|---|
| Composite still (frame one) | `shortNN_still[_<shot>_<character>].png` | `short09_still_a_rocco.png` |
| First / last frame grab | `shortNN_firstframe.png`, `shortNN_lastframe.png` | `short08_lastframe.png` |
| Silent generated clip | `shortNN_clip[_<shot>][_vN].mp4` | `short12_clip_v3.mp4` |
| Finished Short with sound | `shortNN_final.mp4` | `short14_final.mp4` |
| Voice line | `shortNN_vo_<character>_NN.mp3` (or `_tag`) | `short07_vo_nugget_03.mp3` |
| Voice take (whole Short, one file) | `shortNN_vo_<character>_take.mp3` | `short07_vo_nugget_take.mp3` |
| Continuation tail clip | `shortNN_clip_tail.mp4` | `short06_clip_tail.mp4` |
| Sound effect | `shortNN_sfx_<name>.mp3` | `short11_sfx_tractor.mp3` |
| Character reference | `<character>[_<variant>]_ref.png` | `nugget_hero_ref.png` |

Rules of thumb:

- **Multi-shot Shorts** use a shot letter after the type: `_a_`, `_b_`, `_c_`…
- **Versions** are `_v1`, `_v2`… Don't add `_2`, `_final_final`, `(1)`, etc.
- **Retakes**: keep only the approved take in the Short's folder; move the
  replaced one to `archive/shorts/shortNN/`.
- **Docs** go in `docs/` with no `doodlepop-kids-` prefix and no version suffix.
  Replace the file in place and let git keep the history. Copy an old version
  to `archive/docs/` only if it needs to stay easy to find.
- **New Short**: create `shorts/shortNN_<slug>/` and add it to the table above.
