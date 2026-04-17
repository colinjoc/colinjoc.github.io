---
title: "Iberian Wildfire: Recent Burning Beats Seasonal Averages"
date: 2026-04-11
domain: "Wildfire Risk / Mediterranean Fire Ecology"
blurb: "Which weeks on the Iberian Peninsula produce catastrophic wildfires? Using 14 years of satellite data, we found that recent fire activity -- not historical seasonal patterns -- is the strongest signal, even after excluding fires that simply continue burning from the week before."
weight: 28
tags: ["wildfire", "fire-risk", "Portugal", "Spain", "Iberian-Peninsula", "EFFIS", "satellite-observations", "temporal-cross-validation"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/iberian_wildfire/paper.md).*

## The Question

The Iberian Peninsula burns more than any other part of Western Europe. Portugal and Spain between them lose hundreds of thousands of hectares of forest every year, and in extreme years the losses are catastrophic -- in June 2017, the Pedrogao Grande fire killed 66 people in central Portugal. But not all fire weeks are equal. Most weeks during the fire season produce moderate burning that suppression crews can contain. Roughly one week in eight produces a "very large fire week," defined as more than 5,000 hectares burned at the country level, and those weeks account for the vast majority of total burned area and virtually all fatalities.

We asked: what signals from fire activity data best identify these catastrophic weeks? We built three families of predictors entirely from satellite-detected fire observations -- seasonal climatology (what usually burns each week of the year), recent fire dynamics (how current burning compares to historical norms), and cumulative season stress (total fire activity year-to-date). Importantly, we deliberately excluded actual weather data (temperature, humidity, wind, the Fire Weather Index), which limits the scope of our conclusions but isolates the value of fire-activity signals alone.

## What We Found

Recent fire activity features -- the ratio of current burning to historical averages, plus what burned in the previous one to two weeks -- are far more informative than seasonal climatology for identifying catastrophic fire weeks.

- Using a penalised linear model with strict train-on-the-past, test-on-the-future validation across 14 years, recent fire activity features scored 0.952 on a 0-to-1 discrimination scale, versus 0.809 for seasonal climatology. The 95 percent confidence intervals do not overlap.
- Nearly half (47 percent) of catastrophic fire weeks are "persistence" events -- the same fire burning across a weekly boundary. A trivial baseline that uses only last week's burned area scores 0.814.
- When persistence events are stripped out and only the onset of new catastrophic fire weeks is evaluated, recent fire activity still dominates (0.921 versus 0.799), confirming the signal is not just detecting fires already underway.
- Tree-based models using all features score 0.993, exceeding 0.977 in every individual test year from 2015 to 2025.
- The advantage of recent fire activity features grows at more extreme thresholds: at 20,000 hectares (the most severe 3.5 percent of weeks), the gap widens to nearly 25 percentage points.

## Why That's Surprising

Seasonal climatology is the backbone of most operational fire danger systems. Fire agencies rely on historical averages and weather-derived danger indices to set staffing levels weeks in advance. The expectation going in was that knowing "this is historically the worst week of the year" would be the strongest predictor of catastrophic burning.

Instead, knowing "burning right now is running well above normal" proved far more informative -- and not simply because ongoing fires carry over from one week to the next. Even after excluding those persistence events, the recent-activity signal identified new catastrophic fire onsets with high accuracy. This suggests that elevated burning acts as an integrating sensor: it reflects the combined state of drought, fuel dryness, wind patterns, and landscape preconditioning in a way that seasonal averages cannot. It is worth noting, however, that this study compared fire-activity signals against each other, not against actual weather data. Whether recent fire activity would also outperform real-time meteorological indices remains an open question.

## What It Means

For fire agencies already monitoring the European Forest Fire Information System's weekly statistics, the practical suggestion is straightforward: track the ratio of current fire activity to the historical average for each calendar week. When that ratio exceeds roughly two during fire season, the probability of new catastrophic fires developing is elevated. This is a complement to weather-based fire danger forecasting, not a replacement.

The broader implication is methodological. Fire-activity observations are globally available from satellite systems and require no ground-station network, no reanalysis pipeline, and no fuel-moisture sampling. In regions where meteorological fire weather indices are unavailable or poorly calibrated -- much of Sub-Saharan Africa, Southeast Asia, and South America -- the autoregressive fire-activity signal documented here could serve as a first-pass early warning layer.

## How We Did It

We downloaded 14 years (2012--2025) of weekly fire statistics from the [European Forest Fire Information System](https://api2.effis.emergency.copernicus.eu/statistics/v2/gwis/weekly?country=PRT&year=2024) via the GWIS country profile API, supplemented by [MODIS MCD64A1 burned area data](https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/MCD64A1_burned_area_full_dataset_2002_2024.zip) and [GlobFire event records](https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/GLOBFIRE_burned_area_full_dataset_2002_2024.zip) -- all real satellite observations, no synthetic data. We constructed three predictor families (10, 10, and 7 features respectively), ran a six-model tournament with temporal cross-validation, and added persistence analysis, onset-only evaluation, and threshold sensitivity experiments in response to adversarial review through the [HDR methodology](https://github.com/colinjoc/hdr_autoresearch).

## Further Reading

- Tedim F et al. "Defining Extreme Wildfire Events." *Science of the Total Environment* (2018). [doi:10.1016/j.scitotenv.2018.05.199](https://doi.org/10.1016/j.scitotenv.2018.05.199) -- framework for classifying extreme fire events on the Iberian Peninsula.
- Turco M et al. "Exacerbated Fires in Mediterranean Europe Due to Anthropogenic Warming." *Nature Communications* (2018). [doi:10.1038/s41467-018-06358-z](https://doi.org/10.1038/s41467-018-06358-z) -- climate attribution of increasing Mediterranean fire severity.
- San-Miguel-Ayanz J et al. "EFFIS: Ten Years of a Pan-European System." JRC (2012). [doi:10.2788/1490](https://doi.org/10.2788/1490) -- description of the European fire monitoring infrastructure used in this study.
- Full technical paper: [paper.md](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/iberian_wildfire/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** -- the framework and full project history
