---
title: "Irish Courts: Which Court Has the Largest 2024 Net Filing Surplus?"
date: 2026-04-16
domain: "Irish Courts"
blurb: "Using the Courts Service's newly-open 2017-2024 annual data, we decomposed the 2024 annual net filing surplus (new cases minus cases resolved in the same year — a flow quantity, NOT a true pending-caseload stock) by jurisdiction. The District Court has by far the largest 2024 net flow surplus: 493,151 incoming versus 435,255 resolved, a single-year surplus of 57,896 cases (resolution ratio 88.3 percent, bootstrap 95 percent CI [81.8, 95.1]). Road Traffic drives 23,583 of that annual surplus. Per-judge load is ~7,954 incoming/judge — an order of magnitude above every other jurisdiction. Circuit, Central Criminal and Supreme Courts all closed more cases than they opened in 2024."
weight: 11
tags: ["ireland", "courts", "public-services", "backlogs", "policy"]
---

*Plain-language version. Full technical write-up in the [analysis script](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_courts_waits/analysis.py).*

**Note: retroactively revised on 2026-04-15.** The original Phase 0 version of this summary referred to a "cumulative backlog" and claimed "a roughly 2-in-5 chance of waiting more than a year". A retroactive Phase 2.75 blind reviewer cycle found that the data supports neither framing: the Courts Service CSVs report annual incoming/resolved *flows*, not pending-case *stocks*, and contain no per-case wait times. The current version relabels everything as "net filing surplus", adds bootstrap confidence intervals, cross-checks against the Courts Service 2024 Annual Report press release, and adds per-judge normalisation. See `paper_review.md` and `paper_review_signoff.md` in the project directory for the audit trail.

## What this is (and what it isn't)

**This is a flow analysis, not a stock measurement.** The Courts Service publishes, for each (jurisdiction, area of law, category, year), the number of cases *filed* that year and the number *resolved* that year. It does NOT publish opening or closing pending-case counts. A "cumulative incoming minus resolved" curve therefore mixes real carry-over with legacy pre-2017 cases and with boundary artefacts (cases filed in 2020, resolved in 2024, showing in both flows with no wait-time tag). We call the quantity **net filing surplus** (annual or cumulative), not backlog.

## The question

Eight years of data (2017-2024), 1,189 rows, seven jurisdictions, 94 case categories. **For cases filed in a given year, what fraction were also resolved in that year, and which jurisdiction has the largest year-ending surplus?**

## What we found

### The District Court has the largest 2024 net filing surplus

493,151 incoming, 435,255 resolved, a single-year net filing surplus of **57,896 cases**. That is an 88.3 percent in-year resolution ratio (bootstrap 95% CI [81.8, 95.1]) — roughly 12 of every 100 incoming 2024 cases were not resolved within 2024.

![Cumulative net filing surplus since 2017 by jurisdiction (2017 anchored at zero). The District Court line dominates; everything else is close to flat. This is a flow aggregate, not a pending-case stock.](plots/cumulative_backlog.png)

### Every other court is keeping pace or clearing

| Jurisdiction | 2024 incoming | 2024 resolved | Net (in − out) | Resolution ratio |
|---|---|---|---|---|
| District Court | 493,151 | 435,255 | **+57,896** | **88.3%** |
| High Court | 36,303 | 34,446 | +1,857 | 94.9% |
| Court of Appeal | 3,487 | 2,376 | +1,111 | **68.1%** |
| Special Criminal Court | 68 | 47 | +21 | 69.1% |
| Supreme Court | 231 | 239 | −8 | 103.5% |
| Central Criminal Court | 2,810 | 3,338 | **−528** | **118.8%** |
| Circuit Court | 63,048 | 66,417 | **−3,369** | **105.3%** |

### Per-judge load is the real story

Normalised by authorised judge strength, the District Court handles roughly 7,954 new cases per judge per year — an order of magnitude more than any other jurisdiction:

| Jurisdiction | Judges | Incoming per judge (2024) | Net surplus per judge |
|---|---|---|---|
| District Court | 62 | **7,954** | +934 |
| Circuit Court | 43 | 1,466 | −78 |
| High Court | 43 | 844 | +43 |
| Court of Appeal | 16 | 218 | +69 |
| Supreme Court | 10 | 23 | −1 |

This is the defensible version of the "drowning" framing from the Phase 0 draft: it is a **capacity-per-judge** claim, not a pending-stock claim.

### Inside the District Court, Road Traffic and Child Care lead the surplus

| Category | 2024 incoming | 2024 resolved | Net surplus | Resolution ratio |
|---|---|---|---|---|
| Road Traffic | 185,578 | 161,995 | **+23,583** | 87.3% |
| Liquidated Debt | 19,401 | 9,802 | +9,599 | **50.5%** |
| Child Care | 21,797 | 12,973 | **+8,824** | **59.5%** |

Bootstrap 95% intervals across the 2017-2024 panel (year-level resample, B=1,000):

- Road Traffic (District): 76.7%, 95% CI [68.2, 83.2]
- Child Care (District): 73.2%, 95% CI [66.6, 81.4]
- Breach of Contract (High Court): 20.1%, 95% CI [10.7, 34.7]

The 2024 single-year Child Care figure (60%) sits on the low tail of the multi-year distribution, which is a reminder that single-year headlines have ~15-point uncertainty bands.

### High Court Breach of Contract is volatile (probably a coding artefact)

Breach-of-Contract filings at the High Court are 246 (2021) → 1,458 (2022) → 336 (2023) → 1,435 (2024). That 4x-up-4x-down-4x-up pattern is almost certainly a reporting or coding boundary effect, not a real caseload swing. The 2024 single-year "17% resolution ratio" should be read against the panel bootstrap of 20% [11%, 35%].

## External cross-check

Two checks against the Courts Service 2024 Annual Report press release (RTE / Law Society Gazette, July 2025):

- Road Traffic 2024 incoming: ours = 185,578; press release = 185,578. Exact match.
- District Court Sexual Offences 2024 incoming: ours = 3,650; press release = 3,650. Exact match.

Both checks match exactly because the press release and our CSV share the same source. This confirms correct parsing but does NOT independently validate the stock.

## What this does not establish

- **No wait-time per case.** We explicitly withdraw the Phase 0 line "a new filing has a roughly 2-in-5 chance of waiting more than a year" — this dataset cannot support a survival claim.
- **No true pending stock.** Without the 2017 opening balance (not in the open CSV release), cumulative net filing surplus is not pending-case stock. Sensitivity analysis over 0-200k opening brackets preserves the sign of the District Court trajectory but leaves the absolute level indeterminate.
- **No causal attribution.** The Courts Service itself reported that 24 new judges appointed in 2023 reduced backlogs; that mechanism is external to our analysis.
- **No per-venue breakdown.** District Court has 24 venues; we do not see which.

## What it means

The District Court carries ~10x higher per-judge incoming load than any other jurisdiction and does not clear its year in 2024 (88% resolution ratio, CI 82-95%). Road Traffic is the single largest absolute contributor to the carry-over. A policy lever worth asking about is the overlap between criminal Road Traffic and the fixed-charge penalty notice regime — diverting more volume out of court altogether is a different question from "do we need more District Court judges?"

For a litigant in a Child Care or Liquidated Debt matter in the District Court: roughly half of Liquidated Debt cases and four in ten Child Care cases filed in 2024 were not resolved within 2024. We cannot say from this data how long the carry-over takes.

## How we did it

We downloaded the Courts Service 2017-2024 Annual Report datasets (data.courts.ie, CC BY 4.0), concatenated a 1,189-row panel, case-normalised the jurisdiction strings (the raw CSVs had "Court Of Appeal" and "Court of Appeal" as distinct strings), computed incoming-minus-resolved per row, bootstrapped 95% CIs on headline ratios (B=1,000), audited category stability via presence + YoY-jump flaggers, cross-checked against external press-release figures, and normalised 2024 flows by authorised judge strength. All code and intermediate artefacts are in the project directory.
