---
title: "Do Y Combinator startups really outperform? We can't tell"
date: 2026-04-19
domain: "Entrepreneurial Finance"
blurb: "The belief that Y Combinator graduates beat everyone else is treated as common sense. The cleanest public test cannot confirm it — and why it can't is the real story."
weight: 25
tags: ["startups", "venture-capital", "y-combinator", "causal-inference", "sec-filings", "null-result"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/yc_vs_non_yc/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Using only fully public data, we cannot confirm that Y Combinator graduates outperform comparable non-YC seed-stage companies on follow-on fundraising. The raw five-year follow-on rate is identical, 29.1 percent for both. A properly matched comparison nudges YC ahead by about 6 percentage points, but the confidence interval still crosses zero. More importantly, the public record has a systematic hole exactly where researchers need to look, and the hole biases any such test downward.

## The question

Y Combinator has graduated thousands of companies since 2005. An entire genre of industry commentary takes for granted that being "a YC company" is itself a meaningful advantage. The academic record is more mixed — some studies find a 5 to 15 percentage-point boost on follow-on funding and survival, others find essentially nothing once you control for the ecosystems YC founders come from.

We wanted to rerun this comparison using only fully public data — the Y Combinator portfolio list and the United States Securities and Exchange Commission's structured record of private fundraising filings — and a matched-pair design that compares YC companies to non-YC companies that look otherwise identical on industry, geography, timing, round size, and local investor density.

## What we found

Three things, in tension with each other.

- The raw comparison — 117 YC companies from the 2014 to 2019 batches versus the entire non-YC pool of about 31,700 comparable seed-stage filers — shows exactly zero advantage. Both groups raise a follow-on round at a five-year rate of 29.1 percent.
- The properly matched comparison, done right, moves YC ahead by about 6 percentage points. But the confidence interval on that estimate crosses zero. We cannot rule out that the true effect is nothing, and we cannot rule out that it is in the range the existing literature reports.
- There is a hidden data problem that biases the answer downward. When we pick the 117 non-YC companies that most resemble YC companies on everything we can observe, their filing rate is not 29 percent. It is 8 percent. Their "disappearance" is not failure. They are raising through modern instruments — uncapped SAFEs, direct private placements — that do not trigger the public filing we are using as the outcome measure.
- Only one in thirteen YC companies from 2014 to 2019 filed a Regulation D offering in their own name within five years of graduating. The rest raised through instruments that left no public paper trail.

![Covariate ladder plus lookalike-placebo: the estimate moves up with ecosystem controls, and the lookalike gap exposes channel bias](plots/covariate_ladder.png)

## Why that matters

The dominant narrative is that this question is already settled — that of course YC companies do better, and anyone who doubts it has not looked at the numbers. Our result is that the numbers, done honestly, cannot settle it.

The surprise is not really about Y Combinator. It is about what modern fundraising looks like. A decade of the "SAFE" contract and direct private placements means the public record of early-stage startup finance has quietly become full of holes — and the holes are not random. They are concentrated precisely in the high-quality, well-networked companies that researchers most want to study. Any paper that uses public filings as its outcome and forgets this is effectively measuring who is old-fashioned about paperwork, not who is doing well.

A true +6 percentage-point YC effect cannot be ruled out and would be consistent with both our data and the prior literature's higher estimates. Correcting for the channel bias plausibly pushes the real effect upward, not downward. The honest claim is that the data does not allow a clean answer either way — and the project's main scientific value is diagnosing why.

## What it means in practice

**For founders deciding whether to apply to YC.** Our result is not evidence against applying. If anything it is evidence that the true effect is obscured by a measurement problem that biases estimates toward zero. The advantage is probably real; the public data cannot pin down its size.

**For journalists and investors citing "the YC outperformance" as a settled fact.** The cleanest public test of the claim does not confidently support it. The gap between narrative and evidence is wider than commonly assumed, and the confident tone of the claim does not match the quality of the public evidence.

**For policymakers and regulators thinking about transparency in private markets.** This is a concrete example of what private-funding opacity costs. Even a basic question about accelerator effectiveness — one with real policy relevance for innovation support and regional economic development — cannot be answered from the public record. A public register of SAFE and direct-placement raises would dramatically raise the ceiling on what researchers can learn about early-stage finance.

**For academic researchers using SEC Form D as an outcome measure.** The lookalike-placebo test we describe — taking the public-pool companies that most structurally resemble the treated firms and checking their outcome rate — is the diagnostic that exposes the problem. Any study using Regulation D filings as a success measure in the modern fundraising era should run it.

## How we did it

We joined the open [Y Combinator portfolio list](https://github.com/yc-oss/api) with the [SEC's public Form D quarterly archive](https://www.sec.gov/dera/data/form-d) to assemble a panel of seed-stage raises from 2014 through 2019, matched Y Combinator companies to otherwise-similar non-YC filings by name, and compared five-year follow-on raise rates using propensity-score matching with a ladder of progressively richer ecosystem controls (local venture density, metro flags, and the VIX at time of filing). A lookalike-placebo design then checked whether the matched control group was behaviourally comparable to the treated group on the outcome itself — and revealed the filing-channel bias described above.

## Further reading

- Hallen, Cohen, and Bingham (2020), "Do Accelerators Work?", *Strategic Management Journal* — one of the positive-effect studies in the literature.
- Cohen, Fehder, Hochberg, and Murray (2019), "The Design of Startup Accelerators", *Research Policy* — another positive-effect study.
- Kerr, Lerner, and Schoar (2014), "The Consequences of Entrepreneurial Finance", *Review of Financial Studies* — the admission-score natural-experiment design, and a more equivocal estimate.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/yc_vs_non_yc/paper.md) — the covariate ladder, the lookalike-placebo design, and every sensitivity check.
