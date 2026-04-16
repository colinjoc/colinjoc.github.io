---
title: "How Many Irish Planning Permissions Actually Lapse Without Being Built?"
date: 2026-04-17
domain: "Irish Housing"
blurb: "About 9.5% of Irish residential planning permissions with known unit counts granted 2017-2019 show no commencement notice in the Building Control Management System (cluster-bootstrap 95% CI: 4.4-15.6%). An earlier draft reported 27.4%, but a blind reviewer found this was predominantly data-join failure (application-number format mismatches between the national planning register and BCMS), not genuine permission lapse. Cork County alone contributed 37% of apparent non-matches due to structurally incompatible number formats. The true non-commencement rate reduces actionable housing supply by roughly 5-15%, not the one-quarter originally claimed."
weight: 18
tags: ["housing", "ireland", "planning-permission", "lapse-rate", "policy-evaluation"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_lapsed_permissions/paper.md).*

## The question

Ireland grants roughly 35,000-40,000 residential planning permissions per year. How many of those permissions actually become construction starts? The difference — permissions that expire without the developer ever filing a commencement notice — is the "lapse rate," and it tells us how much of the headline permissions figure is genuinely actionable housing supply.

## What we found

### About 9.5% of residential permissions do not commence

On the cleanest available subsample — 18,403 residential permissions with known unit counts (NumResidentialUnits > 0) granted 2017-2019, matched against the BCMS commencement register — **9.5% have no commencement-notice match** (Wilson CI: 9.1-9.9%). Accounting for the clustered nature of the data (similar LAs have correlated match rates), the **cluster-bootstrap 95% CI widens to 4.4-15.6%**.

This is consistent with international comparables: UK permission lapse rates are typically 6-14%; New Zealand resource consent lapse rates are 10-20%.

### The original headline of 27.4% was mostly data-join failure

An earlier draft reported a 27.4% "lapse rate" across all 46,073 residential permissions 2014-2019. A Phase 2.75 blind reviewer demonstrated that this was predominantly measuring application-number format incompatibility between the national planning register and BCMS, not genuine permission lapse:

- **Cork County** alone contributed ~4,700 false "lapses" (37% of all non-matches nationally) due to structurally incompatible number formats
- Local Authorities using simple numeric formats (Carlow, Laois, Leitrim) showed 0% apparent lapse — not because every permission commenced, but because their formats match perfectly
- The gradient-boosting "champion" model (AUC 0.826) was 84.5% explained by the LA-encoding feature — it was predicting which LAs had compatible number formats, not which permissions actually lapsed. Stripped of format-proxy features, AUC collapsed to 0.583.

![Left: permission-to-commencement yield for the clean NRU>0, 2017-2019 cohort (90.5% commenced, 9.5% no match). Right: non-commencement rate by scheme size — larger schemes lapse more, consistent with real-options theory.](plots/lapse_analysis.png)

### Larger schemes lapse more — consistent with real-options theory

Non-commencement rates by scheme size (NRU>0, 2017-2019):
- **1 unit**: 9.1%
- **2-9 units**: 11.2%
- **10-49 units**: 14.5%
- **50+ units**: 18.8%

This gradient is consistent with the real-options literature: larger schemes have higher holding costs and more exposure to market-cycle risk, so developers are more likely to let permissions lapse if conditions deteriorate between grant and the commencement deadline.

## What this does NOT establish

- **Not a true lapse rate.** "No BCMS match" is a proxy for non-commencement, not a definitive measurement. Some non-matched permissions may have commenced under number formats we cannot reconcile; others may have been extended under Section 42 and commenced after 2019.
- **Not a causal model.** The scheme-size gradient is consistent with real-options theory, but we cannot disentangle intentional strategic delay from inability to secure finance, labour, or materials.
- **Not nationally representative.** The 9.5% figure is conditional on NRU>0 (only 40% of the register), so it excludes permissions where the register did not record unit counts — and those are disproportionately older applications from 2014-2016 when the register was less complete.

## What it means

For policy: the non-commencement rate reduces actionable housing supply by roughly 5-15%, not the one-quarter sometimes claimed. The 2025 Amendment Act (Section 28, allowing un-commenced extensions of up to 3 years) targets the right problem, but its impact is bounded by this relatively modest lapse rate.

For the Housing for All target: if 35,000 permissions are granted annually and ~9.5% lapse, roughly 31,700 commence. Not all of those will complete within a policy-relevant window (the companion [commencement-notice cohort](/hdr/results/irish-commencement-cohort/) project found median commencement-to-CCC of 498 days). The yield from permission to occupied home is addressed in the companion [end-to-end pipeline](/hdr/results/irish-housing-pipeline/) project.

## How we did it

Joined the national planning-application register (491,206 rows, all applications since 2012, from DHLGH open data) against the BCMS commencement-notice register (231,623 rows, from NBCO) on Application Number. Phase 2.75 blind reviewer found the join was dominated by format-mismatch artefacts; mandated 10 experiments (R1-R10) executed including formal join-failure audit, Cork County reconciliation, cluster-bootstrap CIs, and GBM feature-importance decomposition. The GBM "lapse predictor" was retracted (predicting format compatibility, not lapse). Full HDR pipeline with independent Phase 3.5 signoff (NO FURTHER BLOCKING ISSUES).
