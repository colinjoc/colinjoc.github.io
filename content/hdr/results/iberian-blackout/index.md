---
title: "The Blackout Nobody Saw Coming Was the Opposite Kind"
date: 2026-04-11
domain: "Energy / Power System Stability"
blurb: "On April 28, 2025, Spain and Portugal went dark when too much voltage -- not too little power -- collapsed the grid in 24 seconds. We built a stress detector from public data, then discovered it could not actually predict the blackout it was designed to explain."
weight: 29
tags: ["energy", "power-systems", "blackout", "cascading-failure", "voltage-stability", "solar-PV", "renewable-energy", "Spain", "Portugal", "overvoltage", "reactive-power"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/iberian_blackout/paper.md).*

## The Question

At 12:33 on Monday, April 28, 2025, the entire electrical grid of Spain and Portugal collapsed. Roughly 31 gigawatts of generation disconnected in under 24 seconds. Trains stopped in tunnels. Traffic lights went dark across Madrid, Barcelona, and Lisbon. Hospitals switched to backup generators. Approximately 47 million people lost power for up to ten hours.

Every previous major European blackout -- Italy in 2003, the continental split in 2006, Turkey in 2015, the United Kingdom in 2019 -- followed the same pattern: generation dropped, frequency fell, and the system collapsed. The instinctive explanation for the Iberian event was the same: too much solar, not enough spinning mass. But the 472-page investigation by 49 experts told a different story. We asked: what actually caused it, and can the dangerous conditions be identified in advance from publicly available data?

## What We Found

The European investigation (ENTSO-E, March 2026) revealed that the grid died from too much voltage, not too little power. This is the first documented overvoltage-driven cascading blackout in the Continental European synchronous area -- a failure mode that classical power system stability theory barely considers.

- At the moment of collapse, solar panels alone produced 59% of Spain's generation, the grid was exporting surplus to three countries, and spot prices had gone negative.
- When a group of renewable plants reduced output by 500 megawatts, they simultaneously withdrew the invisible voltage support they had been providing. Transmission voltage spiked above 435 kilovolts (versus a safe range of 380-420), and a self-reinforcing cascade brought the system down in 24 seconds.
- Dropping the inertia proxy from the model changed nothing -- directly confirming the investigation's finding that "even with significantly higher inertia values, the loss of system synchronism would not have been avoided."
- A simple threshold rule on a composite stress score, with no machine learning at all, scored higher than the best trained model (F1 = 0.933 versus 0.857), exposing a fundamental circularity in the labelling approach.
- When the actual blackout date was held out, every model assigned it near-zero risk. The models detected stress-score exceedances, not the cascade itself.

## Why That's Surprising

Two things are surprising here, and they cut in opposite directions.

First, the physics. The dominant public narrative -- "too much solar, not enough spinning mass" -- is wrong in a specific, testable way. The grid did not collapse because it lacked generation. It collapsed because it had too much, specifically non-synchronous generation that provided no dynamic voltage support. Reactive power absorbers that could have prevented the cascade were available but required manual activation. The failure mode is the mirror image of everything power engineers have spent decades preparing for.

Second, the machine learning. The model appeared to work well: the ensemble reached an area under the receiver operating characteristic curve of 0.948. But the eight "high-risk" days it was detecting were not independently identified grid events. Seven of eight were created by applying a threshold to a composite stress score computed from the same features the model uses. The model was being tested on its ability to recover its own labelling rule. With only one actual blackout and no independent label source, the reported metrics measure pattern-matching on training artifacts, not genuine cascade prediction. The 95% confidence interval for the best model's F1 score spanned from 0.571 to 1.000 -- nearly the entire possible range.

## What It Means

Solar energy did not cause this blackout. Insufficient voltage control infrastructure, outdated protection relay settings, fixed power factor operating modes, and manual rather than automatic reactive power management caused it. The conditions that produced the cascade -- high solar output, low demand, heavy exports, negative prices -- are not unique to Spain. Germany, Australia, California, and every other region with rapidly growing solar capacity will face the same challenge.

The domain-informed features themselves -- voltage stress, reactive power gap, export fraction -- do capture the conditions the investigation identified. Monitoring them in real time, even with a simple threshold, could alert operators to days where preventive measures may be warranted: activating shunt reactors, switching renewable plants from fixed to active voltage regulation, and dispatching synchronous condensers. But honest assessment requires acknowledging that with one blackout event and no independent grid-event labels, we built a stress detector, not a cascade predictor. Whether those extreme conditions are necessary, sufficient, or even reliably correlated with actual cascade risk cannot be determined from a single event.

## How We Did It

All data are real operational records from the [REE REData API](https://apidatos.ree.es/en/datos/), the open-data platform of Spain's transmission system operator, covering daily generation by technology, hourly demand, interconnector flows with France, Portugal, and Morocco, and spot electricity prices from January through May 2025 (94 days, no synthetic data). We decomposed the [ENTSO-E final report](https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/) root cause analysis into three physics proxy features, ran a five-model tournament with leave-one-out cross-validation, conducted six ablation experiments, and tested threshold sensitivity across six percentile cutoffs -- 25 total experiments survived or were reverted.

## Further Reading

- ENTSO-E Expert Panel (2026). [Final Report on the Grid Incident in Spain and Portugal on 28 April 2025](https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/) -- the official 472-page investigation establishing the overvoltage cascade mechanism.
- Various (2026). ["The overvoltage-driven blackout of the Iberian Peninsula on 28th April 2025."](https://www.sciencedirect.com/science/article/abs/pii/S235246772600007X) *Electric Power Systems Research* -- the first peer-reviewed paper classifying this as a novel failure mode.
- Full technical write-up: [paper.md](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/iberian_blackout/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
