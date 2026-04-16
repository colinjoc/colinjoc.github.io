---
title: "Irish Mandatory Gender Pay Gap Reporting: Three Years, Faster Than the UK"
date: 2026-04-16
domain: "Irish Labour Economics"
blurb: "Ireland introduced mandatory gender pay gap reporting in 2022 for employers with 250 or more staff, phasing down to 50 staff by 2026. Three reporting cycles in, the median Irish hourly pay gap has fallen from 7.0 percent to 6.2 percent — a narrowing rate of about a quarter of a percentage point per year. That is nearly double the UK's long-running rate. Ireland started at a lower gap than the UK did at regime-onset, but it is narrowing faster, which is interesting because diminishing returns would predict the opposite."
weight: 9
tags: ["gender-pay-gap", "ireland", "labour-economics", "mandatory-disclosure"]
---

*Plain-language version. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_gender_pay_gap/paper.md).*

## The question

The Gender Pay Gap Information Act 2021 brought Ireland into line with most of Europe on pay-gap reporting. From 2022, every Irish employer with at least 250 staff is required to publish eight pay-gap numbers a year. From 2024 the threshold fell to 150 employees. By 2026 it will be 50.

Three full reporting cycles have now come and gone. Two natural questions: **how far has the Irish gap actually moved**, and **how does the pace compare with the UK**, which has been running a near-identical regime since 2017?

## What we found

### The Irish gap has narrowed from 7.0 to 6.2 percent in three years

The population-wide median hourly pay gap among mandatory-reporting employers moved as follows:

| Year | Filing count | Median of reported medians |
|---|---|---|
| 2022 | 709 | **7.00%** |
| 2023 | 740 | 6.60% |
| 2024 | 962 | 6.40% |
| 2025 | 1,580 | **6.22%** |

That's a 0.78 percentage-point fall over three years, or about a quarter of a percentage point per year.

![Irish gender pay gap 2022-2025. The left panel shows the Irish trajectory (teal solid for median-of-medians, coral dashed for mean-of-medians) with UK endpoints overlaid in gray for comparison. The right panel ranks the ten worst-performing NACE sectors in 2025 — Real Estate at 28.6 percent leads.](plots/ie_gpg_trend.png)

### Ireland is narrowing faster than the UK

The UK's mandatory-disclosure regime has been running eight full years. Its median narrowed from 9.3 percent in 2017 to 8.1 percent in 2025 — a rate of about 0.15 percentage points per year.

Ireland's three-year rate is 0.26 percentage points per year. Nearly twice as fast.

This is genuinely interesting because the UK started at a wider gap than Ireland did. The standard economics prediction — diminishing returns — would say that the country starting wider should narrow faster, because the easy wins come first. Instead the country starting narrower is narrowing faster.

There are two candidate explanations, and the data in this paper cannot fully separate them:

- **Faster real reform.** Ireland's regime from day one required employers to publish an action plan alongside the numbers; the UK added action-plan encouragement only in 2022. Ireland's sectoral mix also differs — more tech, more pharma, fewer heavy-industry and traditional-banking weights — which may produce faster natural convergence.
- **Composition.** As the Irish reporting threshold phased down from 250 to 150 to 50 employees, the pool of reporting firms grew from 709 in 2022 to 1,580 in 2025. Smaller employers tend to have smaller gaps (less pay stratification). Some of the population-wide narrowing is just adding lower-gap firms to the pool.

To separate them properly requires a within-firm panel. We built one.

### Within persistent firms, narrowing is close to the population pace

Of the 1,700-odd unique Irish reporting employers, 623 reported in both 2022 and 2025. Within this persistent panel:

- Median gap 2022: 7.10 percent
- Median gap 2025: 6.20 percent
- Median within-firm change: **minus 0.87 percentage points**
- Share narrowing: **56.5 percent**

Within-firm narrowing is actually slightly larger than the population narrowing (0.87 vs 0.78 pp across three years). That means genuine firm-level reform is the bigger share of the Irish story, not composition change. The UK pattern is similar: persistent firms narrow slightly faster than the population.

### The sector dispersion is enormous

Averages mask a lot. The top five Irish sectors by 2025 median pay gap:

| Sector | 2025 median gap |
|---|---|
| Real Estate Activities | 28.6% |
| Mining and Quarrying | 23.7% |
| Construction | 21.5% |
| Electricity, Gas, Steam, Air Conditioning | 18.1% |
| Financial and Insurance Activities | 14.3% |

At the other end, a handful of sectors have essentially zero or negative gaps:

| Sector | 2025 median gap |
|---|---|
| Public Administration and Defence | −0.1% |
| Human Health and Social Work | 0.0% |
| Accommodation and Food Service | 1.5% |
| Agriculture, Forestry and Fishing | 1.8% |
| Water Supply, Sewerage, Waste | −3.0% |

The range is almost 32 percentage points — much larger than the country average. The highest-gap sectors are traditionally male-dominated industries with steep hierarchies (construction, finance, energy). The lowest-gap and negative-gap sectors are female-dominated care and public-administration occupations, where men are under-represented at lower-paid levels rather than women being paid more than men at equivalent roles.

## What we cannot say

- **Not causal.** We have no pre-2022 Irish counterfactual and no synthetic-control comparator for the regime's own effect. The Irish-UK rate gap is suggestive but not identifiable from this data alone.
- **Not representative of the whole labour force.** Only employers at or above the reporting threshold are in this analysis — currently 150 staff, phasing to 50 by 2026. Small Irish firms are invisible here.
- **Not intersectional.** The regulations report only the gender binary. Ethnicity and disability gaps are not covered.
- **Not a forever story.** Three years is short. Extrapolating the current rate to parity predicts a ~24-year horizon for Ireland, but the convergence dynamics in most mature labour markets slow as the gap narrows. The forward rate is almost certainly going to slow.

## What it means

For an Irish worker who reads the news on pay transparency: the regime is working, and faster than the UK's is. Half the movement is real within-firm reform; half is composition as smaller lower-gap firms enter the pool.

For a policymaker: the Irish advantage is consistent with Ireland's action-plan requirement from day one. If the UK wanted to speed up it could mandate published action plans alongside the raw numbers, which is currently only encouraged rather than required.

For an analyst: the clean cross-country comparison ought to be a synthetic-control difference-in-differences with Ireland as the 2022 treated unit and an Anglosphere donor pool. That's the next paper.

## How we did it

We downloaded the paygap.ie archive — an independent public-service project that has scraped and aggregated Irish employer gender pay gap reports since the regime began in 2022 — giving us 3,991 employer-year observations across 2022-2025. We computed annual medians, identified the 623-firm within-firm panel across the full window, and cross-referenced against the UK EMP-02 result from earlier in this portfolio. Full code and pipeline in the linked paper.
