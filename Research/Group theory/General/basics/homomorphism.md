---
title: "Homomorphism, Kernel, Image"
author: maumayma
language: en
source: "Dummit & Foote, Abstract Algebra (3rd ed.), §1.6"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - status/validated
related:
  - "[[group]]"
  - "[[normal-subgroup]]"
  - "[[quotient-group]]"
---

# Homomorphism, Kernel, Image

## Definition

A **group homomorphism** is a map φ: G → H between groups such that for all a, b ∈ G:
$$φ(a · b) = φ(a) · φ(b)$$

(The operation on the left is in G; on the right, in H.)

**Kernel:** ker(φ) = {g ∈ G | φ(g) = eₕ} — the preimage of the identity. Always a normal subgroup of G.

**Image:** im(φ) = φ(G) = {φ(g) | g ∈ G} — always a subgroup of H.

*Source: D&F §1.6, Definition.*

## Special cases

- **Isomorphism:** φ is bijective. G ≅ H means G and H have the same algebraic structure.
- **Endomorphism:** φ: G → G (same group).
- **Automorphism:** bijective endomorphism. Aut(G) is the group of automorphisms.

## First Isomorphism Theorem

If φ: G → H is a homomorphism, then:
$$G/\ker(φ) \cong \text{im}(φ)$$

*Source: D&F §3.3, Theorem 7.*

This is the foundational result connecting quotient groups to homomorphisms: every surjective homomorphism G ↠ H presents H as G/ker(φ).

## Why it matters

Homomorphisms are the structure-preserving maps of group theory — they tell us when two groups have the same algebraic content (isomorphisms) and how groups can be projected onto quotients (surjective homomorphisms). The kernel characterizes what gets "killed" by the map; the First Isomorphism Theorem says the quotient by the kernel recovers the image.

## Examples

- **Sign map Sₙ → {±1}:** a permutation maps to +1 (even) or −1 (odd). Kernel = alternating group Aₙ.
- **Abelianization G → G/[G,G]:** the quotient by the commutator subgroup. Kernel = [G,G]. Every group maps to its abelianization; this is the maximal abelian quotient.
- **Exponential map ℝ → S¹:** t ↦ e^{2πit}. Kernel = ℤ. Image = S¹. Shows ℝ/ℤ ≅ S¹.

## Related concepts

- [[normal-subgroup]] — kernels are always normal; conversely, every normal subgroup is the kernel of the quotient map.
- [[quotient-group]] — G/N is the codomain of the quotient homomorphism G → G/N.
