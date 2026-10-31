---
name: rakuten-listing-builder
description: Creates fact-checked Japanese Rakuten RMS listing copy and structured upload data from an approved product truth set.
license: MIT
metadata:
  author: repository-owner
  version: "1.0"
---

# Rakuten Listing Builder

## Mission
Turn the approved product truth set, approved selling-point strategy, and SKU manifest into a coherent Japanese Rakuten listing package. This module complements product-image production; it does not replace it.

## Required inputs
- Product name/category and intended use.
- Confirmed product attributes: material, dimensions, weight, quantity, functions, compatibility, care instructions.
- SKU/variant manifest: exact IDs, option values, pack counts, source-photo mapping.
- Package contents and exclusions.
- Confirmed shipping/fulfillment promises, restrictions, warnings, warranty/returns where supplied.
- Approved core selling points and any user-locked copy.
- Target customer and keyword research, when available.

Build a fact ledger with three states: CONFIRMED (source noted), PROPOSED (copy only, not a new product claim), and UNKNOWN (must be omitted or flagged). Never promote UNKNOWN to CONFIRMED by inference.

## Outputs
Prepare a structured, editable listing pack with:
1. Japanese product title (楽天商品名).
2. Catch copy (キャッチコピー).
3. Product description (商品説明文), organized for mobile scanning.
4. Key feature bullets / selling-point summary.
5. SKU and variant option names (商品オプション・選択肢).
6. Specifications and attributes table.
7. Search keyword map: primary, secondary, synonym, and seasonal terms, with evidence/source and relevance notes where research is available.
8. Category / genre suggestion with rationale; mark as recommendation if not confirmed.
9. Package contents, exclusions, use/care instructions, warnings, and FAQ.
10. Image-to-copy consistency map showing which approved image communicates each claim.
11. Missing-information list and pre-publication QA checklist.

## Japanese copy rules
- Write natural, concise Japanese suitable for Japanese shoppers; avoid literal Chinese-to-Japanese phrasing.
- Use terminology appropriate to the category and actual product.
- Keep title keyword-rich but readable; do not keyword-stuff.
- Keep catch copy persuasive but factual.
- Structure descriptions with clear headings, short paragraphs, and mobile readability.
- Preserve user-approved copy verbatim. Any suggested rewrite must be separately labeled as a proposal.
- Do not invent scarcity, rankings, certifications, safety claims, medical/therapeutic effects, material, origin, delivery dates, stock, discounts, or guarantees.

## SEO research rules
- Separate verified search evidence from hypotheses.
- Do not claim a keyword has search volume or ranking strength without a source.
- Prefer relevant buyer-intent phrases over unrelated high-volume terms.
- Include synonyms and natural Japanese variants only when they accurately describe the item.
- Seasonal terms are optional and must match actual campaign timing and product relevance.

## Cross-asset consistency
Use the same product truth set and selling-point IDs as the image suite. Verify that:
- Title, catch copy, description, images, SKU labels, dimensions, materials, and package contents do not contradict one another.
- Every image claim exists in the fact ledger.
- Every variant shown in images exists in the SKU manifest.
- Pack counts and included/excluded accessories match the actual offer.
- Product-page copy does not promise something the supplier or seller has not confirmed.

## RMS readiness
This skill prepares content for human review and entry into Rakuten RMS. Do not claim that content has been uploaded or published unless an authorized RMS integration actually performs and confirms that action. Do not request or store passwords or secret keys in generated files.

## Output format
Return:
- A clean Japanese copy pack ready for review.
- A structured SKU/options table.
- A fact/claim evidence ledger.
- A list of unresolved fields.
- A pre-publication QA checklist.
- Optional CSV/JSON-ready field mapping only when the target RMS workflow and field schema are known.
