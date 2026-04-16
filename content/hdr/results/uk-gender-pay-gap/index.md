---
title: "Nine Years of UK Mandatory Gender Pay Gap Disclosure: Has the Gap Actually Narrowed?"
date: 2026-04-16
domain: "UK Labour Economics"
blurb: "Since 2017 every UK employer with 250 or more staff has been legally required to publish six gender pay gap numbers every year. Nine reporting cycles and 93,000 filings later, has the gap actually moved? The population median has fallen from 9.3 to 8.1 percent (95% CI on the gap: -1.70 to -0.57 pp). Of the 5,259 employers that reported in both 2017 and 2025, the within-firm median dropped 2.1 pp and 61 percent narrowed their gap (Wilcoxon p < 1e-97). The COVID-adjusted rate of progress is 0.15 to 0.20 percentage points per year, implying a 40-to-55-year horizon to parity under the current regime."
weight: 8
tags: ["gender-pay-gap", "uk", "labour-economics", "policy-evaluation", "mandatory-disclosure"]
---

*Plain-language version. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/uk_gender_pay_gap/paper.md).*

**Note: this page was retroactively revised on 2026-04-15 after an independent blind review flagged missing uncertainty quantification, a missing COVID-regime correction, and a missing sector breakdown. Two headline numbers changed: the rate of progress was revised down from ~0.25 to 0.15-0.20 pp/year (so the horizon to parity moved from ~30 years to 40-55), and a genuine sector-level result was added (Public Administration narrowing fastest; Education widening due to Multi-Academy-Trust growth into the reporting pool, not due to schools getting worse).**

## The question

The Equality Act 2010 (Gender Pay Gap Information) Regulations 2017 introduced a rule the UK had never had before: every employer with 250 or more staff must publish, every April, six specific numbers — the mean and median hourly pay gap between men and women, the mean and median bonus gap, the share of men and women who got a bonus, and the gender composition of each quartile of hourly pay. Nine April deadlines have come and gone. Has the headline gap actually narrowed?

There are two ways that gap can move. A company can genuinely reform — promote more women into senior roles, recruit differently, restructure pay bands — which lowers its own reported gap. Or the population can recompose — smaller, less pay-disparate companies enter the disclosure pool as they grow past the 250-employee threshold, dragging the average down without anyone at any single company having changed anything. We can distinguish between these with the right panel structure.

## What we found

### The population median narrowed from 9.3 to 8.1 percent, and the interval excludes zero

Across the 93,777 employer-year filings in the public disclosure corpus, the median hourly pay gap fell from 9.30 percent in 2017 (95% CI 9.00 to 9.70) to 8.11 percent in 2025 (95% CI 7.80 to 8.56) — a 1.19 percentage-point narrowing with a 95% CI of -1.70 to -0.57. The trajectory went modestly up during COVID (2019-2021) and has fallen every year since.

![UK gender pay gap 2017-2025. The left panel shows the median and mean of medians — both narrowing, with 2025 the lowest on record. The right panel shows the share of employers filing after the deadline: 2025 is also a record low.](plots/gpg_annual_trend.png)

### The rate of progress is slower than the endpoint-difference suggests

The naive 2017-to-2025 endpoint division gives about 0.25 percentage points per year. Once you account for the COVID filing-waiver regime, though, the real rate is slower. Three specifications agree:

- Plain OLS on year, no COVID dummy: **-0.198 pp/year** (95% CI -0.359 to -0.037)
- OLS excluding 2019-2021: **-0.145 pp/year** (95% CI -0.257 to -0.033)
- OLS with a COVID dummy for 2019-2021: **-0.152 pp/year** (95% CI -0.240 to -0.065)

The honest range is **0.15 to 0.20 percentage points per year**. At that rate, reaching parity under the current regime is a 40-to-55-year project, not the 30-year figure implied by the naive endpoint calculation.

### Within persistent firms, the progress is close to twice as fast (and overwhelmingly statistically significant)

Of the 22,482 unique employers that filed at least once, 5,259 filed under the same name in both 2017 and 2025. Within that persistent panel:

- Median gap in 2017: 9.20 percent
- Median gap in 2025: 6.10 percent
- Within-firm median change: **minus 2.10 percentage points** (95% CI -2.45 to -1.90)
- Share of firms that narrowed their gap: **61.1 percent** (95% CI 59.8 to 62.4)
- Wilcoxon signed-rank test that the median change is zero: **p < 10-to-the-minus-97**. The within-firm narrowing is not a statistical artefact.

We tested three different ways of identifying "the same firm in both years" (`EmployerName`, `EmployerId`, `CompanyNumber`) and got results within 0.3 percentage points of each other. The finding is robust.

The within-firm narrowing is 1.8 times the population-wide narrowing. That means roughly half of the apparent population-level progress comes from genuine reform at firms that kept reporting throughout, and roughly half comes from composition change as lower-gap firms newly entered the disclosure pool.

### Which sectors moved?

Mapping each filing to a 1-digit SIC division (A-U), the three fastest-improving divisions from 2017 to 2025 were:

- **Public Administration**: 7.6 percent to 2.7 percent (-4.86 pp)
- **Information / Communication**: 18.0 percent to 14.0 percent (-4.00 pp)
- **Construction**: 25.0 percent to 21.0 percent (-3.91 pp)

The single striking outlier in the other direction is **Education, which appears to have widened from 10.2 to 22.9 percent**. That is not a real deterioration inside schools. The number of Education-sector filings nearly tripled from 342 in 2017 to 961 in 2025 as Multi-Academy Trusts consolidated and crossed the 250-employee threshold. Primary and secondary schools have a majority-female workforce with a male-dominated senior-leader stratum, so adding a large number of new school-trust filings mechanically shifted the sector median up. The message is compositional, not reformist failure.

### The biggest firms have the smallest gaps

Employer size buckets from the 2025 filings:

| Size | Median hourly gap |
|---|---|
| 20,000 or more staff | **5.0%** |
| Less than 250 (voluntary filers) | 5.5% |
| 5,000 to 19,999 | 6.5% |
| 1,000 to 4,999 | 7.3% |
| 250 to 499 | 9.0% |
| 500 to 999 | 9.0% |

The 250-to-999 band — which is where the mandatory threshold first bites and where formal HR infrastructure is often still developing — carries the largest gaps. The very largest employers (20,000+ staff, typically national banks, supermarkets, public-sector agencies) have the smallest gaps, around five points.

### Late filers have smaller gaps inside the mandatory bands — but the voluntary <250 case flips

A natural hypothesis is that employers who file late do so because they have something to hide. The raw data points the other way: late filings have a median gap of 7.00 percent vs 9.40 percent for on-time. An independent reviewer pointed out that this could be a size confound (Simpson's paradox) because smaller firms and voluntary filers behave differently.

After stratifying by employer size and running an OLS with size and year fixed effects, the late-minus-on-time difference is **-1.85 percentage points** (95% CI -2.28 to -1.43, p < 10-to-the-minus-17). The finding is real for the mandatory-reporting bands. But in the voluntary **<250 staff** pool, the direction reverses: late filers have a median gap of 12.7 percent vs 8.1 percent for on-time — late voluntary filers really are high-gap organisations. The "late filing = hidden bad news" hypothesis is wrong for mandatory firms but right for the voluntary tail. A more careful way to put it: for firms legally required to file, late filing is not a signal of a hidden bad gap; for the self-selected sub-250 filers, it is.

### Compliance has improved massively

The 2025 reporting year had a 2.5 percent late-filing rate — a record low, and a step change from 6.7 percent in 2024 and 7.5 percent in 2021. Mandatory disclosure regimes are often criticised as having no teeth; the compliance data suggests the UK regime has been absorbed into normal corporate practice over the decade since it was introduced.

## What we cannot say

- **No causal counterfactual.** We have no "UK without mandatory disclosure" scenario to compare against. Ireland introduced a near-identical regime in 2023 (currently for 150+ employee firms, phasing to smaller thresholds). An Ireland-minus-UK difference-in-differences is the natural next paper and the Irish data is in the `paygap.ie` portal.
- **No intersectional analysis.** The regulations report only on the gender binary. Ethnicity and disability pay gap reporting is not part of the regime.
- **Threshold truncation is permanent.** Employers below 250 staff are exempt; roughly 60 percent of the UK workforce is in firms under that threshold. Most of the UK labour market is not in this analysis at all.
- **Sectoral deltas partly reflect composition.** Education is the extreme case; smaller compositional effects likely contribute to other sector deltas too. A within-firm-only sectoral breakdown is a natural refinement.

## What it means

For a commuter reading the morning paper: the gap is genuinely moving in the right direction. Progress within established reporting employers averages about 0.15 to 0.20 percentage points per year. That is real and sustained, but slower than a casual read of the 2017-to-2025 endpoints suggests.

For a policymaker: at the current rate, full parity under the existing regime is a 40-to-55-year project. Proposals to accelerate (lower the 250-employee threshold, add ethnicity reporting, mandate sectoral benchmarks, require published action plans) would shift the rate, but the pure mandatory-disclosure lever has produced what mandatory-disclosure levers usually produce: gradual convergence, not a step change.

For a researcher: the dataset is beautifully clean, completely public, and nine years deep. It is one of the best panels available anywhere for studying the slow dynamics of gender pay disparity under a regulatory treatment. Extensions to within-firm-only sector breakdowns, intersectional analysis (if the regulations expand), and cross-country DiD against Ireland are all tractable from this base.

## How we did it

We downloaded the full gov.uk Gender Pay Gap Service archive — one CSV per reporting year, 2017-18 through 2025-26 — concatenated into a 93,777-row employer-year panel, computed annual medians and means, identified the 5,259-employer within-firm panel that reported in both endpoint years, and cross-tabulated by filing timeliness and employer size. After a blind review, we added: 1,000-draw bootstrap CIs on every headline estimate; a Wilcoxon signed-rank test on the 5,259-firm paired delta; a size-stratified OLS of the late-filer comparison; a three-specification COVID-sensitivity analysis of the trend slope; a robustness test across three different firm identifiers; and a 1-digit SIC sectoral decomposition. Full code and data pipeline are in the linked paper.
