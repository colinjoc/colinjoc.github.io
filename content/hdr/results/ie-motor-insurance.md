---
title: "Where Did the Irish Motor Insurance Savings Actually Go?"
date: 2026-04-17
domain: "Irish Insurance Policy"
blurb: "In April 2021 Ireland introduced new rules that were supposed to cut personal-injury settlement costs by up to 50 percent and pass the savings on to drivers. Three years of Central Bank data show the savings were real — but drivers only saw about 40 percent of them in their premiums. Insurers kept the rest."
weight: 10
tags: ["insurance", "ireland", "consumer-policy", "motor", "regulation"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_motor_insurance/paper.md).*

## The Question

Irish motor insurance has been a political grievance for a decade. Premiums rose by roughly 36 percent between 2015 and 2019 while industry groups and consumer lobbies argued over whether claim costs justified the increases. The government's eventual response was a single big lever: in April 2021 a new schedule called the Personal Injuries Guidelines replaced the old "Book of Quantum" and was advertised as cutting the value of typical personal-injury settlements by somewhere between 30 and 50 percent.

The promise attached to all of this was simple. Claim costs fall, premiums fall in step, drivers save money. Three years of post-reform data now exist. Did that actually happen?

## What We Found

The guidelines did cut claim costs — but not at all in the way they were supposed to, and drivers only got a share of the benefit.

- The average cost of Irish motor insurance premiums fell about 15 percent in the three years after the reform, while the underlying cost of third-party-injury claims fell about 39 percent.
- Almost the entire claim-cost drop came from fewer people claiming, not smaller settlements. The number of injury claims per thousand policies fell by 39 percent, while the average settlement size barely budged.
- The policy's intended mechanism — steering more claimants through the state personal-injuries assessment board instead of the courts — did not happen. The mix between direct, litigated and assessment-board settlements barely moved.
- Inside the claims that did happen, mid-sized settlements in the 15,000 to 30,000 euro range got pushed down into the 0 to 10,000 euro band. The largest settlements, over 30,000 euros, were essentially unchanged.
- The loss ratio (what insurers paid out in injury claims for every euro of premium collected) dropped from 0.32 to 0.23 — meaning margins on this part of the business widened substantially.

Roughly 40 percent of the overall savings flowed to drivers as lower premiums. The other 60 percent stayed with insurers.

## Why That's Surprising

The political story around the reform was that it would cut the size of individual settlements. Every speech, press release and explainer focused on the schedule of payouts. What actually happened is that the average payout barely moved; it was the number of claims that collapsed. Something about the new schedule appears to have deterred people from claiming in the first place — either because smaller injuries are no longer worth pursuing, or because the reclassification of mid-range injuries into the lowest band made claims less attractive to legal funders.

The second surprise is that the mechanism the reform was specifically designed to push — routing more claims away from courts and through the state assessment board — did not move at all. The savings came from a pathway the legislation was not aiming at.

## What It Means

For drivers, the reform did deliver lower premiums, but you received roughly 40 cents of every euro of savings it generated. The remainder became insurer margin. Whether that is the right split is a political question, not a data question, but the data now exists to have that argument with real numbers.

For policymakers, the reform's stated mechanism (steer claimants to the assessment board) is not what delivered the outcome; the observed mechanism (fewer claims start in the first place) is a different lever and a different consequence. If the intent was fewer legal-system contacts per injury, the reform worked; if the intent was faster, cheaper resolution of the same volume of injuries, it did not.

One important caveat: Ireland's open data only covers third-party-injury claims, which make up roughly 30 to 50 percent of total motor claim costs. The remaining share — property damage and own-vehicle claims — is not public. The full insurer income picture could look different once those are included.

## How We Did It

The analysis uses three Central Bank of Ireland open-data releases from the [National Claims Information Database](https://opendata.centralbank.ie/): quarterly premium totals from 2010 to 2024, annual claim-settlement data by channel from 2015 to 2024, and annual claim-settlement data by cost band over the same period. Pre- and post-reform windows were compared with bootstrap confidence intervals, with exposure normalised by earned vehicle years to rule out the COVID driving-reduction confound.

## Further Reading

- [Central Bank of Ireland National Claims Information Database](https://opendata.centralbank.ie/) — the open-data portal underlying the analysis
- [Personal Injuries Guidelines explainer (Judicial Council)](https://judicialcouncil.ie/personal-injuries-guidelines/) — the reform itself
- [Full technical write-up](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_motor_insurance/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
