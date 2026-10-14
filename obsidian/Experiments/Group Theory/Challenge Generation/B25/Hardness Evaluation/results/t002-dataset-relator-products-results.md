---
title: "T-002: random products over the 820 relators — results"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: hardness-evaluation
status: validated
author: asetlearning
date: 2026-10-15
todo: T-002
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/validated, results]
---

# T-002: random products over the 820 relators — results

> **Terms.** Project terms are defined once in [[challenge-gen-glossary]] (ρ_min16, screen/certify, aut8 / 16 images, loop erasure, fixed point, pre-check, relator table, controls, cell names, G1/G2 and others); this note links rather than restates them.

Pre-registration: [[t002-dataset-relator-products-2026-10-15]]. Harness: [[hardness-baselines-results]]. Relators: [[ds-b25-trivial-2-5reduced-aut8-20261014]]. Metrics: [[challenge-gen-success-metrics]]. Status: **validated for the engineering claims**. Group: **free B(2,5)**, with the triviality of the dataset words resting on the dataset's Knuth–Bendix proof. All 7,550 words were decided locally (no rjob job, 0 undecided at the end). No new math claim needed Validator (a product of conjugates of words trivial in the group is trivial there).

## Provenance
- Code: `b25_pyproject_agentic` branch `14-t002-dataset-relator-products` (off `12-hardness-harness`, merged with main incl. T-011), local commits, not pushed. Registered run at `d7aa636`; analysis scripts added afterwards (`t002_analyze.py`, `t002_post.py`, flag `--only-ids`).
- tcgraph: `tcgraph_agentic@1b52b4d` (the new pin), `tcgraph_ext` built standalone from a worktree of that commit (g++ 13.3, pybind11 3.1.0, Python 3.12.13).
- Dataset sha256 `e0eeb777…631dda1` verified at load; relator-table sha256 `fd1a6fed…c5d1` (in every sample record).
- Seeds 2000001–2000005 (calibration 2000000, not reported). Sampler: pure Python with an explicit `random.Random`; it passes a Kolmogorov–Smirnov comparison with the C++ sampler (expanded length D = 0.022, factor count 0.018, mean conjugator length 0.033, critical 0.061, 1,000 words each).
- Run dir: `~/Research/challenge-gen/runs/t002-products-20261015/` (samples, evalA/evalB, evalUA/evalUB for the 86 long words, merged/, analysis_final/). Host: VM, two shards, about 57 minutes of wall-clock for the main run (two shards) plus about 83 minutes for the long words (two shards).
- Tests: 22 pytest cases pass (power-free shortcut vs reducer, canonical form, sampler determinism).

## Results per cell (certify mode, ρ_min16 convention, free B(2,5))

N = 7,550 words. 2,080 reduce to the empty word, **5,221 are L1**, **4,012 are L1 and novel** (guard G2 below), 0 are L2. All L0 checks pass (7,550/7,550). Table (novelty by the refined guard G2; the registered guard G1 in the second to last column):

| Cell | words | empty | L1 | L1 rate [95% CI] | novel L1 (G2) | novel rate [95% CI] | novel (G1) | ρ_min16 median (min) | n median (max) | D median (max) |
|---|---|---|---|---|---|---|---|---|---|---|
| P0-K1-short100 | 300 | 300 | 0 | 0.000 [0.000, 0.012] | 0 | 0.000 [0.000, 0.012] | 0 | - | 16 (23) | 0.062 (0.100) |
| P0-K2-short100 | 300 | 300 | 0 | 0.000 [0.000, 0.012] | 0 | 0.000 [0.000, 0.012] | 0 | - | 32 (46) | 0.064 (0.167) |
| P0-K3-5-short100 | 300 | 300 | 0 | 0.000 [0.000, 0.012] | 0 | 0.000 [0.000, 0.012] | 0 | - | 60 (104) | 0.066 (0.111) |
| P0-K6-10-short100 | 150 | 150 | 0 | 0.000 [0.000, 0.024] | 0 | 0.000 [0.000, 0.024] | 0 | - | 118 (173) | 0.066 (0.093) |
| P0-K11-30-short100 | 50 | 50 | 0 | 0.000 [0.000, 0.071] | 0 | 0.000 [0.000, 0.071] | 0 | - | 296 (462) | 0.068 (0.078) |
| P25-K1-short100 | 300 | 232 | 66 | 0.220 [0.174, 0.271] | 0 | 0.000 [0.000, 0.012] | 18 | 0.96 (0.80) | 18 (62) | 0.056 (0.100) |
| P25-K2-short100 | 300 | 175 | 123 | 0.410 [0.354, 0.468] | 42 | 0.140 [0.103, 0.184] | 60 | 0.76 (0.51) | 37 (118) | 0.054 (0.167) |
| P25-K3-5-short100 | 300 | 111 | 131 | 0.437 [0.380, 0.495] | 74 | 0.247 [0.199, 0.299] | 86 | 0.66 (0.50) | 91 (234) | 0.043 (0.119) |
| P25-K6-10-short100 | 150 | 11 | 79 | 0.527 [0.444, 0.609] | 79 | 0.527 [0.444, 0.609] | 79 | 0.62 (0.50) | 188 (350) | 0.040 (0.069) |
| P25-K11-30-short100 | 50 | 1 | 20 | 0.400 [0.264, 0.548] | 20 | 0.400 [0.264, 0.548] | 20 | 0.58 (0.50) | 458 (832) | 0.041 (0.063) |
| P50-K1-short100 | 300 | 154 | 145 | 0.483 [0.426, 0.541] | 0 | 0.000 [0.000, 0.012] | 43 | 0.96 (0.83) | 39 (62) | 0.026 (0.100) |
| P50-K2-short100 | 300 | 79 | 220 | 0.733 [0.679, 0.783] | 88 | 0.293 [0.242, 0.348] | 121 | 0.79 (0.51) | 70 (121) | 0.029 (0.143) |
| P50-K3-5-short100 | 300 | 35 | 239 | 0.797 [0.747, 0.841] | 201 | 0.670 [0.614, 0.723] | 206 | 0.79 (0.50) | 132 (266) | 0.029 (0.094) |
| P50-K6-10-short100 | 150 | 3 | 131 | 0.873 [0.809, 0.922] | 131 | 0.873 [0.809, 0.922] | 131 | 0.74 (0.51) | 268 (479) | 0.030 (0.072) |
| P50-K11-30-short100 | 50 | 0 | 47 | 0.940 [0.835, 0.987] | 47 | 0.940 [0.835, 0.987] | 47 | 0.75 (0.54) | 678 (1090) | 0.029 (0.058) |
| P75-K1-short100 | 300 | 80 | 218 | 0.727 [0.672, 0.776] | 0 | 0.000 [0.000, 0.012] | 65 | 0.96 (0.83) | 53 (63) | 0.019 (0.100) |
| P75-K2-short100 | 300 | 34 | 265 | 0.883 [0.841, 0.917] | 164 | 0.547 [0.488, 0.604] | 185 | 0.93 (0.50) | 86 (121) | 0.023 (0.091) |
| P75-K3-5-short100 | 300 | 4 | 285 | 0.950 [0.919, 0.972] | 263 | 0.877 [0.834, 0.912] | 268 | 0.87 (0.50) | 168 (284) | 0.024 (0.083) |
| P75-K6-10-short100 | 150 | 0 | 150 | 1.000 [0.976, 1.000] | 150 | 1.000 [0.976, 1.000] | 150 | 0.87 (0.53) | 344 (538) | 0.023 (0.043) |
| P75-K11-30-short100 | 50 | 0 | 50 | 1.000 [0.929, 1.000] | 50 | 1.000 [0.929, 1.000] | 50 | 0.86 (0.68) | 909 (1336) | 0.023 (0.028) |
| P100-K1-short100 | 300 | 11 | 285 | 0.950 [0.919, 0.972] | 0 | 0.000 [0.000, 0.012] | 91 | 0.95 (0.83) | 54 (63) | 0.019 (0.031) |
| P100-K2-short100 | 300 | 8 | 282 | 0.940 [0.907, 0.964] | 277 | 0.923 [0.887, 0.951] | 278 | 0.97 (0.50) | 106 (124) | 0.019 (0.028) |
| P100-K3-5-short100 | 300 | 0 | 299 | 0.997 [0.982, 1.000] | 299 | 0.997 [0.982, 1.000] | 299 | 0.97 (0.54) | 210 (288) | 0.019 (0.025) |
| P100-K6-10-short100 | 150 | 0 | 150 | 1.000 [0.976, 1.000] | 150 | 1.000 [0.976, 1.000] | 150 | 0.97 (0.58) | 412 (564) | 0.019 (0.021) |
| P100-K11-30-short100 | 50 | 0 | 50 | 1.000 [0.929, 1.000] | 50 | 1.000 [0.929, 1.000] | 50 | 0.96 (0.81) | 1094 (1610) | 0.019 (0.021) |
| P100-K2-S1 | 200 | 3 | 196 | 0.980 [0.950, 0.995] | 193 | 0.965 [0.929, 0.986] | 193 | 0.97 (0.51) | 114 (127) | 0.018 (0.026) |
| P100-K3-5-S1 | 200 | 0 | 199 | 0.995 [0.972, 1.000] | 199 | 0.995 [0.972, 1.000] | 199 | 0.97 (0.63) | 228 (308) | 0.018 (0.024) |
| P100-K2-S2 | 200 | 0 | 200 | 1.000 [0.982, 1.000] | 199 | 0.995 [0.972, 1.000] | 199 | 0.98 (0.51) | 130 (145) | 0.015 (0.024) |
| P100-K3-5-S2 | 200 | 0 | 200 | 1.000 [0.982, 1.000] | 200 | 1.000 [0.982, 1.000] | 200 | 0.97 (0.74) | 258 (346) | 0.015 (0.017) |
| P100-K2-S3 | 200 | 0 | 200 | 1.000 [0.982, 1.000] | 200 | 1.000 [0.982, 1.000] | 200 | 0.98 (0.62) | 154 (173) | 0.013 (0.016) |
| P100-K3-5-S3 | 200 | 0 | 200 | 1.000 [0.982, 1.000] | 200 | 1.000 [0.982, 1.000] | 200 | 0.98 (0.79) | 312 (413) | 0.013 (0.015) |
| P100-K2-S4 | 200 | 0 | 200 | 1.000 [0.982, 1.000] | 200 | 1.000 [0.982, 1.000] | 200 | 0.99 (0.63) | 190 (228) | 0.011 (0.014) |
| P100-K3-5-S4 | 200 | 0 | 200 | 1.000 [0.982, 1.000] | 200 | 1.000 [0.982, 1.000] | 200 | 0.99 (0.86) | 377 (538) | 0.011 (0.013) |
| P50-K3-5-short100-L2 | 300 | 36 | 251 | 0.837 [0.790, 0.877] | 196 | 0.653 [0.597, 0.707] | 207 | 0.82 (0.51) | 124 (275) | 0.031 (0.200) |
| P50-K6-10-short100-L2 | 150 | 3 | 140 | 0.933 [0.881, 0.968] | 140 | 0.933 [0.881, 0.968] | 140 | 0.80 (0.51) | 254 (501) | 0.032 (0.097) |

Cell naming: P<percent of factors from the dataset>-K<number of factors>-<dataset subset>; subset short100 = the shortest 100 words, S1–S4 = length quartiles by rank, suffix L2 = standard relators with |v| ≤ 2 only. The two L2 cells are the standard-length sensitivity check.

## Hypotheses

| H | Registered claim | Result | Verdict |
|---|---|---|---|
| H1 | one-factor cell: L1 rate ≥ 0.93, every L1 word non-novel | L1 285/300 = 0.950 [0.919, 0.972] holds. **Novel under the registered guard G1: 91 of 285**, so as registered, **falsified**. All 91 are the same cyclic word as a used relator up to the reducer's length-neutral rewrites (87 same length, 4 shorter); under the refined guard G2 novel = 0/285 | **falsified as registered (guard flaw)**; the L1 part held |
| H2 | pure-dataset cells, k ≥ 2: L1 ≥ 0.9 and novel ≥ 0.9 | k=2: 0.940 / 0.923 (G2); k=3–5: 0.997 / 0.997; k=6–10: 1.000 / 1.000; k=11–30: 1.000 / 1.000 (50/50, after the long words were run locally) | held |
| H3 | L1 rate non-decreasing in the dataset share, P0 = 0 | k=2: 0, .41, .73, .88, .94; k=3–5: 0, .44, .80, .95, .997; k=6–10: 0, .53, .87, 1, 1; k=11–30: 0, .40, .94, 1, 1; all P0 cells L1 = 0 (1,100 words) | held |
| H4 | L2 = 0 and D < 0.25 | L2 = 0 in all 7,550; D max 0.200 (a mixed cell with short standard relators); D median ≈ 0.02 in pure-dataset cells | held |
| H5 | strata S1–S4: L1 and novel ≥ 0.9, spread ≤ 0.1 | L1 rates 0.98–1.00, novel 0.965–1.000, spread ≤ 0.02 | held |
| H6 | power-free shortcut agrees with the reducer | **420/420** shortcut words (all of them, n ≤ 600) match: screen length = certify length = |cyc(w̄)|; 6/6 on the 16-image sub-check. (Pre-registered subsample was only 14 words; the full check is post-hoc.) | held |
| H7 | 10% of screen-empty words: certify also empty | 176/176 agree | held |
| H8 | independent L0 passes everywhere | 7,550/7,550 | held |

> **2026-10-15 (owner decision):** guard G2 is the adopted definition of "novel L1"; G1 is superseded and kept here only as a historical number ([[challenge-gen-glossary#novel L1 and the guards G1 and G2]]).

## Findings
1. **Products of the dataset words survive the 2.5 reducer, standard-relator products do not.** With one dataset factor and k−1 standard factors the standard parts are removed and the dataset conjugate remains (that is why p matters through ρ, not through survival): L1 rises with p because ρ_min16 ≈ (letters from dataset factors)/(all letters) crosses the 0.5 threshold near p = 0.25, as predicted. Pure-dataset products with k ≥ 3 are L1 in 99.7–100% of cases.
2. **D is far from 1.** Every dataset factor has ≥ 32 letters, so D = |F\*|/|w̄| ≈ k/n ≤ about 0.03 for pure-dataset words (median 0.019–0.021 at k=6–30). The best value anywhere is 0.200, from short standard relators that the reducer removes anyway. L2 needs D ≥ 1, which this construction cannot reach without massive cancellation between factors. This answers the T-002 question: **L1 is easy with these relators; L2 is out of reach for random products.**
3. **The registered novelty guard was flawed.** Comparing the reducer's output with the used relators' classes fails because the reducer applies length-neutral rewrites (p = 5/2) and, through the greedy-first step on a non-cyclically-reduced word, can even lengthen the cyclic class (for example a 53-letter relator conjugate coming out as 55 letters). Refined guard G2 (post-hoc): R is non-novel if it matches a used relator's class or the reducer's output on one of the single factors `c⁻¹ r c`. G1 reports 4,335 novel of 5,221 L1; G2 reports **4,012**. Both are reported; G2 gives 0 novel in all one-factor cells, as it must.
4. **L1 is not conjugation-invariant in the harness.** In the one-factor cell 15 of 300 words (5%) are not L1 although their cyclic word is a conjugate of a dataset word: lines 14 and 15 (the two replaced words, 8 words) and five further lines (18, 26, 44, 76, 79; 7 words). The linear greedy step on the conjugated word w̄ creates powers at the junction with the conjugator, and the images of those words reduce. So "L1 by construction" for a single factor holds for 95%, not 100%.
5. **Examples of novel L1 words** (ids in `merged/results.jsonl`): `P100-K2-short100-2000002-0` (two inverse dataset factors, lines 82 and 49; n = 116, |R₂.₅| = 116, ρ_min16 = 1.0, |F\*| = 2, D = 0.017); `P50-K3-5-short100-2000001-0` (four factors, three from the dataset and one inverse standard-range index; n = 185, |R₂.₅| = 168, ρ_min16 = 0.908, |F\*| = 4, D = 0.022).
6. **Cost.** The exact power-free shortcut resolved 420 words for free; the whole grid cost about 4.3 hours of reducer CPU time, dominated by ρ_min16 on long survivors. The 86 words with n between 812 and 1,610 took about 83 minutes on two cores locally; the estimate from the n^2.96 fit (6,500 s) was accurate.

## Deviations
- Sampler is Python (reason in the pre-registration). Mixing is Bernoulli per factor.
- The limits of the registered run (ρ_min16 for n ≤ 800) left 86 words undecided; I ran them locally afterwards instead of submitting an rjob job, because the estimate (about 1.8 core-hours) was below the remote overhead. The decision rule was local-first; the limit was a calibration choice, not a result.
- Novelty guard G1 as registered is kept in the table; G2 is the refined, post-hoc guard (finding 3).
- H6's check was extended after the run to all shortcut words.

## What still needs remote
Nothing from T-002. Remote becomes necessary for longer products (k > 30 or longer relators), where ρ_min16 on n above about 2,000 costs minutes per word.

## Reproduce
`python -m experiments.challenge_gen.hardness.run_products {sample|eval|summary|xcheck}`, then `t002_analyze` and `t002_post` (see the module docstrings); `tcgraph_ext` on `PYTHONPATH`, `TCGRAPH_SRC` pointing at the tcgraph worktree.
