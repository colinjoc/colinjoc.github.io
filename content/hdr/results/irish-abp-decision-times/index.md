---
title: "An Bord Pleanála Decision Times: From 18 to 42 Weeks and (Partially) Back"
date: 2026-04-16
domain: "Irish Housing"
blurb: "The statutory objective is that An Bord Pleanála decide planning appeals within 18 weeks. Mean time to dispose doubled from 23 weeks in 2018 to 42 weeks in 2023-2024. Statutory-objective compliance collapsed from 69% in 2019 to 25% in 2024. The queue utilisation ratio (intake over throughput) peaked at 1.45 in 2022 — the board was taking in cases 45% faster than it could clear them — which is arithmetically consistent with the backlog crystallising in 2023. 2025 quarterly data show partial recovery to the 25-30 week range with 65% SOP compliance year-to-date. The queue-theoretic story does NOT establish causation, only the accounting relationship; other factors (board-member resignations 2022, judicial-review pressure, case-mix shift toward SHD/LRD) overlap and cannot be cleanly separated in this dataset."
weight: 6
tags: ["housing", "ireland", "planning-permission", "decision-times", "An-Bord-Pleanala", "policy-evaluation"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_abp_decision_times/paper.md).*

## The question

An Bord Pleanála (now An Coimisiún Pleanála) is Ireland's planning appeals board. It decides appeals against Local-Authority planning decisions and first-instance applications for strategic projects. It has a statutory objective to decide cases within **18 weeks** for most appeals.

Press reporting over 2022-2024 flagged severe backlogs and missed deadlines. How bad did it get, and has the situation stabilised?

## What we found

### Decision times nearly doubled from 2018 to 2024

Mean time to dispose of all cases (including appeals, referrals and strategic applications):

| Year | Mean weeks | Bootstrap 95% CI | Within statutory period |
|---:|---:|:---:|---:|
| 2017 | ~18 | ±2 (chart read-off) | ~64% |
| 2018 | 23 | 22-24 | 43% |
| 2019 | 22 | 21-23 | 69% |
| 2020 | 23 | 22-24 | 73% |
| 2021 | 20 | 19-21 | 57% |
| 2022 | 26 | 25-27 | 45% |
| **2023** | **42** | **40.6-43.4** | **28%** |
| **2024** | **42** | **40.6-43.4** | **25%** |

The 2023-2024 values are more than double the statutory objective. By 2024 only one in four cases met the 18-week target — the worst performance in the observable record.

### 2025 shows partial recovery

Quarterly statistics for Q1-Q3 2025 show mean disposal times back in the 25-30 week range and monthly SOP compliance ranging 37% to 77%, with a year-to-date average of about 58-65% (trend-line OLS; an earlier iid-bootstrap estimate in the draft overstated the precision and was withdrawn).

![Left: mean weeks to dispose an ABP case, 2017-2024, with statutory objective line at 18 weeks. Right: percentage of cases disposed within the statutory objective period, same years. Red bars mark sub-60% years.](plots/abp_decision_times.png)

### The queue utilisation ratio peaked at 1.45 in 2022

A simple queueing accounting identity: ρ = intake / throughput. If ρ exceeds 1, cases come in faster than the board clears them, and the backlog grows. For ABP:

- 2022: **ρ = 1.45** (95% CI 1.37-1.53)
- 2023: ρ = 1.00 (CI 0.95-1.05) — flat
- 2024: ρ = 0.74 (CI 0.70-0.77) — clearing

The timing lines up arithmetically with the 2023-2024 decision-time peak. **This is an accounting relationship, not a causal story** — ρ > 1 necessarily produces backlog growth, but what caused ρ > 1 (board-member resignations in 2022, case-mix shift, staff turnover, COVID disruption) cannot be separated from this dataset alone.

### SHD mean of 124 weeks is a small-N tail, not typical

In 2024, mean disposal time for Strategic Housing Development appeals was 124 weeks — more than 2.3 years — but this is a mean over 40 cases with heavy-tailed residual SHD workload still being cleared after the regime ended in 2021. The **median** SHD disposal was about 79 weeks with interquartile range 42-151. Large-scale Residential Development (LRD) appeals, by contrast, had a median of about 13 weeks over 2024-2025Q1, consistent with a normal modern appeal cadence on a 15-month window.

The "SHD is slow, LRD is fast" narrative in press reporting is directionally right but the magnitude comparison is inflated by comparing a small-N tail of ancient SHD holdovers with a well-cleared LRD cohort.

### The decision-time trend cannot be cleanly attributed to any single cause

The 2022-2024 deterioration overlapped several potentially causal events:

- **Board-member crisis** (2022-2024): from 2022 a sequence of resignations and allegations reduced Board capacity below statutory minimum for extended periods; remediation added members in 2024.
- **Judicial-review pressure** (ongoing): JRs increased defensive-drafting time per case, though the effect is not separable from volume.
- **Case-mix shift**: SHD peaked 2019-2021 with large complex apartment schemes; these took proportionally more Board time.
- **COVID disruption** (2020-2021): site-visit disruption, inspector availability, hearing postponements.
- **Planning and Environment List** (November 2022): speeds JR disposal, not ABP disposal, but may have changed the pressure profile.
- **Planning and Development Act 2024**: enacted but largely not yet in force; its effect begins 2025-2026.

A proper causal decomposition requires case-level data that is not in the published annual reports. The published dataset supports a descriptive trajectory and a queueing accounting identity; it does not support claims like "board-member crisis *caused* the 2023 peak".

### Out-of-sample validation matters

The draft of this paper picked an interrupted time-series model with three knots (2018, 2022, 2023) that fit the 2018-2024 data to within 0.57 weeks mean-absolute-error — but this was in-sample only. A leave-one-year-out cross-validation raises the out-of-sample MAE to 1.65 weeks — still the champion vs four alternative models, but 2.9× worse than in-sample. The model is useful for descriptive smoothing; it is **not** a reliable forecast of 2026-2028.

## What this does NOT establish

- **Not causation.** Queue utilisation ρ is an accounting relationship, not an explanation.
- **Not the ACP effect.** An Coimisiún Pleanála took over formally in June 2025; the recovery visible in H1 2025 pre-dates the name change and cannot be attributed to the new institution.
- **Not a forecast.** Scenario analysis in the paper (Phase B) has Monte Carlo 90% intervals spanning 60+ percentage points; the scenarios are directional, not quantitative.
- **Not case-level.** Everything here is annual or quarterly aggregate; behaviour of specific inspectors, applicants, or case complexity is not decomposable.

## What it means

For housing commentators: the "ABP collapse" framing is directionally accurate for 2023-2024 but the 2025 data show a real recovery. Calibrate rhetoric against both ends.

For policymakers: the queueing-identity finding (ρ > 1 in 2022 → backlog peak in 2023) means that if the Planning and Development Act 2024 does not keep ρ below 1.0 durably, the backlog returns. Throughput is the constraint.

For anyone tracking the ACP transition: current baseline is 25-30 week mean with 58-65% SOP compliance. Watch whether that holds through 2026.

## How we did it

Primary data: ABP annual-report appendices 2018-2023 (decision-time tables and SOP-compliance tables); ABP 2024 full annual report; ABP quarterly casework statistics Q1-Q3 2024 and Q1-Q3 2025. Methods: interrupted time-series with knots at policy/institutional events, leave-one-year-out cross-validation, bootstrap CIs on every headline number, delta-method CIs on ρ, Oaxaca-Blinder-style case-mix decomposition for the 2018→2024 trend, Monte Carlo sensitivity on scenario parameters. Ran through the full HDR pipeline including an independent Phase 2.75 blind reviewer (10 mandated experiments R1-R10 executed; Phase B demoted from quantitative forecast to directional-only; causal language replaced with correlation/accounting identity throughout) and an independent Phase 3.5 signoff.
