---
title: "Where the Irish motor insurance savings went"
date: 2026-05-08
domain: "Public Policy / Insurance"
blurb: "Ireland's 2021 injury-award reform delivered the cuts insurers were promised. Drivers got about two-fifths of the windfall."
weight: 45
tags: ["public-policy", "insurance", "ireland", "ncid", "personal-injuries-guidelines", "claims"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_motor_insurance/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Ireland's April 2021 Personal Injuries Guidelines (PIG) — the judicial reform sold as a way to lower motor premiums — cut the rate at which drivers lodge third-party-injury claims by 39 percent. Premiums fell about 15 percent. The arithmetic is uncomfortable: consumers received roughly two-fifths of the savings; insurers kept the rest.

<figure>
  <img src="plots/premium_vs_claims.png" alt="Average premium and third-party-injury claim cost per policy, Ireland, 2015-2024." />
  <figcaption>Average premium per policy and third-party-injury claim cost per policy, 2015-2024. The PIG took effect in April 2021. Source: Central Bank of Ireland, NCID open-data portal.</figcaption>
</figure>

## The question

For most of the last decade Irish motor insurance has been a political grievance with the unusual feature of having a numbered list of villains. Premiums climbed roughly 36 percent between 2015 and 2019, peaking near €672 per policy. The Cost of Insurance Working Group, the Judicial Council Act of 2019 and finally the Personal Injuries Guidelines of April 2021 were the staged government response. The guidelines replaced the older Book of Quantum and were marketed with a specific, testable promise: settlement values for personal injuries would fall 30 to 50 percent, and savings would be passed through to drivers. After almost three full post-reform years of data, we ask the question the political economy makes inevitable. Did consumers get the savings, or did the insurance industry?

## What we found

The reform worked, but not in the way the official explanation suggested. Using the Central Bank of Ireland's National Claims Information Database (NCID), we compared a pre-reform window (2017-2020) to a post-reform window (2022-2024), skipping 2021 as the transition year.

The headline change is in claim **frequency**, not severity. The number of third-party-injury (TPI) claims fell from 5.71 to 3.48 per thousand policies — a 39 percent drop, with a bootstrap 95 percent confidence interval that excludes zero by a wide margin. Average settlement size, by contrast, was almost exactly unchanged (-0.2 percent, with a confidence interval that crosses zero). PIG did not lower the typical award. It lowered the rate at which awards happen.

The mechanism the policy was designed around — funnelling claims away from litigation and toward the state-run Personal Injuries Assessment Board (PIAB) — barely moved at all. The split between direct, litigated and PIAB settlements changed by less than one percentage point in any direction. Whatever PIG did, it did not do by changing the route claims took through the system.

The cost-band data tells the actual story. Mid-value claims of €15,000 to €30,000 collapsed from a third of all settlements (33.4 percent) to just over a fifth (22.0 percent) — a fall of 11.4 percentage points. The €0-10,000 band almost doubled, gaining 14.3 percentage points. Claims above €30,000 — the genuinely serious injuries — barely moved. PIG did not cut the largest awards. It compressed the middle of the distribution downward, reclassifying many mid-value injuries into a much cheaper band.

We then asked how much of that windfall reached drivers. Total TPI claim cost per vehicle year fell 39 percent, from €219 to €134. Average premiums fell 15 percent, from €672 to €572. The TPI loss ratio — claim costs divided by earned premium — fell from 0.32 to 0.23. Dividing the 15-point premium cut by the 39-point cost cut gives a pass-through of roughly 40 percent. The remaining three-fifths of the saving stayed with the underwriters, at least within the third-party-injury slice we can observe.

## Why that matters

Irish motor insurance has been the subject of half a dozen formal reviews and a piece of constitutional legislation. The political case for the reform was that pricing was unfairly high relative to the underlying risk, and that cheaper claims would mean cheaper cover. The first half of that promise is, on the data, comprehensively delivered. The second half is partially delivered — and the gap between the two is large enough to matter to every household with a car.

It also matters how the saving was generated. A reform that lowered the cost of every settlement uniformly would be a clean transfer from claimants to insurers (and onward, in part, to drivers). A reform that suppressed claims altogether — as appears to have happened — has different distributional consequences. Some of the missing claimants were probably opportunistic; some were probably people with genuine but modest injuries who concluded the new guidelines made a claim not worth pursuing. The data we have cannot separate the two.

## What it means in practice

**For drivers.** The premium cut is real and roughly €100 a year on the average policy. It is also smaller than the cost reduction it was paid for with. If you negotiated a renewal between 2022 and 2024, the savings you saw represent about 40 percent of the underlying improvement; the rest sits on insurer balance sheets as margin within the TPI window.

**For policymakers.** The headline figure of "39 percent claims-cost reduction" is right, but the mechanism is not the one the legislation targeted. Channel mix into PIAB barely moved. The actual lever was the guideline values themselves applied to mid-range injuries — a fact relevant to any future review of how much further the schedule should be tightened, and to whether pass-through should be regulated rather than left to market competition. The 2024 government commitment to a further 30 percent awards reduction is being made on the basis of an outcome that, on these numbers, did not flow through to consumers in full.

**For insurers.** The TPI loss ratio fell almost a third — from 0.32 to 0.23 — across the post-reform window. That is a meaningful cushion against claim-cost inflation, the renewed premium uptick visible in 2024, and the unfinished business of property-damage and own-vehicle claim trends, which the open data does not let us see.

## How we did it

The Central Bank of Ireland publishes three NCID open-data files: quarterly premium aggregates from 2010 onward, and annual third-party-injury claim settlements broken down by channel and by cost band from 2015 onward. The premium series goes through 2024 Q4; the claims series ends in 2024. Together they describe national aggregates — there is no Eircode, no insurer-level and no non-injury claim detail in the public release. The TPI restriction is the most consequential limitation: TPI is historically 30 to 50 percent of total claim cost, so the loss-ratio numbers in this study are partial.

We compared the four pre-reform years 2017-2020 to the three post-reform years 2022-2024, treating 2021 as a transition year. Bootstrap 95 percent confidence intervals (n = 2,000 resamples) on every pre-versus-post difference flag the frequency change, the premium change and the loss-ratio change as statistically robust, and the severity change as indistinguishable from zero. To rule out a COVID-driving-reduction artefact, we re-ran the headline frequency calculation on a per-vehicle-year basis using NCID earned vehicle years; the 39 percent drop is unchanged. The cost-band decomposition is a straightforward share-of-claimants calculation per band. We did not run a synthetic-control comparison against Northern Ireland or the United Kingdom, and we cannot decompose insurer profits — only the loss ratio, which is one component of the combined ratio. Both are flagged as priorities for follow-up work if the relevant data become available.

## Further reading

- [Central Bank of Ireland NCID open-data portal](https://opendata.centralbank.ie/) — premium and claims aggregates used here.
- [Personal Injuries Guidelines (Judicial Council, 2021)](https://judicialcouncil.ie/personal-injuries-guidelines/) — the schedule that replaced the Book of Quantum on 24 April 2021.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_motor_insurance/paper.md) — bootstrap diagnostics, exposure normalisation, channel and cost-band tables.
