---
title: "Can Policy Fixes Make Irish Housing Viable? Not Really."
date: 2026-04-18
domain: "Irish Housing"
blurb: "Policy-set costs (VAT, Part V, development contributions, BCAR compliance, planning fees) make up only about 15% of total residential development cost. Even eliminating ALL of them makes only 4 of 26 counties viable — and once price pass-through is accounted for (VAT savings flow partly to buyers, not developers), zeroing VAT alone makes zero additional counties viable. The median viability gap of €144,000 per unit far exceeds total policy costs of €70-100k. Ireland's housing viability crisis is fundamentally a market-cost problem — construction labour and materials, not government levies."
weight: 8
tags: ["housing", "ireland", "construction-costs", "policy", "viability", "VAT", "Part-V"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_policy_vs_market_costs/paper.md).*

## The question

Politicians and industry groups frequently call for VAT reductions, Part V reform, and lower development contributions to make housing development viable. **How much of the total cost is actually policy-set, and would halving or eliminating these costs change the viability picture?**

## What we found

### Policy costs are only 15% of total development cost

For a representative Dublin 3-bed semi-detached (110 sqm, €592k total development cost):

| Component | Amount | % of total | Type |
|:---|---:|---:|:---|
| Materials + labour | ~€255k | 43% | Market |
| Land | ~€47k | 8% | Market |
| Developer margin | ~€77k | 13% | Market |
| Finance | ~€36k | 6% | Market |
| Professional fees | ~€52k | 9% | Market |
| **VAT (13.5%)** | **~€45k** | **7.6%** | **Policy** |
| **Development contributions** | **~€25k** | **4.2%** | **Policy** |
| **Part V obligation** | **~€20k** | **3.4%** | **Policy** |
| **BCAR compliance** | **~€5.5k** | **0.9%** | **Policy** |
| **Planning fees** | **~€1.5k** | **0.3%** | **Policy** |
| **Total policy** | **~€97k** | **16.4%** | |

### Eliminating ALL policy costs makes only 4 of 26 counties viable

| Scenario | Counties that become viable |
|:---|---:|
| Zero VAT (no pass-through) | 3 (Dublin, Wicklow, Kildare) |
| Zero VAT (50% pass-through to buyers) | **0** |
| Abolish Part V entirely | 0 |
| Halve development contributions | 0 |
| Abolish BCAR | 0 |
| **All policy costs zeroed** | **4** (Dublin, Wicklow, Kildare, Meath) |

The Phase 2.75 reviewer caught a critical point: if VAT is reduced, the benefit partially flows to buyers via lower sale prices, not to developers via wider margins. With 50% pass-through, zeroing VAT makes **zero** additional counties viable.

### The viability gap dwarfs policy costs

The median per-unit viability gap (from the companion [viability study](/hdr/results/irish-viability-frontier/)) is **€144,000**. Total policy costs per unit are €70-100k. Even eliminating every government levy leaves a €44-74k gap. The problem is construction cost (materials + labour = 43% of total), not policy.

### What would actually work?

The experiments tested increasingly radical interventions:

| Intervention | Additional counties viable |
|:---|---:|
| Modular construction (-20% hard costs) | 2 |
| CPO land at agricultural price | 2 |
| All policy zeroed + modular + CPO land | 9 of 26 |
| €50k per-unit subsidy | 3 |
| €150k per-unit subsidy | 15 |
| €200k per-unit subsidy | 24 |

Only direct per-unit subsidies at scale (€150k+) or combined radical interventions (modular construction + compulsory land purchase + policy zeroing) make a meaningful number of counties viable. No single policy lever does it.

## What this does NOT establish

- **Not that policy reforms are pointless.** Zeroing VAT saves €45k/unit — real money for buyers even if it doesn't fix developer viability.
- **Not that the market is efficient.** Developer margins at 15-20% are partly convention; affordable-housing schemes operate at 6-8%.
- **Not that costs are fixed.** Modular construction, workforce expansion, and materials innovation could reduce hard costs over time.

## What it means

For policymakers: stop framing housing viability as a "reduce the levies" problem. Policy costs are 15% of total; the gap is 30-40% of total. The interventions that move the needle are structural: construction-workforce expansion (C-1 found labour is the steady-state cost driver), modular/offsite manufacturing, and direct subsidies where viability fails.

For the Housing for All framework: a national viability gap fund covering 33,000 completions/yr at €144k/unit would cost ~€4.4 billion annually. That's the honest number.

## How we did it

Decomposed total development cost into 10 components using Buildcost.ie trade-level data, CSO RZLPA02 (land), and published fee/levy schedules for 26 counties. Classified each as policy-set or market-driven. Ran 20 counterfactual scenarios testing each policy lever individually and in combination. Phase 2.75 blind reviewer mandated a price-pass-through experiment (E31) — with 50% pass-through, the VAT headline collapses from 3 to 0 counties viable. Full HDR pipeline with Phase 3.5 signoff.
