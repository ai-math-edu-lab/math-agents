---
title: "Hardness Evaluation — experiment type"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: hardness-evaluation
author: asetlearning
status: validated
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/pending, experiment-type]
---

# Hardness Evaluation (B(2,5))

**Measure how hard a certified trivial word is**, with the owner's metrics from [[challenge-gen-success-metrics]]: L0 (certificate valid), Metric 1 ρ (2.5-reduction resistance), Metric 2 D (Dehn proxy on the minimised certificate F*), and the L0 to L3 level classification. This is the evaluation layer every later challenge-gen item (T-002 to T-010) is judged with. It generates nothing.

- Methodology and pre-registration: [[hardness-harness-baselines-2026-10-13]] (T-001)
- Project: [[project-challenge-gen]] · Progress: [[Challenge Generation/_progress]]
- Generator being evaluated: [[B25/PatternBoost Generation/_type|PatternBoost Generation]]

## Terms
Project terms (defined once in [[challenge-gen-glossary]], not restated): [[challenge-gen-glossary#aut8 and the 16 images|aut8 / 16 images]], [[challenge-gen-glossary#canon (canonical class)|canon]], [[challenge-gen-success-metrics#Notation|certificate, factor word, w̄, n, R₂.₅]], [[challenge-gen-glossary#screen mode and certify mode|screen / certify mode]], [[challenge-gen-glossary#rho_min16|ρ_min16]], [[challenge-gen-glossary#rho_cyc and the cyclic reduction|ρ_cyc]], [[challenge-gen-glossary#loop erasure|loop erasure / F*]], [[challenge-gen-glossary#D_raw|D_raw]], [[challenge-gen-glossary#fixed point of the reducer|fixed point]], [[challenge-gen-glossary#pre-check: no square and power-free|pre-check, power-free shortcut]], [[challenge-gen-glossary#novel L1 and the guards G1 and G2|novel L1, G1, G2]], [[challenge-gen-glossary#positive and negative control|positive / negative control]], [[challenge-gen-glossary#standard relators and dataset relators|standard and dataset relators]], [[challenge-gen-glossary#relator map, relator table and relator file|relator table]], [[challenge-gen-glossary#undecided, timeout|undecided / timeout]], [[challenge-gen-glossary#seeds and calibration seed|seeds]].

Type-local terms:
- **T-001 cells S1–S7.** Random standard-relator sampling cells of the baselines (relator length L, factor range, conjugator length); fixed table in [[challenge-gen-glossary#cell and cell names]]. Not related to the T-002 strata of the same names.
- **T-002 cell name `P<pct>-K<k>-<subset>[-L2]`.** Dataset share in percent, factor-count range, dataset subset (`short100`, or a stratum), optional suffix `-L2` for short standard relators. Example: `P100-K2-short100` = every factor from the 100 shortest dataset words, 2 factors. Full rules in the glossary entry above.
- **S1–S4 strata (T-002).** Dataset words by length-rank quartile: ranks 1–205, 206–410, 411–615, 616–820.
- **Word id.** `<cell>-<seed>-<index>`, for example `P100-K2-short100-2000002-0`.
- **Level counts.** "empty" = reduced to the empty word (not L1); "L1 and novel" is counted by guard G2 unless a column says G1.
- **Harness modules** (`experiments/challenge_gen/hardness/`, b25): `certificate.py` (independent expansion and L0), `minimise.py` (loop erasure), `reduction.py` (reducer driver, `images16`), `powerfree.py`, `canon.py`, `classify.py` (levels), `run_baselines.py` / `run_products.py` (drivers for T-001 / T-002).
