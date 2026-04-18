---
title: "Humid Nights Do Not Predict Which Heat Waves Kill"
date: 2026-04-11
domain: "Public Health / Climate Hazards"
blurb: "A prominent climate-health hypothesis says warm, muggy nights are what turn heat waves deadly. On 13 years of city mortality data, the signal is not there."
weight: 21
tags: ["public-health", "climate", "heat-mortality", "wet-bulb", "hypothesis-testing", "negative-result", "early-warning-systems"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/heat_mortality/paper.md) has the 22 humidity encodings and the robustness checks. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Several countries are rebuilding their heat-wave warning systems around the idea that warm, humid nights are what make a heat wave lethal. On 13 years of mortality data across 30 American and European cities, that signal does not appear. Tracking the daytime extreme and how long it has lasted is still the best guide to which weeks will be deadly.

## The Question

When a heat wave turns deadly, what makes the difference? A prominent strand of climate-health research says the answer is the night. During the day your body overheats, but overnight cooling normally gives you a recovery window. If nights stay hot and humid enough that sweat can't work, the recovery window closes and people die. Laboratory experiments confirm that the human body hits a hard physiological wall at around 30.5 degrees Celsius of wet-bulb temperature — a measure that combines heat and humidity.

Several countries were in the middle of redesigning their heat-wave warning systems around this night-time signal when we started this project. We wanted to know whether it actually shows up in real city-level death data — because if it doesn't, retooling a warning system around it could make the warnings worse, not better.

## What we found

Across 30 cities in the United States and Europe, across 13 years of weekly deaths, the night-time humidity signal is not there at this scale. No version of it we tried.

- We pre-committed to 22 different ways of measuring overnight humidity before running anything. Twenty-one added nothing to the predictions. The one that did help turned out to be tracking how long the current heat wave has already been going, not the overnight conditions themselves.
- Stacking all 22 night-humidity measures into a single model made predictions worse, not better.
- The strongest predictors of deadly weeks were boringly simple: how many consecutive days crossed the local extreme-heat threshold, what happened last week, and what time of year it is.
- A stripped-down warning system using just two of those simple inputs performed nearly as well as the full 70-input model. Neither of the two involves night-time humidity.
- An alert system built around the proposed night-humidity rule would miss more deadly weeks and raise more false alarms than a system built around plain daytime temperature. At the tested alert budget, the night-humidity rule missed 63 percent of lethal weeks compared to 52 percent for the daytime rule.
- A matched comparison — pairing each lethal heat-wave week with a non-lethal week from the same city and season — found that once daytime temperature was accounted for, humidity on the lethal weeks was actually *lower*. The opposite direction from the hypothesis.

## Why that matters

The expectation in the field was the opposite. Peer-reviewed studies in top journals had found that warm nights carry independent mortality risk. Projections of climate-driven mortality were leaning on compound day-and-night heat. National agencies were already building overnight humidity into their next generation of alert criteria.

The most likely explanation for the disconnect is scale. The laboratory experiments that measured the body's breaking point are real physiology, measured on individual people under controlled exposure. A city-level early warning system works at a completely different resolution: weekly death counts across a whole metropolitan population, where demographics, reporting lags, and the momentum of the last few hot days dominate the signal. At that resolution, last week's death count tells you more about this week than last night's humidity does. Studies using finer daily data on smaller populations may be catching a real within-day pattern that weekly aggregation simply smears out.

## What it means in practice

**For city planners and emergency managers.** Our findings do not support prioritising overnight humidity over daytime temperature in your alert system. The current approach — tracking daytime heat extremes and how long they have lasted — is not broken. A warning system that swapped it out for the night-humidity rule would miss more deaths and cry wolf more often.

The upgrades worth chasing are unglamorous. Build "heat memory" into your system by incorporating the last few days and weeks of exposure. Use a streak-based measure of extreme heat. Adjust for the season. These are inputs most systems either already have or could add cheaply.

**For researchers.** The finding does not invalidate the laboratory physiology. It means the jump from "individual bodies fail under sustained humid heat" to "city-level death counts track overnight humidity" is not visible at the population-week scale. Closing that gap needs individual-level studies at daily or finer resolution, especially in tropical and subtropical cities where the physiological thresholds are actually routinely approached.

## How we did it

We built a dataset of weekly all-cause deaths for 30 cities — 15 in the United States from [CDC data](https://data.cdc.gov/), 15 in Europe from [Eurostat](https://ec.europa.eu/eurostat) — and matched each city-week to hourly weather from [NOAA's Integrated Surface Database](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database). The data covered 2013 to 2025, with the pandemic years excluded, for 9,276 city-weeks in total. We then ran 116 pre-committed single-change experiments, followed by 10 robustness checks and 8 additional experiments that the independent reviewer asked for — including a matched case-by-case comparison that directly tested the night-humidity claim. None of them reversed the finding.

## Further reading

- Vecellio et al. (2022), "Evaluating the 35 °C wet-bulb temperature adaptability threshold" — the laboratory study that lowered the known physiological limit.
- Gasparrini et al. (2015), "Mortality risk attributable to high and low ambient temperature", *The Lancet* — the landmark multi-country heat-mortality study across 384 locations.
- Achebak et al. (2022), "Hot nights and heat-related mortality in Europe", *The Lancet Planetary Health* — the study that motivated the night-time hypothesis at the population level.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/heat_mortality/paper.md).
