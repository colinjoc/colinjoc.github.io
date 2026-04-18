---
title: "Your grocery bill went up 19 percent. Unless it went up 51."
date: 2026-04-16
domain: "Irish Cost of Living"
blurb: "The headline Irish food-inflation number hides a distribution that runs from plus two percent to plus fifty-one. What you eat decides which one you got."
weight: 27
tags: ["cost-of-living", "ireland", "groceries", "inflation", "CPI"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_grocery_drift/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Between January 2022 and January 2026, Irish food prices rose a median 19 percent. But the median is an average that hides the story. Sugar rose 51 percent. Beef rose 48. Chocolate 46. Milk 39. Butter 38. Meanwhile fresh seafood rose 2 percent and jams rose 5. After accounting for the roughly 18 percent nominal wage growth over the same period, the worst-hit categories cost between 15 and 33 percentage points more in real terms than wages covered. And the shock is a clean break from history — seven of the ten worst-hit categories had been getting cheaper in the four years before 2022.

## The question

If your weekly shop feels meaningfully more expensive than it did a few years ago, the official data agrees with you. The median Irish food-inflation figure for January 2022 through January 2026 is 19 percent. That is already a lot. But a headline average is not how anyone actually experiences inflation. The real question is which specific categories got most expensive, whether the rise is unprecedented or just a continuation of a pre-existing trend, and how much of it has been matched by pay going up.

## What we found

![Price indices for the worst-hit food subcategories since 2020. The dashed line marks the Russian invasion of Ukraine in February 2022. All six categories were broadly flat before the shock and roughly tripled their trend line after it.](plots/top_food_subcategories.png)

- Sugar rose 51 percent, beef 48, chocolate 46, milk 39, butter 38, fresh meat 36, bottled water 36, soft drinks 35, eggs 33, confectionery 33. The top ten categories are clustered tightly at one-third-or-more real-price increases.
- After deflating by nominal wage growth of roughly 18 percent, every one of those ten categories is still 15 to 33 percentage points worse in real terms than pay has delivered.
- The shock is not a continuation of anything. Across 2016 to 2020, seven of these ten categories were actively getting cheaper. Sugar got 15 percent cheaper. Beef got 6 percent cheaper. Chocolate got 16 percent cheaper. Eggs got 9 percent cheaper. The 2022 break is clean.
- At the other end of the distribution, your grocery bill depends on your basket. Fresh fruit rose 9 percent, jams 5, fresh seafood just 2. If you eat a lot of fruit, vegetables and fish, you have been broadly protected in real terms.
- About half the shock is global. Sugar and chocolate track world commodity futures almost exactly — those prices are decided in London and Chicago, not Dublin.
- The other half is not. Milk, butter, fresh meat, bottled water, soft drinks and eggs are Irish-produced and Irish-bottled. Their 33-to-39 percent rises cannot be explained by imported commodity inflation. The candidates are energy pass-through, labour pass-through (Irish minimum wage rose roughly 30 percent over the same period), packaging pass-through, or margin expansion among Irish food processors. This analysis does not separate them.

## Why that matters

The standard policy response to food inflation — a targeted cut to value-added tax — affects the entire basket proportionally. It does not address the dispersion. A household that eats mostly fruit, vegetables and fish benefits almost identically to a household that lives on dairy, meat and sugar. But the first household has barely been hit and the second has been hit hard. Blanket VAT cuts are a poor instrument for a problem that lives in the tails of the distribution, not in the mean.

The locally-determined half of the story is the more interesting one. Global sugar and cocoa markets explain why sugar and chocolate got expensive. They do not explain why Irish whole milk rose 39 percent. Whatever is driving the locally-produced categories is inside the Irish supply chain — it has not been priced in from abroad.

## What it means in practice

**For households.** The dispersion is the story. Look at what you buy. If your basket is heavy on dairy, meat and sugar-containing products — which covers most households with children — you have been hit much harder than the 19 percent headline. If your basket is heavy on fruit, vegetables and fish, the real-terms damage is small.

**For policymakers.** The fact that locally-determined categories rose as much as globally-determined ones suggests domestic cost pass-through or domestic margin expansion is contributing materially, over and above imported inflation. Targeted VAT cuts are a blunt instrument against a problem this unevenly distributed. Interventions aimed at the categories that rose more than imported commodities can explain would be closer to the right lever.

**For journalists.** The 19 percent median is not a lie, but it is misleading as a shorthand for what households experienced. Reporting on food inflation should lead with the dispersion, not the mean.

## How we did it

We used the Central Statistics Office's consumer price index at commodity-subcategory resolution (74 food and non-alcoholic-beverage subcategories within [table CPM24](https://data.cso.ie/table/CPM24)), pulled monthly from 1996 to 2026 via the PxStat JSON-stat API. We indexed every series to January 2020 equals 100, computed four-year growth across two windows — 2016 to 2020 as a pre-shock baseline and 2022 to 2026 as the shock — and ran endpoint-sensitivity checks using 91 pairs per category drawn from a plus-or-minus six-month window. Global-versus-local classification is rule-based. Wage deflation uses CSO Average Weekly Earnings nominal growth.

## Further reading

- [CSO Consumer Price Index (table CPM24)](https://data.cso.ie/table/CPM24) — the source dataset.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_grocery_drift/paper.md).
