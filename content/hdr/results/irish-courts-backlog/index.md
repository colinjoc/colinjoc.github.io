---
title: "One Irish court handles ten times the load of any other"
date: 2026-04-16
domain: "Irish Courts"
blurb: "Six of Ireland's seven courts cleared their 2024 caseloads. One did not. It is also the one carrying ten times more work per judge."
weight: 11
tags: ["ireland", "courts", "public-services", "backlogs", "policy"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_courts_waits/analysis.py) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** The District Court took in 57,896 more cases in 2024 than it closed. Every other court in Ireland either kept pace or closed more than it opened. Normalised by how many judges each court has, the District Court is carrying nearly ten times the per-judge load of anywhere else in the system — and Road Traffic offences alone account for almost half of the overhang.

## The question

Every so often Irish headlines warn of a court system buckling under backlogs. The Courts Service has, since 2017, published annual data on how many cases each jurisdiction takes in and how many it resolves — but the raw numbers are easy to misread. We asked a narrow, defensible version of the question: in 2024, which court took in more than it closed, by how much, and how does that compare to the number of judges sitting?

A note on what this is. The Courts Service publishes annual flows — cases filed and cases resolved in a given year — but not the opening or closing pending-case balance. So the quantity we can honestly talk about is the **net filing surplus** (cases in minus cases out in the same year). That is not a backlog in the strict sense of accumulated stock. It is a year-on-year flow gap.

## What we found

Across Ireland's seven courts, six kept pace or cleared cases in 2024. One did not — and not by a small margin.

![Cumulative net filing surplus since 2017 by jurisdiction, anchored at zero in 2017. The District Court line dominates; every other jurisdiction stays close to flat.](plots/cumulative_backlog.png)

- The District Court took in 493,151 cases in 2024 and resolved 435,255, a single-year shortfall of 57,896 cases. That is an in-year resolution rate of 88 percent — meaning 12 of every 100 cases filed in 2024 were not resolved in 2024.
- Every other jurisdiction either kept pace or cleared cases. The Circuit, Central Criminal and Supreme Courts all closed more than they opened. The High Court and Court of Appeal ran small positive surpluses.
- Per-judge load is where the District Court sits in a league of its own. It handles roughly 7,954 new cases per judge per year. The Circuit Court is at 1,466. The High Court at 844. The Supreme Court at 23.
- Road Traffic offences account for 23,583 of the District Court's 2024 surplus — the single biggest contributor. Liquidated Debt and Child Care cases carry the next-worst in-year resolution rates, around half and six in ten respectively.
- Breach-of-Contract filings at the High Court swing wildly year to year — 246, then 1,458, then 336, then 1,435 — in a pattern almost certainly caused by how cases are coded or reported rather than any real swing in demand.

## Why that matters

The public conversation about Irish courts often treats "the courts" as one system. The data says the opposite. Six of seven courts are broadly in balance. The stress is concentrated in one jurisdiction, in a small number of case types, and it is visible most clearly when you ask how much work each judge is being handed.

That reframes the policy question. It is not "the court system is overwhelmed" — it is "the District Court is doing ten times the per-judge work of any other tier, and the single largest contributor is Road Traffic". Those two facts together suggest the pressure valve is not obviously more judges. It could equally be diverting volume out of the court altogether — expanding the fixed-charge penalty regime so that routine Road Traffic offences never reach a courtroom.

## What it means in practice

**For litigants.** If your case is at the Circuit Court or above, the 2024 data does not show your court falling behind. If you have a Child Care or Liquidated Debt matter in the District Court, the picture is tighter — roughly four in ten Child Care cases and half of Liquidated Debt cases filed in 2024 were not resolved within the same year. The data cannot tell you how long the carry-over actually takes to clear.

**For policymakers.** The District Court's per-judge load is an order of magnitude above every other jurisdiction. Two independent levers exist: add judicial capacity, or shrink the District Court's remit. The Road Traffic overlap with the fixed-charge penalty notice regime is an obvious candidate for the second lever.

**For journalists.** Talk about "Ireland's court backlog" is too coarse. The problem lives in one jurisdiction and a handful of categories. Headline numbers for the Supreme Court, Central Criminal Court, or Circuit Court do not describe a system falling behind.

## How we did it

We used the [Courts Service 2017-2024 annual data](https://data.courts.ie/), an 1,189-row panel of cases filed and resolved per jurisdiction, area of law and category each year. We computed in-year net filing surplus at every level, bootstrapped 95 percent confidence intervals over the eight-year panel, normalised 2024 flows by authorised judge strength, and cross-checked our numbers against the Courts Service's own 2024 Annual Report press release (both spot checks matched exactly). The dataset does not include 2017 opening balances, so we cannot produce a true pending-case stock.

## Further reading

- [Courts Service of Ireland open data portal](https://data.courts.ie/) — the source CSVs used here.
- Courts Service 2024 Annual Report (July 2025 press release) — independent confirmation of the District Court filing totals.
- [Full technical paper and code](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_courts_waits/analysis.py).
