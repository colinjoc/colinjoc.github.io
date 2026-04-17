---
title: "Can We Predict Which Housing Markets Crash First? Probably Not."
date: 2026-04-14
domain: "Real Estate / Economic Forecasting"
blurb: "We tried to predict which US metros would experience a 10 percent home-price decline in the 2022-2023 cycle using publicly-available data -- Zillow price history, Realtor.com inventory, and mortgage rates. The headline result looked promising at four-to-five times better than random. Every honest check dissolved it. The apparent signal was mostly a single rural Mississippi town and a handful of other declining small markets -- and the model was strictly worse than just looking at last year's price change."
weight: 22
tags: ["real-estate", "housing", "crash-prediction", "null-result", "early-warning", "econometrics"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/housing_crashes/paper.md).*

## The Question

When the US housing market wobbles, certain metros crash harder and earlier than others. In 2022-2023 the Federal Reserve raised rates at the fastest pace in four decades, and popular commentary flagged Austin, Phoenix, and Boise as likely casualties. Can a model trained on ordinary public data — home price history, listing inventory, mortgage rates — tell you *in advance* which markets are about to fall?

This question matters for first-time buyers trying to time a purchase, for homeowners deciding whether to relocate, for local banks sizing their loan-loss reserves, and for municipal budgets that depend on property-tax revenue. If crash prediction works, it should work on public data — not only on expensive private datasets.

## What We Found

**The short answer is no — at least not at the metro level, over a 12-month horizon, with data that is free to download.**

- The headline model looked encouraging: it identified crash-prone metros at roughly 4.7× the base rate out-of-sample, which would be a useful result if it were real.
- Every honest check on that number dissolved it.
- When we properly accounted for the fact that the same crashing metro contributes up to 16 consecutive rows to the test set, the confidence interval on the lift included "barely above random."
- When we compared the model to the simplest possible baseline — just using last year's price change as the risk score — the baseline **beat** the model.
- When we permuted the crash labels at the metro level (preserving autocorrelation structure), the observed result was indistinguishable from noise: the permutation p-value was 0.49.
- Removing a single market (Clarksdale, Mississippi) dropped the model's performance by 39 percent.

**Who actually crashed.** The metros that crossed the 10-percent-decline threshold in 2022-2023 are not the Austin-Phoenix-Boise headline story. They are mostly small rural micropolitans — Clarksdale MS, Johnstown PA, Beeville TX, Kennett MO, Natchez MS-LA, McComb MS, Zapata TX — markets experiencing decades-long secular decline rather than a cyclical housing correction. Boise, Idaho is the one widely-cited Sun Belt market in the group. Austin and Phoenix did not cross the 10 percent threshold on the data source we used.

![The apparent signal dissolves under honest inference](plots/headline_dissolution.png)

## Why That's Surprising

Housing-crash prediction tools are routinely sold as commercial products. Real-estate data firms publish rankings of "most overvalued" markets. News outlets run stories titled "the 10 metros most likely to crash in 2025". If any of this worked as advertised on public data, our model should have produced a clear signal — and it didn't. The diagnostic checks that dissolved the signal are not exotic: a block bootstrap that respects metro clustering, a permutation test that preserves autocorrelation, a comparison to a single-feature baseline. Applying all three should be standard practice, and rarely is.

The other surprise is the population of actual crashers. Popular commentary focuses on post-pandemic Sun Belt boomtowns with visible inventory build-up, but the metros that actually hit a 10-percent-in-12-months decline in our data are mostly shrinking rural areas that were in chronic decline long before 2022. They don't "crash" — they keep bleeding. A cyclical-crash model trained on them won't generalise to the next actual cyclical crash.

![Where the signal actually comes from](plots/crashing_metros.png)

## What It Means

**For buyers and homeowners.** A published "metro crash probability" derived from public data is probably worth less than you think. Specifically, any such score that doesn't cite a metro-clustered confidence interval and a block-permutation p-value should be treated as informed opinion, not analysis.

**For researchers and data vendors.** Publishing a list of "the most vulnerable metros" without three specific diagnostics — metro-cluster bootstrap, block permutation, and a single-feature dominance check — is insufficient. If the paper has only a single-number out-of-sample PR-AUC or ROC, the result is probably driven by a handful of markets whose removal would change the headline.

**For the broader literature.** The null result aligns with the sceptical side of the early-warning research tradition (Schularick & Taylor on bank crises, Gourinchas & Obstfeld on currency crises, Beutel & colleagues on machine-learning crisis prediction). These authors repeatedly find that early-warning models that look good in-sample rarely generalise. Our finding extends that tradition to US metro-level housing using the specific 2022-2023 rate-shock episode.

## How We Did It

We pulled Zillow's monthly [Home Value Index](https://www.zillow.com/research/data/) for approximately 900 US metros back to 2000, joined it to [Realtor.com's monthly inventory metrics](https://www.realtor.com/research/data/) (active listings, days on market, price reductions) from 2016 onward, and added the [FRED 30-year mortgage rate](https://fred.stlouisfed.org/series/MORTGAGE30US) as a national macro series. We defined a "crash" as a 12-month forward decline of 10 percent or more, trained a standard regularised logistic model through mid-2022, and evaluated on the 18 months that followed.

All source data is publicly downloadable. All code and results are in the repository linked at the top.

## Further Reading

- Schularick, M. & Taylor, A. M. (2012). [Credit Booms Gone Bust: Monetary Policy, Leverage Cycles, and Financial Crises, 1870–2008.](https://www.aeaweb.org/articles?id=10.1257/aer.102.2.1029) *American Economic Review* 102(2).
- Gourinchas, P.-O. & Obstfeld, M. (2012). [Stories of the Twentieth Century for the Twenty-First.](https://www.aeaweb.org/articles?id=10.1257/mac.4.1.226) *American Economic Journal: Macroeconomics* 4(1).
- Beutel, J., List, S. & von Schweinitz, G. (2019). [Does machine learning help us predict banking crises?](https://doi.org/10.1016/j.jfs.2019.100693) *Journal of Financial Stability*.
- Himmelberg, C., Mayer, C. & Sinai, T. (2005). [Assessing High House Prices: Bubbles, Fundamentals, and Misperceptions.](https://www.aeaweb.org/articles?id=10.1257/089533005775196769) *Journal of Economic Perspectives* 19(4).
- [The full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/housing_crashes/paper.md).

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
