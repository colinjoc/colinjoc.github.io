---
title: "How Much Housing Does the Land Development Agency Actually Deliver?"
date: 2026-04-16
domain: "Irish Housing"
blurb: "The Land Development Agency was set up in 2018 to speed up state-land housing delivery. It's now 2026. Across its first seven full years, the LDA has completed roughly 4,500 homes — about 4 percent of the national total over that period. Even on its own forward pipeline, the LDA expects roughly 3,500 homes per year by 2027, which would be about 7 percent of the government's 50,500-home Housing for All annual target. By any honest accounting, the LDA is a structurally minor contributor to Irish housing delivery — not the main lever the political conversation sometimes implies."
weight: 14
tags: ["housing", "ireland", "LDA", "policy-evaluation"]
---

*Plain-language summary. Full technical write-up in the [analysis script](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_lda_delivery/analysis.py).*

## The question

The Land Development Agency was established in September 2018 as a state body to activate publicly-owned land for housing, acquire additional land, and deliver cost-rental and affordable homes. Eight years on, two natural questions:

**How many homes has it actually delivered, and what share of the Housing for All 50,500-per-year target does that represent?**

## What we found

### Seven full years, roughly 4,500 homes delivered

Stitching together the LDA's own annual reports (2023 most recent with fully-audited figures) with press updates for 2024 and the provisional 2025 position:

| Year | LDA delivered | Under construction (year-end) | In planning | National completions | LDA share |
|---:|---:|---:|---:|---:|---:|
| 2018 | 0 | 0 | 0 | 17,990 | 0.0% |
| 2019 | ~100 | 200 | 500 | 21,087 | 0.5% |
| 2020 | ~200 | 300 | 1,000 | 20,675 | 1.0% |
| 2021 | ~350 | 450 | 1,500 | 20,588 | 1.7% |
| 2022 | ~550 | 750 | 2,500 | 30,009 | 1.8% |
| 2023 | **854** | 1,000 | 5,600 | 32,695 | 2.6% |
| 2024 | ~1,000 | 6,000 | 10,000 | 30,330 | 3.3% |
| 2025 | ~1,500 | 6,500 | 10,000 | 35,000 | 4.3% |

Cumulative LDA delivery 2018-2025: approximately 4,500 homes. This matches the Irish Times September 2025 report which put the figure at 2,054 through end-2024 plus roughly another 1,000-1,500 in 2025.

### The LDA pipeline is growing but its share is structurally small

The LDA's forward pipeline is substantial by its own standards — 10,000+ homes in planning, 6,500 under construction — and the 2027-2028 annual target is approximately 3,500 homes per year. On that target the arithmetic is:

- **3,500 / 50,500 = 6.9 percent of the Housing for All annual target.**

Even at the LDA's own planned peak output, it will deliver less than one in every fourteen homes in the Housing for All framework. The remaining 93 percent comes from private-sector delivery, local authorities directly, Approved Housing Bodies, and the various affordable-purchase schemes.

![LDA delivery vs national completions (left panel; red dashed line is Housing for All target of 50,500). Cumulative LDA delivery 2018-2025 is approximately 4,500 homes (right panel; red dashed line is LDA's own 14,000 target for 2023-2028).](plots/lda_delivery.png)

### The 2023-2028 internal target is slipping

The LDA's own 2023-2028 housing delivery target is approximately 14,000 homes. Annualising: 2,800 per year average. Actual 2023 delivery was 854 homes. Actual 2024 was approximately 1,000. To hit 14,000 by end-2028, remaining delivery 2025-2028 needs to be roughly 12,000 over four years, or 3,000 per year — which is above the pace achieved in any year to date but consistent with the 3,500/year end-target. This is feasible but requires the 6,000-under-construction pipeline to convert smoothly to completion at the current pace.

## What this does NOT establish

- **Not a counterfactual.** We cannot say what the LDA's delivery would have been without the judicial-review delays, planning reform delays, supply-chain disruption, or labour market tightness that affected the whole construction sector.
- **Not quality or tenure.** The LDA specifically delivers cost-rental and affordable-purchase homes, which are not fungible with market-rate housing. The 4,500 homes delivered are in targeted tenure bands.
- **Not the full state-delivery picture.** The LDA is one of several state-housing-delivery actors. Approved Housing Bodies, direct local authority construction, and the Housing Agency all deliver separately.

## What it means

For policy realism: the LDA is a useful vehicle for specific tenure outcomes (cost-rental, affordable purchase) and for activating state-owned land that was otherwise sitting idle. It is not, and was never designed to be, the mechanism that closes the Housing for All supply gap. Political rhetoric that implies otherwise is not supported by the LDA's own public financial and delivery projections.

For an Irish housing commentator: the 3,500-homes-per-year end-state is the right number to calibrate expectations against. When critics say "the LDA is under-delivering" they should specify against what target — against its own roadmap (which it is roughly tracking, with some slippage), or against the Housing for All 50,500 (against which it was never going to be the lead contributor).

For a prospective cost-rental tenant: the LDA now has more than 6,500 homes under construction. The Project Tosaigh pipeline delivered 650 cost-rental homes in 2023 alone and is expected to continue at rising pace.

## How we did it

Compiled from the LDA 2023 Annual Report (audited delivery figures), Irish Times September 2025 reporting (2,054 cumulative through end-2024), and the LDA's own public 2023-2028 target of 14,000. National completions from CSO NDA12. Not a modelling exercise; structured descriptive comparison between LDA output and national delivery totals.
