---
name: rakuten-production-checklist
description: Production and QA checklist for Japanese Rakuten product-image suites.
---

# Rakuten Production Checklist

## Before generation

- [ ] Platform confirmed as Rakuten, not Amazon.
- [ ] Image type and dimensions confirmed or safely defaulted.
- [ ] User's copy mode identified: copy-led, autonomous, or hybrid.
- [ ] All source photos catalogued.
- [ ] SKU labels mapped to source photos.
- [ ] Product facts separated into confirmed / unknown.
- [ ] Product-preservation constraints written.
- [ ] Storyboard approved where required.
- [ ] Suite Visual DNA approved or derived from supplied references.

## Per-image brief

- [ ] Unique image role.
- [ ] Distinct shopper question / motivation.
- [ ] Correct SKU and source-photo reference.
- [ ] Exact Japanese copy and status (locked / proposed).
- [ ] Composition and scene described.
- [ ] Verified facts only.
- [ ] Correct aspect ratio and slot dimensions.
- [ ] Mobile-safe text placement.

## Image-generation dispatch

- [ ] Existing product-shots-image-gen engine used.
- [ ] API key configuration checked by the engine.
- [ ] Original product photo included as reference where appropriate.
- [ ] Correct image-to-image / text-to-image use case selected.
- [ ] Exact Japanese copy is not left solely to image generation when accuracy matters.
- [ ] Output path returned and recorded.

## Final QA

- [ ] Product geometry matches the source.
- [ ] Product color and texture match the source.
- [ ] SKU, quantity, accessories, and package contents are correct.
- [ ] No invented certification, safety mark, material, dimension, or performance.
- [ ] Japanese is natural and error-free.
- [ ] User-locked copy is unchanged.
- [ ] Mobile readability and crop are acceptable.
- [ ] Shadows, perspective, and contact points look realistic.
- [ ] Visual DNA is consistent across the set.
- [ ] Each image adds distinct information.
- [ ] Approved images have not been changed unintentionally.

## Release status

Use one of these statuses for every image:
- **PASS** — accurate and ready.
- **REVISE** — a specific correctable issue remains.
- **HOLD** — a critical source fact or image is missing.
- **OMIT** — the module is not relevant or would require unsupported claims.

Never report the whole suite as complete while any critical image is HOLD or REVISE.
