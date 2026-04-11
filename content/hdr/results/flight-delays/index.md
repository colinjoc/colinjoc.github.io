---
title: "When Your Flight Is Late, How Far Does the Delay Ripple?"
date: 2026-04-10
weight: 7
blurb: "We tracked 3.4 million US domestic flights through their aircraft rotation chains and found that airport congestion and an aircraft's incoming delay jointly determine whether a delay spreads or dies. A single delayed morning flight can cascade through up to ten subsequent flights on the same aircraft."
domain: "Transport / Aviation Operations"
tags: ["transport", "aviation", "flight-delays", "delay-propagation", "BTS", "tail-number", "rotation-chain", "airline-scheduling", "network-analysis", "United-States"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/flight_delays/paper.md).*

## The Question

Every frequent flyer knows the drill. You arrive at the gate, the departure board shows a delay, and the gate agent announces that "the inbound aircraft is running late." Your flight to Denver cannot leave until the plane arrives from Atlanta, the passengers get off, the cabin is cleaned, and your group boards. If the plane was 40 minutes late from Atlanta, and the airline only scheduled a 45-minute turnaround, you are almost certainly going to be late too. And if the plane has two more flights after yours tonight, so are those passengers.

We wanted to know: how far does this actually ripple? When a morning flight is delayed, how many subsequent flights on the same aircraft are affected? What determines whether a delay is absorbed or amplified? And are some routes, airports, or airlines more contagious than others?

## What We Found

We reconstructed the rotation chains for 3.4 million flights over six months (January through June 2024) by tracking each aircraft's FAA tail number through its daily sequence of flights. Aircraft rotation -- the fact that the same physical airplane flies multiple flights per day -- accounts for 41 percent of all airline-reported delay minutes, more than operational issues (33 percent), air traffic control congestion (20 percent), or weather (7 percent).

The results are striking:

- **Half of all initial delays are contained immediately.** If the first flight of the day is late, there is a 50-50 chance the second flight departs on time anyway, because the airline built enough buffer into the schedule.
- **The other half propagate.** Among delays that do spread, the average cascade affects two additional flights. In extreme cases, a single delayed morning flight in January 2024 caused ten subsequent flights on the same aircraft to arrive late.
- **Delays accumulate relentlessly through the day.** Morning flights (before 9 AM) arrive an average of two minutes early, because the aircraft starts from a clean overnight reset. By 7 PM, the average flight is 17 minutes late. The cascade resets overnight.

![Delays accumulate through the day, from near-zero at 6 AM to a peak of +17 minutes by 7 PM](plots/hourly_delay_accumulation.png)

## Two Signals, Not One

A machine learning model trained to predict whether any given flight will arrive more than 15 minutes late (AUC 0.92, well-calibrated and stable across months) reveals that delay prediction depends on two complementary signals, not one.

The first signal is **what is happening at the airports right now**. Destination airport arrival delay, origin departure delay, and taxi-out time are the top three most important features by SHAP analysis, collectively accounting for about 47 percent of the model's predictive power. If the airports at both ends of your route are running smoothly, your flight is unlikely to be late regardless of aircraft history.

The second signal is **what happened to this specific aircraft earlier today**. Turnaround time, the delay-buffer interaction, and buffer-over-minimum are the top rotation features, accounting for about 28 percent. A plane arriving 30 minutes late from its previous flight, at an airline with a 40-minute turnaround, is almost certain to depart late. The same plane at an airline with a 90-minute turnaround has time to recover.

Neither signal alone is sufficient. First-flight-of-the-day passengers (who have no aircraft rotation history to inherit) still face a delay risk that the model predicts with an AUC of 0.88 using only airport and temporal features. But for later flights, adding rotation history pushes that to 0.93.

![How far delays cascade: half are contained, but some ripple through 7 to 10 subsequent flights](plots/propagation_depth.png)

## The Super-Spreaders

Not all routes are equal. Some corridors consistently propagate more delay than others. We ranked routes by a propagation risk score that combines delay frequency, the magnitude of rotation-caused delay, and traffic volume. The top super-spreader routes are hub-to-hub corridors: San Francisco to Las Vegas, Tampa to Dallas/Fort Worth, Orlando to Dallas/Fort Worth.

Dallas/Fort Worth appears in four of the top ten most contagious routes and ranks first among all airports on both delay propagation risk and network degree centrality (the number of routes it connects). It is both the most connected airport and the one where delays are most contagious -- a combination that amplifies its system-wide impact. Miami, Fort Lauderdale, Orlando, and San Francisco round out the top five propagation hubs.

![Airlines with more turnaround buffer propagate less delay](plots/carrier_propagation.png)

## What It Means

For passengers, the practical advice is straightforward. Book the first flight of the day -- it has no rotation history to inherit, and the data shows morning flights arrive two minutes early on average. Avoid late-afternoon connections through major hubs, especially Dallas/Fort Worth and the Florida airports, where cascade risk peaks. If you must connect, prefer airlines with longer scheduled turnarounds.

For airlines, the finding is consistent with what operations researchers have argued for over a decade: schedule padding is an effective tool for controlling delay propagation. Adding five minutes to turnaround times at the busiest airports has been estimated (via simulation) to reduce total propagated delay by 15 to 20 percent. Our data shows that carriers with turnarounds above 150 minutes have substantially lower late-aircraft delay per flight, though other factors like route mix and fleet composition also contribute.

## How We Did It

We used six months of real data (January through June 2024) from the Bureau of Transportation Statistics (BTS) On-Time Performance database, which collects mandatory reports from every US carrier with significant domestic traffic. The dataset contains 3.4 million flights across 15 carriers and approximately 350 airports. We reconstructed aircraft rotation chains from tail numbers, engineered 29 features capturing rotation history, airport congestion, carrier buffer strategy, and temporal patterns, and trained an XGBoost classifier with strict temporal cross-validation (always train on the past, test on the future). The model achieves AUC 0.923 (cross-validation) and 0.920 (holdout month), with a Brier score of 0.074 and expected calibration error of 0.009. Feature attribution uses SHAP TreeExplainer for unbiased importance estimates. Full details, including all code, SHAP analysis, and reproducibility instructions, are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/flight_delays).

## Further Reading

- [Full technical paper with methodology and results](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/flight_delays/paper.md)
- [BTS On-Time Performance Data](https://www.transtats.bts.gov/) -- the public data source
- Beatty et al. (1999) -- first quantification of rotation-caused delays
- AhmadBeygi et al. (2008) -- delay propagation through rotation chains
- Fleurquin et al. (2013) -- epidemic spreading model for airport delay networks
- Lundberg and Lee (2017) -- SHAP values for model interpretation
