---
title: "Only one Irish county is close to a profitable housing market"
date: 2026-04-18
domain: "Housing and Real Estate"
blurb: "Try building a typical house for sale in most of Ireland and you will lose money. Not a little. A lot. The culprit is not the one Dublin op-eds blame."
weight: 11
tags: ["ireland", "housing", "viability", "construction", "land", "real-estate"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_viability_frontier/paper.md) has the county-by-county residual-method appraisals and the Monte Carlo sensitivity output. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Across 18 Irish counties with enough data to appraise, just one — Dublin — comes close to a price where a private builder can buy land, build houses, and sell them at a profit. Everywhere else the arithmetic does not close, often by enormous margins, and the dominant reason is construction cost, not land price or regulation.

## The Question

Ireland's housing plan asks for 50,500 new homes a year. The country delivers about 30,000. There are nearly 8,000 hectares of serviced land zoned for housing — space for roughly 263,000 homes at conventional density. The usual explanations for the gap focus on the planning system, on land hoarding, or on regulatory delay. But there is a simpler question underneath them all. If a private developer were to buy a typical piece of zoned land in each Irish county, build standard houses on it, and try to sell them at the local market price, would they make money, lose money, or roughly break even?

We ran the numbers for every county with enough data, using the standard professional method chartered surveyors use for viability assessments.

## What we found

In 17 of 18 counties, the arithmetic does not work. In the 18th, it barely works.

- Dublin sits at a margin of minus 3.1 percent — the cost of building a median new home exceeds the achievable sale price by about three percent.
- Every other county assessed is worse. The commuter belt (Meath, Kildare) is around minus 9 to 11 percent. The regional cities (Cork, Galway, Limerick) are around minus 20 to 30 percent. Rural counties reach minus 60 to 95 percent — costs nearly double the achievable price.
- Construction cost is the dominant lever. It has roughly nine times more influence on the profit margin than land cost. A 15 percent construction-cost cut shifts the national average margin by more than 30 percentage points. A 25 percent land-cost cut shifts it by only 3.4.
- Apartments, at higher density on the same land, come out profitably viable on a national average basis — about plus 5 percent margin — because smaller unit sizes and more units per hectare both work in their favour.
- Planning application rates closely track viability. Where a county's margin improves, planning applications follow almost one-for-one. The correlation is 0.91 across counties.

## Why that matters

The assumption that most overturns here concerns what is actually expensive about an Irish home. Public debate focuses on land — land hoarding, compulsory purchase, the Residential Zoned Land Tax, site assembly. Those are real policy questions. But the viability arithmetic does not put land at the top. Land is about 8 percent of a new home's cost on a national average. Construction — the materials, labour, site works, and professional fees — is roughly 70 percent. Moving the smaller number around does very little. Moving the larger one does a great deal.

The second surprise is the size of the rural gap. It is tempting to assume that low land prices compensate for low sale prices. They do not. The construction cost of a three-bed semi-detached house is not materially lower in Leitrim than in Meath — the bricks, concrete, electrical trade, and plumbing cost the same everywhere. But the Leitrim sale price is less than half the cost of building, so the viability gap widens rather than closes. No realistic policy lever — land reform, tax cut, regulation change — bridges a 95 percent gap. What bridges it is either direct state construction or a large per-unit subsidy.

The third surprise is the apartment finding. In most public debate, apartments are treated as a cost-inflator — expensive, elevator-requiring, harder to deliver than a house. The viability arithmetic points the other way. Apartments at 75 square metres and 100 units per hectare achieve positive margin nationally because higher density dilutes the land cost across more units, and smaller unit size reduces the per-unit construction bill. Where planning permits density, apartments are the typology that closes the viability gap.

## What it means in practice

**For anyone buying or waiting for a new home outside Dublin.** The shortage in your area is not a conspiracy of developers or a failure of planning officials. It is a mathematical gap between the cost of building and the price a buyer can pay. Planning reform cannot close that gap. Nor can tax reform by itself.

**For policymakers.** The picture has a clear structure. Dublin is a marginal commercial market that scale and efficiency can push over the line. The commuter belt needs modest cost reduction — a 15 percent construction-cost cut, plausibly achievable through factory-built housing at scale, brings Meath, Kildare, and Cork into viability. The secondary cities need more. Rural counties cannot be solved by market levers at all, and any serious plan for rural housing supply must involve direct public delivery, cost-rental, or explicit subsidy. There is no single national policy. There are three or four viability zones, each needing a different lever.

**One more implication.** Because construction cost is the dominant lever, policies that reduce it — modern methods of construction, factory building, standardised designs, volume procurement — are worth more than any combination of tax and land-policy changes. Planning reform is not pointless, but without construction-cost reduction it cannot on its own build enough homes.

## How we did it

We applied the standard Royal Institution of Chartered Surveyors residual-method viability appraisal to every Irish county with enough data, using the [Central Statistics Office Residential Zoned Land Prices (RZLPA02)](https://data.cso.ie/table/RZLPA02) for land costs, the [Buildcost.ie H1 2025 Construction Cost Guide](https://buildcost.ie/) for build costs, and the [Central Statistics Office Residential Property Price Index](https://data.cso.ie/table/HPM09) for sale prices. For each county, total development cost was assembled component by component — land, build, site works, professional fees, finance carry, development contributions, Part V obligations, and a required profit margin — and compared against the achievable new-build sale price. A Monte Carlo simulation propagated parameter uncertainty, and a sensitivity analysis ranked the levers by how much each moves the margin. The national average output was validated against an independent Society of Chartered Surveyors Ireland estimate of new-housing delivery costs and came within 0.6 percent.

## Further reading

- [Central Statistics Office Residential Zoned Land Prices (RZLPA02)](https://data.cso.ie/table/RZLPA02) — the zoned-land transaction series.
- [Buildcost.ie Construction Cost Guide H1 2025](https://buildcost.ie/) — the build-cost source.
- RICS (2019). *Assessing Viability in Planning under the NPPF* — the professional guidance for the residual method.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_viability_frontier/paper.md).
