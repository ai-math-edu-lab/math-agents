---
title: "Rewriting Systems and Geometric Three-Manifolds"
authors: Susan Hermiller, Michael Shapiro
year: 1999
venue: "Geometriae Dedicata, vol. 76, pp. 211–228"
url: "https://arxiv.org/abs/math/9611205"
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date: 2026-06-11
key_concepts:
  - "[[Concepts/complete-rewriting-systems]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[Research/Group theory/Word Problem/knuth-bendix-1970|knuth-bendix-1970]]"
  - "[[Research/Group theory/Word Problem/dershowitz-jouannaud-1990|dershowitz-jouannaud-1990]]"
  - "[[le-chenadec-1986]]"
cited_by: []
author: ethan-k
tags:
  - agent/research
  - user/ethan-k
  - domain/group-theory
  - topic/rewriting-systems
  - topic/complete-rewriting-systems
  - topic/word-problem
  - topic/geometric-group-theory
  - topic/3-manifolds
  - topic/fundamental-group
  - topic/knuth-bendix
  - paper
  - status/draft
---

# Rewriting Systems and Geometric Three-Manifolds

## Abstract

The fundamental groups of most (conjecturally, all) closed three-manifolds with uniform geometries have finite complete rewriting systems. The fundamental groups of a large class of amalgams of circle bundles also have finite complete rewriting systems. The general case remains open.

## TL;DR

Hermiller and Shapiro prove that the fundamental group of any closed 3-manifold carrying one of Thurston's eight uniform geometries admits a finite complete rewriting system (hence has a decidable word problem via normal-form reduction), provided the manifold is hyperbolic only if it virtually fibers over a circle. They extend this to a large class of non-uniform graph manifolds built from circle bundles with "shear" gluings, and leave the fully general case as an open question.

## Problem

Do the fundamental groups of closed 3-manifolds (satisfying Thurston's geometrization conjecture) admit finite complete rewriting systems? A finite complete rewriting system gives a concrete, confluent, Noetherian string rewriting presentation that solves the word problem by reducing every word to a unique normal form — so the question is whether such presentations exist for geometrically constrained 3-manifold groups.

## Approach

The paper splits into two parts:

**Uniform geometries (Section 3):** Uses Thurston's classification of closed Riemannian 3-manifolds with uniform metrics into eight geometry types (Proposition 3.5 in the paper). For each geometry type the authors invoke four previously known closure properties of the class of groups with finite complete rewriting systems:
- Proposition 3.3 [3]: finite-index subgroups transfer finite complete rewriting systems upward.
- Proposition 3.4 [2]: extensions $1 \to K \to G \to Q \to 1$ with $K$ and $Q$ having finite complete rewriting systems give $G$ one as well.
- Known results for surface groups (Prop. 3.2), $\mathbb{Z}$ (Prop. 3.1), and the trivial group (Prop. 3.0).

Each geometry type is handled by expressing $\pi_1(M)$ as a virtual extension of groups already known to carry finite complete rewriting systems.

**Non-uniform / graph manifolds (Sections 5–6):** Constructs explicit finite complete rewriting systems. For a manifold built from two circle bundles glued by a "shear gluing" (matrix $\begin{pmatrix}1 & n \\ 0 & 1\end{pmatrix} \in SL_2(\mathbb{Z})$), the authors write down an explicit rule set $R$, prove it is Noetherian via recursive path ordering (Lemma 5.1), and verify completeness by checking that the irreducible language bijects to the group via a normal-form argument (Lemmas 5.2–5.3 and Theorem 2). Section 6 extends this to arbitrary graphs of circle bundles satisfying a loop-deletion-gives-a-tree condition, using a two-stage Knuth–Bendix completeness argument on the rule system $R_0$ (no blue HNN relators) then extending to the full system $R$ via a disorder-function ordering; 84 critical pairs were resolved computationally (Section 6, proof of Theorem 3).

## Key result

**Theorem 1 (§ 3):** Suppose $M$ is a closed three-manifold bearing one of Thurston's eight geometries. Suppose further that if $M$ is hyperbolic, then $M$ virtually fibers over a circle. Then $\pi_1(M)$ has a finite complete rewriting system.

**Theorem 2 (§ 5):** If the manifold $M$ can be decomposed into two vertex manifolds, such that each vertex manifold is the product of a surface with boundary with a circle, and such that these are connected with a shear gluing, then $\pi_1(M)$ has a finite complete rewriting system.

**Theorem 3 (§ 6):** Suppose that $\Gamma$ is a graph for which, when all of the loops in $\Gamma$ are removed, the resulting graph is a tree. If $M$ can be decomposed into a graph of circle bundles with graph $\Gamma$, such that each vertex manifold is the product of a surface with boundary with a circle, and such that the gluing corresponding to each edge and loop is a shear gluing, then $\pi_1(M)$ has a finite complete rewriting system.

The completeness of the rule system $R$ in Section 6 was verified computationally using Knuth–Bendix; **84 critical pairs** were resolved (stated explicitly in the proof of Theorem 3).

## Assumptions

- Manifolds are closed (compact, without boundary).
- Theorem 1 applies only to manifolds with *uniform* Riemannian metrics (Thurston's eight geometries); the non-uniform / geometrization-conjecture case requires additional structure.
- For hyperbolic manifolds in Theorem 1: the hypothesis that $M$ virtually fibers over a circle is invoked (Thurston's question 18 conjectures this always holds for closed hyperbolic 3-manifolds).
- Theorems 2 and 3 require that vertex manifolds be circle bundles over surfaces with boundary (not general Seifert-fibered spaces) and that gluings are "shear" ($SL_2(\mathbb{Z})$ matrix of the form $\begin{pmatrix}1 & n \\ 0 & 1\end{pmatrix}$).
- The paper relies on [6] (Hermiller–Meier) for the implication: infinite $\pi_1$ + finite complete rewriting system $\Rightarrow$ tame combing, and on [12] (Mihalik–Tschantz) for: tame combing $\Rightarrow$ universal cover homeomorphic to $\mathbb{R}^3$.

## Limitations / scope

- The general non-uniform case (arbitrary Seifert-fibered pieces or non-shear gluings) is explicitly left open (Section 7 question).
- No claim is made about non-geometric 3-manifolds or 3-manifolds that do not satisfy the geometrization conjecture.
- The Knuth–Bendix verification for Theorem 3 is computational (software-assisted) rather than a hand proof of completeness for the full rule set.
- The paper does not address automatic-group structure directly; it focuses on finite complete rewriting systems, which are strictly stronger than automaticity (every group with a finite complete rewriting system is automatic, but not vice versa).

## Replication evidence

No independent replication of the main theorems identified in this vault. The result for uniform geometries (Theorem 1) is a corollary of known closure properties and is not in doubt. The explicit rewriting systems for shear gluings (Theorems 2 and 3) rely on a Knuth–Bendix computation verified using the Rewrite Rule Laboratory software [9]; the critical-pair count (84) is stated explicitly and could be checked independently with any KB implementation.

## Why this paper matters

This paper establishes that large and natural classes of 3-manifold groups have word problems solvable by finite string rewriting — a stronger condition than just decidability. Finite complete rewriting systems give not just decidability but an explicit reduction procedure (normal-form algorithm), making them valuable for computation in geometric group theory.

The paper sits at the intersection of low-dimensional topology and computational algebra: it applies machinery from term rewriting theory (recursive path ordering, Knuth–Bendix completion) to questions about 3-manifold topology. The result connects directly to Thurston's geometrization program, which at the time of writing was still a conjecture (proven by Perelman 2003); the paper's framing as "most (conjecturally, all)" reflects this.

The extension to graph manifolds (Sections 5–6) is the more technically substantial contribution: instead of appealing to closure theorems it constructs and verifies explicit rewriting systems, demonstrating a methodology applicable to amalgamated products and HNN extensions of groups that arise from manifold splittings. The "shear gluing" restriction is a natural algebraic simplification of the general $SL_2(\mathbb{Z})$ gluing freedom and captures a geometrically significant subclass.

## Quotes

1. > "A finite complete rewriting system for a group is a finite presentation which solves the word problem by giving a procedure for reducing each word down to a normal form." — Section 1

2. > "Our computation resolved 84 critical pairs." — Section 6, proof of Theorem 3

## Open questions surfaced

- **Main open question (Section 7):** Does every fundamental group of a closed 3-manifold satisfying Thurston's geometrization conjecture have a finite complete rewriting system? The paper covers uniform-geometry manifolds and graph manifolds with shear gluings but the general case (arbitrary $SL_2(\mathbb{Z})$ gluings, general Seifert-fibered vertex manifolds) is open.
- Does the result extend to non-compact or orbifold versions of the eight geometries?
- For the non-shear gluing case: is the obstacle purely technical (difficulty of finding the right normal form) or is there a class of 3-manifold groups that genuinely do not admit finite complete rewriting systems?
- The paper notes that completeness for the general graph-of-circle-bundles case "becomes much more difficult" — is there a uniform algebraic criterion (beyond shear gluings) that guarantees a finite complete rewriting system for amalgams along $\mathbb{Z}^2$?

## Related material in vault

- Parent overview: [[Research/Group theory/Word Problem/word-problem-overview|word-problem-overview]]
- MOC: [[Research/Group theory/_MOCs/_moc-word-problem|_moc-word-problem]]
- MOC: [[Research/Group theory/_MOCs/_moc-knuth-bendix|_moc-knuth-bendix]]
- Cites: [[Research/Group theory/Word Problem/knuth-bendix-1970|knuth-bendix-1970]] — the KB algorithm used to verify completeness
- Cites: [[Research/Group theory/Word Problem/dershowitz-jouannaud-1990|dershowitz-jouannaud-1990]] — source for recursive path ordering (Def. 2.1, cited as [1])
- Related: [[Research/Group theory/Word Problem/epstein-et-al-1992-word-processing|epstein-et-al-1992-word-processing]] — automatic groups and word processing; automatic-group structure is a consequence of finite complete rewriting systems
- Related: [[Research/Group theory/Word Problem/techniques/automatic-groups|automatic-groups]] — conceptual context for the relationship between complete rewriting systems and automaticity

---
*Author: [[People/ethan-k|ethan-k]]*
