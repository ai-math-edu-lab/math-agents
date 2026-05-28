---
title: "Group"
author: maumayma
language: en
source: "Dummit & Foote, Abstract Algebra (3rd ed.), §1.1"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - status/validated
related:
  - "[[subgroup]]"
  - "[[homomorphism]]"
  - "[[group-action]]"
---

# Group

## Definition

A **group** is a set G together with a binary operation · : G × G → G satisfying:

1. **(Associativity)** For all a, b, c ∈ G: (a · b) · c = a · (b · c).
2. **(Identity)** There exists e ∈ G such that for all a ∈ G: e · a = a · e = a.
3. **(Inverses)** For each a ∈ G, there exists a⁻¹ ∈ G such that a · a⁻¹ = a⁻¹ · a = e.

The identity e and inverses a⁻¹ are unique. A group is **abelian** (or commutative) if additionally a · b = b · a for all a, b ∈ G.

*Source: D&F §1.1, Definition 1.*

## Why it matters

Groups are the algebraic abstraction of symmetry. Every set of symmetries (bijections from a set to itself, closed under composition) forms a group. The axioms distill exactly what is needed: composition of symmetries is associative; there is a "do nothing" symmetry (identity); and every symmetry can be reversed (inverse). The group axioms are minimal — removing any one axiom gives a weaker structure (monoid, semigroup, or quasigroup) that loses key theorems.

## Examples

- **Integers under addition:** (ℤ, +) — abelian, infinite, identity = 0.
- **Nonzero rationals under multiplication:** (ℚ*, ×) — abelian, infinite, identity = 1.
- **Symmetric group Sₙ:** bijections from {1,...,n} to itself under composition — non-abelian for n ≥ 3, |Sₙ| = n!.
- **Cyclic group ℤ/nℤ:** integers mod n under addition — abelian, |G| = n.
- **GL(n, F):** invertible n×n matrices over a field F under matrix multiplication — non-abelian for n ≥ 2.

## Related concepts

- [[subgroup]] — a subset of G that forms a group under the same operation.
- [[homomorphism]] — a map G → H preserving the group structure.
- [[group-action]] — a way for a group to act on a set, encoding symmetry.
- [[normal-subgroup]] — a subgroup closed under conjugation (key for forming quotient groups).
