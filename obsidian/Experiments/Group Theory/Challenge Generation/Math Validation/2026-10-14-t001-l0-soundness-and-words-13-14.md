---
title: "T-001 L0 soundness and words 13/14 — verdict"
status: proven
domain: group-theory
project: challenge-gen
claim: "(1) L0 with literal-5th-power relators and exact re-expansion proves w trivial in free B(2,5); (2) words idx 13, 14 of ds-b25-trivial-2-5reduced-aut8-20261007 are trivial in free B(2,5), and are not fixed points of the 2.5 reducer"
claimant: Experimenter
verification_method: "hand proof from the definition B(2,5)=F/⟨⟨x⁵⟩⟩; explicit step-checked rewriting certificate (own script, independent of tcgraph and kbprog)"
tools_used: [python3 (own scripts, scratch/t001_trace.py, t001_search.py), "tcgraph reducer (claim producer, not used)"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, project/challenge-gen, status/proven, proof]
---

# Verification — T-001 L0 soundness; words 13, 14
Triage: [[2026-10-14-t001-l0-soundness-and-words-13-14-triage]]. Source: [[hardness-baselines-results]]. Group throughout: **free B(2,5) = F(a,b)/N**, N = normal closure of {x⁵ : x ∈ F(a,b)} (definition; no finite quotient used anywhere).

## Claim 1 — L0 soundness: PROVEN
Let r be a relator whose letters are literally u·u·u·u·u (a string) with u ∈ F. Then r =_F u⁵ ∈ N. For a conjugator c, c⁻¹rc ∈ N since N is normal; free reduction does not change the element of F. A product of such elements lies in N. If the independent re-expansion of the factor word equals w̄ **as a freely reduced word** (exact string equality, not abelianization), then w̄ =_F ∏ c_i⁻¹ r_i c_i ∈ N, so w̄ = 1 in B(2,5). ∎
Scope and limits:
- Pure proof from the definition, no circularity (the relators are 5th powers by inspection, not by being built from a presentation of B(2,5)).
- "Cyclically reduced" is not needed for soundness; it only makes "literal 5th power" well-defined as a test.
- Needs: (i) the table check really ran (each r_i is a string u⁵ — reported by Experimenter, table sha256 `9db81f16…` for L=2; **I did not re-run it**); (ii) the final comparison is full freely-reduced word equality. Abelianization and the table hash are bug checks only (necessary, not sufficient).
- It certifies triviality only. It says nothing about hardness or about shorter certificates.

## Claim 2 — words 13 and 14 are trivial in free B(2,5): PROVEN
**Lemma (2.5 rewriting is sound).** Let v be a word, m=|v|, V = vvv… , and u = V[0:L] with L ≤ 5m. Then u·V[L:5m] = v⁵ ∈ N, so u = (V[L:5m])⁻¹ in B(2,5). For L > 5m, u = v⁵·V[0:L−5m] = V[0:L−5m]. The new word is no longer than the old iff L ≥ 2.5m. Rotations and cyclic free cancellations are conjugations, which preserve triviality. ∎

**Certificates.** `scratch/t001_search.py` found, and `check_step` verified at string level (sub + complement == v⁵, new == inverse of complement), these traces (cyclic words, step = rotate, replace, cyclically reduce):

idx 13 (44 letters, exponent sums ≡ 0 mod 5 in a and b), 12 steps, lengths 44, 44, 43, 42, 41, 38, 30, 27, 26, 21, 13, 5, 0:
`AABABAbabaBBababABABAABABBABABaababAAbabaBAB`
0. BABAB=(BA)^{5/2} → ababa
1. aaa → AA
2. babAAbabAAbab=(babAA)^{13/5} → aaBABaaBABaa
3. aaa → AA
4. BABAABABAABAB=(BABAA)^{13/5} → aababaababaa
5. ababababa=(ab)^{9/2} → B
6. aaaa → A
7. aaa → AA
8. ABABAABABAABA=(ABABA)^{13/5} → ababaababaab
9. ababababa → B
10. ababababa → B
11. BBBBB → ε

idx 14: step 0 is the length-neutral move babab=(ba)^{5/2} → ABABA, which gives exactly the word of idx 13 after one more neutral move (BABAB → ababa); then the idx 13 steps 1–11. Total 13 steps. Full per-step words in `Agents/asetlearning/Validator/scratch/` reproduction: `python3 -I t001_search.py <data file> 13 14` (replay printout reproduced in the session; the two traces above are exhaustive for 13, and idx 14 = one extra neutral step).

This is an independent proof of triviality in **free** B(2,5), not relying on kbprog, tcgraph, or any finite quotient.

## Dataset claim "every word is a fixed point": DISPROVEN as stated
Both stored strings reduce to the empty word, so for them the claim is false in the sense "not reduced by the 2.5 reducer". Observation: with a strict length-shortening rule (p > 2.5 only) my script finds **no** applicable step on idx 13, 14, 0, 1; the first move needs the length-neutral p = 5/2 step. So the dataset-note vetting ("not shortened") and the harness result (ρ = 0) are both reproducible with different readings of "reducer": a reducer that allows neutral p = 2.5 moves (greedy then cyclic exhaustive, as Experimenter reports) empties them. Which reading the pin a0d5e92 vs 7e50fea implements was **not** checked by me (conjectured explanation). Consequence: the dataset's property_claimed needs rewording, and the positive control H4 is falsified for these two words under the harness reducer. The two words stay valid trivial words (they are trivial); they are not "2.5-reduced" in the dataset's sense.

## Verdict
- Claim 1 (L0 soundness): **#status/proven** (conditional on implementation checks listed above, which I did not re-run).
- Claim 2 (idx 13, 14 trivial in free B(2,5)): **#status/proven**, explicit certificate.
- Dataset property "every word is a fixed point": **#status/disproven** for idx 13, 14.

## Notes for downstream agents
- Remove or correct the fixed-point claim in the dataset note; consider filtering words that reduce to ε (and check the 818 others are also not reducible by neutral moves if the claim is to be kept).
- I did not check the other 818 words, nor kbprog's proof for them.
