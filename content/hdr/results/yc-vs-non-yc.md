---
title: "Do Y Combinator startups really outperform? The data says: we can't tell"
date: 2026-04-17
domain: "Entrepreneurial Finance"
blurb: "Y Combinator is the most famous startup accelerator in the world, and the belief that its graduates beat comparable non-YC startups is treated as common sense. We re-ran the test with public filings data and found the honest answer is neither a clean yes nor a clean no — and the reason is itself revealing about how modern startups raise money."
weight: 25
tags: ["startups", "venture-capital", "y-combinator", "causal-inference", "sec-filings"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/yc_vs_non_yc/paper.md).*

## The Question

Y Combinator has graduated thousands of companies since 2005, and an entire genre of industry commentary takes for granted that being a "YC company" is itself a meaningful advantage. The academic record is more mixed: some studies find a five-to-fifteen-percentage-point boost on follow-on funding and survival, others find essentially nothing once you control for which ecosystems YC founders come out of.

We wanted to rerun this comparison using only fully public data — the Y Combinator portfolio list and the United States Securities and Exchange Commission's structured record of private fundraising filings — and a matched-pair design that tries to compare YC companies with non-YC companies that look otherwise identical.

## What We Found

Three things, in tension with each other.

- The raw comparison — YC companies versus the entire non-YC pool of seed-stage Regulation D filers — shows exactly zero advantage. Both groups raise a follow-on round at a 29.1% rate over five years.
- Once the comparison is done properly, matching each YC company to otherwise-similar non-YC filings on industry, geography, timing, round size, and local investor density, YC pulls ahead by about six percentage points. But the confidence interval on that estimate crosses zero. We cannot rule out that the true effect is nothing.
- There is a hidden data problem that biases the answer downward. The non-YC companies that most look like YC companies are precisely the ones that raise money through modern instruments that never trigger a public filing. Their true raise rate is invisible to us. Correcting for this channel bias means the real YC effect is plausibly larger than our six-point estimate, not smaller.
- Only one in thirteen YC companies files a Regulation D offering in their own name within five years of graduating. The rest raise through instruments that leave no public paper trail.

## Why That's Surprising

The dominant narrative is that this question is already settled — that of course YC companies do better, and anyone who doubts it has not looked at the numbers. Our result is that the numbers, done honestly, cannot settle it.

The surprise is not really about Y Combinator. It is about what modern fundraising looks like. A decade of the "SAFE" contract and direct private placements means that the public record of early-stage startup finance has quietly become full of holes — and the holes are not random. They are concentrated precisely in the high-quality, well-networked companies that researchers most want to study. Any paper that uses public filings as its outcome and forgets this is in effect measuring who is old-fashioned about paperwork, not who is doing well.

## What It Means

For founders deciding whether to apply to YC, our result is not evidence against applying — if anything it is evidence the true effect is obscured by a measurement problem. The advantage is probably real; our data just cannot pin down its size.

For journalists and investors citing "the YC outperformance" as a settled fact, it is a caution. The cleanest public test of the claim does not confidently support it, and the gap between narrative and evidence is wider than commonly assumed.

For policymakers and regulators thinking about transparency in private markets, it is a concrete example of what private-funding opacity costs: even a basic question about accelerator effectiveness cannot be answered from the public record.

## How We Did It

We joined the open [Y Combinator portfolio list](https://github.com/yc-oss/api) with the [SEC's public Form D quarterly archive](https://www.sec.gov/dera/data/form-d) to assemble a panel of seed-stage raises from 2014 through 2019, matched Y Combinator companies to otherwise-similar non-YC filings by name, and compared five-year follow-on raise rates using propensity-score matching with a ladder of progressively richer ecosystem controls. A lookalike-placebo design then checked whether our matched control group was behaviourally comparable to the treated group on the outcome — and revealed the filing-channel bias described above.

## Further Reading

- Hallen, Cohen, and Bingham (2020), "Do Accelerators Work?" — *Strategic Management Journal*
- Cohen, Fehder, Hochberg, and Murray (2019), "The Design of Startup Accelerators" — *Research Policy*
- Kerr, Lerner, and Schoar (2014), "The Consequences of Entrepreneurial Finance" — *Review of Financial Studies*
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/yc_vs_non_yc/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
