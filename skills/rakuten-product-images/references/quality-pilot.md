---
name: rakuten-quality-pilot
description: Three-image quality gate for validating Rakuten visual quality before scaling.
---
# Rakuten Quality Pilot — 3-image gate

## Purpose
A successful API response is not proof of professional design quality. Validate one product with three deliberately different images before scaling to a 10–20+ image suite.

## Pilot images
1. **Hero / main visual** — follow the user's composition instruction. For the current squishy-toy test, the butter-stick squishy is the enlarged primary subject; other supplied SKUs appear only as supporting variety. Do not alter product geometry.
2. **Core experience / selling point** — show the actual squeeze / decompression experience. This product's core appeal is decompression. Do not force unrelated conventional pain-point storytelling. Depict deformation, rebound, texture, or sound only if source photos/video substantiate it.
3. **Lifestyle / use scene** — show a plausible everyday context such as desk, study break, or home leisure. Composite the exact real product from source photos whenever fidelity matters.

## Before any render
- Record source filenames and assign SKU IDs exactly as supplied (numeric or alphabetic).
- Create a fact sheet: confirmed facts, user-provided claims, unknown facts.
- Identify mode: autonomous, copy-led, or hybrid.
- Lock user-supplied copy; do not silently rewrite.
- Lock one Visual DNA sheet: palette, Japanese type family, type scale, grid, margins, lighting, background treatment, icon style.
- Prepare storyboard and get approval before paid rendering.

## Compositing-first method
1. Use original product image as immutable foreground.
2. Remove background / mask only where needed; preserve original pixels and proportions.
3. Generate or create background separately.
4. Composite original product into scene with proportional scaling, realistic contact shadow, and matching perspective.
5. Typeset Japanese text after image generation in a deterministic layout step. Never rely on the image model for exact Japanese copy.
6. Export proof and inspect at full resolution and phone-size preview.

If no image API is configured, planning, storyboard, copy QA, Visual DNA, source mapping, and layout mockups can still be tested. Generated photoreal backgrounds require a configured image model or local model runtime. Do not imply they were generated for free.

## Weighted quality rubric (100 points)
| Dimension | Points | Pass condition |
|---|---:|---|
| Product fidelity | 25 | Shape, color, texture, print, count, accessories and SKU match source |
| Visual craft | 20 | Clear focal point, polished lighting, composition, believable shadows |
| Japanese typography | 15 | Correct characters, natural line breaks, hierarchy, phone readability |
| Selling-point clarity | 15 | One clear message; visual supports the claim |
| Suite coherence | 15 | Same Visual DNA; each image has a distinct role |
| Japanese accuracy | 10 | Natural Japanese; no unsupported or misleading claims |

Target: 90/100 for production; 85–89 requires focused revision; below 85 rejects the pilot. Any product-identity error, false claim, or incorrect Japanese is an automatic fail.

## Review protocol
For each image provide full-size and phone-size previews, score by dimension, exact defects, revision instructions limited to that image, version number, and change log. Do not average away critical defects.

## Scaling gate
Only after all three pilot images pass: freeze Visual DNA, expand the storyboard, render in controlled batches, keep approved images locked, and track cost, revision count, and accepted-image rate. Re-test when changing model, gateway, prompt family, or category.
