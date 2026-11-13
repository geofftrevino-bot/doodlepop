# DoodlePop Kids — CHARACTER BIBLE (LOCKED)
### Baseline established from the four approved reference renders

These four designs are now canon. Every prompt from here forward uses the
descriptions on this page **verbatim**. Do not paraphrase, do not abbreviate,
do not add details that aren't listed.

> **Channel:** DoodlePop Kids  ·  **Show:** Fix-It Farm
**Reference files:** `refs/characters/rocco_ref.png` · `clover_ref.png` · `sprocket_ref.png` · `nugget_sidekick_ref.png` / `nugget_hero_ref.png`

---

## ⚠️ CORRECTIONS TO ALL EARLIER PROMPTS

The approved renders differ from the descriptions I was using. **The old
character tags in the shot list and shorts pack are now wrong** and will
produce off-model results. Specific changes:

| Character | Old prompt said | Approved design actually has |
|---|---|---|
| **Rocco** | "red kerchief" around neck | **No kerchief.** Red band on the hat. Golden-yellow neck feathers. **Teal tail** — this is his signature color. |
| **Clover** | "green gardening apron with seed-packet pockets" | **Green overalls** with yellow buttons and a single front pocket holding a carrot |
| **Sprocket** | "tiny welding goggles pushed up on his head" | **No goggles.** Tool belt with a gold buckle and two brown pouches |
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

> **ROCCO:** a cheerful tall cartoon rooster with an orange-red body, a long
> neck and a red face, big round expressive eyes with blue irises, a large
> yellow beak, a red comb and wattle, golden-yellow scalloped neck and chest
> feathers, a large curved **teal-turquoise tail**, teal wingtips he gestures
> with like hands, yellow legs and feet, and a woven straw farmer's hat with a
> red band.

*Updated after Short 15 (v2 look): taller and slimmer than v1, bigger blue-iris
eyes, bigger beak. Reference: `refs/characters/rocco_ref.png`; v1 is in
`archive/refs/rocco_ref_v1.png`. Every Short now shows the v2 look (Short 11 was the last, rebuilt Oct 3).*

- **Silhouette cue:** the teal tail. It reads instantly at thumbnail size.
- **Posture:** chest out, upright, confident. He takes up space.
- **Never:** without the straw hat.
- **Pose references** (`refs/characters/poses/`, approved 2026-11-11; see *Pose
  references* below):

  | File | Pose | Use for |
  |---|---|---|
  | `rocco_pose_wave.png` | one wingtip raised in a hello | greetings, intros, talking to the viewer |
  | `rocco_pose_point.png` | wingtip pointing out to his side | "look at this!", presenting a prop or problem |
  | `rocco_pose_thinking.png` | wingtip under his beak, other across his tummy, eyes up | puzzles, "whose is this?", listening for a sound |
  | `rocco_pose_proud.png` | wingtips on hips, chest out | confident starts, "all fixed / tidy!" moments |

---

## CLOVER — the rabbit who tends the garden

> **CLOVER:** a soft white cartoon rabbit with tall upright ears with pink
> inner ears, big glossy black eyes, rosy pink cheeks, a small pink nose, two
> little front teeth, a fluffy round tail, wearing **bright green overalls**
> with yellow round buttons and a front pocket holding an orange carrot.

- **Silhouette cue:** tall upright ears. They stay **up** — she's alert and happy, not timid.
- **Props:** small trowel with a wooden handle, watering can, seed packets.
- **Never:** floppy/drooping ears except as a deliberate sad beat.
- **Ear length on screen:** Veo grows her ears in the first second if a start
  frame has the ref's shorter ears. Every new still and reference passes
  `shorts/short16_droopy_sunflower/short16_still_v2.png` "for her ear length
  only"; her scene and pose references already have the settled length.
- **Pose references** (`refs/characters/poses/`, approved 2026-11-12; see *Pose
  references* below):

  | File | Pose | Use for |
  |---|---|---|
  | `clover_pose_wave.png` | one paw raised in a hello | greetings, intros, talking to the viewer |
  | `clover_pose_point.png` | paw pointing out to her side | "look at this!", showing a plant or a problem |
  | `clover_pose_thinking.png` | paw on her chin, other across her tummy, eyes up | puzzles, "what does it need?", wondering |
  | `clover_pose_proud.png` | paws on hips, ears up | confident starts, "it grew!" moments |

---

## SPROCKET — the pig who fixes everything

> **SPROCKET:** a cheerful chunky cartoon piglet with a soft pink body, floppy
> pink ears, a big pink snout, rosy cheeks, solid glossy black eyes with a
> small white highlight (no coloured irises), dark brown hooves, a curly pink
> tail, wearing a **brown leather tool belt with a gold buckle** and two brown
> tool pouches holding a red-handled screwdriver and a blue-handled tool.

- **Silhouette cue:** the tool belt at his waist.
- **Props:** silver wrench (his signature), screwdriver, oil can, toolbox.
- **Never:** without the tool belt.
- **No wrench in the pouches.** His wrench is a hand prop. In every still and
  reference his pouches hold only the red screwdriver, a small silver tool and
  the blue-handled tool, so the wrench never appears twice. Say "no wrench
  anywhere on him" in the prompt and still check each option's pouches —
  `sprocket_noprop_ref.png` shows a wrench in a pouch and the model copies it.
- **He never takes a tool out of his belt.** Veo refills the pouch, so the tool
  shows twice (the shelved "Rattly Tractor"). The tool he uses is a separate prop placed in the
  scene or his hoof from frame one. See `docs/prop-rules.md`.
- **Pose references** (`refs/characters/poses/`, approved 2026-11-12; see *Pose
  references* below):

  | File | Pose | Use for |
  |---|---|---|
  | `sprocket_pose_wave.png` | one front hoof raised in a hello | greetings, intros, talking to the viewer |
  | `sprocket_pose_point.png` | hoof pointing out to his side | "look at this!", showing what's broken |
  | `sprocket_pose_thinking.png` | hoof under his chin, other across his tummy, eyes up | puzzles, "what's wrong with it?", choosing a tool |
  | `sprocket_pose_proud.png` | hooves on hips above the belt | confident starts, "all fixed!" moments |

---

## NUGGET — the chick who helps with everything

### ⚠️ NUGGET HAS TWO FORMS. Pick by how large he is in frame.

| Form | When | Chest patch | Reference |
|---|---|---|---|
| **SIDEKICK** | He's ≤20% of frame height — beside Sprocket, in a group, background | **No patch.** Too small to read; adding it makes him look dirty | `nugget_sidekick_ref.png` |
| **HERO** | He's >20% of frame height — his own Short, close-ups, anytime he leads | **Pale cream fuzzy oval on his chest** — mandatory | `nugget_hero_ref.png` |

**This is permanent.** The patch was present in Short 7 and missing in Short 12,
which is exactly the inconsistency to stop. If he's big enough to see, the patch
is there.

> **NUGGET (sidekick):** a very small round fluffy yellow cartoon chick with soft
> fuzzy texture, a **three-feather tuft** on top of his head, oversized glossy
> black eyes, an orange beak, peachy-orange blush cheeks, tiny yellow wings, and
> orange legs and feet.

> **NUGGET (hero):** a round fluffy yellow cartoon chick with soft fuzzy texture,
> a **three-feather tuft** on top of his head, oversized glossy dark eyes, an
> orange beak, peachy-orange blush cheeks, small yellow wings, orange legs and
> feet, and a **soft pale cream circular patch of lighter downy feathers across
> his chest and belly**, fluffier and paler than the yellow around it.

**In prompts, always name the patch for hero shots** — "a soft pale cream
circular patch of lighter fluffy feathers on his chest" — and never mention it
for sidekick shots.

- **Silhouette cue:** round fuzzy body with the head tuft. Smallest of the cast.
- **Scale rule:** roughly **one-third** of Sprocket's height. Every prop he
  carries should look comically oversized — that's the entire joke.
- **Never:** slim or tall. He is a fuzzy ball.
- **Pose references** (`refs/characters/poses/`, approved 2026-11-12; see *Pose
  references* below). Eight, split by form: four **hero** poses (patch) for
  when he leads, four **sidekick** helper poses (no patch) for when he's beside
  a bigger character in their set.

  | File | Form | Pose | Use for |
  |---|---|---|---|
  | `nugget_hero_pose_wave.png` | hero | one wing raised in a hello | his own Shorts: greetings, intros |
  | `nugget_hero_pose_point.png` | hero | wing pointing out to his side | "look at this!" (beak very slightly open — reads as a smile) |
  | `nugget_hero_pose_thinking.png` | hero | wing tip under his beak, other on his tummy, eyes up | puzzles, counting, "how do I…?" |
  | `nugget_hero_pose_proud.png` | hero | wings on hips, patch puffed out | "I did it!" moments |
  | `nugget_sidekick_pose_cheer.png` | sidekick | both wings up | celebrating a friend's fix |
  | `nugget_sidekick_pose_look_up.png` | sidekick | head tipped back, gazing up | listening to Rocco / Sprocket / Clover |
  | `nugget_sidekick_pose_hop.png` | sidekick | mid-hop, wings out | eager arrival, "can I help?" |
  | `nugget_sidekick_pose_salute.png` | sidekick | wing at his brow | "ready to help!" |

  Both forms follow their own reference: hero eyes are dark brown
  (`nugget_hero_ref.png`), sidekick eyes are black (`nugget_sidekick_ref.png`).
  Check every option for the patch (hero: present; sidekick: absent) and a
  closed beak — the beak opened on about a quarter of Nugget's 40 options.

---

## POSE REFERENCES

Four standard starting poses per character, each on a plain soft cream
background with a soft floor shadow, so one pose works on any of the
character's four scene references (`refs/scenes/`, see
`docs/location-bible.md`). Pose x set covers 16 openings from 8 images.

`refs/characters/poses/<character>_pose_<name>.png` · 1536×2752 (9:16, 2K) ·
`gemini-3-pro-image` from the character's ref only (~$0.30 an option, 4 options
a run).

**The standard:** full body, centred, about 60–70% of the frame height, facing
camera, empty-handed, eyes open, mouth closed. **Tail/ears on the same side as
the character's ref** — reject options where the model mirrors the character
(it did on 2 of Rocco's 16). One clear gesture per pose.

**Done — all four characters:** Rocco, Clover and Sprocket (wave, point,
thinking, proud; Sprocket empty-handed, the wrench added per Short); Nugget
(hero wave, point, thinking, proud + sidekick cheer, look-up, hop, salute).
Reject splayed or off-length ears, open mouths/beaks, mirrored options, stray
props (e.g. a wrench in Sprocket's pouch) and the wrong Nugget form.

**Prompt template:**

> Vertical 9:16 bright, clean 3D cartoon for preschoolers. A character pose
> reference sheet: plain soft cream background with a soft shadow under
> `<their>` feet, nothing else. Keep `<NAME>` exactly on-model from the
> reference: `<bible description line>`. Full body, centred, about 70% of the
> frame height, standing on the ground facing the camera. POSE: `<the pose, one
> clear gesture>`; eyes open, mouth closed. Empty-handed, no props, no other
> characters, no text, no letters.

**Using a pose in a Short:** see *Using a scene reference in a Short* in
`docs/location-bible.md` — the pose ref goes in as the second image.

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
