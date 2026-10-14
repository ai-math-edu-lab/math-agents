---
title: t002-dataset-relator-products-2026-10-14
hypothesis: "Random products of conjugates of the 820 proved-trivial 2.5-reduced words (alone or mixed with standard 5th-power relators) are mostly L1: at least 90% of words in every pure-dataset cell with 2 to 30 factors survive 2.5 reduction with rho_min16 >= 0.5 and are novel (not a conjugate class of a single input relator), while D stays far below 1, so no word reaches L2."
status: validated
author: asetlearning
date: 2026-10-14
todo: T-002
project: challenge-gen
instance: B(2,5)
experiment_type: hardness-evaluation
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, topic/word-problem, project/challenge-gen, status/pending, experiment, methodology]
---

# T-002: random products over the 820 relators — pre-registration

> **Terms.** Project terms are defined once in [[challenge-gen-glossary]] (ρ_min16, screen/certify, aut8 / 16 images, loop erasure, fixed point, pre-check, relator table, controls, cell names, G1/G2 and others); this note links rather than restates them.

> **Phase 1.** Written 2026-10-14 before the registered run. A calibration run on a separate seed (2000000, 8 words per cell, no reported numbers) was used for timing only; it fixed the size limits and per-cell counts below. TODO item **T-002** ([[todo-challenge-gen]]). Harness: [[hardness-baselines-results]] (T-001). Metric definitions and the min-16 convention: [[challenge-gen-success-metrics]]. Relators: [[ds-b25-trivial-2-5reduced-aut8-20261014]] (the corrected dataset, not the 20261007 one).

## Question

Do random **products of conjugates** of the 820 proved-trivial, 2.5-reduced words survive the 2.5 reducer (L1), and with what D? T-000 and the T-001 baselines showed that random products of conjugates of standard v⁵ relators always reduce to the identity (L1 = 0, 7,000/7,000). The dataset words have no powers ≥ 2.5 to speak of, so the open question is whether their products inherit that resistance. Group: **free B(2,5)**. Every word is a product of conjugates of relators trivial in free B(2,5), so it is trivial there. The dataset words are trivial by the dataset's own Knuth–Bendix proof (plus Validator's certificates for the two replaced words, [[2026-10-14-t001-l0-soundness-and-words-13-14]]); the standard relators are literal 5th powers.

## Hypotheses (falsifiable; point estimates, with 95% Clopper–Pearson intervals reported)

- **H1 positive control.** Cell P100-K1-short100 (one dataset factor): L1 rate ≥ 0.93; every L1 word is non-novel (R₂.₅ is a conjugate class of the single input relator). The only expected non-L1 words are those built on dataset lines 14 and 15 (the two words that are fixed points only for the stored representative). **Falsified** if the L1 rate is below 0.93 or any L1 word of this cell is novel.
- **H2 main.** In each pure-dataset cell (P100) with k = 2, 3–5, 6–10 and 11–30 factors from the shortest-100 subset: L1 rate ≥ 0.9 and novel-L1 rate (among all words of the cell) ≥ 0.9. **Falsified** by any cell below 0.9.
- **H3 mixing trend.** At fixed k ∈ {2, 3–5, 6–10, 11–30}, the L1 rate is non-decreasing in the dataset fraction: L1(P0) = 0 ≤ L1(P25) ≤ L1(P50) ≤ L1(P75) ≤ L1(P100) (point estimates, on decided words). Reason: standard v⁵ factors are removed by the reducer, so ρ ≈ (letters from dataset factors)/(all letters), which falls with the standard share and crosses the ρ ≥ 0.5 threshold near p ≈ 0.25. **Falsified** by any violation of the order.
- **H4 D.** L2 = 0 in every cell, and D (on F*) < 0.25 for every word. Reason: every dataset factor has ≥ 32 letters, so D ≈ k/n ≤ about 1/32, and standard factors (5 to 15 letters) cannot raise it past 1 without massive cancellation. **Falsified** by any word with D ≥ 0.25.
- **H5 length strata.** For the strata cells S1–S4 (relators ranked 1–205, …, 616–820 by length) at k = 2 and 3–5, L1 and novel-L1 rates are ≥ 0.9, and the spread of L1 rates across S1–S4 within each k is ≤ 0.1. **Falsified** otherwise.
- **H6 pre-check.** The exact power-free shortcut (no power ≥ 2.5 in w̄ and in cyc(w̄), see § Pipeline) agrees with the real reducer on the whole verified subsample (screen length = certify length = |cyc(w̄)| and, on a smaller subsample, all 16 images too). **Falsified** by one mismatch.
- **H7 screen-empty.** On a random 10% subsample of words that reduce to the empty word in screen mode, certify mode also gives the empty word. **Falsified** by one disagreement.
- **H8 L0.** The independent L0 check passes for every word (re-expansion equals the stored word, every relator is a dataset word or its inverse by hash-pinned membership, or a literal 5th power, abelianization trivial). **Falsified** by one failure.

Positive control: H1. Negative control: the P0 cells (all-standard relators, with the same conjugators), which the T-001 baselines predict to be L1 = 0.

## Problem set

Relator table (hashed; sha256 recorded in provenance and in every sample record):

| Indices | Content |
|---|---|
| 1–820 | the 820 dataset words in file order (length-sorted) |
| 821–1640 | their inverses |
| 1641–1684 | standard relators v⁵, |v| ≤ 3 (44 relators, `build_standard_relators(3, 2)`); cells marked L2 use only those of length ≤ 10 (|v| ≤ 2, 16 relators) |

Dataset: [[ds-b25-trivial-2-5reduced-aut8-20261014]], file `b25_trivial_2_5reduced_unique_aut8_20261014.txt`, sha256 `e0eeb777…631dda1` (verified at every load; mismatch stops the run). Dataset subsets by rank in the length-sorted file: **short100** = ranks 1–100 (lengths 32–55), S1 = 1–205 (≤ 59), S2 = 206–410 (≤ 67), S3 = 411–615 (≤ 83), S4 = 616–820 (≤ 123).

### Cells (35)

A factor comes from the dataset with probability p (then a uniform word of the subset, word or inverse with equal probability), otherwise a uniform standard relator. Conjugators are uniform in length 0..4, non-backtracking random words. A word is resampled if its freely reduced length is below 10.

| Group | Cells | Words per seed |
|---|---|---|
| Main grid: p ∈ {0, 0.25, 0.5, 0.75, 1} × k ∈ {1, 2, 3–5, 6–10, 11–30}, short100, standard |v| ≤ 3 | 25 | k=1,2,3–5: 60; k=6–10: 30; k=11–30: 10 |
| Strata: p = 1, S1–S4 × k ∈ {2, 3–5} | 8 | 40 |
| Standard-length sensitivity: p = 0.5, short100, |v| ≤ 2, k ∈ {3–5, 6–10} | 2 | 60 and 30 |

5 seeds per cell: total **7,550 words**. The counts are smaller for the long products because their screen and certify cost grows steeply (calibration: full cost per word ≈ n^2.96, about 7 s at n = 500 and 28 s at n = 800, 16 images included).

## Pipeline (per word, one process, sequential)

1. **L0** (independent, pure Python): re-expand the stored factor word, check every relator, abelianization.
2. **F\*** by chronological loop erasure; D = |F\*|/|w̄|, D_raw = |F|/|w̄|.
3. **Exact shortcut.** If neither w̄ (linear windows) nor cyc(w̄) (cyclic windows of the doubled word, length ≤ n) contains a power ≥ 2.5, the reducer is provably a no-op in every shift (the rewrite needs `q ≥ 2.5`, `greedy_reduction.cpp`): R₂.₅(w) is cyc(w̄) up to rotation, and the same holds for all 16 images. These words cost nothing. Tested against the reducer (H6).
4. **Otherwise** run the reducer: **screen** (shifts {0, 0.5}) on the generated word for every word. If it reduces to the empty word the word is decided, not L1 (H7 checks this). If it survives: **certify** (all shifts), then **ρ_min16** (certify on all 16 images; owner convention). Limits (set from the calibration): certify only if n ≤ 2000; ρ_min16 only if n ≤ 800; each reducer call has a 120 s timeout. Words beyond the limits, and timeouts, are recorded as **undecided** (`L0?`), never counted as L1 or as failures.
5. **Level** (free B(2,5)): L0; L1 = certify R ≠ empty and ρ_min16 ≥ 0.5; L2 = L1 and D ≥ 1.
6. **Novelty guard** (L1 words only). Let R be the certify result. canon(·) is the shortlex-least string over the 16 images and all rotations. R is **non-novel** if canon(R) equals canon of one of the relators used in this word's F (up to inversion and the 8 letter automorphisms). Otherwise **novel**. Also recorded: whether canon(R) equals canon of *any* of the 820 words.

## Seeds, sampler and reproducibility

- Sampler seeds 2000001–2000005 (calibration 2000000). Distinct from T-001 (1000001–5) and from PatternBoost's seed range.
- **Pure-Python sampler** with `random.Random(f"T002-{seed}-{cell}")`, so seeds fully determine the words on any machine. Reason for not using the C++ sampler: the mixing ratio p needs a weighted draw between two relator sources, which `generate_words` cannot do, and the Python sampler does not depend on the T-011 stream change. Distribution check against the C++ sampler (T-001 cell S4, 1,000 words, standard relators, 3–8 factors, conjugators ≤ 4): expanded length, factor count and mean conjugator length pass a two-sample Kolmogorov–Smirnov test at 5% (D = 0.022, 0.018, 0.033 against the critical 0.061). Every sampled word is stored in JSONL.
- Merged b25 main (T-011) into the branch; `tcgraph_ext` rebuilt against `tcgraph_agentic@1b52b4d` (the new pin). The reducer is unchanged by T-011; the build SHA is recorded in provenance.

## Statistics

Rates with exact two-sided 95% Clopper–Pearson intervals per cell (novel-L1 rate as Lead asked). Trend and spread statements (H3, H5) are descriptive point-estimate comparisons; no p-value is claimed. D and ρ distributions as medians and extremes. This experiment measures a baseline, so no gain over a competitor is tested.

## Execution

- **Local (VM)**, two sequential shards of the same eval (two heavy processes, under the cap; `pgrep` before launch), `timeout` on every call.
- **Remote only for undecided words** (n > 800 for ρ_min16, n > 2000 for certify, or timeouts). After the run I send Lead the list and a wall-clock estimate before any rjob submission. Expected: mostly cells with 11–30 factors.
- Branch `14-t002-dataset-relator-products` off `12-hardness-harness` (renamed from 13 on Lead's request), local commits only.

## Anti-pattern check

- *Tuning on the test set:* limits and counts come from seed 2000000, not from the reported seeds; the cell grid is fixed above.
- *Seeds:* all five are listed; every word is stored.
- *Circularity:* the dataset relators are trusted through the dataset's own KB proof, and that is stated, not re-derived; L0 is independent of the C++ expansion.
- *Necessary versus sufficient:* L1 here means "resists the 2.5 reducer", not "hard to decide". ρ ≥ 0.5 and D are the owner's proxies. A survivor can still be easy for another solver; nothing here shows hardness beyond the metrics.
- *Group named:* free B(2,5) throughout; B₀(2,5) is not used.

## Deviations from the brief (reasons)

- Sampler is Python, not the C++ fresh-process workaround (ratios, seeds). Mixing is a Bernoulli draw per factor, so the realised dataset share varies per word; it is stored (`n_dataset`).
- Standard source is |v| ≤ 3 in the main grid; |v| ≤ 2 only in two sensitivity cells.
- Counts per cell are unequal and smaller for long products; ρ_min16 is capped at n ≤ 800 locally; an exact power-free shortcut replaces the reducer where it provably does nothing.
- Screen-empty words are classified without a certify run, with a 10% verification subsample.

## Results
See [[t002-dataset-relator-products-results]]. H2–H8 held; H1 held for L1 rate but its novelty clause was falsified as registered (guard flaw, refined guard G2 in the results).
