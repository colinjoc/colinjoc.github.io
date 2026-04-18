---
title: "Polluted fog lasts two hours longer in Italy's Po Valley"
date: 2026-04-12
domain: "Atmospheric Science"
blurb: "Northern Italy's famous winter fog — and its famously bad air — are more closely linked than forecasters assume. Cold days make the coupling sharper."
weight: 31
tags: ["atmospheric-science", "fog", "aerosol", "po-valley", "air-quality", "italy", "open-data"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/po_valley_fog/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Across 3,021 fog events at ten Italian airports, fog on polluted days persisted an average of two hours longer than fog on clean days. Below freezing, the pollution premium almost doubles. Air-quality policy and fog are coupled more tightly than current operational forecasts assume.

## The Question

Northern Italy's Po Valley is both one of Europe's foggiest regions and one of its most polluted. Hemmed in by the Alps and the Apennines, the valley traps cold, humid air every autumn and winter, producing thick fog that grounds flights, slows motorway traffic, and shrouds cities for days. It is also home to roughly 20 million people and dense industry, pushing particulate pollution to some of the highest levels in western Europe.

Physics says the two problems should be linked. Pollution particles act as tiny seeds around which fog droplets form. More seeds mean more, smaller droplets. Smaller droplets are lighter and settle out of the air more slowly, so the fog should live longer. A 2024 satellite study found up to three extra hours of fog on polluted days — but satellite observations include fog layers well above the ground. We wanted to know whether the same effect is visible in direct ground-level visibility measurements: the data that tells a pilot whether she can see the runway.

## What we found

Fog on polluted days persists about two hours longer than fog on clean days — and the coupling starts at surprisingly low pollution levels.

{{< figure src="plots/duration_by_pollution.png" alt="Fog duration distributions under clean and polluted conditions" caption="Fog duration under clean conditions (PM2.5 below 23 micrograms per cubic metre, blue) and polluted conditions (above 23, red). The polluted distribution has a heavier tail of long-lasting events. Mean duration: 5.8 hours clean, 7.9 hours polluted." >}}

- Splitting 3,021 fog events at the regional median fine-particle concentration, polluted fog averaged 7.9 hours versus 5.8 for clean fog — a 2.1-hour difference that held across every statistical test.
- The largest duration gap — 2.6 extra hours — appeared at a fine-particle concentration of just 16 micrograms per cubic metre, well below the EU daily limit of 25. Even modestly dirty air produces noticeably longer fog.
- Cold weather amplifies the effect. Below 2 degrees Celsius, the pollution premium reaches 2.8 hours — nearly double the 1.6-hour premium at warmer temperatures.
- Eight of ten airports individually confirmed the pattern; only two smaller stations fell short of statistical significance, though both pointed in the same direction.
- Particulate pollution ranked sixth and seventh among predictors of fog duration in a tree-based model — behind the hour fog began, humidity, and wind speed, but ahead of temperature and calendar month. Roughly 18 percent of the model's predictive power came from air-quality inputs alone.

{{< figure src="plots/threshold_scan.png" alt="Fog duration difference across PM2.5 and PM10 thresholds" caption="The extra hours of fog under polluted conditions, plotted against the pollution threshold used to define 'polluted.' The duration premium is consistently positive and peaks at relatively low concentrations." >}}

## Why that matters

The conventional wisdom among forecasters is that fog duration is almost entirely a weather story: how calm the air is, how moist the boundary layer is, whether a front is on the way. Pollution is treated as a health nuisance, not a driver of visibility. Most operational fog forecasting models ignore air quality entirely.

What the data show is that you cannot fully separate the two. The pollution effect persists even after controlling for wind, pressure, temperature and humidity — and its pattern matches what the microphysics predicts. In cold, stable conditions where polluted air is trapped near the surface with no vertical mixing to dilute it, the small-droplet mechanism has the most leverage: the fog has nowhere to go. At warmer temperatures, solar heating can break fog up regardless of how many particles are in the air. That temperature dependence is exactly what the physics of droplet settling predicts, and it is hard to explain purely by the coincidence of stagnant weather causing both pollution and fog.

{{< figure src="plots/temp_pollution_interaction.png" alt="Aerosol effect on fog duration by temperature range" caption="The pollution-fog duration premium is largest in cold conditions and shrinks as temperatures rise, consistent with the small-droplet settling mechanism." >}}

## What it means in practice

**For residents and transport users in the Po Valley.** Reducing particulate emissions would shorten the fog events that disrupt transport and daily life every winter, not just improve respiratory health. The coupling is a two-for-one: cleaner air means clearer winters. Italy and the EU have been tightening particulate standards, and regional mean fine-particle concentrations in the Po Valley have already dropped from 33 to 19 micrograms per cubic metre over the past decade — over the same period, average fog duration has fallen from about 9.3 to roughly 6 hours.

**For airport operators and logistics planners.** Incorporating real-time air-quality observations into fog-duration forecasts could improve predictions during the October-to-March fog season. Current forecasting approaches miss about 18 percent of the predictive signal by ignoring pollution — a gap that could translate into better flight scheduling and road-safety warnings.

**For atmospheric scientists.** The ground-level measurements reproduce the satellite-era finding with a slightly smaller magnitude, which is what you would expect if the satellite view was partly picking up elevated fog layers. The aerosol-indirect effect on fog lifetime is detectable in routine ground observations, not just research campaigns.

## How we did it

We downloaded 798,952 hourly visibility and weather observations from the [NOAA Integrated Surface Database](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) for 10 Po Valley airports, and matched them with 3.3 million validated particulate-matter measurements from 275 monitoring stations via the [European Environment Agency download service](https://eeadmz1-downloads-webapp.azurewebsites.net/). We ran a family-of-model tournament with a set of pre-registered experiments, six interaction sweeps, and six adversarial robustness checks. The 2.1-hour pollution premium and its temperature dependence emerged from threshold scans and stratification and were confirmed by multivariate controls, wind-speed stratification, and per-station replication. No synthetic data were used.

{{< figure src="plots/feature_importance.png" alt="Feature importance for fog duration prediction" caption="What controls how long fog lasts: the hour of fog onset leads (fog starting late at night has more time before sunrise heating), followed by humidity and wind speed. Pollution ranks sixth and seventh — below the main meteorological variables but ahead of temperature and month." >}}

## Further reading

- Pauli, E. et al. (2024). ["Synoptic Scale Controls and Aerosol Effects on Fog and Low Stratus Life Cycle Processes in the Po Valley, Italy"](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL111490), *Geophysical Research Letters* — the satellite study finding up to three extra hours of fog under polluted conditions.
- Henning, S. et al. (2025). ["From Molecules to Droplets: The FAIRARI 2021/22 Campaign"](https://journals.ametsoc.org/view/journals/bams/106/1/BAMS-D-23-0166.1.xml), *Bulletin of the American Meteorological Society* — the Po Valley field campaign studying aerosol-fog microphysics at the droplet level.
- Vautard, R. et al. (2009). ["Decline of fog, mist and haze in Europe over the past 30 years"](https://doi.org/10.1038/ngeo414), *Nature Geoscience* — the long-term European fog decline.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/po_valley_fog/paper.md) — all experiments and robustness checks.
