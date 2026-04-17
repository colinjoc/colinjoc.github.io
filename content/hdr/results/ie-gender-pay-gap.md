---
title: "Ireland's Gender Pay Gap: Narrowing Inside Firms, Not Yet in the Population"
date: 2026-04-17
domain: "Labour Economics"
blurb: "Three years into Ireland's mandatory gender-pay-gap disclosure regime, the typical reporting employer's gap narrowed by about 0.87 percentage points and 56 percent of persistent firms closed their gap. But the population-wide move is statistically indistinguishable from zero, and the popular claim that Ireland is narrowing faster than the UK does not survive a matched-window comparison."
weight: 15
tags: ["ireland", "gender", "pay-gap", "policy", "labour"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_gender_pay_gap/paper.md).*

## The Question

Since 2022 Irish employers with more than 250 staff have been required to publish their gender pay gap every year. From 2024 the threshold dropped to 150 staff, and from 2026 it drops again to 50. Three years of data are now in the public record.

Two questions follow. First: has the Irish gender pay gap actually moved over those three years, or is the reporting regime just producing a lot of filings and no change? Second: is the change — if any — happening inside existing firms, or is it the statistical artefact of smaller firms (which tend to have smaller gaps) being dragged into the pool as the threshold falls?

## What We Found

Across 3,991 employer filings from 1,712 unique companies:

- The typical reporting firm's median hourly gender pay gap moved from **7.00 percent in 2022 to 6.22 percent in 2025** — a narrowing of just under a percentage point.
- Of the 623 firms that reported in both 2022 and 2025, **56.5 percent narrowed their gap** and the median within-firm move was **−0.87 percentage points**.
- Essentially all of the population-level narrowing is within-firm reform, not composition change. New entrants under the lowered threshold barely moved the overall figure.
- The population rate of change is **−0.26 percentage points per year with a 95 percent confidence interval from −0.60 to +0.14** — *not* statistically distinguishable from zero over three years.
- The spread across sectors is roughly **28 percentage points**: Real Estate and Construction at one end (21 to 29 percent gaps), Public Administration and Human Health at or below zero.
- An earlier claim that Ireland was narrowing "nearly twice as fast" as the UK did not survive a proper comparison. Matched to the same 2022-to-2025 calendar window, the UK narrowed slightly faster than Ireland.

## Why That's Surprising

The intuitive worry about mandatory reporting was that any headline change would be composition-driven: lower the threshold, pull in smaller firms with smaller gaps, and the national figure moves without any individual firm doing anything differently. The decomposition shows the opposite. New entrants contributed almost nothing to the shift (+0.02 percentage points). Exiting firms contributed almost nothing (+0.10 points). The −0.78-point population move is almost exactly the −0.90-point within-firm move.

The second surprise is how much of the public narrative evaporates under a proper statistical test. Three years is simply too short a window to call a trend. The Irish rate sits inside a confidence interval that includes zero; it also sits inside the UK's comparable confidence interval. There is no defensible "Ireland is beating the UK" claim in the data yet. Both regimes are producing within-firm narrowing on the order of a quarter to a third of a percentage point per year, against very different macroeconomic backdrops — the UK's first three years absorbed the 2020 pandemic shock, Ireland's three years rode a tight labour market.

The third surprise, and the most policy-relevant, is sector dispersion. The gap between a construction firm and a health-and-social-care firm in 2025 is roughly 28 percentage points — larger than most cross-country gaps. Whatever mechanism is operating on pay gaps is heavily sector-specific.

## What It Means

For a female graduate choosing a sector: on median 2025 data, a finance role enters a 14-percent-gap workplace, a construction role enters a 22-percent-gap workplace, and a public-administration or health role enters a workplace with essentially no gap. These are population-level medians and the variation around each sector average is substantial, but the sector choice itself is about as consequential as the firm choice.

For a policymaker: three years is too short to know whether the Gender Pay Gap Information Act 2021 is working at the population level. What the data do show — with reasonable confidence — is that persistent reporting firms are narrowing their gaps, and that the narrowing is not an artefact of the threshold phase-down. The durable policy lever the data identifies is sector-specific action plans in the persistent high-gap sectors of construction, finance, manufacturing, and energy.

For an employer: the firms that narrowed their gap between 2022 and 2025 did so inside a regulatory regime that simply requires publication. The mechanism is likely a combination of reputational pressure, comparison with peer firms once numbers are in the open, and internal review processes triggered by having to compile the figures.

## How We Did It

We used the [paygap.ie](https://paygap.ie) archive — an independent public-service portal that has scraped and aggregated Irish gender-pay-gap filings since 2022 — covering 3,991 employer-year submissions from 1,712 unique companies. We tracked the median gap year by year, restricted attention to firms that reported in both the first and latest year (the within-firm panel), decomposed the population shift into within-firm, entrant, and exit components, and compared Ireland against three matched windows of UK data. Confidence intervals came from a cluster bootstrap over firms.

## Further Reading

- [paygap.ie](https://paygap.ie) — the independent aggregator of Irish gender pay gap reports
- [Gender Pay Gap Information Act 2021](https://www.irishstatutebook.ie/eli/2021/act/20/enacted/en/html) — the statutory basis of the disclosure regime
- [UK Gender Pay Gap service](https://gender-pay-gap.service.gov.uk/) — the cross-country comparator
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_gender_pay_gap/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
