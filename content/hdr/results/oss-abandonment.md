---
title: "To predict if an open-source project will die, watch who you watch"
date: 2026-04-17
domain: "Software Engineering"
blurb: "Fifteen years of research have tried to predict which open-source projects will quietly die. The hard part is not the model. It is the crowd you pick to model in the first place."
weight: 40
tags: ["open-source", "software-supply-chain", "github", "prediction", "null-result"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/oss_abandonment/paper.md) has the cohort-definition comparisons and the feature ablations. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** When you predict whether a living open-source project will be dead in a year, what drives the forecast is not any clever signal about the project. It is how you define "living project" in the first place. Tighten that definition and easy gains vanish; every feature we invented was essentially noise on top of that decision.

## The Question

Modern software is built on mountains of open-source code, maintained — often — by one or two volunteers. When those maintainers quietly walk away, the consequences are not small: the xz-utils backdoor of 2024, the Log4j crisis of 2021, and a long list of other incidents all trace back to under-resourced projects. A natural question follows. Can you look at a repository's public activity today and forecast whether it will still be alive in a year?

The research literature has tried for fifteen years. We wanted to see how far you get using nothing but the free, public event stream that GitHub publishes for anyone to download — no special access, no private data.

## What we found

The biggest predictor of whether a project gets abandoned is not any fancy feature of the project itself. It is how you define what counts as a "live project" to begin with.

- Watching every repository with even a single commit in a three-day window produced a crowd dominated by one-off tutorials, new-year resolutions, and homework assignments — most of them already effectively dead.
- Tightening the watch-list to repositories with ten or more real human commits in that window raised prediction quality by seven percentage points on our main ranking metric.
- Adding a second filter — flag a project as abandoned only when its activity drops by more than ten-fold year over year — produced the best model we built.
- By contrast, every individual feature we engineered — popularity, engagement patterns, bot ratios, issue-response rates — moved the needle by essentially nothing.
- No single feature family was load-bearing. Strip any one of them and the model barely notices.

## Why that matters

A decade of research on this problem has focused on feature engineering — squeezing better signals out of the same data. The working assumption is that a smarter analysis of a project's behaviour will unlock better forecasts. Our result flips that frame. The honest bottleneck is not the analysis, it is the population. Most of the repositories on GitHub that the literature scores against are not really "projects" in any meaningful sense. Including them makes the problem look easier than it is — because predicting that an abandoned tutorial will stay abandoned is trivial — and simultaneously makes real progress invisible, because the signal from genuine projects is buried in noise.

Once you restrict attention to projects that actually have a pulse, the baseline is honest, and the marginal value of clever features collapses.

## What it means in practice

**For anyone building an early-warning system for critical open-source dependencies.** Security teams, foundations, and package-manager operators should spend their effort on defining the watch-list, not on engineering exotic features. A short, defensible definition of "this is a real project" beats a long list of signals applied to the whole firehose.

**For researchers.** Benchmark improvements on an inflated population are not the same as real progress. A two-percent gain on a population where 95 percent of rows are already abandoned tutorials is not two percent of anything useful. The honest benchmark is a curated cohort.

## How we did it

We built our panel from [GH Archive](https://data.gharchive.org), the public, free stream of GitHub's event timeline. We defined a cohort of projects active in a three-day window and checked which of them had gone silent one year later, then trained a tree-based ranking model to separate the survivors from the abandoned. The comparison that matters is not model against model — it is cohort-definition against cohort-definition.

## Further reading

- [GH Archive](https://data.gharchive.org) — the public event-stream dataset.
- Valiev, Vasilescu, and Herbsleb (2018). "Ecosystem-level determinants of sustained activity in open-source projects".
- Avelino et al. (2019). "A novel approach for estimating Truck Factors".
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/oss_abandonment/paper.md).
