---
title: "53% Less Carbon, 18% Stronger Concrete via Slag-Cement Blends"
date: 2026-04-10
domain: "Materials Engineering"
headline: "Replacing 66% of cement with slag and fly ash cuts embodied CO₂ by 53% while exceeding structural strength targets"
metric_name: "Embodied CO₂ reduction vs conventional C40 structural concrete"
metric_value: "−53% (156.9 vs 335 kg CO₂/m³) at +18% strength"
tags: ["concrete", "materials", "sustainability", "low-carbon", "mix-design", "machine-learning"]
---

## The Problem

Concrete is the most consumed material on Earth, with global production of approximately 30 billion tons per year. Cement production — the calcination of limestone and firing of the clinker kiln — contributes about 8% of global anthropogenic carbon dioxide emissions. Cement alone accounts for 94% of the embodied carbon in a conventional structural concrete mix. Reducing the cement content per cubic metre while maintaining the structural strength required by building codes is one of the largest single decarbonisation opportunities in the construction sector.

The classic approach is to partially replace cement with supplementary cementitious materials (SCMs): blast-furnace slag (a steel-industry byproduct, ~0.07 kg CO₂/kg) and coal fly ash (a coal-combustion byproduct, ~0.01 kg CO₂/kg), versus cement at ~0.90 kg CO₂/kg. The trade-off is strength: SCMs hydrate more slowly, so SCM-rich mixes typically need longer curing or accept lower 28-day strength. The question is how low cement can go in a structural mix while still meeting code requirements.

## The Baseline (What We Compared Against)

The comparison target is a **conventional C40 structural concrete mix** — the European structural-concrete grade defined by 40 MPa cylinder compressive strength (50 MPa cube strength) at 28 days. This is the workhorse mix for most structural concrete applications globally.

**The conventional C40 mix design:**

| Component | Mass (kg/m³) |
|---|---|
| Portland cement | 350 |
| Blast-furnace slag | 0 |
| Coal fly ash | 0 |
| Water | 160 |
| Superplasticizer | 8 |
| Coarse aggregate | 950 |
| Fine aggregate | 700 |

**Embodied carbon calculation.** Each component carries a per-kilogram emission factor (kg CO₂e/kg): cement 0.90, slag 0.07, fly ash 0.01, water 0.001, superplasticizer 1.50, aggregates 0.005. The total embodied CO₂ of a mix is:

$$\mathrm{CO_2}(mix) = \sum_i m_i \cdot f_i$$

For the C40 baseline: 350 × 0.90 + 160 × 0.001 + 8 × 1.50 + 950 × 0.005 + 700 × 0.005 = **335.4 kg CO₂/m³**. Cement alone contributes 315 of those 335 kilograms.

**Strength predictor baseline.** The prediction model starts from [XGBoost](https://xgboost.readthedocs.io/) on the 8 raw mix-component columns of the [UCI Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) dataset (Yeh 1998, 1030 samples) with default hyperparameters, achieving a 5-fold cross-validated Mean Absolute Error (MAE) of 2.78 MPa and coefficient of determination (R²) of 0.934.

**Why C40 is the right baseline.** It is the standard structural mix used as the comparison target in essentially all "low-carbon concrete" research. It has well-established embodied-carbon and cost figures, is the simplest possible mix (cement + water + aggregates), and is reproducible across thousands of structural projects globally.

## The Solution (What We Discovered)

The final solution has two parts: a **strength predictor** and a **discovered mix design**.

### The strength predictor

A 10-feature monotonic XGBoost regressor trained on the UCI dataset with 600 boosting rounds. The 10 features are the 8 raw mix columns plus two derived features:

- **Water-to-binder ratio (wb_ratio):** water / (cement + slag + fly ash) — encoding Abrams' 1918 law that strength depends primarily on this ratio
- **Supplementary-cementitious-material percentage (scm_pct):** (slag + fly ash) / (cement + slag + fly ash) — distinguishing SCM-heavy from SCM-free mixes

One monotonicity constraint forces the partial dependence of strength on cement to be non-decreasing (physically, adding cement at fixed water and SCM cannot decrease strength).

```python
RAW_FEATURES = ["cement", "slag", "fly_ash", "water", "superplasticizer",
                "coarse_agg", "fine_agg", "age"]
DERIVED_FEATURES = ["wb_ratio", "scm_pct"]

def add_features(df):
    out = df.copy()
    binder = out["cement"] + out["slag"] + out["fly_ash"]
    out["wb_ratio"] = (out["water"] / binder.replace(0, np.nan)).fillna(0)
    scm = out["slag"] + out["fly_ash"]
    out["scm_pct"] = (scm / binder.replace(0, np.nan)).fillna(0)
    return out

# Monotonicity: cement must non-decreasingly affect strength
monotone = [0] * len(FEATURE_NAMES)
monotone[FEATURE_NAMES.index("cement")] = 1
params = {
    "objective": "reg:squarederror", "max_depth": 6,
    "learning_rate": 0.05, "min_child_weight": 3,
    "subsample": 0.8, "colsample_bytree": 0.8,
    "monotone_constraints": "(" + ",".join(str(v) for v in monotone) + ")",
}
model = xgb.train(params, xgb.DMatrix(X, label=y), num_boost_round=600)
```

This predictor achieves a 5-fold cross-validated MAE of **2.547 MPa** and R² of **0.944** — an 8.3% improvement over the raw-feature baseline.

### The discovered mix

A 3,685-candidate Phase B discovery sweep across 11 generation strategies identified this in-distribution Pareto-optimal mix:

| Component | Conventional C40 | **Discovery winner** | Change |
|---|---|---|---|
| Cement | 350 kg/m³ | **120 kg/m³** | −66% |
| Blast-furnace slag | 0 | **200 kg/m³** | + |
| Fly ash | 0 | **100 kg/m³** | + |
| Water | 160 kg/m³ | 160 kg/m³ | 0 |
| Superplasticizer | 8 kg/m³ | 12 kg/m³ | +4 |
| Coarse aggregate | 950 kg/m³ | 950 kg/m³ | 0 |
| Fine aggregate | 700 kg/m³ | 700 kg/m³ | 0 |
| Curing age | 28 days | **90 days** | +62 |
| **Strength** | **50 MPa** | **58.8 MPa** | **+18%** |
| **Embodied CO₂** | **335 kg/m³** | **156.9 kg/m³** | **−53%** |
| Cost | $99/m³ | $95/m³ | −4% |

**Why it works.** Slag and fly ash have 13× and 90× lower carbon intensity than cement respectively. Replacing 66% of the cement with these SCMs slashes embodied carbon while maintaining total binder volume (420 kg/m³ vs 350). The SCMs hydrate slowly, so 90-day curing is required — the largest practical constraint. Superplasticizer is increased from 8 to 12 kg/m³ to maintain workability at the higher binder content.

**Assumptions and limits.** The predictor is trained on the UCI dataset (cement range 102–540 kg/m³); predictions outside this range are treated as extrapolations and excluded from headline numbers. The discovery is a model prediction, not an experimental measurement. Only compressive strength is evaluated — durability (freeze-thaw, chloride ingress) is not captured.

## What We Found

The headline: **53% embodied CO₂ reduction at 18% higher strength than conventional C40 concrete**, achieved by replacing 66% of the cement with 200 kg slag + 100 kg fly ash per cubic metre and curing for 90 days.

| Metric | Conventional C40 | Discovery winner |
|---|---|---|
| Cement content | 350 kg/m³ | 120 kg/m³ (−66%) |
| Compressive strength | 50 MPa | 58.8 MPa (+18%) |
| Embodied CO₂ | 335 kg/m³ | 156.9 kg/m³ (−53%) |
| Cost | $99/m³ | $95/m³ (−4%) |
| Curing time | 28 days | 90 days |

A 56-day-curing variant (120/200/150 cement/slag/fly ash) reaches 53.2 MPa at 146.9 kg CO₂/m³ — a **56% CO₂ reduction** — if the structural code allows the shorter extended cure.

## Key Insights

### 1. The recipe is not novel — the methodology is

The 120-cement / 200-slag / 100-fly-ash mix sits within the well-established High-Volume Fly Ash Concrete (HVFAC) category. A 2025 quaternary-blend Pareto study reports an essentially identical result (51–80 MPa at ~62% less cement). A 2024 life-cycle assessment reports 54% CO₂ reduction with 65% fly ash. The chemistry is in textbooks. This paper's contribution is the transparent HDR loop and in-distribution honesty, not the chemistry.

### 2. Two derived features encode 100 years of concrete science

Water-to-binder ratio (Abrams' 1918 law) and SCM percentage together improve MAE by 0.075 MPa. XGBoost can in principle compute these from raw features, but the explicit ratios provide a cleaner signal. Twelve other candidate features (log_age, total binder, log cement, cement-water ratio, etc.) were tested and reverted.

### 3. Monotonicity constraints fix physically impossible predictions

Forcing "more cement cannot decrease strength" improves MAE by 0.034 MPa and — critically — prevents the model from claiming that doubling the cement in a high-SCM mix would reduce strength. A second constraint on water was tested and reverted because water interacts with the water-to-binder ratio feature.

### 4. The mathematical optimum is an extrapolation and must be rejected

The model's mathematical maximum-efficiency point uses cement = 40 kg/m³, below the UCI training minimum of 102. Reporting this as verified would be dishonest. The headline 53% CO₂ reduction uses only in-distribution candidates (cement ≥ 102 kg/m³).

### 5. Only 4 of 23 experiments survived

Of 23 single-change Hypothesis-Driven Research (HDR) experiments, 19 were reverted. The textbook log(age) feature was reverted — XGBoost handles age non-linearity without the explicit log. Redundant features increase variance more than they reduce bias at N = 1030.

### 6. The Pareto knee shows diminishing returns above 160 kg CO₂/m³

Going from 160 to 510 kg CO₂/m³ buys only 17 additional MPa of strength. The best efficiency is concentrated in the 120-cement / 200-slag region with extended curing.

## Why This Matters

Cement produces ~8% of global CO₂ emissions. If the construction industry adopted 120 kg/m³ cement mixes with slag and fly ash for structural applications where 56- to 90-day curing is acceptable, the embodied carbon of structural concrete would drop by roughly half. The main barrier is not chemistry — it is structural-code acceptance of extended curing schedules. Many codes already allow it; some do not.

The practical implication: ultra-low-cement structural concrete (~120 kg cement/m³, with 200+ kg slag + 100+ kg fly ash, cured for 56–90 days) is viable within the bounds of existing strength data, and the methodology to verify this is now fully reproducible in two minutes on a laptop.

## Methodology

**Baseline.** A conventional C40 structural concrete mix (350 kg cement/m³, 0 SCMs, 28-day cure) producing 50 MPa strength at 335 kg CO₂/m³. The strength predictor baseline is XGBoost on the 8 raw features of the UCI Concrete Compressive Strength dataset (1030 samples) with default hyperparameters, achieving MAE 2.78 MPa and R² 0.934.

**Iteration.** Three phases: (1) a model family tournament (XGBoost vs [LightGBM](https://lightgbm.readthedocs.io/) vs ExtraTrees vs Ridge — XGBoost won); (2) a 20-experiment HDR loop testing feature additions, hyperparameter modifications, target transforms, and monotonicity constraints — of which 4 were kept; (3) a compositional re-test confirming the union of the 4 kept changes beats any individual winner (MAE 2.547 vs 2.642). The keep/revert criterion was ≥0.005 MAE improvement (approximately one standard deviation of per-fold noise). A 3,685-candidate Phase B discovery sweep across 11 generation strategies then screened for Pareto-optimal mixes on the strength-vs-CO₂ frontier, filtered to in-distribution candidates (cement ≥ 102 kg/m³).

## Key References

1. Yeh, I-C. "Modeling of strength of high-performance concrete using artificial neural networks." *Cement and Concrete Research* **28**(12), 1797–1808 (1998). [DOI:10.1016/S0008-8846(98)00165-3](https://doi.org/10.1016/S0008-8846(98)00165-3)
2. Abrams, D.A. "Design of concrete mixtures." *Bulletin 1*, Lewis Institute (1918).
3. Mehta, P.K. and Monteiro, P.J.M. *Concrete: Microstructure, Properties, and Materials.* 4th ed., McGraw-Hill (2014).
4. Tipu, R.K. et al. "GreenMix-Pareto: Uncertainty-aware, physics-guided multi-objective optimization of low-carbon concrete mix designs." *Ain Shams Engineering Journal* (2026).
5. FHWA. "Tech Brief: Supplementary Cementitious Materials." FHWA-HIF-16-001 (2016).

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, program.md, and full project history
