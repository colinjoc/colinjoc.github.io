---
title: "What is already burning beats what usually burns"
date: 2026-04-11
domain: "Wildfire Risk / Mediterranean Fire Ecology"
blurb: "Fire agencies rely on historical seasonal averages to pre-position crews. Fourteen years of Iberian satellite data says another signal matters more."
weight: 28
tags: ["wildfire", "fire-risk", "Portugal", "Spain", "Iberian-Peninsula", "EFFIS", "satellite-observations", "temporal-cross-validation"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/iberian_wildfire/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** For identifying which Iberian fire weeks will turn catastrophic, current fire activity — how much is burning right now, compared to the historical average for this calendar week — is a far stronger signal than seasonal climatology. That is true even after stripping out the obvious case where the same fire simply keeps burning into the next week.

## The question

The Iberian Peninsula burns more than any other part of Western Europe. Portugal and Spain between them lose hundreds of thousands of hectares of forest every year. In extreme years the losses are catastrophic — in June 2017, the Pedrogao Grande fire killed 66 people in central Portugal. But not all fire weeks are equal. Most weeks during the fire season produce moderate burning that suppression crews can contain. Roughly one week in eight crosses the threshold for a "very large fire week" — more than 5,000 hectares burned at country level — and those weeks account for the vast majority of total burned area and virtually all fatalities.

What signals from fire-activity data best identify these catastrophic weeks? We built three families of predictors entirely from satellite-detected fire observations — seasonal climatology (what usually burns each week of the year), recent fire dynamics (how current burning compares to the historical average), and cumulative season stress (total fire activity year-to-date). We deliberately excluded real-time weather data (temperature, humidity, wind, the Fire Weather Index), which limits the scope of our conclusions but isolates the value of fire-activity signals on their own.

## What we found

Recent fire activity is by far the most informative family. A simple linear model using it correctly ranks catastrophic weeks against normal weeks about 95 times out of 100. Seasonal climatology, used on its own, gets it right about 81 times out of 100. That gap is large, consistent across 14 years of train-on-the-past, test-on-the-future splits, and holds up when persistence events are stripped out.

- Nearly half — 47 percent — of catastrophic fire weeks are "persistence" events: the same fire burning across a weekly boundary. A trivial baseline that uses only last week's burned area already does surprisingly well here.
- When persistence events are stripped out and only the onset of new catastrophic fire weeks is evaluated, recent fire activity still dominates seasonal climatology. The signal is not just detecting fires already underway.
- Tree-based models using every feature together essentially solve the problem — ranking catastrophic weeks correctly in 99 tests out of 100, and doing so in every individual year from 2015 to 2025.
- The advantage of recent fire activity grows at more extreme thresholds. At 20,000 hectares (the most severe 3.5 percent of weeks), the gap over seasonal climatology widens to nearly 25 percentage points.

## Why that matters

Seasonal climatology is the backbone of most operational fire danger systems. Fire agencies rely on historical averages and weather-derived danger indices to set staffing levels weeks in advance. The expectation going in was that knowing "this is historically the worst week of the year" would be the strongest predictor of catastrophic burning.

Instead, knowing "burning right now is running well above normal" proved more informative — and not simply because ongoing fires carry over. Even after excluding persistence events, the recent-activity signal identified new catastrophic fire onsets with high accuracy. Elevated burning appears to act as an integrating sensor: it reflects the combined state of drought, fuel dryness, wind patterns, and landscape preconditioning in a way that seasonal averages cannot. One important caveat: this study compared fire-activity signals against each other, not against real-time weather data. Whether recent fire activity would also outperform real-time meteorological indices remains open.

## What it means in practice

**For fire agencies already watching the European Forest Fire Information System.** Track the ratio of current fire activity to the historical average for each calendar week. When that ratio exceeds roughly two during fire season, the probability of new catastrophic fires developing is elevated. This complements weather-based fire-danger forecasting — it does not replace it.

**For regions without good weather-based fire-danger forecasting.** Fire-activity observations are globally available from satellite systems and need no ground-station network, no reanalysis pipeline, and no fuel-moisture sampling. In regions where meteorological fire-weather indices are unavailable or poorly calibrated — much of sub-Saharan Africa, Southeast Asia, and South America — the autoregressive fire-activity signal documented here could serve as a first-pass early warning layer.

## How we did it

We downloaded 14 years (2012-2025) of weekly fire statistics from the [European Forest Fire Information System](https://api2.effis.emergency.copernicus.eu/statistics/v2/gwis/weekly?country=PRT&year=2024) via the GWIS country profile API, supplemented by [MODIS MCD64A1 burned area data](https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/MCD64A1_burned_area_full_dataset_2002_2024.zip) and [GlobFire event records](https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/GLOBFIRE_burned_area_full_dataset_2002_2024.zip) — all real satellite observations, no synthetic data. We constructed three predictor families (10, 10, and 7 features respectively), ran a model tournament with train-on-the-past, test-on-the-future validation, and added persistence analysis, onset-only evaluation, and threshold sensitivity experiments as additional checks.

## Further reading

- Tedim F et al. "Defining Extreme Wildfire Events." *Science of the Total Environment* (2018). [doi:10.1016/j.scitotenv.2018.05.199](https://doi.org/10.1016/j.scitotenv.2018.05.199) — framework for classifying extreme fire events on the Iberian Peninsula.
- Turco M et al. "Exacerbated Fires in Mediterranean Europe Due to Anthropogenic Warming." *Nature Communications* (2018). [doi:10.1038/s41467-018-06358-z](https://doi.org/10.1038/s41467-018-06358-z) — climate attribution of increasing Mediterranean fire severity.
- San-Miguel-Ayanz J et al. "EFFIS: Ten Years of a Pan-European System." JRC (2012). [doi:10.2788/1490](https://doi.org/10.2788/1490) — description of the European fire monitoring infrastructure used in this study.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/iberian_wildfire/paper.md).
