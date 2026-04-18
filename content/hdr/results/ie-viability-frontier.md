---
title: "Only Dublin Is Close to a Profitable Irish Housing Market"
date: 2026-04-18
domain: "Housing and Real Estate"
blurb: "Across 18 Irish counties with enough data to test, just one — Dublin — comes close to a price where a builder can buy land, build houses, and sell them at a profit. Everywhere else, the numbers do not close, often by huge margins, and the main reason is not land prices or regulations but the sheer cost of construction itself."
weight: 11
tags: ["ireland", "housing", "viability", "construction", "land", "real-estate"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_viability_frontier/paper.md).*

## The Question

Ireland's housing plan asks for 50,500 new homes a year and delivers about 30,000. There are nearly 8,000 hectares of serviced land zoned for housing — space for roughly 263,000 homes at a conventional density. The usual explanations for the gap focus on the planning system, on land hoarding, or on regulatory delay. But there is a simpler question underneath all of them. If a private developer were to buy a typical piece of zoned land in each Irish county, build standard houses on it, and try to sell them at the local market price, would they make money, lose money, or roughly break even?

We ran the numbers for every county for which there is enough data, using the standard professional method that chartered surveyors use for viability assessments.

## What We Found

In 17 of 18 counties, the math does not work. In the 18th, it barely works.

- Dublin sits at minus 3.1 percent margin — the cost of building a median new home exceeds the achievable sale price by about three percent.
- Every other county assessed is worse. The commuter belt (Meath, Kildare) is around minus 9 to 11 percent. The regional cities (Cork, Galway, Limerick) are around minus 20 to 30 percent. Rural counties reach minus 60 to 95 percent — costs nearly double the achievable price.
- Construction cost is the dominant constraint, with nine times more influence on the profit margin than land cost. A 15 percent cut in construction cost shifts the national average margin by more than 30 percentage points; a 25 percent cut in land cost shifts it by only 3.4 percentage points.
- Apartments, at higher density on the same land, come out profitably viable on a national average basis — about plus 5 percent margin — because smaller unit sizes and more units per hectare both work in their favour.
- Planning application rates closely track viability. Where a county's viability margin improves, planning applications follow almost one-for-one. The correlation is 0.91 across counties.

## Why That's Surprising

The finding that overturns the most assumptions concerns what is actually expensive about an Irish home. The headline debate is about land — land hoarding, compulsory purchase, the Residential Zoned Land Tax, site assembly. Those are real policy questions, but the viability arithmetic does not put land at the top. Land, on the national average, is about 8 percent of a new home's cost. Construction — the materials, the labour, the site works, and the professional fees — is roughly 70 percent. Moving the smaller number around does very little; moving the larger one does a great deal.

The second surprise is the size of the rural gap. It is easy to assume that low land prices compensate for low sale prices in rural counties. They do not. The construction cost of a three-bed semi-detached house is not much lower in Leitrim than in Meath; the bricks, the concrete, the electrical trade, and the plumbing cost the same everywhere in the country. But the sale price in Leitrim is less than half the cost of building, so the viability gap widens rather than closes. No realistic policy lever — land reform, tax cut, regulation change — bridges a 95 percent gap. What bridges it is either direct state construction or a large per-unit subsidy.

The third surprise concerns the apartment finding. In most of the public debate, apartments are treated as a cost-inflator — expensive, elevator-requiring, harder to deliver than a house. The viability arithmetic points the other way. Apartments at 75 square metres and 100 units per hectare achieve positive margin nationally, because the higher density dilutes the land cost across more units, and the smaller unit reduces the per-unit construction bill. Where planning permits high density, apartments are the typology that closes the viability gap.

## What It Means

For someone buying or waiting for a new home outside Dublin, the most practical implication is that the shortage in their area is not a conspiracy of developers or a failure of planning officials — it is a mathematical gap between the cost of building and the price a buyer can pay. Planning reform cannot close that gap. Nor can tax reform by itself.

For policymakers, the picture has a clear structure. Dublin is a marginal commercial market that scale and efficiency can push across the line. The commuter belt needs modest cost reduction — a 15 percent construction-cost cut, plausibly achievable through factory-built housing at scale, brings Meath, Kildare, and Cork into viability. The secondary cities need more. Rural counties cannot be solved by market levers at all, and any serious plan for rural housing supply must involve direct public delivery, cost-rental, or explicit subsidy. There is no single policy; there is a different policy in each of three or four viability zones.

There is one more implication worth stating plainly. Because construction cost is the dominant lever, policies that reduce construction cost — modern methods of construction, factory building, standardised designs, volume procurement — are worth more than any combination of tax and land-policy changes. The finding is not that planning reform is pointless; it is that planning reform without construction-cost reduction cannot, on its own, build enough homes.

## How We Did It

The analysis applied the standard Royal Institution of Chartered Surveyors residual-method viability appraisal to every Irish county with enough data, using the [Central Statistics Office Residential Zoned Land Prices (RZLPA02)](https://data.cso.ie/table/RZLPA02) for land costs, the [Buildcost.ie H1 2025 Construction Cost Guide](https://buildcost.ie/) for build costs, and the [Central Statistics Office Residential Property Price Index](https://data.cso.ie/table/HPM09) for sale prices. For each county, total development cost was assembled component by component — land, build, site works, professional fees, finance carry, development contributions, Part V obligations, and a required profit margin — and compared against the achievable new-build sale price. A Monte Carlo simulation propagated parameter uncertainty, and a sensitivity analysis ranked the levers by how much each one moves the margin. The national average output was validated against an independent Society of Chartered Surveyors Ireland estimate of new-housing delivery costs and came within 0.6 percent.

## Further Reading

- [Central Statistics Office Residential Zoned Land Prices (RZLPA02)](https://data.cso.ie/table/RZLPA02) — the zoned-land transaction series
- [Buildcost.ie Construction Cost Guide H1 2025](https://buildcost.ie/) — the build-cost source
- RICS (2019). *Assessing Viability in Planning under the NPPF* — the professional guidance for the residual method
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_viability_frontier/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
