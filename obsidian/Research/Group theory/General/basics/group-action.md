---
title: "Group Action"
author: maumayma
language: en
source: "Dummit & Foote, Abstract Algebra (3rd ed.), §1.7"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - status/validated
related:
  - "[[group]]"
  - "[[homomorphism]]"
  - "[[subgroup]]"
---

# Group Action

## Definition

A **group action** of G on a set Ω is a map · : G × Ω → Ω satisfying:

1. **Identity:** e · ω = ω for all ω ∈ Ω.
2. **Compatibility:** (gh) · ω = g · (h · ω) for all g, h ∈ G, ω ∈ Ω.

Equivalently, a group action is a homomorphism φ: G → Sym(Ω) (the symmetric group on Ω), where g maps to the permutation ω ↦ g · ω.

*Source: D&F §1.7, Definition.*

## Key definitions

- **Orbit of ω:** G · ω = {g · ω | g ∈ G} ⊆ Ω.
- **Stabilizer of ω:** G_ω = {g ∈ G | g · ω = ω} ≤ G (always a subgroup).
- **Orbit-Stabilizer Theorem:** |G · ω| × |G_ω| = |G| for finite G.
- **Kernel of the action:** {g ∈ G | g · ω = ω for all ω} = ker(φ) ⊴ G.
- **Faithful action:** kernel is trivial (G injects into Sym(Ω)).

## Why it matters

Group actions formalize symmetry concretely. Every abstract group G can be realized as a group of permutations (Cayley's theorem: G acts on itself by left multiplication, giving an embedding G ↪ Sym(G)). Actions are the tool for:

- **Counting** (Burnside's Lemma — not to be confused with the Burnside problem about exponents).
- **Structure theory:** the orbits partition Ω; the stabilizers are subgroups; studying the interplay gives structural information about G.
- **Coset enumeration:** G acts on the cosets of H by left multiplication; the orbit is the set of all cosets; the stabilizer of H is H itself. This is the Todd-Coxeter algorithm's underlying action.

## Examples

- **Left multiplication:** G acts on itself by g · h = gh. Faithful, transitive. Kernel = {e}.
- **Conjugation:** G acts on itself by g · h = ghg⁻¹. Orbits = conjugacy classes. Stabilizer of h = centralizer C_G(h).
- **G acts on cosets of H:** G acts on G/H by g · (aH) = (ga)H. This gives the permutation representation of G with kernel ∩_{g∈G} gHg⁻¹ (the largest normal subgroup of G contained in H).
- **Geometric symmetry:** The dihedral group D_n acts on the vertices of a regular n-gon by rotation and reflection.

## Burnside's Lemma (counting)

If G acts on a finite set Ω, the number of orbits equals:
$$\frac{1}{|G|} \sum_{g \in G} |Ω^g|$$
where Ω^g = {ω ∈ Ω | g · ω = ω} is the set of fixed points of g.

*Source: D&F §4.2, Theorem 11.*

**Note:** This "Burnside's Lemma" is about counting orbits, unrelated to the Burnside problem about groups of finite exponent (which concerns the Burnside groups B(m,n)).

## Related concepts

- [[group]] — G is the acting group.
- [[subgroup]] — stabilizers Gω are subgroups; kernels are normal subgroups.
- [[homomorphism]] — a group action is the same as a homomorphism G → Sym(Ω).
