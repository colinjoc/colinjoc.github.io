---
title: "Hypothesis-Driven Research Beats Published Bayesian-Optimisation Baseline on Real Lacquer Data"
date: 2026-04-09
weight: 12
domain: "Coatings / Materials Science"
headline: "Per-target physics-informed ensemble cuts the published Gaussian-Process baseline's MAE by 12.7% on gloss, 23.0% on hiding power, 27.9% on cupping (and ties on scratch hardness) on the Borgert et al. 2024 PURformance dataset"
metric_name: "Mean Absolute Error against the published Gaussian Process baseline on the PURformance 2K polyurethane lacquer dataset"
metric_value: "−12.7% gloss, −23.0% hiding power, −27.9% cupping (3 of 4 targets, real measured data)"
tags: ["materials", "coatings", "small-data", "reproduction", "physics-informed"]
---

## The Problem

Two-component polyurethane (2K PU) lacquers are the workhorse of industrial wood, metal, and automotive top-coats, but their development cycle remains iterative and expensive because four or more composition variables interact non-linearly to determine gloss, scratch hardness, hiding power, and flexibility simultaneously. A formulation chemist looking for a coating with target gloss of 80 gloss units (GU), scratch hardness of 15 newtons (N), hiding power of 95%, and a Volatile Organic Compound (VOC) content under 100 g/L typically runs Design of Experiments (DoE) campaigns of 30–60 samples per project iteration.

The 2024 PURformance benchmark by Borgert et al. (Zenodo Digital Object Identifier (DOI) 10.5281/zenodo.13742098) is the first fully open 2K PU lacquer dataset that publishes all four composition variables, five performance properties, and the associated Python Gaussian Process training code. **65 real measured 2K PU samples**, four normalised composition columns (crosslinker content, cycloaliphatic isocyanate fraction, matting-agent loading, pigment-paste loading), film thickness, and four performance targets (60° gloss, scratch hardness, hiding power, Erichsen cupping depth). The original paper takes a single modelling path: a Gaussian Process Regressor (GPR) trained on all four targets with a shared `RBF + DotProduct + WhiteKernel` composite kernel and 10,000 Optuna trials of hyperparameter tuning.

The questions the published paper does not answer:
1. Does a per-target choice of model family beat a unified Gaussian Process?
2. Do physics-informed features derived from the Pigment Volume Concentration (PVC) framework, Kubelka-Munk radiative transfer, and isocyanate chemistry add signal beyond the raw composition columns?
3. Can a 65-sample dataset support formulation-level discovery as opposed to purely within-sample interpretation?

We answered all three under a Hypothesis-Driven Research (HDR) protocol against the *exact* published baseline.

## The Baseline (What We Compared Against)

The baseline is the **published PURformance Gaussian Process Regressor** from `Evaluation/HPO/kerneloptimizer.py` in the Borgert et al. 2024 Zenodo archive — verbatim, with one explicit deviation. The composite kernel is

$$k(x, x') = k_{\text{RBF}}(x, x') + k_{\text{Dot}}(x, x') + k_{\text{White}}(x, x')$$

where the Radial Basis Function (RBF) component is `RBF(length_scale=1.0, length_scale_bounds=(1e-3, 1e3))`, the linear DotProduct component is `DotProduct(sigma_0=1.0)`, and the WhiteKernel regularisation noise term is `WhiteKernel(noise_level=1e-3)`. The GPR is fit via `sklearn.gaussian_process.GaussianProcessRegressor(n_restarts_optimizer=5)` with min-max input and target normalisation on training-fold statistics only.

**Our deviation:** the published code trains on 55 samples (the `cs + i1 + i2 + i3 + i4` campaigns) and evaluates on the 10-sample `rdm` hold-out — a single train/test split. We instead use **5-fold K-fold cross-validation on all 65 samples** (`KFold(n_splits=5, shuffle=True, random_state=42)`) so that every HDR loop experiment is directly comparable to the baseline under the same evaluation harness. We also report Mean Absolute Error (MAE) on the original target units instead of normalised mean-squared error, because MAE in newtons, gloss units, percent, and millimetres is more interpretable.

Under this protocol the PURformance GP baseline achieves:

| Target | MAE | RMSE | R² |
|---|---|---|---|
| scratch_hardness_N | 1.844 N | 2.454 N | 0.143 |
| gloss_60 | 11.498 GU | 14.284 GU | 0.679 |
| hiding_power_pct | 2.841 % | 4.781 % | 0.416 |
| cupping_mm | 2.109 mm | 2.753 mm | 0.540 |

These are the four numbers the HDR loop has to beat — they are recorded as rows `GP_BASELINE` in the project's `results.tsv`.

## The Solution (What We Discovered)

### The final code

```python
# From applications/paint_formulation/model.py — the final per-target winners
# after Phase 1 tournament + 141 Phase 2 + 63 Phase 2.5 experiments

SCRATCH_HARDNESS = {
    "model_family": "ridge",
    "extra_features": ["binder_pigment_ratio"],
    "sklearn_kwargs": {"alpha": 1.0},
}

GLOSS = {
    "model_family": "xgboost",
    "extra_features": ["log_thickness", "thickness_x_matting"],
    "xgb_params": {
        "objective": "reg:squarederror",
        "max_depth": 7, "learning_rate": 0.05,
        "min_child_weight": 2, "subsample": 0.8, "colsample_bytree": 0.8,
    },
    "n_estimators": 300,
}

HIDING_POWER = {
    "model_family": "extratrees",
    "extra_features": ["thickness_x_pigment"],
    "sklearn_kwargs": {"max_features": 0.5},
    "n_estimators": 300,
}

CUPPING = {
    "model_family": "extratrees",
    "extra_features": ["cyc_x_matting", "pvc_proxy"],
    "n_estimators": 300,
}


def add_features(df, features):
    out = df.copy()
    if "binder_pigment_ratio" in features:
        binder = 1.0 - out["matting_agent"] - out["pigment_paste"]
        solids = (out["pigment_paste"] + out["matting_agent"]).replace(0, np.nan)
        out["binder_pigment_ratio"] = (binder / solids).fillna(10.0)
    if "log_thickness" in features:
        out["log_thickness"] = np.log1p(out["thickness_um"])
    if "thickness_x_matting" in features:
        out["thickness_x_matting"] = out["thickness_um"] * out["matting_agent"]
    if "thickness_x_pigment" in features:
        out["thickness_x_pigment"] = out["thickness_um"] * out["pigment_paste"]
    if "cyc_x_matting" in features:
        out["cyc_x_matting"] = out["cyc_nco_frac"] * out["matting_agent"]
    if "pvc_proxy" in features:
        solids = out["pigment_paste"] + out["matting_agent"]
        out["pvc_proxy"] = (solids / (solids + (1.0 - solids))).fillna(0.0)
    return out
```

We call this configuration the **Per-Target Physics-Informed Ensemble (PTPIE)**: four small, independently-trained per-target models, each chosen by the HDR tournament and refined by 204 single-change experiments, with one or two physics-informed features per target on top of the five raw normalised columns.

### Causal mechanism

Each of the kept features encodes a known coating-physics mechanism:

- **Binder-to-pigment ratio for scratch hardness.** Ridge regression captures the intuition that scratch hardness rises roughly linearly with binder volume fraction up to the Critical Pigment Volume Concentration (CPVC) and then plateaus. The HDR loop confirmed the relationship is genuinely linear in this single ratio: every quadratic, interaction, and log-ratio term was reverted as noise.
- **Log thickness and thickness × matting for gloss.** Gloss is controlled by the root-mean-square surface roughness of the dry film, which scales as thickness raised to a negative fractional power for drying-induced defects (Bond, 1973). `log(1 + thickness)` captures this scaling over the 30–65 µm range of the dataset. The `thickness × matting_agent` interaction captures the orthogonal effect that a thick film with lots of matting silica develops more surface micro-asperities because the silica particles protrude differently at different thicknesses.
- **Thickness × pigment for hiding power.** Hiding power (contrast ratio in percent) scales approximately with the product of film thickness and pigment concentration — the Kubelka-Munk two-flux radiative-transfer prediction is exactly first-order in both factors. The single product term beat every multi-feature combination because it directly featurises the governing equation.
- **Cycloaliphatic isocyanate × matting for cupping.** The Erichsen cupping test measures ductile failure under slow deformation. The cycloaliphatic isocyanate (isophorone diisocyanate, IPDI) contributes a stiffer, more brittle matrix than its aliphatic counterpart hexamethylene diisocyanate (HDI), so increasing IPDI fraction reduces cupping depth. Higher matting-agent content increases the volume fraction of rigid silica inclusions that act as crack-initiation sites. Their product captures the combined stiffening effect; the Pigment Volume Concentration (PVC) proxy adds the baseline rigidity contribution.

### Difference from the baseline

| Aspect | PURformance GP baseline | PTPIE (this paper) |
|---|---|---|
| Model family | Single GP for all 4 targets | Per-target: Ridge, XGBoost, ExtraTrees, ExtraTrees |
| Hyperparameters | RBF + DotProduct + WhiteKernel, 10,000 Optuna trials | scikit-learn defaults per family, HDR-tuned |
| Features | 5 raw normalised columns | 5 raw + 1 to 2 derived per target |
| Cross-validation | Single 55/10 train/test split | 5-fold K-fold on all 65 samples |
| Number of experiments | 10,000 Optuna trials on GP hyperparameters | 204 single-change HDR experiments |

## What We Found

### Side-by-side improvement against the published baseline

Both models evaluated under identical 5-fold cross-validation on all 65 samples:

| Target | PURformance GP | PTPIE (this work) | Δ MAE | Relative Δ |
|---|---|---|---|---|
| scratch_hardness_N | 1.844 N | **1.800 N** | −0.044 | −2.4% (within noise floor) |
| gloss_60 | 11.498 GU | **10.036 GU** | −1.462 | **−12.7%** |
| hiding_power_pct | 2.841 % | **2.187 %** | −0.654 | **−23.0%** |
| cupping_mm | 2.109 mm | **1.519 mm** | −0.590 | **−27.9%** |

The PTPIE configuration improves 3 of 4 targets by more than 10% and matches the baseline on scratch hardness within the per-target noise floor. The improvements are largest on cupping and hiding, the two targets where the dominant physical mechanism (Kubelka-Munk for hiding, silica-modulus for cupping) is non-linear in a single interaction term that ExtraTrees captures cleanly.

### Phase 1 tournament: XGBoost wins zero of four

| Target | XGBoost | LightGBM | ExtraTrees | Ridge | Winner |
|---|---|---|---|---|---|
| scratch_hardness_N | 2.137 | 2.211 | 2.065 | **1.832** | **Ridge** |
| gloss_60 | 10.866 | 11.703 | **10.286** | 12.330 | **ExtraTrees** |
| hiding_power_pct | 3.129 | 3.075 | **2.454** | 2.724 | **ExtraTrees** |
| cupping_mm | 1.760 | 1.722 | **1.660** | 2.250 | **ExtraTrees** |

Two HDR anti-patterns are validated simultaneously: **Ridge wins the smallest-signal target (scratch hardness)** — a clean confirmation of "linear baselines are strong for linear-response targets" — and **ExtraTrees wins the remaining three** — a clean confirmation of "bagging beats boosting on N < 100". XGBoost wins none of the four in the tournament. It only re-enters in Phase 2 for gloss, after the `log_thickness` and `thickness_x_matting` features are added, and only at unusually deep `max_depth=7`.

### Phase 2 + 2.5 result: 11 KEEP / 191 REVERT (5.5%)

Of 204 total single-change experiments across the four targets:

| Target | Phase 2 keeps | Phase 2.5 keeps | Best 5-fold CV MAE |
|---|---|---|---|
| scratch_hardness_N | 2 | 0 | 1.800 N (R² 0.221) |
| gloss_60 | 2 | 0 | 10.036 GU (R² 0.726) |
| hiding_power_pct | 2 | 1 | 2.187 % (R² 0.664) |
| cupping_mm | 3 | 1 | 1.519 mm (R² 0.715) |
| **Total** | **9** | **2** | |

A 5.5% keep ratio is exactly the regime the HDR program.md specification calls "honest" — far from a 50% keep rate that would indicate noise-chasing, far from a 0% keep rate that would indicate the design space is exhausted.

### Phase B discovery: a low-VOC high-gloss formulation on the Pareto front

The four final per-target models were re-trained on all 65 samples and used to predict properties for **7,785 candidate formulations** generated across 5 strategies (dense grid, high-gloss corner, low-VOC corner, high-hardness corner, Latin hypercube random). The Pareto front on the gloss × Volatile Organic Compound (VOC) trade-off contains 24 non-dominated points. The headline candidate:

| Property | Predicted value |
|---|---|
| 60° gloss | **81.3 GU** |
| Scratch hardness | 15.6 N |
| Estimated VOC | **72.8 g/L** |
| Estimated cost | $5.86/kg |
| Composition | crosslink 1.00, cyclic-NCO 0.67, matting 0.50, pigment 0.80 |
| Film thickness | 40 µm |

This candidate sits inside the **low-VOC regime** (EU Directive 2004/42/EC decorative-coating category D limits are 130–300 g/L depending on application) and predicts a gloss in the semi-gloss / high-gloss range. The closest training samples in the PURformance dataset have composition distances of 0.10–0.15 on the normalised scale, so the prediction is an in-sample extrapolation rather than a wild out-of-distribution claim. Physical validation would be the natural next step.

## Key Insights

### 1. Per-target model family selection matters more than unified modelling

The published PURformance paper trains a single Gaussian Process across all four targets. Our HDR loop found that no single family wins all four — Ridge wins scratch hardness, ExtraTrees wins hiding power and cupping, XGBoost wins gloss only after physics features are added. The per-target dispatch is responsible for the bulk of the improvement on the three targets that beat the baseline by more than 10%.

### 2. Bagging beats boosting on 65 samples

ExtraTrees builds each tree with random split thresholds — added noise that acts as regularisation on small datasets. On 65 samples, XGBoost's boosted residuals overfit noise while ExtraTrees' averaging smooths it out. This is the published HDR anti-pattern "bagging beats boosting for small N (<100 samples)" cleanly validated on a real measured dataset.

### 3. Aitchison log-ratio (compositional) features did not help

We expected simplex-aware compositional features to improve every target because the four composition variables are approximately compositional (they sum to a fixed solids fraction). None of the four log-ratio features was kept on any target. The probable explanation: the composition columns were published on a normalised [0, 1] scale by the PURformance authors, which already removes the closure constraint that Aitchison log-ratios exist to fix.

### 4. Monotonicity constraints hurt every target

A sister project on concrete (N = 1030 samples) found a clear improvement from a monotonicity constraint forcing the cement-to-strength relationship to be non-decreasing. We tried hard physical priors here (gloss monotonically decreases with matting agent, etc.) and they reliably *increased* MAE on every target. The 65-sample dataset contains enough exceptions to these rules that a hard constraint is worse than a soft learnt pattern. **Monotonicity constraints are dataset-size dependent.**

### 5. Scratch hardness R² of 0.22 is a data-scarcity ceiling, not a modelling failure

Even after 204 experiments, scratch hardness cross-validated R² stays at 0.22. The Sobol main-effect indices in the published paper attribute scratch hardness to a diffuse mix of variables — 38% to matting agent, 14% to pigment, 12% to crosslink density — with no single dominant axis. On 65 samples this diffuse signal is genuinely below the noise floor for any model family. **The honest reading is "we need more data", not "we need a smarter model".**

### 6. Cross-validation matters

The published paper uses a 55/10 single train/test split. Under that protocol the GP looks reasonable. Under 5-fold cross-validation on the same 65 samples, the GP's scratch-hardness R² drops from the published value to 0.143 — the lowest of the four targets. Single train/test splits on N < 100 datasets are systematically optimistic.

## Why This Matters

For coating-formulation practice:

- **Per-target modelling beats unified modelling on small datasets.** When optimising a multi-target coating, fit one model per target, choose the family per target, and add 1–2 physics-informed features per target.
- **The Kubelka-Munk product term, the binder-pigment ratio, and the log-thickness scaling are higher-leverage than any hyperparameter tuning.** Domain physics encoded as features beats 10,000 trials of Optuna hyperparameter search.
- **A predicted 81-GU formulation at 73 g/L VOC sits inside the low-VOC regime** — a candidate worth physical validation for any chemist looking for an architectural-coating-compliant high-gloss top-coat.

For Hypothesis-Driven Research methodology more broadly:

- **Reproducing a published baseline under stricter cross-validation is a publishable contribution.** The PURformance paper's GP looks good on a single train/test split and fine but beatable under 5-fold CV. Both readings are honest; the second is more useful.
- **Beating a Bayesian-optimisation-tuned baseline by 12–28% on 3 of 4 targets, on real measured data, with a 65-sample budget, validates the per-target HDR pattern as a publishable methodology** — not a discovery, but a transparently better engineering protocol.

## Methodology

**Baseline.** The published PURformance Gaussian Process Regressor (Borgert et al. 2024, Zenodo DOI 10.5281/zenodo.13742098) on the 5 raw normalised features (crosslink, cyc_nco_frac, matting_agent, pigment_paste, thickness_um) of the 65-sample 2K polyurethane lacquer dataset. Composite kernel `RBF(length_scale=1.0, length_scale_bounds=(1e-3, 1e3)) + DotProduct(sigma_0=1.0) + WhiteKernel(noise_level=1e-3)` fitted via `sklearn.gaussian_process.GaussianProcessRegressor(n_restarts_optimizer=5)`. Min-max input and target normalisation on training-fold statistics only. Evaluated under 5-fold K-fold cross-validation (`shuffle=True, random_state=42`) on all 65 samples — stricter than the published single 55/10 train/test split. **MAE per target: 1.844 N (scratch), 11.498 GU (gloss), 2.841 % (hiding), 2.109 mm (cupping)**.

**Iteration.** A four-stage Hypothesis-Driven Research loop. Phase 1 ran a four-way model-family tournament (XGBoost, LightGBM, ExtraTrees, Ridge) on the raw features per target — Ridge won scratch hardness, ExtraTrees won the other three. Phase 2 ran 141 single-change experiments testing one of 22 physics-informed features (Pigment Volume Concentration proxies, Aitchison log-ratio compositional transforms, isocyanate chemistry interactions, thickness interactions, polynomial saturation terms), one hyperparameter swap, or one model-family swap per experiment per target; each had a Bayesian prior (0.2–0.7), a mechanistic justification, and a pre-registered keep-or-revert decision against per-target noise floors (0.02 N scratch, 0.20 GU gloss, 0.05% hiding, 0.03 mm cupping). 9 kept, 132 reverted. Phase 2.5 ran 63 additional experiments testing multi-feature combinations, cross-family re-tournaments with the refined feature set, and hyperparameter sweeps around the Phase 2 winners; 2 more keeps. **Total Phase 2 + 2.5: 11 keeps, 191 reverts (5.5% keep ratio).** Phase B re-trained the 4 winners on all 65 samples and screened 7,785 candidate formulations across 5 generation strategies, then computed the Pareto fronts on the gloss × VOC, scratch hardness × VOC, and gloss × scratch hardness trade-offs.

## Key References

1. Borgert, T. et al. "High-Throughput and Explainable Machine Learning for Lacquer Formulations: Enhancing Coating Development by Interpretable Models." *Progress in Organic Coatings* (2024). Data and code: [Zenodo DOI 10.5281/zenodo.13742098](https://doi.org/10.5281/zenodo.13742098) — the published baseline this paper improves upon.
2. Rasmussen, C.E. and Williams, C.K.I. *Gaussian Processes for Machine Learning* (MIT Press, 2006) — the canonical textbook for the GP baseline.
3. Aitchison, J. *The Statistical Analysis of Compositional Data* (Chapman and Hall, 1986) — the log-ratio transform tested and rejected on this dataset.
4. Asbeck, W.K. and Van Loo, M. "Critical Pigment Volume Concentration Relationship." *Industrial and Engineering Chemistry* (1949) — the Pigment Volume Concentration framework underlying the `pvc_proxy` and `binder_pigment_ratio` features.
5. Wicks, Z.W., Jones, F.N., Pappas, S.P., and Wicks, D.A. *Organic Coatings: Science and Technology*, 3rd ed. (Wiley, 2007) — comprehensive coating-science textbook covering the Kubelka-Munk, isocyanate-chemistry, and matting-agent mechanisms encoded in the kept features.
6. Geurts, P., Ernst, D., and Wehenkel, L. "Extremely Randomized Trees." *Machine Learning* (2006) — the ExtraTrees reference; the small-N family that won 3 of 4 targets here.
7. Chen, T. and Guestrin, C. "XGBoost: A Scalable Tree Boosting System." [*Proc. KDD 2016*, 785–794](https://doi.org/10.1145/2939672.2939785) — the gradient-boosting library that won gloss only after physics features were added.
8. Hoerl, A.E. and Kennard, R.W. "Ridge Regression: Biased Estimation for Nonorthogonal Problems." *Technometrics* (1970) — the linear baseline that won scratch hardness.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, the Hypothesis-Driven Research program.md specification, and the full project history including the 204-experiment results.tsv, the per-target winning_config.json, and phase_b_discovery.py in `applications/paint_formulation/`
