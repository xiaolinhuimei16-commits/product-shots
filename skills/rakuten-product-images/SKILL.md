---
name: rakuten-product-images
description: "Plans and produces Japanese Rakuten product main images and secondary image suites. Handles hero image, selling-point images, usage scenes, detail, size, SKU, package contents, Q&A, and Japanese mobile-first layouts. Routes to the existing product-shots-image-gen engine after a storyboard is approved."
license: MIT
metadata:
  author: repository-owner
  source: custom Rakuten adaptation
  version: "1.0"
---

# Rakuten Product Images

You are the execution skill for Japanese Rakuten product-image suites. You turn the approved brief from `rakuten-suite-planner` into an image-by-image production plan, then dispatch visual generation to the existing `product-shots-image-gen` engine.

## Mandatory operating gate for employee work

Follow `references/employee-production-sop.md` in addition to the shared skills. In particular: create an evidence-linked SKU manifest; **lock the exact approved reference image and approved Japanese copy before rendering**; reject any invented SKU or product repaint; and require independent JPGs, per-file QA verdicts, and a complete index before announcing completion. Generative illustrations are not reliable replacements for supplier photos. A contact sheet is a preview, never the deliverable. For the crispy-squishy example, A–M are **13 sales options**, not 13 butter colors; honor each exact supplier option and verify 12-packs/random colors. If source images retain watermarks or Chinese supplier annotations, mark affected images BLOCKED rather than claiming Rakuten listing readiness.

## Scope

- Rakuten product main image and secondary product images.
- Image count is dynamic. Determine the smallest complete set from verified benefits, SKU complexity, shopper questions, use cases, specifications, and destination slot limits. Never fix the count at 12 or pad with repetitive images.
- Single-image requests are supported.
- Store banners and campaign banners are separate tasks; do not force square product-image rules onto them.
- This skill does not create Amazon A+ modules.

## Critical differences from Amazon

Do not blindly inherit Amazon main-image rules such as pure-white-only background or no-text requirements. Rakuten product-image art direction may use designed hero compositions and Japanese copy when appropriate to the user's store and current platform rules. However:
- Never imply that any particular overlay, badge, text density, or claim is officially permitted without checking current Rakuten rules.
- Keep the product immediately identifiable at thumbnail size.
- Keep copy concise and readable on mobile.
- If the user requests a clean white-background image, follow that request.
- If the user provides a store-specific template or reference, treat it as the visual baseline.

## Execution procedure

### Step 0 — Load the shared Rakuten rules

Read:
- `rakuten-suite-planner`
- `rakuten-japanese-copy`
- `rakuten-visual-design`
- `rakuten-product-integrity`
- `rakuten-listing-builder` (for RMS listing copy and structured upload data)
- `references/image-plan-framework.md`
- `references/production-checklist.md`
- `references/quality-pilot.md`
- `references/no-api-preflight.md`
- `references/three-image-pilot-brief.md` when using the current crispy squishy toy test product
- `references/production-governance.md` (binding authority, dynamic image count, copy/product/design locks)
- **`references/employee-production-sop.md` (mandatory employee handoff: A–M SKU source manifest, approved-reference lock, Japanese editorial gate, human QA and file-by-file delivery)**

### Step 1 — Establish the product truth set

Build a compact fact sheet from the user's materials:
- Product identity and intended use.
- Confirmed material, dimensions, weight, quantity, and included accessories.
- SKU/variant names and source-photo mapping.
- User-provided claims and locked copy.
- Unknowns and intentionally omitted information.

Never fill gaps with assumptions. If data is absent and nonessential, omit it. If it affects the accuracy of the image, ask one focused question.

### Step 2 — Determine creative mode

- Copy-led: exact user copy is locked. Design around it.
- Autonomous: develop the buyer motivation and Japanese copy from confirmed facts.
- Hybrid: lock supplied phrases and label new copy as proposals.

Do not repeatedly ask for details already visible in the supplied images or messages.

### Step 3 — Plan the suite

Use `references/image-plan-framework.md` and the binding `references/production-governance.md`. Select the image count from product complexity; 10-12 may be a planning reference only, never a fixed target or cap. Each image must have a distinct purpose. Preserve any explicit user-specified order.

For every image define:
- Image number and role.
- Shopper question / purchase motivation.
- Composition and scene.
- Main product source photo and SKU.
- Exact Japanese copy.
- Secondary graphics / icons / annotations.
- Dependencies and factual proof.
- Mobile crop / safe area notes.

### Step 4 — Lock Visual DNA

Define one shared design system:
- Product-led palette and accent colors.
- Japanese type family and type hierarchy.
- Grid, alignment, spacing, margins.
- Background, light direction, shadow, perspective.
- Icon, annotation, badge, border, and corner treatment.
- Rules for scene variation and product scale.

Do not make every image a copy of the hero. Maintain the same design language while changing composition to suit each message.

### Step 4A — Quality-first pilot gate

Before scaling any new product into a full suite:
- Load `references/quality-pilot.md`.
- If no image API or local renderer is configured, load `references/no-api-preflight.md` and stop before any paid generation.
- For the current crispy squishy decompression toy, use `references/three-image-pilot-brief.md`.
- Prepare a small representative pilot (normally hero, core experience, and lifestyle/use scene) to validate visual direction. Pilot size may change with product complexity.
- The hero must follow the user's explicit direction: enlarged butter-stick squishy as the dominant product, other SKUs only as supporting variety.
- Do not claim a visual quality score until actual rendered files have been inspected against source photos.
- Require pilot images to pass the product-fidelity hard gate and target 90/100 before scaling to the planned full set.

### Step 5 — Generate images through the existing engine

Call the existing `product-shots-image-gen` skill for each approved image. Do not implement a second API client or hard-code a provider.

- Pass the original product photo as a reference image whenever supported.
- Use image-to-image for edits and product-preserving compositions.
- Prefer cutout + compositing for exact product appearance.
- Generate backgrounds / lifestyle environments separately if that better protects product fidelity.
- For Japanese text that must be exact, generate the visual composition first and typeset the copy in a deterministic post-processing step. Never trust image generation alone for long or small Japanese text.
- Pass `use_case=text-overlay` when the chosen engine's routing requires crisp text; otherwise use the model best suited to the visual task.
- Use 1:1 for standard product-image slots unless the user supplies another exact Rakuten slot or format. Do not assume every Rakuten asset is square.

### Step 6 — Product-preservation review

Compare every result with the source:
- Shape and proportions.
- Color, pattern, print, material, texture.
- Number of pieces and accessories.
- Package and labels.
- SKU identity.
- Realistic scale, shadows, contact points, and perspective.

Reject any image with altered product details. Correct by compositing the original product, not by repeatedly asking a model to redraw it.

### Step 7 — Japanese and mobile review

Check:
- Natural Japanese spelling, grammar, punctuation, and terminology.
- User-locked copy unchanged.
- Headline hierarchy and readable line breaks.
- Contrast and mobile legibility.
- No clipping at common mobile crops.
- No tiny dense specification text.
- No unsupported or misleading claims.

### Step 8 — Build the Rakuten listing pack

After the product truth set and selling-point strategy are approved, invoke `rakuten-listing-builder` to prepare the Japanese product title, catch copy, description, SKU/options, specifications, keyword map, category suggestion, package contents, purchase notes, and FAQ. Keep image copy and listing copy as separate assets, but derive both from the same fact ledger and selling-point IDs. Run a cross-asset consistency check before delivery. This prepares RMS-ready content; it does not publish to RMS unless a confirmed authorized integration is available.

### Step 9 — Delivery and change control

Deliver:
- Final image set with original file names where requested.
- Numbered image index and role.
- Any copy list / source mapping if requested.
- A QA report listing pass / revise / omitted items.

Use version labels. The AI leads routine production without repeatedly asking the user to continue. Lock approved copy, product/SKU mapping, Visual DNA, and images. Do not redesign approved images when revising another image. Ask only when a material factual conflict blocks accurate production.

## Output rules

- Do not claim a file was generated unless the engine returned a real file path.
- Do not claim a full suite is complete when only a storyboard or prompt has been produced.
- Do not claim product integrity has passed without comparing the output to source photos.
- Be transparent when a step requires a configured image-generation API key or local execution environment.
