---
title: "Where Do Irish Housing Permissions Actually Go?"
date: 2026-04-16
domain: "Irish Housing"
blurb: "Between 2019 and 2025 Irish planning authorities granted permission for roughly 267,000 housing units. In the same window, 167,000 houses were actually completed. We compare the two CSO series — permissions (BHQ15) and completions (NDA12) — to ask how much of the permission flow is being converted into finished homes. The two-year aggregate conversion ratio climbs from 41 percent in 2019 to 65 percent in 2022, but pre-2019 CSO data (BHQ16) show 2016-2017 conversions of 77-86 percent, so the 2019-22 rise is best read as a recovery from a COVID-era trough, not as a move above the pre-COVID baseline. Permissions themselves have been roughly flat at 32-43 thousand per year — still the number that would have to rise to hit the government's 50,500-home annual target."
weight: 12
tags: ["housing", "ireland", "planning-permissions", "housing-crisis"]
---

*Plain-language summary. Full technical write-up in the [analysis script](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_housing_pipeline/analysis.py). Retroactively revised on 2026-04-15 to surface reviewer-flagged methodological caveats.*

## The question

Every month the press reports a "housing permissions" number, usually comparing it to the government's 50,500-home-per-year target under Housing for All. These are two very different numbers: permissions are what councils and An Bord Pleanála say developers are allowed to build, and completions are what actually got built. The gap between them is a mix of objections, finance, labour, materials, design revisions, and straight-up developer delay.

**Are Irish permissions actually getting built, or is the system stockpiling approvals that never produce houses?** And has that changed as the housing crisis has intensified?

A note on framing: we do **not** observe the whole construction pipeline. We compare two end stages — permissions granted and completions recorded — and never see the middle stage (commencement notices, which are held by the Department of Housing, not CSO PxStat). So what follows is a permission-vs-completion comparison with a lag, not a cohort-traced pipeline.

## What we found

### Permissions vs completions, year by year

Central Statistics Office tables BHQ15 (planning permissions 2019-2025, with a strategic-vs-non-strategic split) and NDA12 (new-dwelling completions 2012-2025, aggregated across 867 named towns and cities) give the two end stages:

| Year | Permissions granted | Completions | 2-year aggregate ratio (completions T+2 ÷ permissions T) |
|---:|---:|---:|---:|
| 2019 | 38,461 | 15,935 | **41%** |
| 2020 | 42,371 | 15,583 | 54% |
| 2021 | 42,991 | 15,624 | 57% |
| 2022 | 34,177 | 22,704 | 65% |
| 2023 | 41,225 | 24,316 | 61% |
| 2024 | 32,401 | 22,136 | — |
| 2025 | 34,974 | 25,237 | — |

*Footnote to ratio column: this is a population-level aggregate, not a cohort-tracked rate. Permissions granted in 2019 may complete in 2025 or 2026; completions in 2021 partly reflect permissions granted before 2019, which BHQ15 does not cover. A rising ratio can reflect a changing mix as much as genuinely higher follow-through.*

Two things stand out.

**Completions have nearly doubled.** From 15,935 in 2019 to 25,237 in 2025. The building system is genuinely delivering more houses than it was five years ago.

**Permissions have been flat.** Every year between 2019 and 2025 Irish planning authorities issued between 32,000 and 43,000 unit permissions. There is no long-term upward trend. Given the government target of 50,500 completions per year, this remains the bottleneck: even at 100 percent conversion, the current permissions flow would not deliver the target.

**The aggregate conversion ratio has risen — but from a COVID trough, not from a pre-COVID baseline.** Pulling the longer CSO permissions series BHQ16 back past 2019 gives:

| Permission year T | Permissions (units) | Completions T+2 | 2-year aggregate ratio |
|---:|---:|---:|---:|
| 2016 | 15,950 | 13,649 | 86% |
| 2017 | 20,776 | 15,935 | 77% |
| 2018 | 28,939 | 15,583 | 54% |
| 2019 | 38,461 | 15,624 | 41% |
| 2022 | 34,177 | 22,136 | 65% |

The 2019 trough is the start of our BHQ15 window, not a natural floor. The 41% → 65% rise reported above is a recovery from the 2019-2021 COVID-era delivery trough back toward — but still below — pre-COVID conversion ratios of 77-86%. Two distinct stories are compatible with the data: (a) the system is genuinely getting better at converting permissions; (b) the 2020-2022 completions we now see reflect a post-COVID catch-up of permissions issued in a higher pre-2019 regime. We cannot distinguish these from aggregate series alone. Both readings support the headline that permission volume is the binding constraint.

### Lag sensitivity

Swapping the 2-year lag for 1-year or 3-year lags changes the *level* of the ratios but not the ranking: 2022 is the highest-ranked permission year at every lag (71% / 65% / 74%) and 2019-2020 are the trough at every lag.

### The SHD window: descriptive only

The Strategic Housing Development (SHD) scheme, which ran from late 2017 to late 2021, fast-tracked 100+ unit developments through An Bord Pleanála:

- 2019-2021 SHD permissions: **60,605 units**
- 2019-2021 Non-SHD permissions: **63,218 units**
- Total 2019-2021 completions (2-yr lag, 2021-2023): **62,644 units**

Both streams cleared in roughly equal unit volume. We are not inferring relative per-scheme productivity here: SHD schemes are apartment-dominant 100+ unit developments; non-SHD permissions are a mix of one-off houses, scheme houses, and small apartment developments, and BHQ15 does not give us scheme counts split by SHD status. The numbers are reported descriptively, not as a fast-track evaluation.

## Caveats

- **Aggregate ratios, not cohort tracking.** The T+2 ratio is national completions ÷ national permissions with a lag. It is not per-permission tracking. Some 2019 permissions will complete in 2026-2028; some 2020-2021 completions reflect pre-2019 permissions BHQ15 does not cover.
- **The 41% → 65% rise is a recovery, not an all-time improvement.** Pre-2019 BHQ16 data show 2-yr conversion ratios of 77-86% in 2016-2017, falling through 2018 (54%) and 2019 (41%). The recent rise is a return toward — still below — the pre-COVID regime.
- **Commencement notices are not in this analysis.** The construction middle stage (commencement) is held by the Department of Housing, not CSO PxStat, and is not ingested here. The analysis compares only the two ends — permissions and completions — with a lag. It is not a three-stage pipeline.
- **SHD vs non-SHD is not apples-to-apples.** SHD schemes are apartment-dominant 100+ unit developments; non-SHD permissions are dominated by smaller schemes and one-off houses. Unit-level totals are comparable; per-scheme productivity is not computable from BHQ15.
- **No cancellation/lapse accounting.** Irish planning permissions lapse after 5 years. We cannot distinguish completed-late from never-built.
- **No cost or tenure.** These are unit counts irrespective of price, rent, or social/affordable/market status.
- **No judicial-review channel.** The SHD scheme was throttled in practice by the rate at which ABP decisions were quashed in the High Court. A separate paper on SHD judicial reviews identifies that channel.
- **No uncertainty quantification.** The 41% → 65% jump is a point estimate with no confidence interval.

## What it means

For a commuter watching the housing crisis: completions are rising materially year on year and the conversion ratio is better now than at its 2019-2021 trough — but likely not better than it was in 2016-2017. The number of permissions being issued has not grown beyond the 2019 level, and the government's 50,500-home target cannot be met at current permission rates even under the most optimistic conversion.

For a policymaker: the primary chokepoint is permission volume, not "developers aren't building what they're permitted to build." This conclusion is robust to the caveats above: under either reading of the conversion trajectory — genuine improvement or COVID-recovery — completions still cap out far below target as long as permissions stay in the 32-43k range.

## How we did it

Downloaded CSO PxStat tables BHQ15 (Planning permissions 2019-2025 with SHD split), NDA12 (New Dwelling Completions by urban area × house type, 2012-2025), and BHQ16 (Planning Permissions Granted by region, 1975-2025, for pre-2019 context). Aggregated BHQ15 across quarters to annual, avoiding double counting between "Apartment units" and "All house units". Aggregated NDA12 across all 867 named areas under "All house types". Computed 1-, 2-, and 3-year lagged aggregate ratios. No modeling. No cohort tracking — the data does not support it.
