---
title: "T-020 — F* interleaving (Peiffer) loophole and its fix"
status: validated
domain: group-theory
project: challenge-gen
claim: "Two non-contiguous factors that cancel after Peiffer moves survive loop erasure; a pairwise test removes them; finite B(2,5) would give a linear Dehn function over {u⁵}"
claimant: MathExpert (via Lead), Developer (PR #9)
verification_method: "hand proofs; witnesses; exhaustive deletion-order search; randomised checks against direct re-expansion"
tools_used: ["python3 3.12.3", "b25 hardness harness @ b98c938 (expand, loop_erase, std_table)", "PR #9 peiffer_reduce @ 9a35fd2", "tcgraph_ext relator table (tcgraph_agentic@a0d5e92 build)"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/proof-certificates, topic/dehn-function, project/challenge-gen, status/validated, proof]
---

# Validation — T-020 Peiffer loophole
Triage: [[2026-10-14-t020-peiffer-loophole-triage]]. Scripts: `Agents/asetlearning/Validator/scratch/t020_*.py`.

**Terms.** A factor is f = c⁻¹rc, with r a relator u⁵ and c the conjugator. F = (f_1,…,f_N) and w = f_1⋯f_N, freely reduced. P_k = f_1⋯f_k is the k-th prefix. N* = |F*|, the factor count after loop erasure (the removal of contiguous blocks whose product is 1). **Prefix coordinates:** g_k = P_{k−1} f_k P_{k−1}⁻¹. These give w = g_N⋯g_1 (the product telescopes). A **Peiffer move** swaps neighbours: f_k f_{k+1} = f_{k+1}·(f_{k+1}⁻¹ f_k f_{k+1}).

## Claim 1 — the loophole: VALIDATED (proof). T-001 case: NOT an instance
If f_j = (M⁻¹ f_i M)⁻¹ with M = f_{i+1}⋯f_{j−1}, then f_i M f_j = f_i M M⁻¹ f_i⁻¹ M = M in F(a,b). So deleting f_i and f_j leaves w unchanged. f_j is a legitimate factor: f_j = (c_i M)⁻¹ r_i⁻¹ (c_i M). Loop erasure keeps both, because no prefix state repeats. So N* overstates the certificate by 2, while true area (a minimum) is unaffected. In data: PR #9 finds 2 pairs on the T-003 job-1 word (N* 15 → 11, Developer).

**T-001 "|F*| > |F_orig|" (seed 11, L=2, 300 cases; reproduced with `std_table`, case 132):** N_orig 8, padded 16, F* 9. PR #9 finds **0 pairs** in that F*, and N stays 9. Mechanism: chronological loop erasure hit an earlier prefix state through padding. It dropped the original factor (1, a) together with pad halves, and kept two orphaned halves of *different* pads, (5, ε) and (2, ε), whose product equals that one factor. This is an artifact of erasure order (first-occurrence erasure is not the minimum over erasure orders). The pair fix does not address it.

## Claim 2a — test correctness: VALIDATED
- The M-form test (f_j == free_reduce(M⁻¹ f_i⁻¹ M)) is equivalent to **g_j = g_i⁻¹**, by direct computation from P_{j−1} = P_{i−1} f_i M. The two forms agree on 536/536 planted pairs.
- The test compares **elements of F**, so relator labels play no role. A rotation of r⁻¹, a different conjugator, or another table entry with the same element are all covered. Conjugacy alone is *not* enough, and the test correctly does not accept it.
- **Exact general criterion:** deleting any set S = {s_1 < … < s_r}, with the other f's kept, leaves w unchanged **iff g_{s_r}⋯g_{s_1} = 1** (ordered product of the current g's). Proof: deleting f_s alone gives g_s⁻¹·w and conjugates the later g's by g_s; induct over S. Checked against direct re-expansion on 28,685 random subsets (660 deletable): 0 mismatches.
- PR #9 code: the test is correct, w is asserted unchanged after every deletion, and an adjacent inverse pair is the case j = i+1 (M empty).

## Claim 2b — deletion order: MATTERS (replicated, empirical)
Deleting a pair conjugates the g's strictly between i and j. That can create or destroy *crossing* pairs (k < i < l < j). Exhaustive search over all maximal deletion sequences: 4/400 planted words had different final N (always by 2). Developer's order (i ascending, smallest j, rescan) missed the minimum in **1/2,300** words, by 2. So N*_P (N* after pair deletion) is an upper bound that depends on order. Exact minimisation is exponential, so keep the deterministic order and document it.

## Claim 2c — larger blocks: EXIST (witness); frequency in practice unknown
- **Proper-power tuples.** If the table holds v⁵ with v = t^k a proper power ((aa)⁵, (aaa)⁵, …), then a⁵·a⁵·(AA)⁵ = 1 with no inverse pair. Witness: F = [(ab)⁵, a⁵, a⁵, (b⁵)^g, ((AA)⁵)^M], N = 5. Loop erasure keeps 5, the pair test finds none, and w equals the expansion of 2 factors. By Lyndon–Schützenberger (x^m y^n z^p = 1 with m, n, p ≥ 2 in a free group ⇒ x, y, z commute), a triple of conjugates of 5th powers multiplies to 1 *only* if the three share a root. Larger relation-free tuples are not ruled out.
- **Sufficient test for them (root test):** write each g_k = (h s h⁻¹)^e with s primitive, group by the element h s h⁻¹, and delete any subset whose exponents sum to 0. This is sound by the exact criterion. With all g's computed once it costs O(N·ℓ) plus small subset sums (ℓ = expanded length). On Peiffer-scrambled planted triples it was never worse than pairs, and better on 108/600.
- **Pairs hidden by Peiffer moves (most important).** After 1–4 random Peiffer moves of planted pairs, the alternating pair fixpoint misses them in **114/300** cases. **N*_P is not invariant under reordering the certificate**, so a search that reorders factors can still hide a cancelling pair. A complete test amounts to minimising the factor count (an area problem), so N*_P stays an upper bound. Optional extension: close the pair test under one Peiffer move, cost O(N³ℓ).

## Extra question (Lead) — re-run loop erasure in the fixpoint: YES (witness)
F = [Y, a⁵, f, a⁵, (AA)⁵, X, f′, Z], with f′ = (M⁻¹ f M)⁻¹ and M = a⁵(AA)⁵X. Loop erasure keeps 8. PR #9 deletes the one pair and stops at 6, since the rescan finds no pair. A second loop erasure removes the now contiguous trivial triple [a⁵, a⁵, (AA)⁵], giving 3, with w unchanged. (Random planted pairs never showed this: 0/2,300.)

## Claim 2d — cheap computation: VALIDATED
Compute all g_k once: O(N·ℓ), each freely reduced. Hash the g_k and find pairs by looking up g_k⁻¹. After deleting (i, j): **g_k ← g_i⁻¹ g_k g_i for i < k < j; all others unchanged** (2,000/2,000 random deletions matched a full recompute). Cost per deletion O((j−i)·ℓ), against O(N²ℓ) for PR #9's rescan. For N ≲ 60 the rescan is fine. Use the hash version if N grows.

## Claim 3 — Dehn caution: VALIDATED (with corrected statement)
Suppose B(2,5) is finite of order K. Any K+1 consecutive prefixes of a word contain two equal ones, so every trivial w with |w| > K contains a trivial subword v with 1 ≤ |v| ≤ K. Then w = u v u′ = (u u′)·(u′⁻¹ v u′), so area(w) ≤ area(u u′) + area(v), with |u u′| < |w|. Iterating gives area(w) ≤ |w|·A(K), where A(K) = max area over the **finitely many** trivial words of length ≤ K. Each of those has a finite certificate, because it lies in ⟨⟨u⁵⟩⟩. So A(K) is finite even though the presentation {u⁵} is infinite, and the Dehn function over {u⁵} is linear. Contrapositive: a family *proved* to have super-linear (e.g. quadratic) **minimal** area over {u⁵} proves B(2,5) infinite. The converse fails (infinite groups can have linear Dehn functions, e.g. hyperbolic ones). The constant A(K) depends on the group, not only on its order. The owner's text in [[project-challenge-gen]] § Cautions on D is correct. Suggested precision: "over the infinite presentation {u⁵}; the pigeonhole argument does not need the presentation to be finite; the converse is false".

## Verdict
| Claim | Status |
|---|---|
| 1 pair deletion sound | validated (proof) |
| 1 T-001 case is an instance | rejected (erasure-order artifact; reproduced) |
| 2a test correct, element equality covers rotations/conjugators | validated (proof + 28,685 checks) |
| 2b order independence | rejected (order matters, rare: 1/2,300 suboptimal) |
| 2c pairs suffice | rejected in general (proper-power tuples; Peiffer-hidden pairs); practical frequency unknown |
| extra: loop erasure in fixpoint | needed (witness) |
| 2d incremental g update | validated |
| 3 Dehn argument | validated, wording refined |

## Sign-off review — PR #9 @ 728b350 (2026-10-14)
Reviewed `hardness/minimise.py` (`_prefix_coordinates`, `peiffer_reduce`, `reduce_certificate`) and `t003/padding.py` against S1, S2, S4 and S5 (S3 deferred by the owner; TODO present).
- **Math:** the g-form pair test (g_j = g_i⁻¹), the order (smallest i with a partner, its smallest j), the incremental update g_k ← g_i⁻¹ g_k g_i for i < k < j, and the loop erasure ↔ pair fixpoint all match the spec and the proofs above. Deleting gs[j] before gs[i] is correct.
- **Tests:** `test_peiffer.py` and `test_hardness.py` give 28 passed (Python 3.12, from a `git archive` snapshot of 728b350). They include the S1 witness (8 → 6 → 3), T-001 case 132 (stays 9), and the S3 triple as a documented limit (stays 5).
- **Independent fuzz (mine):** 1,000 inputs (planted pairs; pairs and proper-power triples scrambled by Peiffer moves) through the 728b350 code. w changed 0, N grew 0, pair left at the end 0, loop-erasable block left 0. The pair order differed from my reference 0 times, and the result was never worse than my reference fixpoint.
- **Non-blocking:** `median_pairs_removed = (F_star − F_star_P)//2` mislabels removals once loop erasure inside the fixpoint can drop an odd number of factors (e.g. a contiguous triple). Rename it to factors removed, or report the raw difference.
- **Verdict:** sign-off **yes** for the math.
