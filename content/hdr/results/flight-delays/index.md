---
title: "How one late morning flight can derail ten more"
date: 2026-04-11
domain: "Transport / Aviation Operations"
blurb: "The gate agent says the inbound aircraft is running late. That's the polite version. In the worst case, it's the start of a ten-flight cascade."
weight: 27
tags: ["transport", "aviation", "flight-delays", "delay-propagation", "network-analysis", "airline-scheduling", "United-States"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/flight_delays/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Tracked by tail number through six months of US domestic aviation, the same aircraft flying multiple legs per day is the single biggest source of flight delay — bigger than weather, air traffic control, or airline operations. Morning flights arrive two minutes early on average. By 7 PM the average flight is 17 minutes late. The cycle resets overnight and starts again.

## The question

Every frequent flyer has heard the gate agent explain that the inbound aircraft is running late. Your flight to Denver cannot leave until the plane arrives from Atlanta, the passengers deplane, the cabin is cleaned, and your group boards. If the plane was 40 minutes late and the airline only scheduled a 45-minute turnaround, you are almost certainly going to be late too. And if that plane has two more flights tonight, so are those passengers.

How far does this actually ripple? When a morning flight is delayed, how many subsequent flights on the same aircraft are affected? What decides whether a delay is absorbed or spreads? Are some routes, airports, or airlines more contagious than others?

## What we found

We reconstructed the daily flight chains for 3.4 million flights over six months by tracking each aircraft's Federal Aviation Administration tail number through its sequence of legs. Aircraft rotation — the fact that the same physical airplane flies multiple flights per day — accounts for 41 percent of all airline-reported delay minutes. That is more than operational issues (33 percent), air traffic control (20 percent), or weather (7 percent).

- Half of initial delays are contained immediately. When the first flight of the day is late, there is roughly a 50-50 chance the next flight still departs on time, because the airline built enough buffer into the schedule.
- The other half propagate, sometimes deeply. The average cascade affects two additional flights. In the worst observed case, a single delayed morning flight caused ten subsequent flights on the same aircraft to arrive late.
- Delays build through the day. Morning flights before 9 AM arrive two minutes early on average, thanks to a clean overnight reset. By 7 PM, the average flight is 17 minutes late. The system resets overnight and the cycle repeats.
- Two complementary signals drive the prediction. Current airport congestion — how delayed other flights at your origin and destination are right now — accounts for about 47 percent of the model's predictive power. The aircraft's own rotation history accounts for about 28 percent. Neither alone is enough.
- Dallas/Fort Worth is the most contagious node in the network. It ranks first on both delay propagation risk and number of routes connected, appearing in four of the ten most delay-prone corridors. Miami, Fort Lauderdale, Orlando, and San Francisco round out the top five.

## Why that matters

Most published models for flight delay treat each flight as an independent event, ignoring what happened to the aircraft earlier that day. The implicit assumption is that delays are primarily caused by weather, air traffic control, or airline operations at the moment of departure. The data says otherwise. Aircraft rotation — the carry-forward of delay from one leg to the next — is the single largest cause category, larger than any of the others individually.

The shape of the signal is also striking. A simple linear model using only airport congestion and rotation features already captures most of the predictive power. Fancier tree-based models add only a modest improvement, primarily by picking up interaction effects like a large incoming delay combined with a short scheduled turnaround. The core physics of delay propagation — current delay is roughly proportional to previous delay, softened by buffer and congestion — is largely linear.

## What it means in practice

**For passengers.** Book the first flight of the day. It has no rotation history to inherit, and morning flights arrive two minutes early on average. Avoid late-afternoon connections through major hubs, especially Dallas/Fort Worth and the Florida airports, where cascade risk peaks. If you must connect in the afternoon, prefer airlines with longer scheduled turnarounds.

**For airlines.** The finding is consistent with what operations researchers have argued for over a decade: schedule padding works. Prior simulation studies estimated that adding just five minutes to turnaround times at the busiest airports would reduce total propagated delay by 15 to 20 percent. Our data confirms the association at scale — carriers with turnarounds above 150 minutes show substantially lower propagation rates, though route mix and fleet composition also contribute.

**For regulators and hub operators.** The dominance of Dallas/Fort Worth as a contagion node is a network-level problem no individual airline can fix. Coordinated slot management and extra buffer at the most contagious hubs would benefit every carrier operating through them.

## How we did it

We used six months of real data (January through June 2024, 3.4 million flights across 15 carriers and roughly 350 airports) from the [Bureau of Transportation Statistics On-Time Performance database](https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ), which collects mandatory reports from every US carrier with significant domestic traffic. We reconstructed aircraft rotation chains from tail numbers, engineered 29 features capturing rotation history, airport congestion, carrier buffer strategy, and temporal patterns, and evaluated four model families with strict train-on-the-past, test-on-the-future validation using [scikit-learn](https://scikit-learn.org/) and tree-based gradient boosting. Feature attribution uses Shapley-value-based explanations for unbiased importance estimates.

## Further reading

- Beatty R et al. "Preliminary evaluation of flight delay propagation through an airline schedule." *Air Traffic Control Quarterly* (1999). [doi:10.2514/atcq.7.4.285](https://doi.org/10.2514/atcq.7.4.285) — the first quantification of rotation-caused delays at 30-40 percent.
- AhmadBeygi S et al. "Analysis of the potential for delay propagation in passenger airline networks." *Journal of Air Transport Management* (2008). [doi:10.1287/trsc.1070.0207](https://doi.org/10.1287/trsc.1070.0207) — traced delay propagation trees finding cascades of 4 to 7 flights from a single root.
- Fleurquin P et al. "Systemic delay propagation in the US airport network." *Scientific Reports* (2013). [doi:10.1038/srep01159](https://doi.org/10.1038/srep01159) — epidemic spreading model identifying super-spreader hubs.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/flight_delays/paper.md).
