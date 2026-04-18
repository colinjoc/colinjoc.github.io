---
title: "Predicting Which US Cities Will Crash First: You Can't"
date: 2026-04-17
domain: "Real Estate Economics"
blurb: "Every cycle, commentators claim they can see the next housing crash coming. Can they, actually? We checked."
weight: 20
tags: ["housing", "real-estate", "prediction", "null-result", "early-warning"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/housing_crashes/paper.md) has the diagnostics. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** With only the housing data the public can download, nobody — not us, not the commentators — can reliably pick which American city will crash next. The apparent signal turns out to be momentum in a handful of small rural towns in long-term decline.

## The Question

Every housing cycle brings the same story. Someone points at a chart, names a few cities, and predicts the next crash. With the sharp rise in mortgage rates in 2022 and 2023, those predictions were everywhere.

We asked a tighter version of the question. Using only what anyone can download — home-price indices, listings, days on market, the national mortgage rate — can you actually predict, ahead of time, which American metros will see home prices fall by more than 10 percent over the next year?

## What we found

You cannot. Not from public data, not at the signal-to-noise ratio this cycle produces.

- A carefully built statistical model looked about five times more accurate than random guessing. That is the kind of number people point to when they claim crash prediction is working.
- Every honest check we ran on that signal made it evaporate. Accounting for the way housing markets move together across time and regions widened the confidence interval so much it included "no real predictive power at all".
- A fair comparison test — scramble which cities crashed and rerun the model — found our prediction was statistically indistinguishable from luck.
- The simplest possible forecast — "places that have already been falling will keep falling" — was actually more accurate than our ten-feature model.
- The whole apparent signal rested on two distressed rural towns, with Clarksdale, Mississippi at the top. Remove those, and half the accuracy went with them.

## Why that matters

Housing-crash prediction has a deep academic literature and an even deeper popular-commentary presence. The shared assumption is that enough data plus enough model will eventually crack it. On public data, at this cycle's signal-to-noise ratio, the problem has not been cracked. It has been hidden by statistical procedures that do not account for how housing markets are correlated over time and space.

The bigger surprise is which markets are doing the "crashing". The places that fell more than 10 percent in 2022 and 2023 are not Austin and Phoenix. They are mostly rural towns in long-term population decline — Clarksdale, Johnstown, Beeville, Natchez. When the single most influential example in the training data is a small Delta-region town losing its population, "we predict housing crashes" is not the claim the data supports. What we predict is continued decline in places already in decline.

## What it means in practice

**For homeowners and buyers worried about whether their city is next.** The honest answer is that public-data early-warning models do not yet work well enough to give you a reliable one. Anyone selling that certainty is selling momentum repackaged.

**For journalists and forecasters.** Any claim that a metro-level crash model works should come with three specific checks: a resampling procedure that respects how metros cluster together, a time-aware shuffle test, and a demonstration that the model beats a simple one-feature momentum score. Without all three, the apparent signal is almost certainly an artefact.

**For policymakers and regulators.** Public data tells you about the aftermath. The inputs that might give real early warning — mortgage-level credit data, regulatory filings — sit behind restricted access.

## How we did it

We built a monthly panel for every metro area in America by joining [Zillow's home value index](https://www.zillow.com/research/data/), [Realtor.com's inventory data](https://www.realtor.com/research/data/) and the [Federal Reserve's 30-year mortgage rate series](https://fred.stlouisfed.org/series/MORTGAGE30US). The model trained on data through mid-2022 and was tested on the 2022–23 rate-shock window. We then put the apparent signal through four independent stress tests. All four pointed the same way: no signal.

## Further reading

- Gourinchas & Obstfeld (2012), "Stories of the Twentieth Century for the Twenty-First".
- Schularick & Taylor (2012), "Credit Booms Gone Bust", *American Economic Review*.
- Beutel, List & von Schweinitz (2019), "Does machine learning help us predict banking crises?".
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/housing_crashes/paper.md).
