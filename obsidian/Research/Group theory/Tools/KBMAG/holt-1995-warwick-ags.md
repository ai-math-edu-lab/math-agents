---
title: "The Warwick Automatic Groups Software"
authors: Derek F. Holt
year: 1995
venue: "Geometric and Computational Perspectives on Infinite Groups, DIMACS Series in Discrete Mathematics and Theoretical Computer Science, vol. 25, pp. 69–82"
url: "https://arxiv.org/abs/math/9507202"
language: en
domain: group-theory
status: draft
methodology_type: empirical
citation_count: 21
citation_count_date: 2026-06-11
key_concepts: []
extends:
  - "[[epstein-et-al-1992-word-processing]]"
contradicts: []
replicates: []
cites:
  - "[[epstein-et-al-1992-word-processing]]"
  - "[[epstein-holt-rees-1991]]"
cited_by:
  - "[[epstein-sanders-2000]]"
quality_notes: "Foundational software-description paper for the Warwick Automata package, the direct predecessor of KBMAG. 21 citations (Semantic Scholar, 2026-06-11)."
author: ethan-k
tags:
  - agent/research
  - user/ethan-k
  - domain/group-theory
  - topic/automatic-groups
  - topic/knuth-bendix
  - topic/kbmag
  - topic/finite-state-automata
  - topic/word-acceptor
  - topic/computational-group-theory
  - topic/software-tools
  - topic/rewriting-systems
  - paper
  - status/draft
---

# The Warwick Automatic Groups Software

## Abstract

This paper provides a description of the algorithms employed by the Warwick Automata package for calculating the finite state automata associated with a short-lex automatic group. The aim is to provide an overview of the whole process, rather than concentrating on technical details, which have already been published elsewhere. A number of related programs are also described.

## TL;DR

Holt describes the complete pipeline of the Warwick Automata package: starting from a finite group presentation with an ordered generating set, the software attempts to compute a short-lex automatic structure (word-acceptor + multiplier automata) by interleaving Knuth-Bendix completion to seed word-difference automata with an iterative FSA-based verification loop. This is the primary algorithmic reference for the package that was later distributed and evolved into KBMAG.

## Problem

Given a finitely presented group G with an ordered monoid-generating set A, does G have a short-lex automatic structure, and if so, how can it be computed? The paper asks: how do you go from a group presentation to explicit verified finite-state automata (word-acceptor W and multipliers M_x) constituting the automatic structure — and what is the practical scope of such a computation?

## Approach

The Warwick Automata package implements a 6-step iterative procedure (Section 3):

1. **Step 1 — Build D1.** Run the Knuth-Bendix procedure on the group presentation to generate reduction rules. At intervals, construct a candidate word-difference automaton D1 (states = word-differences derived from current rules). Halt KB and move on when D1 appears stable (several successive identical candidates).

2. **Step 2 — Build word-acceptor W.** Using D1 and the short-lex order automaton GT, compute W = (A\* · E(D1 ∧ GT) · A\*)'. W accepts w ∈ A\* iff w has no reducible substring detectable via D1.

3. **Step 3 — Build D2.** Construct the equality word-difference automaton WD$, seeding its state set from D1's states plus their inverses and generators. D2 is meant to accept all word-differences between accepted paths (property P2).

4. **Step 4 — Build multipliers M_x.** For each generator x, construct M_x with state space S(W) × S(W) × S(D2). If W turns out to accept two distinct words for the same element, restart from Step 1.

5. **Step 5 — Check D2 correctness.** Verify W ∧ E(M_x)' has empty language for all x. If not, find missing word-differences, augment D2, repeat from Step 3.

6. **Step 6 — Axiom check.** Verify that the composite multiplier M_r equals M$ for each defining relator r. This step uses repeated determinization and minimization; it is typically the most time-consuming.

Throughout, all logical operations (intersection, complement, existential projection, concatenation, minimization) are performed directly on finite-state automata. Knuth-Bendix is used only to seed Step 1; it need not terminate. The key theoretical underpinning is the fellow-traveler property: for a short-lex automatic group, the word-difference set WD is finite, so the loop terminates after finitely many iterations.

## Key result

**Completeness (Section 3):** If G is short-lex automatic with respect to the given ordered generating set A, the algorithm will, in principle, terminate and output the correct automatic structure (word-acceptor and multipliers), given sufficient time and memory.

**Practical scope (Section 4):** Several worked examples with timing and automaton sizes:
- Gunn's hyperbolic tessellation group (6 generators): word-acceptor 48 states, multipliers 145–175 states; 545 seconds on SGI Iris XS24 (32 MB).
- Thurston's (2,2,2,2,2,2)-orbifold group (12 generators): word-acceptor 131 states, multipliers 132–232 states; 930 seconds.
- Fibonacci group F(2,8): word-acceptor 212 states, multipliers 1861 states; ~9 hours on a 128 MB Solbourne machine.
- F(2,9) (Section 3, added in revised draft): word-acceptor 3251 states, multipliers ~25000 states (pre-minimization: ~860000); ~12 hours, ~130 MB on SPARCstation 20.
- Picard group SL(2,Z[i]): word-acceptor 403 states, multipliers 403–3718 states; required 12 iterations of the D2-correction loop.
- Seifert-Weber fundamental group: word-acceptor 1429 states, multipliers ~14000 states.

**Growth series (Section 5):** The growth function fG,A(t) = Σ w(i)t^i is computed from the word-acceptor as a rational function. Example: growth function for the example G1 is (1 + 3t + 3t² + t³)/(1 − 9t + 9t² − t³).

**Geodesic word-acceptor (Section 5):** Algorithm to compute the geodesic word-acceptor from a short-lex structure, exploiting Papasoglu's characterization that groups with the geodesic fellow-traveler property are hyperbolic.

## Assumptions

- Group G is finitely presented; generators A are closed under inversion.
- The algorithm is specialized to **short-lex** automatic structures. It provides no information about groups with non-short-lex automatic structures or non-automatic groups (Section 1: "I am not aware of any existing software which can do the same thing for automatic structures which are not short-lex").
- The ordering of the generating set matters: short-lex automaticity depends on both the choice and ordering of A.
- Sufficient memory: exponential blowup in automaton states is possible (determinization of 2-variable automata can square state counts), making large examples memory-bound.

## Limitations / scope

- **No termination guarantee for non-short-lex-automatic groups.** If G has no short-lex automatic structure with respect to A, the procedure may diverge without signalling failure.
- **Step 1 heuristics are incomplete.** There is no fully satisfactory criterion for when to stop KB and move to Step 2; the user may need to intervene interactively if D1 never stabilizes (Section 3).
- **Restart cost.** On failure at Steps 3 or 6, the procedure restarts from Step 1 completely, discarding partial work (Section 3: "we begin again completely, because it seems too difficult and space-consuming to attempt to restart from where we left off").
- **No braid groups ≥ 4.** The paper notes (Section 1) that braid groups B_n for n ≥ 4 are automatic but "probably have no short-lex automatic structures at all," so the package cannot handle them.
- **Short-lex only.** The package cannot verify automaticity for non-short-lex word orders (e.g., geodesic-based orderings) beyond the experimental geodesic algorithm in Section 5.

## Replication evidence

Partial. The algorithms and theoretical correctness proofs are given in full in the companion paper Epstein-Holt-Rees 1991 (reference [2]). The examples in Section 4 reproduce and extend those from that paper. The Warwick Automata package was distributed via anonymous FTP and subsequently superseded by KBMAG, which reimplements and extends these algorithms; the KBMAG package's correctness on standard examples constitutes indirect replication.

## Why this paper matters

This paper is the primary algorithmic description of the software that directly preceded and evolved into KBMAG — the standard tool for automatic-group computation in the computational group theory community. Whereas the companion paper (Epstein-Holt-Rees 1991) gave full proofs and technical details, this paper gives a conceptual overview of the *complete pipeline*, framing the algorithm in terms of logical operations on finite-state automata rather than string rewriting per se. This framing is both pedagogically clearer and more accurate to the implementation.

The paper's significance is primarily practical: it documents the algorithms in working software, demonstrates that real-world geometric group theory problems (hyperbolic manifold groups, orbifold groups, Fibonacci groups, linear groups over rings) are tractable with this approach, and establishes the short-lex automatic structure as a concrete computable object rather than a purely theoretical notion. The verification at Step 6 (axiom-checking via multiplier composition) is particularly important: Holt explicitly argues that this self-verification step makes the output more reliable than typical computational algebra output. This design philosophy carries through into KBMAG.

The paper also surfaced important open problems that shaped subsequent work: the need for better Step 1 heuristics (how to know when KB has generated enough rules), and the challenge of groups like F(2,n) for odd n where automaticity is unknown.

## Quotes

1. > "I believe that the fact that these programs effectively verify the correctness of the results that they produce renders the results intrinsically more reliable than those produced by many computer programs." — Section 1

2. > "The most important problem now is to try to find improved methods of carrying out Step 1." — Section 3

## Open questions surfaced

- **Better Step 1 termination criterion.** The paper identifies no satisfactory stopping rule for the KB-to-D1 phase; heuristics based on D1 stability can fail when superfluous states prevent convergence. What theoretically-grounded criterion can replace the stability heuristic?
- **Alternative non-KB approaches to Step 1.** Holt explicitly notes no non-KB approach to computing D1 has been found. Is there a direct construction of the word-difference automaton that bypasses KB entirely?
- **Automaticity of F(2,n), n odd.** F(2,9) was proved automatic by this software; n > 9 odd cases remain unknown at time of writing.
- **Non-short-lex automatic structures.** The package cannot handle groups that are automatic but have no short-lex structure (e.g., braid groups B_n, n ≥ 4). How would one extend the pipeline to non-short-lex orderings?
- **Restart efficiency.** The full-restart on Step 1 failure discards valid partial computations. Can incremental reuse of multiplier/automaton data reduce the cost of recovery loops?

## Related material in vault

- Extends: [[epstein-et-al-1992-word-processing]]
- Cites: [[epstein-et-al-1992-word-processing]]
- Parent overview (KBMAG tools): [[Research/Group theory/Tools/KBMAG/kbmag-tools-overview|kbmag-tools-overview]]
- GAP package (successor): [[Research/Group theory/Tools/GAP/package-kbmag|package-kbmag]]
- Domain tools overview: [[Research/Group theory/Tools/group-theory-tools-overview|group-theory-tools-overview]]
- Concept note (automatic groups): [[Research/Group theory/Word Problem/techniques/automatic-groups|automatic-groups]]
- Author: [[People/ethan-k|ethan-k]]
