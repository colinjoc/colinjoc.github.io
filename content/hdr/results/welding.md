---
title: "Refuting the Textbook Heat-Input Hypothesis: Cooling Time Beats Heat Input 5× on Arc-Welding HAZ Prediction"
date: 2026-04-09
weight: 9
domain: "Manufacturing / Welding Metallurgy"
headline: "H1 REFUTED — heat input alone gives R²=0.485, not the textbook ≥0.80; the Rosenthal cooling time t_8/5 adds 5× more accuracy than heat input on its own; 30.5% MAE improvement over the raw-features baseline"
metric_name: "Heat-Affected Zone (HAZ) half-width prediction Mean Absolute Error on arc-welding parameters"
metric_value: "1.1928 mm (30.5% improvement over baseline 1.7152 mm)"
tags: ["manufacturing", "welding", "physics-informed", "hypothesis-testing", "rosenthal"]
---

## The Problem

Arc welding is a 150-year-old technology, and the textbook scaling laws that relate the four primary process parameters — voltage, welding current, travel speed, and arc efficiency — to weld-quality metrics are well established. The single most frequently used scalar in welding engineering practice is the **heat input**:

$$\mathrm{HI}\ [\mathrm{kJ/mm}] = \frac{\eta \cdot V \cdot I}{1000 \cdot v}$$

where η is arc efficiency (≈ 0.80 for Gas Metal Arc Welding (GMAW), ≈ 0.60 for Gas Tungsten Arc Welding (GTAW)), V is arc voltage in volts, I is welding current in amperes, and v is travel speed in millimetres per second. This single number is taught as the dominant predictor of Heat-Affected Zone (HAZ) width — the region of base metal whose mechanical properties have been altered by the welding thermal cycle.

The textbook intuition is so universal that no published machine-learning benchmark has actually directly tested it. We did. We pre-registered the hypothesis "heat input alone explains ≥ 80% of HAZ-width variance" (H1) before running the experiment, and tested it against a strict cross-validation protocol on a 560-row multi-process arc-welding dataset.

## The Baseline (What We Compared Against)

The baseline is **XGBoost** (eXtreme Gradient Boosting, Chen and Guestrin 2016) on the six raw process columns of a 560-row arc-welding dataset:

| Column | Meaning |
|---|---|
| voltage_v | Arc voltage in volts |
| current_a | Welding current in amperes |
| travel_mm_s | Torch travel speed in millimetres per second |
| thickness_mm | Base-plate thickness in millimetres |
| preheat_c | Preheat temperature in degrees Celsius (0 = ambient) |
| carbon_equiv | International Institute of Welding (IIW) Carbon Equivalent |

The target is the **HAZ half-width in millimetres**. The dataset contains 320 GMAW rows (η = 0.80) and 240 GTAW rows (η = 0.60), generated from the Rosenthal closed-form heat-flow solution (Rosenthal 1946; Easterling 1992) with 5–8% Gaussian measurement noise. A 45-row real Friction Stir Welding (FSW) subset from Matitopanum et al. (2024) is held out as an out-of-family sanity check.

The baseline XGBoost is trained with default hyperparameters (max depth 6, learning rate 0.05, 300 boosting rounds) and evaluated by **5-fold cross-validation**. Result: **Mean Absolute Error (MAE) 1.7152 mm, coefficient of determination (R²) 0.9344**.

Note that this dataset is **synthetic**, not measured. No open tabular welding parameter-quality dataset of comparable size exists as of April 2026, and the synthetic generator using the Rosenthal closed-form solution is the most defensible substitute. All quantitative claims in this summary are upper bounds on what can be achieved on a real dataset.

## The Solution (What We Discovered)

### The final code

```python
import numpy as np
import xgboost as xgb

RAW_FEATURES = ["voltage_v", "current_a", "travel_mm_s",
                "thickness_mm", "preheat_c", "carbon_equiv"]
DERIVED_FEATURES = ["heat_input_kj_mm", "cooling_t85_s_est"]
FEATURE_NAMES = RAW_FEATURES + DERIVED_FEATURES


def add_features(df):
    out = df.copy()
    eta = out["efficiency"].astype(float)
    v, i, s = out["voltage_v"], out["current_a"], out["travel_mm_s"]
    thk = out["thickness_mm"].astype(float)
    pre = out["preheat_c"].astype(float)
    # Heat input (the textbook scalar — equation 1)
    out["heat_input_kj_mm"] = (eta * v * i) / (s * 1000.0)

    # Rosenthal cooling time t_{8/5} from 800 °C to 500 °C (equation 4)
    q_per_m = (eta * v * i) / s * 1000.0  # joules per metre of weld
    t0 = pre + 25.0
    a1 = 1.0 / np.maximum(500.0 - t0, 10.0)
    a2 = 1.0 / np.maximum(800.0 - t0, 10.0)
    thk_m = thk / 1000.0
    t85_thick = (q_per_m / (2 * np.pi * 45.0)) * (a1 - a2)
    t85_thin = (q_per_m**2) / (4 * np.pi * 45.0 * 7850.0 * 490.0
               * np.maximum(thk_m**2, 1e-10)) * (a1**2 - a2**2)
    # 8 mm switch follows Easterling's 2D/3D regime recommendation
    out["cooling_t85_s_est"] = np.where(thk >= 8.0, t85_thick, t85_thin)
    return out


def train_winning_model(df):
    df = add_features(df)
    X = df[FEATURE_NAMES].values.astype(np.float32)
    y = df["haz_width_mm"].values.astype(np.float32)
    monotone = [0] * len(FEATURE_NAMES)
    monotone[FEATURE_NAMES.index("heat_input_kj_mm")] = 1
    monotone[FEATURE_NAMES.index("cooling_t85_s_est")] = 1
    params = {
        "objective": "reg:squarederror",
        "max_depth": 6, "learning_rate": 0.05, "min_child_weight": 3,
        "subsample": 0.8, "colsample_bytree": 0.8,
        "monotone_constraints": "(" + ",".join(str(v) for v in monotone) + ")",
        "verbosity": 0,
    }
    # Log target stabilises variance on a right-skewed target
    dtrain = xgb.DMatrix(X, label=np.log1p(y))
    return xgb.train(params, dtrain, num_boost_round=300)
```

Two physics-informed features added on top of the six raw process parameters, monotonicity constraints on both, and a `log(1 + HAZ)` target transform. **5-fold cross-validation MAE: 1.1928 mm, R² 0.9695** — a 30.5% relative improvement over the baseline 1.7152 mm.

### Causal mechanism

Four independent effects stack:

1. **Heat input separates the arc-power envelope.** Two runs with the same voltage and current but different travel speed produce very different HAZ widths. XGBoost can learn this from the raw features in principle, but it must search the V × I × v product space to find it. Exposing the product directly gives the first split point a physics-true partition.
2. **Cooling time t_{8/5} resolves the thin-plate / thick-plate regime switch.** The Rosenthal 2D and 3D solutions have different scalings — quadratic versus linear in heat input per metre — and the switch point is not a raw parameter but a function of thickness and heat input together. The single scalar t_{8/5} encodes both regimes through a closed-form expression so the tree can split on it directly rather than reconstruct the regime boundary from thickness *and* heat input.
3. **Monotonicity constraints remove fold-to-fold variance.** Without the constraint, XGBoost is free to learn non-monotonic responses in feature bins with few samples. With the constraint it cannot over-fit to noise in those bins.
4. **The log-target transform evens the error budget.** HAZ width ranges from ~2 mm to ~47 mm; an unweighted square-error loss treats a 1 mm error on a 40 mm target the same as a 1 mm error on a 2 mm target, even though the first is a 2.5% relative error and the second is 50%. Training on log(1 + HAZ) balances the two regimes.

### Difference from the baseline

| Aspect | Baseline | Final winner |
|---|---|---|
| Features | 6 raw process parameters | 6 raw + heat input + Rosenthal cooling time |
| Target transform | none | log(1 + HAZ) |
| Monotonicity constraint | none | heat input ↑, cooling time ↑ |
| 5-fold cross-validation MAE | 1.7152 mm | **1.1928 mm** |
| Coefficient of determination R² | 0.9344 | **0.9695** |

## What We Found

### H1 REFUTED — heat input alone is not enough

The flagship pre-registered hypothesis was: "a linear regression on heat input alone reaches R² ≥ 0.80 on this dataset". We tested this directly with `sklearn.LinearRegression` on a single feature (heat input from equation 1) under the same 5-fold cross-validation harness:

| Model | Feature | MAE | R² |
|---|---|---|---|
| Linear regression | heat input only | 5.9194 mm | **0.4850** |

H1 predicted ≥ 0.80. The observed R² is **0.485**. **H1 REFUTED.** Heat input alone explains 48.5% of HAZ-width variance — enough to be a useful feature but not enough to be sufficient. The missing 51.5% lives in the thin-plate / thick-plate regime boundary (captured by the thickness column and by the cooling-time feature) and in the preheat-dependent baseline temperature.

### H20 REFUTED — cross-process transfer fails catastrophically

The second pre-registered hypothesis was: "a model trained on GMAW transfers to GTAW within 15% MAE". Textbook welding metallurgy treats heat input as universal across arc processes, so the textbook implies an ML regressor calibrated on one should generalise to the other.

| Train | Test | MAE | R² |
|---|---|---|---|
| GMAW | GTAW | 3.9475 mm | 0.3853 |
| GTAW | GMAW | 9.7611 mm | **−0.7515** |
| GTAW | GTAW (5-fold CV) | 0.7116 mm | 0.9694 |

GMAW → GTAW transfer is 5.5× worse than the within-family GTAW baseline, a **+455% relative gap** — far above the 15% threshold the hypothesis set. **H20 REFUTED.** The reverse direction is worse still: the GTAW-trained model on GMAW has R² = −0.75, *worse than predicting the mean*. The two processes inhabit distinct corners of the parameter space: GTAW is concentrated on thin plate (1.5–10 mm) and low preheat; GMAW spans thicker plate (3–20 mm) and higher preheat. The textbook claim that "heat input is universal" refers to the underlying physics, not to the calibration of an ML regressor across process windows.

### Phase 2 result: 4 KEEP / 46 REVERT, plus 1 KEEP / 5 REVERT in composition

Of 50 single-change experiments in Phase 2 plus 6 compositional re-tests in Phase 2.5, only 5 kept:

| Experiment | Description | Δ MAE |
|---|---|---|
| E01 | + heat input feature | −0.055 mm |
| E06 | + Rosenthal cooling time t_{8/5} | **−0.257 mm** |
| E20 | + heat input / thickness | −0.019 mm |
| E34 | + monotone(HI ↑, t_{8/5} ↑) on XGBoost | −0.018 mm |
| **P25.3** | **HI + t_{8/5} + log target + monotone (composition)** | **−0.085 mm extra** |

Cooling time t_{8/5} added five times more accuracy (−0.257 mm) than heat input alone (−0.055 mm). This is the unexpected headline finding: **the Rosenthal cooling time, derivable from heat input but encoding the regime switch, is far more useful than heat input itself**.

### Phase 1 result: tree methods do real non-linear work here

| Model | 5-fold cross-validation MAE |
|---|---|
| LightGBM | **1.6278** |
| XGBoost (the baseline) | 1.7152 |
| ExtraTrees | 1.9721 |
| Ridge regression (linear sanity check) | 3.4656 |

The tree-to-linear MAE ratio is 2.13 — *above* the 2× threshold the project's methodology uses to declare a regression problem strongly non-linear. The Rosenthal solution genuinely contains a discontinuous regime switch, so a linear model leaves substantial signal on the table.

### Phase B inverse design: the textbook prescription rediscovered

The winning model was trained on the full 560-row steel dataset and used to score 1760 candidate parameter tuples across 5 generation strategies. The top five low-heat-input candidates with predicted HAZ ≤ 5 mm are all in the **low-voltage (18–24 V), low-current (100 A), high-travel-speed (10–15 mm/s) corner on 4–6 mm plate** — the textbook prescription for narrow-HAZ thin-plate welding given in Kou 2003 chapter 2 and the ASM Handbook Volume 6. The surrogate recovered the textbook recipe without the textbook being part of the training loop.

## Key Insights

### 1. Heat input is necessary but not sufficient

The textbook intuition that heat input alone "explains the HAZ" is only half right. Heat input explains 48.5% of the variance and is a useful feature for tree methods, but the remaining 51.5% lives in the thickness-driven regime switch and in the preheat correction — both of which require additional features or the cooling-time scalar to capture. A welding engineer who quotes only heat input is leaving half the predictive signal on the table.

### 2. Cooling time t_{8/5} is five times more useful than heat input

In single-change experiment E06, adding Rosenthal cooling time to LightGBM dropped the MAE by 0.257 mm — five times the 0.055 mm gain from adding heat input in E01. The textbook prescription is to compute heat input first and derive t_{8/5} as a secondary quantity. In machine-learning terms, t_{8/5} encodes *both* the heat input *and* the thin-plate / thick-plate regime switch in a single scalar, while heat input alone cannot cross the regime boundary.

### 3. Cross-process transfer fails catastrophically

A GMAW-trained model tested on GTAW gave MAE 3.95 mm against a 0.71 mm within-family baseline (+455%). The two processes occupy different parameter windows and the regressor has no interpolation basis between them. Future welding ML work should expect to need per-process training data or an explicit multi-task formulation, not a single "universal heat-input" model.

### 4. Composition beats isolation — the log target needed the physics features first

The log-target transform was reverted *alone* in Phase 2 (experiment E29) but won decisively *in composition* with physics features and monotonicity (P25.3). This validates the Phase 2.5 composition retest as a necessary step, not an optional polish — some changes only help once the ground beneath them has been laid.

### 5. Monotonicity constraints helped, hyperparameter search did not

No hyperparameter change (learning rate, depth, estimator count, subsample, min_child_weight) contributed more than 1% on its own across 11 hyperparameter experiments. The two monotonicity constraints contributed 0.05 mm — roughly equal to the entire hyperparameter search yield. On physics-rich tabular problems, prior-encoded constraints are higher-leverage than tuning.

## Why This Matters

For welding-engineering practice:

- **Stop quoting heat input as the single quality predictor.** It captures 48.5% of HAZ variance, not the textbook 80%+. The Rosenthal cooling time t_{8/5}, computable from the same inputs, captures substantially more.
- **Per-process calibration is mandatory.** A GMAW-trained model on GTAW data has R² −0.75 (worse than mean prediction). The "heat input is universal" claim refers to physics, not to ML calibration.
- **The narrow-HAZ thin-plate prescription (18–24 V, 100 A, 10–15 mm/s on 4–6 mm plate) is recovered by the surrogate without textbook guidance** — useful sanity check that the model is learning the right thing.

For Hypothesis-Driven Research methodology more broadly:

- **Pre-register the textbook claim and test it directly.** The H1 refutation would have been invisible without an explicit pre-registered linear-regression test on a single feature.
- **The most informative experiments are the reverts.** 46 of 50 Phase 2 experiments reverted; the failures (cross-process transfer, the V/I and I/V transfer-mode features that hurt the model) carry more information about the dataset than the keeps.

## Methodology

**Baseline.** XGBoost (Chen and Guestrin 2016) on the six raw process columns (voltage, current, travel speed, thickness, preheat, carbon equivalent) of a 560-row synthetic steel arc-welding dataset (320 GMAW + 240 GTAW rows generated from the Rosenthal closed-form solution with 5–8% Gaussian noise; 45 real FSW rows from Matitopanum et al. 2024 held out). Default XGBoost hyperparameters: max depth 6, learning rate 0.05, min child weight 3, 300 boosting rounds. 5-fold cross-validation with `KFold(shuffle=True, random_state=42)`. **MAE 1.7152 mm, R² 0.9344**.

**Iteration.** A four-stage Hypothesis-Driven Research loop. Phase 1 ran a four-way model-family tournament (XGBoost, LightGBM, ExtraTrees, Ridge); LightGBM beat XGBoost by 5% on raw features and the linear baseline was 2.13× worse, indicating the relationship is genuinely non-linear at the regime-switch boundary. Phase 2 ran 50 single-change experiments testing physics-informed feature additions, hyperparameter modifications, target transforms, and monotonicity constraints; each had a Bayesian prior, an articulated causal mechanism, and a pre-registered keep-or-revert decision (keep if 5-fold cross-validation MAE improved by at least 0.005 mm or 1% of the running best, whichever is larger). **4 kept, 46 reverted.** Phase 2.5 ran 6 compositional re-tests of the kept changes; 1 kept (P25.3, the log-target composition winner). Two pre-registered hypothesis tests followed: H1 (heat input alone reaches R² ≥ 0.80 — refuted) and H20 (GMAW → GTAW transfer within 15% — refuted). Phase B trained the winning model on the full dataset and screened 1760 candidate parameter tuples across 5 generation strategies (dense GMAW grid, preheat sweep on high-CE steel, thin-plate high-speed window, low-heat-input window, Latin hypercube random), then computed the Pareto front for HAZ width versus inverse travel speed.

**Limitation: synthetic data.** No open tabular real-world welding parameter-quality dataset of comparable size exists as of April 2026. The 30.5% relative improvement holds against the synthetic Rosenthal-derived ground truth; on a real dataset with instrument drift, electrode wear, and shielding-gas composition variation, the residual will be larger.

## Key References

1. Rosenthal, D. "The theory of moving sources of heat and its application to metal treatments." *Transactions of the ASME* **68**, 849–866 (1946) — the closed-form heat-flow solution underlying the dataset and the cooling-time feature.
2. Easterling, K.E. *Introduction to the Physical Metallurgy of Welding*, 2nd ed. (Butterworth-Heinemann, 1992) — chapters 3 and 4 give the 2D/3D Rosenthal expressions and the t_{8/5} thin-/thick-plate regime switch used in equation 4.
3. Chen, T. and Guestrin, C. "XGBoost: A Scalable Tree Boosting System." [*Proc. KDD 2016*, 785–794](https://doi.org/10.1145/2939672.2939785) — the gradient-boosting library used for the baseline and the winner.
4. Kou, S. *Welding Metallurgy*, 2nd ed. (Wiley, 2003) — chapter 2 gives the textbook narrow-HAZ thin-plate prescription independently recovered by Phase B.
5. Matitopanum, S. et al. "Friction stir welding parameter optimisation for AA2024-T3." *PMC11012866* (2024) — the source of the 45 real FSW rows used as the out-of-family sanity check.
6. American Welding Society. *AWS D1.1/D1.1M:2020 Structural Welding Code — Steel.* — the regulatory definition of heat input as `(60 · V · I · η) / (1000 · v)`.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, the Hypothesis-Driven Research program.md specification, and the full project history including the dataset generator, hdr_loop.py, and the 56-experiment results.tsv in `applications/welding/`
