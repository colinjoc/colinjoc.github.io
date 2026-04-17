---
title: "The Textbook Welding Rule Is Only Half Right"
date: 2026-04-12
domain: "Manufacturing / Welding Metallurgy"
blurb: "Welding textbooks say one number -- heat input -- explains weld quality. We tested that claim directly and found it explains less than half the variation. A different physics-based measure, derivable from the same inputs, proved five times more useful."
weight: 30
tags: ["manufacturing", "welding", "physics-informed", "hypothesis-testing", "negative-result"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/welding/paper.md).*

## The Question

Every welding textbook gives the same prescription: calculate the "heat input" -- a single number derived from the voltage, current, and travel speed of the welding torch -- and use it to predict the width of the Heat-Affected Zone (HAZ). The HAZ is the strip of metal next to a weld whose mechanical properties have been altered by the thermal cycle. Its width matters because a wider HAZ means more material with degraded strength, and controlling it is central to structural weld quality.

This rule is embedded in welding codes such as the American Welding Society's structural standard, in European qualification procedures, and in quality control practices across the manufacturing industry. Yet no published study has directly tested how much of the HAZ variation heat input actually captures using a modern statistical method. We pre-registered the hypothesis "heat input alone explains at least 80 percent of the variation in HAZ width" and tested it on a multi-process arc welding dataset covering two common processes on carbon and stainless steels.

## What We Found

Heat input alone explains only 48.5 percent of the variation in HAZ width -- well below the 80 percent the textbook implies, and far too little to justify its status as the sole quality predictor. A different physics-based measure proved five times more useful, and a model trained on one welding process failed catastrophically when tested on another.

- Heat input, the textbook's single recommended predictor, explains less than half the variation in HAZ width -- not the 80 percent that textbook intuition would suggest.
- A related quantity called the cooling time (from 800 to 500 degrees Celsius) was five times more useful than heat input, because it captures both energy density and the transition between thin-plate and thick-plate heat-flow regimes in a single number.
- Adding just two physics-informed features to a tree-based model improved prediction accuracy by 30.5 percent, reducing error from 1.72 mm to 1.19 mm.
- A model trained on one arc welding process and tested on another showed a 455 percent error increase over the within-process baseline -- the textbook claim that heat input is "universal" does not hold for data-driven models.
- An inverse-design sweep over 1,760 candidate parameter combinations independently recovered the classical textbook prescription for narrow-HAZ welding (low voltage, low current, high travel speed, thin plate) without ever seeing the textbook.

![Heat input alone explains less than half the variance; the cooling time feature adds five times more](plots/headline_finding.png)

![Permutation importance ranking of all eight features in the winning model](plots/feature_importance.png)

## Why That's Surprising

The welding engineering community has treated heat input as the central number for more than 75 years, since Rosenthal's foundational 1946 analysis. It is the number printed on welding procedure specifications, written into structural codes, and taught in every undergraduate welding course. The expectation was straightforward: if you know how much energy goes into each millimetre of weld, you know how wide the heat-affected zone will be.

What the data revealed is that heat input is necessary but not sufficient. The missing half of the signal lives in something the textbook treats as a secondary derived quantity: the time it takes the weld to cool through a critical temperature range. This cooling time encodes the plate-thickness regime switch -- a transition between fundamentally different heat-flow physics depending on whether the plate is thin or thick relative to the heat source. Heat input alone cannot represent this transition because it contains no information about plate geometry. A GMAW-trained model tested on the other process (GTAW) performed worse than simply guessing the average, revealing that "universal heat input" is a physics statement, not a machine-learning one. The two processes inhabit such different parameter windows that a model calibrated on one has never seen the other's operating regime.

![Cross-process transfer fails catastrophically in both directions](plots/cross_process_transfer.png)

## What It Means

For welding engineers: heat input is necessary but not sufficient. The cooling time from 800 to 500 degrees Celsius, computable from the same process parameters you already record (voltage, current, travel speed, plate thickness, preheat temperature), encodes both the energy density and the plate-thickness regime transition in one number. It is a strictly better summary of the thermal cycle for predicting HAZ width. Welding procedure specifications built around heat input limits alone may be missing half the signal.

For anyone building machine-learning models for welding quality: expect to need per-process training data. A model calibrated on one arc welding process will not transfer to another, even when both share the same physics-informed features. Future work should either collect multi-process datasets or adopt explicit multi-task formulations that account for the distinct parameter windows each process occupies.

## How We Did It

We generated a 560-row arc welding dataset from the Rosenthal closed-form heat-flow solution -- the foundational equation of welding heat transfer -- with 5 percent Gaussian measurement noise, covering two arc welding processes on carbon and stainless steels. We ran a four-family model tournament, 50 single-change experiments in a Hypothesis-Driven Research loop, and a six-round compositional retest. Four of the 50 experiments survived the keep criterion, plus one composition retest that became the winner. The dataset is synthetic because no open tabular welding parameter-quality dataset of comparable size and scope exists as of April 2026. The physics features used by the winning model are derived from the same formulas that generated the data, so the reported improvement is an upper bound on what would be achievable on real measured welds. All claims should be interpreted as synthetic-data-conditional until validated on measured weld specimens.

## Further Reading

- Kou S. *Welding Metallurgy* (Wiley, 2003) -- the standard textbook whose narrow-HAZ prescription was independently recovered by the model's inverse-design sweep.
- Easterling K.E. *Introduction to the Physical Metallurgy of Welding* (Butterworth-Heinemann, 1992) -- the textbook that gives the thin-plate/thick-plate regime switch used in the cooling time calculation.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/welding/paper.md) -- all 50 experiments, ablation tables, and reproducible code.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
