---
title: "Predicting Open-Source Death: The Question Matters More Than the Model"
date: 2026-04-14
domain: "Software Engineering"
blurb: "We tried 23 different ways to predict which active open-source projects would go silent within a year. Engineering better signals barely moved the needle. The single biggest improvement came from being more careful about which projects counted as 'active' in the first place."
weight: 4
tags: ["open-source", "software-engineering", "github", "negative-result", "hdr", "supply-chain"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/oss_abandonment/paper.md).*

## The Question

Every few years, a piece of software that millions of people depend on quietly falls apart. The xz compression tool was almost hijacked through its burned-out solo maintainer. The Log4j logging library — used by nearly every large company's servers — was maintained by three unpaid volunteers when a devastating security flaw was found. The left-pad library, just eleven lines of code, briefly broke thousands of websites when its sole author pulled it from the internet.

These crises share a pattern: critical software, maintained by one or two people, with no one watching for signs of trouble. So we asked a simple question: given a year of public activity data for an active open-source project, can we tell whether it will still have a pulse twelve months later?

## What We Found

The biggest surprise: defining "active" carefully was worth more than every other improvement combined.

- Tightening which projects counted as genuinely active — rather than including every repository with a single commit — improved predictions by 7.6 percentage points across 23 experiments.
- All 22 attempts to engineer better predictive signals (commit patterns, contributor concentration, engagement ratios, popularity metrics) moved the needle by less than 0.2 percentage points each.
- Stripping the model down to just six basic activity measures barely hurt predictions — the other eleven signals contributed almost nothing collectively.
- When we narrowed the pool to repositories with substantial recent activity, the "abandonment" rate dropped from 95% to 82%, and the model's ability to separate the doomed from the surviving jumped dramatically.
- The practical output isn't a prediction score — it's the filtered list of roughly 14,000 projects that meet a stringent activity bar and whose forward activity dropped by more than 10 times.

## Why That's Surprising

A decade of research on open-source health has focused on building better features: contributor concentration (how many people would need to leave before the project stalls), engagement metrics, sentiment analysis, network position, even personality profiles of maintainers. The implicit assumption is that if you measure enough things about a project, you can see abandonment coming.

Our 23-experiment search found that assumption is backwards — at least for short-horizon prediction using public event data. The real problem wasn't measuring the right things; it was measuring them for the right projects. When 95% of your "active" repositories are tutorials, homework assignments, and abandoned New Year's resolutions with a single commit, no amount of clever engineering can extract a meaningful signal. Narrow the aperture to genuinely active projects, and even a simple model with six features does nearly as well as the fully loaded version.

## What It Means

If you're a company that depends on open-source software — and you almost certainly are — this finding reframes where to invest monitoring effort. Don't build increasingly elaborate dashboards tracking dozens of health metrics across every repository in your dependency tree. Instead, identify the projects that are genuinely active and critical to your stack, then watch a handful of simple signals: are humans still committing? Are there multiple contributors? Is the pace holding steady?

For open-source funding bodies, the implication is similar: the hard problem is not ranking projects by fragility — it's deciding which projects belong in the ranking at all. A well-defined cohort of critical, actively-maintained projects is more actionable than a fragility score computed over half a million repositories that includes coding tutorials and abandoned side projects.

## How We Did It

We pulled 36 hours of public GitHub event data from [GH Archive](https://data.gharchive.org) spanning two three-day windows one year apart, covering 662,593 repositories with at least one human commit. After filtering out bot activity, we ran 23 single-change experiments through the Hypothesis-Driven Research loop — starting from a 230-citation literature review and a pre-registered queue of 120 hypotheses. The key finding emerged in Phase 2: cohort-definition experiments dominated every feature-engineering and model-tuning variant tested.

## Further Reading

- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/oss_abandonment/paper.md) — 23-experiment details, model tournament, and feature ablation results
- [GH Archive](https://data.gharchive.org) — the public GitHub event timeline used as the sole data source
- Census III of Free and Open Source Software (Linux Foundation / Harvard, 2024) — the dependency-concentration study that motivates this work

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
