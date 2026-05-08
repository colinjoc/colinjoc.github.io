---
title: "Irish construction costs: it isn't really the materials"
date: 2026-05-08
domain: "Construction economics"
blurb: "Over a decade, Irish materials and labour costs grew at almost the same rate. The headlines blamed the wrong villain."
weight: 45
tags: ["ireland", "housing", "construction", "inflation", "policy", "nzeb"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_construction_cost_decomp/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Between 2015 and 2024, Irish residential construction materials inflated at almost exactly the same rate as construction labour — about four percent a year. The popular story that "materials prices are the problem" is largely an artefact of Covid-era volatility. The structural frame, structural steel and cement, is the single biggest contributor to cost growth, and the tighter energy regulations introduced in 2019 do not show up in unit prices once you compare like with like.

## The question

Ireland needs roughly ninety-three thousand new homes a year and built only thirty thousand in 2024. Politicians, builders and homebuyers all point at construction cost as the binding constraint. But "construction cost" is not one number. It is concrete and steel and timber and insulation, plus electricians and bricklayers and plant hire, plus a long tail of professional fees, land, finance, value-added tax and developer margin. To intervene in the right place, you need to know which component is actually moving the dial — and how much of any recent jump is the underlying trend versus a passing shock.

This study takes the Central Statistics Office's monthly index of forty wholesale building-material prices, lines it up against quarterly construction labour costs, and decomposes the past decade into its component drivers.

## What we found

The headline number — about four percent annual inflation in construction materials over 2015 to 2024 — hides enormous variation. Structural steel grew by roughly seven point eight percent a year. Plaster, cement and precast concrete were not far behind. At the other end, glass barely moved at half a percent a year, despite a regulatory mandate for triple glazing. The gap between the fastest- and slowest-growing material is a factor of sixteen.

The most striking finding is also the simplest. Wholesale materials prices and construction hourly labour costs grew within zero point zero four percentage points of each other across the full decade. Their trajectories are different — materials spiked sharply during Covid and again after the invasion of Ukraine and partly reverted, while labour rose steadily and did not — but the ten-year averages are almost indistinguishable.

A statistical decomposition of the forty material series finds that just three latent factors explain ninety percent of the price variance. The dominant factor, accounting for more than four-fifths of the variance, is a "rising tide" that lifts almost everything together. The second separates domestically-quarried minerals from internationally-traded metals and timbers; the third separates finished manufactured products from bulk commodities.

Combining cost shares with growth rates, the structural frame — steel and concrete — emerges as the single largest contributor to overall cost growth, even though it is not the largest line item in a typical bill of quantities.

The result that most surprised us came from the regulatory analysis. A naive comparison of the period before and after the 2019 Nearly Zero Energy Building rules looks damning: insulation, glass, heating-ventilation-and-air-conditioning equipment and electrical fittings all show two to nearly five percentage points of excess inflation per year after the regulation took effect. But when those materials are compared against a control group of materials untouched by the regulation — cement, structural steel, plaster, concrete blocks — the control group accelerated even more. On a like-for-like basis, the regulation-affected materials inflated less than the unaffected ones. The naive pre-versus-post story was being driven by Covid and the energy shock, not by the rules.

<figure>
  <img src="plots/weighted_contribution.png" alt="Weighted contribution of each construction trade to annual hard-cost inflation, with the structural frame leading at over half a percentage point per year.">
  <figcaption>Weighted contribution of each trade to annual hard-cost inflation. The structural frame (steel plus concrete) is the largest single contributor.</figcaption>
</figure>

## Why that matters

Three things follow from this. First, public debate has overweighted the materials story and underweighted the labour story. Headlines naturally chase the most volatile series, and timber prices doubling during Covid are far more dramatic than the steady, year-on-year creep in tradesperson hourly rates. Yet across the decade the two contributed almost identically, and the labour increases have not reverted.

Second, the persistent inflation in cement and structural steel reflects very different mechanisms. Steel prices are set in international commodity markets dominated by Chinese production; Irish builders are price-takers. Cement is the opposite — it is too heavy to import economically, so its price is set by domestic demand against finite local capacity. After both Covid and Ukraine, cement prices kept rising rather than reverting, suggesting a structural floor rather than a passing spike.

Third, blaming the energy-efficiency regulations for soaring construction costs does not survive a proper control comparison. That does not mean the regulations are free — thicker insulation, triple glazing and heat pumps mean more material per dwelling, and a wholesale price index per unit of material cannot see that quantity effect. The Sustainable Energy Authority of Ireland separately estimates a one-off uplift of roughly two percent of total construction cost from the regulation, which is consistent with a quantity-driven rather than a price-driven mechanism.

## What it means in practice

**For homebuyers.** The price you pay is not being driven mainly by a single runaway material. The biggest single driver is the structural frame — a global commodity exposure — and a steady, decade-long climb in labour costs that policymakers cannot easily wish away.

**For builders.** Material price hedging makes sense for steel and timber, where shock-driven volatility is real and partly reverts. It is far less useful for cement, where the price floor seems to keep rising. Designs that swap structural steel for engineered timber or that reduce concrete content can shift the cost-share away from the fastest-inflating commodity.

**For policymakers.** Two of the most popular targets for cost-control intervention — "materials inflation" as a general phenomenon, and the energy-efficiency rules — are not the right targets. Skills shortages in the trades, which feed directly into the labour-cost trajectory, look more like the structural problem. So does cement supply capacity. Both are slow-moving levers; neither is glamorous.

## How we did it

The analysis uses the [Central Statistics Office](https://www.cso.ie/) Wholesale Price Index for Building and Construction Materials — a panel of forty material price indices observed monthly since 2015 — together with the Earnings, Hours and Employment Costs Survey for the construction sector. We computed compound annual growth rates for each material, ran a principal-component analysis to identify the latent factors, applied a structural-break test to confirm that Covid (March 2020) and the Ukraine invasion (February 2022) were genuinely distinct regimes, and combined trade-level cost shares from the Society of Chartered Surveyors Ireland and Buildcost industry guides with material-specific inflation rates to build the weighted contribution analysis.

For the regulatory question, we used a difference-in-differences design: comparing materials directly affected by the 2019 standard (insulation, glass, heating-ventilation-and-air-conditioning equipment, electrical fittings) against a control group of materials whose use and specification were not changed by the rules. All data is real public-sector microdata downloaded from the StatBank application programming interface; no synthetic data was generated.

## Further reading

- [CSO Wholesale Price Index for Building and Construction Materials (WPM28)](https://data.cso.ie/table/WPM28)
- [CSO Earnings, Hours and Employment Costs Survey (EHQ03)](https://data.cso.ie/table/EHQ03)
- [Society of Chartered Surveyors Ireland — Tender Price Index](https://scsi.ie/)
- [Sustainable Energy Authority of Ireland — Nearly Zero Energy Building guidance](https://www.seai.ie/)
- Davy (2024), *Ireland requires 93,000 new homes per year to 2031*
- Full technical write-up and reproducible code: [hdr_autoresearch repository](https://github.com/colinjoc/hdr_autoresearch/tree/main/applications/ie_construction_cost_decomp)
