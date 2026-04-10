---
title: "The Textbook Welding Rule Is Only Half Right"
date: 2026-04-09
weight: 10
blurb: "Welding textbooks say one number -- the heat input -- explains weld quality. We tested it directly for the first time and found it explains less than half. A different physics-based measure, derivable from the same inputs, is five times more useful."
domain: "Manufacturing / Welding Metallurgy"
tags: ["manufacturing", "welding", "physics-informed", "hypothesis-testing", "negative-result"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/welding/paper.md).*

## The Question

Arc welding is a 150-year-old technology, and the textbook wisdom for predicting weld quality has been the same for decades: calculate the heat input -- a single number derived from the voltage, current, and travel speed of the welding torch -- and use it as the dominant predictor of how wide the heat-affected zone will be. The heat-affected zone is the region of base metal whose mechanical properties have been altered by the welding thermal cycle, and controlling its width is central to structural weld quality.

This rule is so universally taught that no published study has ever directly tested it with a modern statistical method. We pre-registered the hypothesis "heat input alone explains at least 80 percent of the variation in heat-affected zone width" and tested it on a multi-process arc welding dataset.

## What We Found

Heat input alone explains 48.5 percent of the variation -- well below the 80 percent the textbook implies. It is a useful feature, but it is nowhere near sufficient. A different physics-based measure -- the cooling time from 800 to 500 degrees Celsius, derivable from the same welding parameters -- added five times more predictive accuracy than heat input did.

- The pre-registered hypothesis was refuted. Heat input explains less than half of what drives heat-affected zone width.
- The missing signal lives in two places: the transition between thin-plate and thick-plate heat flow regimes (captured by the cooling time feature), and the preheat temperature correction.
- The cooling time feature encodes both the heat input and the regime transition in a single number. A tree-based model can split on it directly instead of having to reconstruct the regime boundary from raw parameters.
- A second pre-registered hypothesis -- that a model trained on one welding process transfers to another within 15 percent error -- also failed. The transfer error was 455 percent, and in the reverse direction the model performed worse than simply predicting the average.
- An inverse design sweep using the trained model recovered the classical textbook prescription for narrow heat-affected zone welding (low voltage, low current, high travel speed on thin plate) without ever seeing the textbook.

![Heat input alone explains less than half the variance; the cooling time feature adds five times more](plots/headline_finding.png)

## Why That's Surprising

The heat input rule is not just a classroom simplification -- it is embedded in welding codes (the American Welding Society's structural code specifies it), in qualification procedures, and in quality control practices across the manufacturing industry. Entire welding procedure specifications are built around heat input limits. The finding that it captures less than half the signal, while a readily computable alternative captures substantially more, has practical implications for how welding engineers specify and monitor processes.

The catastrophic failure of cross-process transfer is equally surprising. The textbook treats heat input as a universal quantity -- the same value should produce the same thermal cycle regardless of whether the process is gas metal arc or gas tungsten arc welding. In machine-learning terms, this universality does not hold. The two processes occupy different regions of the parameter space, and a model trained on one has no basis for interpolation to the other.

![Cross-process transfer fails catastrophically in both directions](plots/cross_process_transfer.png)

## What It Means

For welding engineers: stop treating heat input as the sole quality predictor. The cooling time from 800 to 500 degrees, computable from the same parameters, encodes both the heat input and the plate-thickness regime transition in one number. It is a strictly better summary of the thermal cycle for predicting heat-affected zone width.

For anyone building machine-learning models for welding: expect to need per-process training data. A model calibrated on one arc welding process will not generalise to another. The claim that heat input is universal refers to the underlying physics, not to the calibration of a data-driven regressor.

## How We Did It

We generated a 560-row arc welding dataset from the Rosenthal closed-form heat-flow solution -- the foundational equation of welding heat transfer -- with realistic measurement noise, covering two common arc welding processes on carbon and stainless steels. A 45-row real friction stir welding subset was held out as a sanity check. We ran a four-family model tournament, 50 single-change experiments, and a six-round compositional retest. The dataset is synthetic because no open tabular welding dataset of comparable size and scope exists. All claims are upper bounds on what can be achieved on real measured data. Full code and data are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/welding).

Note: these results are based on synthetic data generated from the Rosenthal heat-flow equation, not measured weld specimens.

## Further Reading

- Rosenthal D. "The Theory of Moving Sources of Heat." *Transactions of the ASME* (1946). -- the foundational heat-flow solution underlying the dataset and the cooling-time feature.
- Easterling KE. *Introduction to the Physical Metallurgy of Welding* (Butterworth-Heinemann, 1992). -- the textbook that gives the thin-plate/thick-plate regime switch used in the cooling time calculation.
- Kou S. *Welding Metallurgy* (Wiley, 2003). -- the textbook whose narrow heat-affected zone prescription was independently recovered by the model's inverse design sweep.

---
📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)**
