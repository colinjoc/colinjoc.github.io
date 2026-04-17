---
title: "How Many Irish Planning Permissions Actually Lapse?"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "Irish political debate assumes that a large share of granted housing permissions never turns into a home — with estimates of 20% to 30% commonly cited. We linked the national planning register to the building-control database and found the real lapse rate is closer to 10%. The larger headline numbers were produced by a simple technical problem: the two databases use incompatible application-number formats, so many commencements that did happen could not be matched against their permissions."
weight: 12
tags: ["housing", "ireland", "planning-permissions", "data-quality", "lapsed-permissions"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lapsed_permissions/paper.md).*

## The Question

For years, Irish housing debate has been animated by the claim that the country has tens of thousands of "dead" planning permissions — approvals that were granted but will never produce a home. The 2024 Housing Commission report cites roughly 60,000 live permissions, and critics argue a large fraction of them are speculative, abandoned, or sitting idle while developers wait for market conditions to improve. The 2025 Planning and Development (Amendment) Act responded by creating a mechanism to extend uncommenced permissions for up to three more years.

But nobody had carefully measured how many permissions actually lapse. Earlier studies reported lapse rates of 23% to 27%. We set out to check the number at the national level, for every residential permission granted between 2014 and 2019.

## What We Found

**The real lapse rate for Irish residential permissions is about 9.5% — not 23% or 27%.** The earlier headline figures were inflated by a technical problem nobody had diagnosed: the two databases involved use different application-number formats, so many permissions that *did* have a matching commencement notice could not be linked to it.

- Simple numeric application numbers — used by rural councils like Carlow, Laois, Leitrim — match between the two databases 88.6% of the time.
- Complex application numbers with slashes and letter prefixes — used by Cork County, Dublin City, Donegal — match only 53.0% of the time.
- Cork County alone accounts for 37% of all unmatched records nationally, almost entirely because its numbering convention is incompatible with the building-control database's convention.
- When we restricted the analysis to a clean subsample where the underlying residential-units field is properly populated, the lapse rate was 9.5%, with a confidence range of 4.4% to 15.6%.
- That rate is in line with international comparators: 6% to 14% in the United Kingdom, 10% to 20% in New Zealand. Ireland is not an outlier.
- Larger schemes lapse more often than small ones (19% for 50+ unit schemes versus 9% for single homes) — consistent with economic theory of waiting to build when costs are uncertain.
- An earlier version of the study used a tree-based model that appeared to predict lapse well. On audit, the model was almost entirely predicting *which councils use which number format*, not actual lapse risk. Once that proxy was removed, the model performed barely better than chance.

## Why That's Surprising

The 20-to-30-percent lapse headline has shaped Irish housing policy for years. It fed a narrative of developer hoarding, of approvals gathering dust while the housing crisis deepened, of a need for strong-arm state intervention to force use of existing permissions. The actual number is less than half that, and most of the apparent lapse was a database-join artefact nobody had bothered to audit.

The deeper lesson is about data quality. Two public-sector administrative systems — the national planning register and the building-control database — record the same underlying object (a planning permission) using different number formats. Nobody harmonised them. When researchers tried to match permissions to commencements, the matches that failed were invisibly labelled as "lapsed." A policy problem was manufactured out of a metadata mismatch.

The real lapse rate matters politically too: at around 10%, it is a bounded problem, consistent with the normal rate of exercise of any option in any market. It is not evidence of pervasive bad faith by developers.

## What It Means

For a policymaker, the implication is that the 2025 Amendment Act's extension mechanism addresses a real but bounded problem — roughly 3,000 to 9,000 permissions out of the 60,000 live stock, not the 15,000+ implied by the earlier rates. It will help, but it will not transform housing delivery. Whether developers exercise extended permissions depends on the same economics that made them pause in the first place — construction costs, financing, market demand — rather than on the validity clock.

For a housing journalist or analyst, the right number to cite is now approximately 10%, with the raw 23-27% figures quoted only as database-contaminated upper bounds. The narrative of "developers sitting on a quarter of all approvals" is not supported by the cleaner data.

For anyone working with Irish administrative data, there is a cautionary tale: always test whether a database-linkage result is robust to the quality of the join. In this case, a model that looked like it predicted lapse was actually predicting which council used which number format.

## How We Did It

We linked two public datasets: the [National Planning Application Register](https://www.gov.ie/) from the Department of Housing, covering 491,206 applications, and the [Building Control Management System](https://nbco.localgov.ie/) commencement-notice database. For residential permissions granted between 2014 and 2019, we computed the share without a matching commencement notice. We then audited the match quality by application-number format, compared simple versus complex formats, and computed confidence intervals that account for clustering at the council level. A reliability flag was attached to each council-level estimate based on its match rate.

## Further Reading

- [National Building Control Office](https://nbco.localgov.ie/) — source for the commencement-notice database.
- [Department of Housing, Local Government and Heritage](https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/) — source for the planning register.
- [Housing Commission Final Report (2024)](https://www.gov.ie/en/publication/e8145-report-of-the-housing-commission/) — context for the "60,000 live permissions" figure.
- [Detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lapsed_permissions/paper.md) — with the full format-audit tables and cluster-bootstrap confidence intervals.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
