# DoodlePop Kids — LOCATION BIBLE (LOCKED)
### Seven approved background plates · all 1672×941 (16:9)

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

Upload alongside the character refs, lowercase:

```
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/barn_ext.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/barn_int.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/garden.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/workshop.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/tractor_yard.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/fence_line.png
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/windmill_field.png
```

**One limitation to plan around:** image-to-video animates *from* the source
image, so the characters have to be added by the prompt. Expect them to come
out less on-model than the background. For shots where a character's design
really matters, generate a still with the character composited into the plate
first, approve it, then animate from that.

---

## ASPECT RATIO

All plates are 16:9 — right for episodes, wrong for Shorts. For vertical you
have two options: generate 9:16 versions of the plates you need most
(`windmill_field`, `garden`, `workshop`, `tractor_yard`), or frame Shorts tight
on characters so the background crop matters less. The first is cleaner; the
second is cheaper.
