---
title: "Group Presentations and Order — Map of Content"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/finitely-presented-groups
  - topic/coset-enumeration
  - topic/moc
  - status/validated
---

# Group Presentations and Order — Map of Content

**This MOC is a curated reading path for group presentations and order computation** — from the foundational definitions (free groups, presentations, coset enumeration), through the tools for computing group order and structure, to the Cayley graph as a geometric view. Navigate here when you want to understand how groups are specified and how their structure is computed.

---

## Foundational definitions

- [[Research/Group theory/General/presentations-and-relations/free-groups]] — The free group F(X) as the universal group on generators; unique reduced forms; why every group is a quotient of a free group. The conceptual starting point for understanding presentations.

- [[Research/Group theory/General/presentations-and-relations/presentations]] — The presentation ⟨X | R⟩ = F(X)/⟪R⟫; relators vs. relations; finite vs. infinite presentations; FPGs as the setting of the word problem. The language in which all KB input is specified.

- [[Research/Group theory/General/orders-and-finiteness/order-exponent]] — Group order |G|, element order, exponent, torsion — the basic vocabulary for describing finite and infinite groups. Includes the Burnside problem framing (exponent n ⟹ finite?).

---

## Manipulation of presentations

- [[Research/Group theory/General/presentations-and-relations/tietze-transformations]] — Elementary operations that preserve the presented group: add/remove relators, add/remove generators. Used in simplification (Reidemeister-Schreier output) and in automated tools (GAP's `SimplifiedFpGroup`).

- [[Research/Group theory/General/presentations-and-relations/coset-enumeration]] — Todd-Coxeter algorithm for computing [G:H] and the coset table; terminates iff [G:H] < ∞; the computational version of Lagrange's theorem. The standard approach to computing |G| for a finitely presented group.

---

## The geometry

- [[Research/Group theory/General/presentations-and-relations/cayley-graphs]] — The Cayley graph Γ(G, S) as the geometric realization of a group; word metric; hyperbolicity (Gromov); growth functions; connection to automatic groups via regular-language normal forms and to coset enumeration via Schreier coset graphs.

- [[Research/Group theory/General/orders-and-finiteness/classification-fsg]] — The CFSG pointer note: every finite simple group is in one of four families. Relevant as background for understanding what "finite" means at the deepest structural level.

---

## Key paper

- [[havas-robertson]] — 1994 survey of computational tools for FPGs: coset enumeration, Reidemeister-Schreier, Tietze transformation, KB. The systematic pipeline for computing with unknown finitely presented groups. Contains the most practical discussion of when to use which tool.

---

## Tools (compute order and enumerate cosets)

- [[Research/Group theory/Tools/GAP/examples/01-group-order]] — GAP: compute |G| from a presentation (`Order(G)`) — verified with S3 (order 6) and B(2,3) (order 27).

- [[Research/Group theory/Tools/GAP/examples/02-coset-enumeration]] — GAP: enumerate right cosets of a subgroup and compute index. Verified: S3, Index [G:⟨a⟩] = 3.

- [[Research/Group theory/Tools/GAP/examples/04-exponent-subgroups]] — GAP: compute group exponent and list all subgroups. Verified: D4 (10 subgroups), Z/2Z × Z/2Z (exponent 2, not 4).

- [[Research/Group theory/Tools/GAP/gap-overview]] — GAP overview note with key function reference and ordering of tools.

---

## Related MOCs

- [[_moc-word-problem]] — What presentations enable (the word problem); navigate there for decidability and algorithms.
- [[_moc-knuth-bendix]] — KB as a presentation-based word-problem algorithm; navigate there for KB specifics.
- [[_moc-burnside]] — The Burnside groups as the primary application; presentations of B(m,n) are the inputs to all KB experiments.
