# Rakuten Creative OS — Employee Production SOP

> Status: operating procedure, not a guarantee that any image-generation backend preserves products. Before using or publishing assets, a human must inspect every delivered file.

## 1. Intake: do not ask the seller to repeat known information

Create a job folder with `sources/`, `references/`, `plan/`, `output/`, `qa/`.
Collect the actual product photos, SKU screenshot/table, product facts, mandatory copy, approved design examples, target Rakuten storefront and output specifications. Reuse provided materials. Do not reconstruct missing evidence from memory or an AI mockup. Missing nonessential dimensions, material, weights, age labels or certifications are **omitted**, not guessed.

Required truth manifest for *each selectable sales option*:
`sku_id | exact_supplier_label | Japanese_name_reviewed | units_per_order | assortment_rule | source_photo_paths | confirmed_visible_details | source_of_confirmation | blocked_unknowns`.

**The number of selectable options is not the number of unique product shapes.** A 12-pack / assortment is its own sales option with different contents. Do not display a single item and promise a full display box; do not convert a multi-category assortment into color variants.

## 2. Five authoritative locks — in this priority order

1. **Product/SKU lock:** supplied actual product and packaging photos, supplied sales options and confirmed pack contents. No repainting, regeneration or fabricated variant.
2. **Fact lock:** confirmed information only. Unknown facts are omissions/flags. Avoid unsupported claims about sound, therapeutic benefit, age, materials, durability or safety.
3. **Copy lock:** user-approved Japanese copy is verbatim; other copy is drafted by Rakuten operator + Japanese copy editor, reviewed and frozen **before** visual design.
4. **Visual DNA lock:** use the *specific* seller-approved reference image, not merely a similar aesthetic. Record filename/hash and concrete design tokens. The design may vary by image job without changing its visual identity.
5. **Approved-image lock:** once a numbered image is approved, do not silently regenerate it while fixing another.

If any conflict occurs, stop the affected asset, document it, and continue only on unaffected assets.

## 3. Rakuten operator's conversion plan

Before design, write a numbered storyboard. For every image record:
- buyer question / purpose, distinct from other images;
- exact verified claim and evidence ID;
- exact Japanese headline, subtitle and small notices;
- actual SKU(s) and corresponding source photo(s);
- suggested composition, scene/cutout technique and mobile reading order;
- no-go details, QA reviewer and status.

The current crispy-squishy test case uses a 12-image shopper narrative **only because this seller requested 12**:
01 hero (butter stick dominant, authentic other SKU supporting); 02 curiosity/sensory interest; 03 visible real shell cracking; 04 hands-on squeeze; 05 another *confirmed* differentiator or substitute meaningful comparison; 06 plausible real usage; 07 authentic detail/print/packaging; 08 confirmed visible features (no invented material); 09 distinct SKU/buying choice clarification; 10 real steps to use; 11 alphabetically indexed SKU choice; 12 actual included contents and purchase notices.
For other products use as many as warranted. No padding, no twelve-panel collage passed off as twelve files.

## 4. Japanese copy editorial gate

The Rakuten senior-operator role prioritizes the buyer question and supported selling points, then Japanese ecommerce-copy role supplies:
- Japanese H1, supporting line and optional notice;
- what source photograph demonstrates the claim;
- prohibited or unverified formulations;
- user-locked versus proposed/approved status.

Examples of *not acceptable without supporting evidence*: `医療効果`, `不安が治る`, `安全素材`, `無臭`, `音が鳴る`, `低反発`, `3歳以上`, `No.1`.
Do not let image models improvise exact text. Prefer deterministic typography compositing and image-text proofread after export.

## 5. Visual system: the seller's approved references

For this *particular test case*, record the seller's approved yellow butter-hand-squeeze hero and the approved **A–D chocolate four-panel SKU image** as two distinct reference anchors. Exact local source filenames or stable links must be supplied in the job reference folder; never pretend an unrelated web search or newly generated sample is an approval.

The approved A–D image is a guide to SKU *layout*: large `SKU早見表` headline, readable `ご注文時にA～Dをご確認ください` ordering message, four balanced cells, large letter badges, clear Japanese item names, dominant real product photograph per cell, playful pink/cream/yellow/chocolate palette, thick outlined display typography and restrained hearts/sparkles. For other blocks E–H and I–L, use the same grid, type treatments, colors and spacing, changing **only** the real product asset, correct letter and label. M is a one-option layout using that same visual identity.

Do not reinterpret E–M as 13 butter colors or invented cartoon characters. Do not rely on image generation to reproduce SKU integrity; cut out and composite the actual photo without changing its shape, colors, cracks, print or packaging.

## 6. Explicit A–M test-case manifest — supplier names, not inferred art direction

| Code | Source sales option | Japanese label draft (verify before release) |
|---|---|---|
| A | 黑巧克力脆皮捏捏 | ブラックチョコ風・単品 |
| B | 粉巧克力脆皮捏捏 | ピンクチョコ風・単品 |
| C | 白巧克力脆皮捏捏 | ホワイトチョコ風・単品 |
| D | 巧克力12个混装【送端盒】随机色 | チョコ風12個ミックス（色ランダム・展示箱付） |
| E | 马卡龙脆皮甜甜圈 | マカロンカラーのドーナツ風・単品 |
| F | 甜甜圈12个【送端盒】 | ドーナツ風12個セット（展示箱付） |
| G | 马卡龙脆皮猫爪 | マカロンカラーの肉球風・単品 |
| H | 猫爪12个【送端盒】 | 肉球風12個セット（展示箱付） |
| I | 脆皮黄油条捏捏 | バター風スクイーズ・単品 |
| J | 脆皮黄油条12个【送端盒】 | バター風12個セット（展示箱付） |
| K | 脆皮粉油条捏捏 | ピンクのバター風・単品 |
| L | 脆皮绿油条捏捏 | グリーンのバター風・単品 |
| M | 脆皮香皂满12【送端盒】随机色 | せっけん風12個セット（色ランダム・展示箱付） |

The Japanese labels above are **editorial drafts** and not locked listing option values. Do **not** infer J's assortment or color distribution from the label. For M, check the exact source wording `满12` and fulfillment before claiming buyer receives a display box. No imagined motifs, colors, materials, measurements, packaging or individual pack count. E–H and M must show their own real category, **not butter bars**.

## 7. Source-image handling and no-redraw rule

Permitted: crop, proportionate resize, product-photo cutout, composite, natural contact shadow, background styling, exact text typesetting.
Forbidden: AI paint-over on the product, remade texture/shell cracks, added toppings/face/prints, changed package artwork, replacement with a better-looking but different stock photo, altering item counts.
Source images may have Chinese supplier annotations or watermarks. Do **not** call such unlicensed/obstructed assets retail-ready. Obtain usable clean licensed photos or a crop that retains the real product and avoids misrepresentation; do not falsify or claim watermark clearance.
If an image-generation backend cannot guarantee product consistency, render only the **background and graphics**, and place the untouched source-photo cutout afterward.

## 8. Per-image QA: all six must pass

1. **Identity:** actual SKU, color, shape, texture, print, packaging, count and accessories match the source.
2. **Copy:** Japanese natural, exactly matches approved copy, legible on smartphone, no invented claims.
3. **Purpose:** answers a distinct buyer question; a product swap or new headline alone is not a new selling point.
4. **Design DNA:** actual comparison against approved reference, including headline, border, palette, spacing and cell composition; no silent new style.
5. **Retail readiness:** no stray Chinese supplier captions, watermark, unreadable label, misleading package count, erroneous dimensions or fabricated certifications.
6. **Export:** correct requested size/format, **one image per file**, verifiable path/name, no twelve-cell contact sheet masquerading as final images.

Each result: `PASS | REWORK | BLOCKED`; cite exact defect and affected image. **Never mark all assets PASS just because JPG files or a ZIP exist**.

## 9. Full-suite gate, version control and delivery

Audit across all images: consistent design, correct sequence, coverage of all distinct selling points and SKU options, no duplicated hero 12 times. Approved images are frozen; rework only rejected numbers. Export individual JPGs at the seller's chosen size (for this test 1000×1000) retaining agreed filenames, then ZIP. Deliver an index with `image_number, filename, message, SKUs_used, source_assets, claim_ids, copy_lock_status, QA_status, version, reviewer_notes`.

Do not automatically post to Rakuten RMS. Final sign-off is human. Do not state a real image is ready if only prompts, concepts, collages, watermarked supplier crops or generated mockups exist.
