---
title: "Irish Mandatory Gender Pay Gap Reporting: Three Years In, Narrowing Inside Firms, Not Yet Distinguishable From Noise at the Population Level"
date: 2026-04-16
domain: "Irish Labour Economics"
blurb: "Ireland introduced mandatory gender pay gap reporting in 2022 for employers with 250 or more staff, phasing down to 50 staff by 2026. Three reporting cycles in, the median Irish hourly pay gap has fallen from 7.0 percent to 6.2 percent — about a quarter of a percentage point per year. Once a cluster-bootstrap is run over firms, that rate has a 95 percent confidence interval of minus 0.60 to plus 0.14 percentage points per year: the population-level narrowing is *not yet statistically distinguishable from zero*. The more robust finding is within-firm: 623 firms reporting in both 2022 and 2025 narrowed by a median of 0.87 points, and 56.5 percent narrowed. A decomposition shows essentially all of the population-level drop is within-firm reform, not composition from the phased-down threshold. The original draft of this summary claimed Ireland was narrowing faster than the UK; window-matched reviewer experiments overturned that claim, and this page has been corrected."
weight: 9
tags: ["gender-pay-gap", "ireland", "labour-economics", "mandatory-disclosure"]
---

*Plain-language version. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_gender_pay_gap/paper.md).*

**Retroactively revised on 2026-04-15** after a Phase 2.75 blind-reviewer cycle. The original version of this page claimed Ireland was narrowing its gender pay gap nearly 2x as fast as the UK. Reviewer-mandated window-matched and bootstrap experiments overturned that headline. The corrected version below foregrounds the within-firm evidence, which is what survives.

## The question

The Gender Pay Gap Information Act 2021 brought Ireland into line with most of Europe on pay-gap reporting. From 2022, every Irish employer with at least 250 staff is required to publish eight pay-gap numbers a year. From 2024 the threshold fell to 150 employees. By 2026 it will be 50.

Three full reporting cycles have now come and gone. Two natural questions: **how far has the Irish gap actually moved**, and **how does the pace compare with the UK**, which has been running a near-identical regime since 2017?

## What we found

### The population gap has drifted from 7.0 to 6.2 percent in three years, but the rate is not yet significant

The population-wide median hourly pay gap among mandatory-reporting employers moved as follows:

| Year | Filing count | Median of reported medians |
|---|---|---|
| 2022 | 709 | **7.00%** |
| 2023 | 740 | 6.60% |
| 2024 | 962 | 6.40% |
| 2025 | 1,580 | **6.22%** |

That is a 0.78-point fall over three years, or about minus 0.26 percentage points per year. When we bootstrap that rate by resampling firms (1000 replicates), the 95 percent confidence interval is **minus 0.60 to plus 0.14 percentage points per year**. Three years of data is simply not long enough to declare the population trend statistically different from flat. The point estimate is suggestive of narrowing; the noise band still includes "no change."

![Irish gender pay gap 2022-2025. The left panel shows the Irish trajectory (teal solid for median-of-medians, coral dashed for mean-of-medians) with UK endpoints overlaid in gray for comparison. The right panel ranks the ten worst-performing NACE sectors in 2025 — Real Estate at 28.6 percent leads.](plots/ie_gpg_trend.png)

### The narrowing is real inside firms that were always in the pool

A fair worry: the 2022-2025 population is not the same set of firms, because the reporting threshold phased down from 250 to 150 employees mid-period, roughly doubling the reporting pool. Maybe the drop is just smaller (lower-gap) firms entering the sample, not real reform.

We tested this two ways.

**Threshold-invariant cohort.** Restrict to the 705 firms that reported in 2022 (i.e. the original 250-plus cohort) and follow only them through 2025. On this stable cohort, the trajectory is 7.00 percent (2022) to 6.20 percent (2025), a rate of minus 0.267 pp/year — essentially identical to the full-sample rate. If composition were the story, the stable cohort would not narrow.

**Within-firm change-score panel.** Of the 1,712 unique Irish reporting employers, 623 reported in both 2022 and 2025. Within this persistent panel:

- Median gap 2022: 7.10 percent
- Median gap 2025: 6.20 percent
- Median within-firm change: **minus 0.87 percentage points**
- Share narrowing: **56.5 percent**

**Decomposition.** We split the population 0.78-point drop into three components: change within firms that reported in both years, the effect of new firms entering the pool post-2022, and the effect of firms exiting. The arithmetic is:

- Within persistent firms: **minus 0.90 percentage points**
- New entrants (935 firms, coming in under the lower threshold): plus 0.02 points
- Exiters (82 firms dropping out): plus 0.10 points
- Total: minus 0.78 points (matches observed)

**Essentially all of the narrowing is within-firm reform.** The phased-down reporting threshold has not mechanically lowered the headline — the new smaller firms were not systematically lower-gap at the point they joined.

### Ireland versus the UK: no clear winner on matched windows

The original draft of this page claimed Ireland was narrowing its gap "nearly 2x faster" than the UK. That claim compared Ireland's three-year rate to the UK's eight-year average. Once you match windows properly, the comparison does not support the claim:

| Country / window | Start | End | Years | pp/year |
|---|---|---|---|---|
| UK 2017-2025 (full regime)                  | 9.30% | 8.11% | 8 | −0.15 |
| UK 2017-2020 (first three years, to match Ireland's regime age) | 9.30% | 10.00% | 3 | **+0.23** (widened) |
| UK 2022-2025 (same calendar years as Ireland) | 9.18% | 8.11% | 3 | **−0.36** |
| Ireland 2022-2025                           | 7.00% | 6.22% | 3 | −0.26 (95% CI [−0.60, +0.14]) |

The UK's first three years are not a useful baseline for Ireland's 2022-2025 performance because COVID distorted the UK in 2020 (and the UK 2019 cycle was suspended). The UK's 2022-2025 calendar-matched rate is actually *faster* than Ireland's (−0.36 vs −0.26 pp/year), and both are within each other's uncertainty bands.

**The honest statement** is that both regimes are delivering within-firm narrowing on the order of a quarter to a third of a percentage point per year, with wide uncertainty over a three-year window. There is no evidence from this data that one country is structurally outperforming the other.

### The sector dispersion is enormous, and that is what actually matters for policy

Averages mask a lot. The top five Irish sectors by 2025 median pay gap (with 95% confidence intervals, and small-sample flags where applicable):

| Sector | n firms | 2025 median | 95% CI |
|---|---|---|---|
| Real Estate Activities                | 7 (small) | 28.6% | [22.0, 40.0] |
| Mining and Quarrying                  | 3 (small) | 23.7% | [19.8, 27.0] |
| Construction                          | 58        | 21.5% | [16.0, 24.9] |
| Electricity, Gas, Steam, Air Conditioning | 22    | 18.1% | [9.3, 25.7] |
| Financial and Insurance Activities    | 168       | 14.3% | [12.0, 16.3] |

At the other end:

| Sector | n firms | 2025 median | 95% CI |
|---|---|---|---|
| Accommodation and Food Service        | 131 | 1.5% | [1.0, 2.0] |
| Human Health and Social Work          | 114 | 0.0% | [−1.2, 0.7] |
| Public Administration and Defence     | 114 | −0.1% | [−2.4, 2.0] |
| Water Supply, Sewerage, Waste         | 5 (small)  | −3.0% | [−26.1, 12.6] |

Real Estate (7 firms), Mining (3 firms), and Water/Waste (5 firms) have wide confidence intervals and are reported for completeness rather than as load-bearing headline numbers. The robust high-gap sectors — Construction, Finance, Manufacturing, Energy, Professional/Scientific/Technical — cover over 500 firms between them, and they are the durable targets for sector-specific action-plan scrutiny.

## What we cannot say

- **Not causal.** We have no pre-2022 Irish counterfactual and no synthetic-control comparator for the regime's own effect.
- **Population rate not significant.** Over a three-year window the 95 percent CI on the annualised population rate spans [−0.60, +0.14] pp/year. More years are needed before any "the regime is narrowing the population gap" claim can be made with confidence. The within-firm finding is stronger.
- **Coverage of the mandatory universe not audited.** paygap.ie is a volunteer-maintained scrape of employer reports. We have not been able to audit coverage against the CSO Business Demography (BIS-02) or IBEC 150-plus member list for 2024/2025 within this review cycle. If coverage is materially below 100 percent, non-reporter selection bias (plausibly biasing the sample toward higher-transparency, lower-gap firms) cannot be ruled out. Flagged for Phase B.
- **Not representative of the whole labour force.** Only employers at or above the reporting threshold are in this analysis.
- **Not intersectional.** The regulations report only the gender binary.

## What it means

For an Irish worker reading the news on pay transparency: inside Irish reporting firms the gap is drifting down at around 0.26 to 0.27 percentage points per year on both the full sample and the stable ≥250-employee cohort. 56.5 percent of persistent firms narrowed between 2022 and 2025. That is probably real, but three years is short and the population-level rate cannot yet be declared statistically different from zero.

For a policymaker: the sector dispersion is the durable story. Construction, Finance, Manufacturing, and Energy are a 15-to-22-point gap sitting persistently above the economy average. That is where action-plan scrutiny should focus. The cross-country rhetoric about Ireland beating the UK does not hold up to window-matched comparison and should not be used as a policy selling-point.

For an analyst: the clean next step is a synthetic-control difference-in-differences with Ireland as the 2022 treated unit and a non-mandatory-reporting Eurozone donor pool, plus a paygap.ie coverage audit against the CSO BIS-02 universe.

## How we did it

We downloaded the paygap.ie archive — an independent public-service project that has scraped and aggregated Irish employer gender pay gap reports since the regime began in 2022 — giving us 3,991 employer-year observations across 2022-2025. We computed annual median-of-medians, restricted to a threshold-invariant ≥250-employee cohort (705 firms first observed in 2022), built the 623-firm within-firm panel across 2022-2025, decomposed population change into within/entry/exit components, bootstrapped 95 percent confidence intervals on the annualised rate and on each NACE sector's 2025 median, and cross-referenced the UK regime's year-by-year median-of-medians over three matched windows. Full code and pipeline in the linked paper; reviewer-mandated follow-up experiments in `analysis_phase275.py`.
