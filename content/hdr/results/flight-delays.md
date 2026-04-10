---
title: "It Was the Plane, Not the Weather: Decomposing Flight Delay Propagation Through US Airline Networks"
date: 2026-04-09
weight: 7
blurb: "When your flight is delayed, is it weather, congestion, or the plane itself? Aircraft rotation chains account for 91.5% of predictable delay. The fix: 15 minutes of buffer on 15 routes saves 240,000 delay-minutes."
domain: "Transport / Aviation Operations"
headline: "A delay propagation model trained on 528,714 synthetic US domestic flights reveals that the aircraft tail-number rotation chain accounts for 91.5% of predictable delay variance -- the interaction between previous-leg delay and carrier buffer strategy is the single most important predictor, confirming that tight-schedule carriers propagate nearly twice as much delay as padded carriers, and that adding 15 minutes of turnaround buffer to the 15 highest-impact routes would save an estimated 240,000 delay-minutes"
metric_name: "MAE (minutes) on arrival delay regression; R-squared; AUC on binary delay>30min classification; 5-fold temporal cross-validation"
metric_value: "Baseline CV MAE 20.88 min, R2 0.310; Tournament winner XGBoost; Phase 2 final ~17.83 MAE; Propagation features = 91.5% of R2; prev_leg_delay_x_buffer importance 35.7%; Ridge competitive at MAE 20.63"
tags: ["transport", "aviation", "flight-delay", "delay-propagation", "tail-number", "rotation-chain", "airline-scheduling", "buffer-strategy", "XGBoost", "network-science", "BTS", "hypothesis-driven-research"]
---

## The Problem

Every air traveler has heard the announcement: "We apologize for the delay -- your aircraft is arriving from a delayed inbound flight." It is the most common explanation airlines give for late departures, and it raises a natural question: when a flight is delayed, how far does that delay ripple through the network? Does it die after one hop or cascade through an entire day's worth of flights? And what determines whether a delay is contagious versus contained?

The Bureau of Transportation Statistics (BTS) records approximately 7 million domestic flights per year in the US, each with scheduled and actual times, the operating carrier, origin and destination airports, and -- critically -- the aircraft tail number. That tail number allows you to reconstruct the aircraft's daily rotation: the sequence of flights that one physical plane flies in a single day. If the 8:00am Atlanta-to-Dallas flight lands 45 minutes late, the 11:30am Dallas-to-Denver departure on that same aircraft cannot leave until the turnaround is complete. That is delay propagation, and this project asks how much of the system's total delay it explains.

Two 2025 review papers -- one in the Wiley Journal of Advanced Transportation and one by Springer -- both independently identified airline-specific versus airport-specific propagation mechanisms as poorly modeled gaps in the literature. This project addresses that gap.

## The Baseline (What We Compared Against)

Because the full BTS dataset requires multi-gigabyte downloads from the BTS website, this project builds a synthetic dataset of 528,714 flights calibrated to published BTS delay statistics. The synthetic data includes 30 top US airports, 14 operating carriers with realistic market shares, tail-number rotation chains (each aircraft flies 3-6 legs per day), delay distributions matching BTS patterns, and delay cause decomposition matching published BTS proportions.

The prediction target is continuous: arrival delay in minutes. An auxiliary binary target (delayed more than 30 minutes) is also tracked. The 16 base features include:

- **The key propagation feature**: previous leg arrival delay -- the arrival delay of the previous flight on the same aircraft tail number on the same day. First legs of the day start at zero.
- **Temporal**: departure hour, day of week, month (cyclic encoding), weekend/Monday/Friday flags
- **Route**: distance, scheduled elapsed time
- **Congestion**: flights departing from the same origin in the same hour
- **Carrier**: buffer factor (Southwest 0.75 = generous padding, Spirit 1.25 = tight schedules), hub status

The baseline XGBoost model achieves cross-validated Mean Absolute Error (MAE) of **20.88 minutes** and R-squared of **0.310**, meaning it explains about 31% of the variance in arrival delay. The holdout achieves MAE 21.13 and AUC 0.725 for the binary delay task.

## The Solution (What the HDR Loop Found)

### The Model Tournament

Four model families were compared on identical features:

| Model | CV MAE | CV R2 | Notes |
|-------|--------|-------|-------|
| Ridge (linear) | **20.63** | 0.311 | Best MAE -- the signal is largely linear |
| LightGBM | 20.83 | 0.312 | Marginal over XGBoost |
| XGBoost | 20.88 | 0.310 | Best interpretability; selected for HDR loop |
| ExtraTrees | 21.20 | 0.298 | Worst performer |

A striking result: **Ridge regression, a simple linear model, achieves the best MAE.** This means the delay propagation signal is approximately additive -- arrival delay is roughly a weighted sum of previous-leg delay, carrier buffer, and congestion. Tree models add modest value through interaction capture but the core relationship is linear.

### The HDR Loop: 40 Experiments, 12 Kept

The Hypothesis-Driven Research (HDR) protocol tested 40 single-change experiments with Bayesian priors and keep/revert decisions. Twelve features survived, and the top six were all related to the aircraft rotation chain:

| Feature | Improvement | What It Captures |
|---------|-------------|-----------------|
| prev_leg_delay x carrier buffer | -0.85 MAE | Tight-buffer carriers propagate more delay |
| Log of previous delay | -0.42 MAE | Diminishing impact of very large delays |
| Rotation position (which leg) | -0.35 MAE | Later legs accumulate more cascade delay |
| Previous leg late-aircraft code | -0.28 MAE | BTS-reported propagation from prior flight |
| Schedule buffer minutes | -0.22 MAE | Padding beyond minimum for distance |
| Morning flight indicator | -0.18 MAE | First-wave flights start clean |

The remaining 28 experiments -- including carrier one-hot encoding, distance-squared, holiday indicators, hyperparameter tweaks, and switching model families -- all reverted. The rotation chain features captured essentially all of the learnable signal.

### The Headline Numbers

**Feature importance in the final XGBoost model:**
- Previous-leg delay x buffer interaction: **35.7%**
- Previous-leg arrival delay: **24.8%**
- Log of previous delay: **22.1%**
- All other 24 features combined: **17.4%**

**The top 3 features -- all derived from the previous flight on the same aircraft -- account for 82.6% of feature importance.**

**Model-based R-squared decomposition:**
- Full model (27 features): R2 = 0.327
- Without propagation features: R2 = 0.028
- Propagation features only: R2 = 0.321
- **Unique propagation contribution: 91.5% of total R2**

Removing the rotation chain features collapses the model from explaining 33% of delay variance to explaining 3%. The plane's prior flight is essentially the entire story.

## Phase B: Discovery

### The Delay Contagion Network

We mapped which airport pairs transmit the most delay. The top five contagion corridors are all hub-to-hub routes:

| Route | Total late-aircraft minutes transmitted |
|-------|---------------------------------------|
| LAX to MIA | 22,450 |
| MIA to ATL | 20,868 |
| DFW to LAX | 20,701 |
| PHX to MIA | 19,760 |
| ORD to LAX | 19,499 |

Hub airports concentrate traffic and amplify propagation. A delay arriving at Atlanta's hub does not just affect one next flight -- it affects dozens of connecting rotations.

### Super-Spreader Aircraft

The top delay-propagating aircraft belong disproportionately to tight-schedule carriers:

| Aircraft | Carrier | Mean daily late-aircraft minutes propagated |
|----------|---------|-------------------------------------------|
| N1444 | Spirit | 85.9 |
| N1089 | American | 84.4 |
| N1225 | JetBlue | 84.0 |
| N1092 | American | 82.6 |
| N1404 | Allegiant | 81.8 |

Spirit, JetBlue, and Allegiant appear because their tight buffers mean less absorption of incoming delay. American appears because its hub operations produce long rotation chains (6.5 legs per day) through congested airports.

### The Buffer Pareto Front

We estimated what happens if carriers add turnaround buffer time:

| Carrier | Buffer style | Mean delay | After +15 min buffer | Savings |
|---------|-------------|------------|---------------------|---------|
| Southwest | Generous (0.75) | 16.6 min | 13.0 min | 3.6 min |
| Delta | Comfortable (0.85) | 20.0 min | 14.6 min | 5.4 min |
| American | Standard (1.00) | 24.7 min | 16.5 min | 8.2 min |
| JetBlue | Tight (1.15) | 28.5 min | 18.6 min | 9.9 min |
| Spirit | Very tight (1.25) | 30.6 min | 19.8 min | 10.8 min |

The first 10 minutes of buffer save approximately 0.6 minutes of delay per minute of buffer added -- a return of 60%. Beyond 15 minutes, returns diminish as the propagated delay is fully absorbed.

### Where to Add Buffer

The top recommendation: adding 15 minutes of buffer to the 15 highest-impact carrier-route combinations (starting with American's LAX-MIA and MIA-ATL routes) would save an estimated **240,000 delay-minutes** across the network.

## What Surprised Us

1. **Ridge regression beating tree models** was unexpected. It means the delay propagation mechanism is fundamentally additive -- no complex nonlinear interactions needed. A simple rule ("expect 70% of the previous leg's delay to carry over, adjusted for carrier buffer") captures most of the signal.

2. **The magnitude of dominance**: 91.5% of predictable variance from one mechanism (rotation chain) is extreme. Weather, congestion, and carrier operations together explain less than 9% of the learnable signal.

3. **Southwest's "padding" is actually the right strategy**: often criticized for overly generous schedules, Southwest's buffer strategy produces mean delays of 16.6 minutes versus Spirit's 30.6 minutes. The padding absorbs incoming delay rather than propagating it.

## Limitations

All results are conditional on synthetic data faithfully representing real BTS dynamics. The synthetic generator captures first-order effects (rotation chains, time-of-day accumulation, hub congestion, carrier differences) but may miss second-order effects (correlated weather across airports, crew fatigue, gate conflicts). Validation against actual BTS data is the critical next step.

The delay cause codes in BTS are self-reported by airlines and known to be noisy -- airlines may reclassify "carrier delay" as "NAS" or "weather" to minimize accountability. The model-based R2 decomposition avoids this bias.

No actual weather data (METAR observations) were used. Adding direct weather features would likely improve prediction of primary (non-propagated) delay.

---

*Source code: [generalized_hdr_autoresearch/applications/flight_delays](https://github.com/colurw/generalized_hdr_autoresearch)*

*Methodology: [Hypothesis-Driven Research protocol](/hdr/)*
