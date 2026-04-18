---
title: "The Pentagon's UAP Cases: What the Numbers Actually Say"
date: 2026-04-18
domain: "Data Science"
blurb: "The Pentagon's AARO office has received 1,652 UAP reports. Of the 292 resolved or recommended for closure, every single one turned out to be something mundane — balloons, birds, drones, satellites, aircraft. The 21 cases that merit further intelligence analysis represent 2.8% of intake — exactly in line with the historical 3-6% 'unidentified residual' from prior programs. A Bayesian analysis gives an unresolved case only 4.3% posterior probability of being genuinely anomalous. The data is fully consistent with a world in which the entire residual is explained by sensor limitations, not exotic phenomena."
weight: 22
tags: ["UAP", "UFO", "AARO", "Pentagon", "Bayesian", "base-rate"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/aaro_case_resolution/paper.md). Companion to the [NUFORC sighting patterns](/hdr/results/ufo-sighting-patterns/) analysis.*

## What AARO has

The All-domain Anomaly Resolution Office (AARO) has received **1,652 cumulative UAP reports** as of June 2024. Of these:
- **292 resolved or recommended for closure** (17.7%) — every one prosaic
- **21 merit further IC/S&T analysis** (2.8% of total — the "interesting" ones)
- **~1,360 remain in the open backlog**

## Every resolved case is mundane — but that's partly selection bias

100% of resolved cases turned out to be balloons, birds, UAS (drones), satellites, or aircraft. But this is the easy fraction — cases with clear sensor data that allows identification. The 82.3% that remain open are mostly data-insufficient (poor sensor coverage, brief observation, no corroboration), not "confirmed anomalous."

The distinction matters: **unresolved ≠ anomalous.** Most open cases are open because the data is bad, not because the object is exotic.

## The backlog is growing, but not as fast as headlines suggest

AARO receives about 37 current-period cases per month and resolves about 22. That's a 1.7x intake/resolution gap — the backlog grows, but slowly. The headline "757 new cases" includes 272 catch-up reports from prior periods (36%), which inflates the apparent intake rate.

## The "unidentified residual" matches historical base rates

Every major UAP investigation program converges on a similar residual:
- **Project Blue Book** (1952-1969): 5.6% unidentified after investigation
- **Hendry study** (1979): 11.4% (less rigorous methodology)
- **GEIPAN (France)**: 3.5% unidentified
- **AARO 21 IC-merit cases**: 2.8% of intake

AARO's residual is **exactly where you'd expect** if the phenomenon is prosaic objects observed under poor conditions.

## Bayesian: 4.3% posterior probability of "anomalous"

Starting from a 5% prior (generous — assumes roughly 1 in 20 unresolved cases might be genuinely novel), and updating with the likelihood ratio from AARO's resolution data:
- P(unresolved | prosaic) = 0.587 (most prosaic objects go unresolved due to bad data)
- P(unresolved | anomalous) = 0.5-1.0 (range — anomalous objects might also produce good data)

The posterior probability that any given unresolved case is genuinely anomalous: **4.3%** (at P(unresolved|anomalous)=0.5). This is BELOW the prior — the AARO data actually makes "anomalous" LESS likely, not more, because the high rate of prosaic cases going unresolved dilutes the signal.

## What the data cannot answer

Whether the 21 IC-merit cases contain something genuinely novel depends on classified sensor data that the public reports don't contain. The limiting factor is not methodology but instrumentation — until purpose-built calibrated sensors (AARO's planned GREMLIN system) capture multi-modal data at the moment of observation, most cases will remain data-insufficient.

## How we did it

Systematically extracted every quantitative figure from AARO FY2024 and ODNI 2022 reports. Built a resolution-rate model, backlog-growth projection, base-rate comparison against historical programs, and two-dimensional Bayesian posterior surface over prior and likelihood assumptions. Phase 2.75 reviewer caught: Bayesian likelihood error (P(unresolved|anomalous)=1.0 was too strong), backlog ratio inflation (catch-up reports in denominator), and selection-bias diagnostic missing. All corrected. Phase 3.5 signoff cleared.
