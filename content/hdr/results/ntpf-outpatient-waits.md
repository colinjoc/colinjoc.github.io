---
title: "Predicting Which Irish Hospitals Will Still Have the Longest Waits"
date: 2026-04-17
domain: "Health Services"
blurb: "Roughly 600,000 people sit on Ireland's public outpatient waiting list, and a politically defining 5 to 10 percent of them have been waiting more than 18 months for a first specialist appointment. Using five years of monthly hospital data, we built a forecast that identifies which hospitals are about to see their longest waits grow. The surprise: which hospital it is barely matters. The signal is almost entirely in each hospital's own recent history, and children's queues turn out to be more predictable than adults'."
weight: 12
tags: ["healthcare", "ireland", "waiting-lists", "forecasting", "public-services"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ntpf_outpatient_waits/paper.md).*

## The Question

Ireland has one of the lowest staffed acute-bed densities in the developed world and one of the highest public outpatient waiting lists. The number that dominates political debate is the fraction of people on that list who have been waiting more than 18 months — beyond that point, access to a first specialist appointment becomes, in practice, foreclosed. Successive governments have poured hundreds of millions of euros a year into shortening it.

The question a patient, a GP, or a local councillor actually wants answered is not abstract. It is: is my local hospital's backlog growing or shrinking this month, and which way is it about to go next?

## What We Found

It is possible to forecast, month by month and hospital by hospital, whether the "more than 18 months waiting" share is about to rise — but the signal comes from somewhere unexpected.

- The forecast correctly identifies growing backlogs substantially better than chance on a rolling out-of-sample test, and the probability scores it produces are well-calibrated enough to treat as actual risk estimates.
- Which hospital it is turns out to be almost completely uninformative. Dropping every hospital-identity feature changes the forecast accuracy by essentially zero. The model does not need to know a hospital's name to predict its trajectory.
- Almost all of the predictive power is carried by recent history — the current long-waits share and its changes over the previous one and three months.
- The model is sharper when the question is tightened from "any growth at all" to "growth of at least two percentage points" or "at least ten extra long-waiters". The signal strengthens for policy-relevant changes and fades for knife-edge noise.
- Children's waiting lists are materially more predictable than adults'. This survives holding each of the large children's hospitals out of the training set, so it is not an artefact of those specific hospitals.

## Why That's Surprising

The intuitive picture of a waiting list is that local factors dominate — this consultant is on leave, that operating theatre is under refurbishment, a nearby town's population is growing faster. If that were the main story, hospital identity should matter a lot. It almost doesn't. Queues at Irish hospitals appear to follow a common dynamic driven mostly by each hospital's own recent trajectory, with the specific hospital contributing almost nothing on top.

The children's-list result is a second surprise. A smaller, narrower population is more predictable than a larger one, and the effect survives even when the biggest children's hospitals are excluded. The most plausible explanations are fewer specialties to track, less patient substitution between services, and scheduling tied to school-term rhythms — but the empirical pattern is clear regardless of mechanism.

## What It Means

For policymakers and hospital managers, the finding that hospital identity is largely uninformative is practical: a dashboard that treats every hospital as roughly exchangeable and predicts purely from each hospital's own recent history would work about as well as one that tries to model each hospital's specific character. That simplifies tooling.

For the public, it means the trajectory of a local backlog is mostly inherited from the recent past, not from hospital-specific idiosyncrasies. If your local hospital's long-wait share has been creeping up for three months, that is the single strongest signal it will keep doing so next month. Intervention from outside that pattern — new funding, a new consultant contract, capacity bought from the private sector — would register as a break in this otherwise autocorrelated flow.

This study does not establish what specific policy interventions have worked or not worked. That is a different analysis, explicitly flagged as the priority follow-up.

## How We Did It

The data is the [National Treatment Purchase Fund Open Data portal](https://www.ntpf.ie/waiting-list-data/open-data/), which publishes monthly outpatient-waiting-list CSVs for each of Ireland's 46 public hospitals, split between adult and child lists, from April 2021 to the present. The analysis trains a tree-based forecast on each hospital-month in the panel, with strictly time-forward cross-validation to prevent the model from learning from its own future, and compares its accuracy against a simple autoregressive benchmark. Results are reported with cluster-bootstrap uncertainty intervals and a permutation-null sanity check.

## Further Reading

- [National Treatment Purchase Fund Open Data](https://www.ntpf.ie/waiting-list-data/open-data/) — the monthly hospital-level source data
- [Sláintecare programme](https://www.gov.ie/en/campaigns/slaintecare/) — the Irish government's health-reform strategy
- [Full technical write-up](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ntpf_outpatient_waits/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
