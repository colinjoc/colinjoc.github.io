---
title: "Where in Ireland can a developer actually build housing at a profit?"
date: 2026-05-08
domain: "Housing economics / Development viability"
blurb: "Ireland has zoned land for 263,000 homes and a target of 50,500 a year. On the median numbers, only one county pencils out — and barely."
weight: 32
tags: ["housing", "Ireland", "viability", "construction-cost", "land-economics", "RICS", "CSO", "policy", "real-data"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_viability_frontier/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** On real Irish land, construction, and sale-price data, the median three-bed semi-detached house is unviable to build in seventeen of eighteen counties — total development cost exceeds the achievable sale price by about a third. Dublin is the sole marginal case, and the binding constraint is construction cost, not land.

## The question

Ireland's Housing for All plan targets 50,500 new homes a year. Delivery in 2024 came in at 30,330 — barely sixty percent of target, and down on the previous year. The standard explanation is planning dysfunction: too few permissions, too many delays, too much regulation. But there is an economic question underneath that nobody can wave away. If a developer buys a serviced site, builds houses, and sells them at the going price, do the numbers add up?

The Royal Institution of Chartered Surveyors has a standard answer to that question — the residual method. We applied it to every Irish county for which the data exists, using the Central Statistics Office's first systematic dataset of zoned residential land transaction prices, the Buildcost.ie Construction Cost Guide for the first half of 2025, and Central Statistics Office property price data calibrated to end-2025.

## What we found

The headline is stark. The national weighted-average viability margin — sale price minus all-in development cost, expressed as a percentage of sale price — comes in at minus thirty-one percent. On the median land, at the median sale price, with industry-standard cost assumptions, total development cost exceeds the achievable sale price by about a third.

The picture is a gradient, not a uniform crash.

- Dublin sits at minus three percent — marginal but workable for projects that sell above the median, which is most Dublin projects. Consistent with Dublin being the most active construction market in the country.
- The commuter belt — Meath at minus nine percent, Kildare at minus eleven — is close enough to viability that a modest cost reduction would close the gap.
- Secondary cities — Cork at minus twenty, Galway at minus twenty-four, Limerick at minus thirty — sit in territory no market mechanism can bridge without help.
- Rural and remote counties are off the chart. Leitrim's break-even sale price exceeds the local median by one hundred and fifteen percent.

The single most important finding sits underneath all of that. Construction cost dominates. A fifteen percent move in construction cost shifts the national margin by thirty percentage points. A twenty-five percent move in land cost shifts it by three. That is a nine-to-one sensitivity ratio. Land hoarding, the policy obsession of the past five years, addresses about a tenth of the actual problem.

Two more findings deserve weight. First, viability margin correlates with planning application rate at r equals 0.91 across counties — the supply shortfall tracks the economics, not the planning system. Second, apartment-density schemes — seventy-five square metres at one hundred units a hectare — cross into positive territory at a national margin of plus five percent, while the same arithmetic on a one-hundred-and-ten-square-metre house at forty units a hectare gives minus thirty-one. The shift toward apartments and duplexes that has been visible in completion statistics is not a fashion. It is the only geometry that pencils.

## Why that matters

The policy conversation in Ireland has spent a decade circling land — Residential Zoned Land Tax, compulsory purchase, state land banks. Those instruments target the smallest lever in the equation. At the national-average all-in construction cost of about €2,460 per square metre on a one-hundred-and-ten square metre unit, construction alone consumes seven-tenths of the median sale price before land, finance, contributions, or developer profit are added. You cannot tax your way out of that with a levy on undeveloped sites.

The RICS framework is not exotic — it is what valuers use in court. Plugging Irish numbers into it produces an answer that is both unsurprising in retrospect and starkly absent from the public debate. Estate housing, on median land, at median prices, does not work. The fact that any homes get built at all reflects four mechanisms: above-median sale prices in Dublin, the shift to apartments, state cost-rental and direct-build programmes, and developers using land banked before the current price cycle.

## What it means in practice

**For homebuyers.** If you are looking outside Dublin and the immediate commuter belt, the structural reason new estates are scarce is that they cannot be built profitably at the prices the market will pay. That is not going to change without either a substantial fall in construction cost or a substantial rise in sale prices.

**For developers.** The numbers favour two strategies. Density — apartments and duplexes spread land cost over more units and shrink the per-unit construction bill. And scale — the model shows two-hundred-unit schemes outperform ten-unit schemes by about twelve percentage points of margin, through procurement and overhead efficiency.

**For policymakers.** The single highest-leverage intervention is construction cost reduction. International experience with factory-built housing suggests achievable savings of twenty to thirty percent. A fifteen percent reduction alone makes three counties viable. A combined package — eliminating Part V obligations, waiving development contributions, cutting construction costs by fifteen percent, and accepting a fifteen percent developer margin — gets four counties (Dublin, Meath, Kildare, Cork) into the viable column. It still leaves fourteen counties out. For those, no market mechanism closes the gap. Direct state construction or per-unit subsidies of €50,000 to €150,000 are the only tools that work.

The cost-rental programme — at €1,200 a month capitalised at four-and-a-half percent — is independently viable on the model with no subsidy. That is a meaningful endorsement of the cheapest route the state has to closing the gap in places where the market simply will not.

## How we did it

We applied the residual-method viability appraisal — the framework set out by the Royal Institution of Chartered Surveyors — to every Irish county with sufficient transaction data, computing for each the difference between achievable sale price and total development cost (land, construction, site works, professional fees, finance, development contributions, developer profit). Land prices come from the Central Statistics Office's RZLPA02 series, the first systematic dataset of zoned residential land transactions in Ireland — n = 355 transactions across 35 counties and regions in 2024. Construction costs come from the Buildcost.ie Construction Cost Guide for the first half of 2025, with regional ratios applied from the Society of Chartered Surveyors Ireland Rebuilding Guide. Sale prices come from the Central Statistics Office's residential property price index, calibrated to end-2025.

The model's national-average all-in development cost reproduces the Society of Chartered Surveyors Ireland 2023 published delivery cost benchmark to within one percent — a useful external check that the framework is anchored to industry numbers, not invented ones. A Monte Carlo simulation across uncertain parameters produces a viable outcome in 38.5 percent of draws nationally and a near-certain viable outcome for Dublin at above-median sale prices. An earlier version of this analysis used the wrong construction-cost reference — the Society of Chartered Surveyors Ireland House Rebuilding Guide, which is calibrated for insurance reinstatement after demolition rather than new build on serviced land. Switching to the Construction Cost Guide is what produced the gradient described here.

## Further reading

- Crosby N and Wyatt P. "Financial viability appraisals for site-specific planning decisions." *Environment and Planning C* (2016). The standard academic treatment of the residual method as applied to planning.
- Society of Chartered Surveyors Ireland (2023). *The Real Cost of New Housing Delivery.* The benchmark our calibration is checked against.
- Central Statistics Office. *Residentially Zoned Land Prices (RZLPA02), 2024.* The first systematic dataset of zoned land transactions in Ireland.
- Central Bank of Ireland (2023). *Rising Construction Costs and the Residential Real Estate Market.* Independent corroboration of construction cost as the binding macro constraint on Irish housing supply.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_viability_frontier/paper.md).
