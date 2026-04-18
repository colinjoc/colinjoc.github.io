---
title: "Why Ireland doesn't build: the economics of an empty site"
date: 2026-04-18
domain: "Irish Housing"
blurb: "Ireland has enough zoned land for 417,000 homes. Developers file permission for almost none of it. The reason isn't planning — it's arithmetic."
weight: 1
tags: ["housing", "ireland", "viability", "construction-costs", "economics", "zoned-land"]
---

*A plain-language summary. The [full technical paper set](https://github.com/colinjoc/generalized_hdr_autoresearch/tree/main/applications) — six linked studies — has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

*Part 1 of 4 in the Irish Housing series. Next: [Part 2: The pipeline](/hdr/results/irish-housing-pipeline-complete/) | [Part 3: Planning and judicial review](/hdr/results/irish-planning-and-judicial-review/) | [Part 4: What would fix it](/hdr/results/irish-housing-bottleneck-and-levers/)*

**Bottom line.** Ireland has 7,911 hectares of zoned residential land — enough for roughly 417,000 homes at standard densities. On 83 percent of that land, the numbers do not work: sale prices are below the cost of building. Only Dublin apartment schemes are clearly viable. Construction costs in Ireland are not unusually high by European standards, and policy-set costs like VAT and social-housing requirements are only 15 percent of the total. Zeroing every single policy cost would still leave development unviable in all but four of Ireland's 26 counties.

## The question

Ireland's housing shortage is the defining economic story of the last decade. The standard list of villains — slow planning, too much red tape, a cartel of builders, uniquely expensive construction — has been in the public debate for years. We wanted to pull apart each of those claims and ask, with open data, what the economics of building an Irish home actually looks like. Why aren't developers building on land that has already been zoned for housing?

## What we found

![Viability margin by county — sale price minus total development cost, as a percentage of sale price.](plots/viability_map.png)

- There is enough zoned residential land in Ireland for about 417,000 homes. But only around 21,000 residential planning applications get filed each year. The filing rate is just under five applications per hectare per year.
- Across most of Ireland, development is uneconomic. Dublin apartments run a plus-5 percent margin — viable. Dublin houses are at minus 3 percent. The commuter belt is at minus 9 to 11. Secondary cities are at minus 20 to 24. Rural counties sit at minus 60 percent or worse.
- That means roughly 6,580 hectares — 83 percent of zoned land — sits in places where the numbers do not work. This is the single most important fact about Irish housing supply, and it gets almost no airtime in the public debate.
- Construction cost is the dominant driver of viability — about ten times more sensitive than land cost. But Ireland's construction costs are not uniquely high. Ireland's construction price level is exactly the European Union average. Cumulative cost growth from 2015 to 2025 was 41 percent in Ireland, compared to 71 percent in Germany and the Netherlands.
- Labour and materials grew at nearly identical rates over that decade — roughly 4 percent per year each. The common story that "materials are the problem" is an artefact of pandemic-and-war volatility that has since reverted. Labour costs rose steadily and have not come back down.
- Cement is the one material whose price never reverts — it ratchets upward through every crisis at roughly 7 percent a year.
- Energy-efficiency regulations did not drive excess cost inflation. Materials directly affected by the new building-energy standards (insulation, electrical, heating-and-ventilation) actually rose less than unaffected control materials.
- Policy-set costs — VAT, the social-housing requirement, development contributions, the building control regime — total about 15 percent of the cost of an Irish home. Even eliminating all of them makes development viable in only 4 of 26 counties. With realistic VAT pass-through to buyers (about half), zeroing VAT makes zero additional counties viable.
- Infrastructure is a secondary constraint. About a quarter of Ireland's 1,063 wastewater treatment plants are at or over capacity, blocking 950 to 1,700 hectares — 12 to 22 percent — of zoned land. But 83 percent of zoned land is already economically unviable, so fixing the sewage does not help if the numbers still do not work.

## Why that matters

The conventional frame — "Irish housing is blocked by high regulatory costs, slow planning, and uniquely expensive materials" — does not survive contact with the data. Irish construction costs are middle-of-the-pack in Europe. Policy costs are a modest share. Planning and infrastructure are real constraints but secondary ones. The primary constraint is that, outside Dublin, the sum of land plus labour plus materials plus financing plus developer margin exceeds what buyers can pay. That is an economics problem, not a planning problem.

That diagnosis matters because the standard political instruments — VAT cuts, planning-system reform, development-contribution reductions — operate on the 15-percent slice of cost that is policy-set. Zeroing all of them does not move most counties into the viable column. What moves the viability map is the 85 percent that is market cost: construction productivity, labour supply, and the price of cement.

## What it means in practice

**For developers.** The data confirms what your viability models already tell you. Outside Dublin apartments, the numbers do not support private-sector delivery at current prices. The cost-side levers that do move viability — modular construction at roughly 20 percent off hard costs, and workforce expansion that shortens build durations — are the ones worth pushing.

**For policymakers.** The VAT-cut instinct is understandable but empirically weak. Policy costs are a small share of the total and do not move the viability map. The higher-leverage interventions are on the construction-productivity side: modular technology, workforce expansion, and accepting that cement prices will not revert. The "Irish costs are uniquely high" narrative is not supported and should stop anchoring debate.

**For housing advocates.** The land is already zoned. The planning system is not primarily what is holding back supply. The binding constraint is that buyers in most of the country cannot pay what it costs to build. Any serious plan to lift supply outside Dublin has to engage with that number, not with planning or regulation.

## How we did it

This synthesis consolidates six linked studies. We used the [Residential Zoned Land Tax register](https://www.gov.ie/en/publication/8c51e-residential-zoned-land-tax/) for zoned hectares, [Eurostat's construction price level index](https://ec.europa.eu/eurostat/web/construction) for international comparison, [CSO wholesale price series](https://data.cso.ie/) for the materials-and-labour breakdown, and [EPA capacity data](https://www.epa.ie/publications/monitoring--assessment/waste-water/) for infrastructure. We ran county-by-county viability calculations, a tornado sensitivity analysis on cost components, a difference-in-differences test for the effect of energy-efficiency regulations on material prices, and a pass-through simulation for VAT and other policy costs.

## Further reading

- [Zoned land conversion study](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_zoned_land_conversion/paper.md).
- [Viability frontier study](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_viability_frontier/paper.md).
- [International construction cost comparison](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_intl_construction_costs/paper.md).
- [Construction cost decomposition](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_construction_cost_decomp/paper.md).
- [Policy versus market costs](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_policy_vs_market_costs/paper.md).
- [Infrastructure capacity study](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_infra_capacity/paper.md).
