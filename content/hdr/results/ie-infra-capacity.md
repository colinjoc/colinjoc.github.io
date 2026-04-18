---
title: "The Sewer Plants That Sterilise a Fifth of Ireland's Housing Land"
date: 2026-04-18
domain: "Housing and Infrastructure"
blurb: "Ireland has nearly 8,000 hectares of land zoned for homes, yet roughly one in five of those hectares sits in a sewer catchment whose treatment plant cannot accept any new connections. Three-quarters of the full-up plants have no upgrade scheduled, and about a sixth of all zoned land is blocked by both the sewer constraint and the cost constraint at once — undevelopable under any realistic scenario."
weight: 11
tags: ["ireland", "housing", "infrastructure", "water", "planning", "policy"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_infra_capacity/paper.md).*

## The Question

Ireland is short of homes. The usual explanations — slow planning, expensive construction, cautious developers — are all real, but each assumes that if the zoning and the permissions and the builders lined up, a home could actually be built. That assumption has a hidden dependency: the sewer. Before a new estate can connect to the public network, the national water utility has to confirm that the downstream treatment plant has spare capacity. If the plant is full, the connection is refused and planning stalls.

We set out to measure how big that hidden constraint actually is. Of the roughly 7,900 hectares zoned for housing in Ireland, how much sits in a catchment where the treatment plant simply cannot take any more?

## What We Found

The constraint is large, concentrated, and mostly unscheduled for relief.

- About a quarter of Ireland's 1,063 public wastewater treatment plants are at capacity or nearly so.
- Translating that to land, roughly 1,500 hectares of zoned residential land — about one-fifth of the national total — sit in constrained catchments.
- Seventy-four percent of the plants flagged as full have no upgrade project in the water utility's investment pipeline.
- About 1,265 hectares (one-sixth of all zoned land) are "double-stranded" — sitting simultaneously in a constrained catchment and on land that is economically unviable to build on at today's construction costs. These hectares need both a plant upgrade and a cost or price shift before a home can be built.
- Cork accounts for the largest absolute block of constrained land (about 305 hectares). Kerry has the highest share of full plants (42 percent). Dublin's big treatment plant at Ringsend is fine, but the separate project that was meant to unlock growth in north and west Dublin has slipped from 2025 to an estimated 2032.

## Why That's Surprising

The finding that cuts hardest against intuition is the double-stranding. It is well known that Ireland has a viability problem — construction costs are high relative to sale prices in much of the country — and the sewer constraint has been discussed in isolation. Put the two together and a subset of the land emerges that is blocked twice over. For those hectares, fixing the sewer plant does nothing on its own, because the economics still do not work; shifting the economics does nothing on its own, because the sewer still cannot accept the connection. Only solving both constraints at the same location at the same time releases the land. That is a much higher bar than solving either one.

The second surprise is how uneven the plant classifications look against headline perceptions. Dublin, frequently described as the epicentre of the infrastructure crisis, has a low treatment-plant constraint rate — a legacy of the large Ringsend upgrade that completed recently. Kerry, far from the policy spotlight, has the highest constraint rate in the country. The mismatch is real but partly misleading: the sewer network of pipes and pumping stations in Dublin is under severe strain too, and that strain is not visible in the treatment-plant register used here. The register is explicit that it covers plants only, not pipes.

A third surprise concerns the pipeline. Of the 164 plants classified as full, only 42 have an upgrade scheduled. The rest — 122 plants — are simply waiting, with no project, no date, and no budget line. Any new home in those catchments depends on an upgrade that has not yet begun its planning cycle, and sewer-plant upgrades typically take seven to fifteen years from identification to operation.

## What It Means

For a buyer or developer, the practical implication is that the public sewer plant serving a site is a first-order question, worth checking before anything else. The water utility publishes a traffic-light register per county, updated periodically, and a red classification at the serving plant means no new significant connections can be confirmed — regardless of whether the site is zoned, permitted, or economically viable.

For national policy, the analysis produces a shortlist of specific plants whose upgrade would unlock the most zoned land. That shortlist fits directly into the water utility's EUR 10.3 billion capital plan for 2025 to 2029 and into the housing-supply strategy. The reframing is useful: the housing shortage has often been debated as a planning, cost, or developer problem, but in about a quarter of catchments a prior physical constraint applies. Building a home there is not slow or expensive — it is, for the moment, impossible.

Beyond Ireland, the pattern matches what the United Kingdom has seen with nutrient-neutrality rules (an estimated 145,000 homes blocked) and the Netherlands with nitrogen limits (around 23,000 homes forgone), and sits alongside New Zealand's ongoing reform of water-sector financing. The shared lesson across those four cases is that water infrastructure is the first system to bind when housing demand accelerates and the slowest to unbind when it does.

## How We Did It

The primary data came from the [Uisce Éireann Wastewater Treatment Capacity Register](https://www.water.ie/connections/developer-services/wastewater-capacity-register/), which classifies every public treatment plant as green, amber, or red, together with the national planning applications register covering 491,206 records across 31 planning authorities. We matched treatment-plant catchments to counties, combined those shares with county-level zoned-land estimates from the Goodbody 2021 study, and produced a range of blocked-hectare estimates under conservative (red-only), central, and plant-size-weighted definitions. We layered the result onto an independent viability analysis of the same zoned land to identify the double-stranded subset, and benchmarked the pattern against comparable infrastructure-driven housing blocks in the United Kingdom, the Netherlands, and New Zealand. All inputs are real, publicly accessible datasets; no synthetic data was used.

## Further Reading

- [Uisce Éireann Wastewater Treatment Capacity Register](https://www.water.ie/connections/developer-services/wastewater-capacity-register/) — the per-county red / amber / green classification
- [Uisce Éireann Strategic Funding Plan 2025-2029](https://www.water.ie/) — the EUR 10.3 billion capital programme that would fund the missing upgrades
- Goodbody (2021). *Analysis of Zoned Residential Land in Ireland* — the 7,911-hectare zoned-land baseline
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_infra_capacity/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
