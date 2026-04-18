---
title: "Late-arriving flights turn around faster, not slower"
date: 2026-04-12
domain: "Transport / Aviation Operations"
blurb: "Ever watched a ground crew rush your plane between flights? We tracked 2.5 million turnarounds to see what actually drives the clock."
weight: 29
tags: ["transport", "aviation", "turnaround-time", "ground-operations", "airline-scheduling"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/turnaround_time/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Across 2.5 million real aircraft turnarounds in the United States, the airline's own scheduled buffer explains roughly four-fifths of why some turnarounds are fast and others are slow. And flights arriving late actually turn around faster — ground crews compress their work to recover delay, and the effect only breaks down when flights are extremely late.

## The Question

Every frequent flyer has sat at a gate watching ground crews work against the clock. The turnaround — the time an airplane spends on the ground between arriving from one flight and departing on the next — involves deplaning, cleaning, catering, fuelling, boarding, and pushback. Airlines schedule buffer time for all of this, but the actual turnaround varies wildly. The same aircraft type at the same airport can turn in 32 minutes one day and 71 the next.

We wanted to know what determines whether a turnaround is fast or slow. Is the bottleneck cleaning, fuelling, catering, crew changes, or gate conflicts? And does a delayed inbound flight make things worse — or force the crew to work faster?

## What we found

The airline's own schedule overwhelms everything else. By tracking each aircraft's tail number through consecutive flights at the same airport, we reconstructed 2.5 million turnaround events from 3.4 million US domestic flights over six months of real data from the [Bureau of Transportation Statistics](https://www.transtats.bts.gov/).

{{< figure src="turnaround_distribution.png" caption="Distribution of 2.5 million turnaround times (left) and the relationship between scheduled and actual turnaround (right). The median turnaround is 63 minutes, but the distribution has a long right tail extending past 300 minutes." >}}

- The schedule is the mechanism. How much time the airline allows between the arrival of one flight and the departure of the next accounts for roughly four-fifths of the predictive model's power. Most turnaround variability is not operational chaos — it is baked into the timetable.
- Delayed flights turn around faster, not slower. Flights arriving 30 to 60 minutes late spend an average of 67 minutes on the ground, compared to 89 minutes for flights arriving early. Ground crews compress operations when running behind. But the effect reverses beyond two hours of delay, where recovery becomes impossible and turnarounds expand again.
- Southwest turns planes nearly twice as fast as the legacy carriers. Southwest averages 62 minutes per turnaround; United and American average 103 to 104 minutes. The gap widens further at specific airports.
- Morning turnarounds are longer than evening ones — not because morning crews are slower, but because airlines front-load scheduling slack early in the day and compress it later. A plane arriving at 7 in the morning sits for nearly two hours on average; by 5 in the evening that drops to 70 minutes.
- Weekday turnarounds barely differ. Saturdays are the slowest day (about 89 minutes on average) and Fridays the fastest (about 81 minutes), but the spread across the whole week is only about 10 percent.

{{< figure src="inbound_delay_effect.png" caption="The rush effect: flights arriving late have shorter turnarounds as ground crews compress operations. The effect reverses for extreme delays beyond 120 minutes, where recovery becomes impossible." >}}

## Why that matters

The conventional wisdom — and recent academic literature — focuses on delay propagation: a late inbound aircraft should cause a late outbound because there is less time for ground operations. One recent preprint even identified whether the previous user of the same gate was delayed as a dominant predictor of turnaround variability.

The data tells a different story. Late arrivals are associated with shorter turnarounds, not longer ones. Ground crews clearly adapt their pace to the situation. When a plane lands late, the pressure to recover pushes crews to work faster. This "rush effect" persists even after controlling for time of day, ruling out the possibility that it is just a quirk of evening schedules being tighter.

Meanwhile, the dominance of the scheduled buffer suggests that most of the variation passengers notice is not operational chaos — it is deliberate timetable design. Airlines choose to give some flights generous buffers and others razor-thin ones. That single scheduling decision explains more than weather, congestion, crew, and equipment factors combined.

{{< figure src="turnaround_by_carrier.png" caption="Mean turnaround time by carrier. Southwest's rapid-turnaround model is clearly visible. Regional carriers cluster in the middle." >}}

## What it means in practice

**For passengers.** Before you book, check the scheduled ground time at your connection. If the airline has scheduled a 90-minute buffer between the inbound flight and your departure, turnaround problems are unlikely to delay you. If the buffer is only 35 minutes, you are flying on the edge. This information is available in the schedule before you buy the ticket.

**For airlines and operations teams.** The rush effect reveals something important about ground crews: they are already capable of compressing operations significantly when pressure is on. That raises an obvious question about schedule design. If crews can turn a plane in 67 minutes when it arrives late, why schedule 89 minutes of buffer when it arrives on time? The answer likely involves reliability margins and labour considerations — but it suggests either that current tight schedules are only surviving because crews absorb the pressure, or that there is room to tighten schedules without increasing delays.

**For regulators and researchers.** The deeper question — which specific ground task is actually the bottleneck — remains unanswered here, and cannot be answered from public data. Publicly available records do not include gate assignments, ground crew task timestamps, or pushback clearance logs. Answering "is it the cleaning or the catering?" requires airport-specific operational data that is not publicly released.

## How we did it

We used six months of real Bureau of Transportation Statistics On-Time Performance data (January through June 2024, 3.4 million flights). Turnaround events were reconstructed by sorting each tail number's flights chronologically and computing the time gap between consecutive flights at the same airport — yielding 2.5 million events across 340 airports. We engineered 12 features and compared a naive baseline, a simple linear model, and a tree-based model using strict temporal cross-validation. The tree-based model predicted turnaround time about 3.7 times more accurately than guessing the average. Feature importance was computed via permutation on a 50,000-event subsample.

{{< figure src="feature_importance.png" caption="Permutation-based feature importance. The scheduled buffer dominates, followed by inbound delay. All other features combined account for less than five percent of predictive power." >}}

## Further reading

- Beatty R et al. (1999). ["Preliminary evaluation of flight delay propagation through an airline schedule"](https://doi.org/10.2514/atcq.7.4.285), *Air Traffic Control Quarterly* — the first quantification that 30 to 40 percent of delay minutes come from aircraft rotations.
- Fleurquin P et al. (2013). *Systemic delay propagation in the US airport network*, *Scientific Reports* — modelled delay cascades as epidemic spreading and identified super-spreader hubs.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/turnaround_time/paper.md) — all figures, tables, and methodology.
