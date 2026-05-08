---
title: "The hospitals where the backlog is about to grow"
date: 2026-05-08
domain: "Irish health policy"
blurb: "Ireland's longest hospital queues move with the rhythm of physics, not politics — and a hospital's recent past tells you almost everything."
weight: 45
tags: ["health", "ireland", "waiting-lists", "ntpf", "forecasting", "policy"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ntpf_outpatient_waits/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Whether a hospital's "more than 18 months waiting" share is about to grow next month is partly forecastable from its own recent trend — but the hospital's name and quirks add almost nothing. The list behaves like a slow-moving queue, not a story about local management.

## The question

Roughly 600,000 people are sitting on Ireland's public outpatient waiting list. The politically charged number — the one that turns up in Dáil questions and news bulletins — is the share who have already waited more than 18 months for a first specialist appointment. Beyond that point, access starts to feel less like a delay and more like a refusal.

For a voter, the question is concrete: is my local hospital's long-wait backlog about to get worse, or better, next month? And does the answer depend on which hospital it is — on the local consultant roster, the building, the management — or on something more impersonal?

## What we found

We trained a forecaster on five years of monthly hospital-level returns from the National Treatment Purchase Fund (NTPF) and asked it to predict, for each of 46 public hospitals, whether the over-18-months share would rise the following month. The headline finding is unflattering to the idea that local context matters much.

- The forecaster correctly distinguishes "growing" from "shrinking" hospital-months noticeably better than chance, and the lift survives every robustness check we threw at it.
- When we restricted the question to **policy-relevant** growth — a jump of at least two percentage points, or at least ten extra long-waiting patients — the model got sharper, not noisier. It is better at catching real deterioration than knife-edge wobbles.
- Stripping out every feature that identifies the hospital — name, size rank, top-20 indicator — barely moved the forecast. Beaumont's recent trajectory predicts Beaumont's next month roughly as well as Beaumont's identity does.
- Almost all of the forecast's lift comes from the recent trend in the hospital's own long-wait share. A simple two-month-memory benchmark already captures most of the signal; the elaborate feature set adds only a sliver.
- Children's waiting lists are markedly more predictable than adults', and that finding holds even when we hold out each large children's hospital one at a time. It is not an artefact of CHI Temple Street or Crumlin.

## Why that matters

The received wisdom in Irish health-policy debate is granular and personal: this consultant retired, that hospital lost theatre time, this manager is new, that catchment is older. Such things may all be true, and they may all matter for **levels** of waiting. But for the **next move** in the long-wait share — whether things are about to drift up or down at a given hospital — the data say something flatter and more mechanical. The list moves like a queue with slow physical dynamics: a fixed number of consultant slots, a roughly steady inflow of referrals, and an outflow capped by capacity. Once you know its current state and its momentum, the hospital's identity adds nothing detectable.

That is consistent with a system in which policy levers — Sláintecare funding, NTPF outsourcing budgets, the 2023 public-only consultant contract — have to push against the same physics in every hospital. It is not consistent with the implicit assumption behind a lot of operational reporting, which is that each hospital's queue is its own special story.

## What it means in practice

**For patients.** If your local hospital's over-18-months share has been creeping up for the past few months, that drift is the strongest single signal about the next month. Reassurances that "this is a temporary spike" should be treated with caution — the data say drift persists.

**For HSE managers.** A simple, honest early-warning dashboard built on two or three months of lagged share would catch most of what an elaborate model catches. The marginal value of bespoke per-hospital tuning is small. The value of doing the basic thing consistently, across all hospitals, is large.

**For policymakers.** Children's queues behave differently and more predictably than adult ones, in a way that is not driven by the two big paediatric hospitals. That is a clue — possibly about specialty mix, possibly about scheduling rhythm — worth chasing, because it implies the system has at least one regime where intervention effects should be cleaner to measure.

**For everyone reading the headlines.** A monthly fall in the long-wait share at a single hospital is, on its own, a weak signal. The trend over a quarter is a much better one. Treat one-month wins with the same scepticism you would treat one-month losses.

## How we did it

We assembled a panel of 4,740 hospital-month observations, covering 46 Irish public hospitals from April 2021 to March 2026, using the [NTPF Open Data portal](https://www.ntpf.ie/waiting-list-data/open-data/), which publishes monthly hospital-level outpatient waiting-list breakdowns by adult and child cohort and by duration band. We framed the forecast as a binary question — will this hospital's over-18-months share rise next month? — and trained a tree-based model on lagged share, recent change, hospital size and seasonality features, evaluated on rolling time-ordered folds so the model never sees the future. We then stress-tested the result with cluster bootstrap, permutation null, materiality thresholds, and leave-one-hospital-out for the children's subset to make sure no single hospital was carrying the conclusion.

## Further reading

- [NTPF Open Data portal](https://www.ntpf.ie/waiting-list-data/open-data/) — the underlying monthly hospital-level waiting-list microdata.
- [Sláintecare Implementation Progress Report 2024](https://www.gov.ie/en/department-of-health/) — the Department of Health's own accounting of waiting-list reductions claimed since 2023.
- [Walsh, Bergin, Keegan, Brick (2021), "Paying more to wait less"](https://www.esri.ie/) — ESRI estimate of the cost of clearing Ireland's public hospital backlog.
- [Full technical paper (paper.md)](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ntpf_outpatient_waits/paper.md) — diagnostics, robustness battery and experiment logs.
