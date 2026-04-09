---
title: "Reproducing High-Volume Slag-Cement Concrete With a Transparent HDR Loop"
date: 2026-04-09
domain: "Materials Engineering"
headline: "120 kg cement plus 200 kg slag plus 100 kg fly ash → 58.8 MPa at 53% lower carbon dioxide than conventional concrete — a known result, reproduced honestly"
metric_name: "Carbon dioxide reduction at equivalent compressive strength"
metric_value: "−53% (157 vs 335 kg CO₂/m³, in-distribution)"
tags: ["materials", "sustainability", "concrete", "reproduction", "multi-objective"]
---

## The Problem

Concrete is the most consumed material on Earth — about 30 billion tons per year — and cement production accounts for 8% of global carbon dioxide (CO₂) emissions. Reducing the cement content of structural concrete is one of the highest-leverage decarbonisation strategies available.

The classic approach is supplementary cementitious materials (SCMs): partially replace cement with blast-furnace slag (a steel-industry byproduct) or coal fly ash (a coal-combustion byproduct). Both have much lower embodied CO₂ per kilogram than cement (slag ≈ 0.07 kg CO₂/kg, fly ash ≈ 0.01, vs cement at 0.90). The trade-off is strength: SCMs hydrate more slowly than cement, so SCM-rich mixes typically need longer curing or accept lower 28-day strength.

This is a well-studied area. The category "High-Volume Fly Ash Concrete" (HVFAC) has been formalised since the 1990s. We did NOT discover that ultra-low-cement structural concrete is viable — we reproduced a known result transparently, with explicit honesty about the limits of our predictor's training data.

## The Baseline (What We Compared Against)

The comparison target is **conventional C40 structural concrete**, the standard mix used in most structural engineering globally. C40 is the European structural-concrete grade defined by 40 megapascals (MPa) cylinder strength / 50 MPa cube strength at 28 days. A typical C40 mix:

| Component | Mass (kg per cubic metre) |
|---|---|
| Portland cement | 350 |
| Blast-furnace slag | 0 |
| Fly ash | 0 |
| Water | 160 |
| Superplasticizer | 8 |
| Coarse aggregate (gravel) | 950 |
| Fine aggregate (sand) | 700 |
| Curing age | 28 days |

Embodied CO₂ is computed as the sum over components of (mass × emission factor):

$$\mathrm{CO_2}(C40) = 350 \cdot 0.90 + 160 \cdot 0.001 + 8 \cdot 1.50 + 950 \cdot 0.005 + 700 \cdot 0.005 = 335 \text{ kg/m}^3$$

Cement alone contributes 315 of those 335 kilograms — 94% of the conventional mix's embodied carbon comes from cement. Cost: about $99 per cubic metre, with cement being about half ($52.50). Strength: about 50 MPa at 28 days.

We also compared the strength predictor against a baseline: XGBoost on the eight raw mix-component columns of the [UCI Concrete Compressive Strength dataset](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) (Yeh 1998, 1030 samples), with default hyperparameters. 5-fold cross-validation Mean Absolute Error (MAE): **2.78 MPa**, R² = 0.934. Each subsequent experiment was compared against this number.

## The Solution (What the HDR Loop Found)

### The strength predictor

```python
import numpy as np
import xgboost as xgb

RAW_FEATURES = ["cement", "slag", "fly_ash", "water", "superplasticizer",
                "coarse_agg", "fine_agg", "age"]
DERIVED_FEATURES = ["wb_ratio", "scm_pct"]
FEATURE_NAMES = RAW_FEATURES + DERIVED_FEATURES


def add_features(df):
    out = df.copy()
    binder = out["cement"] + out["slag"] + out["fly_ash"]
    out["wb_ratio"] = (out["water"] / binder.replace(0, np.nan)).fillna(0)
    out["scm_pct"] = ((out["slag"] + out["fly_ash"]) / binder.replace(0, np.nan)).fillna(0)
    return out


def train_winning_model(df):
    df = add_features(df)
    X = df[FEATURE_NAMES].values.astype(np.float32)
    y = df["strength"].values.astype(np.float32)
    monotone = [0] * len(FEATURE_NAMES)
    monotone[FEATURE_NAMES.index("cement")] = 1
    params = {
        "objective": "reg:squarederror",
        "max_depth": 6, "learning_rate": 0.05, "min_child_weight": 3,
        "subsample": 0.8, "colsample_bytree": 0.8,
        "monotone_constraints": "(" + ",".join(str(v) for v in monotone) + ")",
        "verbosity": 0,
    }
    return xgb.train(params, xgb.DMatrix(X, label=y), num_boost_round=600)
```

10 features (8 raw + 2 derived), one monotonicity constraint forcing the partial dependence of strength on cement to be non-decreasing, 600 boosting rounds. **5-fold cross-validation MAE: 2.55 MPa, R² = 0.944.**

### How it differs from the baseline

| Aspect | Baseline | Final winner |
|---|---|---|
| Features | 8 raw columns | 8 raw + water-to-binder ratio + supplementary-cementitious-material percentage |
| Monotonicity constraint | none | cement → strength must be non-decreasing |
| Boosting rounds | 300 | 600 |
| 5-fold cross-validation MAE | 2.78 MPa | **2.55 MPa** |

### The discovered mix

After training on the full dataset, we screened 3,685 candidate mix designs across 11 generation strategies. The in-distribution (cement ≥ 102 kg per cubic metre, the UCI training minimum) Pareto-front winner:

| Component | Conventional C40 | **Discovery winner** | Difference |
|---|---|---|---|
| Cement | 350 kg/m³ | **120 kg/m³** | **−66%** |
| Blast-furnace slag | 0 | **200 kg/m³** | + |
| Fly ash | 0 | **100 kg/m³** | + |
| Water | 160 kg/m³ | 160 kg/m³ | 0 |
| Superplasticizer | 8 kg/m³ | 12 kg/m³ | +4 |
| Coarse aggregate | 950 kg/m³ | 950 kg/m³ | 0 |
| Fine aggregate | 700 kg/m³ | 700 kg/m³ | 0 |
| Curing age | 28 days | **90 days** | +62 |
| **Predicted strength** | **50 MPa** | **58.8 MPa** | **+18%** |
| **Embodied CO₂** | **335 kg/m³** | **156.9 kg/m³** | **−53%** |
| Cost | $99/m³ | $95/m³ | −4% |

A 56-day-curing variant (120 cement / 200 slag / 150 fly ash) reaches 53.2 MPa at 146.9 kg CO₂/m³ — a **56% reduction** at the same structural strength target, if 56-day curing is acceptable to the structural code.

## What We Found

**This recipe is not novel.** It sits within the well-established High-Volume Fly Ash Concrete category, formalised by Bilodeau and Malhotra in the 1990s. A 2025 *Buildings* paper on quaternary-blended-cement Pareto optimisation reports an essentially identical result (51–80 MPa at approximately 62% less cement than conventional). A 2024 *Journal of Cleaner Production* life-cycle assessment reports a 54% CO₂ reduction with 65% fly ash. The 90-day curing trick is documented in standard concrete textbooks (Mehta and Monteiro 2014, Neville 2011) and codified in [Federal Highway Administration Tech Brief HIF-16-001](https://www.fhwa.dot.gov/) (2016).

What this paper actually adds:

1. **Transparent Hypothesis-Driven Research methodology**. Every experiment has a stated Bayesian prior, an articulated mechanism, and a pre-registered keep-or-revert decision recorded in `results.tsv`. Most published concrete-machine-learning papers report only the winning configuration, not the full 24-experiment loop.
2. **In-distribution honesty**. We explicitly filter the Phase B sweep to candidates within the UCI training range (cement ≥ 102 kg per cubic metre) and reject the 75% CO₂ reduction claim that earlier artifact-derived narratives reported as an extrapolation. Most published papers in this area report mathematical optima without checking training-data coverage.
3. **A fully reproducible code-and-data package**. `pip install`, run two scripts, get the exact paper numbers in approximately two minutes on a laptop.
4. **A modest technical refinement**: a 10-feature predictor with one monotonicity constraint and 600 boosting rounds, MAE 2.55 MPa. Not state of the art (Tipu et al. 2026 report R² = 0.997 vs our 0.944), but sufficient for the Pareto sweep.

## Key Insights

### 1. The standard XGBoost defaults are mostly already right

Of 20 hypothesis-driven Phase 2 experiments, 16 were reverted. Of the 4 kept, 2 were derived features (water-to-binder ratio, supplementary-cementitious-material percentage), 1 was a monotonicity constraint, and 1 was simply increasing the boosting-round count from 300 to 600. Hyperparameter tuning (learning rate, max depth, min child weight, subsample) was tested across 7 experiments and none of them improved the result by more than the noise floor.

### 2. The textbook log(age) feature was rejected

Abrams' law treats concrete strength as a function of log(age), so adding `log(age)` as an explicit feature was an obvious thing to try. Prior was 70%. Result: it hurt the model by 0.06 MPa. XGBoost can already handle the age-vs-strength relationship non-linearly without an explicit log transform, and adding a redundant feature increased variance more than it reduced bias on the small N=1030 dataset.

### 3. The monotonicity constraint on cement is the most important physical prior

XGBoost's flexibility lets it learn relationships that are physically wrong on small datasets. The model can infer that "in some local region of feature space, increasing cement decreases strength" — which is impossible at fixed water and SCM. Adding the constraint that cement must non-decreasingly affect strength improves cross-validation MAE by 0.034 MPa AND substantially improves the model's behaviour on extrapolated mixes.

A second monotone constraint on water (forcing strength to be non-increasing in water) was tested and **reverted**, because water interacts with the water-to-binder ratio feature and forcing one of them monotonic violates the joint relationship.

### 4. The 75% reduction claim from prior artifact-derived narratives is an extrapolation

A previous version of this project (lost in a destructive operation earlier in the day, then restarted from scratch) reported a 75% CO₂ reduction at 50 MPa using an 80 kg/m³ cement mix. The current rerun finds that 80 kg cement is below the UCI training range (which starts at 102 kg/m³) and is therefore an extrapolation. The verified in-distribution result is 53–56% reduction, not 75%. We report the verified number.

### 5. Cost is not a barrier — only structural-code curing requirements are

The discovered mix is approximately the same cost as conventional C40 ($95 vs $99 per cubic metre). Cement is no longer the dominant cost component once you have it (only 53% of the total in conventional C40), so reducing cement does not save money proportionally. The real practical barrier is whether structural codes accept 56-day or 90-day strength specifications. Many codes do; some do not.

## Why This Matters

If you are a structural engineer designing a building today:

- **The 53–56% CO₂ reduction is achievable with standard materials and standard methods** — no exotic chemistry, no novel admixtures, no proprietary process. Just slag plus fly ash plus extended curing.
- **The main barrier is regulatory, not technical**. If your local building code accepts 56-day strength specifications (many European and increasingly US codes do), the recipe is immediately deployable.
- **The recipe is not new, but the transparency is useful**: this paper releases the full code, the dataset reference, the candidate generator, and the keep-or-revert log so any engineer can reproduce, extend, or refute the result.

## Methodology

**Baseline.** Conventional C40 structural concrete: 350 kg cement, no SCM, 160 kg water, 28-day curing. Embodied CO₂ 335 kg/m³ via standard industry life-cycle-assessment factors (cement 0.90, slag 0.07, fly ash 0.01, water 0.001, superplasticizer 1.50, aggregates 0.005 — all in kg CO₂ per kg of ingredient). Cost $99/m³ at typical 2024 US industrial prices. Predicted strength about 50 MPa. The strength predictor baseline is XGBoost on the eight raw UCI columns with default hyperparameters: 5-fold cross-validation MAE 2.78 MPa, R² 0.934.

**Iteration.** A three-stage Hypothesis-Driven Research loop. Phase 1 was a tournament between three model families (XGBoost, LightGBM, ExtraTrees) plus a Ridge linear baseline; XGBoost won. Phase 2 was 20 single-change experiments testing feature additions, hyperparameter modifications, target transforms, and monotonicity constraints; each had a Bayesian prior and a pre-registered keep-or-revert decision (keep if cross-validation MAE improved by at least 0.005). 4 kept, 16 reverted. Phase 2.5 was an 8-experiment compositional re-test that combined the kept changes; 2 of those kept improvements led to the final P25.5 winning configuration at MAE 2.55 MPa. Phase B trained the winning model on the full dataset and screened 3,685 candidate mix designs across 11 generation strategies (dense grids at 28-, 56-, and 90-day curing, ternary blends, ultra-low-cement variants, Latin hypercube sampling, etc.), then computed the Pareto front for the strength-vs-CO₂ pair.

**In-distribution constraint.** The UCI dataset covers cement contents from 102 to 540 kg per cubic metre. Predictions outside this range are extrapolations and are NOT used in this summary's headline numbers.

## Key References

1. Yeh, I-C. "Modeling of strength of high-performance concrete using artificial neural networks." [*Cement and Concrete Research* **28**(12), 1797–1808 (1998)](https://doi.org/10.1016/S0008-8846(98)00165-3) — the source of the UCI dataset.
2. Bilodeau, A. and Malhotra, V.M. "High-volume fly ash system: concrete solution for sustainable development." *ACI Materials Journal* **97**(1), 41–48 (2000) — the foundational High-Volume Fly Ash Concrete paper.
3. MDPI Buildings (2025). "Cost-Performance Multi-Objective Optimization of Quaternary-Blended Cement Concrete." *Buildings* **15**(22), 4074 — reports an essentially identical Pareto result (51–80 MPa with about 62% less cement) by an independent method, a year before this paper was written.
4. Tipu, R.K. et al. "GreenMix-Pareto: Uncertainty-aware, physics-guided multi-objective optimization of low-carbon concrete mix designs." *Ain Shams Engineering Journal* (2026) — physics-guided multi-task model with R² = 0.997 (more accurate than ours) and a published Pareto knee at 50 MPa / 220 kg CO₂.
5. Federal Highway Administration. ["Tech Brief: Supplementary Cementitious Materials"](https://www.fhwa.dot.gov/), FHWA-HIF-16-001 (2016) — the regulatory framework permitting fly ash 18–50% and slag 50–70% replacement.
6. Chen, T. and Guestrin, C. "XGBoost: A Scalable Tree Boosting System." [*Proc. KDD 2016*, 785–794](https://doi.org/10.1145/2939672.2939785).

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the Hypothesis-Driven Research framework, the program.md specification, and the full project history including the kat parser, analysis scripts, and the 24-experiment results.tsv in `applications/concrete/`
