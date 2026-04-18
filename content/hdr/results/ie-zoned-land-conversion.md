---
title: "Ireland has land zoned for 417,000 homes — and nobody is building on it"
date: 2026-04-18
domain: "Housing and Land Use"
blurb: "The housing shortage has a twin: a vast stock of zoned, serviced land sitting idle. A new tax was meant to flush it into the market. It hasn't."
weight: 13
tags: ["ireland", "housing", "planning", "zoned-land", "tax", "policy"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_zoned_land_conversion/paper.md) has the local-authority breakdown and the pre- and post-tax comparison. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Ireland has nearly 8,000 hectares of land zoned and serviced for new homes — enough for about 417,000 dwellings. Each year, only 8.6 percent of that capacity enters the planning pipeline. A 2024 tax designed to force idle zoned land into the market has produced no detectable effect in its first two years. And a single local authority with 44 percent of the national zoned stock is filing the lowest application rate in the country.

## The Question

Ireland's housing debate has two puzzling numbers side by side. The country has a severe shortage of new homes, but it also has about 7,900 hectares of land that is already zoned for housing, serviced with water and roads, and sitting without active planning permission. That is enough land for roughly 417,000 homes at the densities local plans anticipate — many years of delivery at the official Housing for All target. The supply is there, on paper. What is missing is the decision to build.

We asked a simple, under-studied question. Of that 7,900 hectares, how much generates a planning application in a given year? And where the answer is low, what is actually holding the land back — planning delays, regulation, infrastructure, or economics?

## What we found

Only a small share of zoned land converts to a planning application in any given year, and the reasons are economic rather than administrative.

- The national rate is about 2.72 residential planning applications per hectare of zoned land per year. That works out to about 8.6 percent of the zoned capacity entering the pipeline annually. At that pace, the current stock would take about 19 years to fully exhaust.
- The Residential Zoned Land Tax, announced in 2021 to flush idle zoned land into the market, has produced no detectable effect in its first two years. Residential application volumes actually fell by 7.1 percent from the pre-announcement average, though the change is not statistically significant.
- Regional variation is stark. The Southern region files 3.65 applications per hectare per year, the East-and-Midlands 3.09, and the Northern-and-Western region only 1.63 — less than half the rate of the other two.
- A single local authority, Fingal, accounts for 44 percent of the national zoned-land stock but files only 0.08 applications per hectare per year, the lowest rate in the country. The 3,519-hectare Fingal figure uses a broader definition than the national survey, so it probably overstates the true residential-only stock, but even with that caveat Fingal is a major national bottleneck.
- Once the Fingal outlier is set aside, counties with more zoned land do file more applications (correlation 0.64). The "zoned land does not predict applications" headline in earlier analyses was a single-county artefact.
- The average application is tiny — median one unit, mean 2.8 — and 44 percent are single one-off houses. Applications for 50 or more units exist but are uncommon.

## Why that matters

The tax result is the one that most cuts against recent policy expectations. The Residential Zoned Land Tax was explicitly designed on the theory that if holding land becomes expensive, owners will either build or sell to someone who will. Ireland imposed a 3 percent annual levy on the market value of undeveloped zoned land, with the first liability arising in 2024. Standard real-options theory predicts this shifts the optimal moment to build. The data, so far, does not. Applications have not risen; if anything they have drifted slightly downward. The tax may bite as the liability accumulates, or the 3 percent rate may simply be too small to overcome the value of waiting when a scheme is only marginally viable — the difference between 1.26 times cost and 1.20 times cost, which is where many Irish schemes sit.

The second surprise is how little the traditional "planning system" explanations survive the decomposition. Approval rates, decision lags, and refusal rates — the variables usually blamed for slow housing delivery — show no significant relationship with how many applications a local authority receives per hectare. Whatever holds back applications, it is not fear of being refused or of waiting too long for a decision. That points the finger elsewhere: at whether building makes money, at whether the water and transport connections physically exist, and at whether the owner prefers to hold.

The third surprise is the dominance of one-off single-house applications. On an average day, nearly half of all residential planning applications in Ireland are for a single house — often a family home on an inherited or purchased parcel. This fits a behavioural pattern familiar from the real-options literature: develop the minimum, preserve the option on the rest. Large multi-unit schemes, which would actually drain the zoned-land stock, are much rarer than the zoning alone suggests they should be.

## What it means in practice

**For homebuyers and renters.** The reason new homes are scarce in most counties is not missing zoning or refused applications. The zoning exists. The refusals are rare. What is missing is the decision by landowners to bring schemes forward, and that decision is driven by whether the scheme will earn enough to justify the risk. Where national average viability sits at 1.26 times cost — a thin margin that barely covers land, contributions, and a conventional profit — the economics tell owners to wait, and they wait.

**For policymakers.** The analysis points to three practical levers. The first is Fingal: 44 percent of the national zoned stock sits in one local authority with the lowest application rate in the country. Understanding what is blocking Fingal — water and sewer connections, ownership structure, or something else — has more potential than any uniform national policy. The second is viability. At 1.26 times cost, the national economics are fragile. Modest construction-cost increases could tip the country further away from activation, and modest reductions could trigger a disproportionate rise in applications. The third concerns the Residential Zoned Land Tax. A 3 percent holding cost is not yet moving the needle against the option value of waiting for better economics, and the design may need revisiting.

**For the public narrative.** The 50,500-home target implies roughly 85,000 planning applications a year at current pipeline yield. Ireland is running at about 21,500. Closing the gap requires the national application intensity to roughly quadruple — from 2.72 applications per hectare per year to about 10.74. No regional convergence scenario gets there. The target, as currently defined, may require more land, more public-sector direct delivery, or a structural change in viability economics.

## How we did it

We combined the full national planning register — 491,206 applications from 2012 through 2026 — with the [Goodbody (2024) Residential Land Availability Report](https://www.gov.ie/en/publication/08bbf-residential-land-availability-report-2024/), which quantifies zoned and serviced residential hectares by region, and the [Central Statistics Office zoned-land price series (RZLPA02)](https://data.cso.ie/table/RZLPA02) and residential property-price data. Each application was classified as residential using keyword matching on the development description and the residential-units field. We computed application intensity at national, regional, and local-authority levels, tested for a pre- and post-announcement effect of the new land tax, and ran five model families — simple ratios, panel regressions, survival analysis, logistic classification, and spatial autocorrelation — to decompose the variation across counties. All inputs are real public data; no synthetic figures were used.

## Further reading

- [Central Statistics Office Residential Zoned Land Prices (RZLPA02)](https://data.cso.ie/table/RZLPA02) — the county-level land-price series.
- [Goodbody Residential Land Availability Report (2024)](https://www.gov.ie/en/publication/08bbf-residential-land-availability-report-2024/) — the national zoned-and-serviced hectare estimate.
- [Revenue Commissioners — Residential Zoned Land Tax](https://www.revenue.ie/en/property/residential-zoned-land-tax/index.aspx) — the 2024 tax whose early effects are tested here.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_zoned_land_conversion/paper.md).
