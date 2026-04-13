---
title: "Who Gets Abandoned? 23 Experiments on Predicting OSS Project Death from GitHub Events"
date: 2026-04-14
domain: "Software Engineering / Open-Source Sustainability"
blurb: "We ran 23 machine-learning experiments predicting which active GitHub projects would go silent one year later. Feature engineering barely moved the needle (≤0.2 percentage points per try). The one lever that worked was tightening who counts as 'active' in the first place -- +7.6 percentage points of signal from the cohort filter alone."
weight: 4
tags: ["open-source", "software-engineering", "github-archive", "negative-result", "hdr", "xgboost"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/oss_abandonment/paper.md).*

## The Question

The xz-utils backdoor (CVE-2024-3094), Log4Shell, left-pad, event-stream — every recent open-source supply-chain crisis has the same shape: a critical piece of software maintained by one or two unpaid volunteers, who either burn out, hand the project to a stranger, or simply stop responding. The Harvard/Linux Foundation Census III found 10 of the most widely deployed libraries in enterprise software are each maintained by one developer. If your server runs Linux, if your browser loads a webpage, if your phone runs an app — you almost certainly depend, somewhere in the transitive closure, on an open-source project with a sustainability problem.

So a natural question: can we see abandonment coming? Given a year of GitHub event history for an active project, can a model predict whether that project will still have a pulse one year later?

## What We Did

We pulled 36 hourly snapshots from [GH Archive](https://data.gharchive.org) — the public timeline of every event on GitHub — spanning two 3-day windows one year apart (April 2024 for prior activity; April 2025 for the label). That gave us a 2.6-million-row panel across 662,593 repos that were active in the prior window.

We defined abandonment strictly: a repo is abandoned if it had zero human-authored commits across all three sampled forward days. Bot commits (dependabot, renovate, github-actions, and similar) don't count as human activity — a core methodological point that kept getting lost in early modelling literature.

Then we ran the full Hypothesis-Driven Research loop: 230-citation literature review, a 120-hypothesis pre-registered research queue, an 88-variable design catalogue, a 4-model tournament (XGBoost won), and 22 single-change experiments exploring cohort definitions, feature additions, relabelling schemes, model regularisation, and hyperparameter tuning.

## What We Found

**Cohort definition dominates feature engineering. By a lot.**

Our baseline XGBoost classifier on 17 activity/engagement/popularity features achieved a ROC-AUC of **0.8116**. The best single-change experiment lifted that to **0.8879** — a 7.6-percentage-point gain. That single biggest win came not from a clever new feature but from raising the prior-activity threshold: instead of including any repo with at least one commit in the 3-day prior window (a messy cohort of 662k repos with 94.6% eventual-abandonment base rate), we required at least ten human-authored commits in the same window (14,415 repos, 82% base rate).

Every feature-engineering variant — log-transformed star counts, commits-per-author ratios, engagement sub-ratios, deeper trees — changed ROC-AUC by at most 0.002 points. Feature ablation to a minimal 6-feature subset cost only 0.01 ROC-AUC. The 17-feature set is modestly additive; no single family is the lever.

As you tighten the cohort, the base rate falls toward the 5-15% abandonment rate the literature reports at 12-month horizons — which is the regime where a classifier has something to learn. The loose cohort was 95% "abandoned" by our strict definition, meaning the problem was closer to finding the 5% of obviously-real projects in a sea of one-off scripts and tutorials.

## Why It Matters

This is a negative result about feature engineering and a positive one about problem framing. Most of the OSS health-prediction literature proliferates features — truck factor, elephant factor, contributor entropy, issue response time, sentiment — without interrogating who the features are being computed *for*. If your training set is dominated by ephemeral learning exercises, no amount of clever feature engineering will find the signal you want.

For the practical question — which critical open-source projects should funders, downstream corporate users, or security foundations watch closely — the useful output is not our classifier; it's the **sub-cohort** of ~14k repos that meet a stringent real-project activity bar and whose 1-year-forward commits dropped by 10× or more. That's the signal. The ranking within it is almost a formality.

## Limitations

We worked from a thin temporal sample (3 prior days, 3 forward days), used only GH Archive event data (no GitHub API enrichment for contributor stats, issue-response times, or `archived` flag), and did not evaluate on the Census III critical-package subset. Each of those is a clear next step that the literature predicts would add 0.02-0.05 ROC-AUC of signal.

We also did not test the causal question that motivated the project: does a first toxic issue comment, or a maintainer's first public sign of burnout, predict exit? That requires NLP on issue-comment bodies and is the natural Phase II follow-up.

## Code & Data

All code, raw data manifests, and a reproducible pipeline at [`applications/oss_abandonment/`](https://github.com/colinjoc/hdr_autoresearch/tree/main/applications/oss_abandonment). 36 hourly GH Archive files (~4.5 GB gzipped) can be re-downloaded from public URLs via `pull_data.py`. Baseline plus 22 experiments re-runnable from `hdr_loop.py`. 13 unit tests on the event-stream loader and bot filter.
