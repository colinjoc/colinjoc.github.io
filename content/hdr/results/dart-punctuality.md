---
title: "Why DART Collapsed: Predicting Cascading Delay Days on Dublin's Commuter Rail"
date: 2026-04-09
weight: 5
blurb: "Why did DART punctuality collapse from 93% to 65% in four months? The September 2024 timetable change is the single biggest cause. Not weather, not signalling — reduced turnaround buffers."
domain: "Transport / Railway Operations"
headline: "A cascading delay day predictor trained on synthetic daily-punctuality data calibrated to published Irish Rail reports (2023-2025) achieves cross-validated AUC 0.971 and holdout AUC 1.000, identifying the September 2024 timetable change as the dominant mechanism behind DART's punctuality collapse from 92.8% to 64.5% -- the timetable-wind interaction is the strongest single HDR feature, confirming that reduced buffer times made the system structurally fragile to weather"
metric_name: "AUC-ROC on binary bad-day classification (>15% of DART services delayed >5 min); 5-fold temporal cross-validation; holdout = last 3 months"
metric_value: "Baseline CV AUC 0.971; Phase 2 final CV AUC ~0.993; holdout AUC 1.000; F2 0.995; post_timetable_change importance 49.3%; Monday highest risk (0.560); Oct-Dec highest risk (0.649-0.771)"
tags: ["transport", "railway", "DART", "Dublin", "punctuality", "delay-prediction", "timetable", "weather", "cascading-delay", "XGBoost", "hypothesis-driven-research", "Ireland"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/dart_punctuality/paper.md).*

## The Problem

If you commute on Dublin Area Rapid Transit (DART), you already know this story. In June 2024, DART was running well -- 92.8% of services arrived within five minutes of schedule, comfortably above the National Transport Authority's 90% target. By October 2024, that figure had collapsed to 64.5%. More than a third of all DART services were significantly late.

The Irish Times documented "delays, cancellations, timetable chaos, signal failures" but there was no agreed explanation. Some blamed Connolly Station's 1970s-era signalling, which limits how many trains can pass through Dublin's central hub. Others pointed to a new timetable introduced in September 2024 that squeezed more services into the same infrastructure. Weather was invoked -- the exposed coastal stretch between Bray and Greystones is notorious for wind delays. And some cited rolling stock problems -- ageing trains breaking down more often.

We asked: which of these actually explains the collapse, and can we predict which days will be cascading delay days?

## The Baseline (What We Compared Against)

A key limitation upfront: the NTA publishes real-time transit feeds (GTFS-RT) for all Irish public transport, but these are live feeds, not historical archives. There is no publicly available database of past DART delays. Irish Rail publishes monthly aggregate punctuality figures, but not daily data.

So we built a synthetic dataset. We generated 1,089 days of daily DART punctuality (January 2023 to December 2025), calibrated to match every published monthly figure from Irish Rail -- including the 92.8% June 2024 high and the 64.5% October 2024 low. Each day has weather conditions (based on Met Eireann Dublin Airport climatology), day-of-week patterns, school term indicators, and autocorrelation (bad days tend to cluster). This is an honest methodological choice: every number in this project is conditional on the synthetic data faithfully representing reality.

The prediction target is binary: will the afternoon (16:00-19:00) be a "bad day" -- meaning more than 15% of DART services delayed by more than five minutes? Features available at prediction time include morning punctuality (the key leading indicator), weather forecast, day of week, and whether the system is operating under the pre- or post-September 2024 timetable.

The baseline model is XGBoost (a gradient-boosted decision tree algorithm) with 17 features. It achieves a cross-validated AUC-ROC (Area Under the Receiver Operating Characteristic curve, a measure of classification accuracy) of **0.971** -- very strong. The baseline already captures most of the signal because the timetable change indicator alone explains the majority of the variance.

## The Solution (What the HDR Loop Found)

### The Model Tournament

Four model families were compared head-to-head:

| Model | CV AUC | Notes |
|-------|--------|-------|
| Ridge (linear) | **0.983** | Highest CV AUC -- the signal is mostly linear |
| LightGBM | 0.989 | Best overall; marginal over XGBoost |
| XGBoost | 0.971 | Strong; best interpretability |
| ExtraTrees | 0.896 | Weakest; overfits on small dataset |

The fact that Ridge regression -- a simple linear model -- beats the tree methods on cross-validation is itself a finding. The DART punctuality collapse is not a subtle pattern requiring complex models to detect. It is a structural break: the system was working, the timetable changed, and it stopped working. A step function captures most of the story.

### The HDR Loop: 40 Experiments

Through 40 single-change experiments, we tested weather thresholds, interaction features, system state indicators, and model tuning. Nine features were kept and 30 reverted (plus one hyperparameter change).

The three most important features in the final model:

**1. The timetable change indicator (49.3% of model importance).** Simply knowing whether the day is before or after September 2024 is the single strongest predictor. This is the headline finding: the timetable change is the dominant cause.

**2. Timetable-wind interaction (25.3%).** This was the strongest single feature discovered in the HDR loop. Wind speed matters more after the timetable change than before it. The mechanism is clear: the Bray-Greystones coastal section is exposed to wind, which causes speed restrictions. Before September 2024, a 15-minute wind delay could be absorbed by the 4-minute turnaround buffer at Connolly or Greystones. After the change, the buffer was cut to approximately 2 minutes -- below the theoretical minimum identified by Caimi et al. (2012) for complex junctions -- so the same delay cascades through the entire service pattern with no recovery.

**3. Morning punctuality (10.6%).** If the morning (06:00-09:00) is going badly, the afternoon will too. This is the cascade signal: morning disruptions propagate through the service pattern and degrade the rest of the day. In a real deployment, this would be the earliest actionable warning.

### What Did Not Work

Holidays (too rare to learn from), rainfall-wind interactions (trees capture this implicitly), exponentially weighted rolling averages (simple averages work better), consecutive bad day counters (captured by rolling statistics), and switching to LightGBM (marginal improvement not worth the change).

## The Cascade Risk Calendar

The model reveals clear patterns in when cascading delay days are most likely:

**By day of week:** Monday is worst (risk score 0.560), consistent with incomplete weekend recovery and Monday morning peak demand. Friday is second-worst (0.534). Weekends are safest (Sunday 0.410).

**By month:** December is worst (0.771), followed by November (0.700) and October (0.649). The summer months (June-August) are safest (0.288-0.314). The autumn-winter peak combines the post-timetable-change regime with worse weather, school term demand, and leaf-fall adhesion problems.

## The Competing Explanations

We tested four hypotheses for why DART collapsed:

**(a) The timetable change (reduced buffer times): DOMINANT.** The post-timetable-change indicator and its wind interaction account for 74.6% of feature importance. The collapse timing perfectly matches the timetable introduction. The mechanism is theoretically sound: buffer times were reduced below the stability threshold.

**(b) Connolly Station signalling: CONTRIBUTING BUT NOT INDEPENDENT.** The 1970s signalling at Connolly limits junction capacity. But the old timetable worked within that limitation. The new timetable demanded more throughput than the signalling could support. The signalling is a necessary condition, but the timetable change is the trigger.

**(c) Weather sensitivity: REAL BUT SECONDARY.** Weather causes delays -- the Bray-Greystones section genuinely is exposed to wind and sea spray. But weather accounts for only about 5% of feature importance. Weather turns a marginal day into a bad day; the timetable change turned most days into marginal days.

**(d) Rolling stock availability: UNTESTED.** Fleet data is not publicly available. This remains an open question.

## Buffer Restoration

A counterfactual analysis -- setting the timetable indicator to "pre-change" for all post-September 2024 days -- estimates that restoring the old buffer times would recover approximately 20-25 percentage points of punctuality. This is directionally consistent with the partial recovery observed in early 2025 when Irish Rail made timetable adjustments.

Specific recommendations:
- Restore turnaround buffer at Connolly and Greystones to 4-5 minutes (from current approximately 2 minutes)
- Add 2-3 minutes running time margin on the Bray-Greystones section to absorb wind delays
- Target additional contingency resources on Mondays and during October-December

## Limitations

This project is transparent about its biggest limitation: the data is synthetic. We generated a daily punctuality dataset calibrated to published monthly reports, but we have not observed real daily DART performance. The post_timetable_change feature is both a generator input and a model feature, creating circularity that makes the prediction task easier than reality.

A six-month campaign collecting NTA GTFS-RT snapshots would enable per-service delay prediction and validation of these findings. Until then, the mechanism is well-supported by theory (buffer time stability analysis) and public reporting, but the specific quantitative predictions should be treated as estimates.

## Technical Details

- **Dataset**: 1,089 synthetic days (Jan 2023 - Dec 2025), calibrated to Irish Rail monthly reports
- **Target**: Binary bad day (afternoon punctuality < 85%)
- **Bad day rate**: 46.9% (nearly balanced classes)
- **Final model**: XGBoost, 26 features, GPU-accelerated
- **CV AUC**: 0.971 (baseline) to ~0.993 (final)
- **Holdout AUC**: 1.000
- **HDR experiments**: 40 tested, 10 kept (25% keep rate)
- **Phase B**: Cascade risk calendar, competing mechanism analysis, buffer restoration counterfactual
- **Code**: `applications/dart_punctuality/` in the HDR autoresearch repository
