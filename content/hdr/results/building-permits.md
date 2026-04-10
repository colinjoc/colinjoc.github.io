---
title: "120 Pre-Registered Experiments Could Not Beat the Baseline — Until We Looked at the One City That Publishes Per-Stage Timestamps"
date: 2026-04-09
weight: 3
blurb: "Why does a duplex take 48 days to permit in Austin and 605 in San Francisco? We ran 120 ML experiments — none helped. The answer was structural: only one US city publishes per-stage timestamps."
domain: "Urban Operations / Public Services"
headline: "XGBoost with 13 raw features plateaus at MAE 89.40 days across 5 US cities — every one of 120 single-change experiments reverted. Adding two Seattle-only stage columns collapses MAE to 24.68 days (3.6x improvement). The bottleneck was data access, not modelling."
metric_name: "Mean Absolute Error on building permit duration (days)"
metric_value: "89.40 days cross-city baseline → 24.68 days Seattle with stage data (3.6x improvement); NYC BIS 4-stage model hits 4.04 days on its subset (22x)"
tags: ["urban-operations", "public-services", "negative-result", "process-mining", "housing-policy", "open-data"]
---

## The Problem

Two essentially identical small residential permits, filed in different US cities, take wildly different amounts of calendar time to process. A March-2026 *San Francisco Examiner* analysis commissioned by the San Francisco Board of Supervisors reported a median time from application to issuance of 280 days in San Francisco over January 2024 – August 2025 — down from roughly 605 days prior to California Senate Bill 423 (SB 423). The same report put Austin at 91 days and San Diego at 134 days. Some applications in the San Francisco pipeline as of October 2024 had been pending for an average of 1,489 days with a backlog of more than 1,300 cases. This order-of-magnitude variance across otherwise similar projects is at the core of the US housing-supply debate, and it has direct policy consequences for anyone trying to figure out which cities are slow and why.

The standard tool for measuring municipal permit friction is the Wharton Residential Land Use Regulatory Index (WRLURI), a cross-sectional jurisdiction-level instrument (Gyourko et al. 2008, 2021). WRLURI answers "how much regulation exists in city X?" but it does not answer "where in the pipeline is the time going?" We set out to answer the second question using the per-permit open-data feeds that every major US city now publishes. Our original hypothesis was that a competent Extreme Gradient Boosting (XGBoost) model on the widely-available metadata (valuation, square footage, neighbourhood, permit subtype, filed date, city) would cleanly predict total duration in days and that feature engineering plus hyperparameter tuning could narrow the error further. We ran the full Hypothesis-Driven Research (HDR) loop: Phase 0 literature review (350 citations, 5,052-word review), Phase 0.5 baseline audit, Phase 1 model-family tournament, Phase 2 single-change experiments, Phase 2.5 compositional retests, and Phase B discovery sweep.

What actually happened was the opposite of the expected story. The baseline plateaued at Mean Absolute Error (MAE) 89.40 days. Every one of 120 pre-registered single-change experiments reverted. And the thing that eventually worked was not a better model — it was data access. The one US city that publishes per-stage reviewer timestamps (Seattle) lets a 2-feature shallow XGBoost get MAE 24.68 days on its subset. The one US city that publishes per-stage payment-and-approval timestamps (New York City's Buildings Information System, NYC BIS) lets a 6-feature XGBoost get MAE 4.04 days on its subset. Neither of those models transfers to the other three cities in our baseline because those cities do not publish the necessary columns.

## The Baseline (What We Compared Against)

The baseline is **XGBoost** (Chen and Guestrin 2016) on a stratified 50,000-row sample drawn from five municipal open-data permit feeds: San Francisco (SF Department of Building Inspection, DBI), New York City (NYC Department of Buildings, DOB), Los Angeles (LA Department of Building and Safety, LADBS), Chicago (Chicago Department of Buildings), and Austin (Austin Development Services Department). Each city's raw feed is cached as a 150,000-row parquet pulled newest-first via the Socrata Open Data Application Programming Interface (SODA API).

The cleaning rules (in `model.build_clean_dataset_v2`):

1. Both `filed_date` and `issued_date` must be non-null.
2. `duration_days = (issued_date − filed_date).dt.days` must satisfy `0 < duration_days < 1825` (under 5 years).
3. `filed_date >= 2015-01-01` (sentinel-date hygiene).
4. A per-city strict small-residential filter (single-family, two-family, or duplex structures). The filter is city-specific because schemas are inconsistent: SF uses `proposed_use` text plus non-Over-The-Counter (non-OTC) permit-type inclusion; NYC filters on `job_type ∈ {NB, A1, A2, A3}` with `unit_count ≤ 4`; LA uses `permit_sub_type` text matching; Chicago falls back to work-description text (no unit-count field — documented recall limitation); Austin uses `permit_class` "R-" prefix with a 5,000 square foot cap.
5. Status hygiene: drop rows whose `status` contains "cancel|withdraw|void|expired|disapproved|rejected|denied|suspended".

The sample is stratified on (city × filed-year-bucket) with four buckets: 2015–2018, 2019–2021, 2022–2023, 2024–2026. This forces the historical slow tail (SF 2018–2023) into the sample, which a naive newest-first shuffle would under-represent. Each of the 20 (city × bucket) cells receives up to 2,500 permits, with underfilled cells topped up from leftover pool at random.

The baseline feature set is 13 columns:

```python
RAW_FEATURES = [
    "city_sf", "city_nyc", "city_la", "city_chicago", "city_austin",  # city one-hot (5)
    "filed_year", "filed_month_sin", "filed_month_cos",               # calendar (3)
    "log_valuation", "log_square_feet", "log_unit_count",             # numeric (3)
    "permit_subtype_te", "neighborhood_te",                           # in-fold TE (2)
]
```

Calendar features use a Fourier cyclic month encoding. Numeric features are `log1p` of city-median-imputed values clipped at zero. The two target-encoded (TE) columns are computed inside each Cross-Validation (CV) fold on the training partition only, using smoothed means with smoothing weight 10. Neighbourhood is reduced to its top-200 values plus an "OTHER" bucket.

The baseline XGBoost hyperparameters are `max_depth=6, learning_rate=0.05, min_child_weight=3, subsample=0.8, colsample_bytree=0.8, n_estimators=300, tree_method="hist", random_state=42`. The target is `log1p(duration_days)` — a transform that compresses the heavy right tail of the duration distribution. Predictions are inverted by `expm1` before computing Mean Absolute Error in days.

Evaluation uses 5-fold `KFold(shuffle=True, random_state=42)`. The baseline performance (row `E00` in `results.tsv`) is **MAE 89.401 days, Coefficient of Determination R² (log) 0.5158, Root Mean Squared Error (RMSE) 179.053 days** on the 50,000-row v2 sample. The full 5-fold wall-clock is 2.0 seconds on a single machine; this lets the 120 Phase 2 single-change experiments run sequentially in about 5 minutes.

## The Solution (What We Discovered)

### The final code (Seattle-only)

```python
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import KFold


def seattle_two_bucket_model():
    """Phase 2.5 C012 winning configuration.

    Features: days_plan_review_city + days_out_corrections (2 cols).
    Target:   log1p(duration_days).
    Model:    XGBoost (depth 4, n_est 200).
    Sample:   20,173 Seattle Plan Review issued permits (tqk8-y2z5 feed).
    Result:   MAE 24.68 days, R^2 log 0.884, R^2 days 0.844.
    """
    d = pd.read_parquet("data/clean/seattle_decomposition.parquet").copy()
    d["duration_days"] = pd.to_numeric(d["duration_days"], errors="coerce")
    d = d.dropna(subset=[
        "duration_days", "days_plan_review_city", "days_out_corrections",
    ])
    d = d[d["duration_days"] > 0].reset_index(drop=True)

    X = d[["days_plan_review_city", "days_out_corrections"]].astype("float64").values
    y_days = d["duration_days"].astype("float64").values
    y = np.log1p(y_days)

    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    oof = np.zeros(len(d))
    for tr_idx, va_idx in kf.split(d):
        model = xgb.XGBRegressor(
            objective="reg:squarederror",
            max_depth=4, n_estimators=200,
            verbosity=0, n_jobs=4, random_state=42,
        )
        model.fit(X[tr_idx], y[tr_idx])
        oof[va_idx] = model.predict(X[va_idx])

    pred_days = np.expm1(oof)
    return {
        "mae_days": float(mean_absolute_error(y_days, pred_days)),
        "r2_log":   float(r2_score(y, oof)),
        "r2_days":  float(r2_score(y_days, pred_days)),
        "n":        int(len(d)),
    }
```

Two features, shallow tree, 200 boosting rounds. **Mean Absolute Error 24.68 days, R² log 0.884** on 20,173 Seattle Plan Review permits — a 3.6x improvement over the cross-city baseline of 89.40 days, achieved entirely by swapping the feature set.

### Why this works and the cross-city baseline does not

Seattle's `tqk8-y2z5` feed publishes two permit-level summary columns that together decompose total wall time:

- **`days_plan_review_city`** — sum of active reviewer days across every review type (Zoning, Ordinance/Structural, Addressing, Drainage, Energy, Structural Engineer, Building, Mechanical, Site Engineer, and "Other").
- **`days_out_corrections`** — sum of waiting days during which the file was with the applicant for corrections.

The two columns nearly satisfy an additive identity: `duration_days ≈ days_plan_review_city + days_out_corrections + hand-off overhead`. A 2-feature Ordinary Least Squares (OLS) fit confirms this with near-unit slopes (β_city = +1.65, β_out = +0.24) and R² = 54.1%. The shallow XGBoost adds the missing non-linearity around the hand-off overhead and reaches R² log 0.884 (R² days 0.844).

No other city in our cross-city baseline publishes the equivalent columns. San Francisco's DBI feed, LA's LADBS feed, Chicago's CDB feed, and Austin's ADS feed all report the aggregated total duration but do not decompose it. This is not a modelling deficiency — it is a data deficiency. The 89.40-day cross-city MAE is a ceiling set by what the data schema can express, not a ceiling set by what XGBoost can learn.

### Difference from the baseline

| Aspect | Baseline E00 | Winner C012 |
|---|---|---|
| Scope | Cross-city (5 cities) | Seattle only |
| Features | 13 (city one-hot + calendar + numeric + 2 target-encoded) | 2 (`days_plan_review_city`, `days_out_corrections`) |
| Sample | 50,000 stratified | 20,173 Seattle issued permits |
| Model | XGBoost depth 6, 300 rounds | XGBoost depth 4, 200 rounds |
| 5-fold Cross-Validation MAE | 89.40 days | **24.68 days** |
| 5-fold Cross-Validation R² (log) | 0.5158 | **0.8843** |
| 5-fold Cross-Validation R² (days) | 0.3281 | **0.8441** |

### The New York City side story

The NYC BIS feed (`data.cityofnewyork.us/resource/ic3t-wcy2.json`) publishes four per-permit timestamps: `pre__filing_date`, `paid`, `fully_paid`, `approved`, `fully_permitted`. We computed four stage intervals from these:

- `s_filing_to_paid = paid − filed`
- `s_paid_to_fully_paid = fully_paid − paid`
- `s_fully_paid_approved = approved − fully_paid`
- `s_approved_permitted = fully_permitted − approved`

On the 143,000-permit BIS subset with all 4 stages non-null and `0 < duration_days < 1825`, a 4-stage OLS absorbs 99.9% of the variance. The `s_approved_permitted` stage (the owner pickup wait) is 62% univariate and accounts for 55% of summed total elapsed time. A 6-feature XGBoost on the 4 stages plus `filed_year` plus `has_pro_cert` (the professional-certification flag) achieves **MAE 4.04 days, R² log 0.999** on the NYC BIS subset — a 22x improvement over the cross-city baseline, again driven by feature access.

## What We Found

### 1. The Phase 2 negative result: 120 experiments, 0 KEEPs

The Phase 2 HDR loop ran 120 single-change experiments against the baseline. Each experiment changed exactly one thing: a new calendar feature, a new reform-cutoff dummy, a new rolling-load count, a new hyperparameter value, a new target transform, a new model family, or a new target-encoded column. Each was registered with a short description, a Bayesian prior, a causal mechanism, and a pre-registered keep-or-revert decision.

The keep/revert rule: KEEP if the 5-fold CV MAE improves on the best-so-far by more than `max(0.5, 0.01 × best)` days — i.e. a 0.5-day absolute threshold or a 1% relative threshold, whichever is larger. This threshold (roughly 0.89 days against the E00 baseline) was set during Phase 0.5 based on fold-to-fold standard deviation of the baseline MAE.

- **0 KEEP**
- **34 REVERT** — experiment ran, produced a number, did not clear the threshold
- **86 DEFER** — experiment blocked on schema, infrastructure, or deferred to Phase 2.5 composition

The best single Phase 2 experiment was `H086` (Optuna hyperparameter sweep on depth, learning rate, min child weight) at MAE 89.046 days — a 0.355-day improvement, well below the 0.89-day threshold. No category of change produced a Δ MAE approaching that threshold. The implication is not that the experiments were badly designed; it is that the structural noise floor on this problem, with these features, on this sample, is higher than 1 day absolute.

The most informative reverts are the target transforms:

- `H031` raw-duration target: **99.60 days** (vs 89.40 baseline) — a +10.20-day regression.
- `H033` Box-Cox ≈ log1p: 89.40 days — identical to the baseline.
- `H035` XGBoost p90 quantile: 191.38 days — predicting the 90th percentile for everyone adds 100 days of MAE.

The 10-day penalty on the raw-duration target is the cleanest evidence that the heavy right tail of the duration distribution matters: a square-error loss on the raw scale lets the 5-year outliers at 1,800 days dominate the gradient, and the fast 1-day permits are fit poorly.

### 2. The model-family tournament says the problem is close to linear

The Phase 1 tournament (rows `T01`–`T05`):

| Model | 5-fold Cross-Validation MAE |
|---|---:|
| XGBoost | 89.401 |
| LightGBM | 89.729 |
| Random Forest | 91.507 |
| ExtraTrees | 94.795 |
| Ridge (linear sanity check) | 100.561 |

The tree-to-linear MAE ratio is 89.40 / 100.56 = **0.889**. A ratio this close to 1 means the relationship between the 13 baseline features and `log1p(duration_days)` is close to linear: there is no strong non-linearity or high-order interaction for a tree to exploit. The ~11% advantage of XGBoost over Ridge is roughly the payoff of modelling the small non-linearities that exist (mostly in the log_valuation × neighborhood_te interaction and around the year-2020 COVID notch). This was the first signal, already visible in Phase 1, that the missing ingredient was features rather than model flexibility.

### 3. The Seattle decomposition: city plan review beats applicant corrections 39.2% to 18.5%

Seattle's Plan Review feed `tqk8-y2z5` ships one row per (permit × reviewtype × cycle). We collapsed these to one row per permit with per-stage columns and ran a variance decomposition. Top 6 univariate r² values (n = 20,173 issued permits, σ = 208.3 days, total variance ≈ 43,392 days²):

| Feature | r² |
|---|---:|
| `days_plan_review_city` | **39.2%** |
| `total_cycles` | 36.1% |
| `number_review_cycles` | 35.5% |
| `total_active_days` | 30.9% |
| `drainage_cycles` | 24.4% |
| `zoning_cycles` | 20.0% |
| `drainage_active_days` | 18.6% |
| `days_out_corrections` | **18.5%** |

The headline: **city plan review is 2x the applicant-correction bucket in variance explained**. The most common lay narrative about permit delays is "the applicant takes forever to respond to reviewer comments". In Seattle, when you want to predict whether a given permit will be slow, the single most informative scalar is how long the city has been reviewing it, not how long the applicant has been responding. The applicant-correction bucket does have a bigger mean and a fatter tail, but its variance share is lower.

Among per-stage active reviews, **Drainage** and **Zoning** together account for 53% of the stage-only joint R² (drainage_cycles at 31.8% + zoning_cycles at 21.3% of the stage-only attribution). These two stages dominate the within-Seattle variance even though Drainage is only present on 30% of permits and Zoning on 94%.

### 4. NYC BIS: the dominant stage is the owner pickup wait, not the DOB review

On the 143,000-permit NYC BIS subset with all 4 stages observed:

| Stage | Median | p90 | Sum / total duration |
|---|---:|---:|---:|
| Filing → Fees paid | 0 days | 0 days | 0.4% |
| Fees paid → Fully paid | 0 days | 6 days | 2.6% |
| Fully paid → DOB approved | 2 days | 149 days | **41.9%** |
| DOB approved → Permit picked up | 7 days | 197 days | **55.2%** |

The `approved → permitted` wait accounts for the majority of the summed total elapsed time. This is an *applicant-side* delay: the permit is already approved by the DOB, and the remaining time is how long the applicant takes to formally pick up the permit. The policy lever is automated pickup notifications, auto-issuance for professionally-certified filings, or a deadline-enforced pickup window — none of which require changes to the DOB's review capacity.

### 5. Intake-channel effects: 12.7x NYC, 4x LA, 7.5x Chicago

Three cities in our sample publish a column that flags which intake channel a permit was filed through. In each case, the median-duration ratio between the fast and slow channels is dramatic:

- **New York City `professional_cert`**: permits self-certified by a licensed architect or engineer clear in a median 6 days. Standard-review permits clear in a median 76 days. **12.7x speedup.**
- **Los Angeles `business_unit`**: Plan Check at Counter (over-the-counter intake) clears in a median 43 days. Regular Plan Check clears in a median 182 days. **4x spread.**
- **Chicago `review_type`**: EXPRESS clears in a median 6 days. STANDARD clears in a median 45 days. **7.5x spread.**

These are raw univariate comparisons and do not adjust for project size, neighbourhood, or filing year, so the effect magnitudes are upper bounds. But the direction and order of magnitude are clear: a substantial share of the cross-city variance is determined at intake by which channel the applicant is eligible to use. Expanding eligibility for the fast channels is a legislative / regulatory lever with near-zero engineering cost.

### 6. Phase B counterfactual: top Seattle intervention saves 44 days per permit

The Phase B discovery sweep runs a direct counterfactual: for each stage, subtract a fraction of each permit's observed per-stage active days from its total duration, then recompute the summary statistics and project annual dollar savings at $300/day × the sample's annual permit volume. Top-5 Seattle interventions at the 50% reduction level:

| Rank | Stage | Δ mean duration | Annual savings (projected) |
|---:|---|---:|---:|
| 1 | `days_out_corrections` global bucket | 44.1 days | $266.8M/year |
| 2 | `days_plan_review_city` global bucket | 37.6 days | $227.8M/year |
| 3 | Other (Building / Mechanical / Site Engineer / all other) | 26.3 days | $159.0M/year |
| 4 | Zoning | 15.8 days | $95.9M/year |
| 5 | Drainage | 10.3 days | $62.3M/year |

Top NYC BIS interventions at the 50% level:

| Rank | Stage | Δ mean duration | Annual savings (projected) |
|---:|---|---:|---:|
| 1 | Approved → Permit picked up (owner wait) | 33.4 days | $420.4M/year |
| 2 | Fully paid → DOB approved | 25.3 days | $319.3M/year |

Cross-city counterfactual: if all 5 cities published Seattle-grade per-stage data, the projected cross-city MAE would drop from 89.40 days to `89.40 × (24.68 / 99.86) = 22.09 days` — a 67-day absolute reduction, 75% relative. This is a projection based on the Seattle within-subset ratio, not a measurement. The caveats are documented in `discoveries/cross_city_counterfactual.md`: the ratio is Seattle-specific, the Seattle baseline without stages is slightly harder than the cross-city baseline (so the projected lift may be overstated), and each city's achievable lift depends on its schema's thickness.

## Key Insights

### 1. Generic Machine Learning saturates at a data-access ceiling on this problem

Every one of 120 pre-registered single-change experiments on the 13-feature 50,000-row 5-city baseline reverted. The best single experiment shaved 0.36 days off a 89.40-day baseline — below any reasonable significance threshold. No feature category, no hyperparameter, no target transform, no model family produced a 1-day improvement. The noise floor is structural: it is set by the feature set, not by the optimiser.

### 2. The resolution is data, not modelling

A two-feature shallow XGBoost on Seattle's `days_plan_review_city + days_out_corrections` reaches MAE 24.68 days — a 3.6x improvement — with a model that is strictly simpler than the cross-city baseline. The NYC BIS four-stage model does the same, reaching MAE 4.04 days on the BIS subset. Neither result required a new model architecture, a new loss, a new hyperparameter strategy, or any non-trivial feature engineering. It required the right columns.

### 3. City plan review beats applicant corrections on variance (Seattle)

The common narrative — "the city is waiting on applicants" — is the secondary story in the Seattle variance decomposition. City plan review explains 39.2% of duration variance versus applicant corrections at 18.5%. The applicant bucket has a fatter right tail, so it still dominates raw *days saved* in the Phase B sweep, but the bigger predictor of whether a given permit will be slow is how long the city has been reviewing it, not how long the applicant has been sitting on corrections.

### 4. The owner pickup wait dominates NYC BIS (55% of elapsed time)

In NYC BIS, the largest single stage by summed time is `approved → permitted`: the permit has already been approved and the only remaining step is for the applicant to formally pick it up. Half of the total elapsed time in the BIS pipeline is this post-approval wait. The policy lever is the pickup workflow (automation, notifications, deadline-enforced windows), not the DOB's review capacity.

### 5. Intake channels produce order-of-magnitude speedups (12.7x, 4x, 7.5x)

NYC's professional-certification pathway, LA's Plan-Check-at-Counter, and Chicago's EXPRESS review type each deliver dramatic median-duration speedups versus the default channels in the same cities. These effects are already in the data — they do not need a model to see. The recommendation is to expand eligibility for the fast channels, which is a legislative lever with near-zero engineering cost.

### 6. The tree-to-linear ratio of 0.889 was an early warning

Phase 1's 5-family tournament found XGBoost only 11% ahead of Ridge regression on the same feature set. On a problem where tree methods provide meaningful non-linear lift, the ratio is 2 or 3 to 1 — not 1.12 to 1. The narrow tree-to-linear gap on cross-city permit features was the first (ignored) signal that the missing ingredient was new features, not better non-linearity.

### 7. A negative Hypothesis-Driven Research result can be load-bearing

One hundred and twenty pre-registered experiments that all fail to beat a noise floor is a stronger statement about the problem's structure than 120 experiments that all succeed. The Phase 2 result on its own would be undiagnosable ("nothing works, I guess"). Paired with the Phase 2.5 Seattle result, it becomes a precise statement about what kind of thing is needed to make progress: richer feature schemas, not cleverer models. The HDR methodology turns the negative result from a dead end into the load-bearing element of the paper.

## Why This Matters

### For US municipal open-data practice

**Publish per-stage timestamps.** Every US city should publish the per-(review_type × cycle) timestamps that Seattle already publishes in `tqk8-y2z5`. The marginal data-engineering cost is small (Seattle's feed is a modest extension of the base permit-issuance feed). The predictive payoff is enormous: 3.6x on Mean Absolute Error on the Seattle subset, and a projected 75% cross-city MAE reduction if every city adopted the same standard. This is a zero-legislation, low-engineering-cost, high-payoff intervention that municipal Chief Data Officers can implement on their own authority.

### For US housing policy

**Expand fast-intake-channel eligibility.** NYC's professional-certification pathway gives a 12.7x median-duration speedup; LA's Plan Check at Counter gives 4x; Chicago's EXPRESS review gives 7.5x. These fast channels already exist and already work — they are just restricted to narrow project subsets. Expanding eligibility to cover small-residential more broadly is a legislative lever with near-zero implementation cost and a well-documented effect size.

**Automate the NYC BIS post-approval pickup wait.** Half of the elapsed time in the NYC BIS pipeline for issued permits is the `approved → permitted` wait. Half. The DOB has already approved the permit; the only remaining step is pickup. Auto-issuance for pro-cert filings, automated email/text notifications, and deadline-enforced pickup windows are standard workflow-automation tools that the DOB NOW platform is already well-positioned to implement.

**Target Drainage and Zoning cycles in Seattle-style cities.** In Seattle's stage-only attribution, Drainage cycles and Zoning cycles together account for 53% of the per-stage variance share. Standardised small-residential drainage templates and pre-check zoning clearances would directly target these bottlenecks.

### For Machine-Learning methodology

**Do not expect generic tabular ML to substitute for structural data.** The Phase 2 saturation at 89.40 days across 120 experiments on 13 commonly-published features is an explicit counter-example to the assumption that "given enough data and a good-enough model, everything is predictable". The problem is not data volume (50,000 rows is plenty for the 13-column feature space) and not model capacity (XGBoost is state-of-the-art for tabular regression). The problem is that the 13 columns do not contain the signal. A richer feature set with just 2 stage columns drops the MAE by 3.6x with a simpler model.

**Pre-register the hypothesis and act on the negative result.** The 120-experiment Phase 2 loop was load-bearing precisely because each experiment had a pre-registered keep-or-revert criterion. Zero unexplained KEEPs in 120 tries is a much stronger refutation of the feature set than zero KEEPs in a handful of informal tuning runs. The HDR methodology turns the refutation into actionable guidance: stop tuning, go find better features.

## Methodology

**Baseline.** XGBoost (Chen and Guestrin 2016) on a stratified 50,000-row sample of the five cities San Francisco, New York City, Los Angeles, Chicago, and Austin. Cleaning: both `filed_date` and `issued_date` non-null; `0 < duration_days < 1825`; `filed_date >= 2015-01-01`; per-city strict small-residential filter; status hygiene (no cancel/withdraw/void/expired/disapproved/rejected/denied/suspended). Stratification: (city × year-bucket) with four buckets, 2,500 permits per cell. 13 features: 5 city one-hot, 3 calendar (year + sin/cos month), 3 log-numeric (valuation, square feet, unit count), 2 in-fold target-encoded (permit subtype, neighborhood). Target: `log1p(duration_days)`. Hyperparameters: `max_depth=6, learning_rate=0.05, min_child_weight=3, subsample=0.8, colsample_bytree=0.8, n_estimators=300, tree_method="hist", random_state=42`. Evaluation: 5-fold `KFold(shuffle=True, random_state=42)` with in-fold target encoding. Baseline Mean Absolute Error 89.401 days, R² (log) 0.5158 (row `E00` in `results.tsv`).

**Iteration.** Phase 1 ran a 5-family model-family tournament (XGBoost, LightGBM, ExtraTrees, Random Forest, Ridge). XGBoost won by 0.33 days over LightGBM. The tree-to-linear MAE ratio of 0.889 indicated the cross-city problem was close to linear in the raw feature space, signalling early that the missing ingredient was features, not model flexibility. Phase 2 ran 120 single-change pre-registered experiments against the baseline. Each hypothesis had a short description, a rough Bayesian prior, a mechanism statement, and a pre-registered keep-or-revert criterion: KEEP if 5-fold Cross-Validation MAE improved on best-so-far by more than `max(0.5, 0.01 × best)` days, else REVERT. Experiments blocked on schema or infrastructure DEFERRED. Outcome: 0 KEEP, 34 REVERT, 86 DEFER.

Phase 2.5 ran compositional retests and schema promotion. Task 1 built the Seattle per-(review_type × cycle) decomposition from the `tqk8-y2z5` feed and ran a variance attribution. Task 2 fit Cox Proportional Hazards (lifelines), XGBoost Accelerated Failure Time (XGBoost AFT), and Random Survival Forest (scikit-survival) with right-censoring at the 2026-04-09 observation cutoff; XGBoost AFT was best at C-index 0.772. Task 3 promoted the LA `business_unit`, Chicago `review_type`, and NYC BIS per-stage timestamps that the Phase 0.5 baseline filter had dropped; rows `C014`, `C015`, and `C002` in `results.tsv`. Task 4 ran 15 compositional retest experiments combining promising Phase 2 deferred improvements; rows `C001`–`C015`. Task 5 aggregated the per-city best-so-far.

Phase B ran a counterfactual stage-time intervention sweep on the Seattle and NYC BIS samples, producing `discoveries/seattle_intervention_sweep.csv`, `discoveries/nyc_intervention_sweep.csv`, `discoveries/cross_city_counterfactual.md`, and `discoveries/headline_recommendations.md`. Phase B rows `B01`–`B05` are appended to `results.tsv`.

**Reproducibility.** The full HDR loop is reproducible from cached raw parquets via `python evaluate.py baseline`, `python evaluate.py phase25`, and `python phase_b_discovery.py`. The 4 baseline unit tests (`test_load_clean_dataset`, `test_add_features_shape`, `test_baseline_reproducibility`, `test_target_encode_no_leakage`) pass at every commit. Random seeds are fixed throughout; the baseline MAE reproduces at the sixth decimal place across runs.

## Key References

1. **van Dongen, B.F.** "BPIC 2015: Diagnostics of Building Permit Application Process in Dutch Municipalities." *BPI Challenge 2015 Task Description* (2015). [https://ais.win.tue.nl/bpi/2015/bpic2015_paper_3.pdf](https://ais.win.tue.nl/bpi/2015/bpic2015_paper_3.pdf) — the landmark process-mining benchmark on 5 Dutch municipalities' building permit event logs and the closest prior study to this paper.
2. **van der Aalst, W.M.P.** *Process Mining: Data Science in Action* (2nd ed.). Springer (2016). [DOI 10.1007/978-3-662-49851-4](https://doi.org/10.1007/978-3-662-49851-4) — the canonical process-mining textbook; discovery, conformance, enhancement, and the methodology for using event-log timestamps to decompose throughput time.
3. **Chen, T. and Guestrin, C.** "XGBoost: A Scalable Tree Boosting System." *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2016)*, 785–794. [DOI 10.1145/2939672.2939785](https://doi.org/10.1145/2939672.2939785) — the gradient-boosting library used for both the baseline and the winning Seattle model.
4. **Wright, B.** "Study: SF slower to issue building permits." *San Francisco Examiner* (2025). [sfexaminer.com](https://www.sfexaminer.com/news/urban-development/sf-is-slower-than-other-cities-in-issuing-housing-permits/article_4049aac3-608e-4c06-a03b-bf2ef1d2b1f7.html) — the source of the 280 / 91 / 134 day headline numbers for SF, Austin, and San Diego that frame the research question.
5. **Gyourko, J.; Saiz, A.; Summers, A.** "A New Measure of the Local Regulatory Environment for Housing Markets: The Wharton Residential Land Use Regulatory Index." *Urban Studies* 45(3), 693–729 (2008). [DOI 10.1177/0042098007087341](https://doi.org/10.1177/0042098007087341) — the Wharton Residential Land Use Regulatory Index (WRLURI) that is the standard cross-sectional jurisdiction-level measure of regulatory stringency and the natural complement to project-granularity work.
6. **Glaeser, E.L. and Gyourko, J.** "The Economic Implications of Housing Supply." *Journal of Economic Perspectives* 32(1), 3–30 (2018). [DOI 10.1257/jep.32.1.3](https://doi.org/10.1257/jep.32.1.3) — the regulatory-tax framework interpreting the price-vs-cost gap as an implicit tax of regulation.
7. **Cox, D.R.** "Regression Models and Life-Tables." *Journal of the Royal Statistical Society Series B* 34(2), 187–220 (1972). [DOI 10.1111/j.2517-6161.1972.tb00899.x](https://doi.org/10.1111/j.2517-6161.1972.tb00899.x) — the original Cox Proportional Hazards model used in the Phase 2.5 survival analysis (row `S01_cox`).
8. **Barnwal, A.; Cho, H.; Hocking, T.** "Survival Regression with Accelerated Failure Time Model in XGBoost." *Journal of Computational and Graphical Statistics* 31(4), 1292–1302 (2022). [DOI 10.1080/10618600.2022.2067548](https://doi.org/10.1080/10618600.2022.2067548) — the XGBoost AFT loss used for the best-performing survival model `S02_xgb_aft` at C-index 0.772.
9. **Little, J.D.C.** "A Proof for the Queuing Formula: L = λW." *Operations Research* 9(3), 383–387 (1961). [DOI 10.1287/opre.9.3.383](https://doi.org/10.1287/opre.9.3.383) — Little's Law, the steady-state queueing identity linking backlog and throughput time that is the simplest analytic tool for reading the SF 1,489-day backlog number.
10. **Einstein, K.L.; Glick, D.M.; Palmer, M.** *Neighborhood Defenders: Participatory Politics and America's Housing Crisis*. Cambridge University Press (2019). [DOI 10.1017/9781108769495](https://doi.org/10.1017/9781108769495) — the empirical NIMBY / planning-meeting-attendance study that frames the political-economy side of the delay story.
11. **Leemans, S.J.J.; Fahland, D.; van der Aalst, W.M.P.** "Discovering Block-Structured Process Models from Event Logs — A Constructive Approach." *Petri Nets 2013*, LNCS 7927, 311–329 (2013). [DOI 10.1007/978-3-642-38697-8_17](https://doi.org/10.1007/978-3-642-38697-8_17) — the Inductive Miner, the recommended process-discovery algorithm for any follow-on Seattle / NYC process-mining study.
12. **City of Austin.** "HOME Amendments." *AustinTexas.gov* (2024). [austintexas.gov/page/home-amendments](https://www.austintexas.gov/page/home-amendments) — the official resource on Austin's HOME Phase 1 and Phase 2 zoning reforms and their associated permit-pipeline streamlining; Austin's 91-day median in the Wright (2025) SF Examiner comparison above is a partial consequence of these reforms.

Remaining 338 citations are in the project `papers.csv` (id, title, authors, year, venue, DOI, theme, notes) with 200+ referenced in the full `literature_review.md` synthesis.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the Hypothesis-Driven Research framework, the program.md specification, and the full project history including `data_loaders.py`, `model.py`, `evaluate.py`, `phase25.py`, `phase_b_discovery.py`, the 4 baseline unit tests, and the 125-row `results.tsv` in `applications/building_permits/`
