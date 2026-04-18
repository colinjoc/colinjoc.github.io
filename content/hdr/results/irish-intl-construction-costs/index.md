---
title: "Are Irish Construction Costs Really Higher Than Europe?"
date: 2026-04-18
domain: "Irish Housing"
blurb: "No — or at least, not by as much as commonly claimed. Ireland's construction cost index grew 41% from 2015-2025, ranking 6th of 10 EU comparators. Germany (+71%), Netherlands (+71%), and Austria grew significantly faster. On absolute EUR/sqm, Ireland sits near the EU-10 average (rank varies #3-#9 depending on scope assumptions). Eurostat's construction-specific price level index puts Ireland at 99.7 — exactly the EU-27 average. The Irish housing crisis is a supply volume problem, not a construction-cost-per-unit problem."
weight: 9
tags: ["housing", "ireland", "construction-costs", "international-comparison", "Eurostat"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_intl_construction_costs/paper.md).*

## The question

It's commonly said that Irish construction costs are unusually high, and that this explains why Ireland can't build enough homes. **Is that true compared to the rest of Europe?**

## What we found

### Ireland grew slower than the EU average on construction costs

Using Eurostat's quarterly construction cost index for new residential buildings (base 2015=100), Ireland's cumulative growth of **41.3%** over 2015-2025 places it **6th of 10 EU comparators**. Countries that grew faster:

| Country | Cumulative growth 2015-2025 |
|:---|---:|
| Germany | +71.2% |
| Netherlands | +71.2% |
| Austria | +67.0% |
| Denmark | +47.6% |
| Finland | +42.7% |
| **Ireland** | **+41.3%** |
| Belgium | +38.3% |
| Sweden | +36.9% |
| France | +32.1% |
| Spain | +29.8% |

![Construction cost index trajectories for Ireland vs EU comparators. Ireland (thick blue) tracks near or below the EU-9 average (black dashed). Germany and Netherlands diverge sharply upward.](plots/headline_cost_trajectories.png)

### On absolute EUR/sqm, Ireland is near the EU average

Ireland's base construction cost is approximately **€1,975/sqm** (Buildcost.ie Construction Cost Guide). Anchored against known comparator values:

- UK: ~€2,800/sqm (BCIS mid-range, converted at prevailing GBP/EUR)
- Germany: ~€2,500/sqm
- Denmark: ~€2,400/sqm
- Netherlands: ~€2,200/sqm
- **Ireland: ~€1,975/sqm**
- Belgium: ~€1,800/sqm
- Spain: ~€1,400/sqm

Ireland's absolute rank varies **#3 to #9** depending on scope (base cost vs all-in) and exchange-rate assumptions. The Phase 2.75 reviewer correctly flagged that the anchor values aren't perfectly comparable across countries — the range reflects this uncertainty.

### Eurostat's construction price level puts Ireland at exactly 100

Eurostat publishes a construction-specific purchasing power index (PLI) for residential buildings. Ireland's 2024 value is **99.7** — essentially the EU-27 average of 100. By contrast, Ireland's general consumption PLI is 127 (one of Europe's most expensive countries for everyday goods). Construction is the one sector where Ireland is *not* unusually expensive.

### The cost trajectory is cyclical, not structural

Ireland's cost movements track pan-European shocks (COVID supply disruption, Ukraine energy crisis) at below-average intensity. A structural-break analysis finds no Ireland-specific breakpoint — every Irish inflection aligns with a European one. Ireland clusters with Belgium and Sweden on trajectory shape, not with the high-growth DE/NL/AT group.

## What this does NOT establish

- **Not that building is cheap in Ireland.** €1,975/sqm base + site works + fees + VAT = €3,000-4,000/sqm all-in. That's expensive in absolute terms — just not uniquely so.
- **Not that costs don't matter for viability.** The companion [viability study](/hdr/results/irish-viability-frontier/) shows only Dublin apartments are viable. Costs ARE the constraint — they're just not the Ireland-specific, policy-fixable constraint the debate assumes.
- **Not that comparisons are exact.** Anchor values come from different industry sources with different scope definitions. The #3-#9 ranking range is the honest uncertainty band.

## What it means

For policymakers: the narrative "Irish construction costs are uniquely high and that's why we can't build" is not supported by the Eurostat data. Ireland is at the EU average on construction-specific price levels. The binding constraint is supply volume (too few permissions filed, too few applications, too much zoned land in unviable areas) — not per-unit construction cost being out of line with Europe.

For the broader housing story: this finding reinforces the [bottleneck analysis](/hdr/results/irish-housing-bottleneck/). Permission volume is #1. Construction costs are a constraint everywhere in Europe, not an Irish anomaly.

## How we did it

Eurostat STS_COPI_Q construction cost index (41 countries, quarterly, 2002-2025), anchored to absolute EUR/sqm using Buildcost.ie (Ireland), UK BCIS, and industry estimates for 10 comparators. Panel regression with country × time interaction, structural-break detection, cluster analysis, PPP adjustment using Eurostat PRC_PPP_IND construction-specific PLI (not general consumer PPP — a Phase 2.75 correction). Full HDR pipeline with Phase 3.5 signoff.
