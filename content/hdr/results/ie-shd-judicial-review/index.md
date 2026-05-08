---
title: "Ireland's housing fast track met the High Court — and lost"
date: 2026-05-08
domain: "Planning policy / Public administration"
blurb: "A planning fast track designed to deliver Ireland's housing crisis solution lost in the High Court roughly nine times out of ten — and was scrapped four years in."
weight: 35
tags: ["housing", "ireland", "planning-policy", "judicial-review", "shd", "abp"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_shd_judicial_review/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Between 2018 and 2021, fourteen of the sixteen Strategic Housing Development (SHD) decisions that reached a High Court ruling went against An Bord Pleanála (ABP) — twelve permissions quashed by judges, two conceded by the planning board before judgment. The fast track was scrapped at the end of 2021, four years after it began.

## The question

In July 2017 the Oireachtas — Ireland's parliament — passed a law creating the Strategic Housing Development regime. The pitch was simple. Large housing schemes — originally one hundred or more units, plus large student-accommodation projects — could skip the local council stage entirely and apply straight to An Bord Pleanála, the national planning board. Through the mid-2010s, a big housing site in Ireland could expect roughly eighteen to thirty months for a council decision and another eighteen-plus months on appeal. SHD promised a twenty-four-week turnaround. It was the late-2010s government's headline answer to a deepening housing shortage.

Did it work? The board approved roughly four out of every five applications it received, and at the promised pace. By that yardstick the regime did exactly what its drafters wanted. But almost as soon as the first permissions issued, residents' associations, environmental groups and competing developers began bringing those decisions to the High Court — and winning. We pulled the Office of the Planning Regulator's published register of decided judicial reviews involving An Bord Pleanála, isolated the SHD-specific cases for the active-regime years, and asked what the courts had actually done with them.

## What we found

Sixteen SHD judicial reviews were decided in the High Court between 2018 and 2021. Twelve ended with the permission quashed outright. Two more were conceded by the board before a hearing — meaning ABP withdrew its own decision rather than defend it. Two were refused or dismissed. That is fourteen state losses out of sixteen contested cases — roughly eighty-eight percent.

![Strategic Housing Development judicial reviews decided per year, 2018 to 2022, with state losses highlighted. The 2020 spike — eight quashings and one concession in a single year — is the year the regime's legal position became unsustainable. The 2022 column is hatched because the underlying register was published in October of that year and the row is partial-year only.](plots/shd_jr_by_year.png)

The losses were not evenly spread across the four years. Nine of them landed in 2020 alone — eight quashings and one concession in twelve months. That single year's tally is roughly when the regime's legal exposure became unsustainable rather than uncomfortable.

Press coverage at the time put the loss rate higher still — closer to ninety-one percent across roughly thirty-five SHD challenges. The two figures reconcile cleanly. The press totals counted every SHD judicial review *lodged* in the High Court, including those later settled, withdrawn or still pending. The Planning Regulator's register counts *decided* cases only. Both views agree: the state was losing in the high-eighties to low-nineties. The denominators differ; the direction does not.

The pattern in the rulings is striking. The single most common reason the courts gave for quashing an SHD permission was that ABP had granted permission for a development which materially contravened the local development plan — typically on building height — without recording adequate reasons for doing so. The legislation allowed the board to override the local plan, but required it to justify the override in specific written terms. In case after case, the courts found the board had not. Secondary themes included inadequate environmental screening under the European Habitats Directive — a Meath case turned on Lapwing habitat at the Boyne Estuary — and procedural failures such as not posting application documents on a dedicated public website.

The financial trail was equally clear. An Bord Pleanála's published legal costs for defending judicial reviews ran at three-and-a-half million euro in 2019. The following year they reached eight-point-two million — more than double in twelve months. The jump tracks the rise in decided SHD challenges from two in 2019 to ten in 2020. We did not independently audit the board's statutory accounts; the figures here come from press reporting of the board's annual disclosures.

The regime was abolished at the end of 2021 and replaced from mid-2022 by a new framework called Large-scale Residential Development, which routes large housing applications back to local councils with a tighter pre-application stage, time limits, and — pointedly — explicit documentation requirements designed to address the reasoning failures that had been the pattern in the SHD quashings.

## Why that matters

The headline rate is striking on its own — most regulatory regimes survive the High Court most of the time. SHD did not. But the more useful finding is *why* it lost. The policy error was not the fast track itself. The error was running a fast track without an internal documentation process robust enough to survive judicial review on the most predictable line of attack — material contravention of local development plans on height. The courts repeatedly found the board's reasoning either absent or inadequate on a class of question the legislation specifically required reasoning on. Once a few early cases established the pattern, well-prepared challenges had a near-mechanical route to victory.

There is a wider lesson there for any planning reform that proposes to bypass an existing tier of decision-making. Bypassing the council was not what failed in court. Failing to document why the bypass was justified — in legally-survivable form, case by case — was. The successor regime appears to have been designed with exactly that lesson in mind.

## What it means in practice

**For applicants.** Speed at the application stage was real — the board did issue permissions quickly — but the speed bought a fragile permission. A challenged SHD permission was, by the late stages of the regime, more likely to fall in the High Court than not. Lenders and contractors learned to price that risk in.

**For objectors.** Well-prepared challenges targeting documented material contraventions of development plans, especially on height, succeeded at very high rates. This was not loose obstruction; it was a specific legal strategy exploiting a real procedural gap in how decisions were being recorded.

**For policymakers.** Fast tracks need not be slower than slow tracks if they fail in court at this rate. The replacement regime's emphasis on documentation, pre-application engagement and time limits reads as a direct response to the SHD failure mode.

## How we did it

We downloaded the Office of the Planning Regulator's published register of decided judicial reviews involving An Bord Pleanála — covering 2012 through October 2022 — extracted the text from the source PDF, and parsed each case record using a regex-based extractor. The extractor splits records on numbered row boundaries rather than on raw date literals (so that PDF rows wrapping across two text lines are not mis-assigned), takes the decision year from the neutral citation rather than the date column, and classifies each outcome as quashed, conceded, refused, dismissed, or upheld-on-appeal.

We then isolated the SHD-specific cases — n equals sixteen for the active-regime window 2018 to 2021, plus six more in the partial-2022 register — by manually labelling each entry against case names, addresses and the underlying development descriptions. A regression suite pins the ground-truth decision year and outcome for every SHD case in scope. The legal-cost figures come from press reporting of the board's annual disclosures and were not independently audited; we flag this as a known limitation. There is no model and no forecast — this is a structured extraction against a hand-verified ground truth.

What this work does *not* do: it does not capture the full universe of SHD challenges (settled and withdrawn cases sit outside the register), it does not break challengers down by identity, and it does not estimate the counterfactual — what Irish housing delivery would have looked like had SHD never existed. The companion paper on Ireland's wider housing pipeline addresses the downstream commencement-and-completion question.

## Further reading

- [Why Irish planning appeals slowed to a crawl, then started moving again](/hdr/results/ie-abp-decision-times/) — the broader An Bord Pleanála throughput record across the same window.
- [Ireland's housing bottleneck](/hdr/results/ie-housing-bottleneck/) — companion analysis of the wider permission-to-completion pipeline.
- [Office of the Planning Regulator](https://www.opr.ie/) — publisher of the source register of decided judicial reviews.
