---
title: "Drivers got 40 cents of every euro the insurance reform saved"
date: 2026-04-17
domain: "Irish Insurance Policy"
blurb: "Ireland's big 2021 insurance reform cut claim costs by roughly two-fifths. Premiums fell by a lot less. Follow the missing money."
weight: 10
tags: ["insurance", "ireland", "consumer-policy", "motor", "regulation"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_motor_insurance/paper.md) has the bootstrap confidence intervals and the exposure-normalisation check. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** The 2021 Personal Injuries Guidelines cut the cost of Irish motor-injury claims by about 39 percent. Premiums fell by only 15 percent. Roughly 40 cents of every euro the reform saved flowed to drivers. The other 60 cents stayed with insurers.

## The Question

Irish motor insurance has been a political grievance for a decade. Premiums rose about 36 percent between 2015 and 2019 while industry and consumer groups argued over whether claim costs justified the increases. The government's response was a single big lever: in April 2021 a new schedule called the Personal Injuries Guidelines replaced the old "Book of Quantum" and was advertised as cutting the value of typical personal-injury settlements by somewhere between 30 and 50 percent.

The promise was simple. Claim costs fall, premiums fall in step, drivers save. Three years of post-reform data now exist. Did that actually happen?

## What we found

The guidelines did cut claim costs — but not in the way they were supposed to, and drivers only got a share of the benefit.

- The average Irish motor insurance premium fell about 15 percent in the three years after the reform. The underlying cost of third-party-injury claims fell about 39 percent.
- Almost the entire claim-cost drop came from fewer people claiming, not smaller settlements. Injury claims per thousand policies fell 39 percent. The average settlement size barely budged.
- The policy's intended mechanism — steering more claimants through the state assessment board rather than the courts — did not happen. The mix between direct, litigated, and assessment-board settlements barely moved.
- Inside the claims that did still happen, mid-sized settlements in the EUR 15,000 to 30,000 band got pushed down into the EUR 0 to 10,000 band. Settlements above EUR 30,000 were essentially unchanged.
- The loss ratio — what insurers paid out in injury claims for every euro of premium collected — fell from 0.32 to 0.23. Margins on this slice of the business widened substantially.

Roughly 40 percent of the overall savings flowed to drivers as lower premiums. The other 60 percent stayed with insurers.

## Why that matters

The political story around the reform was that it would cut the size of individual settlements. Every speech, press release, and explainer focused on the schedule of payouts. What actually happened is that the average payout barely moved — the number of claims collapsed. Something about the new schedule deterred people from claiming at all, either because smaller injuries were no longer worth pursuing, or because the reclassification of mid-range injuries into the lowest band made claims less attractive to legal funders.

The second surprise is that the mechanism the reform was specifically designed to activate — routing more claims through the state assessment board — did not move at all. The savings came from a pathway the legislation was not aiming at.

## What it means in practice

**For drivers.** The reform did deliver lower premiums. You received about 40 cents of every euro of savings it generated. The rest became insurer margin. Whether that split is right is a political question, not a data question, but the data now exists to have the argument with real numbers.

**For policymakers.** The reform's stated mechanism (steer claimants to the assessment board) is not what delivered the outcome. The observed mechanism (fewer claims start in the first place) is a different lever and a different consequence. If the intent was fewer legal-system contacts per injury, the reform worked. If the intent was faster, cheaper resolution of the same volume of injuries, it did not.

**One important caveat.** Ireland's open data only covers third-party-injury claims, which make up roughly 30 to 50 percent of total motor claim costs. Property damage and own-vehicle claims are not published. The full insurer income picture could look different once those are included.

## How we did it

The analysis uses three Central Bank of Ireland open-data releases from the [National Claims Information Database](https://opendata.centralbank.ie/): quarterly premium totals from 2010 to 2024, annual claim-settlement data by channel from 2015 to 2024, and annual settlement data by cost band over the same period. Pre- and post-reform windows were compared with bootstrap confidence intervals, and exposure was normalised by earned vehicle years to rule out the pandemic-era driving-reduction confound.

## Further reading

- [Central Bank of Ireland National Claims Information Database](https://opendata.centralbank.ie/) — the open-data portal underlying the analysis.
- [Personal Injuries Guidelines explainer (Judicial Council)](https://judicialcouncil.ie/personal-injuries-guidelines/) — the reform itself.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_motor_insurance/paper.md).
