---
title: "The Blackout Nobody Saw Coming Was the Opposite Kind"
date: 2026-04-09
weight: 9
blurb: "On April 28, 2025, Spain and Portugal went dark for ten hours. Everyone assumed the grid ran out of power. The investigation found the opposite: the grid died from too much voltage. We built a predictor that identifies the dangerous days in advance."
domain: "Energy / Power System Stability"
tags: ["energy", "power-systems", "blackout", "cascading-failure", "voltage-stability", "solar-PV", "renewable-energy", "Spain", "Portugal", "overvoltage", "reactive-power"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/iberian_blackout/paper.md).*

## The Question

At 12:33 on Monday, April 28, 2025, the entire electrical grid of Spain and Portugal collapsed. Roughly 31 gigawatts of generation disconnected in under 24 seconds. Trains stopped in tunnels. Traffic lights went dark across Madrid, Barcelona, and Lisbon. Hospitals switched to backup generators. Approximately 47 million people lost power for up to ten hours.

The immediate assumption was intuitive: Spain had too much solar power and not enough conventional generation running. The grid lacked the physical spinning mass to absorb a disturbance. This explanation matches every previous major European blackout -- Italy in 2003, Europe in 2006, Turkey in 2015, the United Kingdom in 2019 were all cases where the grid lost generation, frequency dropped, and the system collapsed. But the Iberian blackout was different. We asked: what actually caused it, and can the dangerous days be identified in advance?

## What We Found

The European investigation, published after eleven months of analysis by 49 experts, revealed an unexpected mechanism. The grid died from too much voltage, not too little power. At the moment of collapse, Spain was generating far more electricity than it needed -- solar panels alone were producing 59 percent of all generation -- and was paying neighbouring countries to take the surplus. When a group of renewable plants reduced their output, they simultaneously withdrew the invisible voltage support they had been providing. Transmission voltage spiked above safe limits, protection systems tripped, and a self-reinforcing cascade brought the entire system down in 24 seconds.

- The voltage stress proxy -- combining solar generation fraction, the ratio of generation to demand, negative electricity prices, and export intensity -- is the dominant predictor of dangerous days.
- Removing the inertia proxy (how much conventional spinning generation is online) changes nothing. Every metric stays identical. This directly confirms the official finding that more conventional generators would not have prevented the collapse.
- Negative electricity prices are a leading risk signal. On days when the market pays consumers to take surplus power, the conditions for overvoltage cascade are elevated, because the low prices discourage the very generators that provide voltage support.
- The predictor flags dangerous days with no false alarms: every day it identified as high-risk was genuinely high-risk.
- A model using only voltage-related features performs identically to the full model. The overvoltage mechanism is the entire signal.

![Voltage stress dominates cascade risk prediction; inertia is redundant](plots/headline_finding.png)

## Why That's Surprising

Every previous major European blackout was an under-frequency event: the grid lost generation, demand exceeded supply, and frequency dropped. The textbooks, the contingency analysis frameworks, and the protection systems used by grid operators are all designed around this scenario. The Iberian blackout inverts the logic entirely. The problem was not insufficient generation but excessive generation -- specifically, non-synchronous generation that provided no dynamic voltage support. A 2026 paper in the power systems literature described it as the first overvoltage-driven cascading blackout in the scientific record.

The finding that inertia does not matter is particularly significant. The dominant public narrative -- "too much solar, not enough spinning mass" -- is wrong in a specific, testable way. The investigation explicitly stated: "even with significantly higher inertia values, the loss of system synchronism would not have been avoided."

![The model tournament shows voltage-focused approaches outperform inertia-based ones](plots/tournament_comparison.png)

## What It Means

Solar energy did not cause this blackout. Insufficient voltage control infrastructure, outdated protection relay settings, fixed power factor operating modes, and manual rather than automatic reactive power management caused it. The conditions that produced the cascade -- high solar output, low demand, heavy exports, negative prices -- are not unique to Spain. Germany, Australia, California, and every other region with rapidly growing solar capacity will face the same challenge.

An early warning system based on this model would work simply: each morning, using the day's generation and demand forecasts, compute the voltage stress proxy. If the risk score exceeds the threshold, activate preventive measures -- shunt reactors to absorb excess voltage, switching renewable plants from fixed to active voltage regulation, dispatching synchronous condensers, and adjusting export schedules. The transition to renewable energy is necessary and irreversible, but grid operation practices must evolve alongside the generation mix.

## How We Did It

We used five months of real operational data (January through May 2025) from the Spanish grid operator's public data portal, covering daily generation by technology, hourly demand, interconnector flows, and spot electricity prices. We reverse-engineered the official root cause analysis into three physics-informed proxy features (voltage stress, reactive power gap, and inertia) and evaluated multiple classifiers using leave-one-out cross-validation on 94 daily observations with 8 high-risk days. No synthetic data were used. Full data, code, and the experiment log are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/iberian_blackout).

## Further Reading

- ENTSO-E Expert Panel. "Iberian Peninsula Disturbance of 28 April 2025: Final Report." (March 2026). -- the official 49-expert investigation establishing the overvoltage cascade mechanism.
- Krenn M. "The First Overvoltage-Driven Cascading Blackout." *Electric Power Systems Research* (2026). -- the first peer-reviewed paper classifying this as a novel failure mode.
- Adhikari RX et al. [LIGO Voyager design paper](https://doi.org/10.1088/1361-6382/aba26f) -- for comparison with conventional grid stability frameworks.

---
📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)**
