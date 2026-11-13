# DoodlePop Kids — LOCATION BIBLE (LOCKED)
### Seven approved background plates · all 1672×941 (16:9) · plus 9:16 scene references for Shorts (see the end)

All seven match the character art style and each other. The rainbow windmill,
red barn with the slate roof and silo, split-rail fencing, apple trees, and
rolled hay bales recur across plates — that shared vocabulary is what will make
the world read as one place.

> **Channel:** DoodlePop Kids  ·  **Show:** Fix-It Farm
---

## ⚠️ THE GAP: THESE ARE ALL "AFTER" PLATES

Every plate shows the farm **clean, tidy, planted, and working**. Episode 1's
entire first half depends on the opposite — an overgrown garden, a barn full
of boxes, scattered tools, and a tractor that won't start.

**Four "before" variants are needed before Episode 1 can be shot:**

| Need | Base plate | What changes |
|---|---|---|
| `BARN_INT_MESSY` | BARN_INT | Towers of cardboard boxes, crooked shelves, upside-down wheelbarrow, tangled hoses, one sock on a rafter |
| `GARDEN_OVERGROWN` | GARDEN | Beds buried in waist-high weeds, empty pots, no crops visible, potting bench cluttered |
| `WORKSHOP_MESSY` | WORKSHOP | Tools scattered on the floor, pegboard half-empty, drawers open, parts everywhere |
| `TRACTOR_RUSTY` | TRACTOR_YARD | Tractor is rusty, dull, faded, one wheel flat, hood up, sitting crooked |

The approved plates then become the **reveal** at the end — which is exactly
the payoff the episode is built around. Same camera angle, before and after,
is the single most satisfying shot you can give a preschool audience.

---

## ⚠️ TRACTOR COLOR CONFLICT

The plate shows a **blue** tractor in good condition. The script (Short 4 and
Scene 6) says Sprocket repaints it **bright red**.

Pick one and make it canon:

- **Keep it blue** — matches the approved plate, no repaint beat, simpler.
  Change Short 4's prompt to drop the color change.
- **Rusty → blue** — the "before" variant is rusty and faded, and restoring it
  to this exact blue is the payoff. **This is the better option:** it preserves
  the transformation gag *and* keeps the approved plate as canon.

I'd go with rusty → blue. Nothing else needs to change.

---

## THE PLATES

### `BARN_EXT` — the establishing shot
Red barn with slate roof and attached silo, white X-braced doors, hayloft
window with straw spilling out. Dirt path leading in from camera. Apple trees
flanking, hay bales, split-rail fence, vegetable beds right, corn field right,
rainbow windmill on the hill far right.
**Use for:** shots 15, 18, 22 · channel banner · Short 2 (Rocco)
**Note:** the path leads straight at camera — good for characters walking in.

### `BARN_INT` — inside the barn
Warm wood interior, red walls, exposed beams, hayloft with straw bales, open
doors at back showing green fields, ladder and rope right, wagon wheel and
barrel left, crates of apples, carrots and corn, sunflowers in a blue pot,
milk cans, hanging lantern and green pendant lamp.
**Use for:** shots 24, 29, 56, 69, 77–81
**Note:** already tidy — needs `BARN_INT_MESSY` for scenes 2 and 4.

### `GARDEN` — Clover's domain
Raised wooden beds with carrots, cabbages and tomatoes, sunflowers, potting
bench with terracotta pots and a green glove, blue watering can with a daisy,
trowel, barrel, gate, rainbow windmill and red barn in the distance.
**Use for:** shots 27, 36, 37, 51, 52 · Short 3 (Clover)
**Note:** the blue daisy watering can is a great recurring prop for Clover.

### `WORKSHOP` — Sprocket's domain
Open-sided red workshop, concrete floor, pegboard of wrenches, hammers,
screwdrivers and pliers, workbench with a red vise, red rolling tool chest,
stacked tractor tires, crates of gears, green pendant lamps, fields and the
windmill visible through the left opening.
**Use for:** shots 17, 28, 38, 39, 49 · Short 4 (Sprocket)

### `TRACTOR_YARD` — where the tractor lives
Dirt yard, blue tractor with yellow wheels (it has a face in the grille — nice
touch, keep it), red workshop building right with pegboard and workbench, hay
bales, wagon wheel, shovels and pitchforks, toolboxes, milk cans, corn field
and rainbow windmill behind.
**Use for:** shots 19, 20, 44–46, 70, 73, 74

### `FENCE_LINE` — the golden-hour set
Split-rail fence across the midground, apple trees, sunflowers, daisies, rolled
hay, wide green lawn foreground, red barn with silo mid-distance, rainbow
windmill right, deep blue sky with cloud banks.
**Use for:** shots 2, 3, 5, 13, 76 (the fence-sitting beat)
**Note:** the foreground lawn is wide open — the best plate for staging all
four characters in a row.

### `WINDMILL_FIELD` — the beauty shot
Rainbow-sailed windmill on a hill, patchwork fields in gold, green and blue
stripes, sunflower rows, curving dirt path, hay bales, apple tree, split-rail
fence. The widest, prettiest plate.
**Use for:** shots 1, 75 (the big reveal pan) · Short 1 (farm intro)

---

## CONTINUITY RULES

1. **The windmill is always rainbow-sailed with a cream tower.** It appears in
   six of seven plates and anchors the geography.
2. **The barn is red with a slate-grey roof and a silo.** Not brown, not
   maroon. White X-braced doors.
3. **Fencing is natural wood split-rail.** The white picket fence only appears
   in the far distance — keep it there.
4. **Sky is deep saturated blue with chunky white cloud banks.** Only the
   sunrise and golden-hour shots deviate.
5. **Recurring props:** rolled hay bales, apple trees with red apples, silver
   milk cans, wooden crates, white daisies. Scatter these to tie shots together.

---

## USING PLATES AS VIDEO SOURCES

These are your `image_url` sources for image-to-video. A clip generated from an
approved plate holds the set far better than one generated from text, and it
solves half the consistency problem on its own.

Stored in `refs/locations/`, alongside the character refs in `refs/characters/`:

```
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/refs/locations/barn_ext.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/refs/locations/barn_int.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/refs/locations/garden.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/refs/locations/workshop.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/refs/locations/tractor_yard.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/refs/locations/fence_line.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/refs/locations/windmill_field.png
```

**One limitation to plan around:** image-to-video animates *from* the source
image, so the characters have to be added by the prompt. Expect them to come
out less on-model than the background. For shots where a character's design
really matters, generate a still with the character composited into the plate
first, approve it, then animate from that.

---

## ASPECT RATIO

All plates are 16:9 — right for episodes, wrong for Shorts. For Shorts, use the
9:16 **scene references** below instead: each one is a set already recomposed
vertically with its character standing in it on-model, so a Short no longer
re-invents the set (and drifts) every time.

---

## SCENE REFERENCES (9:16, character in set) — the start point for Shorts

`refs/scenes/<character>_<set>.png` · 1536×2752 (9:16, 2K) · `gemini-3-pro-image`
from the character's ref (image 1) and the set's plate (image 2). Contact sheets
in `refs/scenes/_sheets/`. Four sets per character (two for Nugget).

**The standard frame** (every scene ref, every character):
- The character full body, about 40% of the frame height, lower middle, facing
  the camera, on-model to `refs/characters/`.
- Empty-handed (no story props), eyes open, mouth closed, a friendly smile,
  arms/wings/paws relaxed at the sides.
- Clear open ground in front of them, where a Short's props go.
- The set's landmark behind them (barn, gate, windmill, doors), recomposed for
  vertical. Daylight and the continuity rules above (rainbow windmill with cream
  tower, red barn with slate-grey roof and silo, split-rail fence, deep blue sky
  with chunky clouds; warm bright light indoors).
- No other characters, no text.

### Rocco (approved 2026-11-11)

| File | Set (plate) | Use for |
|---|---|---|
| `rocco_barn_ext.png` | `barn_ext` — barn centred, dirt path toward camera | farm-wide scenes, arrivals, announcements |
| `rocco_fence_gate.png` | `fence_line` — wooden gate in the split-rail fence right behind him, barn and windmill beyond | gate / safety / routine scenes (Short 15's beat) |
| `rocco_barn_int.png` | `barn_int` — open doors centred, hayloft, lantern, crates, milk cans | indoor jobs, tidying, rainy-day scenes |
| `rocco_windmill_field.png` | `windmill_field` — windmill above his hat, curving path, patchwork fields | weather, looking-out-over-the-farm, big-reveal scenes |

### Clover (approved 2026-11-12)

| File | Set (plate) | Use for |
|---|---|---|
| `clover_garden_beds.png` | `garden` — raised beds both sides, gate, barn and windmill behind | planting, growing, harvesting, garden problems |
| `clover_garden_bench.png` | `garden` — potting bench of empty terracotta pots right behind her | potting, seeds, sorting, "what does a plant need?" |
| `clover_fence_flowers.png` | `fence_line` — split-rail fence lined with sunflowers and daisies | flowers, bees and bugs, colours, nature walks |
| `clover_windmill_field.png` | `windmill_field` — windmill beside her ears, path, patchwork fields | weather, sunshine and rain, seasons, big reveals |

Clover-specific rules: made from `clover_noprop_ref.png` (empty pocket) plus
`shorts/short16_droopy_sunflower/short16_still_v2.png` as a third reference
"for her ear length only", so her ears are already at Veo's settled length and
don't grow on screen. No watering can, trowel, glove, seeds or loose carrots in
the sets — those are per-Short story props.

### Sprocket (approved 2026-11-12)

| File | Set (plate) | Use for |
|---|---|---|
| `sprocket_workshop_pegboard.png` | `workshop` — pegboard of hung tools centred behind him, red tool chest, green lamps | tool lessons, "which tool?", tidying tools |
| `sprocket_workshop_bench.png` | `workshop` — workbench with the red vise (top clear), tyres, windmill through the open side | fixing small things on the bench, building, step-by-step jobs |
| `sprocket_tractor_yard.png` | `tractor_yard` — the blue tractor with its grille face behind him, hay, wagon wheel, windmill | tractor and machine fixes, wheels, engines |
| `sprocket_barn_ext.png` | `barn_ext` — barn centred, dirt path, apple tree, windmill | farm-wide fix-it jobs, arrivals, announcements |

Sprocket-specific rules: made from `sprocket_noprop_ref.png` + plate. **His
pouches hold only the red screwdriver, a small silver tool and the
blue-handled tool — no wrench**, so a Short can put the wrench in his hoof
without doubling it (Short 18). The noprop ref itself still shows a wrench in a
pouch and the model copied it into 4 of 16 options even though the prompt
forbade it: check every pouch when picking. `sprocket_barn_ext.png` frames him
larger than the standard (~50% of the height); it was the only clean option.

### Nugget (approved 2026-11-12) — two sets only

| File | Set (plate) | Use for |
|---|---|---|
| `nugget_barn_int.png` | `barn_int` — open barn doors centred, hayloft, lantern, wagon wheel, sunflowers | sorting, counting, indoor helping |
| `nugget_fence_lawn.png` | `fence_line` — fence with sunflowers and daisies, barn and windmill beyond, wide lawn | outdoor learning, practising (flying, hopping), nature beats |

Nugget gets **two** sets, not four: he spends most of his time helping in the
other characters' sets, so a Nugget-led Short often starts from another
character's set instead (see *Nugget in other characters' sets* below). Both
are in **hero form** (cream chest patch), since the standard frame makes him
~40% of the frame height. Made from `nugget_hero_ref.png` + plate.

**Nugget in other characters' sets:** start from that character's scene ref
(image 1), add Nugget with a sidekick pose ref when he's small beside them
(≤20% of the frame height, no patch) or a hero pose ref when he leads the
shot (>20%, patch). See the hero/sidekick table in `docs/character-bible.md`.

All four characters are done. **Prompt and standard for any new set:** the
standard frame above and the prompt below. **Run it with
`creative_generate_in_flow`, `generations_count: 2`** (~$0.80 with two
references, ~$1.00 with three). `run_flow_nodes` always returns 4 options and
doubles the cost — the reference sets were made that way (~$50 for 26 images;
PLAYBOOK credit rule C1). Pick against the standard frame and the character ref.

**The open ground in front of the character is the bottom ~30% of the frame,
which YouTube's title and buttons cover.** Don't stage props or action there;
put them at chest height or beside the character (PLAYBOOK step 4).

**Prompt template** (fill in the character's bible line and the set):

> Vertical 9:16 bright, clean 3D cartoon for preschoolers. A standard reference
> frame. Keep `<NAME>` exactly on-model from the first reference: `<bible
> description line>`. Use the second reference for the set: `<the plate's key
> features>`. Recompose the set for a vertical frame, `<landmark>` behind
> them. `<NAME>` stands `<where>` facing the camera, full body, about 40% of the
> frame height in the lower middle, `<arms>` relaxed at their sides,
> empty-handed, eyes open, mouth closed, friendly smile. Leave clear open ground
> in front of them. Deep blue sky with chunky white clouds, bright daylight. No
> other characters, no text, no letters, no numbers.

Set the node to 9:16 and 2K before running (new nodes default to 16:9 / 1K).

### Using a scene reference in a Short

1. **Pick the scene ref** whose set fits the story, and the **pose ref**
   (`refs/characters/poses/`, see *Pose references* in
   `docs/character-bible.md`) that fits the opening beat.
2. **If the opening is the scene ref's own neutral standing pose with no props
   in hand**, use the scene ref as the Veo start frame directly: no still to
   generate (saves ~$1.61).
3. **Otherwise make the still from them:** `gemini-3-pro-image`, 9:16 / 2K set
   on the node. Image 1 = the scene ref (set, framing, scale), image 2 = the
   pose ref (body pose), image 3 = the character's ref (identity). Prompt:
   "keep the exact set, camera framing and character size of the first image;
   put `<NAME>` in the pose of the second image; keep them on-model to the
   third image; add `<props, exactly one of each>`". The set and framing stay
   put, so the continuity check only has to look at the props and the pose.
   Leave out image 2 when no pose ref fits.
4. Name the Short's still as usual (`shortNN_still.png`) and note the scene ref
   it came from in the spec's `video.description`.
