---
title: "The Blackout Nobody Saw Coming Was the Opposite Kind"
date: 2026-04-11
domain: "Energy / Power System Stability"
blurb: "Spain and Portugal went dark in 24 seconds last April. The cause was the opposite of what everyone assumed."
weight: 29
tags: ["energy", "power-systems", "blackout", "cascading-failure", "voltage-stability", "solar-PV", "renewable-energy", "Spain", "Portugal", "overvoltage", "reactive-power"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/iberian_blackout/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** The Iberian grid did not collapse because it had too little power. It collapsed because it had too much voltage — a failure mode that textbooks and national warning systems were not prepared for. And the machine-learning model we built to predict it turned out not to predict anything.

## The Question

At 12:33 on Monday 28 April 2025, the entire electrical grid of Spain and Portugal collapsed. Around 31 gigawatts of generation disappeared in under 24 seconds. Trains stopped in tunnels. Traffic lights went dark in Madrid, Barcelona and Lisbon. Hospitals switched to backup power. About 47 million people lost electricity for up to ten hours.

Every previous major European blackout has followed the same storyline. Generation drops, frequency falls, the system gives up. The instinctive explanation for Iberia was the same: too much solar, not enough of the heavy spinning generators that hold frequency steady. We asked two questions. What actually caused it, and could anyone have seen it coming using only the data members of the public can download?

## What we found

The official investigation, published in March 2026 by 49 European grid experts, found that the grid died from **too much voltage, not too little power**. This is the first documented cascade of its kind in continental Europe. Classical power-system theory barely considers it.

- At the moment of collapse, Spain was running on 59 percent solar, exporting surplus to three neighbouring countries, with electricity spot prices already negative.
- A small group of renewable plants cut their output by 500 megawatts. As they did, they withdrew the invisible voltage support they had been quietly providing. Transmission voltage shot above 435 kilovolts, well above the safe ceiling of 420. A self-reinforcing cascade brought the system down in 24 seconds.
- Removing the "spinning mass" measure from our model changed nothing, which matches what the official investigation concluded: even much higher inertia would not have stopped the cascade.
- A model built from three carefully chosen physics signals — voltage stress, a reactive-power gap, and how heavily the grid was exporting — did look impressive at first. The most sophisticated version scored a near-perfect 0.948 on the standard machine-learning yardstick.
- That score is an illusion. The "high-risk days" the model was graded on were created by applying a threshold to the same features the model was using. It was grading its own homework. A simple rule — "flag the day if the threshold is crossed" — scored slightly higher than the model.
- When we held out the actual blackout and asked the model to predict it cold, every version assigned it near-zero risk.

## Why that matters

Two lessons, pulling in opposite directions.

**The physics.** The public narrative — too much solar, not enough inertia — is wrong in a specific, testable way. The grid did not collapse because it was short on generation. It collapsed because it had plenty of generation but none of it was providing the moment-to-moment voltage support the system needed. Equipment that could have absorbed the extra voltage was available, but switching it on required a human operator. The failure is the mirror image of everything grid engineers have spent decades preparing for, and the ingredients — high solar output, low demand, heavy exports, negative prices — are not unique to Spain. Germany, Australia, California and anywhere else that has scaled up solar quickly face the same setup.

**The machine learning.** What looked like a working predictor was the model recovering a rule we had fed it. With one real blackout and no other independent way to label "dangerous days", impressive-looking accuracy numbers are almost always an artefact. This is worth remembering the next time a grid operator, a bank, or a hospital claims that a model can predict rare catastrophic events: ask how many of the events the model was trained and tested on.

## What it means in practice

Solar did not cause this blackout. A long list of more prosaic things did: too few voltage-control devices switched on, protection relays set with old assumptions, renewable plants running in modes that did not help regulate voltage, and a control process that relied on humans to activate the equipment that would have saved the grid.

The three physics signals — voltage stress, reactive-power gap, export fraction — are genuinely useful. Operators could watch them in real time, even without any machine learning, and take preventive action on days where they spike. But calling the resulting tool a "cascade predictor" would overstate what we can actually claim. With a sample size of one blackout, it is an alarm for extreme conditions, not a forecast of collapse.

## How we did it

We used 94 days of real operational records from [Spain's grid operator's open data](https://apidatos.ree.es/en/datos/) — generation by technology, hourly demand, interconnector flows, spot prices — covering January through May 2025. We built three physics-based signals from the [official 472-page investigation](https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/), ran five competing model types against each other, and stress-tested the winner by holding out the actual blackout, ablating each feature, and varying every threshold. No synthetic data was used.

## Further reading

- ENTSO-E Expert Panel (2026). [Final Report on the Grid Incident in Spain and Portugal on 28 April 2025](https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/) — the official investigation.
- Various (2026). ["The overvoltage-driven blackout of the Iberian Peninsula on 28th April 2025"](https://www.sciencedirect.com/science/article/abs/pii/S235246772600007X), *Electric Power Systems Research* — the first peer-reviewed paper classifying this as a new failure mode.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/iberian_blackout/paper.md) — all experiments and diagnostics.
