---
title: "A Catalogue of Complete Group Presentations"
authors: Philippe Le Chenadec
year: 1986
venue: "Journal of Symbolic Computation 2 (1986) 363–381"
url: ""
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 3
citation_count_date: 2026-06-11
key_concepts:
  - "[[Concepts/complete-rewriting-systems]]"
extends:
  - "[[knuth-bendix-1970]]"
contradicts: []
replicates: []
cites:
  - "[[knuth-bendix-1970]]"
  - "[[todd-coxeter-1936]]"
  - "[[gilman-1979]]"
cited_by:
  - "[[hermiller-shapiro-1999]]"
  - "[[epstein-holt-rees-1991]]"
quality_notes: "Low citation count (3 per ACM/Semantic Scholar) likely reflects pre-digital era publication. Paper is a concrete empirical catalogue supplementing the 1986 monograph Le Chenadec (1986) 'Canonical forms in finitely presented algebras.' Several results (termination of Dyck groups with even-order generators) remain open conjectures rather than theorems."
author: ethan-k
tags:
  - agent/research
  - user/ethan-k
  - domain/group-theory
  - topic/complete-rewriting-systems
  - topic/group-presentations
  - topic/knuth-bendix
  - topic/confluence
  - topic/word-problem
  - topic/normal-forms
  - topic/rewriting-systems
  - topic/cayley-graphs
  - paper
  - status/draft
---

# A Catalogue of Complete Group Presentations

> **Translation note**: vault language is English. Source paper is in English; no translation needed.

## Abstract

A complete group presentation consists of a set of generators and a set of replacement rules generating a well-founded and confluent relation on words, thereby solving the word problem for this presentation. Complete presentations for surface, Coxeter, Dyck and symmetric groups are discussed. These complete presentations possess interesting combinatorial properties and provide uniform algorithms for the word problem.

## TL;DR

Le Chenadec explicitly constructs complete (well-founded and confluent) rewriting systems for four major classes of groups — surface groups, Coxeter groups, Dyck groups, and symmetric groups — using a Lisp implementation of the Knuth-Bendix procedure, demonstrating that completion is applicable to parametrised infinite families. The paper provides both the rule sets and efficient reduction algorithms (linear-time, no backtracking for surface and Coxeter groups), while honestly noting that termination for Dyck groups with even-order generators remains an open conjecture.

## Problem

Can the Knuth-Bendix completion procedure produce complete (i.e., well-founded and confluent) rewriting systems for well-known, classically-studied group families, and what do those complete presentations look like explicitly? The paper asks whether completion can handle parametrised families (not just isolated finite groups), and whether the resulting normal-form algorithms are practically efficient.

## Approach

Starting from standard finite group presentations drawn from Coxeter & Moser (1980), the author applies a Lisp implementation of the Knuth-Bendix procedure (Le Chenadec 1983) with a chosen lexicographic or weight reduction order. For each family:

1. **Surface groups (§2)**: orientable (torus with $p$ holes, $T_p$) and non-orientable. The completion leads to systems with $4p$ rules (orientable) or $6p$ rules (non-orientable) of uniform rule-length $2p$. Connection to Dehn's algorithm in small cancellation theory is made explicit (§1 and §2.1).

2. **Coxeter groups (§3)**: shown (Theorem 6) that for a Coxeter matrix $M$ with no entry equal to 2 and a linear order $>$, the completion procedure generates the rule set $R_I \cup T_I$ in closed parametric form. Infinite rule sets arise when entries include commuting generator pairs. The paper demonstrates that infinite complete presentations can be described by a single parametrised rule family.

3. **Dyck groups (§4)**: polyhedral and general Dyck groups (rotation subgroups of Coxeter groups). Complete systems given; for generators with odd order, termination proved; for even order, termination is conjectured but not proved due to length-increasing rules.

4. **Symmetric groups (§5)**: two presentations — adjacent transpositions (yielding $n^2 - 2n + 2$ rules, insertion sort) and all transpositions ($O(n^4)$ rules, max/min sort).

Throughout, Cayley-graph geometry is used to describe and justify the complete presentations visually.

## Key result

**Proposition 2** (§2.1): Let $T_p$ be a complete torus presentation as defined. Then there exists a linear-time algorithm which does not involve backtracking and which computes the normal form of a word $M$ with no more than $|M|/2p$ reductions.

**Theorem 6** (§3.1): Let $M$ be a Coxeter matrix on the set $I$ which possesses a linear order $>$. If $m_{ij} \neq 2$, $i, j \in I$, the completion procedure generates the set of rules $R_I \cup T_I$, where $T_I$ consists of all rules of the form $\alpha_1 \ldots \alpha_k l(\alpha_k) \to s(\alpha_1)\alpha_1 \ldots \alpha_k$ subject to the conditions on consecutive components $\alpha_p$.

**Rule-count results**: surface groups $T_p$: $4p$ rules; non-orientable surface groups: $6p$ rules; symmetric group $S_n$ (adjacent transpositions): $n^2 - 2n + 2$ rules; $S_n$ (all transpositions): $O(n^4)$ rules, well below the theoretical upper bound of $2|G| \times |G|$ stated in §1.

**Failures**: the paper explicitly records cases where completion failed — alternating groups (combinatorial explosion), the isolated Coxeter groups $E_6$, $E_7$, $E_8$, and the family $D_n$ ($n \geq 4$). For Dyck groups with even-order generators, termination is conjectured but unproved.

## Assumptions

- Groups are finitely presented (given by generators and relations).
- A linear reduction order can be chosen such that the defining relations are strictly decreasing (required for the completion procedure to start).
- For Coxeter groups (Theorem 6): no entry in the Coxeter matrix equals 2 (i.e., no commuting generators). Failures with commuting generators are noted.
- For Dyck groups with even-order generators: termination is assumed (conjectured) but not formally established.
- Practical computations were run on a Honeywell DPS68; some required several hours of CPU time (§1).

## Limitations / scope

- The paper is a catalogue, not a decidability result: it provides evidence that completion works for these specific families, not a general theorem about when completion terminates.
- Termination for Dyck groups with even-order generators is unproved; the paper states "we conjecture that the reductions are well-founded" (§4.1).
- Completion failed for alternating groups, $E_6$, $E_7$, $E_8$, $D_n$ ($n \geq 4$), and some Coxeter groups with commuting generator pairs.
- Efficiency analysis (Proposition 2) is limited to torus groups; no analogous bounds are proved for Coxeter or Dyck families.
- Infinite complete presentations (e.g., $S_\infty = \bigcup_{n} S_n$) are described but their convergence properties are only partially analysed.
- The work predates the KBMAG system and automatic-groups theory; no connection to fellow-traveler properties or rational normal-form languages is made explicitly.

## Replication evidence

Partial. The specific rule sets presented are deterministic outputs of the Knuth-Bendix procedure given specified orders; a reader can re-derive them by running any correct KB implementation with the same order. No independent replication study is cited. The paper itself validates results by checking confluence (critical-pair resolution) and termination proofs where available. The termination proof for non-orientable surface groups (§2.2) and the Proposition 2 proof (§2.1) are rigorous; Dyck-group termination with even-order generators remains unverified.

## Why this paper matters

This 1986 paper is an early existence proof that the Knuth-Bendix completion procedure is not merely a heuristic for small isolated groups but can systematically handle infinite parametrised families — providing, for the first time, explicit complete rewriting systems for surface groups, all Coxeter groups satisfying a mild condition, polyhedral and Dyck groups, and both standard presentations of symmetric groups. This repositioned KB completion from a case-by-case tool to a principled method for entire families.

The paper also makes the Cayley-graph connection concrete: the complete presentations for surface and Dyck groups have direct geometric descriptions on $(4p)$- and $(4p+2)$-gons, providing intuition that later influenced the automatic-groups program (Epstein et al. 1992 used Cayley-graph regularity as a foundational idea). The symmetric-group result unexpectedly connects complete presentations to sorting algorithms (insertion sort from adjacent transpositions, max-sort from all transpositions), a cross-domain observation cited in later work on string rewriting and combinatorics.

The explicit catalogue of failures is equally valuable: the inability to complete $E_6$, $E_7$, $E_8$ and the alternating groups documented real limitations of KB completion that motivated subsequent work on hybrid methods and coset enumeration comparisons.

## Quotes

1. > "The completion procedure must be thought of as a compilation process, in contrast to the coset enumeration method of Todd & Coxeter." — §1

2. > "The main advantage of completion over enumeration is its ability to handle parametrised classes, thereby providing a solution to the word problem for entire classes of groups." — §6

## Open questions surfaced

1. **Dyck groups with even-order generators**: is termination of the completion procedure provable? The paper conjectures yes but provides no proof. A termination order accommodating length-increasing rules (such as $A^{-2}BC^{-1}DA \to A^3D^{-1}C^2B^{-1}$ in $(6,5,5,5)$) is needed.

2. **Alternating groups**: does a complete presentation exist for $A_n$ ($n \geq 4$)? Completion failed due to combinatorial explosion; it is unclear whether this reflects a fundamental obstruction or just practical limits of the 1986 implementation.

3. **Exceptional Coxeter groups** $E_6$, $E_7$, $E_8$ and family $D_n$: can complete presentations be found for these? A Todd-Coxeter run produced a full coset table for $E_6$ in under 3 minutes (Newman, private communication to Le Chenadec), but completion was not achievable. Is there a theoretical reason?

4. **Complexity for Coxeter/Dyck normal forms**: Proposition 2 gives a linear-time bound for torus groups. Are analogous linear-time bounds provable for the Coxeter $T_I$-rule reduction algorithm described in §3.3?

5. **Infinite rule sets and decision procedures**: for the infinite parametrised rule families (e.g., Coxeter $G_3$, $G_5$), does the existence of a parametrised complete presentation suffice for a decidable (even efficient) word problem algorithm, given that the rule set is infinite?

## Related material in vault

- Extends: [[Research/Group theory/Word Problem/knuth-bendix-1970|knuth-bendix-1970]]
- Concepts introduced/used: (no existing concept hubs — candidates: `complete-rewriting-systems`, `group-presentations`; see report)
- Cites: [[Research/Group theory/Word Problem/knuth-bendix-1970|knuth-bendix-1970]], [[Research/Group theory/Word Problem/dershowitz-jouannaud-1990|dershowitz-jouannaud-1990]], [[Research/Group theory/Word Problem/todd-coxeter-1936|todd-coxeter-1936]]
- Parent overview: [[Research/Group theory/Word Problem/word-problem-overview|word-problem-overview]]
- MOC: [[Research/Group theory/_MOCs/_moc-knuth-bendix|_moc-knuth-bendix]], [[Research/Group theory/_MOCs/_moc-word-problem|_moc-word-problem]]
- Author: [[People/ethan-k|ethan-k]]
