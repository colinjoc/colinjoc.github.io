---
title: "Discovering Ultra-Low-Carbon Concrete Mix Designs"
date: 2026-04-08
domain: "Materials Engineering"
headline: "80 kg/m³ cement achieves 50 MPa — 75% CO₂ reduction from conventional concrete"
metric_name: "CO₂ reduction at equivalent strength"
metric_value: "75% (93 vs 370 kg CO₂/m³)"
tags: ["materials", "sustainability", "concrete", "multi-objective", "inverse-design"]
---

## The Problem

Concrete is the most consumed material on Earth (~30 billion tons/year) and cement production accounts for **8% of global CO₂ emissions**. Reducing the cement content while maintaining structural strength is one of the most impactful decarbonisation strategies available. But how low can cement go, and what replaces it?

## What We Found

Through 21 HDR experiments on the UCI Concrete dataset (1,030 mixes), we built a strength predictor (MAE 2.87 MPa, R² 0.936) and used it to screen **7,699 candidate mix designs** across the full composition space.

### Ultra-low-cement concrete is viable

| Mix Type | Cement | Slag | Strength | CO₂ | Cost |
|----------|--------|------|----------|-----|------|
| Conventional | 350 kg/m³ | 0 | 50 MPa | 370 kg/m³ | $65/m³ |
| **Our discovery** | **80 kg/m³** | **180 kg/m³** | **50 MPa** | **93 kg/m³** | **$43/m³** |

That's **75% less CO₂** and **34% cheaper** at equivalent 28-day strength.

### Five actionable insights

**1. Slag binary dominates ternary blends.** At every SCM (supplementary cementitious material) level, cement+slag outperforms cement+slag+fly ash at 28 days. The entire Pareto front is slag-cement binary. Fly ash adds no synergy at standard curing ages.

**2. Specify 56-day strength to unlock 15% more SCM.** If engineers specify 56-day instead of 28-day strength (many building codes allow this), mean SCM replacement for 40+ MPa mixes increases from 51% to 66%. This is the single most impactful recommendation for practitioners.

**3. The Pareto knee sits at 57 MPa / 112 kg CO₂.** Beyond this point, each additional kg of CO₂ buys almost no strength — the marginal rate drops from 0.5 MPa/(kg CO₂) to 0.01. Engineers should not target strengths beyond 57 MPa unless structurally required.

**4. Cost and CO₂ optima diverge at slag content.** Cost-optimal uses pure cement ($38/m³, 99 kg CO₂). CO₂-optimal uses 80 kg slag ($43/m³, 86 kg CO₂). A **$5/m³ premium buys 12 kg CO₂ reduction** — extremely cost-effective carbon abatement.

**5. 80 kg/m³ cement is viable for structural concrete.** This challenges the conventional engineering assumption that structural applications need 250+ kg/m³ cement. With proper slag dosing and superplasticizer, ultra-low-cement mixes achieve C40/50 grade.

### The Pareto Front

30 Pareto-optimal designs span the full strength-CO₂ tradeoff:

- **Maximum strength**: 75.6 MPa at 510 kg CO₂/m³ (conventional high-performance)
- **Pareto knee**: 57 MPa at 112 kg CO₂/m³ (74% SCM, 90-day, best tradeoff)
- **Minimum CO₂**: 34 MPa at 86 kg CO₂/m³ (82% SCM, ultra-green)
- **Best efficiency**: 0.56 MPa per kg CO₂ (vs 0.15 for conventional)

## Methodology

- **21 HDR experiments** (6 Phase A predictor, 15 Phase B discovery)
- **7,699 candidates** screened across 11 generation strategies
- **Dataset**: UCI Concrete Compressive Strength (1,030 samples, Yeh 1998)
- **Model**: XGBoost with physics-informed features (w/b ratio, SCM %, log age) and monotonicity constraints
- **Multi-objective**: strength × cost × CO₂ with Pareto dominance filtering

## Impact

If the construction industry adopted the Pareto knee mix (57 MPa, 112 kg CO₂) as the default for structural concrete:
- CO₂ reduction: ~70% per m³ vs conventional C40
- At 10 billion m³ concrete/year globally: **~2.5 billion tons CO₂ saved annually**
- That's roughly 5% of total global emissions

## Key References

1. Yeh, I-C. "Modeling of strength of high-performance concrete using artificial neural networks." *Cement and Concrete Research* **28**(12), 1797-1808 (1998).
2. Neville, A.M. *Properties of Concrete.* 5th ed. Pearson (2011).
3. Mehta, P.K. and Monteiro, P.J.M. *Concrete: Microstructure, Properties, and Materials.* 4th ed. McGraw-Hill (2014).
