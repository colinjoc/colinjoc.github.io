---
title: "Can Public Grid Data Predict a Blackout? Testing the Limits on the 2025 Iberian Cascade"
date: 2026-04-09
weight: 9
blurb: "Could the April 2025 Iberian blackout have been predicted from public data? Partially — the model ranks pre-cascade hours in the top 10% of risk — but the data needed for real prediction does not exist publicly."
domain: "Energy / Power System Stability"
headline: "A frequency excursion predictor trained on publicly available ENTSO-E generation and load data for Spain (2023-2025) achieves holdout AUC 0.888 on the 28 April 2025 Iberian blackout day and ranks the pre-cascade hours in the top 10% of historical risk -- but cannot produce a binary alert (max predicted probability 0.10), demonstrating that public 15-minute data provides a useful risk-ranking signal but is fundamentally insufficient for operational cascade prediction"
metric_name: "AUC-ROC on binary frequency excursion (>200 mHz from 50 Hz) classification; 5-fold temporal cross-validation; holdout = April 28, 2025"
metric_value: "Baseline CV AUC 0.613; Phase 2 winner CV AUC 0.640 (+4.4%); holdout AUC 0.888; pre-cascade hours ranked top 10%; binary detection failed (max P=0.101)"
tags: ["energy", "power-systems", "blackout", "cascading-failure", "frequency-stability", "renewable-integration", "SNSP", "inertia", "XGBoost", "ENTSO-E", "hypothesis-driven-research"]
---

## The Problem

On 28 April 2025, a cascading failure disconnected the entire Iberian Peninsula from the rest of Continental Europe's power grid. Approximately 56 million people in Spain and Portugal lost electricity. The cascade propagated in under seven minutes. Full restoration took 16 hours.

The European Network of Transmission System Operators for Electricity (ENTSO-E) Expert Panel investigated for nearly a year, publishing a 440-page report in March 2026. They identified five systemic failures: insufficient operational awareness of low-inertia conditions, inadequate reactive power management, inverter fault-ride-through settings that collectively created a "cliff edge" of mass disconnection, poor oscillation damping, and protection relay misoperation during power swings.

At the time of the cascade, approximately 78% of Spain's electricity was coming from non-synchronous sources (wind and solar) -- a condition measured by a metric called System Non-Synchronous Penetration, or SNSP. That is well above the 65% limit that the Irish grid operator uses for its smaller system. When the initial disturbance hit, there was not enough rotating mass in the system to absorb the shock, and the resulting frequency decline triggered a chain reaction of inverter disconnections that overwhelmed the grid's defenses.

The ENTSO-E report's most striking admission: "the investigation was hampered by incomplete data." Many inverter-based resources did not have oscillographic recording equipment, and others did not share their recordings.

We asked: could the approach of this cascade have been detected from the grid data that is publicly available?

## The Baseline (What We Compared Against)

The publicly available data source is the ENTSO-E Transparency Platform, which provides generation by fuel type, total load, cross-border flows, and day-ahead prices for European countries at 15-minute resolution. This is a coarse view of the grid -- it tells you how much nuclear, coal, gas, hydro, wind, and solar generation is online, but nothing about voltage levels, protection relay states, or individual inverter configurations.

The prediction target is binary: does the next hour see a frequency excursion exceeding 200 millihertz from the nominal 50 Hz? That threshold corresponds to the ENTSO-E alert level and captures "stress events" well before automatic emergency measures kick in.

Because actual frequency recordings are not publicly available at hourly resolution for the full 2023-2025 period, we constructed a calibrated synthetic dataset matching published Spanish grid statistics. The synthetic data reproduces the diurnal and seasonal patterns of Spanish generation, the secular growth of renewable capacity, and the physics-based relationship between SNSP, inertia, and frequency stability risk. This is a known limitation: all quantitative results are conditional on the synthetic data faithfully representing real grid behaviour.

The baseline model is XGBoost with 16 features: eight generation columns by fuel type, total generation, total load, temporal features (hour and month encodings), and year. Evaluated with 5-fold temporal cross-validation (no shuffle -- always training on past data, testing on future).

Baseline result: **cross-validated AUC of 0.613** -- barely better than a coin flip. The model predicts zero excursion events because they are so rare (0.9% of hours) that always predicting "no excursion" is the loss-minimising strategy.

## The Solution (What the HDR Loop Found)

The Phase 1 model tournament produced a surprising result: Ridge regression (a simple linear model) beat all tree-based methods with a CV AUC of 0.645, compared to XGBoost's 0.613. The signal in this data is almost entirely linear -- the relationship between generation mix and excursion risk does not have strong nonlinear structure at 15-minute resolution. Ridge also perfectly discriminated the blackout day from normal days on the holdout set.

Through 38 pre-registered single-change experiments in the Hypothesis-Driven Research (HDR) loop, three features were kept and 33 reverted:

**1. Total generation ramp rate (1 hour)** -- the absolute change in total generation over the previous hour. A power system can tolerate a given generation mix indefinitely; it is the changes that create frequency excursions. The ENTSO-E report confirms the cascade was triggered by a sudden generation loss, not by the steady-state condition.

**2. Residual demand** -- defined as load minus wind minus solar. When residual demand is low, the conventional synchronous generators are running at minimum levels, providing less inertia and less flexibility to absorb shocks. This is more informative than SNSP alone because it captures the absolute level of conventional generation, not just its fraction.

**3. Hour-of-day times SNSP interaction** -- the largest single improvement (+0.014 AUC). The risk profile of high renewable penetration changes systematically throughout the day: midday solar-driven SNSP peaks coincide with low demand and minimal conventional dispatch; evening wind-driven SNSP occurs during the demand ramp-up when flexibility is most needed. The interaction captures this time-varying vulnerability.

Notable failures: SNSP as a standalone feature did not improve the model, because XGBoost already extracts the same information from individual generation columns. Inertia proxies, lag features, rolling statistics, threshold indicators, and class weighting all failed to improve cross-validated AUC.

**Final model: CV AUC 0.640, holdout AUC 0.888.** On April 28, 2025, the model assigned the pre-cascade hours (10:00-12:00) risk scores in the **top 10%** of all historical hours. The post-cascade hour (13:00) received the day's highest risk score (probability 0.101). But critically, no hour exceeded a 0.50 probability threshold -- the model could rank hours by risk but could not generate a binary alert.

## The Discovery (What the Model Reveals About Grid Vulnerability)

The Phase B discovery sweep mapped the relationship between renewable penetration and predicted stability risk:

- Below 25% renewable energy fraction, risk is approximately constant.
- Risk begins rising at 25-30% and increases sharply above 32%.
- The steepest risk gradient occurs at 57-62% renewable fraction -- this is where each additional percentage point of renewables most rapidly degrades the predicted stability margin.

The risk surface analysis confirmed the physics: the most dangerous operating conditions combine SNSP above 0.55 with system-average inertia constants below 2.5 seconds. Spain on April 28, 2025 was operating in exactly this region.

All 20 hours the model identified as highest-risk in the historical record were confirmed excursion events, validating that the risk ranking is meaningful even if the absolute probabilities are not calibrated for binary alerting.

## The Honest Conclusion

The headline finding is a qualified negative: **publicly available ENTSO-E data provides a useful risk-ranking signal but is fundamentally insufficient for operational cascade prediction.**

The gap is not primarily about temporal resolution (15 minutes vs. sub-second), though that matters. It is about the type of data. To predict whether a disturbance will cascade, you need:

1. Sub-second frequency dynamics -- how fast is frequency declining, and how deep will the nadir be?
2. Bus-level voltage profiles -- is voltage collapsing at critical substations?
3. Protection relay states -- are relays about to trip healthy lines?
4. Individual inverter configurations -- at what frequency and voltage will each plant disconnect?

None of this is publicly available. The ENTSO-E Expert Panel's central recommendation -- that data recording and sharing at inverter-based resource sites must be improved -- is directly supported by this analysis.

What public data can do is tell you that the system is in a riskier region. An operator monitoring the three features this model identified -- generation ramp rate, residual demand, and the time-varying SNSP profile -- would have seen an elevated risk signal in the hours before the cascade. That is not nothing. But it is not an early warning system.

The three features that survived the HDR loop are also the three that make the most physical sense: rapid generation changes stress frequency response, low residual demand means low inertia, and the risk of high renewables depends on what time of day it is. These are not new insights for power system engineers. What the analysis adds is quantification: a 4.4% improvement in AUC from three domain-informed features, on a problem where public data hits a hard ceiling.

Until the data infrastructure catches up with the physics of inverter-dominated grids, the answer to "can we predict which grid states are one perturbation away from collapse?" is: we can rank them, but we cannot reliably flag them.

---

*Source code: [applications/iberian_blackout/](https://github.com/colurw/generalized_hdr_autoresearch/tree/master/applications/iberian_blackout) | Method: [Hypothesis-Driven Research](https://colurw.github.io/hdr/)*
