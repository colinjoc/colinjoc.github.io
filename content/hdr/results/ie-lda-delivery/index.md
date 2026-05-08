---
title: "Ireland's state housing agency delivers about three percent of the target"
date: 2026-05-08
domain: "Irish Housing Policy"
blurb: "The Land Development Agency was meant to help fix the housing crisis. In its first audited year it built about 850 homes — none directly."
weight: 25
tags: ["housing", "ireland", "policy-evaluation", "LDA", "open-data"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lda_delivery/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Ireland's state housing-delivery body, the Land Development Agency (LDA), delivered about 850 homes in its first audited year — roughly three percent of national completions — and every one of those homes was bought from a private developer rather than built directly. Even at its own 2028 cumulative target of 8,000 homes, the LDA would account for about three percent of the country's 50,500-per-year Housing for All goal. The agency is doing what it was set up to do; it is not, and was never, the lead vehicle for solving the crisis.

## The Question

The Land Development Agency was created by statute in September 2018 with a brief to assemble state land and deliver affordable and cost-rental housing. It became operationally active as a delivery body only in 2023, once Project Tosaigh — its programme to forward-purchase near-complete homes from private developers — came on stream. Since then it has been treated, in political rhetoric, as a major lever against an acute housing shortage.

The natural questions: how many homes has the LDA actually delivered against verifiable, audited sources, and what share of the 50,500-homes-per-year Housing for All target does that represent?

## What we found

![LDA delivery against two national-completions denominators, with the agency's own 2028 target overlaid.](plots/lda_delivery.png)

**Only one year has an audited delivery total, and it is about 850 homes.** The LDA's 2023 Annual Report — the only published audited account — uses the verbatim figure "ca. 850 homes": about 650 cost-rental and about 200 affordable-for-sale. Earlier circulating numbers giving false precision (a specific "854") are not what the agency itself reports.

**Every one of those 2023 homes was bought, not built.** One hundred percent of 2023 LDA delivery came through Project Tosaigh acquisitions of homes built by private developers under the standard planning regime. The agency's first direct-build project, at Shanganagh in County Dublin, was not expected to deliver its first units until 2025.

**That detail matters for how the headline share is read.** Project Tosaigh homes are already counted in the national completions total — they were built by private developers and would have been built anyway. Reporting the LDA's three percent share of national completions therefore measures attribution (how many national completions the LDA acquired) rather than additionality (how many extra homes the LDA caused to be built). The additionality figure for 2023 is, on the available evidence, close to zero.

**Cumulative delivery through end-2025 is roughly 3,500 homes, not the 4,500 sometimes cited.** The Irish Times reported cumulative LDA delivery through end-2024 at about 2,054 homes, implying about 1,200 in 2024. Press estimates put 2025 in the range of 1,200 to 1,800. Cumulative end-2025 is therefore about 3,200 to 3,900.

**The forward target is 8,000 by 2028, not 14,000.** The "14,000 by 2028" number that has circulated in commentary does not appear in the LDA's 2023 annual report. The report's own forward language is 8,000 homes by 2028 through Project Tosaigh, with a combined Tosaigh-plus-direct-delivery pipeline of over 10,000. Hitting 8,000 cumulative by 2028 from a 2024 base of about 2,054 requires roughly 1,500 deliveries per year for four years — consistent with the current trajectory if the direct-build pipeline converts on schedule.

**Even at target, the agency is a structurally minor share of the national plan.** Eight thousand homes cumulative by 2028 averages about 1,600 per year. Against the 50,500-homes-per-year Housing for All target, that is roughly three percent.

## Why that matters

Irish housing politics has, at times, treated the LDA as a lead instrument for solving an acute supply crisis. The agency's own targets do not support that framing. A body delivering at three percent of the national requirement is not designed to close the gap on its own, and pretending otherwise displaces attention from the larger levers — local-authority direct construction, Approved Housing Bodies (AHBs, the not-for-profit housing providers), and overall private-sector throughput — that together must deliver the remaining 97 percent.

There is also a quieter point about tenure. The LDA's output is concentrated in cost-rental and affordable-for-sale categories that the market does not otherwise supply at scale. A three percent arithmetic share in a tenure band where the alternative is zero supply may matter more than the headline number suggests. That is a different argument from "the LDA will solve the crisis," and it is the argument that fits the evidence.

## What it means in practice

**For renters and homebuyers.** The LDA is a real source of cost-rental and affordable-for-sale supply, but at current pace it will deliver in the low thousands cumulatively by 2028. If your housing strategy depends on an LDA tenancy materialising, the queue is and will remain long.

**For LDA management.** The 2028 target of 8,000 cumulative homes is internally consistent with the current trajectory, but only if direct-build projects come online on schedule. The agency's first direct-build completion is the leading indicator to watch; without it the run-rate stays at the Project Tosaigh ceiling.

**For policymakers and commentators.** The defensible numbers to cite are about 850 (2023, audited), about 2,054 cumulative through end-2024 (Irish Times), and 8,000 cumulative by 2028 (LDA's own target). The 14,000-by-2028 figure in circulation is not in the agency's annual report. Conflating attribution share with additionality share inflates the LDA's measured contribution; the cleaner framing is that the agency's additionality in 2023 was close to zero because every delivered home was a privately-built unit forward-purchased after construction.

## How we did it

This is a descriptive comparison, not a model. The numerator — homes delivered — was taken from the LDA's audited 2023 Annual Report, the Irish Times September 2025 cumulative figure for end-2024, and press reporting for the 2025 range. The denominator — national completions — was taken from the Central Statistics Office, in two forms: the towns-only NDA12 series and the all-Ireland aggregate. Both denominators are presented explicitly because they give materially different share calculations, and only the 2023 row uses an audited numerator paired with an audited denominator. Unaudited rows are flagged as approximate and treated as ranges rather than point estimates throughout.

## Further reading

- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lda_delivery/paper.md) — sources, audited-versus-unaudited row markers, and the additionality-versus-attribution discussion.
- Land Development Agency 2023 Annual Report — the audited source for the "ca. 850" headline and the 8,000-by-2028 forward target.
- Central Statistics Office, New Dwelling Completions (NDA12 and all-Ireland series) — the national denominator.
- Companion analysis on the Strategic Housing Development judicial-review backlog at `ie_shd_judicial_review`, which addresses the supply-side disruption the LDA was, in part, designed to offset.
