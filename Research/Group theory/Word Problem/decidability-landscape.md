---
title: "Word Problem — Decidability Landscape"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/decidability
  - topic/finitely-presented-groups
  - status/validated
---

# Word Problem — Decidability Landscape

## The word problem

**Definition.** Let G = ⟨X | R⟩ be a finitely presented group. The **word problem** for G is the decision problem:

> **Input:** A word w in the free monoid (X ∪ X⁻¹)*.
> **Output:** Does w represent the identity element of G?

Equivalently: is w in the normal closure of R in the free group F(X)?

**Why it is hard.** Two words in the free monoid represent the same element of G iff one can be derived from the other by a finite sequence of applications of the relators in R and their inverses. This is in general an unbounded process — there is no a priori bound on the length of derivations.

## Decidability results

### Free groups

**Theorem (elementary).** The word problem in a free group F(X) is decidable in linear time.

**Proof sketch.** A word w ∈ F(X) equals the identity iff w reduces to the empty word by iterated cancellation of xx⁻¹ pairs. Freely reduced words are canonical forms. □

**Algorithm:** Scan left-to-right; cancel adjacent inverse pairs. O(|w|) time.

### Abelian groups

**Theorem.** The word problem in any finitely generated abelian group is decidable in polynomial time.

**Proof sketch.** A finitely generated abelian group G has presentation ⟨X | R ∪ {xᵢxⱼxᵢ⁻¹xⱼ⁻¹ for all i,j}⟩. Word equality reduces to a linear system over ℤ, solvable by Smith normal form. □

**Algorithm:** Compute Smith normal form of the relation matrix. Polynomial in |X| and |R|.

### 1-relator groups

**Theorem (Magnus, 1932).** Every group with a single defining relator has a decidable word problem.

**Method:** Magnus's Freiheitssatz + induction on the length of the relator. No effective complexity bound known for the general case.

### Hyperbolic groups

**Theorem (Dehn, 1910 for surface groups; Gromov, 1987 in general).** Every hyperbolic group has a decidable word problem, solvable in linear time by Dehn's algorithm.

**Definition.** A finitely presented group G = ⟨X | R⟩ is **δ-hyperbolic** if every geodesic triangle in the Cayley graph is δ-slim (every side lies within a δ-neighborhood of the other two).

**Dehn's algorithm:** A word w equals identity iff it can be shortened by a relator subword of length > |r|/2 (where r is a relator). Linear time: |w| reductions suffice.

### Automatic groups

**Theorem (Cannon, Thurston, Epstein, Holt, Paterson, Levy, 1992).** Every automatic group has a decidable word problem, solvable in quadratic time.

**Definition.** G is **automatic** if it has a regular language of normal forms closed under multiplication by generators (with respect to a finite-state automaton synchronizing pairs of normal forms differing by one generator step).

**Algorithm:** Reduce w to normal form using the multiplier automaton; compare normal forms. O(|w|²).

**Scope:** All hyperbolic groups are automatic. Many important groups are automatic but not hyperbolic (e.g., mapping class groups of surfaces, SL(3,ℤ) — wait, SL(3,ℤ) is NOT automatic; this is a subtle class).

### General finitely presented groups

**Theorem (Novikov 1955; Boone 1957, independently).** There exist finitely presented groups with **undecidable** word problem.

The proofs encode Turing machine computation in the relators. The resulting group has a presentation with ~50 generators and relators; words equal the identity iff the corresponding Turing machine halts.

**Corollary.** The word problem is not decidable for general finitely presented groups.

## Decidability table

| Group family | Word problem | Complexity | Reference |
|---|---|---|---|
| Free groups | Decidable | O(n) | Elementary |
| Finitely generated abelian groups | Decidable | Polynomial | Smith normal form |
| 1-relator groups | Decidable | No known general bound | Magnus (1932) |
| Hyperbolic groups | Decidable | O(n) | Dehn/Gromov (1987) |
| Automatic groups | Decidable | O(n²) | Epstein et al. (1992) |
| General FPGs | **Undecidable** | — | Novikov (1955), Boone (1957) |

## The gap: 2-relator groups

**Open problem (Merzlyakov, Kourovka 9.29, 1984):** Do 2-relator groups with undecidable word problem exist?

Magnus's theorem covers 1-relator groups. General FPGs are undecidable. Whether the threshold is 1 or 2 relators is unknown. See [[Research/Group theory/Open problems/Free groups/2-relator-word-problem-9.29-merzlyakov]].

## Connection to Knuth-Bendix completion

Knuth-Bendix completion, when it terminates with a confluent rewriting system, gives a decision procedure for the word problem. Every word has a unique normal form under the confluent system; two words are equal iff their normal forms are equal.

However: KB termination is sufficient but NOT necessary for decidability. A group may have a decidable word problem (e.g., hyperbolic groups via Dehn's algorithm) even though no finite complete rewriting system exists. Conversely, KB termination proves the group is finite (for groups where the ordering is weight-length compatible and the group has finite exponent). See `Tools/KBMAG/` for practical KB completion.
