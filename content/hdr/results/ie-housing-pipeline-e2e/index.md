---
title: "How many Irish planning permissions become certified homes?"
date: 2026-05-08
domain: "Irish Housing"
blurb: "For every 100 Irish residential planning permissions granted, only about 35 produce a certified home — and roughly 60 produce a built one. The gap is mostly paperwork."
weight: 35
tags: ["housing", "ireland", "planning-permission", "completion", "pipeline", "policy"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline_e2e/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Tracking 66,163 Irish residential planning permissions granted from 2014 to 2019 cohort-by-cohort, only about 35 in every 100 end up with a Certificate of Completion and Compliance. Once self-built homes that are legally exempt from filing are counted in, the build rate rises to roughly 60 in 100. Either way, hitting the Housing for All target of 50,500 homes per year requires somewhere between 85,000 and 144,000 permissions annually — more than double the current rate of about 38,000.

## The question

Ireland's housing crisis is usually described in headline numbers — permissions granted, completions counted, the gap between them. What has been missing is a cohort-tracked answer to a simple question: if you take a real planning permission granted in a real year, how likely is it to end up as a real, occupied home? And what shape does the journey from paper to keys actually take? This study follows the residential 2014-2019 cohort all the way through Ireland's three-stage building-control register — permission, commencement, completion certificate — and asks where the drop-offs really happen.

## What we found

![Pipeline funnel: permissions to commencement to completion certificate, with opt-out self-builds shown separately.](plots/headline_finding.png)

- Of every 100 residential permissions granted between 2014 and 2019 (n=66,163 permissions, 85,565 commenced projects), about 90 had a commencement notice filed within the tracking window. The remaining roughly 10 lapsed — permission granted, ground never broken.
- Of those 90 starts, only about 41 went on to file a Certificate of Completion and Compliance, the regulatory sign-off introduced under the Building Control Amendment Regulations of 2014. That works out to a certified yield of roughly 35 homes per 100 permissions, with a confidence range of about 33 to 37.
- About a third of all commenced projects are one-off self-builds that opted out of the certification regime. They are built and lived in, but never appear in the certificate count. Adding them back gives an estimated build yield of roughly 60 homes per 100 permissions.
- Among scheme housing — the multi-unit developments that cannot opt out — the certified yield rises to about 51 homes per 100 permissions.
- Scheme size is the strongest single predictor of certificate filing. Single-unit projects file a certificate only about 12 percent of the time, mostly because they are dominated by opt-out self-builds. Schemes of 50 units or more file at about 89 percent.
- The median journey from permission granted to certificate filed is 1,096 days — three years on the dot. Half of all projects fall between 1.9 and 4.7 years. The first leg, permission to commencement, takes a median of 234 days. The construction-and-certification leg takes a median of 496 days.
- Local Authority filing rates range from about 8 percent to about 68 percent — a roughly eight-fold spread that hints at large institutional differences in how the regime is administered.
- Approved Housing Body schemes file completion certificates at about 72 percent versus about 40 percent for private schemes. Multi-phase developments file at about 85 percent versus about 27 percent for single-phase. Permissions extended under Section 42 file at about 68 percent versus about 39 percent for non-extended.

## Why that matters

The headline figure of "35 homes certified per 100 permissions" sounds catastrophic next to international benchmarks of 80 to 90 percent. It mostly is not. Most of the missing 65 are not abandoned projects — they are self-built family homes that exist physically but were exempt from the certification regime. Once that measurement gap is closed, Ireland sits in the lower-middle of its peer group.

That distinction matters enormously for policy. If the certified yield is the right denominator, Ireland needs roughly 144,000 permissions per year to hit 50,500 homes. If the build yield is the right denominator, it needs roughly 85,000. The Housing for All target is measured by Electricity Supply Board meter connections, which do count opt-out homes — so the build yield is the right comparator, and 85,000 is the right number to argue about. Either way, current permission volumes of about 38,000 per year are less than half of what is needed.

The second lesson is where the binding constraint actually sits. Halving the lapse rate would add only a few hundred completions per year. Lifting the certificate-filing rate by ten percentage points would add about 3,300. Lifting permission volume to 60,000 per year — still well below the implied target — would add roughly 7,700. Permission volume is the lever with by far the largest marginal effect. The pipeline is not where the system is broken.

## What it means in practice

**For homebuyers.** A typical residential planning permission, once granted, takes about three years to become a certified home — eight months to ground being broken, then about sixteen months to certification. One in four projects takes more than four and a half years. If you are watching a specific scheme, the start of construction is the milestone that signals the project is genuinely live.

**For builders.** Single-phase, single-unit projects are by far the lowest-filing cohort, which is partly a regulatory artefact. Multi-phase scheme housing — and Approved Housing Body schemes in particular — file at much higher rates. Local Authority differences are large enough that where you build appears to matter as much as what you build for sign-off compliance.

**For policymakers.** The pipeline does not need a major efficiency drive. The first-stage lapse rate of about 10 percent is real but small. The certificate-filing gap is mostly an opt-out measurement issue, not a delivery failure. The binding constraint for the Housing for All target is permission volume, which sits upstream of the pipeline entirely. A second, lower-cost reform would be to mandate certificate filing for all residential construction, including self-builds — this would not build any extra homes, but it would close the measurement gap and give policy a single, unambiguous denominator.

## How we did it

This study synthesises four predecessor cohort projects into a single end-to-end pipeline yield estimate. The data spine is the Building Control Management System, the national register of commencement notices and completion certificates, joined conceptually to the national planning register and the Central Statistics Office completion series. The cohort definition is residential permissions granted between 2014 and 2019, ensuring at least six years of follow-up.

The yield is built up stage by stage. The lapse rate at the permission-to-commencement transition comes from a cluster-bootstrap analysis of the planning register. The certificate-filing rate at the commencement-to-completion transition comes from the building-control register, decomposed by opt-out status. The completion-to-occupied rate is estimated from the ratio of Central Statistics Office completions to building-control certificate counts over 2019-2023, which suggests virtually all certified homes are occupied — and that the regulator under-counts rather than over-counts. Five model families were compared as a robustness check; a stage-by-stage product model was retained as primary, with a survival model kept as a framework recommendation for future work with richer covariates.

A failed apartment-versus-dwelling stratification was diagnosed and withdrawn after audit revealed the apartment flag matches zero rows in the building-control register — the underlying field-keyword vocabulary does not include "apartment" or "flat", so any apartment-specific finding from this dataset would have been spurious.

## Further reading

- [Building Control Management System](https://www.localgov.ie/en/link-type/bcms) — the commencement and completion register used throughout.
- [Central Statistics Office BHQ15 — Planning permissions granted](https://data.cso.ie/table/BHQ15).
- [Central Statistics Office NDA12 — New dwelling completions](https://data.cso.ie/table/NDA12).
- [Housing for All — Government of Ireland (2021)](https://www.gov.ie/en/publication/ef5ec-housing-for-all-a-new-housing-plan-for-ireland/).
- [Land Development Agency Annual Reports](https://lda.ie/publications/annual-reports/).
- [End-to-end pipeline yield — full paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline_e2e/paper.md).
