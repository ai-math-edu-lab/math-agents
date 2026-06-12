---
title: "Presentations of Groups and Monoids"
authors: Robert H. Gilman
year: 1979
venue: "Journal of Algebra 57 (1979), 544–554"
url: ""
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 92
citation_count_date: 2026-06-11
key_concepts:
  - "[[Concepts/complete-rewriting-systems]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[knuth-bendix-1970]]"
cited_by:
  - "[[le-chenadec-1986]]"
  - "[[epstein-holt-rees-1991]]"
author: ethan-k
tags:
  - agent/research
  - user/ethan-k
  - domain/group-theory
  - topic/word-problem
  - topic/rewriting-systems
  - topic/knuth-bendix
  - topic/finitely-presented-groups
  - topic/complete-rewriting-systems
  - topic/confluence
  - paper
  - status/draft
---

# Presentations of Groups and Monoids

## Abstract

There is no algorithm to tell from a finite presentation, α, whether or not the group or monoid, G, presented by α is finite. We exhibit an algorithm, A, which gives the order or order of growth, for finite or infinite G respectively, when α is in a certain class, 𝒱, of finite presentations. When applied to an arbitrary finite α, A gives an upper bound for these quantities. Further we give a procedure, P, which, when it terminates, changes an arbitrary finite presentation, α, for G into a presentation γ ∈ 𝒱 for G.

Using P and A we may attempt to find the order or order of growth of the group or monoid, G, from an arbitrary finite presentation α. We succeed (that is, P terminates) if G is finite; but of course P does not always terminate. In fact if γ ∈ 𝒱 presents G, then G has a solvable word problem. We give some examples in section 6. In section 4 we see how our methods apply to abelian monoids. In particular we show that every finitely generated abelian monoid is presented by some γ ∈ 𝒱. P is defined in section 3 and A in section 5.

## TL;DR

Gilman (1979) introduces a completion procedure (Procedure P) that converts an arbitrary finite monoid or group presentation into a complete rewriting system in class 𝒱 — terminating exactly when the presented group or monoid is finite, or equivalently when the congruence ideal I(⟨α⟩) is finitely generated. The companion Algorithm A then reads off the order or order of growth directly from a finite graph constructed over the ideal's generators. This is an independent, contemporaneous development of essentially what became known as Knuth-Bendix completion, stated cleanly in the language of string rewriting over free monoids.

## Problem

Given a finite presentation α for a group or monoid G, the order of G is generally undecidable. The paper asks: for which presentations can we algorithmically determine whether G is finite and, if so, compute |G|? And can we algorithmically transform an arbitrary presentation into one from this privileged class?

## Approach

The paper works over finitely generated free monoids F with a recursive well-ordering < (compatible with multiplication on both sides — a term ordering). For a set α ⊆ F × F, Gilman defines the ideal I(α) of reducible words and the Schreier system S(α) = F − I(α) of irreducible normal forms. A presentation is in class 𝒱 (the class of "complete" presentations, in modern terminology) when I(α) = I(⟨α⟩), i.e., the generators of α already capture all reductions derivable from the congruence.

**Procedure P** (§3): Starting from a normalized α, repeatedly inspect ordered pairs of rules and check the two overlap conditions (Lemma 1):

- **Condition (2)** (inclusion overlap): for each pair ((a,b),(c,d)) and solutions x,y to b = xdy, the words a and xcy must have a common α-descendant.
- **Condition (3)** (overlap of b and d): for solutions x,y to bx = yd (where b and d overlap), ax and yc must have a common α-descendant.

Whenever a condition fails, the required common descendant is computed and added as a new rule. P terminates iff I(⟨α⟩) is finitely generated (Proposition 2); it always terminates when G is finite.

**Algorithm A** (§5): Given a presentation γ ∈ 𝒱, Algorithm A constructs a directed labeled graph Γ(B) over the minimum generators B of I(γ), where vertices are proper initial segments of elements of B. Paths from the root vertex enumerate elements of L = F − I exactly. Algorithm A then reads off the order or growth class of G from the cycle structure of Γ:

- No directed cycles → G is finite, |G| = number of paths (Proposition 3(a)).
- Some vertex on two directed cycles → exponential growth: r < p^n < γ(n) < q^n (Proposition 3(b)).
- Each vertex on at most one cycle, max disjoint cycles on any path = k → polynomial growth of degree k: r·n^k ≤ γ(n) ≤ s·n^k (Proposition 3(c)).

For abelian monoids (§4), Dickson's lemma guarantees that every ideal of a free abelian monoid is finitely generated, so Procedure P always terminates, and every finitely generated abelian monoid has a presentation in 𝒱 (Corollary 1).

## Key result

**Proposition 1** (§2). Let p be a congruence on F and α ⊆ p:
- (a) If F/p is finite, then I(p) is finitely generated;
- (b) If I(α) = I(p), then p = ⟨α⟩;
- (c) If α ∈ 𝒱, then F/⟨α⟩ has a solvable word problem.

**Lemma 1** (§3). Let γ ⊆ F × F be normalized. Then I(γ) = I(⟨γ⟩) if and only if conditions (2) and (3) hold for each ordered pair of elements of γ. (This is the critical-pair / overlap condition — the confluence criterion.)

**Proposition 2** (§3). Let α ∈ F × F be a finite presentation of G = F/⟨α⟩. Procedure P applied to α terminates if and only if I(⟨α⟩) is finitely generated (and in particular if G is finite). When Procedure P terminates, it yields a presentation γ ∈ 𝒱 of G.

**Proposition 3** (§5). Let Γ be constructed by Algorithm A.
- (a) If Γ has no directed cycles, then L = F − I is finite of order equal to the number of paths in Γ from vertex 1.
- (b) If some vertex of Γ lies on two directed cycles, then γ(n) — the number of words in L of length at most n — satisfies $p^n < \gamma(n) < q^n$ for two real numbers 1 < p < q.
- (c) If each vertex of Γ lies on at most one directed cycle and k is the maximum number of pairwise disjoint cycles occurring on any path from vertex 1, then $r \cdot n^k \leq \gamma(n) \leq s \cdot n^k$ for two real numbers 0 < r < s.

**Corollary 1** (§4). Every finitely generated abelian monoid has a finite presentation (recovers a classical result via the new framework).

**Corollary 2** (§4). Every finitely presented abelian semigroup has a solvable word problem.

## Assumptions

- Groups and monoids are finitely presented (given as a finite α ⊆ F × F).
- F is a finitely generated free monoid (or free abelian monoid in §4).
- A recursive well-ordering < of F compatible with multiplication on both sides (a term ordering/reduction ordering) is fixed throughout.
- The word problem results (solvability) depend on α being finite or at least recursively enumerable with T(α) recursive.

## Limitations / scope

- Procedure P is a semi-decision procedure: it terminates for finite groups and finitely generated I(⟨α⟩), but may diverge otherwise (Example 3 shows a group where P does not terminate even though the Schreier system L is regular — regularity of L is necessary but not sufficient for P's termination).
- The convergence of P and the output γ depend on the choice of well-ordering < and on the sequence in which generators are listed: Example 3 shows that different orderings or generator mappings cause P to terminate or diverge on the same group.
- The graph Γ produced by Algorithm A need not be minimal: Example 4 shows Γ may properly cover the minimal automaton Γ(L) (5-vertex minimal automaton vs. 6-vertex Γ).
- The paper does not address infinite groups with solvable word problem by methods other than 𝒱-membership; it does not handle non-string-rewriting presentations.

## Replication evidence

Partial. The results on abelian monoids (Corollaries 1 and 2) recover known theorems (cited as [7, Theorem 72] and [2]). The connection between Procedure P and Knuth-Bendix completion was noted independently in the KB completion literature; Sims' KBMAG implementation (1980s–1990s) implements the same critical-pair logic. The graph-based growth classification (Proposition 3) is consistent with Milnor's growth conjecture [6], which the paper explicitly references. No independent numerical replication is reported in the paper itself.

## Why this paper matters

This paper is a clean, self-contained 1979 formulation of Knuth-Bendix completion for string rewriting systems over monoids — independently and essentially contemporaneously with the community's consolidation of KB theory in the early 1980s. Gilman states the completion criterion (Lemma 1's overlap conditions), the semi-decidability theorem (Proposition 2), and the word-problem corollary (Proposition 1(c)) with mathematical precision, using the language of ideals in free monoids rather than the term-rewriting framework that became dominant later.

The paper has institutional significance for this lab: Gilman was at Stevens Institute of Technology, the same institution where much of the algebraic-computing lineage relevant to the algo_mixing project originates. The 92-citation count is modest but well-distributed across the algebraic-computing community — the paper is a standard reference in treatments of complete presentations for monoids.

The growth-classification algorithm (Proposition 3 / Algorithm A) is a contribution independent of the completion procedure: it gives a combinatorial method for deciding between finite order, polynomial growth, and exponential growth directly from the complete presentation's graph, anticipating later work on automatic groups (where regular-language normal forms and automata-based growth analysis became central).

## Quotes

1. > "P terminates if and only if I(⟨α⟩) is finitely generated (and in particular if G is finite)." — Section 3, Proposition 2

2. > "A necessary condition for Procedure P to terminate is that the Schreier system L = F − I(⟨α⟩) be regular. Example 3 shows that the condition is not sufficient." — Section 6

## Open questions surfaced

1. **Ordering dependence**: P's termination depends on both the choice of well-ordering < and the generator labeling (Example 3). Gilman notes this but does not characterize which orderings guarantee termination for a given G — this became the ordering-strategy problem that KBMAG and modern KB implementations address with shortlex, wreath-product orderings, etc.

2. **Minimality of Algorithm A's graph**: Γ need not be isomorphic to the minimal automaton Γ(L) (Example 4). When does Γ = Γ(L)? What is the complexity of minimizing Γ after Algorithm A?

3. **Regular but non-terminating**: Example 3 constructs a group where L is regular but P diverges. Does there exist an algorithm that detects regularity of L first and then bypasses P entirely? (This is essentially asking about the automatic-groups decision problem — decidable for the automatic-group subclass, undecidable in general.)

4. **Generalization to non-monoid presentations**: The framework is monoid-specific (multiplication by generators on both sides). How do the conditions change for other algebraic structures (e.g., Lie algebras, where a different kind of "normal form" is needed)?

## Related material in vault

- **Parent overview**: [[Research/Group theory/Word Problem/word-problem-overview|word-problem-overview]]
- **Relevant MOCs**: [[Research/Group theory/_MOCs/_moc-presentations-and-orders|_moc-presentations-and-orders]] · [[Research/Group theory/_MOCs/_moc-knuth-bendix|_moc-knuth-bendix]] · [[Research/Group theory/_MOCs/_moc-word-problem|_moc-word-problem]]
- **Foundational predecessor (KB completion)**: [[Research/Group theory/Word Problem/knuth-bendix-1970|knuth-bendix-1970]] — Knuth & Bendix (1970): the original completion paper; Gilman's Procedure P is the same critical-pair completion algorithm, independently framed.
- **Concept note on presentations**: [[Research/Group theory/General/presentations-and-relations/presentations|presentations]] — the ⟨X | R⟩ framework that Gilman's free-monoid presentations generalize.
- **Author**: [[People/ethan-k|ethan-k]]
