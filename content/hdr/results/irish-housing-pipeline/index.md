---
title: "Where Do Irish Housing Permissions Actually Go?"
date: 2026-04-16
domain: "Irish Housing"
blurb: "Between 2019 and 2025 Irish planning authorities granted permission for roughly 267,000 housing units. In the same window, 167,000 houses were actually completed. We built the pipeline and measured what fraction of permissions turn into finished houses. The two-year conversion rate has actually climbed from 41 percent in 2019 to 65 percent in 2022 — the system is getting better at turning permissions into homes, not worse. But permissions themselves have been remarkably flat at 32 to 43 thousand per year, and that is the number that would have to double to hit the government's 50,500-home annual target."
weight: 12
tags: ["housing", "ireland", "planning-permissions", "housing-crisis"]
---

*Plain-language summary. Full technical write-up in the [analysis script](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_housing_pipeline/analysis.py).*

## The question

Every month the press reports a "housing permissions" number, usually comparing it to the government's 50,500-home-per-year target under Housing for All. These are two very different numbers: permissions are what councils and An Bord Pleanála say developers are allowed to build, and completions are what actually got built. The gap between them is a mix of objections, finance, labour, materials, design revisions, and straight-up developer delay.

**Are Irish permissions actually getting built, or is the system stockpiling approvals that never produce houses?** And has that changed as the housing crisis has intensified?

## What we found

### The pipeline, year by year

Central Statistics Office tables BHQ15 (planning permissions 2019-2025, with a useful strategic-vs-non-strategic split) and NDA12 (new-dwelling completions 2012-2025, aggregated across 867 named towns and cities) give the two stages:

| Year | Permissions granted | Completions | 2-year conversion (T → T+2) |
|---:|---:|---:|---:|
| 2019 | 38,461 | 15,935 | **41%** |
| 2020 | 42,371 | 15,583 | 54% |
| 2021 | 42,991 | 15,624 | 57% |
| 2022 | 34,177 | 22,704 | 65% |
| 2023 | 41,225 | 24,316 | 61% |
| 2024 | 32,401 | 22,136 | — |
| 2025 | 34,974 | 25,237 | — |

Two things stand out.

**Completions have nearly doubled.** From 15,935 in 2019 to 25,237 in 2025. The building system is genuinely delivering more houses than it was five years ago.

**Permissions have been flat.** Every year between 2019 and 2025 Irish planning authorities issued between 32,000 and 43,000 unit permissions. There is no long-term upward trend. Given the government target of 50,500 completions per year, this is the bottleneck: even at 100 percent conversion, the current permissions flow would not deliver the target.

**The conversion rate has improved substantially.** Permissions issued in 2019 produced completions in 2021 at a 41 percent two-year ratio. Permissions issued in 2022 produced completions in 2024 at a 65 percent ratio. The Irish housing-delivery system is turning a larger share of permissions into houses than it was five years ago — **not the stockpile-and-never-build story that is sometimes told**.

### The SHD window was not obviously more productive

The Strategic Housing Development (SHD) scheme, which ran from late 2017 to late 2021, was designed to fast-track developments over 100 units through An Bord Pleanála instead of local councils. Its permission counts are separately identifiable in the data:

- 2019-2021 SHD permissions: **60,605 units**
- 2019-2021 Non-SHD permissions: **63,218 units**
- Two-year-lagged completions (2021-2023): **62,644 units**

Roughly half of the 2019-2021 permissions completed within two years. The split between SHD and non-SHD permissions is almost exactly 50-50, which suggests the fast-track did pull a comparable volume through — but not dramatically more than conventional permissions running in parallel.

## What we cannot say from this data

- **Not per-permission tracking.** The data gives annual permission counts and completion counts, not case-level matching. "61 percent converted" is an aggregate ratio, not a tracking of specific permissions to specific homes. Some permissions from 2022 will still complete in 2026 or 2027.
- **Not cancellation.** Some permissions expire without being built. The data doesn't tell us how many.
- **Not cost or tenure.** These are unit counts irrespective of price, rent, or whether the units are social, affordable, or market housing.
- **Not judicial review blocks.** The SHD scheme was killed by the high rate at which ABP decisions were quashed in the High Court. A separate paper on SHD judicial reviews will identify that channel specifically.

## What it means

For a commuter watching the housing crisis: the good news is that completions are rising materially year on year and the conversion of permissions to homes is more efficient now than it was five years ago. The bad news is that the number of permissions being issued has not grown — and the government target cannot be met at current permission rates.

For a policymaker: the chokepoint is not "developers aren't building what they're permitted to build." The chokepoint is permission volume itself. Policies that aim to increase completions by pressing on the conversion side of the funnel are pushing on a mechanism that has already been improving; policies that aim to increase permissions by reforming the planning system are pushing on the actual bottleneck.

## How we did it

Downloaded CSO PxStat table BHQ15 (Planning permissions granted for apartment, multi-development and all-house units, with Strategic Housing Development split, quarterly 2019-2025) and NDA12 (New Dwelling Completions by urban area × house type, annual 2012-2025). Aggregated BHQ15 across quarters to annual, avoiding double counting between "Apartment units" and "All house units", and aggregated NDA12 across all 867 named areas under "All house types". Computed the two-year lagged conversion ratio. No modeling.
