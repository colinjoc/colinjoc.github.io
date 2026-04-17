---
title: "The Fast Track That Judges Killed: Ireland's 2017 Housing Experiment"
date: 2026-04-17
domain: "Irish Planning"
blurb: "Between 2017 and 2021 Ireland ran a planning fast-track that let big housing developments skip local councils entirely. Of the decisions that were challenged in the High Court, around 87 percent were either quashed by judges or conceded by the planning board before a hearing. The scheme was abolished at the end of 2021. This is the anatomy of how a major housing-delivery reform was undone in court."
weight: 13
tags: ["housing", "ireland", "planning-permissions", "judicial-review", "policy-evaluation"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_shd_judicial_review/paper.md).*

## The Question

In July 2017 the Oireachtas created a regime called Strategic Housing Development. For large housing schemes — originally 100 or more units, or 200 or more student bedspaces — developers could skip the local council entirely and apply directly to An Bord Pleanála, the national planning board. The policy promise was straightforward: speed. Large housing schemes in Ireland routinely took 18 to 30 months at council level, plus another 18 months if appealed. The new regime promised a 24-week turnaround.

On the surface the scheme worked. Over four years more than 280 applications were made and roughly 80 percent were granted. The question this project asks is what happened afterwards, when objectors took those grants to the High Court.

## What We Found

Of the sixteen fast-track decisions that reached a substantive High Court outcome between 2018 and 2021, fourteen went against the state — twelve quashed by judges, two conceded by the planning board before judgment. That is an 87.5 percent loss rate on contested cases.

- The most common reason for quashing was that the planning board had granted permission for developments that contravened the local development plan (usually on building height) without writing down adequate reasons. The law allowed contravention, but required documented reasoning; the documentation was often not there.
- Secondary reasons included inadequate assessment of habitat impact under European environmental law, and procedural failures such as not publishing application documents on a dedicated website as the scheme required.
- The planning board's legal costs from defending these challenges more than doubled in a single year, from 3.5 million euros in 2019 to 8.2 million in 2020.
- Press reporting at the time cited a higher total of roughly 35 challenges at a 91 percent loss rate. That figure includes lodged-but-not-decided cases; the official register counts only decided cases. Both sources agree the state was losing somewhere in the high 80s to low 90s.
- The scheme was replaced at the end of 2021 by a new regime that explicitly addressed the reasoning-and-documentation failings.

## Why That's Surprising

The standard assumption about a fast-track process is that the legal risk you are trading off is "some decisions will be rushed and appealed", producing maybe a 20 or 30 percent reversal rate on contested cases. An 87 percent loss rate is a different species of problem. It means the contested cases were not marginal — they were cases where the state was straightforwardly not producing the kind of reasoned decision the courts require.

It is also striking that the fix was not difficult law. In almost every case the board had the power to reach the outcome it reached. It just had to write down why, in a particular form, on a particular range of topics. The fast track failed not because judges disagreed with its decisions, but because it was not generating the paperwork courts needed to defer to them.

## What It Means

For housing policy, the lesson is that a fast-track that bypasses local government does not deliver faster housing unless the fast-track body can produce the procedural reasoning the courts will demand. Speed and robustness are not a trade-off here — a decision quashed three years after issuance is slower than a slower decision that sticks. The replacement regime builds the documentation requirements in from the start.

For objectors and residents' groups, the period showed that well-prepared judicial reviews targeting specific documented procedural gaps had extremely high success rates. The strategy was narrow and legal, not broad and political.

For the wider housing pipeline, most fast-track permissions — roughly 240 to 260 of 280 — were never challenged in court, and those did proceed. The scheme's failure was not total. But the cases that went to court did so at a loss rate that made the regime's legal exposure unsustainable.

## How We Did It

The analysis uses the [Office of the Planning Regulator's Appendix-2 schedule](https://www.opr.ie/), published October 2022, which lists every planning judicial review decided since 2012. The scheme-specific cases for 2018-2021 were extracted with a parser that handles the quirks of the source PDF, cross-checked against a hand-verified ground truth for every case, and confirmed against a 27-test regression suite. Legal-cost figures come from press reporting of the planning board's published annual accounts.

## Further Reading

- [Office of the Planning Regulator](https://www.opr.ie/) — publisher of the canonical case schedule
- [An Bord Pleanála publications](https://www.pleanala.ie/en-ie/publications) — planning-board annual reports
- [Companion follow-up study on the successor regime](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lrd_vs_shd_jr/paper.md) — can the 2021 replacement's effect be measured yet?
- [Full technical write-up](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_shd_judicial_review/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
