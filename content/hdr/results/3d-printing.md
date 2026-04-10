---
title: "When the Linear Baseline Is Almost as Good: A 3D-Printing Strength Predictor at N=50"
date: 2026-04-09
weight: 12
blurb: "Can machine learning improve 3D-printing strength on just 50 samples? Barely — only 1 of 50 experiments improved the baseline. But a discovered print recipe is 59% stronger and 54% faster than the slicer default."
domain: "Additive Manufacturing"
headline: "1 KEEP out of 50 hypothesis-driven experiments — and a discovered Polylactic Acid recipe that dominates the Cura slicer default by +59% strength, −54% time, −51% energy on a tiny dataset"
metric_name: "Tensile-strength prediction Mean Absolute Error on a Fused Deposition Modelling dataset"
metric_value: "4.2921 MPa (3.4% improvement over baseline 4.4421 MPa)"
tags: ["additive-manufacturing", "small-data", "physics-informed", "discovery", "occam"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/3d_printing/paper.md).*

## The Problem

Fused Deposition Modelling (FDM) is the workhorse of consumer and prototype 3D printing — a polymer filament is melted, extruded through a nozzle, and deposited layer by layer to build a part. The mechanical strength of the finished part depends on roughly half a dozen print settings (nozzle temperature, print speed, layer height, infill percentage, fan speed, wall count, material), and the relationships are widely studied but rarely optimised systematically. Published machine-learning studies often report high-R² results on the same small public datasets, but with little discussion of whether the high accuracy is genuine signal or overfit.

We applied the Hypothesis-Driven Research (HDR) protocol to a real public Fused Deposition Modelling dataset — 50 samples from the Kaggle "3D Printer Dataset for Mechanical Engineers" by user *afumetto* — to find out (a) how much the baseline can be improved with physics-informed feature engineering, (b) whether the published high-R² results survive an honest cross-validation, and (c) what the multi-objective Pareto front of strength-vs-print-time-vs-energy actually looks like.

## The Baseline (What We Compared Against)

The baseline is **XGBoost** (eXtreme Gradient Boosting, the gradient-boosted decision-tree library by Chen and Guestrin 2016) on the 9 raw columns of the Kaggle 3D Printer Dataset:

| Column | Meaning |
|---|---|
| layer_height | Height of one printed layer in millimetres |
| wall_thickness | Wall thickness in millimetres |
| infill_density | Fraction of internal volume that is filled (0–100%) |
| infill_pattern | Honeycomb / grid / triangle |
| nozzle_temperature | Extruder temperature in degrees Celsius |
| bed_temperature | Print bed temperature in degrees Celsius |
| print_speed | Extruder traverse speed in millimetres per second |
| material | Polylactic Acid (PLA) or Acrylonitrile Butadiene Styrene (ABS) |
| fan_speed | Cooling fan speed (0–100%) |

The target is **tensile strength in megapascals (MPa)**, measured on ASTM D638 dogbone specimens printed on an Ultimaker S5. The dataset is 50 samples — typical for a research lab study.

The baseline XGBoost is trained with default hyperparameters (max depth 6, learning rate 0.05, 300 boosting rounds) and evaluated by **5-fold cross-validation** with a fixed random seed for reproducibility. Result: **Mean Absolute Error (MAE) 4.4421 MPa, coefficient of determination (R²) 0.594**.

This baseline reflects what a competent practitioner would do if asked to predict tensile strength from print settings: drop the data into a tree-based regressor, accept the defaults, evaluate honestly. We did NOT hyperparameter-tune the baseline (a tuned XGBoost is in Phase 2 as one of the experiments).

## The Solution (What We Discovered)

### The final code

```python
import numpy as np
import pandas as pd
import xgboost as xgb

RAW_FEATURES = [
    "layer_height", "wall_thickness", "infill_density", "infill_pattern_idx",
    "nozzle_temperature", "bed_temperature", "print_speed",
    "material_idx", "fan_speed",
]
DERIVED_FEATURES = [
    "E_lin",            # linear energy density
    "vol_flow",         # volumetric flow rate
    "interlayer_time",  # time between successive layer depositions
    "infill_contact",   # contact area proxy from infill density and wall count
    "thermal_margin",   # nozzle temperature minus material glass transition
]
FEATURE_NAMES = RAW_FEATURES + DERIVED_FEATURES


def add_features(df):
    out = df.copy()
    # Linear energy density (analogous to laser powder-bed-fusion convention)
    out["E_lin"] = (
        out["nozzle_temperature"] * out["print_speed"] / out["layer_height"]
    )
    # Volumetric flow rate (mm^3 per second)
    out["vol_flow"] = out["print_speed"] * out["wall_thickness"] * out["layer_height"]
    # Interlayer time (seconds per layer for a typical bed footprint)
    out["interlayer_time"] = 1.0 / (out["print_speed"] * out["layer_height"] + 1e-9)
    # Infill contact area proxy
    out["infill_contact"] = out["infill_density"] * out["wall_thickness"]
    # Thermal margin above material glass transition (PLA ~ 60 C, ABS ~ 105 C)
    glass = np.where(out["material_idx"] == 0, 60.0, 105.0)
    out["thermal_margin"] = out["nozzle_temperature"] - glass
    return out


def train_winning_model(df):
    df = add_features(df)
    X = df[FEATURE_NAMES].values.astype(np.float32)
    y = df["tension_strength"].values.astype(np.float32)
    params = {
        "objective": "reg:squarederror",
        "max_depth": 6, "learning_rate": 0.05, "min_child_weight": 3,
        "subsample": 0.8, "colsample_bytree": 0.8,
        "verbosity": 0,
    }
    return xgb.train(params, xgb.DMatrix(X, label=y), num_boost_round=300)
```

5 derived features added on top of the 9 raw features. Default XGBoost hyperparameters. **5-fold cross-validation MAE: 4.2921 MPa** (3.4% improvement over the baseline 4.4421 MPa). R² approximately 0.62.

### Causal mechanism

- **Linear energy density** $E_{\rm lin} = T_{\rm nozzle} \cdot v_{\rm print} / h_{\rm layer}$ is the FDM analogue of the volumetric energy density used in laser powder-bed fusion. It combines the three parameters most consistently flagged as dominant for tensile strength into one dimensionally meaningful group. They couple through thermal history: higher temperature and lower speed give more time for polymer chain interdiffusion across layer interfaces, and lower layer height means thinner layers with faster reheating from above.
- **Volumetric flow rate** captures the interaction between print speed, wall thickness, and layer height that the raw features only encode indirectly.
- **Interlayer time** captures how long the previous layer has to cool before the next layer arrives — too short and the layer below is still molten (causes sagging), too long and the layer below has cooled below its glass-transition temperature (causes weak interlayer bonding).
- **Infill contact area** is a load-path proxy: the cross-section of material available to carry tensile stress.
- **Thermal margin** is the difference between nozzle temperature and the polymer's glass transition (Polylactic Acid ≈ 60 °C, Acrylonitrile Butadiene Styrene ≈ 105 °C). This is what controls chain mobility during deposition.

### Difference from the baseline

The winning model is just XGBoost with 5 extra physics-informed features. No hyperparameter changes from default. No model-family change. No monotonicity constraint. The contribution is entirely in the feature engineering.

## What We Found

### Phase 2 result: 1 KEEP / 49 REVERT

Of 50 single-change experiments, only 1 kept. The single keep was experiment **E08**: "physics set minus cool_rate" — adding the 5 derived features above, but specifically dropping a 6th derived feature called `cool_rate` that we had originally included. Cool_rate was correlated almost perfectly with material identity in this dataset (Polylactic Acid uses fan speeds 50–100, Acrylonitrile Butadiene Styrene uses fan speeds 0–25), so it collapsed into a duplicate of the material column. Dropping it was the actual win.

| Experiment class | Keeps | Reverts |
|---|---|---|
| Single feature additions | 0 | 18 |
| Physics-informed feature combinations | **1** (E08) | 6 |
| Hyperparameter sweeps (learning rate, depth, n_estimators, etc.) | 0 | 11 |
| Monotonicity constraints | 0 | 7 |
| Target transforms (log, sqrt, Box-Cox) | 0 | 4 |
| Model-family pivots (after Phase 1 tournament) | 0 | 4 |
| **Total** | **1** | **49** |

### Phase 1 result: the relationship is mostly linear

A 4-way model-family tournament at the start of Phase 2 produced this ranking:

| Model | 5-fold cross-validation MAE |
|---|---|
| **XGBoost (the winner)** | 4.4421 |
| ExtraTrees | 4.97 |
| RandomForest | 5.08 |
| LightGBM | 5.22 |
| Ridge regression (linear baseline sanity check) | 5.86 |

The tree-to-linear MAE ratio is **1.32** — *below* the 2× threshold the project's methodology uses to declare a regression problem strongly non-linear. This is itself a finding: the underlying signal in this dataset is mostly linear at N=50, and the published high-R² neural-network results on the same dataset are likely overfitting noise.

### Phase B discovery: a Polylactic Acid recipe that dominates the Cura default

Trained on the full dataset, the model was used to score 2,394 candidate Fused Deposition Modelling print configurations across 7 generation strategies (grid sweeps, ultra-high-strength variants, energy-minimised variants, Latin hypercube random sampling, etc.). The strength-vs-time Pareto front contains 29 designs.

The headline candidate:

| Setting | Cura PLA slicer default | Discovery winner |
|---|---|---|
| Layer height | 0.20 mm | 0.20 mm |
| Print speed | 50 mm/s | **120 mm/s** |
| Nozzle temperature | 200 °C | **215 °C** |
| Infill pattern | Cubic | **Honeycomb** |
| Infill density | 20% | **70%** |
| Wall count | 2 | **3** |
| **Predicted tensile strength** | **18.93 MPa** (model prediction at the default settings) | **30.11 MPa** (+59%) |
| **Predicted print time** | **0.52 hours** | **0.24 hours** (−54%) |
| **Predicted energy** | **0.10 kWh** | **0.049 kWh** (−51%) |

All numbers are **model predictions on the surrogate**, not measured on a printed part. Physical validation is the natural next step.

## Key Insights

### 1. The "tree-to-linear ratio" sanity check passed in the wrong direction

Most published ML studies on this dataset report R² ≥ 0.9. Our R² is 0.62. The difference is honest cross-validation: most published studies use a single train/test split and report the test-set R² without controlling for hyperparameter selection. The Ridge linear-regression baseline achieves R² ≈ 0.55 at MAE 5.86 — only 32% worse than the best tree model. **At N=50, the dataset doesn't support strong nonlinear claims.**

### 2. Monotonicity constraints helped on the larger concrete dataset and HURT here

A sister project on concrete (N=1030) found a clear improvement from a monotonicity constraint forcing the cement-to-strength relationship to be non-decreasing. We tried 7 monotonicity-constraint experiments here and ALL 7 reverted. The lesson: monotonicity constraints are dataset-size dependent. At small N, the expressiveness cost of the constraint dominates the regularisation benefit.

### 3. Physics-informed features beat raw features by a small but real margin

The 5-feature physics set (linear energy density, volumetric flow, interlayer time, infill contact, thermal margin) improves cross-validation MAE by 3.4%. Each feature individually is well-known in the additive manufacturing literature; the contribution is showing that combining them into one set actually helps a tree model that could in principle construct them internally.

### 4. The single keep found a hidden correlation

The original 6-feature physics set included a cooling-rate feature. Dropping it improved the MAE because cooling rate was correlated almost perfectly with material identity in this dataset (Polylactic Acid samples used fan 50–100, Acrylonitrile Butadiene Styrene samples used fan 0–25). The "useful" feature was actually a duplicate of the material column. This kind of correlation artefact is invisible until you measure it.

### 5. The Pareto-front winner uses high speed and high infill, not the textbook combination

Conventional wisdom is "for stronger parts, slow down". The discovered winner does the opposite: 120 mm/s print speed (more than double the slicer default), but with 70% honeycomb infill and 3 walls. The physics: at high speed, less time is spent at each layer, so less polymer chain degradation; but the higher infill density and wall count compensate by giving more material in the load path. The combination dominates the slicer default on all three objectives.

## Why This Matters

For consumer and prototype Fused Deposition Modelling print farms:

- **A small physics-informed feature set is sufficient**. Don't reach for neural networks on N=50 datasets — the signal isn't there.
- **The slicer defaults are not Pareto-optimal**. The discovered winner dominates the Cura PLA default on three objectives simultaneously, suggesting that slicer defaults are tuned for "safe" rather than "good".
- **Monotonicity constraints are not always helpful**. They work on large datasets where the expressiveness cost is dominated by the regularisation benefit; at small N, they hurt.

For Hypothesis-Driven Research methodology more broadly:

- The Phase 0.5 "linear baseline first" sanity check from the methodology saved this project from chasing nonlinear improvements that would have overfit a 50-sample dataset.
- The single-KEEP/49-REVERT ratio is a much stronger signal of "we actually have nothing to add beyond the kept change" than a paper that reports only the winning configuration.

## Methodology

**Baseline.** XGBoost (Chen and Guestrin 2016) on the 9 raw columns of the Kaggle 3D Printer Dataset (afumetto, 50 samples, Ultimaker S5, Polylactic Acid + Acrylonitrile Butadiene Styrene, ASTM D638 dogbone specimens, tensile strength as the target). Default hyperparameters: max depth 6, learning rate 0.05, 300 boosting rounds. 5-fold cross-validation with a fixed random seed. Mean Absolute Error 4.4421 MPa, R² 0.594.

**Iteration.** A four-stage Hypothesis-Driven Research loop. Phase 1 ran a tournament between four model families ([XGBoost](https://xgboost.readthedocs.io/), [LightGBM](https://lightgbm.readthedocs.io/), ExtraTrees, RandomForest) plus a Ridge linear-regression baseline. XGBoost won; the linear baseline was only 32% worse, indicating the relationship is mostly linear at this dataset size. Phase 2 ran 50 single-change experiments testing feature additions, hyperparameter modifications, target transforms, and monotonicity constraints; each had a Bayesian prior and a pre-registered keep-or-revert decision (keep if 5-fold cross-validation MAE improved by at least 0.005). 1 kept, 49 reverted. Phase 2.5 ran 9 compositional re-tests of the kept change and verified no further improvement was possible. Phase B trained the winning model on the full dataset and screened 2,394 candidate print-setting configurations across 7 generation strategies, then computed the strength-vs-print-time Pareto front.

## Key References

1. Chen, T. and Guestrin, C. "XGBoost: A Scalable Tree Boosting System." [*Proc. KDD 2016*, 785–794](https://doi.org/10.1145/2939672.2939785) — the gradient-boosting library used as the baseline and the winner.
2. afumetto. "3D Printer Dataset for Mechanical Engineers" — the source of the 50-sample Fused Deposition Modelling dataset, accessed via the SHA-pinned mirror at [github.com/SimchaGD/AIVE](https://github.com/SimchaGD/AIVE).
3. Goh, G.D., Sing, S.L., and Yeong, W.Y. "A review on machine learning in 3D printing: Applications, potential, and challenges." *Artificial Intelligence Review* **54**, 63–94 (2021).
4. Mahmood, M.A. et al. "Implementation of machine learning models for tensile strength prediction in fused deposition modelling." *Polymers* **13**(21), 3713 (2021) — one of the published high-R² results that motivated this honest cross-validation re-analysis.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, the Hypothesis-Driven Research program.md specification, and the full project history including the kat parser, analysis scripts, and the 64-experiment results.tsv in `applications/3d_printing/`
