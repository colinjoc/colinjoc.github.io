---
title: "Which Irish hospital backlog is about to get worse?"
date: 2026-04-16
domain: "Irish Healthcare"
blurb: "Six hundred thousand people are waiting on Irish public hospital lists. Using only data a citizen can download, can you tell which queue grows next?"
weight: 24
tags: ["healthcare", "ireland", "waiting-lists", "NTPF", "forecasting"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ntpf_outpatient_waits/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Next month's growth in a hospital's long-waiters share is roughly two-thirds predictable from that hospital's own recent trajectory — and children's queues are materially more forecastable than adult queues, even though the identity of the hospital itself barely matters.

## The question

Every month the National Treatment Purchase Fund publishes open data on Irish public hospital waiting lists. At the end of December 2025, 611,987 people were waiting for a first outpatient appointment. About 40,000 of them had been waiting longer than 18 months — the threshold beyond which access effectively disappears. You are on the list, nobody has scheduled you, and nobody is telling you when they will.

The political backdrop is a decade of investment aimed at shrinking that number. Sláintecare, committed at more than 500 million euros a year since 2018, is the supply-side plan. The NTPF itself spends about 230 million euros a year buying private capacity to pull individuals off public queues. The question an ordinary voter can ask is direct: is my local hospital's backlog growing or shrinking, and is there any way to tell what comes next?

## What we found

Whether a hospital's share of 18-month-plus waiters will grow next month is partially predictable from the hospital's own past. Across 4,740 hospital-months from 46 public hospitals since April 2021, a machine-learning model gets this right about 70 percent of the time, compared to the 50 percent you would get by guessing — and its probabilities are well-calibrated: when it says "60 percent chance", roughly 60 percent is what happens.

- The model is sharper at catching real trouble than at calling tiny jitter. At the knife-edge "any growth at all" threshold, it beats guessing by about 20 percentage points. At "grew by at least 10 extra long-waiters", the gap widens to 31 percentage points — the kind of move a policymaker actually cares about.
- The hospital's identity contributes essentially nothing. Stripping out every hospital-specific indicator barely changes the model. It is not learning Beaumont's quirks or Cork University Hospital's pattern — it is learning generic queue dynamics that apply everywhere.
- Children's waiting lists are materially more predictable than adults'. Within the paediatric subset the model is accurate on about three-quarters of cases, compared to roughly two-thirds for adults — and the gap survives holding each children's hospital out in turn.
- Most of the signal is autocorrelation. A bare-bones model using only the current long-waiter share and two of its recent lags captures almost all of what the 30-feature model can do. The system has slow physical dynamics — limited consultant-hours, limited bed days, steady referral flow — and the best forecast of next month is an extrapolation of this month.

![The share of Irish outpatient waiters past 18 months, nationally, month by month since April 2021.](plots/pct_over18m_trend.png)

## The forecast for next month

Running the model on the most recent data (end of March 2026) ranks the hospital-months most likely to see their long-waiter share grow. The top tier is geographically diverse: a regional Midlands hospital (Mullingar) and a western one (Letterkenny) lead the children's side; the two largest Dublin teaching hospitals (Beaumont and St. James's) appear on the adult side; University Hospital Limerick — already the subject of a January 2024 overcrowding scandal and a 2025 public inquest — shows up on the paediatric list. These are places where the current momentum in the data, with no new information about bed capacity or consultant hires, favours the queue getting longer before it gets shorter.

| Rank | Hospital | Adult / Child | Currently waiting | Over 18 months | Predicted growth probability |
|---|---|---|---:|---:|---:|
| 1 | Midland Regional Hospital Mullingar | Child | 993 | 29 | 62% |
| 2 | Letterkenny University Hospital | Child | 1,320 | 2 | 60% |
| 3 | Mallow General Hospital | Adult | 3,799 | 209 | 59% |
| 4 | Mayo University Hospital | Child | 1,065 | 64 | 56% |
| 5 | University Hospital Limerick | Child | 4,202 | 236 | 56% |
| 6 | Midland Regional Hospital Tullamore | Adult | 18,236 | 152 | 55% |
| 7 | Beaumont Hospital | Adult | 54,019 | 2,787 | 53% |
| 8 | St. James's Hospital | Adult | 27,460 | 1,315 | 52% |
| 9 | Our Lady of Lourdes Drogheda | Adult | 17,086 | 854 | 51% |

## Why that matters

The interesting finding is what the model does not need. Irish outpatient queues are behaving like a single slow-moving object distributed across 46 sites — what happens at Beaumont in terms of trajectory is largely what happens at Cork University Hospital, or at Mayo. That implies queue length is being driven by structural constraints common to the whole system (consultant hours, bed days, referral flow), not by hospital-specific management choices. If a policy intervention — a consultant contract reform, a targeted NTPF purchase — actually works, it has to show up as a deviation from this shared momentum.

The child-adult gap is the other loose thread. Paediatric queues are easier to forecast, and the effect is not driven by the big Dublin children's hospitals. Three candidate explanations survive: paediatric care is dominated by a handful of specialties with more regular referral flows; children cannot substitute into private insurance the way adults can, so the public queue reflects genuine demand rather than demand-minus-substitution; and paediatric scheduling is more tied to school terms. Testing between them requires specialty-level data we did not have.

## What it means in practice

**For people on the list.** The model does not rescue you. But it does explain why your local hospital's backlog has the shape it has — for structural reasons that no single policy announcement is likely to change. If the trajectory is currently upward at your hospital, the most honest forecast is that it stays upward next month.

**For policymakers and health-service watchers.** The model is a baseline. If Sláintecare's consultant-contract reforms are working, they will appear as a downward deviation from the calibrated forecast. If they are not, the lag structure absorbs them and the trajectory marches on. Either way, this gives you an honest counterfactual against which to judge interventions.

**For researchers.** The hospital-identity channel being empty is worth following up. Irish queue dynamics appear to be a shared object, not a collection of local micromanagement stories. The next project is a causal one — staggered difference-in-differences on consultant-contract opt-in, or an interrupted time series on NTPF allocation step-ups — with the specialty-level data this panel did not include.

## What we could not do

This is a short-horizon forecasting project, not a causal evaluation. We did not measure whether Sláintecare has worked, whether the 2023 Public-Only Consultant Contract reduced waits in opt-in hospitals, or whether NTPF-funded private-capacity purchases reduce long waits rather than shuffle them within the queue. We also could not extend the panel back before April 2021: the NTPF schema changed when adult and child lists were separated, and the earlier files are not available at the URL pattern they should be.

## How we did it

We used the full NTPF outpatient Open Data archive (April 2021 through March 2026), built a monthly panel of 46 hospitals across adult and child lists, and asked whether each hospital-month's long-waiter share would grow in the following month. A tree-based model with rolling time-series validation did the forecasting; confidence intervals came from cluster bootstrap and a permutation null, and the children's result was stress-tested by holding each paediatric hospital out in turn.

## Further reading

- National Treatment Purchase Fund — Monthly Outpatient Open Data archive — the raw files the panel is built from.
- Department of Health. *Sláintecare Implementation Strategy* — the supply-side reform programme behind the political context.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ntpf_outpatient_waits/paper.md) — the full hospital-month panel, robustness battery and code.
