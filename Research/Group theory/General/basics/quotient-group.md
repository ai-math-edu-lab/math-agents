---
title: "Quotient Group"
author: maumayma
language: en
source: "Dummit & Foote, Abstract Algebra (3rd ed.), §3.1"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - status/validated
related:
  - "[[normal-subgroup]]"
  - "[[homomorphism]]"
  - "[[group]]"
---

# Quotient Group

## Definition

Let N ⊴ G be a normal subgroup. The **quotient group** (or **factor group**) G/N is the set of left cosets {gN | g ∈ G} with group operation:

$$(aN)(bN) = (ab)N$$

This is well-defined precisely because N is normal (if N were not normal, the product would depend on the choice of coset representatives). The identity is eN = N; the inverse of gN is g⁻¹N.

*Source: D&F §3.1, Proposition 3.*

## Why it matters

Quotient groups capture the idea of "modding out" by a relation. G/N is G with all elements of N identified with the identity. When N = ker(φ) for some homomorphism φ: G → H, the First Isomorphism Theorem gives G/ker(φ) ≅ im(φ) — the quotient exactly recovers the image.

In computational group theory, the main use is the **quotient algorithm:** to understand G, compute G/γᵢ(G) (the nilpotent quotients of G) iteratively, or G/Gⁿ (the n-power quotient), or G/[G,G] (the abelianization).

## Examples

- **ℤ/nℤ = ℤ/⟨n⟩:** integers mod n. The cosets are {0+⟨n⟩, 1+⟨n⟩, ..., (n−1)+⟨n⟩}. Elements add modulo n.
- **Sₙ/Aₙ ≅ ℤ/2ℤ:** the sign map Sₙ → {±1} has kernel Aₙ; quotient is Z₂.
- **G/Z(G):** quotient by the center. If G/Z(G) is cyclic, then G is abelian (a useful lemma).
- **G/[G,G]:** the abelianization, G^{ab}. This is the largest abelian quotient of G.

## Finitely presented groups

For G = ⟨X | R⟩ and a normal subgroup N specified by additional relators S (i.e., N = ⟪S⟫):

$$G/N = \langle X \mid R \cup S \rangle$$

This is the key construction: adding relators to a presentation yields a quotient.

## Related concepts

- [[normal-subgroup]] — N ⊴ G is the prerequisite for forming G/N.
- [[homomorphism]] — G → G/N is the quotient homomorphism (canonical surjection).
- [[group]] — G/N is itself a group.
