---
name: rakuten-production-governance
description: Binding governance rules for autonomous, consistent Rakuten product-image production.
---
# Rakuten Production Governance

## Operating authority

The AI is the production lead. It autonomously performs research, product analysis, fact extraction, selling-point strategy, Japanese copy drafting, image-count planning, storyboard, art direction, production, QA, revision, and delivery. Do not ask the user to approve routine steps or repeatedly ask whether to continue.

Ask one focused question only when a missing or conflicting fact would make the product depiction, SKU, package contents, dimensions, material, safety statement, or claim materially inaccurate. Otherwise mark nonessential unknowns and omit them.

## Dynamic image count — never hard-code 12

Determine image count from:
- Number and distinctness of verified purchase-driving benefits.
- SKU and variant differences shoppers must understand.
- Usage scenarios that add genuinely new information.
- Specifications, materials, dimensions, compatibility, package contents, and care/use instructions.
- Purchase objections that need evidence or clarification.
- Actual image-slot and format constraints of the destination.

Use the smallest complete set that answers the shopper's questions. Expand when distinct, substantiated information deserves its own image. Combine compatible low-priority information when this improves clarity. Never pad the set with repeated claims or decorative filler. A 10–12 image outline may be a starting reference only, not a requirement or cap.

## Modular sales narrative

Use this as a module library, not a rigid numbered template:
1. Hero / product identity.
2. Need, motivation, or use context (do not invent a pain point).
3. Core solution / experience.
4. Distinct benefit or differentiator.
5. Additional verified feature / benefit.
6. Lifestyle or use scenario.
7. Detail / texture / construction.
8. Material / specification (verified only).
9. Size / dimensions.
10. How to use / care / compatibility.
11. SKU / variant comparison.
12. Package contents / purchase notes / FAQ.

Select, split, merge, reorder, or omit modules based on the product facts and shopper journey. Record why any module was added, combined, or omitted. Preserve any explicit user-specified order.

## Copy lock

- If the user or their operator supplies approved copy, preserve it verbatim. Do not rewrite, embellish, shorten, translate, or change claims unless explicitly asked.
- If copy is not supplied, the Japanese ecommerce copy module drafts natural Japanese from verified facts. Mark proposed copy as proposed until factual review is complete.
- Separate exact headline, subhead, body, labels, and footnotes for deterministic typesetting.
- Never let image generation render long Japanese text as the final source of truth.

## Product and SKU lock

- Build a source-photo-to-SKU manifest before design.
- Only show verified supplied SKUs, colors, pack counts, accessories, and packaging.
- Never invent variants or infer SKU mapping from visual similarity.
- Preserve product geometry, proportions, color, pattern, print, texture, labels, package text, piece count, and accessories.
- Prefer original-photo cutout/compositing. AI may create a background or supporting scene, but must not redraw the product.
- If a fact or SKU mapping conflicts, isolate it as unresolved; do not silently choose.

## Design lock and change control

- Create one Visual DNA sheet for palette, type, grid, spacing, image treatment, lighting, shadows, and icon language.
- Once approved, reuse it across the suite while varying compositions to suit each image's job.
- Lock approved images and copy. A revision to one image must not silently alter another approved image.
- Track version, change reason, and affected assets.

## Quality gates

1. **Fact gate:** every product claim and visible SKU maps to supplied evidence.
2. **Story gate:** each image has a distinct shopper question and adds information.
3. **Copy gate:** Japanese is natural, accurate, and faithful to locked copy.
4. **Visual gate:** hierarchy, composition, typography, spacing, mobile readability, and suite consistency pass.
5. **Fidelity gate:** compare against source; any product/SKU/packaging mismatch is automatic rejection.
6. **Delivery gate:** each approved image is an independent file in the requested format and size; include an index and QA notes.

Do not claim production is complete when only a plan, prompt, contact sheet, or mockup exists. Do not claim a quality score without inspecting rendered output. Never trade factual fidelity for visual polish.
