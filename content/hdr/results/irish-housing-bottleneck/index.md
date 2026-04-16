---
title: "Where Does the Binding Constraint on Irish Housing Delivery Actually Sit?"
date: 2026-04-17
domain: "Irish Housing"
blurb: "Meta-analysis across 13 predecessor projects covering the full Irish housing pipeline — from planning permission to occupied home. The binding constraint is permission volume: Ireland grants ~38,000 residential permissions per year but needs ~85,000 to hit the Housing for All 50,500/yr target. No combination of pipeline-efficiency interventions (halving lapse + improving CCC filing + restoring ABP to 18 weeks + removing judicial review entirely) adds more than ~5,000 completions/yr — closing only 31% of the gap. The remaining 69% requires more permissions AND more construction-sector capacity."
weight: 21
tags: ["housing", "ireland", "planning-permission", "bottleneck-analysis", "meta-analysis", "synthesis", "flagship"]
---

*Flagship synthesis. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_housing_bottleneck/paper.md). Synthesises all 13 housing-related projects on this site.*

## The question

Commentators and policymakers cite many reasons Ireland under-delivers housing: slow planning decisions, judicial reviews, permission lapse, construction delays, the LDA's small share, labour shortages. **But which of these is actually the binding constraint — and by how much?**

This meta-analysis combines the findings from 13 predecessor projects on this site into a single quantitative ranking.

## The bottleneck ranking

| Rank | Constraint | Marginal impact | Intervention |
|---:|:---|---:|:---|
| **#1** | **Permission volume** | **+6,100 completions/yr** | per +10,000 permissions granted |
| #2 | Construction-sector capacity | Becomes binding at >58k perms | ~35,000/yr observed ceiling |
| #3 | CCC filing rate | +3,267/yr | per +10 percentage points |
| #4 | ABP decision time | +1,060/yr | restore to 18-week SOP |
| #5 | Judicial review removal | +1,060/yr | (overlaps with #4) |
| #6 | Lapse rate (halved) | +701/yr | from 9.5% to 4.75% |
| #7-8 | Duration reduction, LDA scaling | ~0/yr | shifts timing, not throughput |

**Permission volume is #1 in 100% of 5,000 Monte Carlo parameter draws.** The ranking never swaps under any tested opt-out build rate (50%-100%).

![Left: marginal completions per year from each bottleneck intervention. Right: all efficiency fixes combined close only 31% of the HFA gap.](plots/bottleneck_ranking.png)

## The arithmetic

Ireland grants ~38,000 residential permissions per year. At the opt-out-adjusted build-yield of ~60% (from [S-1](/hdr/results/irish-housing-pipeline-e2e/)), that produces ~23,000 effective completions. The Housing for All target is 50,500. The gap is ~16,300 units per year.

**What efficiency fixes can deliver (combined, with double-count correction):**
- Halve lapse: +701
- Improve CCC filing +10pp: +3,267
- Restore ABP to 18 weeks + remove JR: +1,060 (shared channel)
- **Total: ~5,028 completions/yr = 31% of the gap**

**What requires volume + capacity:**
- Remaining gap: ~11,300 units/yr = 69% of the gap
- This requires approximately 2.2× current permission volume AND addressing the ~35,000/yr construction-sector throughput ceiling

## What this means for policy design

**The single most important finding**: no combination of pipeline-efficiency interventions can close the Housing for All gap. The binding constraint is upstream (not enough permissions being granted) and must be addressed jointly with construction-sector capacity expansion.

This doesn't mean efficiency interventions are worthless — restoring ABP to 18-week compliance and reducing JR friction are worth ~1,000 completions per year each. But framing the housing crisis as a "planning system failure" or a "judicial review problem" misidentifies where the constraint actually sits.

The policy package that works:
1. **Substantially increase permission volume** — zoning reform, density uplift, streamlined application processes
2. **Expand construction capacity** — workforce training, immigration pathways for construction workers, modular/offsite construction
3. **Then** improve pipeline efficiency — faster ABP, fewer JRs, better CCC compliance

In that order. Not the reverse.

## How robust is this?

The ranking survives:
- **All opt-out assumptions** (50%, 70%, 90%, 100% build rate): permission volume stays #1
- **5,000 Monte Carlo draws** propagating CIs from all 13 predecessor projects: #1 rank probability = 100%
- **ABP/JR double-count correction**: combined efficiency revised from 37% to 31% of gap
- The 90% CI lower bound for permission volume (+4,916/yr) exceeds the 90% CI upper bound for CCC filing (+3,712/yr)

## What this does NOT establish

- **Not causation for capacity.** The 35k ceiling is observed throughput, not proven physical capacity. Sufficient demand and profitability might push it higher.
- **Not a policy-ready cost-benefit.** We rank by units/yr, not by cost-effectiveness. The cheapest intervention may not be #1.
- **Not stable over time.** If permissions triple but labour doesn't expand, the constraint shifts to #2 (capacity). Bottlenecks are dynamic.

## The predecessor projects

This meta-analysis synthesises findings from:
- [Housing pipeline](/hdr/results/irish-housing-pipeline/) (aggregate conversion)
- [Commencement cohort](/hdr/results/irish-commencement-cohort/) (232d/498d/962d durations)
- [Lapsed permissions](/hdr/results/irish-lapsed-permissions/) (9.5% non-commencement)
- [LDA delivery](/hdr/results/irish-lda-delivery/) (ca. 850/yr, 3% of HFA)
- [SHD judicial review](/hdr/results/irish-shd-judicial-review/) (87.5% state-loss rate)
- [LRD vs SHD](/hdr/results/irish-lrd-vs-shd-jr/) (data insufficient until ~2027)
- [ABP decision times](/hdr/results/irish-abp-decision-times/) (23→42 weeks)
- [Pipeline yield](/hdr/results/irish-housing-pipeline-e2e/) (35.1% CCC / 59.6% build yield)
- [JR tax on supply](/hdr/results/irish-jr-tax-on-supply/) (105k unit-months direct delay)
- [Courts backlog](/hdr/results/irish-courts-backlog/) (net filing surplus)
- [Graduate emigration](/hdr/results/irish-emigration/) (labour context)
- [Irish gender pay gap](/hdr/results/irish-gender-pay-gap/), [UK gender pay gap](/hdr/results/uk-gender-pay-gap/) (labour market context)

## How we did it

Waterfall accounting model decomposing 38,000 annual permissions through five pipeline stages to effective completions. Five analytical families compared: binomial stage attrition, sensitivity-based ranking, Theory of Constraints, structural equation model, and Monte Carlo simulation (5,000 draws propagating all predecessor CIs). Phase 2.75 blind reviewer mandated opt-out sensitivity sweep, Monte Carlo ranking robustness, ABP/JR double-count audit, and bootstrap CIs. Combined efficiency revised from 37% to 31% after double-count correction. Phase 3.5 signoff cleared.
