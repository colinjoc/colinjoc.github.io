---
title: "Did Replacing Strategic Housing Development Reduce Judicial Reviews?"
date: 2026-04-16
domain: "Irish Housing"
blurb: "In 2021 Ireland replaced the Strategic Housing Development (SHD) regime with Large-scale Residential Development (LRD), partly to reduce judicial-review (JR) exposure. Three years on, the honest answer is: we cannot tell yet. Only two LRD-era judicial reviews have been fully decided at end-2024 (both conceded by the State). The 2023-2024 rise in LRD JR intake (3→7) is indistinguishable from a system-wide JR surge (+58%, with Commercial +150% and Infrastructure +850%). Any regime-effect claim from this data is below the detection floor; a clean test requires approximately 2027."
weight: 16
tags: ["housing", "ireland", "planning-permission", "judicial-review", "LRD", "SHD", "policy-evaluation"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_lrd_vs_shd_jr/paper.md).*

## The question

The companion [SHD judicial-review project](/hdr/results/irish-shd-judicial-review/) found that 14 of 16 SHD judicial reviews decided in 2018-2021 went against the State (87.5%, Clopper-Pearson CI 61.7-98.5%). The natural follow-up: **did the 2021 switch from SHD to Large-scale Residential Development (LRD) reduce judicial-review intensity?**

This was one of the stated motivations for the LRD reform: return first-instance decisions to Local Authorities, restore an appeals route, and reduce the share of big schemes ending up in the High Court under SHD's direct-to-ABP architecture.

## What we found

### The comparison cannot yet be defensibly made

The LRD regime began December 2021. Judicial reviews take 1-3 years to lodge, then 1-2 years to decide. By end-2024 — the latest ABP annual report — **only two LRD-era JRs have been fully decided**, and both were conceded by the State before a judgment (ABP 2024 Table 3). The LRD decided-outcome sample is n=2.

Two other denominators exist, and both have fatal problems when compared with SHD:

1. **Per-appeal-concluded LRD JR rate**: 10/116 = 8.62% (Wilson 95% CI 4.8-15.1%). But this counts JRs *received* (not decided) against a denominator of *LRD appeals* (not *LRD permissions*) — categorically different from the per-permission decided rate computed for SHD.
2. **Per-permission LRD JR rate**: unobtainable from ABP data. LRD restored first-instance decision to Local Authorities, so most LRD permissions are granted by LAs and never reach ABP. The Department of Housing (DHLGH) has not published an LA-by-LA LRD decision count.

The "SHD X% vs LRD Y%" comparison the policy debate wants cannot be constructed from public data as of end-2024.

![Left: decided JRs against residential schemes, SHD era (red) vs LRD era (blue) — only n=2 LRD cases decided to end-2024, both conceded. Right: 2023→2024 JR intake growth by scheme type — LRD grew 3→7 (133%), but Commercial grew 150% and Infrastructure grew 850%, so the LRD growth is not distinguishable from a system-wide trend.](plots/lrd_vs_shd_jr.png)

### The JR surge is system-wide, not LRD-specific

System-wide JR intake at ABP grew 58% from 2023 to 2024 (93 → 147 applications). Within that:
- **Commercial**: 14 → 35 (+150%)
- **Infrastructure**: 2 → 19 (+850%)
- **LRD**: 3 → 7 (+133%)

LRD's growth is indistinguishable from the system-wide pattern. Any regime-effect hypothesis has to compete with: the Heather Hill Supreme Court judgment (July 2022, lowered the Aarhus cost barrier to JR); the High Court Planning and Environment List (November 2022, shortened JR disposal times); and the 2024 State-concession spike (53 concessions vs 15 losses system-wide, possibly reflecting a new ABP defensive posture). At annual resolution with N=8 years of data and three concurrent interventions, the LRD-specific effect cannot be isolated.

### SHD-era baseline (from the companion project)

For context: on the aligned 2018-2021 cohort, the SHD decided-JR rate was 16 JRs against 392 SHD decisions — **4.08%, Wilson 95% CI 2.53-6.53%**. This is the honest SHD baseline (earlier drafts had stitched together misaligned numerators and denominators; see the [retroactively revised SHD paper](/hdr/results/irish-shd-judicial-review/)).

On a lodged-JR basis, press reporting puts SHD lodgement rates around ~8-9% — which is roughly consistent with the LRD 8.6% per-appeal-concluded rate, but again the denominators are not directly comparable.

## What this does NOT establish

- **Not a null finding.** "LRD did not reduce JR exposure" would require evidence that LRD rates were statistically indistinguishable from SHD rates. We don't have enough LRD cases to test that.
- **Not a positive finding either.** The available data are equally consistent with "LRD reduced JRs by 50%" and "LRD increased JRs by 50%" — the CIs are too wide.
- **Not a falsification of the reform rationale.** The LRD reform had other goals (LA primary jurisdiction, appeal route, decision speed) that this analysis does not touch.

## What it means

For policymakers and commentators: claims of the form "LRD has/hasn't reduced judicial reviews" are premature on public data to end-2024. **The earliest date at which a defensible comparison can be made is approximately 2027**, when the 2022-2024 LRD permission cohort will have fully passed the JR lodgement and decision windows. Even then, the comparison will be interpretable only if the three concurrent interventions (Heather Hill, Planning & Environment List, State concession pattern) are properly controlled — which requires case-level data, not annual aggregates.

For the Planning and Development Act 2024 implementation: the LRD reform was substantially re-architected in the 2024 Act before a single LRD judicial-review outcome had been publicly analysed. Policy moved ahead of evidence; whether the 2024 Act's further reforms are better-calibrated than the 2021 LRD reform is a question for ~2029.

## How we did it

Primary data: An Bord Pleanála annual reports 2020-2024 (JR intake, SHD/LRD appeal volumes, Table 3 substantive-outcome data), OPR Appendix-2 decided-JR schedule, OPR Legal Bulletins Issue 10 & 11 for LRD-era case discussion. Methods: Wilson and Clopper-Pearson binomial CIs; interrupted time-series with three concurrent-trend knots (Heather Hill, Planning & Environment List, 2024 concession spike) plus a Commercial-JR placebo series; Firth-penalised logistic regression and weak-prior Bayesian logistic for the small-N LRD outcome cell; difference-in-differences SHD vs LRD vs Commercial placebo. Ran through the full HDR pipeline including an independent Phase 2.75 blind reviewer (12 mandated experiments R1-R12 executed, three headline claims withdrawn including the "SHD 6.4% vs LRD 8.6%, p=0.51" stitch) and an independent Phase 3.5 signoff review.
