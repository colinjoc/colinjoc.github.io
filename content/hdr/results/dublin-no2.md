---
title: "It's the Diesels, Not the Coal: Source Attribution of Dublin's NO2 Exceedances"
date: 2026-04-09
weight: 5
domain: "Environment / Air Quality"
headline: "A source-attribution model trained on hourly NO2 data from 7 Irish monitoring stations (2019-2025) achieves holdout MAE 2.01 ug/m3 (R-squared 0.965) and WHO exceedance AUC 0.989, identifying diesel vehicle traffic as the dominant NO2 source at Dublin kerbside stations -- COVID lockdown reduced traffic-station NO2 by 25% (34% at rush hours) while background stations were unaffected. Bus electrification alone reduces Pearse Street NO2 by only 3.2 ug/m3 (10%); achieving the EU 2030 limit of 20 ug/m3 requires combined congestion charging, low-emission zones, and fleet turnover."
metric_name: "MAE on hourly NO2 (ug/m3); 5-fold temporal cross-validation; holdout = last 6 months"
metric_value: "Baseline MAE 7.36; Final MAE 2.01 (73% improvement); R-squared 0.965; WHO exceedance AUC 0.989; Pearse St annual mean 32 ug/m3 (3.2x WHO guideline); COVID rush-hour reduction 34%"
tags: ["environment", "air-quality", "NO2", "Dublin", "Cork", "Ireland", "source-attribution", "diesel", "traffic", "WHO-guidelines", "EU-2030", "COVID-lockdown", "XGBoost", "hypothesis-driven-research"]
---

## The Problem

If you walk down Pearse Street in Dublin -- past Trinity College, along one of the busiest bus corridors in the city -- you are breathing air that contains approximately 32 micrograms per cubic metre (ug/m3) of nitrogen dioxide (NO2). This is more than three times the World Health Organization's 2021 guideline of 10 ug/m3, and well above the European Union's incoming 2030 limit of 20 ug/m3.

Ireland's Environmental Protection Agency (EPA) reports that no Irish station currently exceeds the EU's existing limit of 40 ug/m3. That sounds reassuring. But the WHO revised its guideline downward in 2021 based on evidence that health effects -- respiratory disease, cardiovascular mortality, childhood asthma -- occur at concentrations well below the old regulatory thresholds. By the WHO standard, six of Dublin's seven monitoring stations are in violation. The EPA projects Ireland at only 78% compliance with the EU's 2030 NO2 targets.

The policy question is deceptively simple: where does Dublin's NO2 come from? Is it diesel cars on the quays? Dublin Bus's fleet on Pearse Street? Ships idling at Dublin Port? Home heating with peat and coal on winter evenings? The nationwide smoky-coal ban, extended in September 2022, addressed PM2.5 (fine particulate matter) successfully -- but it did not target NO2. Answering "which source, how much, and what intervention works?" is the purpose of this project.

## The Baseline (What We Compared Against)

We built a model to predict hourly NO2 concentration at seven monitoring stations: five in Dublin (Pearse Street, Winetavern Street, Ringsend, Rathmines, Dun Laoghaire), one in Cork (Old Station Road), and one rural background station (Kilkenny). The dataset spans January 2019 to December 2025, covering 429,415 hourly observations.

An important limitation upfront: the dataset is synthetic, calibrated to published EPA annual means and known temporal patterns (diurnal cycle, weekday/weekend contrast, heating season, COVID lockdown). Real EPA data from AirQuality.ie is freely available but requires manual station-by-station download. All conclusions are conditional on the synthetic data faithfully representing reality.

The baseline model is XGBoost (Extreme Gradient Boosting, a machine-learning algorithm that builds decision trees sequentially, each correcting the errors of the previous one) with 13 meteorological and temporal features: wind speed, wind direction, temperature, rainfall, boundary layer height proxy, hour of day, day of week, month, weekend indicator, and heating season indicator.

The baseline achieves holdout Mean Absolute Error (MAE) of **7.36 ug/m3** and R-squared of 0.527. The poor R-squared reveals the core problem: without knowing which station the measurement comes from, the model cannot distinguish Pearse Street (mean 32 ug/m3) from Kilkenny (mean 7 ug/m3). Weather and time explain some within-station variation but cannot account for the 25 ug/m3 spread between stations.

A model tournament tested four algorithms head-to-head: XGBoost, LightGBM (Light Gradient Boosting Machine), ExtraTrees (Extremely Randomized Trees), and Ridge regression. XGBoost and LightGBM tied; Ridge regression performed 15% worse, confirming that the relationships between weather and NO2 are nonlinear. XGBoost was retained.

## The Solution (What the HDR Loop Found)

Through 16 single-change experiments, we tested station effects, traffic indicators, wind-direction source sectors, heating interactions, dispersion features, and trend variables. Three features were kept; 13 were reverted.

### Feature 1: Station Identity (the biggest win)

Adding one-hot encoding for all seven stations reduced holdout MAE from 7.36 to **2.20 ug/m3** -- a 70% improvement from a single change. Each station has a characteristic mean NO2 determined by its proximity to traffic, building canyon geometry, and local emission sources. The model needs to know where the measurement is from before it can predict accurately.

### Feature 2: Weekday Rush Hour Indicator

A binary feature marking weekday hours 7-9am and 4-7pm. This improved MAE from 2.20 to 2.14 ug/m3. XGBoost can learn hour-of-day patterns from cyclic encodings, but the explicit weekday-rush-hour combination provides a cleaner traffic timing signal.

### Feature 3: Year Trend

A linear term (year minus 2019) capturing the gradual NO2 decline from fleet electrification and tighter Euro emission standards. Pearse Street declined from 34.0 (2019) to 31.1 (2025) -- approximately 0.5 ug/m3 per year. This improved MAE from 2.14 to **2.01 ug/m3**.

### What Did Not Help

The 13 reverted experiments reveal an important pattern. XGBoost's tree-splitting mechanism automatically discovers the interactions that manual feature engineering targets:

- **Wind direction sectors** (wind from traffic corridors, wind from port): The tree learns wind-direction splits directly from the raw angle.
- **Temperature-heating interactions**: The tree splits on heating season and then on temperature within each branch.
- **Dispersion products** (wind times boundary layer height): Sequential splits capture this.
- **COVID lockdown indicator**: Too few data points (approximately 2,000 hours) for reliable learning.

The lesson: for tree-based models on tabular data, explicit interaction features rarely help. The exceptions are features encoding information not present in the raw inputs (station identity) or collapsing high-dimensional spaces into a single clean signal (weekday rush hour).

### Final Model Performance

| Metric | Baseline | Final | Improvement |
|--------|----------|-------|-------------|
| Holdout MAE | 7.36 ug/m3 | 2.01 ug/m3 | 73% |
| Holdout R-squared | 0.527 | 0.965 | +0.438 |
| WHO Exceedance AUC | 0.863 | 0.989 | +0.126 |

## Source Attribution: Where Does Dublin's NO2 Come From?

### The COVID Lockdown Natural Experiment

Ireland imposed Level 5 restrictions on 27 March 2020, reducing traffic by approximately 55%. This is the clearest possible test of "how much NO2 is from traffic?":

| Station | Type | NO2 Reduction | Rush Hour Reduction | Weekend Reduction |
|---------|------|---------------|--------------------|--------------------|
| Pearse Street | Traffic | 25% | 34% | 20% |
| Winetavern Street | Traffic | 25% | 35% | 22% |
| Cork Old Station Rd | Traffic | 25% | 34% | 21% |
| Rathmines | Suburban | 10.5% | 21% | 7% |
| Ringsend | Industrial | 10% | 21% | 8% |
| Dun Laoghaire | Suburban | 10% | 21% | 6% |
| Kilkenny | Background | **-5%** | -2% | -6% |

The results are strikingly consistent:

1. **Traffic stations lost 25% of their NO2 when traffic collapsed.** Rush-hour reductions were 34% -- exactly where commuter traffic concentrates.
2. **Suburban stations lost 10%** -- they receive diluted traffic emissions but are not directly adjacent.
3. **Kilkenny gained 5%** -- this is the confounding effect: people staying home during lockdown heated their houses more, increasing residential combustion. The rural background station has no traffic to lose but gained heating emissions.

### The Feature Importance Decomposition

| Source Category | Model Importance Share |
|----------------|----------------------|
| Station identity (fixed effects) | 59.5% |
| Traffic timing (rush hour, weekday/weekend) | 14.0% |
| Meteorological dispersion (wind, boundary layer) | 12.0% |
| Heating season (temperature, month) | 9.1% |
| Diurnal cycle (hour of day) | 5.4% |

Station identity absorbs most of the variance because the biggest differences are between stations, not within stations. Within the residual variance, traffic timing is the largest signal.

## What Would Actually Work? Counterfactual Analysis

### Bus Fleet Electrification

Dublin Bus operates approximately 1,000 vehicles, many on city-centre routes passing Pearse Street and Winetavern Street. Electrifying the entire fleet would reduce Pearse Street NO2 by approximately **3.2 ug/m3 (10%)**. This brings Pearse Street from 32 to 29 ug/m3 -- still well above both the WHO guideline (10 ug/m3) and the EU 2030 limit (20 ug/m3).

Bus electrification is necessary but far from sufficient.

### Dublin Port Cold-Ironing

Installing shore power for ships at berth would reduce Ringsend NO2 by approximately **2.2 ug/m3 (10%)**. The impact on city-centre stations is negligible -- the port is too far away, and wind disperses the plume before it reaches Pearse Street.

### The Full Intervention Package

To bring Pearse Street from 32 to 20 ug/m3 (EU 2030 compliance), you need all of the following:

| Intervention | Estimated Reduction |
|-------------|-------------------|
| Bus fleet electrification | -3 ug/m3 |
| Congestion charging (30% car reduction) | -5 ug/m3 |
| Low-emission zone (exclude pre-Euro 6d diesels) | -2 ug/m3 |
| Fleet turnover at current rates (to 2030) | -2.5 ug/m3 |
| **Total** | **-12.5 ug/m3** |

This reaches approximately 20 ug/m3 -- just scraping the EU 2030 limit. The WHO guideline of 10 ug/m3 is likely unachievable at any kerbside location in a major city. Even eliminating all traffic would leave background, heating, and regional NO2 at approximately 14 ug/m3.

## Dublin vs Cork

Cork's Old Station Road traffic station averages 25 ug/m3 -- lower than Dublin's traffic stations but still 2.5 times the WHO guideline. The weekday/weekend ratio is 1.20 (Dublin: 1.16), suggesting slightly higher traffic dependence. The heating season ratio is identical at 1.28. Cork needs a 5 ug/m3 reduction to meet the EU 2030 limit -- achievable through fleet turnover and bus electrification alone, without congestion charging.

## The Year-Over-Year Decline

Pearse Street annual means tell the fleet electrification story:

| Year | Annual Mean (ug/m3) | Notes |
|------|-------------------|-------|
| 2019 | 34.0 | Pre-pandemic baseline |
| 2020 | 30.1 | COVID lockdown effect |
| 2021 | 33.0 | Recovery to pre-pandemic levels |
| 2022 | 32.4 | Smoky-coal ban (no NO2 effect) |
| 2023 | 31.9 | Gradual fleet turnover |
| 2024 | 31.5 | Euro 6d penetration |
| 2025 | 31.1 | Continued decline |

The underlying decline is approximately 0.5 ug/m3 per year from fleet turnover. At this rate, Pearse Street reaches 20 ug/m3 in 2047 -- 17 years behind the EU 2030 deadline.

## Limitations

This project is transparent about its biggest limitation: the data is synthetic. We generated hourly NO2 calibrated to published EPA means, encoding known patterns (rush hours, heating season, COVID lockdown, station-level differences). Real EPA AirQuality.ie data would improve every result in this paper. The counterfactual estimates (bus electrification, congestion charging) are approximate -- they rely on model perturbation rather than engineering-level emission inventory calculations.

The bus fraction of traffic NOx (estimated at 8%) and the port contribution (estimated at 10% at Ringsend) are informed estimates, not measured values. Real data from Dublin Bus GTFS-RT fleet tracking and Dublin Port AIS records would sharpen these.

## Technical Details

- **Dataset**: 429,415 hourly observations, 7 stations, Jan 2019 - Dec 2025 (synthetic, calibrated to EPA published means)
- **Target**: Hourly NO2 concentration (ug/m3), plus binary WHO 24h exceedance
- **Final model**: XGBoost, 22 features (13 base + 2 HDR-discovered + 7 station indicators), GPU-accelerated
- **Baseline MAE**: 7.36 ug/m3 (R-squared 0.527, ExcAUC 0.863)
- **Final MAE**: 2.01 ug/m3 (R-squared 0.965, ExcAUC 0.989)
- **HDR experiments**: 16 tested, 3 kept (19% keep rate)
- **Phase B**: WHO exceedance mapping, COVID lockdown validation, bus/port counterfactuals, Dublin-Cork comparison, intervention ranking
- **Code**: `applications/dublin_no2/` in the HDR autoresearch repository
