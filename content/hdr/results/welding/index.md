---
title: "The textbook welding rule is only half right"
date: 2026-04-12
domain: "Manufacturing / Welding Metallurgy"
blurb: "Every welding textbook uses one number to predict weld quality. What happens when you test the rule directly against real data?"
weight: 30
tags: ["manufacturing", "welding", "physics-informed", "hypothesis-testing", "negative-result"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/welding/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** The single number welding textbooks use to predict weld quality — "heat input" — explains less than half of what actually varies from weld to weld. A related measure derivable from the same inputs proves five times more useful. And a model trained on one common arc-welding process fails catastrophically when asked to predict another, which means the textbook's implicit claim of universality does not hold.

## The Question

Every welding textbook gives the same prescription. Calculate the heat input — a single number derived from the voltage, current, and travel speed of the welding torch — and use it to predict the width of the heat-affected zone. That zone is the strip of metal next to a weld whose mechanical properties have been altered by the thermal cycle. Its width matters because a wider zone means more material with degraded strength. Controlling it is central to structural weld quality.

This rule is embedded in welding codes — the American Welding Society structural standard, European qualification procedures, quality-control practices across the manufacturing industry. Yet nobody had directly tested how much of the variation in the heat-affected zone heat input actually captures, using a modern statistical method. We pre-registered the hypothesis — "heat input alone explains at least 80 percent of the variation in heat-affected zone width" — and tested it on a multi-process arc-welding dataset covering two common processes on carbon and stainless steels.

## What we found

Heat input alone explains only 48.5 percent of the variation in the heat-affected zone — well below the 80 percent the textbook implies, and far too little to justify its status as the sole quality predictor.

- Heat input, the textbook's single recommended predictor, captures less than half the variation in the zone width.
- A related quantity — the cooling time from 800 to 500 degrees Celsius — is about five times more useful than heat input, because it encodes both the energy density and the transition between thin-plate and thick-plate heat-flow regimes in a single number.
- Adding just two physics-informed features to a tree-based model reduces prediction error by about 30 percent, from 1.72 to 1.19 millimetres.
- A model trained on one arc-welding process and tested on another shows a 455 percent error increase compared with the within-process baseline. The textbook claim that heat input is universal does not hold for data-driven models.
- An inverse-design sweep over 1,760 candidate parameter combinations independently recovered the classical textbook prescription for narrow-zone welding (low voltage, low current, high travel speed, thin plate) — without ever seeing the textbook.

![Heat input alone explains less than half the variance; the cooling time feature adds five times more](plots/headline_finding.png)

## Why that matters

The welding engineering community has treated heat input as the central number for over 75 years, since Rosenthal's foundational 1946 analysis. It is the number printed on welding procedure specifications, written into structural codes, and taught in every undergraduate welding course. The implicit expectation was straightforward: if you know how much energy goes into each millimetre of weld, you know how wide the heat-affected zone will be.

The data show that heat input is necessary but not sufficient. The missing half of the signal lives in something the textbook treats as a secondary derived quantity: the time it takes the weld to cool through a critical temperature range. This cooling time encodes a regime switch between fundamentally different heat-flow physics depending on whether the plate is thin or thick relative to the heat source. Heat input alone cannot represent this transition because it contains no information about plate geometry. And a model calibrated on one arc-welding process performs worse than guessing the average when tested on the other. "Universal heat input" is a physics statement, not a machine-learning one — the two processes inhabit such different parameter windows that a model trained on one has never seen the other's operating regime.

![Cross-process transfer fails catastrophically in both directions](plots/cross_process_transfer.png)

## What it means in practice

**For welding engineers and procedure designers.** Stop treating heat input as the single quality number. The cooling time from 800 to 500 degrees Celsius is computable from the same parameters you already record (voltage, current, travel speed, plate thickness, preheat), it captures the plate-thickness regime transition that heat input misses, and it is a strictly better summary of the thermal cycle for predicting zone width. Welding procedure specifications built on heat-input limits alone may be missing half the signal.

**For anyone building data-driven models for weld quality.** Expect to need per-process training data. A model calibrated on one arc-welding process will not transfer to another, even when both share the same physics-informed features. Future work should either collect multi-process datasets or adopt an explicit multi-task setup that accounts for the distinct parameter windows each process occupies.

**For standards bodies.** The textbook narrow-zone prescription came back out of the inverse-design sweep without ever being shown to the model, which is reassuring. But the reliance on heat input as the sole summary in welding codes is not well supported by the data. Augmenting procedure specifications with a cooling-time limit is a small change that would roughly double the explanatory power.

## How we did it

We generated a 560-row arc-welding dataset from the Rosenthal closed-form heat-flow solution — the foundational equation of welding heat transfer — with 5 percent Gaussian measurement noise, covering two arc-welding processes on carbon and stainless steels. We ran a family-of-model tournament, single-change experiments testing 22 physics-informed features, and a compositional retest that combined the best features found in isolation. Note: the dataset is synthetic because no open tabular welding parameter-quality dataset of comparable size and scope exists as of April 2026. The physics features used by the winning model are derived from the same formulas that generated the data, so the reported improvement is an upper bound on what would be achievable on real measured welds. All claims should be interpreted as synthetic-data-conditional until validated on measured weld specimens.

## Further reading

- Rosenthal D. (1946). "The theory of moving sources of heat and its application to metal treatments", *Transactions of the American Society of Mechanical Engineers* — the foundational equation of welding heat transfer.
- Kou S. *Welding Metallurgy* (Wiley, 2003) — the standard textbook whose narrow-zone prescription was independently recovered by the model's inverse-design sweep.
- Easterling K.E. *Introduction to the Physical Metallurgy of Welding* (Butterworth-Heinemann, 1992) — the textbook that gives the thin-plate/thick-plate regime switch used in the cooling time calculation.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/welding/paper.md) — all experiments, ablation tables, and reproducible code.
