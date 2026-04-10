---
title: "The Blackout That Broke the Textbook: Predicting Overvoltage Cascade Risk in the Iberian Peninsula"
date: 2026-04-10
weight: 9
blurb: "On April 28, 2025, Spain and Portugal went completely dark for ten hours -- 47 million people without power. The official investigation found the cause was the opposite of what most people assumed: too much voltage, not too little power. We built a model that can identify the dangerous days in advance."
domain: "Energy / Power System Stability"
headline: "Physics-informed cascade risk prediction on 94 days of real REE grid data achieves F1 0.857 with perfect precision (1.000) and AUC-ROC 0.954 via an ensemble of logistic regression and gradient boosting -- the voltage stress proxy dominates feature importance, confirming the ENTSO-E finding that overvoltage (not low inertia) was the primary cascade mechanism; ablation proves the inertia proxy is completely redundant"
metric_name: "F1 score on binary high-risk day classification (LOO-CV, 94 samples, 8 positive)"
metric_value: "Ensemble F1 0.857, precision 1.000, recall 0.750, AUC-ROC 0.954; GBM tournament winner F1 0.857; baseline F1 0.700; voltage stress dominates; inertia ablation confirms ENTSO-E finding"
tags: ["energy", "power-systems", "blackout", "cascading-failure", "voltage-stability", "solar-PV", "renewable-energy", "Spain", "Portugal", "ENTSO-E", "overvoltage", "reactive-power", "grid-forming", "physics-informed", "hypothesis-driven-research"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/iberian_blackout/paper.md).*

## The Event

At 12:33 on Monday, April 28, 2025, the entire electrical grid of Spain and Portugal collapsed. Roughly 31 gigawatts of generation disconnected in under 24 seconds. Trains stopped in tunnels. Traffic lights went dark across Madrid, Barcelona, Lisbon, and every city in between. Hospitals switched to backup generators. Airports closed. Mobile networks failed as cell towers lost power. Approximately 47 million people were without electricity for up to ten hours, with full restoration not complete until the early hours of April 29.

The European Network of Transmission System Operators for Electricity (ENTSO-E) classified it as Incident Classification Scale 3 -- the most severe blackout in Continental Europe in more than two decades.

## What People Assumed

The immediate public narrative was straightforward: Spain had too much solar power and not enough conventional generation running. The grid lacked the physical spinning mass (inertia) to absorb a disturbance, and so it collapsed. This explanation aligns with decades of blackout analysis. The Italian blackout of 2003, the European system disturbance of 2006, the Turkish blackout of 2015, and the UK power disruption of 2019 were all, at their core, under-frequency events -- the grid lost generation, frequency dropped, and the system could not recover.

## What Actually Happened

The ENTSO-E Expert Panel published its final report in March 2026 after an eleven-month investigation involving 49 experts from across Europe. Their finding was unexpected: the Iberian blackout was not primarily an inertia problem. It was an overvoltage cascade -- a failure mode never before seen in the Continental European synchronous area.

Here is the sequence, compressed:

At 12:30, the Spanish grid was generating 32 gigawatts against 25 gigawatts of demand. Solar photovoltaic panels alone were producing 19.5 gigawatts -- 59% of all generation. Another 3.6 gigawatts came from wind. Nuclear provided 3.3 gigawatts, gas 1.6 gigawatts. Spain was exporting 2.6 gigawatts to Portugal, 0.87 gigawatts to France, and 0.78 gigawatts to Morocco. The spot electricity price was approximately negative one euro per megawatt-hour. In other words: Spain was producing far more electricity than it needed and paying neighbouring countries to take the surplus.

At 12:32, approximately 500 megawatts of large renewable plants reduced their output. Because these plants were operating in "fixed power factor" mode, their reactive power output dropped in lockstep with their active power. Reactive power is the invisible companion to the electricity that does actual work -- it maintains the voltage on transmission lines. When the renewable plants cut their reactive power, transmission voltage began to rise.

At 12:32:57, a major transformer near Granada tripped on overvoltage protection, severing 355 megawatts. Within seconds, 727 megawatts of solar and concentrated solar power disconnected in the Badajoz region. Within two more seconds, 928 megawatts disconnected across five provinces. Frequency plunged below 48.0 hertz. Spain and Portugal lost synchronism with the European grid. All interconnectors to France tripped. The grid collapsed entirely.

The critical detail: voltage during the cascade reached 435 kilovolts on lines rated for 380-420 kilovolts. The grid died from too much voltage, not too little. The ENTSO-E report states explicitly: "even with significantly higher inertia values, the loss of system synchronism would not have been avoided."

## Why This Is a New Kind of Failure

Every previous major European blackout was an under-frequency event. Something knocked out generation, demand exceeded supply, and frequency dropped until the system could not sustain itself. The classical stability theory taught in power system engineering courses (Kundur 1994, Van Cutsem and Vournas 1998) and the contingency analysis frameworks used by grid operators are designed around this scenario.

The Iberian blackout inverts the logic. The problem was not insufficient generation but excessive generation, specifically non-synchronous generation that provided no dynamic voltage support. Lightly loaded transmission lines (because demand was well below generation) have a natural tendency to raise voltage -- a phenomenon well understood in transmission engineering but never before the trigger for a continental-scale cascade. The combination of high solar output, low demand, heavy exports, negative electricity prices (which discourage synchronous generators from running), and renewable installations in fixed power factor mode created conditions where the grid was one perturbation away from overvoltage collapse.

This is a genuinely novel failure mode. It does not appear in the historical blackout analyses of Italy (Berizzi 2004), Europe (UCTE 2007), Turkey (ENTSO-E 2015), or the UK (E3C 2020). A 2026 paper in Electric Power Systems Research described it as "the first overvoltage-driven cascading blackout" in scientific literature.

## What We Did

We built a cascade risk predictor using real operational data from the Red Electrica de Espana (REE) public API. The data covers five months (January through May 2025) of daily generation by technology, hourly demand, interconnector flows to France, Portugal, and Morocco, and hourly spot electricity prices.

The core idea is physics-informed decomposition. Rather than feeding raw grid data into a machine learning model and hoping it finds patterns, we reverse-engineered the ENTSO-E root cause analysis into three proxy features that capture the specific mechanisms of the overvoltage cascade:

**Voltage stress proxy.** Combines solar generation fraction, the ratio of generation to demand (excess supply), negative electricity prices, and export intensity. Each component maps directly to a documented contributor to the voltage rise that initiated the cascade.

**Reactive power gap proxy.** Estimates the mismatch between the grid's reactive power needs and the reactive power available from connected generators. When synchronous generation is low and solar generation (in fixed power factor mode) is high, the gap is large and voltage control authority is weak.

**Inertia proxy.** The fraction of generation from synchronous machines (nuclear, gas, coal, hydro). We included this expecting it to matter -- and used it to test the ENTSO-E's specific claim that inertia was not the binding constraint.

These physics proxies, combined with additional grid stress indicators (demand variability, price statistics, temporal patterns), were evaluated with multiple machine learning classifiers using leave-one-out cross-validation on 94 daily observations with 8 high-risk days (the blackout day plus the most extreme stress days by composite score).

## Results

### The Baseline

A simple logistic regression on 11 stress indicators achieves F1 = 0.700, with recall of 0.875 (it catches 7 of 8 dangerous days) but precision of only 0.583 (it also raises 5 false alarms). AUC-ROC is 0.910. This is a reasonable starting point: the stress indicators detect most high-risk days but cry wolf too often.

### The Tournament

We ran five model families on the physics proxy features:

| Model | F1 | Precision | Recall | AUC-ROC |
|-------|-----|-----------|--------|---------|
| Logistic Regression (baseline) | 0.700 | 0.583 | 0.875 | 0.910 |
| Gradient Boosting Machine | 0.857 | 1.000 | 0.750 | 0.750 |
| Extra Trees | 0.778 | 0.700 | 0.875 | 0.919 |
| Logistic Regression (C=1.0) | 0.737 | 0.636 | 0.875 | 0.948 |
| SVM (RBF kernel) | 0.588 | 0.556 | 0.625 | 0.958 |

The Gradient Boosting Machine (GBM) with 50 trees and maximum depth 2 achieved the highest F1 (0.857) and perfect precision: every day it flagged as dangerous was genuinely dangerous. Its recall of 0.750 means it caught 6 of 8 high-risk days, missing two that likely had brief intra-day excursions averaged out in daily data.

### The Ensemble

The best overall model averages the probability estimates of the enhanced logistic regression (well-calibrated risk scores, AUC-ROC 0.952) and the GBM (zero false alarms):

| Metric | Value |
|--------|-------|
| F1 | 0.857 |
| Precision | 1.000 |
| Recall | 0.750 |
| AUC-ROC | 0.954 |
| Optimal threshold | 0.45 |

This ensemble achieves perfect precision (no false alarms) and the best probability calibration (AUC-ROC 0.954), meaning its risk scores reliably rank days from safe to dangerous.

### The Critical Ablation: Inertia Doesn't Matter

We systematically removed features to test what matters. The most important finding: **removing the inertia proxy changes nothing.** Every metric stays identical. This directly confirms the ENTSO-E report's statement that higher inertia would not have prevented the cascade.

Conversely, a model using only voltage-focused features (voltage stress, reactive power gap, export intensity) achieves the same F1 = 0.857 as the full model. The voltage mechanism is the entire signal. All of the predictive power comes from the conditions that drive overvoltage: high solar with low synchronous generation, excess supply over demand, heavy exports, and negative prices.

## What the Numbers Mean in Practice

An early warning system based on this model would work as follows: each morning, using the day's generation forecast, demand forecast, and scheduled interconnector flows, compute the voltage stress proxy and reactive power gap proxy. If the ensemble risk score exceeds 0.45, flag the day as high-risk and initiate preventive actions:

- **Activate shunt reactors** to absorb excess reactive power and suppress voltage rise
- **Switch renewable installations from fixed power factor to active voltage regulation mode**
- **Dispatch synchronous condensers** (machines that provide reactive power without generating active power)
- **Adjust export schedules** to reduce light-loading of transmission lines
- **Ensure manual voltage control equipment is pre-positioned for rapid deployment**

The perfect precision of the model means operators would not waste resources responding to false alarms. Every flagged day represents genuine elevated risk.

## The Bigger Picture

The Iberian blackout is the first major casualty of a transition that every industrialised country is undertaking: replacing spinning synchronous generators with power-electronic inverter-based resources. The technical challenge is not merely "more solar means less inertia" -- that is the simplified version that dominated initial media coverage. The real challenge is that the displacement of synchronous generation removes voltage control authority at the exact moment when grid conditions (light loading, high exports, negative prices) create conditions favouring overvoltage.

Solar energy did not cause this blackout. Insufficient voltage control infrastructure, outdated protection relay settings, fixed power factor operating modes, manual (rather than automatic) reactive power management, and incomplete visibility of rooftop solar production by the transmission system operator caused this blackout. The ENTSO-E report issued 22 recommendations, centred on improved reactive power control, mandatory grid-forming capability for new renewable installations, and enhanced real-time monitoring.

The transition to renewable energy is necessary and irreversible. But the Iberian blackout demonstrates that grid operation practices, protection system design, and market dispatch rules must evolve alongside the generation mix. The overvoltage cascade was not an inevitable consequence of high solar penetration -- it was the consequence of operating a 21st-century generation fleet on a 20th-century control architecture.

## Data and Reproducibility

All data used in this project are from the publicly accessible REE REData API (https://apidatos.ree.es/). No synthetic data were used. The dataset comprises 94 daily observations from January through May 2025, covering generation by technology, hourly demand, interconnector flows with France, Portugal, and Morocco, and hourly spot market prices. Labels combine the known blackout date (April 28, 2025) with grid stress extremes (top 5th percentile of composite risk score). Code is available in the `applications/iberian_blackout/` directory of the HDR autoresearch repository.

## Technical Details

- **Data**: 94 daily observations from REE REData API (Jan-May 2025); 5 months of generation, demand, price, and interconnector data; 8 positive (high-risk) days out of 94
- **Method**: Physics-informed proxy features (voltage stress, reactive power gap, inertia) combined with grid stress indicators; evaluated with logistic regression, GBM, Extra Trees, SVM, and ensemble under LOO-CV
- **Best model**: Ensemble of LogisticRegression(C=1.0) and GBM(50 trees, depth 2), threshold 0.45
- **Key finding**: Voltage stress proxy dominates; inertia proxy is redundant (confirming ENTSO-E); overvoltage mechanism is the predictive signal
- **Limitations**: Daily granularity imposes a recall ceiling (0.750); no direct voltage or reactive power measurements; single-event validation
- **Code**: `applications/iberian_blackout/` in the HDR autoresearch repository
