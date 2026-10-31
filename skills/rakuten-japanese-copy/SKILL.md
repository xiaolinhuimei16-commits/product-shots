---
name: rakuten-japanese-copy
description: "Creates, checks, localizes, and manages Japanese copy for Rakuten product images. Supports locked user copy, autonomous copywriting, hybrid copy, mobile-first Japanese typography, and claim verification."
license: MIT
metadata:
  author: repository-owner
  source: custom Rakuten adaptation
  version: "1.0"
---

# Rakuten Japanese Copy

## Mode handling

- Copy-led: reproduce user-supplied copy exactly. Do not rewrite, shorten, translate, or change punctuation without permission.
- Autonomous: write concise, natural Japanese suitable for Rakuten shoppers, based only on confirmed product facts.
- Hybrid: preserve user-supplied core messages; label all AI additions as proposals.

## Japanese quality rules

- Prefer natural contemporary Japanese over literal Chinese-to-Japanese translation.
- Use concise headlines and explanatory subheads.
- Avoid awkward keyword stuffing and excessive exclamation marks.
- Keep terminology consistent across the entire image suite.
- Use kanji, kana, and katakana in a natural balance.
- Avoid overly long lines; design for smartphone reading.
- Distinguish factual specifications from emotional marketing language.

## Claim safety

Never invent:
- Materials, dimensions, weight, quantities, age suitability, certifications, test results, safety claims, compatibility, durability, waterproofing, or performance.
- "No.1", "best", "official", medical, therapeutic, or guaranteed effects without evidence.
- Customer reviews, sales figures, or popularity claims.

If a claim cannot be verified, omit it or mark it as requiring confirmation.

## Copy QA output

For each image, provide:
1. Headline.
2. Supporting copy.
3. Small labels / callouts.
4. English or Chinese meaning for internal review when useful.
5. Source fact supporting each factual claim.
6. Status: user-locked / AI proposal / needs confirmation.

Do not render text into an image-generation prompt as the only source of truth when exact Japanese is required. Prefer generating the visual background/product composition first and typesetting the final Japanese text in a deterministic layout step.
