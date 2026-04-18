---
title: "Are Irish developers hoarding permissions? A database bug says otherwise"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "For years, Irish politics has blamed developers for sitting on a quarter of all granted housing approvals. Most of that number was two databases failing to talk to each other."
weight: 12
tags: ["housing", "ireland", "planning-permissions", "data-quality", "lapsed-permissions"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lapsed_permissions/paper.md) has the format-audit tables and the cluster-bootstrap confidence intervals. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** The widely cited claim that 23 to 27 percent of Irish planning permissions never turn into homes is mostly a measurement artefact. The real lapse rate is closer to 10 percent — in line with the United Kingdom and New Zealand. Ireland is not uniquely afflicted by developer hoarding.

## The Question

Irish housing debate has been animated for years by the claim that the country has tens of thousands of "dead" planning permissions — approvals granted but destined never to produce a home. The 2024 Housing Commission report cites about 60,000 live permissions. Critics argue a large fraction are speculative, abandoned, or parked while developers wait for better market conditions. The 2025 Planning and Development (Amendment) Act responded by creating a mechanism to extend uncommenced permissions by up to three more years.

Nobody had actually measured how many permissions lapse. Earlier studies reported 23 to 27 percent. We set out to check the number at national level, for every residential permission granted between 2014 and 2019.

## What we found

The real lapse rate is about 9.5 percent, not 23 or 27. The earlier headlines were inflated by a technical problem nobody had diagnosed: the two administrative databases involved record the same permission using different application-number formats, and the mismatched ones were being silently counted as lapsed.

- Simple numeric application numbers — used by rural councils like Carlow, Laois, and Leitrim — match between the two databases 88.6 percent of the time.
- Complex application numbers with slashes and letter prefixes — used by Cork County, Dublin City, and Donegal — match only 53.0 percent of the time.
- Cork County alone accounts for 37 percent of all unmatched records nationally, almost entirely because of numbering conventions.
- On a clean subsample where the underlying residential-units field is properly populated, the real lapse rate is 9.5 percent, with a confidence range of 4.4 to 15.6 percent.
- International comparators sit in the same range: 6 to 14 percent in the United Kingdom, 10 to 20 percent in New Zealand.
- Larger schemes lapse more often than small ones — 19 percent for schemes of 50 or more units, 9 percent for single homes — which is consistent with the economic theory of waiting to build when costs are uncertain.
- An earlier version of this study used a predictive model that looked impressive. On audit, the model was almost entirely predicting which councils use which number format, not actual lapse risk. Once the proxy was removed, it performed barely better than chance.

## Why that matters

The 20-to-30-percent lapse headline has shaped Irish housing policy for years. It fed a narrative of developer hoarding, of approvals gathering dust while the crisis deepened, and of a need for strong-arm state intervention. The actual number is less than half that, and most of the apparent lapse was a database-join artefact nobody had bothered to audit.

The deeper lesson is about data quality. Two public-sector administrative systems — the national planning register and the building-control database — record the same object using different number formats. Nobody harmonised them. When researchers tried to match permissions to commencements, failures were invisibly labelled "lapsed". A policy problem was manufactured out of a metadata mismatch.

Politically, the real rate matters too. At about 10 percent, lapses are a bounded problem — the normal rate at which any market option goes unexercised — not evidence of pervasive bad faith.

## What it means in practice

**For policymakers.** The 2025 Amendment Act's extension mechanism addresses a real but bounded problem — roughly 3,000 to 9,000 permissions out of 60,000, not the 15,000-plus implied by the earlier rates. It will help, but it will not transform housing delivery. Whether developers actually use extended permissions depends on the same economics that made them pause — construction costs, financing, market demand — rather than on the validity clock.

**For journalists and analysts.** The right number to cite is approximately 10 percent. The 23 to 27 percent figures should appear only as database-contaminated upper bounds. The narrative of developers sitting on a quarter of all approvals is not supported by the cleaner data.

**For anyone working with Irish administrative data.** Always test whether a database-linkage result is robust to the quality of the join. A model that looked like it predicted lapse was in fact predicting which council used which number format.

## How we did it

We linked two public datasets: the [National Planning Application Register](https://www.gov.ie/) from the Department of Housing, covering 491,206 applications, and the [Building Control Management System](https://nbco.localgov.ie/) commencement-notice database. For residential permissions granted between 2014 and 2019, we computed the share without a matching commencement notice. We then audited match quality by application-number format, compared simple versus complex formats, and computed confidence intervals that account for clustering at the council level. Each council-level estimate carries a reliability flag based on its match rate.

## Further reading

- [National Building Control Office](https://nbco.localgov.ie/) — source for the commencement-notice database.
- [Department of Housing, Local Government and Heritage](https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/) — source for the planning register.
- [Housing Commission Final Report (2024)](https://www.gov.ie/en/publication/e8145-report-of-the-housing-commission/) — context for the "60,000 live permissions" figure.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lapsed_permissions/paper.md).
