---
title: "Where in Ireland Can You Actually Build a House at a Profit?"
date: 2026-04-17
domain: "Irish Housing"
blurb: "Most of Ireland is unviable for residential development at current costs and prices. Only Dublin apartment schemes clear the viability hurdle (+5.1% margin). Dublin houses are marginal (-3.1%), the commuter belt is moderately unviable (-9 to -11%), secondary cities are clearly unviable (-20 to -24%), and rural counties are deeply unviable (-60% or worse). About 6,580 of Ireland's 7,911 hectares of zoned residential land sit in areas where the numbers don't work. Viability margin correlates r=0.91 with planning application rates — confirming that developers aren't filing where it doesn't pay."
weight: 5
tags: ["housing", "ireland", "development-viability", "construction-costs", "upper-funnel"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_viability_frontier/paper.md).*

## The question

The [zoned-land study](/hdr/results/irish-zoned-land-conversion/) found that Ireland has enough zoned land for 417,000 homes but only files ~21,000 residential applications per year. The [bottleneck analysis](/hdr/results/irish-housing-bottleneck/) identified permission volume as the #1 constraint. But **why don't developers apply?**

The most likely answer: it doesn't pay. If the cost of building a home exceeds its sale price, no rational developer files a planning application — regardless of how much zoned land exists or how fast the planning board decides.

## What we found

### The viability equation

For each county we computed:

**Total development cost** = Land cost per unit + Construction cost (€1,900-2,050/sqm base + €225/sqm site works + 12% professional fees) + Finance cost (7% on 60% drawdown) + Development contributions + 15% profit margin

**Sale price** = CSO median residential property price by region

**Viability margin** = (Sale price - Total cost) / Sale price

### Most of Ireland is unviable for standard housing

| Area | Viability margin | Verdict |
|:---|---:|:---|
| Dublin apartments (high density) | **+5.1%** | Viable |
| Dublin houses | -3.1% | Marginal |
| Meath (commuter) | -9.2% | Moderately unviable |
| Kildare (commuter) | -11.2% | Moderately unviable |
| Cork city | -19.5% | Clearly unviable |
| Galway city | -23.7% | Clearly unviable |
| Rural counties | -60% to -95% | Deeply unviable |

Only Dublin apartment-density schemes consistently clear the viability bar. Standard houses in Dublin are right on the edge. Outside the capital, the numbers don't work at market prices and current construction costs.

![Viability margin by county — Dublin apartments are the only consistently viable segment. Most zoned land sits in unviable areas.](plots/headline_finding.png)

### 6,580 hectares of zoned land are economically stranded

Of Ireland's 7,911 hectares of zoned residential land, approximately **6,580 hectares (83%) sit in areas where development is unviable** at current costs and prices. That's roughly 263,200 potential housing units that exist on paper but cannot be profitably built.

### Construction cost is the dominant factor — 10x more sensitive than land cost

A tornado sensitivity analysis shows that a ±15% swing in construction cost moves the viability margin more than any other variable — roughly 10x the impact of a ±25% swing in land cost. This matters for policy: land-price interventions (RZLT, CPO, state land) are less effective than construction-cost interventions (modular building, labour supply, materials competition).

### Viability predicts application rates almost perfectly

The correlation between county-level viability margin and planning-application intensity (from the companion [zoned-land study](/hdr/results/irish-zoned-land-conversion/)) is **r = 0.91**. Developers file applications where the numbers work and don't where they don't. This closes the loop on the [bottleneck analysis](/hdr/results/irish-housing-bottleneck/): the reason permission volume is low isn't planning barriers or land supply — it's that development is uneconomic in most of the country.

## What this does NOT establish

- **Not that homes can't be built.** 30,000+ homes were built in 2025. But many are one-off self-builds (different cost structure), social housing (state-subsidised), or apartments in Dublin (the one viable segment).
- **Not that viability is fixed.** Construction costs, sale prices, and state subsidies all change. A 15% reduction in construction cost would make the commuter belt viable.
- **Not the full cost picture.** We use Buildcost.ie's Construction Cost Guide figures, cross-validated against SCSI benchmarks (within 0.6%). Actual costs vary by site, design, and contractor.

## What it means

For policymakers: the housing supply problem is fundamentally an economics problem. Zoning more land, speeding up planning boards, and reducing judicial reviews don't help if the arithmetic doesn't work. The three highest-leverage interventions are:
1. **Reduce construction costs** — modular/offsite construction, workforce expansion, materials competition
2. **Increase effective sale price** — state subsidies for affordable housing, cost-rental support, shared-equity schemes
3. **Increase density** — apartment schemes are viable where houses are not

The RZLT (taxing zoned land) addresses land hoarding but cannot force development where the numbers are negative.

## How we did it

Residual viability appraisal per county combining CSO HPM09 (sale prices by region), CSO RZLPA02 (land prices by county), Buildcost.ie H1 2025 cost guide (construction costs per sqm), and CSO BEA04 (construction production index for time-series). Phase 2.75 blind reviewer caught a calibration error (rebuild costs used instead of construction costs, overstating cost by 19%) — corrected, now cross-validates against SCSI 2023 within 0.6%. Full HDR pipeline with Phase 3.5 signoff.
