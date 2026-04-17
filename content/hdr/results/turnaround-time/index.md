---
title: "Flights Arriving Late Actually Turn Around Faster"
date: 2026-04-12
domain: "Transport / Aviation Operations"
blurb: "We tracked 2.5 million aircraft turnarounds and found that the airline's own schedule -- not ground crew speed -- explains most of the variability. Even more surprising: planes arriving late spend less time on the ground, because crews rush to recover the delay. The effect only breaks down when flights are extremely late."
weight: 29
tags: ["transport", "aviation", "turnaround-time", "ground-operations", "airline-scheduling", "tail-number-tracking", "United-States"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/turnaround_time/paper.md).*

## The Question

Every frequent flyer has sat at a gate watching ground crews work against the clock. Turnaround -- the time an airplane spends on the ground between arriving from one flight and departing on the next -- involves deplaning, cleaning, catering, fueling, boarding, and pushback. Airlines schedule buffer time for all of this, but the actual turnaround varies wildly. The same aircraft type at the same airport can turn around in 32 minutes one day and 71 minutes on another.

We wanted to know: what determines whether a turnaround is fast or slow? Is the bottleneck cleaning, fueling, catering, crew changes, or gate conflicts? And does a delayed inbound flight make things worse -- or force the crew to work faster?

## What We Found

The airline's own schedule overwhelms everything else. By tracking each aircraft's Federal Aviation Administration tail number through consecutive flights at the same airport, we reconstructed 2.5 million turnaround events from 3.4 million US domestic flights over six months of real data from the [Bureau of Transportation Statistics](https://www.transtats.bts.gov/).

{{< figure src="turnaround_distribution.png" caption="Distribution of 2.5 million turnaround times (left) and the relationship between scheduled and actual turnaround (right). The median turnaround is 63 minutes, but the distribution has a long right tail extending past 300 minutes." >}}

- **The schedule is the mechanism.** How much time the airline puts between the arrival of one flight and the departure of the next accounts for roughly four-fifths of the predictive model's power. Most turnaround variability is not random -- it is baked into the timetable.
- **Delayed flights turn around faster, not slower.** Flights arriving 30 to 60 minutes late spend an average of 67 minutes on the ground, compared to 89 minutes for flights arriving early. Ground crews compress operations when running behind. But the effect reverses for extreme delays beyond two hours, where turnarounds expand again as recovery becomes impossible.
- **Southwest turns planes nearly twice as fast as legacy carriers.** Southwest averages 62 minutes per turnaround; United and American average 103-104 minutes. The gap widens further at specific airports.
- **Morning turnarounds are longer than evening ones -- not because morning crews are slower, but because airlines front-load scheduling slack early in the day and compress it later.** An aircraft arriving at 7 AM sits for nearly two hours on average; by 5 PM that drops to 70 minutes.
- **Weekday turnarounds barely differ from each other.** Saturdays are the slowest day (about 89 minutes on average) and Fridays the fastest (about 81 minutes), but the spread across the whole week is only about 10 percent.

{{< figure src="inbound_delay_effect.png" caption="The rush effect: flights arriving late have shorter turnarounds as ground crews compress operations. The effect reverses for extreme delays (>120 minutes) where recovery becomes impossible." >}}

## Why That's Surprising

Conventional wisdom -- and recent academic literature -- focuses on delay propagation: a late inbound aircraft should cause a late outbound because there is less time for ground operations. One recent preprint (arXiv 2601.00875, 2025) even identified whether the previous user of the same gate was delayed as a dominant predictor of turnaround variability.

The data tells a different story. Late arrivals are associated with *shorter* turnarounds, not longer ones. Ground crews clearly adapt their pace to the situation. When a plane lands late, the pressure to recover pushes crews to work faster. This "rush effect" persists even after controlling for time of day, ruling out the possibility that it is just a quirk of evening schedules being tighter.

Meanwhile, the overwhelming dominance of the scheduled buffer suggests that most of the variation people notice is not operational chaos -- it is deliberate timetable design. Airlines choose to give some flights generous buffers and others razor-thin ones. That single scheduling decision explains more than all weather, congestion, crew, and equipment factors combined.

{{< figure src="turnaround_by_carrier.png" caption="Mean turnaround time by carrier. Southwest's rapid-turnaround model is clearly visible. Regional carriers cluster in the middle." >}}

## What It Means

For passengers, the practical advice is straightforward: before you book, check the scheduled ground time. If the airline has scheduled a 90-minute buffer between the inbound flight and your departure, turnaround problems are unlikely to delay you. If the buffer is only 35 minutes, you are flying on the edge. This information is available in the schedule before you buy the ticket.

For airlines, the rush effect reveals something important about their ground crews: they are already capable of compressing operations significantly when the pressure is on. This raises a question about schedule design. If crews can turn a plane in 67 minutes when it arrives late, why schedule 89 minutes of buffer when it arrives on time? The answer likely involves reliability margins and labor considerations, but it suggests there may be room to tighten schedules without increasing delays -- or alternatively, that current tight schedules are only surviving because crews absorb the pressure.

The deeper question -- which specific ground task is the real bottleneck -- remains unanswered. Publicly available data does not include gate assignments, ground crew task timestamps, or pushback clearance logs. Answering "is it the cleaning or the catering?" requires airport-specific operational data that is not publicly released.

## How We Did It

We used six months of real Bureau of Transportation Statistics On-Time Performance data (January through June 2024, 3.4 million flights). Turnaround events were reconstructed by sorting each tail number's flights chronologically and computing the time gap between consecutive flights at the same airport -- yielding 2.5 million events across 340 airports. We engineered 12 features and compared a naive baseline, a linear model, and a tree-based model using strict temporal cross-validation with [scikit-learn](https://scikit-learn.org/). The tree-based model predicted turnaround time about 3.7 times more accurately than guessing the average, and feature importance was computed via permutation on a 50,000-event subsample.

{{< figure src="feature_importance.png" caption="Permutation-based feature importance. The scheduled buffer dominates, followed by inbound delay. All other features combined account for less than 5% of predictive power." >}}

## Further Reading

- Beatty R et al. "Preliminary evaluation of flight delay propagation through an airline schedule." *Air Traffic Control Quarterly* (1999). [doi:10.2514/atcq.7.4.285](https://doi.org/10.2514/atcq.7.4.285) -- the first quantification that 30-40% of delay minutes come from aircraft rotations.
- Fleurquin P et al. "Systemic delay propagation in the US airport network." *Scientific Reports* (2013). -- modeled delay cascades as epidemic spreading and identified super-spreader hubs.
- [Detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/turnaround_time/paper.md) -- the full technical write-up with all figures, tables, and methodology.

---

**[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** -- the framework and full project history
