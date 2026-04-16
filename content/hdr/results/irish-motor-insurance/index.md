---
title: "Where Did the Irish Motor Insurance Savings Go?"
date: 2026-04-16
domain: "Irish Insurance"
blurb: "In April 2021 the government rolled out the Personal Injuries Guidelines, marketed as a mechanism to cut settlement costs by 30 to 50 percent and pass the savings to drivers. Did it work, and who actually got the money? Using the Central Bank's open claims database we decomposed the answer. The injury-claim cost really did fall — by 39 percent — but not by cutting per-claim settlements. It fell by making 39 percent fewer people claim. Consumer premiums fell 15 percent. The remaining savings stayed with insurers."
weight: 5
tags: ["insurance", "ireland", "policy-evaluation", "personal-injuries-guidelines"]
---

*Plain-language version. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_motor_insurance/paper.md).*

## The question

Irish drivers have spent most of the last decade watching their motor insurance premiums go up and then, more recently, come back down again. The headline numbers from the Central Bank's National Claims Information Database tell a clean arc: the average Irish motor insurance premium rose from roughly €493 per policy in 2015 to a 2019 peak of about €672, fell back to about €557 by 2023, and began climbing again in 2024 (€592).

The government's flagship intervention in this story is the **Personal Injuries Guidelines**, published by the Judicial Council and effective 24 April 2021. They replaced the old Book of Quantum with a new schedule of recommended settlement awards. The public promise at the time was that awards would fall by 30 to 50 percent, and that the savings would be passed on to consumers as lower premiums.

The question this analysis answers: **did the savings materialise, and who actually got them?**

## What we found

The Personal Injuries Guidelines did cause a large drop in third-party-injury claim costs — but not through the mechanism that was advertised.

### Per-claim settlements barely moved

If you compare the average third-party-injury settlement across 2017-2020 (after the Cost of Insurance Working Group reforms but before the Guidelines) with 2022-2024 (after the Guidelines), the numbers are effectively identical: about €38,350 pre, €38,290 post. The bootstrap 95 percent confidence interval on the difference spans a range of roughly minus €1,200 to plus €1,100. In other words, we cannot reject the null that per-claim severity did not change at all. The advertised 30-to-50-percent cut in the typical settlement did not happen.

### The entire cost drop is in frequency

What did change dramatically was how many people claimed. Per 1,000 active policyholders, the number of third-party-injury claimants fell from 5.71 per year in the pre-period to 3.48 in the post-period — **a 39 percent drop, bootstrap 95 percent confidence interval from minus 2.97 to minus 1.47 per 1,000**. When we normalise by earned vehicle years instead of policies to rule out the possibility that this is just leftover COVID-era reduced-driving, the number barely changes (−38.9 percent). The frequency drop is real and post-pandemic.

So roughly four in every ten people who would have made a third-party-injury claim under the old regime did not make one under the new one. Whether this is because the Guidelines genuinely deterred speculative claims, made the process less attractive to solicitors working on no-win-no-fee terms, or shifted the strategic economics of filing, is not directly answerable from the aggregate data. But the empirical signature is unambiguous: fewer claimants, same average settlement.

![Indexed to 2015. Premiums rose, fell, rose again. Per-claim injury cost drifted upward steadily. The red dashed line marks the April 2021 Personal Injuries Guidelines.](plots/premium_vs_claims.png)

### The cost-band shift is the smoking gun

The Central Bank also publishes settlement counts broken down into seven cost bands. This is where the actual mechanism becomes visible. Pre-Guidelines, about 33 percent of all third-party-injury claimants settled in the €15,000-€30,000 band. Post-Guidelines, that share fell to 22 percent — an 11.4 percentage-point drop. Over the same period, the share in the €0-€10,000 band rose from 17.6 percent to 31.9 percent — a 14.3 percentage-point gain. The bands above €30,000 barely moved.

The Guidelines did not cut big settlements. They moved mid-range settlements downward into the low band. Combined with the 39 percent drop in total claimants, the picture is that a substantial number of people who would have got a five-figure settlement under the old regime either received a sub-€10,000 settlement under the new one, or did not claim at all.

### The channel argument that was supposed to matter didn't

The standard narrative about the Personal Injuries Guidelines was that they would reduce legal costs by shifting claimants away from the courts and towards the Personal Injuries Assessment Board (PIAB). The Central Bank's data shows this did not happen. The share of claimants settling directly with the insurer moved from 49.0 percent to 48.3 percent. The share using PIAB moved from 16.1 percent to 16.5 percent. The share going to litigation moved from 34.9 percent to 35.2 percent. These are rounding-error changes. The intended mechanism — channel migration — is not how the savings were delivered.

### Who got the savings

Third-party-injury claim cost fell about 39 percent (the frequency fell and severity was essentially flat). The average premium per policy fell about 15 percent. The third-party-injury loss ratio — the fraction of each premium euro that gets paid out in third-party-injury claims — fell from 0.325 to 0.233.

Consumers received roughly 40 percent of the aggregate claim-cost savings as a premium cut. Insurers retained the remainder within the third-party-injury loss ratio.

## Why that's surprising (or not)

The Personal Injuries Guidelines were sold as a structural fix to the Irish insurance market: lower awards, passed through to lower premiums. The per-claim average award did not fall. Consumers did get about €100 per policy in annual savings. But the biggest share of the cost reduction came from a 40-percent collapse in claim numbers — the existence of which is either a sign that the previous system was structurally absorbing opportunistic claims the Guidelines now deter, or that the new system has made legitimate claimants worse off and less willing to file, or both. Both stories can be consistent with the data.

The insurance industry got to keep most of the loss-ratio improvement. Whether that translates into profit depends on things we cannot measure here — operating costs, reinsurance costs, capital charges — which together with the loss ratio make up the combined ratio. A falling loss ratio can in principle coexist with a flat combined ratio if expenses rose, though the magnitude of the 2022-2024 loss-ratio improvement would require implausibly large expense growth to offset entirely.

## What we cannot say from this data

- The Central Bank's open-data files include only third-party-injury claims. Property-damage and own-vehicle claims (windscreen, fire, theft) are not in the open export. Third-party-injury is historically about 30 to 50 percent of total claim cost, so the loss-ratio numbers here are partial. The overall loss ratio could in principle move differently if, for example, the Guidelines shifted settlement activity onto property-damage coverage.
- The data is national aggregate. It does not let us look at premium-or-claim inequality by postcode, by insurer, or by driver profile.
- There is no counterfactual — Northern Ireland and Great Britain motor insurance moved during the same period. A synthetic-control comparison would strengthen the causal interpretation; it has not been run here.
- "Profit" is not in the data. Loss ratio is one component of the combined ratio that measures underwriting profit.

## What it means

For a driver renewing in 2026: the 15-percent premium decline from the 2019 peak is real, and it is primarily due to the Guidelines. Expect more modest further gains from this mechanism — the frequency collapse has largely played out by 2024. The 6-percent premium increase in 2024 is consistent with severity drift (injury costs indexed up) starting to bite against a stabilised frequency.

For policy evaluation: the official story about why the Guidelines worked ("lower awards per case") is not what the aggregate data shows. The Guidelines worked through claim deterrence. That matters for how the next generation of similar reforms should be designed — the intervention's real lever was not the award schedule itself but the signal it sent to the claims-filing pipeline. If that signal can be replicated in other consumer-complaint areas (banking-fee disputes, insurance complaints, housing deposits, small-claims), the same structural shift could be delivered without changing the headline award numbers at all.

For Irish voters: roughly 40 percent of the government's claim-cost-reduction went to you; 60 percent stayed with insurers as margin. Whether that's the right split is a political question, not a statistical one.

## How we did it

We downloaded the three publicly available Central Bank National Claims Information Database CSVs — premiums, claim settlements by channel, and claim settlements by cost band — and computed pre-Guidelines (2017-2020) and post-Guidelines (2022-2024) aggregates. We used 2000-resample bootstrap confidence intervals on every pre-post difference, normalised exposure by earned vehicle years to rule out the COVID driving effect, and decomposed the frequency-severity-channel-costband contributions. Code, data pipeline, and all reviewer-mandated experiments are in the linked paper.
