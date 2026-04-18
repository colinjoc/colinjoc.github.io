---
title: "147,890 UFO reports: what the data actually shows"
date: 2026-04-18
domain: "Data Science"
blurb: "The largest independent database of UFO reports has patterns in it. The question is whether those patterns are about the skies — or about us."
weight: 21
tags: ["UFO", "UAP", "NUFORC", "citizen-science", "reporting-bias", "Starlink"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ufo_sighting_patterns/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** UFO reports in the United States peaked in 2014 and have been falling since. The arc tracks internet adoption almost perfectly, not any change in the skies. The iconic "flying saucer" is being replaced in the public imagination by the "orb" — and the shift is driven by the words people have available, not by what they see. Starlink satellite trains produce a real but modest bump in formation sightings, and the highest per-person reporting rates come from rural dark-sky states, not military hotspots.

## The Question

The National UFO Reporting Center has been collecting reports from ordinary people since 1974. Over the past three decades, it has amassed 147,890 text-level reports — the largest independent, freely downloadable record of its kind. Enough volume that statistical patterns should be visible.

This is not a "do UFOs exist" study. It is a reporting-pattern analysis. A cluster of sightings near a military base could mean unusual aircraft, or it could mean people near bases look up more often. We measure the patterns and let the reader decide what the patterns are about.

## What we found

- **Reports peaked in 2014 and the rise tracks the internet.** Annual reports grew from around 500 a year in 1990 to about 8,800 in 2014, then fell to roughly 4,200 by 2023. The rising phase correlates with US internet penetration almost one-to-one. The rise-and-fall is the shape of a new reporting channel going mainstream, not a change in the sky overhead.
- **The "flying saucer" is being replaced by the "orb".** The classic disk or saucer shape fell from about ten percent of reports in the 1990s to about six percent in the 2020s. Over the same period, "orb" rose from about two percent to nine percent. "Light" has stayed dominant throughout at 22 to 25 percent.
- **The shift is cultural, not optical.** The word "saucer" inside the report text matches disk-shape reports almost perfectly year to year; the word "orb" matches orb-shape reports even more tightly. People describe what they see using the vocabulary of their era. The archetype has shifted from metallic craft to luminous sphere.
- **Starlink: real but modest.** An interrupted time-series analysis shows a statistically significant increase in "formation" sightings after SpaceX began launching Starlink satellite trains in 2019 — about 30 percent above baseline. But formations only went from 3.5 to 4.4 percent of monthly reports, and the effect is already fading as people learn to recognise Starlink on sight.
- **Hotspots are rural dark-sky states, not military zones.** After normalising by population, the highest per-capita reporting rates are in Washington (94.6 per hundred thousand), Vermont (94.2) and Montana (92.3) — northern, rural, dark-sky states. Texas (21.2) and Georgia (25.4) are at the bottom. A spatial regression finds the residual is explained by sky darkness and latitude, not proximity to military bases.

![Annual sighting reports 1990-2024 vs internet adoption.](plots/annual_trend.png)

## Why that matters

The NUFORC data are not evidence about what is in the sky. They are evidence about what people notice, what they are willing to report, and what vocabulary they have for describing it. Three of our findings pin that down. The fact that reports track internet adoption means the database's growth was driven by reporting friction falling, not by an increase in events. The fact that the shape people report correlates almost perfectly with the shape-word they use means the cultural archetype drives the perception. And the fact that hotspots line up with dark skies rather than with military installations means even the geographic pattern is an artefact of observer conditions.

![Shape evolution over decades.](plots/shape_evolution.png)

None of this tells you whether any particular sighting is real. But it does tell you that when a journalist reports "UFO sightings are on the rise" or "the Pacific Northwest is a hotspot", the headline is mostly about the observers, not about whatever is or isn't above them.

## What it means in practice

**For journalists and commentators.** The raw trend line in NUFORC reports is not a signal about the sky. If you want a time-series of UFO events, you have to de-trend by at least internet penetration and, ideally, by Starlink launches. The per-state ranking needs at minimum a population and dark-sky correction. Without those, the story is about reporting channels and light pollution, not UFOs.

**For defence and aviation policy.** The classifier trained to predict which reports would receive explanations performed no better than random — 99.46 percent of reports remain unannotated, and the ones NUFORC does explain are mostly short and uninformative. The database is not a useful input for operational filtering of anomalous aerospace activity.

**For researchers and citizen-science database designers.** Reporting databases like this one are dominated by observer-side effects — internet access, cultural vocabulary, light pollution, time of day. A serious anomaly-detection system would need to log viewing conditions, observer density, and at minimum the phase of major cultural media cycles before attempting to extract signal. NUFORC's 50-year corpus is a treasure for sociology and for studying how the public notices unusual things. It is not a detector.

## What this does not establish

This is not a claim that UFOs are or are not real. It is not a claim that all sightings are misidentifications — only a fraction of one percent of reports have any annotation at all. And NUFORC is not a nationally representative dataset; it is a self-selected volunteer database, heavily US-biased.

## How we did it

We parsed 147,890 structured reports from the [NUFORC archive on HuggingFace](https://huggingface.co/datasets/kcimc/NUFORC) plus 80,332 geocoded reports from the [planetsig/ufo-reports dataset](https://huggingface.co/datasets/planetsig/ufo-reports). The analysis used time-series decomposition for the trend, negative binomial spatial regression for per-state rates (Poisson was rejected because the data is overdispersed), interrupted time-series analysis for the Starlink step change, a tree-based classifier for the explained-versus-unexplained question, and text-feature correlation for the cultural-archetype analysis.

## Further reading

- National UFO Reporting Center — the [NUFORC archive](https://nuforc.org/) is the raw data source.
- Federal Aviation Administration & Department of Defense (2021-2024), *Unidentified Aerial Phenomena Reports to Congress* — the official government-side perspective, for contrast.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ufo_sighting_patterns/paper.md) — all statistical tests and the full dataset pipeline.
