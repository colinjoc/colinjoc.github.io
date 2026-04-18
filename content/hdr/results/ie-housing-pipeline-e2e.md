---
title: "For Every 100 Irish Permissions, How Many Become Homes?"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "Ireland's planning system is accused of losing two out of three permissions. Follow 85,565 projects from paperwork to front door and the real answer is closer to four out of ten lost — and most of that is a measurement artefact."
weight: 10
tags: ["housing", "ireland", "planning-permissions", "pipeline-analysis"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline_e2e/paper.md) has the stratification tables and sensitivity analysis. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** For every 100 residential planning permissions Ireland grants, about 60 end up as real homes with people living in them. Not the 35 the official paperwork implies. The gap between those numbers is mostly a quirk of which projects are legally required to file a completion certificate — not homes that were never built.

## The Question

Ireland's housing crisis has been narrated for a decade in aggregate numbers. So many permissions granted in one year. So many completions recorded a few years later. A gap between the two that everybody agrees is too large.

Nobody had actually followed permissions *through* the system. Of all the permissions a council granted today, how many become homes someone lives in? And where along the way are the others lost?

We built the first end-to-end estimate of that journey for Irish residential housing, following 85,565 projects granted permission between 2014 and 2019 from the moment the council said yes to the moment a completion certificate was filed.

## What we found

For every 100 residential permissions Ireland granted, **about 35 ended with a completion certificate on file — but about 60 ended as homes someone actually lived in**. The difference between those two numbers is the most important finding in this study.

- About 9 or 10 permissions out of every 100 never get started at all. The developer walked away. These are real losses.
- Of the 90 or so that do get started, only about 41 end up filing a completion certificate. That looks catastrophic. It isn't.
- Roughly a third of all started projects are one-off self-builds — someone building their own house. These are legally exempt from filing a completion certificate under the 2014 building-control rules. The home is built, it is connected to the grid, someone moves in. It just never appears in the certification database.
- Once you account for that exemption, the real build rate is closer to 60 percent. That is in line with the United Kingdom and with other comparable countries.
- The typical project takes just over three years from permission to certified completion. A quarter finish in under two years. A quarter take more than four and a half.
- The size of a scheme matters enormously. Single-unit projects file certificates about 12 percent of the time, because most of them are self-builds. Multi-unit schemes file 68 to 89 percent of the time, depending on size.
- Housing associations file certificates 72 percent of the time. Private developers file 40 percent. Multi-phase schemes file 85 percent. Single-phase schemes, 27 percent.

## Why that matters

The common reading of the Irish statistics — "the system loses two-thirds of its permissions" — turns out to be largely a measurement artefact. Roughly half of the apparent loss is paperwork that was never legally required in the first place, not homes that were never built. That changes the diagnosis of what is wrong with the pipeline, and therefore what would fix it.

The surprise runs in both directions. The optimistic side: Ireland's pipeline is not uniquely broken compared to its peers. The pessimistic side: even at the healthier 60 percent build rate, Ireland would need to grant roughly 85,000 permissions a year to hit the Housing for All target of 50,500 homes. Current permission volumes run at about 38,000 a year. Using the stricter certification-only yield, the figure rises to 144,000. Either way, it is far out of reach under current approval rates. The binding constraint is not how efficiently permissions turn into homes. It is how few permissions are being granted.

There is also a quieter finding in the statistical work. A reasonably sophisticated model designed to predict which individual permissions would eventually complete performed no better than random. With the data Irish councils record, the outcome of any single project is genuinely unpredictable. The pipeline yield is a property of the population, not of projects.

## What it means in practice

**For homeowners and buyers.** The realistic picture is closer to 60 homes out of every 100 permissions, not 35. The pipeline is leaky, but meaningfully less leaky than the headline numbers imply.

**For policymakers.** Chasing lapsed permissions or tightening the certification regime can each add a few thousand homes a year. But even combined, they cannot close the gap to the national target. The only route to 50,500 homes a year runs through granting more permissions and expanding the capacity of the construction sector to deliver them. A secondary win that is nearly free: extend the completion certificate requirement to self-builds. That alone would close the gap between the administrative statistics and the physical reality, and give everyone a clearer view of what is actually happening.

**For self-builders.** The finding is reassuring in one way: people who start a one-off home overwhelmingly finish it, even though the official paper trail disappears along the way.

## How we did it

We combined four data sources: the [Building Control Management System](https://nbco.localgov.ie/) (commencement and completion filings), the National Planning Application register, the [Central Statistics Office](https://data.cso.ie/) aggregate series, and the Land Development Agency's published delivery figures. For the cohort granted permission between 2014 and 2019 — giving us at least six years of follow-up — we estimated each stage of the journey independently (permission to start, start to certificate, certificate to occupied home) and combined them. We then checked the result with four unrelated modelling approaches and they all agreed.

## Further reading

- [Central Statistics Office — housing statistics](https://data.cso.ie/) — the aggregate permissions and completions data.
- [National Building Control Office](https://nbco.localgov.ie/) — the building-control filings.
- [Housing for All](https://www.gov.ie/en/publication/ef5ec-housing-for-all-a-new-housing-plan-for-ireland/) (Government of Ireland, 2021) — the 50,500-per-year target.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline_e2e/paper.md).
