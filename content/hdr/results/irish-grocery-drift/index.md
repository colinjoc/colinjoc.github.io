---
title: "Where Did Your Irish Grocery Bill Actually Go Up?"
date: 2026-04-16
domain: "Irish Cost of Living"
blurb: "Irish food prices rose a median 19 percent between January 2022 and January 2026, but the headline number hides enormous dispersion. Sugar went up 51 percent. Beef up 48. Chocolate 46. Milk 39. Butter 38. Fresh meat 36. Bottled water 36. Eggs 33. Meanwhile jams rose 5 percent and fresh seafood just 2. After deflating by average wage growth of roughly 18 percent, all ten worst-hit categories are still 15 to 33 percentage points worse in real terms than wages have delivered. The shock is also historically unusual: seven of those ten categories had been getting cheaper in the four years before 2022."
weight: 7
tags: ["cost-of-living", "ireland", "groceries", "inflation", "CPI"]
---

*Plain-language version. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_grocery_drift/paper.md).*

## The question

If you've noticed your weekly shop is noticeably more expensive than it was a few years ago, the Central Statistics Office consumer-price data agrees with you. The headline "food inflation" number between January 2022 and January 2026 is about 19 percent — median across all food and non-alcoholic-beverage categories. That's already a lot. But the headline hides the story.

The real question is **which specific categories got most expensive, whether the rise is unprecedented or just more of the same, and how much of it has been matched by your pay going up**.

## What we found

### The categories with the biggest price shocks

Using CSO table CPM24, which tracks the Consumer Price Index at roughly 74 separate food subcategories, here are the ten worst hit over January 2022 to January 2026:

| Subcategory | Nominal rise 2022 → 2026 | Real rise (after wage growth) |
|---|---|---|
| Cane and beet sugar | **+51%** | +33% |
| Beef | **+48%** | +30% |
| Chocolate and cocoa products | +46% | +28% |
| Whole milk | +39% | +21% |
| Butter and dairy-derived oils | +38% | +20% |
| Fresh meat (all) | +36% | +18% |
| Bottled water | +36% | +18% |
| Soft drinks | +35% | +17% |
| Eggs | +33% | +15% |
| Sugar, confectionery, desserts | +33% | +15% |

At the other end of the distribution, some categories barely moved: fresh fruit rose 9 percent, jams rose 5 percent, fresh seafood rose just 2 percent. Your grocery inflation experience is basically a function of what's in your basket.

![Price indices for the worst-hit food subcategories since 2020. The red dashed line marks the Russian invasion of Ukraine in February 2022. All six categories were broadly flat before the shock and roughly tripled their previous trend line after it.](plots/top_food_subcategories.png)

### The shock is historically unusual

For seven of those top-ten categories, the pre-shock trajectory was **negative**. Between January 2016 and January 2020, sugar got 15 percent cheaper, beef got 6 percent cheaper, chocolate got 16 percent cheaper, bread got 6 percent cheaper, eggs got 9 percent cheaper. The 2016-to-2020 four-year window was a cheap-food period. The shock that began in 2022 is not a continuation of any pre-existing trend — it is a clean break from the prior pattern.

The "shock multiple" — how much bigger the 2022-2026 rise is than the 2016-2020 rise — is often mathematically undefined (the denominator was negative) or sits at three to eight times when both are positive.

### All the top ten categories outpaced wages

CSO Average Weekly Earnings nominal growth between 2022 Q1 and 2025 Q4 is approximately 18 percent. Every single one of the top-ten food categories rose more than 18 percent. In real (wage-deflated) terms, the worst categories cost 15 to 33 percentage points more than your pay covered. For a household whose basket over-indexes on sugar, beef, chocolate, dairy, meat, bottled water, soft drinks, or eggs, grocery costs have outpaced wages by a meaningful double-digit share over four years.

### Some of the rise is global. A lot of it is not

The two most-hit categories — sugar and chocolate — are globally-determined. World sugar futures and world cocoa futures both ran large rallies across 2022-2026, and the Irish retail pass-through is broadly consistent with commodity-market moves. If you eat a lot of those two things, the story is mostly the global commodity market.

But six of the top ten categories are locally-determined: whole milk, butter, fresh meat, bottled water, soft drinks, and eggs. These are Irish-produced and Irish-bottled. Their 33-to-39 percent rises cannot be explained by imported commodity inflation. The candidate explanations are: energy-cost pass-through into processing, labour-cost pass-through (Irish minimum wage rose roughly 30 percent over the same period), packaging-cost pass-through, or genuine margin expansion among Irish food processors. This analysis does not distinguish between them.

## What we cannot say from this data

- **Supermarket-level dispersion is invisible.** The CSO consumer-price index is a weighted average across retail outlets. It does not let us ask whether Aldi and Lidl held the line while the incumbent supermarkets did not. Answering that requires shelf-price microdata from Kantar or trolley.ie.
- **No causal attribution.** Whether the rise in locally-determined categories is energy, wages, packaging, or margin — or all four — is not answerable from CPI alone.
- **No cross-country benchmark.** UK ONS publishes the same-structure data (COICOP 01.1.x). A side-by-side comparison with the UK would separate "global pass-through" from "Ireland-specific".

## What we can say

For a household: the dispersion is the story. The 19-percent food-median headline masks a distribution that ranges from +2 percent on seafood to +51 percent on sugar. The actual impact on your household depends entirely on what you buy. The households hit hardest are the ones who eat a lot of dairy, meat, and sugar-containing products — which covers, broadly, households with children. Households that eat less of these and more fruit, vegetables, and fish have been broadly protected in real terms.

For policy: the fact that locally-determined categories rose as much as globally-determined ones suggests domestic cost-pass-through or domestic-margin expansion contributes significantly to Irish grocery inflation over and above the imported component. The obvious policy lever — targeted VAT cuts — affects the entire basket proportionally and doesn't address dispersion. A more effective intervention would target the categories that rose more than imported commodity inflation can explain, which this analysis narrows down but does not fully identify.

## How we did it

We downloaded CSO table CPM24 (Consumer Price Index by 344-way ECOICOP-v2 commodity classification, monthly 1996-2026) via the CSO's PxStat JSON-stat API, filtered to the 74 food and non-alcoholic-beverage subcategories, indexed each series to January 2020 = 100, and computed four-year growth across two windows (2016-01 → 2020-01 as baseline, 2022-01 → 2026-01 as shock). Endpoint-sensitivity envelopes use 91 pairs per category drawn from a ±6-month window. Global-vs-local classification is rule-based. Wage deflation uses approximate CSO Average Weekly Earnings nominal growth of 18 percent. Code and reviewer-mandated robustness are in the linked paper.
