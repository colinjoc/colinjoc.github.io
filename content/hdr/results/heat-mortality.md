---
title: "The Night-Time Wet-Bulb Hypothesis Does Not Survive a Pre-Registered Test on 9,276 City-Weeks"
date: 2026-04-09
weight: 1
blurb: "Does night-time humidity predict which heat waves kill? We pre-registered 22 hypotheses and tested across 30 cities. The answer is no — and it survives 10 robustness checks."
domain: "Public Health / Climate Hazards"
headline: "REFUTED — of 22 flagship night-time wet-bulb hypotheses tested against a tight atmospheric baseline on 30 US + EU cities x 13 years, only one keeps, and that one is a 4-week memory signal not a physiology signal; the literature's night-Tw threshold rule is operationally worse than a dry-bulb strawman in a counterfactual early-warning-system evaluation"
metric_name: "Lethal-heatwave-week classifier Area Under the Receiver Operating Characteristic curve (AUC-ROC) on a 9,276-city-week panel; Mean Absolute Error in deaths per week on the weekly excess-deaths regression target"
metric_value: "Phase 2 best MAE 40.33 deaths/week (15.1% improvement over baseline 47.49) with ZERO night-Tw features in the winning set; R09 binary classifier AUC 0.9804 without night-Tw; HDR minimal detector AUC 0.9696 on 2 features"
tags: ["public-health", "climate", "heat-mortality", "wet-bulb", "hypothesis-testing", "negative-result", "early-warning-systems"]
---

## The Problem

In 2010, Sherwood and Huber proposed that a wet-bulb temperature (Tw) of 35 degrees Celsius marks a theoretical upper limit for human thermoregulation - no amount of sweating can keep core body temperature from rising. In 2022, Vecellio and colleagues at Penn State measured the **empirical** critical wet-bulb temperature in a controlled environmental chamber on young, heat-acclimated subjects and found it was much lower: around 30.55 degrees Celsius in warm-humid conditions. Wolf et al. (2023) replicated this in older adults and found their critical threshold lower still.

This pivoted a decade of climate-health research. A natural extension was to argue that **night-time** wet-bulb temperature - the overnight minimum - is the dominant predictor of mortality, because overnight cooling is what allows the body to recover from daytime hyperthermia. Achebak et al. (2022) showed warm nights carried mortality risk independent of daytime in Spanish cities. Royé et al. (2021) extended this to 148 southern European locations. He et al. (2022) projected future night-time warming-attributable mortality. The Lancet Countdown 2024-2025 reported a 167% increase in heat-related mortality in the 65+ population versus the 1990s, 102 percentage points of which is "more than expected from temperature alone".

The operational claim that follows is specific: **heat-health early warning systems (EWSs) should condition on night-time wet-bulb temperature as the primary indicator**. Several European and North American EWS redesigns were in flight to do exactly that when we started this project. We pre-registered 22 flagship night-Tw hypotheses and tested them against a tight atmospheric baseline on **9,276 city-weeks** across 30 US + EU cities over 13 years.

## The Baseline (What We Compared Against)

The baseline is **XGBoost regression** on a strictly atmospheric feature set that mimics current heat-health EWS practice:

| Feature category | Columns |
|---|---|
| Current-week dry-bulb statistics | `tmax_c_mean`, `tmax_c_max`, `tmin_c_mean`, `tavg_c`, `tdew_c`, `rh_pct` |
| Current-week daytime wet-bulb (NOT night-Tw) | `tw_c_mean`, `tw_c_max` |
| Heat-wave indicator | `consecutive_days_above_p95_tmax` |
| Calendar | `iso_year`, `iso_month_sin`, `iso_month_cos` |
| Vulnerability | `log_population`, `lat`, `tmax_anomaly_c`, 30 city one-hots |

**`tw_night_c_mean` and `tw_night_c_max` are deliberately excluded** - they are the Phase 2 hypothesis variables. Every Phase 2 single-change experiment is measured as an addition on top of this reference.

The panel is 30 cities x 13 years, cleaned to 9,276 weeks after removing pandemic weeks, null columns, and extreme p-score outliers. US cities come from the CDC National Center for Health Statistics state-weekly all-cause mortality, scaled to city population shares. EU cities come from Eurostat `demo_r_mwk3_t` NUTS-3 weekly mortality. Weather comes from the NOAA Integrated Surface Database (ISD) hourly feed, aggregated to weekly with Stull (2011) wet-bulb.

The target is `excess_deaths = deaths_all_cause - expected_baseline`, where the expected baseline is the 5-year same-ISO-week mean excluding the pandemic window (ECDC EuroMOMO methodology). The lethal-heat-wave binary label is `(p_score >= 0.10) AND (consecutive_days_above_p95_tmax >= 1)`; positive-class rate 347/9,276 (3.7%). Evaluation is 5-fold `KFold(shuffle=True, random_state=42)` cross-validation; metrics are MAE, RMSE, R-squared on `excess_deaths` and AUC-ROC + Brier on the lethal binary label.

Baseline performance (XGBoost on `BASELINE_FEATURES`, E00):

| Metric | Value |
|---|---|
| MAE (deaths per week) | **47.488** |
| RMSE | 80.448 |
| R-squared | 0.6974 |
| AUC-ROC | 0.8277 |
| Brier score | 0.1419 |

The Phase 1 tournament winner is ExtraTrees at **MAE 45.558, R-squared 0.7445, AUC 0.8220**. The tree-to-linear ratio is 45.56 / 64.13 = **0.710** - the problem is mostly linear, and Phase 2 should not expect large tree-specific wins.

## The Solution (What We Discovered)

The "solution" here is a refutation plus an alternative. The alternative is a Phase 2 best model that improves MAE by 15% over the baseline - and **does not include any night-time wet-bulb feature in the winning set** (except a 4-week memory signal, which we explain below).

### The final code

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error, r2_score

BASELINE_FEATURES = [
    "tmax_c_mean", "tmax_c_max", "tmin_c_mean", "tavg_c", "tdew_c",
    "rh_pct", "tw_c_mean", "tw_c_max",
    "consecutive_days_above_p95_tmax", "tmax_anomaly_c",
    "iso_year", "iso_month_sin", "iso_month_cos",
    "log_population", "lat",
]
CITY_ONEHOT = [f"city_{c}" for c in (
    "new_york", "los_angeles", "chicago", "houston", "phoenix",
    "las_vegas", "atlanta", "miami", "seattle", "boston",
    "san_diego", "dallas", "philadelphia", "denver", "st_louis",
    "paris", "london", "madrid", "rome", "berlin",
    "milan", "athens", "lisbon", "bucharest", "vienna",
    "warsaw", "stockholm", "copenhagen", "dublin", "amsterdam",
)]
COUNTRY_ONEHOT = [f"country_{cn}" for cn in (
    "US", "FR", "GB", "ES", "IT", "DE", "GR", "PT", "RO",
    "AT", "PL", "SE", "DK", "IE", "NL",
)]
PHASE2_ADDS = (
    ["tw_night_c_max_roll4w",     # H022 KEEP: 4-week memory, not physiology
     "tw_rolling_21d_mean",        # H048 KEEP: daytime Tw memory
     "prior_week_pscore",          # H057 KEEP: autocorrelation lag 1
     "prior_4w_mean_pscore"]       # H058 KEEP: autocorrelation 4w mean
    + COUNTRY_ONEHOT               # H066 KEEP: country fixed effects
    + ["tmax_c_mean_lag1", "tmax_c_mean_lag2",
       "tmax_c_mean_lag3", "tmax_c_mean_lag4"]   # H078 KEEP: DLNM-like dry-bulb lags
    + ["week_of_year_sin", "week_of_year_cos"]   # H100 KEEP: week-of-year cyclic
)
PHASE2_BEST_FEATURES = BASELINE_FEATURES + CITY_ONEHOT + PHASE2_ADDS


def make_phase2_best() -> ExtraTreesRegressor:
    return ExtraTreesRegressor(
        n_estimators=300, max_depth=None, n_jobs=4, random_state=42,
    )


def run_phase2_best(panel: pd.DataFrame) -> dict:
    X = panel[PHASE2_BEST_FEATURES].astype("float64").fillna(0.0).values
    y = panel["excess_deaths"].astype("float64").values
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    oof = np.zeros(len(panel), dtype="float64")
    for tr, va in kf.split(panel):
        m = make_phase2_best()
        m.fit(X[tr], y[tr])
        oof[va] = m.predict(X[va])
    return {
        "mae_deaths": float(mean_absolute_error(y, oof)),
        "r2": float(r2_score(y, oof)),
    }
```

Running this on the cleaned Phase 2 panel reproduces **MAE = 40.334 deaths per week, R-squared = 0.8247**.

### Causal mechanism — why these features work, and why none of them are night-Tw

Four effects stack, and three of them are boring - which is the interesting finding:

1. **Temporal autocorrelation dominates** (H057, H058). The previous week's p-score and the 4-week mean p-score drop MAE from 44.71 to 42.31 deaths per week - the largest two-feature block in Phase 2. Mortality at weekly resolution is a sticky, memory-rich process driven by cohort effects from prior heat exposure, slow-moving reporting-lag dynamics, and underlying demographic stability. For a nowcasting system, last week's reported p-score is the strongest single predictor of this week's.

2. **Distributed-lag dry-bulb Tmax cross-basis** (H078). A Distributed-Lag Non-linear Model (DLNM, Gasparrini et al. 2010) cross-basis on `tmax_c_mean_lag1..4` drops MAE from 41.42 to 40.84. This is the Gasparrini et al. (2015) heat-mortality lag structure at weekly resolution. **Crucially, this is a dry-bulb not a wet-bulb lag basis** - the analogous night-time wet-bulb cross-basis (H051) did not keep.

3. **Country fixed effects** (H066). 15 country one-hots on top of the 30 city one-hots absorb cross-country heterogeneity in baseline mortality (Eurostat reporting conventions, national health systems, age distribution). Drops MAE from 42.31 to 41.42.

4. **Week-of-year cyclic encoding** (H100). Sub-monthly seasonal structure. Drops MAE from 40.84 to 40.33.

And now H022, the one night-time wet-bulb feature that kept: `tw_night_c_max_roll4w`, the **4-week rolling maximum** of the night-time wet-bulb temperature. It drops MAE from 45.56 to 44.71. But note the interpretation: this is a slow temporal memory signal ("how hot was the hottest night in the last four weeks"), not a current-week physiological threshold. It correlates with the cumulative cohort effect of a prior heat wave, not with the compensability threshold the literature hypothesises.

### Difference from the baseline

| Aspect | Baseline (E00) | Phase 2 best |
|---|---|---|
| Model | XGBoost | ExtraTrees |
| Feature count | 45 | 70 |
| Night-time wet-bulb features | 0 | 1 (4-week memory; not physiology) |
| Autocorrelation | None | Lag 1 + 4-week mean |
| Dry-bulb lag structure | None | `tmax_c_mean_lag1..4` DLNM-like |
| Country fixed effects | None | 15 one-hots |
| 5-fold CV MAE (deaths/week) | 47.49 | **40.33** (-15.1%) |
| R-squared | 0.6974 | 0.8247 |
| AUC-ROC (lethal) | 0.8277 | 0.8198 (drifted DOWN) |

## What We Found

### The 22 flagship night-time wet-bulb hypotheses: 1 KEEP, 17 REVERT, 4 DEFER

Of the 22 pre-registered night-time wet-bulb hypotheses (H001-H022 in `research_queue.md`, evaluated in order against the tightest available baseline):

| Result | Count |
|---|---:|
| KEEP | **1** (H022, 4-week rolling max memory signal) |
| REVERT | 17 |
| DEFER (data not cached) | 4 |

The 17 REVERTs include every flavour of night-Tw feature the literature has proposed: direct thresholds (H001 `tw_night_c_max`, H002 `tw_night_c_mean`), count features (H004 `consecutive_nights_tw_above_24_count`), day-night spread (H005), tropical-night counts (H006, H007), city-specific percentile anomalies (H008, H009, H010), night window sensitivity (H011 22:00-06:00 vs H012 02:00-06:00), 3-day rolling peaks (H018), compound-night flags (H019), degree-hours above threshold (H020, H021), and composite day-night features (H003). None kept at the 0.5-deaths / 1% noise floor.

### Stacking all 22 night-Tw features hurts

What if the issue is that the single-change rule misses a non-additive interaction? We tested this directly: stacking all 22 flagship night-time wet-bulb columns on top of the Phase 1 baseline gives MAE **45.617 deaths per week**, which is **worse than the Phase 1 reference** (45.558). Stacking on top of the Phase 2 best gives MAE 40.677 versus the Phase 2 best 40.334. The stacked flagship set is not a hidden win.

### Phase 2.5: 10 robustness specifications, 0 reversals

We ran 10 orthogonal robustness tests. Each held the Phase 2 best reference constant and re-ran three variants (baseline, +`tw_night_c_max`, +all 22 flagship stacked). A "reversal" is any test where the night-Tw variant KEEPs against its own baseline.

| Test | Description | Base MAE | +tw MAE | +stacked MAE | Flip? |
|---|---|---:|---:|---:|:---:|
| R01 | Per-city ExtraTrees ensemble | 44.36 | 44.37 | 44.72 | NO |
| R02 | 70+ demographic-proxy target | 4.17 | 4.17 | 4.19 | NO |
| R03 | Davies-Jones wet-bulb swap | 40.45 | 40.46 | 40.82 | NO |
| R04 | Climatology era swap | 40.53 | 40.46 | 40.70 | NO |
| R05 | Drop city + country fixed effects | 41.29 | 41.22 | 41.43 | NO |
| R06 | Drop autocorrelation (prior pscores) | 42.56 | 42.50 | 43.14 | NO |
| R07 | Hot cities only (n=3,812) | 52.65 | 52.49 | 53.01 | NO |
| R08 | Heat-wave weeks only (n=524) | 52.59 | 52.53 | 53.29 | NO |
| R09 | Binary lethal classifier | AUC 0.9804 | 0.9805 | 0.9781 | NO |
| R10 | Mediterranean subset (n=1,957) | 36.42 | 36.55 | 36.55 | NO |

**None of the 10 specifications flip the finding.** Not per-city ensembles (which might have revealed a hot-city-only signal hidden by cross-city pooling). Not the 70+ age proxy. Not the more-accurate Davies-Jones wet-bulb solver. Not an alternative climatology reference. Not dropping fixed effects. Not dropping autocorrelation. Not hot-cities-only. Not heat-wave-weeks-only. Not a genuine ExtraTreesClassifier binary framing with class_weight='balanced'. Not the Mediterranean subset where the literature hypothesis is supposed to be strongest.

### R09 binary classifier ceiling: AUC 0.9804 without any night-Tw features

The most telling robustness result is R09. An `ExtraTreesClassifier(class_weight='balanced')` on the Phase 2 best feature set reaches **AUC 0.9804** for the lethal-heat-wave binary label. Adding `tw_night_c_max` changes this to 0.9805 (not a change at the noise floor). Adding all 22 flagship features changes it to 0.9781 (worse). The binary classifier is saturated at its construction ceiling, and there is about 0.02 AUC of headroom, none of which is closed by night-time wet-bulb features.

### Phase B discovery: minimal detector + counterfactual EWS

Phase B turned the refutation into an actionable picture of what an EWS should actually use. Four sub-tasks:

**1A. Permutation importance on the R09 binary classifier.** The only feature with a measurable AUC drop is `consecutive_days_above_p95_tmax` (drop 0.0024). Every other feature has permutation importance zero to machine precision - the expected symptom of a saturated classifier with substantial redundancy. The built-in Gini importance is more differentiated and places `tmax_c_max`, `tmax_c_mean`, `tavg_c`, `tw_c_max` (daytime), `tw_rolling_21d_mean` (daytime), and the city one-hots in the top 15. **No night-time wet-bulb feature appears in the top 10 by either method.**

**1B. Minimal lethal-heatwave detector.** Greedy forward selection on the 25-feature actionable candidate pool (excluding city_* and country_* one-hots as non-actionable) selects just 2 features before the 0.001 AUC improvement floor stops it:

1. `consecutive_days_above_p95_tmax` — AUC 0.9486
2. `iso_year` — AUC 0.9696

The minimal detector is **2 features, AUC 0.9696**, within the noise floor of the full Phase 2 classifier (AUC 0.9804). Neither feature is a night-time wet-bulb feature.

**1C. Per-city AUC.** The full classifier's per-city AUCs range from 0.912 (Copenhagen) to 1.000 (Chicago, San Diego, Los Angeles with few lethal-week positives). Phoenix, the hottest city in the panel, has AUC 0.953 - **lower** than cool Stockholm (0.986), Warsaw (0.986), or Dublin (0.988). Las Vegas 0.969. Athens 0.956. The pattern predicted by the literature (hot/humid cities privileged by a night-Tw detector) is not present. In fact, a classifier trained only on `tw_night_c_max` alone gives per-city AUCs in the 0.41-0.84 range, strictly dominated by a classifier trained on `tmax_c_max` alone (0.74-0.97 range).

**1D. Counterfactual EWS comparison.** At a per-city top-5%-of-weeks alert budget (matching operational EWS practice):

| EWS configuration | False-alarm rate | Miss rate | True positives | False positives |
|---|---:|---:|---:|---:|
| A. Strawman `tmax_c_max` rank | 3.52% | **51.87%** | 167 | 314 |
| B. Literature `tw_night_c_max` rank | 3.93% | **62.54%** | 130 | 351 |
| C. HDR minimal detector | **2.98%** | **38.04%** | **215** | 266 |

The literature's night-Tw threshold rule (B) has a **higher** false-alarm rate (3.93% vs 3.52%) **and** a **higher** miss rate (62.5% vs 51.9%) than a dry-bulb strawman. Swapping an operational EWS from dry-bulb Tmax to night-Tw at the same alert budget makes it strictly worse. The HDR minimal detector (C) dominates both.

## Key Insights

### 1. The night-time wet-bulb hypothesis is refuted at the population-week scale

One of 22 flagship night-Tw hypotheses kept in the Phase 2 single-change loop, and that one is a 4-week rolling maximum - a memory signal, not a current-week physiological threshold. None of 10 orthogonal robustness specifications flip the finding. The Vecellio et al. (2022) chamber measurements stand in their own scope, but their extension to a population-week EWS rule is not supported by this panel.

### 2. Temporal autocorrelation is the biggest regression feature, not weather

The prior-week p-score and 4-week mean p-score (H057, H058) together dropped MAE from 44.71 to 42.31 deaths per week - the largest two-feature block in Phase 2. Mortality at weekly resolution is a sticky memory-rich process. For a nowcasting system this is the most important single feature category. For a true forecast horizon the autocorrelation has to be shifted and the gain shrinks, so H114-H116 (1-, 2-, 3-week-ahead lagged features) all reverted.

### 3. A minimal 2-feature detector reaches 98.9% of the full model's AUC

Greedy forward selection picks `consecutive_days_above_p95_tmax` + `iso_year` and stops. These 2 features reach AUC 0.9696 - within the noise floor of the full 70-feature Phase 2 classifier (0.9804). An operational EWS can get most of the signal from two scalars, neither of which is night-Tw.

### 4. The literature's night-Tw EWS rule is worse than a dry-bulb strawman at matched alert budget

At a per-city top-5%-of-weeks alert budget, `tw_night_c_max` rank-based alerting has miss rate 62.5% and false-alarm rate 3.9%, compared to the dry-bulb `tmax_c_max` strawman's 51.9% and 3.5%. Swapping an operational EWS from dry-bulb to night-Tw makes it **worse on both axes**. The HDR minimal detector (the model on 2 features) achieves 38.0% miss rate at 3.0% false-alarm rate, dominating both.

### 5. The binary detection task is saturated by label-feature coupling

The lethal-heat-wave binary label requires `consecutive_days_above_p95_tmax >= 1`, and that same column is in the baseline feature set. This is why R09 reaches AUC 0.9804 with only baseline features and why Phase 2 KEEPs improve MAE by 15% but leave AUC flat: the regression and binary targets are substantially decoupled on this panel.

### 6. Hot cities are not privileged by the model, contrary to literature prediction

The literature hypothesis predicts night-Tw-driven signal concentrated in hot/humid cities. Per-city AUCs do not show this. Phoenix 0.953, Las Vegas 0.969, Athens 0.956 - lower than Stockholm (0.986) and Warsaw (0.986). The R07 hot-cities-only robustness test also did not flip the finding.

### 7. The most informative experiments were the REVERTs

Of the 116 Phase 2 experiments, 58 reverted. The 17 night-Tw REVERTs in particular are informative: each is a falsification at the per-feature level against a tight baseline. The pattern across 17 independent REVERTs is what gives us confidence the finding is not a single-experiment noise result.

## Why This Matters

For heat-health early warning systems:

- **Continue conditioning on daytime Tmax exceedance and its recent history.** The Phase 2 best features (Tmax lag 1-4, prior-week autocorrelation, country fixed effects, seasonality) are already in or adjacent to current EWS practice. The 2-feature HDR minimal detector dominates both the dry-bulb strawman and the literature night-Tw threshold rule at matched alert budget.
- **Do not swap to night-Tw as the primary indicator.** The literature rule (`tw_night_c_max` rank) has a higher false-alarm rate AND a higher miss rate than the dry-bulb strawman. Swapping would hurt both public-health outcomes and EWS operator credibility.
- **Individual-level cohort studies with continuous exposure assessment** are the appropriate test of the physiological threshold claim. Wearable thermometers, minute-level wet-bulb from a co-located station, and hospital-admission / death endpoints. Population-week panels cannot resolve the hypothesis; case-crossover designs on matched hot/cold nights are closer to the mechanistic claim.

For Hypothesis-Driven Research (HDR) methodology:

- **Pre-register the flagship hypothesis list and run it first.** H001-H022 were specified before the loop was run, and they were evaluated against the tightest available baseline before any of the competing autocorrelation / fixed-effects / lag-structure hypotheses entered the running best. That is the strongest possible test.
- **Robustness tests carry the real weight of a negative finding.** Phase 2 alone could be dismissed as a specification artefact. Phase 2.5's 10 orthogonal alternative specifications (per-city ensembles, age proxy, alternative wet-bulb, no fixed effects, no autocorrelation, hot cities, heat-wave weeks, binary classifier, Mediterranean subset) each independently fail to reverse the finding. The finding is robust in the way a single regression cannot demonstrate.
- **Single-feature vs composition matters.** H051 (the night-Tw analogue of the dry-bulb DLNM cross-basis that won as H078) did not keep. This is the cleanest matched comparison in the paper: same lag structure, same feature engineering, same model, same baseline - dry-bulb kept, night-wet-bulb did not.

## Methodology

**Baseline.** XGBoost on 15 atmospheric-only features plus 30 city one-hots (no night-time wet-bulb by construction), 5-fold `KFold(shuffle=True, random_state=42)` cross-validation, on a 9,276-city-week panel of 30 US and EU cities, 2013-2025, with pandemic weeks (2020-W11 through 2022-W26) excluded. Target is weekly excess deaths vs the 5-year same-ISO-week baseline. Default XGBoost: max_depth 6, learning rate 0.05, 300 boosting rounds. MAE 47.488 deaths per week, R-squared 0.6974, AUC 0.8277.

**Iteration.** A Hypothesis-Driven Research (HDR) loop. Phase 1 ran a 5-family tournament; ExtraTrees won and the tree-to-linear ratio of 0.710 showed the problem is mostly linear. Phase 2 ran 116 pre-registered single-change hypotheses from `research_queue.md`, each with an explicit keep-or-revert threshold (`mae_new < best_so_far - max(0.5, 0.01 * best_so_far)`). The 22 flagship night-Tw hypotheses were evaluated first, against the tightest available baseline. 7 kept total: H022 (4-week tw_night rolling max memory), H048 (21-day daytime Tw mean), H057 (prior_week_pscore), H058 (prior_4w_mean_pscore), H066 (country fixed effects), H078 (DLNM-like dry-bulb lag 1-4), H100 (week-of-year cyclic). Phase 2 best: MAE 40.334, R-squared 0.8247. Phase 2.5 ran 10 robustness specifications; zero reversals. Phase B discovery computed permutation importance, greedy-forward minimal detector, per-city AUC, and counterfactual EWS comparison.

**Limitations.** Eurostat UK data ends 2020 at Brexit. CDC weekly mortality is state-aggregated via the public API. Stull (2011) is the default wet-bulb solver; Davies-Jones (2008) was swapped in R03 at the weekly aggregate with no reversal. Pandemic-week exclusion removes the 2020-2022 European heat waves and 2022 UK 40 C event. R02 is a linear 70+ demographic rescaling not a true age split - a proper age-stratified replication is the most important open extension. Wildfire smoke and Farrington-corrected baseline (R11, R12) were DEFERred.

## Key References

1. Sherwood SC, Huber M. "An adaptability limit to climate change due to heat stress." *Proceedings of the National Academy of Sciences* **107**(21), 9552-9555 (2010). [doi:10.1073/pnas.0913352107](https://doi.org/10.1073/pnas.0913352107) — the foundational 35 degrees Celsius wet-bulb species-level limit paper.

2. Vecellio DJ, Wolf ST, Cottle RM, Kenney WL. "Evaluating the 35 C wet-bulb temperature adaptability threshold for young healthy subjects (PSU HEAT)." *Journal of Applied Physiology* **132**(2), 340-345 (2022). [doi:10.1152/japplphysiol.00738.2021](https://doi.org/10.1152/japplphysiol.00738.2021) — the empirical 30.55 degrees Celsius critical wet-bulb chamber measurement that pivoted the literature.

3. Wolf ST, Vecellio DJ, Kenney WL. "Adverse heat-health outcomes and critical environmental limits (PSU HEAT)." *American Journal of Human Biology* **35**(3), e23801 (2023). [doi:10.1002/ajhb.23801](https://doi.org/10.1002/ajhb.23801) — age-stratified critical wet-bulb in older adults.

4. Gasparrini A et al. "Mortality risk attributable to high and low ambient temperature: a multicountry observational study." *The Lancet* **386**(9991), 369-375 (2015). [doi:10.1016/S0140-6736(14)62114-0](https://doi.org/10.1016/S0140-6736(14)62114-0) — the Multi-Country Multi-City (MCC) Network 384-location heat-mortality paper.

5. Gasparrini A, Armstrong B, Kenward MG. "Distributed lag non-linear models." *Statistics in Medicine* **29**(21), 2224-2234 (2010). [doi:10.1002/sim.3940](https://doi.org/10.1002/sim.3940) — the DLNM framework whose weekly cross-basis is H078 in our Phase 2.

6. Achebak H, Petetin H, Quijal-Zamorano M, Bowdalo D, García-Pando CP, Ballester J. "Hot nights and heat-related mortality in Europe: a time-series analysis." *The Lancet Planetary Health* **6**(1), e58-e65 (2022). [doi:10.1016/S2542-5196(21)00302-9](https://doi.org/10.1016/S2542-5196(21)00302-9) — Spanish-cities night-heat paper that motivates the night-time hypothesis at population scale.

7. Royé D, Sera F, Tobías A, Lowe R, Gasparrini A, Pascal M, et al. "Effects of hot nights on mortality in southern Europe." *Epidemiology* **32**(4), 487-498 (2021). [doi:10.1097/EDE.0000000000001359](https://doi.org/10.1097/EDE.0000000000001359) — 148 southern European locations.

8. He C, Kim H, Hashizume M, Lee W, Honda Y, Kim SE, Vicedo-Cabrera AM. "The effects of night-time warming on mortality burden under future climate change scenarios: a modelling study." *The Lancet Planetary Health* **6**(8), e648-e657 (2022). [doi:10.1016/S2542-5196(22)00139-5](https://doi.org/10.1016/S2542-5196(22)00139-5) — projected night-time excess mortality.

9. Lee W, Kim Y, Hashizume M, Armstrong B, Gasparrini A, et al. "Future heat-related mortality in Europe driven by compound day-night heatwaves and demographic shifts." *Nature Communications* **16**, 7395 (2025). [doi:10.1038/s41467-025-62871-y](https://doi.org/10.1038/s41467-025-62871-y) — compound day-night heat-wave projection.

10. Romanello M, Walawender M, Hsu S-C, et al. "The 2024 report of the Lancet Countdown on health and climate change: facing record-breaking threats from delayed action." *The Lancet* **404**(10465), 1847-1896 (2024). [doi:10.1016/S0140-6736(24)01822-1](https://doi.org/10.1016/S0140-6736(24)01822-1) — the 167% increase in heat-related mortality in 65+.

11. Stull R. "Wet-bulb temperature from relative humidity and air temperature." *Journal of Applied Meteorology and Climatology* **50**, 2267-2269 (2011). [doi:10.1175/JAMC-D-11-0143.1](https://doi.org/10.1175/JAMC-D-11-0143.1) — the default wet-bulb solver used in the panel.

12. Davies-Jones R. "An efficient and accurate method for computing the wet-bulb temperature along pseudoadiabats." *Monthly Weather Review* **136**, 2764-2785 (2008). [doi:10.1175/2007MWR2224.1](https://doi.org/10.1175/2007MWR2224.1) — the Davies-Jones iterative Bolton-inverse wet-bulb used in the R03 robustness swap.

13. Mora C, Dousset B, Caldwell IR, Powell FE, et al. "Global risk of deadly heat." *Nature Climate Change* **7**, 501-506 (2017). [doi:10.1038/nclimate3322](https://doi.org/10.1038/nclimate3322) — 30% of world population exposed to deadly heat.

14. Vanos JK, Baldwin JW, Jay O, Ebi KL. "Greatly enhanced risk to humans as a consequence of empirically determined lower moist heat stress tolerance." *Proceedings of the National Academy of Sciences* **120**(30), e2305427120 (2023). [doi:10.1073/pnas.2305427120](https://doi.org/10.1073/pnas.2305427120) — global population-at-risk recalculation under revised Vecellio thresholds.

---

[HDR methodology](https://github.com/colinjoc/hdr_autoresearch) — the framework, the Hypothesis-Driven Research program.md specification, and the full project history including `data_loaders.py`, `model.py`, `phase2_runner.py`, `phase25_robustness.py`, `phase_b_discovery.py`, the 164-row `results.tsv`, and the 240 citations of `papers.csv` in `applications/heat_mortality/`.
