---
title: "Does Evolution Obey a Law of Increasing Functional Information?"
date: 2026-04-19
domain: "Evolutionary Biology / Information Theory"
blurb: "Wong et al. proposed that functional information always increases in evolving systems. We measured it across 12 protein landscapes, the Lenski LTEE, and 4.56 billion years of mineral diversity. The trend holds -- but the rate spans 40 orders of magnitude and the denominator dominates everything."
weight: 24
tags: ["functional-information", "evolution", "deep-mutational-scanning", "Wong-law", "DFE", "epistasis", "LTEE", "mineral-evolution", "information-theory", "fitness-landscapes"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/functional_info_evolution/paper.md) has the methods, tables, and hypothesis tests. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** In 2023 Wong, Cleland, Hazen and colleagues proposed a new law of nature: functional information -- how rare a working configuration is among all possible configurations -- tends to increase over time in any system under selection. We tested this across proteins, bacteria, minerals, and digital organisms. All five system types showed the predicted increase. But the rate varies by a factor of 10<sup>40</sup>, the measured value depends overwhelmingly on how you count the denominator, and deep mutational scanning data -- the richest source of protein fitness information -- captures a static snapshot, not a time series. The law is consistent with the data. It is not confirmed by it.

## What is functional information, and why measure it?

Szostak (2003) defined functional information as I<sub>func</sub> = -log<sub>2</sub>(F(f)/N), where F(f) is the number of configurations that achieve function at or above threshold f, and N is the total number of possible configurations. In plain terms: if only one in a million random protein sequences binds a target, the binding function carries about 20 bits of functional information. The rarer the function, the higher the information content.

Wong et al. (2023) proposed that this quantity always increases over time in systems under functional selection -- not just in biology, but in mineral assemblages, stellar nucleosynthesis, and anywhere combinatorial diversity meets selection. If true, it would be a genuinely new candidate law of nature.

The claim is testable. Deep mutational scanning (DMS) now provides comprehensive maps of how protein sequence relates to function, covering hundreds of thousands of variants per protein. The Lenski Long-Term Evolution Experiment (LTEE) provides 75,000+ generations of continuous fitness data. Mineral diversity records span 4.56 billion years.

## The denominator dominates everything

Our most striking finding is that functional information depends critically on what you count as the total configuration space. For the GB1 protein domain (55 residues, IgG-Fc binding), I<sub>func</sub> at the 75th percentile threshold is about 2 bits when computed against the roughly 537,000 variants actually tested by DMS. But against the full theoretical sequence space (20<sup>55</sup>, roughly 10<sup>71</sup> possible sequences), I<sub>func</sub> is 221 bits.

For TEM-1 beta-lactamase (263 residues), the theoretical I<sub>func</sub> exceeds 1,100 bits.

| Protein | Residues | I<sub>func</sub> (empirical) | I<sub>func</sub> (theoretical) | Difference |
|---------|----------|------------------------------|-------------------------------|------------|
| GB1 | 55 | 2.0 bits | 221 bits | +219 bits |
| TEM-1 | 263 | 2.0 bits | 1,126 bits | +1,124 bits |
| GFP | 238 | 2.0 bits | 1,015 bits | +1,013 bits |

The 2-bit empirical value is essentially a mathematical artifact: at the 75th percentile threshold, 25% of tested variants pass by definition, giving -log<sub>2</sub>(0.25) = 2 bits regardless of the protein. The real information content -- how special a functional protein is in the full space of random amino acid sequences -- is hundreds to thousands of bits. DMS experiments, which test thousands to hundreds of thousands of variants, are sampling a vanishingly small fraction of sequence spaces that range from 10<sup>71</sup> to 10<sup>342</sup>.

## What predicts functional information? The shape of the fitness distribution

Across the eight protein systems we analysed (GB1, TEM-1, GFP, HSP82, BRCA1, PTEN, and SARS-CoV-2 RBD measured for both binding and expression), the strongest predictor of functional information at absolute thresholds is the skewness of the distribution of fitness effects (DFE). The correlation is r = -0.93, p = 0.003, surviving Bonferroni correction across 63 tests.

The interpretation is natural. Proteins under strong purifying selection have negatively skewed fitness distributions: most mutations are harmful, few are neutral or beneficial. A smaller fraction of sequence space is functional at any given threshold, so I<sub>func</sub> is higher. Conversely, proteins with more symmetric fitness distributions (like TEM-1, with positive skew of 0.36) have more sequences near wild-type fitness, producing lower I<sub>func</sub> at the same absolute threshold.

## Same protein, different functions, different information

For SARS-CoV-2 RBD, the binding assay and expression assay produce markedly different results: threshold-sweep area under the curve of 4.38 for ACE2 binding versus 10.01 for surface expression, a 2.3-fold difference. Binding requires precise molecular complementarity; surface expression is more permissive.

This underscores that functional information is not a property of the protein. It is a property of the protein-function pair. Different functions for the same molecule can have different information content and, presumably, different temporal trajectories.

## Epistasis constrains how information accumulates

The GB1 dataset includes 536,000 double-mutant measurements. Of the 536,000 testable pairs, 88.8% show epistasis -- the combined effect of two mutations deviates from the sum of their individual effects. The epistasis is overwhelmingly antagonistic: 81.9% of epistatic pairs show negative epistasis, where the double mutant is less fit than the additive expectation predicts.

This matters for Wong's law because it means each additional beneficial mutation contributes less to fitness improvement than the last. Functional information accumulation decelerates. Adaptive walks on the TEM-1 landscape confirmed this: the rate of fitness gain in the first half of the walk was three times the rate in the second half.

## All five systems show increasing functional information

Despite the caveats, all measured systems show functional information proxies that increase over time:

- **Minerals:** Diversity grew from about 12 species at 4.56 billion years ago to over 5,800 species today, corresponding to an increase from 3.6 to 12.5 bits of diversity information -- roughly 2 bits per billion years.
- **Bacteria (LTEE):** Fitness increases as a power law over 50,000+ generations with no sign of saturation, at a rate of roughly 0.01 bits per generation.
- **Proteins:** Simulated adaptive walks on DMS landscapes accumulate functional information, though these are walks on static landscapes, not observations of real evolutionary change.
- **Digital organisms (Avida):** Published results show genomic complexity increasing under selection, consistent with the prediction.
- **RNA aptamers:** Published data shows each 10-fold improvement in binding affinity requires about 10 additional bits of functional information (Carothers et al. 2004).

The trend is consistent with Wong's law. But the rate varies by roughly 40 orders of magnitude across these systems -- from minerals at about 2 bits per billion years to bacterial adaptation at about 0.01 bits per 20-minute generation.

## The gap to physical speed limits

The companion project, [How Fast Can Evolution Actually Go?](/hdr/results/thermodynamic-info-limits/), derived thermodynamic ceilings on functional information gain. Those ceilings matter here. For an *E. coli* cell, the Landauer limit permits roughly 4 x 10<sup>11</sup> bits per generation; the Bremermann limit allows 1.6 x 10<sup>38</sup>. The observed LTEE rate is about 0.01 bits per generation. The gap is 10<sup>13</sup> to 10<sup>40</sup>.

Evolution is not running up against any physical barrier. It is operating in a regime where the constraint is search efficiency -- how many sequence space configurations can be explored per generation -- not energy or information bandwidth.

The second companion project, [How Far Is AI Training from the Laws of Physics?](/hdr/results/thermodynamic-ml-limits/), extends this comparison to machine learning. GPU-based training also operates vastly below thermodynamic ceilings, but the gap is only about 10<sup>20</sup> -- narrower than evolution's gap, reflecting the engineered efficiency of gradient-based search versus mutation-and-selection.

## The honest conclusion

We tested 20 specific hypotheses. Fifteen were supported, five were rejected. The rejected hypotheses are instructive: F(f) does not always follow exponential decay; single-mutant DMS data does not always underestimate full-landscape I<sub>func</sub>; and the per-substitution information gain is not consistently in the 0.01--1 bit range that simple models predict.

Wong's law holds in a weak sense: functional information tends to increase in systems under selection. But it does not hold in a strong sense of a universal rate law. The rate depends on mutation rate, population size, fitness landscape topology, generation time, and the nature of the selection mechanism. These parameters span enormous ranges across mineral, bacterial, protein, and digital systems.

Most importantly, DMS data -- the richest experimental source -- provides static landscape snapshots, not evolutionary time series. Observing that a static landscape has high functional information is not the same as observing that functional information increased over time. The definitive test would require DMS measurements of ancestral and derived versions of the same protein under the same conditions, using ancestral protein reconstruction.

## What generalises beyond this project

The denominator problem is not unique to functional information. Any information-theoretic measure that divides by a configuration space will be dominated by how that space is defined. Researchers reporting functional information should always state both the empirical value (relative to tested variants) and the theoretical value (relative to full sequence space), and be explicit about which they mean. The two can differ by a thousand bits.
