---
title: "Irish housing: policy costs aren't the binding constraint"
date: 2026-05-08
domain: "Housing economics — Ireland"
blurb: "Strip every levy, tax and social-housing rule from new Irish homes and 22 of 26 counties still cannot break even."
weight: 45
tags: ["housing", "ireland", "policy", "viability", "construction-costs"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_policy_vs_market_costs/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Government-set costs — value-added tax, social-housing obligations, development levies, building-control compliance, planning fees — make up only about 16 percent of what it costs to deliver a new Irish home. Even if every one of them were abolished tomorrow, only four of the country's 26 counties would become commercially viable for speculative housing.

## The Question

Anyone following the Irish housing debate has heard a recurring claim: the reason private developers cannot deliver enough homes is that the state has piled costs onto every site — the 13.5 percent value-added tax on new build, the Part V requirement to hand 20 percent of a scheme to the local authority at cost, development contributions, building-control rules, planning fees. Strip those back, the argument runs, and supply will follow.

This study asked the question the way an accountant would. For a representative three-bedroom semi-detached, a two-bedroom apartment, a four-bedroom detached and a three-bedroom terrace, in each of the 26 Republic of Ireland counties, we built the full cost stack from the ground up — materials, labour, site works, land, finance, professional fees, developer margin, and every separately listed government charge — and asked which counties would actually clear the viability threshold under each reform scenario.

## What we found

Policy-set costs come in between 13 and 17 percent of total development cost across the country, with a median of about 15.5 percent. The other 83 to 87 percent is market-driven: materials are roughly 23 percent of the total, labour 20 percent, developer margin 13 percent, land 7 to 8 percent, finance 6 percent.

Of the policy levers, value-added tax does the heavy lifting. Zeroing it saves around EUR 45,000 per Dublin unit and is the only single policy change that pushes any county across the viability line — Wicklow, Dublin and Kildare, three counties out of 26, become marginally viable under the optimistic assumption that sale prices stay put. Halving every policy cost achieves the same three counties. Zeroing every policy cost adds only one more county, Meath, for a total of four.

The optimism matters. The headline result above assumes developers pocket every euro of saving. The tax-incidence literature suggests at least some of any cost cut flows through to buyers as lower prices. Under a 50 percent pass-through assumption — half to buyers, half to developers — zeroing value-added tax makes zero counties viable, and zeroing the entire policy stack makes only three.

The viability gap — the per-unit subsidy needed to make each county pencil out — has a median of EUR 144,289 and runs as high as EUR 225,873 in Longford. The total bill of all policy costs combined is between EUR 70,000 and EUR 100,000 per unit. The gap is bigger than the entire policy stack in most of the country.

Even the most aggressive combined reform we modelled — modular construction shaving 20 percent off hard costs, compulsory purchase of land at agricultural prices, and complete elimination of every policy cost — makes only nine counties viable.

## Why that matters

The framing that "the state is making housing unaffordable through its own charges" is not wrong on the margin, but it is wrong on the scale. Even the most generous interpretation of policy reform leaves 22 of 26 counties unable to deliver speculative housing. The binding constraint is the cost of building a home — bricks, blocks, timber, steel, electricians, plumbers, finance — and the price of the land underneath it.

That has direct implications for what works and what doesn't. A national viability gap fund big enough to make all counties viable at the government's 33,000-completions-per-year target would cost about EUR 4.4 billion annually. That is the size of the hole when you add up the actual numbers, rather than assuming policy reform will close it.

## What it means in practice

**For homebuyers.** Don't expect a tax cut to translate directly into a cheaper house. Tax incidence research, and the supply-constrained shape of the Irish market, both predict that part of any saving is capitalised into land and existing-stock prices rather than reaching the buyer.

**For builders.** The policy-cost line on a feasibility study is real but not the binding line. The numbers that move viability are the same ones that move every other construction project on the planet: tender rates, productivity, finance terms, and the price you pay for the site.

**For policymakers.** Value-added tax is the only policy lever with material reach, and even it doesn't solve viability outside Dublin's commuter ring. The big numbers sit on the market side. Direct delivery routes — the Land Development Agency, Approved Housing Bodies, local-authority direct build — operate at margins of 6 to 8 percent rather than the 15 percent commercial benchmark, and that margin compression alone moves more units than zeroing development contributions. The state's choice of delivery model is itself the most powerful "policy lever" once you stop drawing the policy-market line at the standard place.

## How we did it

Construction costs were taken from the Buildcost.ie H1 2025 guide, which publishes tender rates per square metre by dwelling type and region using Society of Chartered Surveyors Ireland methodology. We applied a 0.85 scheme factor to convert from one-off rebuild rates to multi-unit scheme costs. Land prices came from Central Statistics Office dataset RZLPA02 (residentially zoned land prices by county, 2024). Material and labour cost trajectories came from CSO datasets WPM28, EHQ03 and BEA04. Sale prices came from the Property Price Register.

Policy-cost parameters came from primary sources: the Revenue Commissioners for value-added tax, the Planning and Development Act 2000 for Part V, published local-authority development contribution schemes, RIAI and SCSI surveys for building-control compliance costs, and Statutory Instrument 600/2001 for planning fees. The model was calibrated against the SCSI benchmark for a EUR 400,000 dwelling (53 percent hard costs, 47 percent soft) and reproduces hard-cost shares of 50 to 53 percent across locations, inside the calibration band.

Viability is defined as a positive margin between achievable new-build sale price and total development cost, with all components included. We ran scenarios in which each policy lever was halved or zeroed individually, then in combinations, then alongside market-side reforms (land at compulsory-purchase prices, modular construction, margin compression). Sensitivity to the pass-through assumption was tested at 50 percent. The cross-subsidy effect of Part V was computed at scheme level rather than assumed.

The study has limits worth naming. It is a static model — it does not solve the supply-demand equilibrium that would tell you how many homes get built once costs change. Land-price data are county medians from small transaction volumes. Density assumptions matter and vary by scheme. None of those limitations change the central arithmetic: the policy share of total cost is too small to be the binding constraint, and the gap between sale prices and full development cost is too large for policy reform to close on its own.

## Further reading

- Buildcost.ie (2025). Construction Cost Guide H1 2025.
- Society of Chartered Surveyors Ireland (2021). Viability Study: Apartment Development in Dublin.
- Crossley, Phillips & Sherwood (2012). The Effect of Value-Added Tax on House Prices. Journal of Public Economics.
- Glaeser & Gyourko (2018). Tax Policy and Housing Supply. Journal of Urban Economics.
- Norris & Shiels (2007). Part V: An Assessment.
- Royal Institution of Chartered Surveyors (2019). Financial Viability in Planning.
