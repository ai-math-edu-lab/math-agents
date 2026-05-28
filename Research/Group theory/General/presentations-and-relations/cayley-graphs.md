---
title: "Cayley Graphs"
author: maumayma
language: en
source: "Dummit & Foote, Abstract Algebra (3rd ed.), §1.2; Lyndon & Schupp, Combinatorial Group Theory, §I.2"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/finitely-presented-groups
  - status/validated
related:
  - "[[presentations]]"
  - "[[group-action]]"
  - "[[coset-enumeration]]"
---

# Cayley Graphs

## Definition

Let G be a group and S ⊆ G a generating set (often required to be closed under inverses: s ∈ S ⟹ s⁻¹ ∈ S). The **Cayley graph** Γ(G, S) is the directed graph with:

- **Vertices:** one per element g ∈ G.
- **Edges:** for each g ∈ G and s ∈ S, a directed edge g → gs labeled by s.

If S is closed under inverses and symmetric (a reasonable convention), Γ(G, S) is treated as an undirected graph.

*Source: D&F §1.2; Lyndon-Schupp §I.2.*

## Why it matters

Cayley graphs make the group's geometry visible. The distance between two vertices g, h in Γ(G, S) equals the word length of g⁻¹h in the generators S — this is the **word metric** on G. The geometry of the Cayley graph (its shape, diameter, growth rate, hyperbolicity) directly reflects algebraic properties of G.

**Key connections:**
- **Word problem geometry:** Solving the word problem for w ∈ F(X) means asking: is the vertex g_w of Γ(G, X) the same as the identity vertex? The Cayley graph is the "arena" in which the word problem is solved.
- **Hyperbolicity (Gromov):** A group is **hyperbolic** iff its Cayley graph (with any finite generating set) is a hyperbolic metric space (δ-slim triangles). This is the key to Dehn's algorithm working in linear time.
- **Automatic groups:** A group is automatic iff its Cayley graph has a "rational structure" — the set of geodesic paths from the identity is a regular language.
- **Coset graphs:** The Schreier coset graph of H ≤ G (vertices = cosets of H, edges = right multiplication by generators) is the Cayley graph of G acting on G/H. Todd-Coxeter fills in this coset graph.

## Examples

- **Cayley graph of ℤ/nℤ:** a cycle of n vertices. Generator set S = {1, −1} (mod n).
- **Cayley graph of Z (the integers):** a two-way infinite path (bi-infinite line). S = {1, −1}.
- **Cayley graph of F₂ (free group of rank 2):** a 4-regular tree — every vertex has 4 edges. The tree has no cycles, reflecting the absence of relators.
- **Cayley graph of S₃:** a hexagon with additional "long" edges (depends on the generating set).

## Growth functions

The **growth function** γ(n) = |{g ∈ G | d(e, g) ≤ n in Γ(G, S)}| counts elements within word length n.

- **Polynomial growth:** abelian groups, nilpotent groups (Gromov's theorem: polynomial growth ↔ virtually nilpotent).
- **Exponential growth:** free groups, most non-elementary groups.
- **Intermediate growth:** Grigorchuk's group (1983) — the first example of a group with growth strictly between polynomial and exponential.

## Related concepts

- [[presentations]] — the generating set S comes from the presentation's generators.
- [[group-action]] — Cayley graph = G acting on itself by left multiplication; Schreier coset graph = G acting on G/H.
- [[coset-enumeration]] — the Todd-Coxeter algorithm constructs the Schreier coset graph.
