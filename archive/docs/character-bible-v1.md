# DoodlePop Kids — CHARACTER BIBLE (LOCKED)
### Baseline established from the four approved reference renders

These four designs are now canon. Every prompt from here forward uses the
descriptions on this page **verbatim**. Do not paraphrase, do not abbreviate,
do not add details that aren't listed.

> **Channel:** DoodlePop Kids  ·  **Show:** Fix-It Farm
**Reference files:** `character-refs/ROCCO_ref.png` · `CLOVER_ref.png` · `SPROCKET_ref.png` · `NUGGET_ref.png`

---

## ⚠️ CORRECTIONS TO ALL EARLIER PROMPTS

The approved renders differ from the descriptions I was using. **The old
character tags in the shot list and shorts pack are now wrong** and will
produce off-model results. Specific changes:

| Character | Old prompt said | Approved design actually has |
|---|---|---|
| **Rocco** | "red kerchief" around neck | **No kerchief.** Red band on the hat. Golden-yellow neck feathers. **Teal tail** — this is his signature color. |
| **Clover** | "green gardening apron with seed-packet pockets" | **Green overalls** with yellow buttons and a single front pocket holding a carrot |
| **Sprocket** | "tiny welding goggles pushed up on her head" | **No goggles.** Tool belt with a gold buckle and two brown pouches |
| **Nugget** | "little blue cap" | **No cap.** Three-feather yellow tuft on top of his head |

Search and replace these in the shot list before generating anything else.

---

## THE MASTER STYLE BLOCK

Prepend to **every** image and video prompt:

> Preschool 3D animated cartoon in a soft toy-like claymation style. Smooth
> matte vinyl surfaces, chunky rounded shapes, no hard outlines, gentle soft
> shading, oversized glossy black eyes with a single bright highlight, rosy
> blush cheeks, bright saturated colors, warm cheerful storybook lighting.
> No text, no logos, no on-screen words.

---

## ROCCO — the rooster who runs the farm

> **ROCCO:** a cheerful chunky cartoon rooster with a bright orange-red body,
> golden-yellow neck and chest feathers, a large curved **teal-turquoise tail**
> and teal wingtips, a small red comb and red wattle, a yellow beak, yellow
> legs and feet, and a woven straw farmer's hat with a red band.

- **Silhouette cue:** the teal tail. It reads instantly at thumbnail size.
- **Posture:** chest out, upright, confident. He takes up space.
- **Never:** without the straw hat.

---

## CLOVER — the rabbit who tends the garden

> **CLOVER:** a soft white cartoon rabbit with tall upright ears with pink
> inner ears, big glossy black eyes, rosy pink cheeks, a small pink nose, two
> little front teeth, a fluffy round tail, wearing **bright green overalls**
> with yellow round buttons and a front pocket holding an orange carrot.

- **Silhouette cue:** tall upright ears. They stay **up** — she's alert and happy, not timid.
- **Props:** small trowel with a wooden handle, watering can, seed packets.
- **Never:** floppy/drooping ears except as a deliberate sad beat.

---

## SPROCKET — the pig who fixes everything

> **SPROCKET:** a cheerful chunky cartoon piglet with a soft pink body, floppy
> pink ears, a big pink snout, rosy cheeks, dark brown hooves, a curly pink
> tail, wearing a **brown leather tool belt with a gold buckle** and two brown
> tool pouches holding a red-handled screwdriver and a blue-handled tool.

- **Silhouette cue:** the tool belt at her waist.
- **Props:** silver wrench (her signature), screwdriver, oil can, toolbox.
- **Never:** without the tool belt.

---

## NUGGET — the chick who helps with everything

> **NUGGET:** a very small round fluffy yellow cartoon chick with soft fuzzy
> texture, a **three-feather tuft** on top of his head, oversized glossy black
> eyes, an orange beak, peachy-orange blush cheeks, tiny yellow wings, and
> orange legs and feet.

- **Silhouette cue:** round fuzzy body with the head tuft. Smallest of the cast.
- **Scale rule:** roughly **one-third** of Sprocket's height. Every prop he
  carries should look comically oversized — that's the entire joke.
- **Never:** slim or tall. He is a fuzzy ball.

---

## USING THESE FOR REAL CONSISTENCY

Text prompts alone will drift no matter how precise the wording. The stronger
method is **image-to-video**: `generate_video` accepts an `image_url`, so a
clip generated from an approved still holds the design far more tightly than
one generated from text.

**The catch:** that field needs a public URL, not a local file. To use it,
host these four PNGs somewhere reachable — a GitHub repo, Imgur, Dropbox
direct link, any static host — then paste those URLs into the generation.
Once you have them, send them over and I'll switch every remaining prompt to
image-to-video.

**In the meantime:** generate a still with `generate_image` first using the
locked tag, eyeball it against the reference, and only animate once it matches.
Cheaper than regenerating video.

---

## SCALE CHART

Tallest to shortest — worth stating in any group shot prompt:

**Rocco** (tallest, hat adds height) → **Clover** (ears add height) →
**Sprocket** (stocky, wide) → **Nugget** (tiny, about one-third of Sprocket)

> Group-shot line to paste: *"Rocco is tallest, Clover is nearly as tall with
> her ears up, Sprocket is shorter and stockier, and Nugget is tiny — about a
> third of Sprocket's height."*
