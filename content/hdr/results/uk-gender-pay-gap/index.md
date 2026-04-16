---
title: "Nine Years of UK Mandatory Gender Pay Gap Disclosure: Has the Gap Actually Narrowed?"
date: 2026-04-16
domain: "UK Labour Economics"
blurb: "Since 2017 every UK employer with 250 or more staff has been legally required to publish six gender pay gap numbers every year. Nine reporting cycles and 93,000 filings later, has the gap actually moved? The population median has fallen from 9.3 percent to 8.1 percent. Of the 5,259 employers that reported in both 2017 and 2025, their within-firm median dropped 2.1 percentage points, and 61 percent narrowed their gap. Progress is real but slow: at the current rate parity is a 30-year project."
weight: 8
tags: ["gender-pay-gap", "uk", "labour-economics", "policy-evaluation", "mandatory-disclosure"]
---

*Plain-language version. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/uk_gender_pay_gap/paper.md).*

## The question

The Equality Act 2010 (Gender Pay Gap Information) Regulations 2017 introduced a rule the UK had never had before: every employer with 250 or more staff must publish, every April, six specific numbers — the mean and median hourly pay gap between men and women, the mean and median bonus gap, the share of men and women who got a bonus, and the gender composition of each quartile of hourly pay. Nine April deadlines have come and gone. Has the headline gap actually narrowed?

There are two ways that gap can move. A company can genuinely reform — promote more women into senior roles, recruit differently, restructure pay bands — which lowers its own reported gap. Or the population can recompose — smaller, less pay-disparate companies enter the disclosure pool as they grow past the 250-employee threshold, dragging the average down without anyone at any single company having changed anything. We can distinguish between these with the right panel structure.

## What we found

### The population median narrowed from 9.3 percent to 8.1 percent

Across the 93,777 employer-year filings in the public disclosure corpus, the median hourly pay gap fell from 9.30 percent in 2017 to 8.11 percent in 2025 — a 1.19 percentage-point narrowing over nine years. The trajectory went modestly up during COVID (2019-2021) and has fallen every year since.

![UK gender pay gap 2017-2025. The left panel shows the median and mean of medians — both narrowing, with 2025 the lowest on record. The right panel shows the share of employers filing after the deadline: 2025 is also a record low.](plots/gpg_annual_trend.png)

### Within persistent firms, the progress is close to twice as fast

Of the 22,482 unique employers that filed at least once, 5,259 filed in both 2017 and 2025. Within that persistent panel:

- Median gap in 2017: 9.20 percent
- Median gap in 2025: 6.10 percent
- Within-firm median change: **minus 2.10 percentage points**
- Share of firms that narrowed their gap: **61.1 percent**

The within-firm narrowing is 1.8 times the population-wide narrowing. That means roughly half of the apparent population-level progress comes from genuine reform at firms that kept reporting throughout, and roughly half comes from composition change as lower-gap firms newly entered the disclosure pool.

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

### Late filers have smaller gaps, not bigger ones

A natural hypothesis is that employers who file late are doing so because they have something to hide. The data does not support that. The 5,920 late filings across the nine years have a median hourly gap of 7.00 percent. The 87,857 on-time filings have a median of 9.40 percent. Late filers have systematically smaller gaps.

The most likely explanation is that late filers are smaller, newer, less formally-structured organisations that have crossed the 250-employee threshold recently and haven't built the compliance machinery. Smaller firms also tend to have smaller gaps because pay bands are less stratified. The simple "bad news delayed" story does not fit.

### Compliance has improved massively

The 2025 reporting year had a 2.5 percent late-filing rate — a record low, and a step change from 6.7 percent in 2024 and 7.5 percent in 2021. Mandatory disclosure regimes are often criticised as having no teeth; the compliance data suggests the UK regime has been absorbed into normal corporate practice over the decade since it was introduced.

## What we cannot say

- **No sector breakdown.** The raw filings include SIC codes but we didn't cross them with ONS industry classifications here. Which sectors made the fastest progress is a natural follow-up.
- **No intersectional analysis.** The regulations report only on the gender binary. Ethnicity and disability pay gap reporting is not part of the regime.
- **No causal counterfactual.** We have no "UK without mandatory disclosure" scenario to compare against. Ireland introduced a near-identical regime in 2023 (currently for 150+ employee firms, phasing to smaller thresholds). An Ireland-minus-UK difference-in-differences is the natural next paper and the Irish data is in the `paygap.ie` portal.
- **Threshold truncation is permanent.** Employers below 250 staff are exempt; roughly 60 percent of the UK workforce is in firms under that threshold. Most of the UK labour market is not in this analysis at all.

## What it means

For a commuter reading the morning paper: the gap is genuinely moving in the right direction. Progress within established reporting employers averages about a quarter of a percentage point per year. That is real, sustained, and — given the mandatory-disclosure regime is the only binding constraint — presumably driven by it rather than by any other macro trend.

For a policymaker: at the current rate, full parity under the existing regime is a 30-year project. Proposals to accelerate (lower the 250-employee threshold, add ethnicity reporting, mandate sectoral benchmarks, require published action plans) would shift the rate, but the pure mandatory-disclosure lever has produced what mandatory-disclosure levers usually produce: gradual convergence, not a step change.

For a researcher: the dataset is beautifully clean, completely public, and nine years deep. It is one of the best panels available anywhere for studying the slow dynamics of gender pay disparity under a regulatory treatment. Extensions to sector, intersectional, and cross-country DiD are all tractable from this base.

## How we did it

We downloaded the full gov.uk Gender Pay Gap Service archive — one CSV per reporting year, 2017-18 through 2025-26 — concatenated into a 93,777-row employer-year panel, computed annual medians and means, identified the 5,259-employer within-firm panel that reported in both endpoint years, and cross-tabulated by filing timeliness and employer size. Full code and data pipeline are in the linked paper.
