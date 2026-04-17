---
title: "What's Actually Blocking Irish Housing Delivery?"
date: 2026-04-17
domain: "Irish Housing"
blurb: "Ireland grants about 38,000 residential planning permissions a year. It needs roughly 85,000 to hit the government's housing target. That gap — not slow planning boards, not judicial reviews, not permission lapse — is the main reason Ireland isn't building enough homes. Every efficiency fix we tested, combined, closes less than a third of the shortfall."
weight: 1
tags: ["housing", "ireland", "planning-permission", "bottleneck-analysis", "meta-analysis", "synthesis", "flagship"]
---

*Flagship synthesis pulling together 13 projects on this site. Full technical detail in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_housing_bottleneck/paper.md).*

## The question everyone asks

Why can't Ireland build enough homes? People blame slow planning decisions, judicial reviews, developers sitting on permissions, the LDA being too small, not enough construction workers. **Which of these actually matters most — and by how much?**

We combined data from 13 separate studies on this site to find out.

## The short answer

**Ireland doesn't grant enough planning permissions.** Everything else is secondary.

The government's Housing for All target is 50,500 homes per year. Ireland currently grants about 38,000 residential planning permissions per year. About 60% of those become actual homes (the rest lapse, get delayed, or fall into an administrative gap). That gives roughly 23,000 effective completions — less than half the target.

To close that gap, Ireland needs roughly **85,000 permissions per year** — more than double what it grants today.

## What about all the other problems?

We tested every commonly-cited obstacle. Here's what each one is actually worth:

| Problem | Extra homes per year if fixed | % of the gap it closes |
|:---|---:|---:|
| **Grant more permissions** (+10,000) | **+6,100** | **37%** |
| Better completion-certificate filing | +3,267 | 20% |
| Faster planning-board decisions (18 weeks) | +1,060 | 6.5% |
| Remove judicial review entirely | +1,060 | 6.5% |
| Halve the permission lapse rate | +701 | 4.3% |
| Faster construction | ~0 | 0% (shifts timing only) |
| Triple the LDA | ~0 | 0% (buys existing homes, doesn't add supply) |

**All efficiency fixes combined: about 5,000 extra homes per year.** That's only 31% of the 16,300-home annual gap.

The other 69% can only come from granting more permissions in the first place — and having enough builders to construct them.

![Left: how many extra homes each fix delivers. Right: even combining every fix, 69% of the gap remains.](plots/bottleneck_ranking.png)

## Why permission volume matters more than everything else

Think of it like a factory. You can speed up every machine on the production line, but if you're only feeding in half the raw materials you need, the factory still under-produces. Planning permissions are the raw material of housing delivery. Ireland is feeding in 38,000 when it needs 85,000.

Speeding up An Bord Pleanala, reducing judicial reviews, and cutting lapse rates are all worth doing — they add about 1,000 homes per year each. But they cannot substitute for the missing permissions.

## The construction ceiling

Even if permissions doubled tomorrow, Ireland's construction sector currently delivers about 35,000 homes per year. That's a workforce of roughly 160,000 — short of the estimated 200,000 needed. So the real policy package needs two things happening together:

1. **More permissions** — through zoning reform, density increases, simpler application processes
2. **More construction capacity** — through workforce training, construction immigration, and modular building

In that order of priority. Not the reverse.

## How confident are we?

Very. We ran 5,000 simulations varying every input within its uncertainty range. Permission volume came out as the #1 constraint in **every single simulation**. The ranking holds whether we assume 50% or 100% of self-builds complete. It holds across Dublin and non-Dublin. It holds for apartments and houses separately.

## What we're NOT saying

- **Not that other fixes are worthless.** Restoring the planning board to 18-week decisions is worth ~1,000 homes a year. That matters.
- **Not that 35,000 is a hard ceiling.** Construction output could grow with investment. The ceiling is what the sector delivers today, not what it could deliver.
- **Not that this is permanent.** If permissions triple, the bottleneck shifts to construction capacity. Constraints move.

## The studies behind this

This pulls together: [housing pipeline](/hdr/results/irish-housing-pipeline/) | [commencement cohort](/hdr/results/irish-commencement-cohort/) | [lapsed permissions](/hdr/results/irish-lapsed-permissions/) | [LDA delivery](/hdr/results/irish-lda-delivery/) | [SHD judicial review](/hdr/results/irish-shd-judicial-review/) | [LRD vs SHD](/hdr/results/irish-lrd-vs-shd-jr/) | [ABP decision times](/hdr/results/irish-abp-decision-times/) | [pipeline yield](/hdr/results/irish-housing-pipeline-e2e/) | [JR tax on supply](/hdr/results/irish-jr-tax-on-supply/) | [courts backlog](/hdr/results/irish-courts-backlog/) | [graduate emigration](/hdr/results/irish-emigration/) | [Irish gender pay gap](/hdr/results/irish-gender-pay-gap/) | [UK gender pay gap](/hdr/results/uk-gender-pay-gap/)

## How we did it

Tracked 38,000 annual permissions through five pipeline stages (grant, commencement, construction, certification, occupation) using national planning-register and building-control data. Tested five analytical approaches. Stress-tested the ranking with 5,000 Monte Carlo simulations. Independent blind reviewer caught a double-counting error between planning-board speed and judicial-review removal (they share the same channel), revising combined efficiency from 37% to 31% of the gap.
