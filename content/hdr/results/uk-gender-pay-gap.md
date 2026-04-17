---
title: "Nine Years of UK Gender Pay Gap Reporting: Has the Gap Actually Moved?"
date: 2026-04-17
domain: "Labour Economics"
blurb: "In April 2017 the UK made every employer with 250 or more staff publish their gender pay gap annually. Nine full reporting cycles later, the gap has narrowed — but more slowly than a back-of-envelope reading of the numbers suggests. At the current rate, closing the gap entirely is a 40 to 55 year project, not the 30-year horizon a naive calculation implies."
weight: 14
tags: ["labour-economics", "uk", "pay-equity", "policy-evaluation", "disclosure"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/uk_gender_pay_gap/paper.md).*

## The Question

In April 2017 the UK became one of the first countries to require every employer with 250 or more staff to publish six gender pay gap measures every year. The policy's theory was that sunlight would do the work: naming the gap publicly, in every company, every year, would produce internal pressure to narrow it. Nine full reporting cycles have now been filed, covering almost 94,000 employer-year submissions from roughly 22,500 unique employers.

The obvious public question: has the gap actually moved?

## What We Found

Yes, but more slowly than the headline figures suggest, and the truest signal is inside companies that have reported every year.

- The median gap across all reporting employers fell from 9.3 percent in 2017 to 8.1 percent in 2025 — a narrowing of 1.19 percentage points, with a confidence interval that excludes zero.
- Among more than 5,000 employers that reported under the same name in both 2017 and 2025, the median within-firm reduction was 2.10 percentage points — nearly twice the population-wide figure. 61 percent of these persistent employers narrowed their gap.
- Once the unusual 2019-2021 COVID reporting regime is properly accounted for, the underlying trend is 0.15 to 0.20 percentage points per year — noticeably slower than the 0.25 per year a simple endpoint calculation suggests. At this rate, closing the gap entirely is a 40 to 55 year project.
- The very largest employers (20,000 or more staff) have the smallest gaps, around 5 percent. The "just over the threshold" band (250 to 999 staff) has the largest, around 9 percent.
- Employers filing their returns late had smaller gaps than on-time filers in every mandatory size band (a roughly 2 percentage point difference after controlling for size and year), but this pattern reverses among smaller firms that report voluntarily.
- Public Administration, Information/Communication and Construction narrowed fastest. Education moved the other way — the population median Education gap nearly tripled, from about 10 percent to 23 percent. This is almost entirely a composition effect: as Multi-Academy Trusts crossed the 250-employee threshold, far more school-associated employers entered the reporting pool, and schools have a strongly female workforce with a male-dominated senior-leader stratum.

## Why That's Surprising

The most surprising finding is the gap between two plausible-sounding numbers: 0.25 percentage points a year (endpoint to endpoint) and 0.15 to 0.20 percentage points a year (once the COVID reporting regime is handled). The first number gets a 30-year horizon to parity. The second gets a 40 to 55 year horizon. Half of any progress claim rests on which of those is quoted.

The Education finding is the other surprise. Read as a headline, "the Education pay gap tripled during mandatory disclosure" sounds like a scandal. The actual story is that the population of Education employers reporting under the regime roughly tripled as academy trusts consolidated past the threshold, and the sector's baseline composition drags the aggregate upward. Inside existing Education employers, the picture is much less dramatic. The right lesson is about how much apparent sectoral progress is real versus compositional.

A third surprise is the late-filer pattern. Inside the mandatory reporting population, late filers are consistently the employers with smaller gaps — not larger, as a compliance-framed intuition would suggest. Whatever is happening, it is not "the laggards are the offenders".

## What It Means

For workers, the headline that the UK gender pay gap is narrowing is correct, but the rate of progress is slow enough that today's entrants will not see the gap close during their careers under the existing regime.

For policy design, the results suggest that mandatory disclosure has produced real within-firm movement (persistent employers narrowing by roughly twice the population rate), but the wider headline figure is diluted by compositional churn. Strengthening the regime — lowering the threshold, mandating action plans, reporting by ethnicity and disability, linking to procurement — is a credible response.

For analysts reading disclosure data, the Education case is a general cautionary tale. When a sector's reporting population triples over the study window, the sector-level median is a composition story before it is a progress story. A within-firm-only sectoral breakdown is the appropriate follow-up.

## How We Did It

The analysis pulls every annual CSV from the [UK government's Gender Pay Gap Service](https://gender-pay-gap.service.gov.uk/) for reporting years 2017-18 through 2025-26 — 93,777 submissions from about 22,500 employers. Population-level trends, within-firm paired changes, compliance patterns, employer-size stratification, and a first-digit industry classification decomposition are reported with bootstrap confidence intervals, alongside a non-parametric significance test on the paired within-firm delta and three alternative ways to handle the COVID reporting years.

## Further Reading

- [UK Gender Pay Gap Service](https://gender-pay-gap.service.gov.uk/) — the public reporting portal
- [Equality and Human Rights Commission guidance](https://www.equalityhumanrights.com/en/advice-and-guidance/gender-pay-gap-reporting) — the regime's oversight authority
- [Full technical write-up](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/uk_gender_pay_gap/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
