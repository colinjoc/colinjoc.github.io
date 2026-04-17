---
title: "Predicting which US cities will have a housing crash first: you can't"
date: 2026-04-17
domain: "Real Estate Economics"
blurb: "A lot of commentary claims that metro-level housing crashes are easy to see coming in public data. We checked. The apparent signal dissolves the moment you apply honest statistical diagnostics, and what looks like prediction turns out to be momentum persistence in a handful of distressed small towns."
weight: 20
tags: ["housing", "real-estate", "prediction", "null-result", "early-warning"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/housing_crashes/paper.md).*

## The Question

Every housing-market cycle brings a wave of commentary claiming that this city will crash first, that one will crash next, and that the patterns are visible in the data if you know where to look. With the sharp rate shock of 2022–2023, those claims were everywhere. We asked a narrower version of the question: using only publicly available data — home price indices, listing inventory, days on market, the national mortgage rate — can you actually predict, out of sample, which US metropolitan areas will see a ten-percent price decline over the next twelve months?

## What We Found

You cannot. Not from public data, not at this cycle's signal-to-noise ratio.

- A carefully built statistical model shows an apparent signal about five times stronger than random guessing — exactly the kind of number people point to when they claim crash prediction is working.
- Every honest check we ran on that signal made it evaporate. Resampling the data in a way that respects the clumpy, autocorrelated structure of metro-level housing markets produced a confidence interval wide enough to include "no real predictive power at all."
- A permutation test that scrambles which cities crashed, keeping everything else fixed, found our model is statistically indistinguishable from luck.
- The simplest possible forecast — "places that have been falling will keep falling" — is actually more accurate than the ten-feature model.
- The pattern is carried by about two distressed rural micropolitan areas (Clarksdale, Mississippi first among them). Remove those, and half the apparent accuracy disappears.

## Why That's Surprising

Housing-crash prediction has a deep academic literature and an even deeper popular-commentary presence. The quiet assumption in both is that enough features plus enough model will eventually crack the problem. Our diagnostics show that on the data the public has access to, the problem hasn't been cracked — it has been hidden by inference procedures that do not account for the way housing markets are correlated across time.

The bigger surprise is what the "crashing markets" actually are. The places that crossed the ten-percent-decline threshold in 2022–2023 are not the Austins and Phoenixes of the popular narrative. They are mostly rural towns in long-term population decline — Clarksdale, Johnstown, Beeville, Natchez. When the most influential training example is a small Delta-region town losing its population, "we predict housing crashes" is not the claim the data supports. What we predict is continued decline in places already in decline.

## What It Means

For homeowners and buyers anxious about whether their metro is about to tank: the honest answer is that public-data early-warning models do not yet work well enough to give you a reliable answer. Anyone selling that certainty is selling you momentum repackaged.

For financial journalists and forecasters, it is a specific methodological warning. Any claim that a metro-level crash model works should come with three specific checks: a resampling procedure that respects how metros cluster, a permutation test that respects the time structure of the panel, and a demonstration that the full model beats a one-feature momentum score. Without all three, apparent predictive power is almost certainly an artefact.

For policymakers and regulators, it is a case for better data. Public data tells you about the aftermath. The inputs that might genuinely give early warning — mortgage-level credit data, regulatory filings — sit behind restricted access.

## How We Did It

We built a monthly metro-level panel by joining [Zillow's Home Value Index](https://www.zillow.com/research/data/), [Realtor.com's metro inventory series](https://www.realtor.com/research/data/), and the [Federal Reserve Economic Data series for 30-year mortgage rates](https://fred.stlouisfed.org/series/MORTGAGE30US). We trained a regularised linear model on data through mid-2022 and tested on the 2022-23 rate-shock window, then subjected the apparent signal to a metro-clustered bootstrap, a within-panel block permutation, a single-feature dominance check, and a leave-one-metro-out analysis. All four diagnostics pointed the same way.

## Further Reading

- Gourinchas and Obstfeld (2012), "Stories of the Twentieth Century for the Twenty-First"
- Schularick and Taylor (2012), "Credit Booms Gone Bust" — *American Economic Review*
- Beutel, List, and von Schweinitz (2019), "Does machine learning help us predict banking crises?"
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/housing_crashes/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
