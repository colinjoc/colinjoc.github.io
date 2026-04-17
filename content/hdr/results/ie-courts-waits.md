---
title: "One Irish Court Handles Ten Times More Cases Per Judge Than Any Other"
date: 2026-04-17
domain: "Irish Courts"
blurb: "Using the Courts Service's newly-open 2017-2024 annual data, we found the District Court absorbed 493,151 new cases in 2024 and resolved 435,255 — a single-year surplus of nearly 58,000 cases and roughly 7,954 incoming cases per judge. Every other Irish court is keeping pace or clearing; Road Traffic alone accounts for about 40 percent of the District Court's carry-over."
weight: 13
tags: ["ireland", "courts", "public-services", "backlogs", "policy"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_courts_waits/paper.md).*

## The Question

Ireland's Courts Service began publishing its annual case data as open machine-readable files for the first time. Eight years of it — 2017 through 2024 — covering every jurisdiction from the Supreme Court to the District Court and broken out by 94 case categories, from Bail to Probate to Liquidated Debt.

A simple question becomes answerable for the first time: of the cases filed in a given year, what fraction were resolved in the same year, and which court is falling behind?

## What We Found

The imbalance is in one place.

| Jurisdiction | 2024 cases in | 2024 cases resolved | Surplus | In-year resolution |
|---|---|---|---|---|
| District Court | 493,151 | 435,255 | **+57,896** | 88 percent |
| High Court | 36,303 | 34,446 | +1,857 | 95 percent |
| Court of Appeal | 3,487 | 2,376 | +1,111 | 68 percent |
| Circuit Court | 63,048 | 66,417 | −3,369 | 105 percent |
| Central Criminal Court | 2,810 | 3,338 | −528 | 119 percent |
| Supreme Court | 231 | 239 | −8 | 104 percent |

Circuit, Central Criminal, and Supreme Courts all closed more cases in 2024 than they opened. The District Court closed 88 of every 100 cases that came in — leaving roughly one in ten to roll into the next year.

Normalising by the number of judges sharpens the picture further. A District Court judge took in about **7,954 cases** in 2024. The comparable figure at the Circuit Court is 1,466; at the High Court, 844; at the Supreme Court, 23. The District Court handles more than an order of magnitude more cases per judge than any other Irish court.

Inside the District Court, Road Traffic is the single biggest contributor to the backlog in absolute terms (+23,583 unresolved in 2024), while Child Care (60 percent same-year resolution) and Liquidated Debt (50 percent) are the slowest-moving categories.

## Why That's Surprising

The usual assumption in Irish court commentary is that delays are a Superior Courts problem — the High Court, Court of Appeal, and Supreme Court being slow and crowded. The data show nearly the opposite. The Superior Courts are, by the in-year resolution metric, keeping up. The Circuit Court is clearing more than it takes in. The backlog is entirely a District Court phenomenon, and almost entirely a question of volume per judge rather than procedural slowness per case.

There is also a methodological surprise for anyone working with the open data. The dataset publishes flows — cases in, cases out — but not the opening and closing stock of pending cases on 1 January and 31 December. Calling the running difference a "backlog" mixes three separate things: real accumulation, the slow grind through pre-2017 legacy cases, and boundary artefacts where a case filed in 2020 and resolved in 2024 appears once in each flow without any wait-time attached. The right framing is net *filing surplus*, a flow quantity, not a pending-caseload stock. The published data do not support per-case waiting-time claims at all.

## What It Means

For a policymaker: the evidence for "we need more District Court judges" is stronger than the evidence for "we need more Superior Court capacity". A single District Court bench handles close to eight thousand incoming cases a year. The Courts Service itself credited 24 judicial appointments in 2023 with reducing backlogs; the per-judge data suggest the effect of further appointments would again land almost entirely at District level.

A second, adjacent lever is where Road Traffic cases are handled. Road Traffic is the largest single category in the 2024 District Court surplus. Every additional case that can be diverted to the fixed-charge penalty-notice regime is a District Court sitting that does not need to happen.

For a litigant, the practical reading is category-specific: Child Care and Liquidated Debt cases in the District Court have the lowest same-year resolution rates. The open data cannot say how long the carry-over takes — only that the system is not finishing most of these matters within the year they are filed.

## How We Did It

We downloaded the Courts Service annual datasets for 2017 through 2024 from [data.courts.ie](https://data.courts.ie), concatenated them into a 1,189-row panel broken out by jurisdiction, area of law, and case category, and computed in-year resolution ratios with bootstrap 95 percent confidence intervals. We audited category stability year to year to flag reporting-boundary artefacts, cross-checked headline figures against the Courts Service 2024 Annual Report press release, and normalised by authorised judge strength to allow per-judge comparisons across jurisdictions of very different sizes.

## Further Reading

- [Courts Service of Ireland data portal](https://data.courts.ie) — the open CSV source
- [Courts Service Annual Report 2024](https://www.courts.ie/annual-report) — the official narrative version
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_courts_waits/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
