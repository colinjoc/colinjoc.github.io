---
title: "Polluted Fog Lasts Two Hours Longer in Italy's Po Valley"
date: 2026-04-12
domain: "Atmospheric Science"
blurb: "We matched 3,021 fog events at ten Italian airports with air pollution records from 275 monitoring stations. Fog on polluted days persists about two hours longer than fog on clean days, and the gap nearly doubles when temperatures drop below freezing."
weight: 11
tags: ["atmospheric-science", "fog", "aerosol", "po-valley", "air-quality", "italy", "open-data"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/po_valley_fog/paper.md).*

## The Question

Northern Italy's Po Valley is both one of Europe's foggiest and most polluted regions. Hemmed in by the Alps and the Apennines, the valley traps cold, humid air every autumn and winter, producing thick fog that grounds flights, slows motorway traffic, and shrouds cities for days at a stretch. It is also home to roughly 20 million people and dense industry, pushing particulate pollution to some of the highest levels in western Europe.

The physics suggests the two problems should be linked. Pollution particles act as tiny seeds on which fog droplets form. More seeds mean more droplets, but each droplet is smaller. Smaller droplets are lighter and settle out of the air more slowly, which should keep the fog alive longer. A 2024 study using satellite data found that fog under polluted conditions lasted up to three hours longer -- but satellite observations include fog layers well above the ground. We wanted to know whether the same effect shows up in direct ground-level visibility measurements: the data that tells you whether a pilot can see the runway.

## What We Found

Fog on polluted days persists about two hours longer than fog on clean days -- and the effect kicks in at surprisingly low pollution levels.

{{< figure src="plots/duration_by_pollution.png" alt="Fog duration distributions under clean and polluted conditions" caption="Fog duration under clean conditions (PM2.5 below 23 ug/m3, blue) and polluted conditions (above 23 ug/m3, red). The polluted distribution has a heavier tail of long-lasting events. Mean duration: 5.8 hours clean, 7.9 hours polluted." >}}

- Splitting 3,021 fog events at the regional median fine-particle concentration, polluted fog averaged 7.9 hours versus 5.8 hours for clean fog -- a difference of 2.1 hours that held across every statistical test.
- The largest duration gap (2.6 extra hours) appeared at a fine-particle concentration of just 16 micrograms per cubic metre, well below the European Union daily limit of 25. Even modestly dirty air produces noticeably longer fog.
- Cold weather amplifies the effect: below 2 degrees Celsius the pollution premium reaches 2.8 hours, nearly double the 1.6-hour premium at warmer temperatures.
- Eight of ten airports individually confirmed the pattern; only two smaller stations fell short of statistical significance, though both pointed in the same direction.
- Particulate pollution ranked as the sixth and seventh most important predictor of fog duration in a tree-based model, accounting for about 18 percent of the model's predictive power -- behind meteorological variables like the hour fog began, humidity, and wind speed, but ahead of temperature and calendar month.

{{< figure src="plots/threshold_scan.png" alt="Fog duration difference across PM2.5 and PM10 thresholds" caption="The extra hours of fog under polluted conditions, plotted against the pollution threshold used to define 'polluted.' The duration premium is consistently positive and peaks at relatively low concentrations." >}}

## Why That's Surprising

The conventional wisdom among forecasters is that fog duration is almost entirely a weather story: how calm the air is, how moist the boundary layer is, whether a front is on the way. Pollution is treated as a nuisance for health, not a driver of visibility. Most operational fog forecasting models ignore air quality entirely.

What the data show is that you cannot fully separate the two. The pollution effect persists even after controlling for wind speed, pressure, temperature, and humidity -- and it follows the pattern that microphysics predicts. In cold, stable conditions where the polluted air is trapped near the surface with no vertical mixing to dilute it, the small-droplet mechanism has the most leverage: the fog simply has nowhere to go. At warmer temperatures, solar heating can break fog up regardless of how many particles are in the air. This temperature dependence is exactly what the physics of droplet settling predicts, and it is hard to explain purely by the coincidence of stagnant weather causing both pollution and fog.

{{< figure src="plots/temp_pollution_interaction.png" alt="Aerosol effect on fog duration by temperature range" caption="The pollution-fog duration premium is largest in cold conditions and shrinks as temperatures rise, consistent with the small-droplet settling mechanism." >}}

## What It Means

For anyone who lives in, drives through, or flies into the Po Valley, the practical takeaway is that air quality policy and fog are coupled. Reducing particulate emissions would not only improve respiratory health -- it could also shorten the fog events that disrupt transport and daily life every winter. Italy and the European Union have been tightening particulate standards for years, and regional mean fine-particle concentrations in the Po Valley have already dropped from 33 to 19 micrograms per cubic metre over the past decade. Over the same period, average fog duration has fallen from about 9.3 hours to roughly 6 hours.

For airport operators and logistics planners, the finding suggests that incorporating real-time air-quality observations into fog-duration forecasts could improve predictions. Current forecasting approaches miss about 18 percent of the signal by ignoring pollution -- a gap that could translate to better flight scheduling and road-safety warnings during the fog season from October through March.

## How We Did It

We downloaded 798,952 hourly visibility and weather observations from the [NOAA Integrated Surface Database](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) for 10 Po Valley airports, and matched them with 3.3 million validated particulate-matter measurements from 275 monitoring stations via the [European Environment Agency download service](https://eeadmz1-downloads-webapp.azurewebsites.net/). We ran a five-family model tournament with 17 pre-registered hyperparameter experiments, six interaction sweeps, and six adversarial robustness checks. The key finding -- the 2.1-hour pollution premium and its temperature dependence -- emerged from the threshold-scanning and stratification analyses and was confirmed by multivariate controls, wind-speed stratification, and per-station replication. No synthetic data were used.

{{< figure src="plots/feature_importance.png" alt="Feature importance for fog duration prediction" caption="What controls how long fog lasts: the hour of fog onset leads (fog starting late at night has more time before sunrise heating), followed by humidity and wind speed. Pollution ranks sixth and seventh -- below the main meteorological variables but ahead of temperature and month." >}}

## Further Reading

- Pauli, E. et al. "Synoptic Scale Controls and Aerosol Effects on Fog and Low Stratus Life Cycle Processes in the Po Valley, Italy." *Geophysical Research Letters* 51 (2024). [Link](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL111490) -- the key predecessor study finding up to 3 hours longer fog under polluted conditions.
- Henning, S. et al. "From Molecules to Droplets: The FAIRARI 2021/22 Campaign." *BAMS* 106 (2025). [Link](https://journals.ametsoc.org/view/journals/bams/106/1/BAMS-D-23-0166.1.xml) -- the Po Valley field campaign studying aerosol-fog microphysics at the droplet level.
- Vautard, R. et al. "Decline of fog, mist and haze in Europe over the past 30 years." *Nature Geoscience* 2 (2009). [Link](https://doi.org/10.1038/ngeo414) -- documents the long-term decline in European fog frequency.
- Full technical write-up: [paper.md](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/po_valley_fog/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
