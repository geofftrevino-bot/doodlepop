# Fix-It Farm — SHORT SPEC FORMAT

> **File:** `shorts/shortNN_<slug>/shortNN_spec.json` · **Read by:** `tools/mix_short.py`
> **Examples:** `short04_spec.json`, `short14_spec.json`

The spec is the one place a Short's timing lives. The Veo prompt, the lip-sync
track and the mix are all generated from it, so they can't disagree. Change
timing here (or with `mix_short.py retime`), never by hand in a command.

Paths resolve against the Short's folder first, then the repo root, so
`"short14_still.png"` and `"audio/theme/theme_sting.mp3"` both work.

---

## FIELDS

| Field | What it is |
|---|---|
| `title` | The Short's name |
| `character` | Who speaks (`rocco`, `clover`, `sprocket`, `nugget`) |
| `cast` | Everyone on screen, for `refcheck` (defaults to `[character]`) |
| `voice` | `name`, ElevenLabs `id`, `model`. Fast path: **`eleven_v3`**, one line per generation with audio tags, joined by `assemble-take` (v3 ignores `<break>`, which doesn't matter then). Single-take recordings with `<break>` tags must use `eleven_multilingual_v2` |
| `take` | The single VO take, e.g. `short14_vo_sprocket_take.mp3` |
| `lines[]` | One entry per spoken line, in order (below) |
| `signoff` | `file` (the reusable `audio/signoffs/signoff_<character>.mp3`) and `at`. `null` = 0.72s after the last line ends |
| `sfx[]` | `file`, `at` (seconds), `gain_db` (default −8) |
| `music` | Bed under the whole Short, ducked under the voice. Normally `audio/theme/theme_sting.mp3` |
| `clip` | The picture the mix uses. After a lip-sync pass this is the synced clip |
| `shots[]` | Instead of `clip`: cuts joined in order. Each has `clip`, optional `from` (start inside that clip), `use` (seconds), optional `xfade` (dissolve into it, seconds), and for generated shots `start_frame` + `beats` |
| `built_from_shots[]` | Kept for reference after a whole-Short lip-sync pass replaces `shots` with the synced `clip` |
| `video` | How the picture is made (below) |
| `beats[]` | What happens on screen, and when (below) |

### `lines[]`

```json
{"text": "Aha! A loose bolt.", "take": [5.51, null], "at": 4.7}
```

- `take`: start and end in the take file, in seconds. `null` end = to the end of the take.
  Get them from `mix_short.py pauses <take>`: cut ~0.05s before speech starts and
  ~0.1s into the silence after it ends.
- `speaker` (optional): who says the line, for Shorts with more than one voice.
- `tempo` (optional, e.g. `1.1`): play the line faster without changing pitch, when the picture is tight. Keep it at or under ~1.15 so the read still sounds natural.
- `at`: where the cut starts on the Short's timeline. Speech is heard a little
  later, by however much silence the cut starts with.

### `video`

| Field | What it is |
|---|---|
| `start_frame` | The approved still the clip starts on |
| `raw_clip` | The Veo output before any lip-sync pass (the lip-sync track is padded to its length) |
| `model` | Normally `veo-3.1-fast-generate-001` |
| `description` | The on-model character and prop description, copied from the character bible |
| `negative[]` | Extra negative-prompt terms. Camera moves, cuts, text and extra characters are always added |

### `beats[]`

```json
{"from": 2.7, "to": 4.6, "mouth": "closed", "action": "He leans in close and inspects the engine."}
```

- `mouth`: `open` while a line is spoken in this beat, otherwise `closed`.
  `check` fails if any line lands in a `closed` beat.
- Before generating, beats are the **plan**. After generating, update them to
  what Veo **actually** did (read off `sheet`), then `retime` the lines to fit.
- Keep to **4–6 beats of at least 0.75s**. Veo skips small beats and runs
  timing early; one clear action per beat holds best.
