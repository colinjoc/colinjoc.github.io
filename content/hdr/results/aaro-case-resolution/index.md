---
title: "What the Pentagon's UAP numbers actually say"
date: 2026-04-18
domain: "Data Science"
blurb: "The Pentagon is taking thousands of UFO reports. Of the ones it has actually closed, how many turned out to be something exotic?"
weight: 22
tags: ["UAP", "UFO", "AARO", "Pentagon", "Bayesian", "base-rate"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/aaro_case_resolution/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed. Companion to the [NUFORC sighting patterns](/hdr/results/ufo-sighting-patterns/) analysis.*

**Bottom line.** Every single one of the 292 unidentified aerial phenomenon cases the US government has resolved has turned out to be balloons, birds, drones, satellites, or aircraft. The 21 cases flagged as worth further intelligence analysis work out to 2.8 percent of intake — exactly the same "unidentified residual" every prior government UFO program has converged on going back to the 1950s.

## The question

The All-domain Anomaly Resolution Office, or AARO, is the Pentagon's official clearinghouse for unidentified aerial phenomenon — what everyone else calls UFO — reports. As of June 2024 it had taken in 1,652 reports. A handful are dramatic: Navy pilots, classified radar returns, sensor anomalies. Most are mundane.

Headlines focus on the backlog. We wanted to know what the actual numbers say. What fraction get resolved? What do they resolve to? How does the unidentified residual compare to every prior US and European UFO program? And when someone says "but most cases are unexplained", what does that actually mean?

## What we found

Of 1,652 reports received, 292 have been resolved or recommended for closure. Every one of them turned out to be a prosaic object. Twenty-one further cases have been flagged as worth deeper intelligence analysis. The rest — about 1,360 — remain open, mostly because the underlying sensor data is too thin to identify anything.

- Every resolved case is a balloon, a bird, a drone, a satellite, or an aircraft. None is anomalous.
- The 21 "worth further analysis" cases are 2.8 percent of total intake. Project Blue Book, the US Air Force's 1952-1969 program, ended up at 5.6 percent unidentified. France's ongoing GEIPAN program sits at 3.5 percent. The same floor keeps appearing.
- Unresolved does not mean anomalous. The 82 percent of cases still open are open because the data is thin — brief observations, no corroboration, poor sensor coverage — not because the object was exotic.
- AARO takes in about 37 new cases per month and closes about 22. The backlog grows, but slowly. Reports of "757 new cases" include 272 catch-up reports from earlier periods, which inflates the apparent intake rate by about a third.
- A Bayesian update starting from a generous five percent prior that any given unresolved case is genuinely anomalous pulls the posterior down to roughly four percent. The AARO data actually makes the anomalous hypothesis slightly less likely, not more, because prosaic objects disappear into the unresolved pile for reasons that have nothing to do with what they were.

## Why that matters

The public narrative around AARO oscillates between "the Pentagon is hiding something" and "the Pentagon has confirmed nothing exotic". The data sits quietly between them. The residual of unexplained cases is real, but it is small, it is exactly the size every prior program found, and it is fully consistent with a world where the entire residual comes from sensor limits rather than novel phenomena.

Whether the 21 cases under deeper analysis contain anything genuinely novel depends on classified sensor data that is not in the public reports. The limiting factor is not methodology. It is instrumentation. Until purpose-built calibrated sensors capture multi-modal data at the moment of observation — which is what AARO's planned GREMLIN system is meant to do — most cases will remain data-insufficient, and the residual will stay stuck around three to six percent.

## What it means in practice

**For journalists covering AARO.** "Unexplained" in the reports almost always means "the sensor data was too thin to identify it", not "it was something exotic". The ratio of prosaic resolutions to exotic findings in the resolved pile is currently 292 to zero.

**For policymakers.** The next useful investment is not more reports. It is better sensors at locations where reports cluster — purpose-built instrumentation that captures calibrated, multi-modal data at the moment of observation. Without that, the residual will stay where every prior program found it.

**For readers who track this stuff.** The historical base rate across Project Blue Book, GEIPAN, and AARO is stable at three to six percent unidentified. AARO is not producing a different answer. It is replicating one.

## How we did it

We extracted every quantitative figure from AARO's Fiscal Year 2024 report and the 2022 Office of the Director of National Intelligence report, built a resolution-rate model and a backlog projection, and compared the unidentified residual to historical US and European UFO program data. We then ran a two-dimensional Bayesian posterior surface across reasonable priors and likelihood assumptions to see how strong the evidence has to be to shift the conclusion.

## Further reading

- AARO Fiscal Year 2024 Annual Report — the Department of Defense's own tally of cases received, resolved, and flagged.
- Office of the Director of National Intelligence, 2022 UAP Report — the assessment of the 2004-2021 backlog of US military sightings.
- Project Blue Book (1952-1969) — the original US Air Force investigation, which ended with a 5.6 percent unidentified residual.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/aaro_case_resolution/paper.md).
