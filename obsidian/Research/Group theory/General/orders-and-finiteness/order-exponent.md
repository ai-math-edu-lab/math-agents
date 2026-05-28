---
title: "Group Order, Exponent, and Torsion"
author: maumayma
language: en
source: "Dummit & Foote, Abstract Algebra (3rd ed.), §§1.1, 2.3"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/finitely-presented-groups
  - status/validated
related:
  - "[[group]]"
  - "[[subgroup]]"
---

# Group Order, Exponent, and Torsion

## Group order

The **order** of a group G is |G| — the cardinality of G as a set.

- |G| = 1: the trivial group {e}.
- |G| finite: G is a **finite group**.
- |G| = ∞: G is an **infinite group**.

**Order of an element:** For g ∈ G, the order of g is the smallest positive integer n with gⁿ = e (or ∞ if no such n exists). Notation: ord(g) or |g|.

**Lagrange's theorem:** For finite G and H ≤ G: |H| divides |G|. Corollary: ord(g) divides |G| for all g ∈ G.

*Source: D&F §3.2.*

## Exponent

The **exponent** of G is the smallest positive integer n such that gⁿ = e for all g ∈ G (or ∞ if no such n exists). Notation: exp(G) or sometimes written as "G has exponent n."

- exp(G) = 1 iff G is the trivial group.
- exp(ℤ/nℤ) = n.
- exp(ℤ/2ℤ × ℤ/2ℤ) = 2 (not 4): every element satisfies g² = e.
- For finite G: exp(G) divides |G| (Lagrange applied element-wise).

**The Burnside problem** asks: if exp(G) = n and G is finitely generated, must G be finite? The answer depends on n:
- n = 1, 2, 3, 4, 6: YES (G is always finite).
- n = 5, 7, 8, ...: open or infinite (Novikov-Adian for large odd n ≥ 665).
- See [[Research/Group theory/Burnside groups/B25/]] for the n=5 case (the primary focus of this vault).

## Torsion

An element g ∈ G is a **torsion element** (or **element of finite order**) if gⁿ = e for some positive integer n. It is **torsion-free** if no non-identity element has finite order.

- G is a **torsion group** if every element has finite order.
- G is **torsion-free** if only the identity has finite order.
- The set of torsion elements of an abelian group forms a subgroup (the **torsion subgroup**); this fails for non-abelian groups.

**Examples:**
- ℤ: torsion-free (every non-zero integer has infinite additive order).
- ℤ/nℤ: torsion group (every element satisfies nz = 0).
- ℚ: torsion-free.
- B(m,n): torsion group (exponent n by definition).

## Relation table

| Property | Meaning | Example |
|---|---|---|
| exp(G) = n | Every element satisfies gⁿ = e | B(m,n), cyclic group ℤ/nℤ |
| Torsion group | All elements have finite order | B(m,n), any finite group |
| Torsion-free | Only e has finite order | Free groups, ℤ, ℚ |
| Finite group | |G| < ∞ | S₃, ℤ/nℤ |

## Related concepts

- [[group]] — basic structure.
- [[subgroup]] — Lagrange's theorem connects order of subgroups to |G|.
