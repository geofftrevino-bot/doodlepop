# Fix-It Farm — ASSET PIPELINE

> **Channel:** DoodlePop Kids · **Show:** Fix-It Farm

---

## ⚠️ NO MORE UPLOAD PICKERS

Every reference since we moved off Runvid went through a manual file picker.
That was unnecessary. There are two ways to skip it entirely:

### 1. Straight from the repo, by URL

`creative_attach_reference_file` takes a **direct https URL**. Any file in the
repo can be attached with no upload at all:

```
https://raw.githubusercontent.com/geofftrevino-bot/doodlepop/main/<file>
```

Verified working. This is the default path from now on.

### 2. From the workspace library, by asset ID

Everything uploaded previously is **still in the ElevenLabs library** —
character refs, every composite, all of it. `creative_get_available_assets`
lists them; they can be reused by id without re-uploading or re-fetching.

---

## THE LOOP, AS IT SHOULD BE

| Step | Who | Notes |
|---|---|---|
| 1. Build the composite | me | in the container |
| 2. **Commit it to the repo** | you | the one manual step that remains |
| 3. Attach by URL and generate | me | no picker |
| 4. **Download the result, commit it** | you | ElevenLabs storage is unreachable from my side |
| 5. Measure, mix, master | me | |

**Two commits per Short.** Previously it was two commits plus an upload for
every reference.

---

## WHAT STILL CAN'T BE AUTOMATED

**I can't push to the repo.** Anything built in the container needs one commit
from you before I can attach it.

**I can't read ElevenLabs storage.** The signed URLs are on a blocked domain, so
finished generations have to come back via the repo.

Both are environment limits, not tool limits. If the container ever gets git
write access or that domain is allowed, the loop closes completely.

---

## STANDING RULES THIS SITS ALONGSIDE

- **Frame one is locked** — anything that must exist at t=0 goes in the still,
  never the prompt
- **Approve the still before paying for motion**
- **Check the schema before passing model parameters** — aspect ratio and
  resolution default wrong, and `auto` exists
- **Estimate before every run**, and don't trust a clean estimate as proof the
  reference uploaded — the run itself is the check
- **Two variations on image edits**, one on video

---

## COST REFERENCE

| Operation | Cost |
|---|---|
| Veo 3.1 Fast video, 8s, 1080p, no audio | **$0.88** |
| gpt-image-2 edit, 2 variations | **$0.53** |
| Sound effect, 2 variations | **$0.02** |
| sync-lipsync-v3 pass | **$1.17** |

A single-character Short is about **$0.88**. A four-shot cut-together Short is
about **$3.50**.
