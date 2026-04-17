---
title: "What Actually Drives Irish Construction Costs?"
date: 2026-04-18
domain: "Irish Housing"
blurb: "Labour and materials grew at nearly identical rates over 2015-2025 (~4%/yr each). The narrative that 'materials are the problem' is an artifact of COVID/Ukraine volatility — materials spiked and partially reverted; labour rose steadily without reverting. Cement is the only major material that ratcheted upward through both crises without mean-reverting. NZEB energy-efficiency regulations did NOT drive excess material inflation — a difference-in-differences analysis shows NZEB-affected materials (insulation, electrical, HVAC) actually rose LESS than control materials (+3.5pp vs +7.6pp)."
weight: 7
tags: ["housing", "ireland", "construction-costs", "materials", "labour", "NZEB"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_construction_cost_decomp/paper.md).*

## The question

The [viability study](/hdr/results/irish-viability-frontier/) found that construction cost is the dominant viability lever — 10x more sensitive than land cost. But what drives construction cost? Is it materials? Labour? Regulation? And which components grew fastest?

## What we found

### Labour and materials grew at the same rate — ~4%/yr each

Over 2015-2025, the materials CAGR was 3.99%/yr and the labour CAGR was 4.03%/yr — a difference of 0.04 percentage points. The common narrative that "material costs are the problem" is an artifact of crisis volatility:

- **Materials**: spiked dramatically during COVID (+25% peak) and Ukraine/energy crisis (+15% peak), then partially reverted
- **Labour**: rose steadily at ~4%/yr without any spike or reversion — a structural trend driven by skilled-trade shortages

The cumulative effect is similar, but labour's trajectory is more concerning because it doesn't mean-revert.

### Top-5 cost drivers by weighted contribution

| Rank | Component | Share of cost | Growth rate | Weighted contribution |
|---:|:---|---:|---:|---:|
| 1 | Frame & upper floors | 12% | 4.71%/yr | 0.57pp/yr |
| 2 | Mechanical services (HVAC + plumbing) | 14% | 3.12%/yr | 0.44pp/yr |
| 3 | Substructure (cement-heavy) | 8% | 5.20%/yr | 0.42pp/yr |
| 4 | External walls & cladding | 10% | 4.04%/yr | 0.40pp/yr |
| 5 | Preliminaries / site overhead | 10% | 4.03%/yr | 0.40pp/yr |

![Weighted contribution of each cost component to total construction cost growth.](plots/weighted_contribution.png)

### Cement is the one material that never reverts

Cement grew at 6.83%/yr — the fastest sustained rate of any major material — and uniquely ratcheted upward through both the COVID and Ukraine crises without reverting. Timber spiked +70% during COVID but mean-reverted to -21% below peak. Steel fell 8%/yr. Cement just kept going up.

### NZEB regulations did NOT drive excess cost inflation

This was the biggest surprise. A difference-in-differences analysis comparing NZEB-affected materials (insulation, electrical fittings, HVAC, glass) against control materials (concrete, steel, timber) found:

- NZEB-affected materials: +3.5pp excess inflation post-regulation
- Control materials: +7.6pp excess inflation (from COVID/Ukraine)
- **DiD = -4.0pp** — NZEB materials rose LESS, not more

This reverses the common narrative that building regulations drove up costs. The energy-efficiency supply chain (insulation, heat pumps, triple glazing) scaled more efficiently than traditional materials during the crisis period. Glass barely moved at all (0.48%/yr) despite the triple-glazing mandate — supply adapted.

### The apparent productivity collapse is a measurement artifact

An earlier draft reported that "employment doubled while output grew only 9%." The Phase 2.75 reviewer caught this: the BEA04 production volume index (+9%) is deflated and does not track physical output. CSO dwelling completions went from ~15,000 to ~36,000 over the same period (+140%). The productivity decline was an index-measurement issue, not a real finding.

## What this does NOT establish

- **Not installed cost per sqm.** WPM28 tracks input material prices, not the installed cost including labour, waste, and specification changes (e.g., thicker walls for NZEB).
- **Not quantity-adjusted.** If NZEB requires 30% more insulation per dwelling, the total insulation spend rises even if the price per unit is flat. We measure price, not quantity.
- **Not a forecast.** Cement's 6.83%/yr trend may not continue; timber's mean-reversion may not either.

## What it means

For policymakers: the cost story is about labour, not materials and not regulation. Labour costs rise steadily without reverting; materials spike but come back. NZEB regulations scaled the energy-efficiency supply chain effectively. The highest-leverage cost intervention is construction-workforce expansion, not regulatory rollback.

For the viability analysis: the 4%/yr construction-cost CAGR is a structural trend. If house prices don't keep pace, more counties will cross the unviability line each year — the viability frontier is moving outward.

## How we did it

Decomposed CSO WPM28 (40 material price indices, monthly 2015-2025) and EHQ03 (construction labour costs, quarterly) into component-level contributions using share × growth-rate weighting from Buildcost.ie cost guides. Three PCA components explain 90% of material-price variance. Difference-in-differences for NZEB impact using pre/post regulation with material-type treatment/control. Full HDR pipeline with Phase 2.75 blind reviewer (caught BEA04 measurement artifact and NZEB confounding) and Phase 3.5 signoff.
