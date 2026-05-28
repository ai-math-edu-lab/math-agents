---
title: "Classification of Finite Simple Groups"
author: maumayma
language: en
source: "Gorenstein, Lyons, Solomon, The Classification of the Finite Simple Groups (1994–present); Aschbacher, Finite Group Theory (2000)"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/finitely-presented-groups
  - status/validated
related:
  - "[[order-exponent]]"
  - "[[group]]"
  - "[[normal-subgroup]]"
---

# Classification of Finite Simple Groups

## The theorem (statement only)

**Theorem (Classification of Finite Simple Groups, CFSG, 1983/2004).** Every finite simple group is isomorphic to one of:

1. **Cyclic groups** ℤ/pℤ for prime p.
2. **Alternating groups** Aₙ for n ≥ 5.
3. **Groups of Lie type** — 16 infinite families, including:
   - Classical groups: PSL(n,q), PSp(2n,q), PΩ(n,q), etc.
   - Exceptional groups: G₂(q), F₄(q), E₆(q), E₇(q), E₈(q), twisted variants.
4. **26 sporadic simple groups** — including the Monster M (order ≈ 8 × 10⁵³), Mathieu groups M₁₁, M₁₂, M₂₂, M₂₃, M₂₄, and 21 others.

*Primary references: Gorenstein-Lyons-Solomon (the "CFSG project"), Aschbacher's revision (2004) closing a gap in the quasithin case.*

## Why it matters for group theory

CFSG is the deepest structural result in finite group theory. It classifies all "atoms" of finite group theory — the building blocks from which all finite groups are assembled via extension. Every finite group G has a composition series:
$$1 = G_0 \trianglelefteq G_1 \trianglelefteq ... \trianglelefteq G_k = G$$
where each factor Gᵢ/Gᵢ₋₁ is simple (Jordan-Hölder theorem). CFSG says: the factors are from the above list.

**Practical consequences:**
- Many questions about finite groups reduce to questions about the groups in the CFSG list.
- The groups in the CFSG list all have known presentations and well-understood computational properties.

## Scope of this note

This is a pointer note only. The proof of CFSG spans approximately 10,000–15,000 pages across hundreds of papers. This vault does not attempt to document the proof. The relevant aspects for group theory computation:

- **Order formulas** for groups of Lie type (needed to verify computed orders match the classification).
- **Presentations** for specific groups (Mathieu groups, PSL(n,q)) as test cases for computational group theory algorithms.
- **The sporadic groups** as hard test cases for coset enumeration and KB algorithms.

## Simple groups as test cases

Groups in the CFSG list appear as benchmark instances for coset enumeration and Knuth-Bendix:
- PSL(2,7) — order 168, the smallest non-abelian simple group with a 2-generator presentation.
- A₅ ≅ PSL(2,5) — order 60, the smallest non-abelian simple group.
- Mathieu group M₁₂ — order 95,040, an important coset enumeration benchmark.

## Related concepts

- [[group]] — simple groups are groups with no non-trivial normal subgroups.
- [[normal-subgroup]] — absence of normal subgroups defines simplicity.
- [[order-exponent]] — CFSG gives the complete list of possible orders of finite simple groups.
