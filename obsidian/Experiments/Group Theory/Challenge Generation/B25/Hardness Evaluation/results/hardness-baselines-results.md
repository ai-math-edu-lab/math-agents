---
title: "Hardness harness and baselines — results (T-001)"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: hardness-evaluation
status: validated
author: asetlearning
date: 2026-10-14
todo: T-001
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/validated, results]
---

# Hardness harness and baselines — results (T-001)

Pre-registration: [[hardness-harness-baselines-2026-10-13]]. Project: [[project-challenge-gen]]. Metric definitions: [[challenge-gen-success-metrics]]. Run directory: `~/Research/challenge-gen/runs/hardness-t001-20261013-r2/` (all local, no rjob job). Status: **validated for the engineering claims**; the math statements below are routed to Validator and stay `#status/conjectured` until a verdict. Group: **free B(2,5)** unless stated.

## Provenance
- Code: `b25_pyproject_agentic@10f1a75` (branch `12-hardness-harness`, clean tree, local commits only, not pushed). Superseded run directory `runs/hardness-t001-20261013/` (commit `0e3b194`, kept; its H5 criterion was too strict, see H5).
- tcgraph: `tcgraph_agentic@a0d5e92`, `tcgraph_ext` built standalone (cmake, g++ 13, pybind11 in a throwaway venv, Python 3.12.13; nothing added to a lockfile).
- Inputs: 820-word file sha256 `62c6431c…1f11e29` verified before use; relator tables for L=2 (16) and L=3 (44) rebuilt from `build_standard_relators`, sha256 stored in every sample record and checked; each relator verified to be a literal 5th power.
- Seeds: 1000001–1000005 (reported), 1000000 (smoke only). Sampler: C++ `generate_words`, one fresh process per (cell, seed); every sampled factor word is stored in `samples/*.jsonl`.
- Host: VM (2 CPUs, 3 GB), one harness process at a time, `pgrep` clean afterwards. Per-word timeout 120 s; **0 timeouts** in every set.
- Tests: `pytest experiments/challenge_gen/hardness/tests` 15 passed.

## Result per hypothesis

| H | Registered claim | Result | Verdict |
|---|---|---|---|
| H1a | loop erasure preserves the expansion | 7,000 sampled words and 2,000 planted cases: 0 changes (every erasure re-expanded) | held |
| H1b | planted `c⁻¹v⁵c·c⁻¹v⁻⁵c` padding is removed, \|F\*\| ≤ \|F_orig\| in 100% of 10³ | registered run (seeds 20261013+L, L=2 and 3, 1,000 each): 0 violations, 0 adjacent cancelling pairs survive, 0 disagreements with the naive quadratic reference. **Not structural:** an exploratory run (seed 11, L=2, 300 cases) found 1 case with \|F\*\| > \|F_orig\|, because the padding's intermediate state equals an earlier prefix state and redirects the erasure | held in the run; guarantee as worded is false in general |
| H1c | independent expansion = C++ `RelatorMap.expand` | 7,000/7,000 equal; L0 passes on 7,000/7,000 (relators 5th powers, table hash, abelianization) | held |
| H2a | every random standard-relator factor word has R₂.₅ = 1 | **7,000/7,000** (1,000 per cell; every seed) | held; 95% upper bound on the survivor rate 0.30% per cell, 0.043% pooled |
| H2b | no random word is L1 | 0/7,000 | held (same bounds) |
| H3 | screen never false-passes against certify | 0/7,000 disagreements **in either direction** (also 0/820). I had claimed the reverse could not happen; that was not proved, so both directions were measured | held |
| H4 | 820/820 fixed points, ρ ≈ 1 | **818/820.** Words 13 and 14 (0-based; 44 letters) reduce to the empty word under greedy then cyclic-exhaustive reduction (ρ = 0), level L0 only. mean ρ = 0.9976 | **falsified** |
| H5 | no-square pre-check implies the reducer returns cyc(w) | 100,000 words, 7,473 with the pre-check true: 0 violations in the sense of length and cyclic word; **20 (0.27%) returned another rotation** of cyc(w), so the literal "exactly the same string" is false and the test criterion was corrected. In 44,994 of 92,527 pre-check-false words the reducer was also a no-op (squares without a power ≥ 2.5): the pre-check is sufficient, not necessary | held up to rotation |
| H6 | D < 1 on all random cells, \|F\*\| = \|F\| in ≥ 95% | D < 1 everywhere (max 0.214, 0/7,000 with D ≥ 1). The 95% part holds in S1, S4, S5, S7 and **fails in S2 (88.4%), S3 (65.0%), S6 (87.5%)**: random words with many factors from few relators contain freely cancelling blocks. \|F\*\| > \|F\| never; 708/7,000 shrink | partly falsified |

## Level counts, ρ and D by set (certify mode, free B(2,5))

| Set | n words | L0 | L1 | L2 | survive (R₂.₅ ≠ 1) | ρ median [min, max] | D median (max) | \|F\| median → \|F\*\| median | \|w̄\| min / median / max |
|---|---|---|---|---|---|---|---|---|---|
| S1 L=2, 3–8 factors | 1000 | 1000 | 0 | 0 | 0 | 0 [0, 0] | 0.090 (0.200) | 6 → 5 | 10 / 60 / 114 |
| S2 L=2, 10–20 | 1000 | 1000 | 0 | 0 | 0 | 0 | 0.090 (0.136) | 15 → 15 | 75 / 162 / 256 |
| S3 L=2, 30–60 | 1000 | 1000 | 0 | 0 | 0 | 0 | 0.091 (0.108) | 45 → 44 | 265 / 486 / 722 |
| S4 L=3, 3–8 | 1000 | 1000 | 0 | 0 | 0 | 0 | 0.066 (0.214) | 6 → 6 | 14 / 82 / 154 |
| S5 L=3, 10–20 | 1000 | 1000 | 0 | 0 | 0 | 0 | 0.066 (0.090) | 15 → 15 | 97 / 222 / 340 |
| S6 L=3, 30–60 | 1000 | 1000 | 0 | 0 | 0 | 0 | 0.067 (0.077) | 45 → 44 | 381 / 662 / 971 |
| S7 L=3, 10–20, conj ≤ 8 | 1000 | 1000 | 0 | 0 | 0 | 0 | 0.053 (0.074) | 15 → 15 | 130 / 282 / 447 |
| 820 words | 820 | L0-ext (kbprog proof in the dataset note) | 818 | 0 (D undefined) | 818 | 1.0 [0, 1.0] | n/a | n/a | 32 / 67 / 123 |
| *Added control:* commutator products N1–N3 | 599 | not certified | n/a | n/a | 599 | 0.89 [0.20, 1.0] | n/a | n/a | 10 / 34 / 432 (median per cell 34, 91, 276) |

|F\*\|/|F| fraction equal: S1 .958, S2 .884, S3 .650, S4 .983, S5 .965, S6 .875, S7 .977. The 820 words are all cyclically reduced (n = n_cyc), so ρ = ρ_cyc there. Screen and certify results are identical on all 7,000 + 820 words.

**Reading.** The owner's prediction holds: random certified factor words (standard relators, L = 2, 3, 3–60 factors, conjugators up to 4 or 8) are never L1, and in fact never survive 2.5 reduction at all. The commutator-product control (abelianization-trivial, not certified trivial) survives with ρ ≈ 0.89, so ρ = 0 is a property of the words and not of the harness. D on random words is ≈ 0.05–0.2, far below the D ≥ 1 target; the best random D (0.214) comes from short words.

## Findings beyond the hypotheses
1. **ρ is not invariant under letter relabelling or inversion** (exploratory, not pre-registered). The reducer is rotation-invariant by construction (all shifts), but its result depends on the representative. For the 820 words, applied to all 16 images (8 letter automorphisms × inversion): 818 words have all 16 images fixed points; word 13 reduces to empty in 13 of 16 images, word 14 in 15 of 16. So "R₂.₅(w) ≠ 1" is a property of a chosen representative; a hardness claim should either fix the representative or take the minimum of |R₂.₅| over the 16 images. The dataset's claim "every word is a fixed point" ([[ds-b25-trivial-2-5reduced-aut8-20261007]]) was verified on the *parent* strings; the stored canonical representatives 13 and 14 are not fixed points (the dataset is immutable; a correction would be a new dataset with `supersedes:`; the decision is Lead's). Both words reduce to the empty word, which, if the rewriting rules are all valid, proves them trivial in free B(2,5); that agrees with the dataset's kbprog proof.
2. **Cost.** Random factor words reduce in the first step: all 7,000 certify runs took 16 s in total, p95 ≤ 7 ms per word (n ≤ 971). Surviving words are the expensive case: fit on 278 control words with n ≥ 100, certify time ∝ n^2.95; extrapolated about 2.5 s at n = 1,000 and about 290 s at n = 5,000 (a fit with no data above n = 432, an extrapolation, to be re-measured on the first real L1 candidates). The 120 s local cap is therefore reached near n ≈ 3,500 for a word that survives. Screen mode is ≤ 4.4 ms on the controls (96% of controls have the same length in screen and certify mode).
3. **Documentation mismatch.** The Python docstring of `greedy_reduce2_5` says it cyclically reduces the word; the C++ `greedyReduce` freely reduces only (`word.reduce()`, `greedy_reduction.cpp:291–296`).

## Deviations from the pre-registration
- The 118-word sets were dropped (owner, 2026-10-13); H4(b),(c) removed.
- **Not done:** the Python-mirror sampler and the Kolmogorov–Smirnov cross-check (fresh-process reproducibility replaced it: two fresh processes gave byte-identical output for cell S4, seed 1000000, 50 words; the reported seeds were sampled once and stored).
- **Done later (2026-10-14, Lead's follow-up):** D cross-check against the C++ `DehnFunctionScorer.score_sample` on all 7,000 random words, for the raw F and for the minimised F\*: 0 mismatches, max absolute difference 0.0 (`runs/…-r2/dehncheck.json`). Definitional difference: none in value; the C++ scorer returns 0 for an empty expansion (never occurs here), the harness returns undefined; both divide by the freely reduced, not cyclically reduced, length. The ρ_min16 option was added (owner decision 2026-10-14): on the 820 words it gives 818 L1, 2 L0 (words 13, 14, ρ_min16 = 0); on the 7,000 random words ρ_min16 = 0 for all (`eval_min16/`, 137 s).
- **Added:** the commutator negative control (replaces the planned replay check) and the 16-image symmetry check (exploratory).
- H5's pass criterion changed after seeing 20 rotation-only cases (stated above); H3's reverse direction measured instead of assumed. The first run directory is superseded by the second.
- No timeouts occurred, so the screen/certify timeout rules were never exercised in the grid; the timeout path is covered by a unit test.

## Math claims routed to Validator
1. Soundness of L0 for standard relators: a cyclically reduced relator that is a literal 5th power is a conjugate of u⁵ in F(a,b), hence trivial in free B(2,5); a product of conjugates of such relators equals w̄ in F(a,b) (re-expansion), hence w̄ is trivial in free B(2,5).
2. Words 13 and 14 of the 820 reduce to the empty word under the 2.5 rewriting (a heuristic tool whose rewriting rules are v^p → v^(p−5), p ≥ 2.5): confirm they are trivial in free B(2,5) (the dataset note already has a kbprog proof) and note the dataset claim mismatch.
Everything else is engineering.

## Validator verdict (2026-10-14, [[2026-10-14-t001-l0-soundness-and-words-13-14]])
1. L0 soundness for standard relators: `#status/proven` (hand proof from B(2,5) = F/⟨⟨x⁵⟩⟩; conditional on the table check and the full freely reduced equality, which Validator did not re-run).
2. Words 13 and 14 of the 820 are trivial in **free** B(2,5): `#status/proven`, with an explicit step-checked certificate (12 and 13 steps) from an independent script.
3. The dataset claim "every word is a fixed point" is `#status/disproven` for words 13 and 14.
Validator's note: the strict p > 2.5 rule finds no step on these words; the first move is length-neutral (p = 5/2, e.g. BABAB → ababa in word 13), and word 14 reaches word 13's form after one neutral move. So the dataset's "not shortened" and the harness's ρ = 0 differ by which reducer variant ran; which pin did which was not checked (conjectured). My harness run used `tcgraph_agentic@a0d5e92`, which does apply the neutral move (the rule is `q ≥ 2.5` in `greedy_reduction.cpp`). Validator suggests fixing the dataset's `property_claimed` and re-checking the other 818 for neutral-move reducibility; the harness already ran that reducer on all 818 (fixed points in all 16 images), so no further check is needed for this reducer. The dataset edit is Lead's decision.

## What still needs remote
Nothing in the registered grid. Remote becomes necessary for L1 candidates with n ≳ 3,500 in certify mode (about 5 min per word at n = 5,000 by the fit), and for any generator run. No jobs were submitted; none are pending.

## Reproduce
`python -m experiments.challenge_gen.hardness.run_baselines {sample|eval|set820|symmetry|controls|selftest|summary}` with `tcgraph_ext` on `PYTHONPATH`; code: `b25_pyproject_agentic:experiments/challenge_gen/hardness/`. Results JSONL per word (fields in the pre-registration) are in the run directory.

Verified by [[2026-10-14-t001-l0-soundness-and-words-13-14]]
