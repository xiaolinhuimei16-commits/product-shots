---
name: rakuten-product-integrity
description: "Protects exact product appearance and factual accuracy across AI-generated and composited Rakuten ecommerce images, including SKU variants, packaging, accessories, dimensions, and approved source-photo usage."
license: MIT
metadata:
  author: repository-owner
  source: custom Rakuten adaptation
  version: "1.0"
---

# Rakuten Product Integrity

## Absolute rule

The real product is the source of truth. AI may improve presentation, but must not redesign the item being sold.

## Locked attributes

Treat these as immutable unless the user explicitly confirms a real variant:
- Shape, silhouette, proportions, construction, seams, openings, and component positions.
- Color, print, pattern, texture, gloss, transparency, and material appearance.
- Number of items, included accessories, package contents, and packaging graphics.
- SKU-to-image mapping and differences between variants.
- Product labels, logos, and printed wording.

## Allowed operations

- Background removal and clean cutouts.
- Proportional resizing and placement.
- Background replacement or scene compositing.
- Lighting and shadow refinement that does not change product color or structure.
- Non-destructive crop and layout.
- Adding separately typeset labels, arrows, measurements, and Japanese copy when verified.

## Prohibited operations

- AI redrawing or inventing product details.
- Adding or removing pieces, accessories, or package contents.
- Changing product color, shape, texture, print, or dimensions.
- Showing a different SKU as if it were the supplied SKU.
- Fabricating certificates, test marks, safety labels, dimensions, or performance.
- Using a lifestyle scene that implies an unsupported function or use.

## Source-photo mapping

For every image in a suite, record:
- Which original photo(s) represent the product.
- Whether the product is directly composited or regenerated.
- Which SKU / variant is shown.
- Which attributes must remain unchanged.
- Any uncertainty that requires user review.

## SKU naming

Accept the user's labels exactly, including numeric labels (1, 2, 3) or alphabetic labels (A, B, C). Never infer a SKU mapping from color or appearance if the source mapping is ambiguous.

## Failure handling

If a source image is too low quality or does not show a critical detail, do not fabricate the missing detail. Request a clearer photo or omit that detail. If a generated result changes the product, reject it and use a compositing-based correction instead.
