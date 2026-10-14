---
title: "Challenge generation — difficulty metrics and success criteria (B(2,5))"
domain: group-theory
project: challenge-gen
instance: B(2,5)
status: draft
author: asetlearning
date: 2026-10-05
tags: [agent/human, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/draft, decision]
---

# Challenge generation: difficulty metrics and success criteria (B(2,5))

> **Owner's definitions**, set 2026-10-05 by Alex Myasnikov (asetlearning). They replace "similarity to the challenge words" as the main objective. Thresholds and design choices were confirmed by the owner. The implementation notes are proposals until code exists.

## Goal

Generate words in the free Burnside group **B(2,5)** that are **provably trivial**, by construction or with a certificate, and that are **not easy to decide**: a solver should not be able to tell quickly that they are trivial.

## Notation

- **Certificate.** F = (k₁,c₁) … (k_m,c_m) is a factor word, i.e. a list of (relator index, conjugator) pairs. Its expansion is w = ∏ cᵢ⁻¹ R_{kᵢ} cᵢ, freely reduced.
- **Reduced word.** w̄ is the freely reduced expansion of F, and n = |w̄|.
- **2.5 reduction.** R₂.₅(w) = `greedyReduceCyclicExhaustive(greedyReduce(w̄))`, in tcgraph `reduction2_5`. From Python it is `greedy_reduce_cyclic_exhaustive2_5(greedy_reduce2_5(w))`, via `tcgraph_ext` / `algorithms/word_problem.py`.

## Level 0: valid challenge (required for everything below)

1. **Certified.** Re-expanding F gives exactly w̄. Every relator used is trivial in free B(2,5):
   - the standard relators v⁵, |v| ≤ L, qualify automatically;
   - relators from a file or from BPE must carry their own certificate of triviality in **free** B(2,5). Triviality in B₀(2,5) is not enough.
2. **Sanity check.** The abelianization is trivial: exponent sums ≡ 0 mod 5. This is a cheap bug detector, not a proof.
3. **Recorded with the challenge:** the minimised certificate F* (see Metric 2) and the generation provenance (code SHAs, config, seeds).

## Metric 1: resistance to 2.5 reduction (heuristic difficulty)

**Definition.** ρ(w) = |R₂.₅(w)| / |w̄|.

**Why this threshold works.** The owner reports, from experiments, that **every randomly generated factor word reduces to the identity under 2.5 reduction**, i.e. ρ = 0. Generic certified words therefore fail this metric, and resisting 2.5 reduction is a meaningful difficulty threshold even though the reducer is heuristic. The baseline should re-measure ρ on random factor words in every new setting, to confirm the threshold still separates them.

**Pass.** R₂.₅(w) ≠ 1 **and** ρ(w) ≥ **0.5**. The value of ρ is reported for every final candidate, so the threshold can be revised later.

**Cost.**

| Step | Cost |
|---|---|
| `greedyReduce` (`findSquares`) | O(n²) |
| `greedyReduceCyclic`, all shifts | ≈ O(n³) |
| `greedyReduceCyclicExhaustive` | repeats `greedyReduceCyclic` |

Guidance for using it sparingly:
- **Two modes.**
  - *Screen* mode passes `fractions = {0, 0.5}` (as the `length_range` scorer does) and is used inside the loop on the pool or top-k.
  - *Certify* mode uses all cyclic shifts and runs only on final candidates. ρ is reported in certify mode.
- **Never run it per local-search neighbour.** Run it on the pool or top-k after each iteration, and cache results by word hash (`WordHash`).
- **Cheap pre-checks.** First test whether w̄ contains any subword power with exponent ≥ 2.5 (maximal-power detection). If none exists, `greedyReduce` cannot rewrite anything. This needs verifying against the code before relying on it.
- Lengths are measured on freely reduced words. Also record the cyclically reduced length.

## Metric 2: Dehn-function proxy (theoretical difficulty)

**Background.** Owner's motivation: Myasnikov–Ushakov ([[myasnikov-ushakov-2011-random-van-kampen]]; the full text was not accessible, so this comes from the abstract and later restatements) show that a **random van Kampen diagram over a fixed finitely presented group is hyperbolic**, even when the group is not. The filling function they introduce is **depth** δ(w): for hyperbolic groups δ(w) = O(log |w|), and a relator-closure solver runs in Õ(|w|·L(R)^{δ(w)}). Random relator-insertion words, which are exactly our baseline factor words, are therefore generic and easy. Hard challenges must have atypically large fillings. The paper's results concern **depth, not area**, and assume a finite presentation, which B(2,5) is not. Using area (D below) is the owner's choice of proxy, and depth is a candidate companion metric (see Open questions).

**Definition.** D(w) = |F*| / |w̄|, where F* is the **minimised** certificate. This is the tcgraph `DehnFunctionScorer` (`pb_scoring.cpp:340`, `#factors / |expanded freely reduced word|`), applied to F* rather than to the raw F.

**Why the certificate must be minimised.** |F| is an upper bound on the area of w̄ (the minimal number of relators in a van Kampen diagram), not the area itself. A raw F can be inflated without changing w̄. The standard set contains both v⁵ and v⁻⁵, so a pair c⁻¹v⁵c · c⁻¹v⁻⁵c cancels freely while adding 2 to |F|. Unminimised scores reward padding. The minimisation:
- **Loop erasure.** Track the freely reduced prefix words P_j = expand(f₁…f_j). If P_i = P_j for some i < j, the block f_{i+1}…f_j freely cancels; delete it and repeat. A hash of the free-reduction stack makes this roughly linear in the total expanded length. This removes adjacent inverse pairs and every longer freely cancelling block.
- **What it does not remove.** Blocks that cancel only modulo relators stay. So D(w) on F* is still an **upper bound** on area/n. True area lower bounds are out of reach in general, and this caveat must accompany any claim.

**Gate.** D is counted toward success only for words that **pass Metric 1**.

**Targets.**
- **Good challenge:** D(w) ≥ 1 on F*, i.e. at least as many factors as letters.
- **Great success:** quadratic growth, |F*| ≍ c·n². This is a property of a **family** across lengths n, not of a single word. Fit the exponent α in |F*| ∝ n^α over Metric-1-passing words at several n; α ≈ 2 is the target. A single word only has a ratio.

## Owner decision 2026-10-14: representative convention for ρ (T-001)

Source: the T-001 baselines ([[hardness-baselines-results]]). The heuristic reducer is rotation-invariant but **not invariant under letter relabelling or inversion**: for 2 of the 820 words of [[ds-b25-trivial-2-5reduced-aut8-20261007]], 13 of 16 and 15 of 16 images (8 letter automorphisms × inversion) reduce to the empty word, while the stored strings were fixed points of the parent form. Validator: the words are trivial in free B(2,5) (proven).

**Decision.** Any hardness claim uses ρ_min16 = min over the 16 images of |R₂.₅(image)| / |w̄|. Screening may use the generated word only; all 16 images are computed on finalists. The definitions above are unchanged; this fixes which representative a reported ρ refers to. Implementation: `--min16` in `experiments/challenge_gen/hardness/run_baselines.py` (b25 branch `12-hardness-harness`), record fields `min16_lens`, `min16_len`, `rho_min16`; the level classification uses ρ_min16 when the flag is set.

## Success levels

| Level | Criterion | Meaning |
|---|---|---|
| L0 Valid | Certificate re-expands to w̄; standard (or certified) relators; abelianization passes | Provably trivial in free B(2,5) |
| L1 Hard (heuristic) | L0, R₂.₅(w) ≠ 1, ρ ≥ 0.5 (certify mode) | Defeats the reducer that kills all random factor words |
| L2 Hard + high filling | L1 and D(w) ≥ 1 on F* | Non-generic filling, an upper-bound proxy |
| L3 Great | A family of L1 words with \|F*\| growing ≈ quadratically in n (fitted α ≈ 2) | Quadratic area as a function of reduced length (proxy) |

**Reporting** for every run: counts and rates at each level, the distribution of ρ and of D (on F*), n, |F| versus |F*|, and the generation cost. The baseline is random factor words from the same sampler; the owner's finding predicts ρ = 0 for all of them.

## Secondary (optional)

Similarity to the 150 real challenge words (edit/Hellinger scorers) is kept as an optional shaping term or diagnostic. It is no longer an objective. The real challenge words are known trivial only in B₀(2,5) ([[2026-09-30-b25-b0-challenge-triviality]]), so they cannot be L0 instances.

## Open questions

- **Evidence so far (2026-07-23 run, [[patternboost-generation-results]]):** maximising raw D alone gave 0/~300k L1 words and a best D of 0.344. It shrank the words instead of growing the factor count. The objective needs a Metric-1 term or a length floor.

- Does PatternBoost with an objective of the form "ρ (screen mode) × D(F*)" escape the generic regime, or does it find shortcuts? Remaining loopholes include cancellation modulo relators and long conjugators that inflate n.
- Is there a cheap **lower** bound on area for B(2,5) words that could replace the upper-bound proxy?
- **Depth versus area.** Compute a depth statistic from the certificate's diagram, i.e. how deeply nested the factors are relative to the boundary. A certificate with many factors can still describe a shallow "fan" diagram that relator-closure solvers finish in a few rounds. Test which of D and depth better predicts solver failure.
- Interaction with length: D ≥ 1 is easier for short w̄. Should successes be reported by length band?

## Related material
- [[project-challenge-gen]] · [[Challenge Generation/_progress]]
- [[B25/PatternBoost Generation/_type|PatternBoost Generation]]: the current generator
- [[myasnikov-ushakov-2011-random-van-kampen]]: theory anchor for Metric 2
- [[dehn-function]] · [[kapovich-2003-generic-case-complexity]] (generic instances are easy) · [[_synthesis-hard-instance-generation]]
- [[dep-tcgraph-agentic]]: 2.5 reduction and `DehnFunctionScorer`
