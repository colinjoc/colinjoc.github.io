---
title: "Ireland's gender pay gap is falling — but not in the way the headlines say"
date: 2026-04-16
domain: "Irish Labour Economics"
blurb: "Three years into mandatory pay-gap reporting, the headline is narrowing. The question is whether the narrowing is real or a statistical mirage."
weight: 13
tags: ["gender-pay-gap", "ireland", "labour-economics", "mandatory-disclosure"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_gender_pay_gap/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Ireland's median gender pay gap has moved from 7.0 percent to 6.2 percent across three years of mandatory reporting. That drop is not, by itself, statistically distinguishable from no change. The firmer story is what happens inside firms that have been reporting the whole time: 623 of them narrowed their gap by nearly a percentage point, and 56 percent of them narrowed at all. Earlier claims that Ireland was narrowing twice as fast as the UK do not survive a proper window-matched comparison.

## The question

The Gender Pay Gap Information Act 2021 brought Ireland into line with most of Europe. From 2022, every Irish employer with at least 250 staff has been required to publish eight pay-gap numbers a year. From 2024 the threshold fell to 150 employees. By 2026 it will be 50. Three full reporting cycles have now come and gone, so two natural questions present themselves — how far has the Irish gap actually moved, and how does the pace compare with the UK, which has run a near-identical scheme since 2017?

## What we found

![Irish gender pay gap 2022-2025. Left panel: Irish trajectory with UK endpoints overlaid. Right panel: the ten worst-performing sectors in 2025 — Real Estate at 28.6 percent leads.](plots/ie_gpg_trend.png)

- The median hourly pay gap among mandatory-reporting employers moved from 7.0 percent in 2022 to 6.2 percent in 2025 — about a quarter of a percentage point per year.
- At the population level, that rate is not yet statistically different from zero. When we resample the firms to test how sure we can be, the plausible range runs from a decline of six-tenths of a point per year to an increase of one-tenth. Three years is simply too short to call.
- Inside firms that have been reporting throughout the period, the picture is firmer. Of the 623 employers that filed in both 2022 and 2025, the median narrowed its gap by 0.87 percentage points, and 56 percent of them narrowed at all.
- The narrowing is not a statistical artefact of smaller firms joining the reporting pool as the threshold dropped. A decomposition shows that essentially all of the population-level drop comes from within-firm change. New entrants contributed almost nothing.
- The earlier claim that Ireland was narrowing "twice as fast as the UK" was an artefact of comparing a three-year Irish window to an eight-year UK window. Match the calendar years properly and the UK's 2022-2025 rate is actually faster than Ireland's. Both sit inside each other's uncertainty bands.
- Sector dispersion is enormous and dwarfs the headline. Real Estate firms have a 29 percent median gap. Construction sits at 22 percent. Finance at 14 percent. At the other end, Accommodation and Food Service is at 1.5 percent, and Health and Public Administration are effectively at zero.

## Why that matters

The political selling-point for mandatory pay-gap reporting has always been the cross-country league table. If Ireland can credibly claim it is closing its gap faster than the UK, that builds support for a stronger version of the regime. The data does not support that claim. Both regimes are delivering roughly a quarter to a third of a percentage point of narrowing per year, with wide uncertainty, and neither is clearly ahead of the other.

The firmer finding — within-firm narrowing — is the one that matters for whether reporting is working as a policy instrument. The point of mandatory disclosure is that firms change behaviour once they see their numbers against industry peers. Fifty-six percent of persistent firms narrowing their gap, and the median firm dropping nearly a point, is the signature of that mechanism working. It is not proof, because we have no pre-regime Irish counterfactual, but it is the expected pattern if the regime is doing what it was designed to do.

## What it means in practice

**For Irish workers.** Inside Irish firms that have been reporting throughout, the gap is drifting down at around a quarter of a percentage point a year, and most firms are moving in the right direction. The dispersion across sectors, however, is vast. Your experience of pay transparency depends heavily on what industry you are in.

**For policymakers.** The durable target for action-plan scrutiny is the high-dispersion sectors — Construction, Finance, Manufacturing, Energy — which sit 15 to 22 percentage points above the economy median and together cover more than 500 reporting firms. Cross-country rhetoric about Ireland beating the UK does not hold up to matched comparison and should not anchor policy debate.

**For analysts.** Three years is too short to declare a population-level trend. A cleaner future test would compare Ireland against a matched control group of European economies without mandatory reporting, and would audit whether the volunteer-maintained employer reports cover the full mandatory universe.

## How we did it

We used the [paygap.ie archive](https://paygap.ie/), a public-service project that scrapes and aggregates Irish employer gender pay gap reports, giving us 3,991 employer-year observations across 2022-2025. We computed annual median-of-medians, restricted to firms that were reporting from the 250-employee baseline onwards to isolate threshold effects, built a within-firm panel across the same persistent employers, and decomposed population-level change into contributions from persistent, entering and exiting firms. We bootstrapped confidence intervals on the annual rate and on each industry's 2025 median, and ran three matched-window comparisons against the UK regime.

## Further reading

- [paygap.ie](https://paygap.ie/) — the independent archive of Irish employer reports.
- UK Government Equalities Office gender pay gap service — the equivalent UK data used for matched-window comparisons.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_gender_pay_gap/paper.md).
