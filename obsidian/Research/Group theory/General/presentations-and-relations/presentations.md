---
title: "Group Presentations ⟨X | R⟩"
author: maumayma
language: en
source: "Lyndon & Schupp, Combinatorial Group Theory (1977), §I.1; Dummit & Foote (3rd ed.), §6.3"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/finitely-presented-groups
  - status/validated
related:
  - "[[free-groups]]"
  - "[[tietze-transformations]]"
  - "[[coset-enumeration]]"
---

# Group Presentations ⟨X | R⟩

## Definition

A **group presentation** is a pair (X, R) where:
- X is a set of **generators** (symbols + their formal inverses X⁻¹).
- R is a set of **relators** — words in F(X) that are declared to equal the identity.

The group **presented** by (X, R) is:
$$G = \langle X \mid R \rangle = F(X) / \langle\!\langle R \rangle\!\rangle$$
where ⟪R⟫ is the normal closure of R in F(X) — the smallest normal subgroup of F(X) containing every element of R.

**Notation:** Relators r ∈ R are written as r = 1 (or sometimes r as a word with implicit = 1). An equation "u = v" is shorthand for the relator uv⁻¹ ∈ R.

*Source: Lyndon-Schupp §I.1.*

## Why it matters

Every group has a presentation; this is the fundamental theorem of presentations (every group is a quotient of a free group). Presentations allow us to specify infinite groups finitely, and to study groups algebraically by studying their relators.

**The word problem** for G = ⟨X | R⟩ asks whether a given word w ∈ F(X) represents the identity in G (i.e., whether w ∈ ⟪R⟫). This is the central decision problem in combinatorial group theory.

## Examples

| Group | Presentation |
|---|---|
| Cyclic group ℤ/nℤ | ⟨a | aⁿ⟩ |
| Dihedral group D_n | ⟨r, s | rⁿ, s², srsr⟩ |
| Symmetric group S₃ | ⟨a, b | a², b³, (ab)²⟩ |
| Free group F₂ | ⟨a, b | ⟩ (no relators) |
| B(2,5) restricted | ⟨a, b | w⁵ = 1 for all words w⟩ → finite presentation from [[Research/Group theory/Burnside groups/B25/havas-wall-wamsley-1974]] |

## Finitely presented groups (FPGs)

A group is **finitely presented** if it has a presentation with finitely many generators and finitely many relators. This is the setting of most computational group theory:

- The word problem may be decidable or undecidable for FPGs in general (Novikov-Boone).
- For specific families (hyperbolic groups, automatic groups), the word problem is efficiently decidable.
- Knuth-Bendix completion attempts to derive a confluent rewriting system from the relators.

## Related concepts

- [[free-groups]] — F(X) is the starting point; G = F(X)/⟪R⟫.
- [[tietze-transformations]] — manipulations of presentations that don't change the presented group.
- [[coset-enumeration]] — algorithmic enumeration of cosets of a subgroup in G.
