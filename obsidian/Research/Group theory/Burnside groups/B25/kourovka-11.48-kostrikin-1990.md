---
title: "Kourovka Problem 11.48 — Kostrikin (1990)"
authors:
  - "A.I. Kostrikin"
year: 1990
venue: "Kourovka Notebook, 11th Issue (1990); reprinted in Kourovka 2022 No. 20"
url: ""
source_path: "docs/papers/Kourovka 2022.pdf"
language: en
domain: group-theory
methodology_type: theoretical
relevance: 1
key_concepts: []
extends: []
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kourovka-2022]]"
cited_by:
  - "[[b25-finiteness-11.48-kostrikin]]"
  - "[[b-exponent-5-adian-4.2b]]"
  - "[[algo-mixing-burnside-slides]]"
quality_notes: "This note covers the mathematical unpacking of Kourovka 11.48 in detail; for the Mixer-attack rationale, see [[b25-finiteness-11.48-kostrikin]]. The two notes are complementary: this one is mathematical, that one is strategic."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/word-problem
  - topic/finitely-presented-groups
  - paper
  - status/draft
project: b25
---

# Kourovka Problem 11.48 — Kostrikin (1990)

**The theoretical stake of all B(2,5) experiments.**

## Abstract

> "Is the commutator [x, y, y, y, y, y, y] a product of fifth powers in the free group ⟨x, y⟩? If not, then the Burnside group B(2, 5) is infinite." — A.I. Kostrikin, Kourovka Notebook, 11th issue (1990)

## TL;DR

Kostrikin's 1990 problem provides a mechanistic sufficient condition for B(2,5) infiniteness: if the weight-7 left-normed commutator [x,y,y,y,y,y,y] is not expressible as a product of fifth powers in the free group, then the unrestricted B(2,5) is infinite. The question is open as of the 2022 Kourovka Notebook.

## Problem

Is the unrestricted Burnside group B(2,5) = ⟨a,b | w⁵ = 1 for all words w⟩ finite or infinite?

Kostrikin's reformulation: Is the weight-7 commutator [x,y,y,y,y,y,y] = `[[[[[[x,y],y],y],y],y],y]` an element of the normal closure N = ⟪w⁵ | w ∈ F(x,y)⟫ in the free group F(x,y)?

**Equivalence:** B(2,5) = F(x,y)/N. If [x,y,y,y,y,y,y] ∈ N, the commutator is trivial in every exponent-5 group → consistent with B(2,5) being finite (nilpotent of class ≤ 6). If [x,y,y,y,y,y,y] ∉ N, this commutator is nontrivial in B(2,5) → B(2,5) is not nilpotent of any finite class → B(2,5) is infinite.

Note: The restricted B(2,5) is finite (5^34, class 12; see [[havas-wall-wamsley-1974]]). The unrestricted group is the object of this problem.

## Approach

No algorithmic attack is described in the problem statement itself. Existing approaches relevant to this problem:

- **KB completion:** If KB on the B(2,5) presentation terminates with a confluent rewriting system, the group is finite → the commutator IS in N. If KB diverges, no conclusion.
- **Structural approaches:** Proving [x,y,y,y,y,y,y] ∈ N would require a certificate (an explicit product of fifth powers equaling the commutator in F(x,y)); proving it ∉ N would require constructing a finitely generated exponent-5 group where this commutator is nontrivial.

## Key result

**Known partial results:**
- B(2,5) restricted = 5^34, class 12 ([[havas-wall-wamsley-1974]]) — does NOT resolve Problem 11.48 (restricted ≠ unrestricted).
- B(m,n) infinite for odd n ≥ 665, m ≥ 2 (Novikov-Adian 1968) — does NOT apply to n=5.
- **Problem 11.48 remains open** (no ∗ marker in Kourovka 2022).

**The weight-7 commutator in the 1974hww generator notation:**
- [2,1] = generator 3 (weight 2)
- [2,1,1] = generator 4 (weight 3)
- [2,1,1,1] = generator 6 (weight 4)
- Continuing left-norming by 1: the weight-7 element [x,y,y,y,y,y,y] maps to a specific weight-7 generator in the B(2,5) presentation. It is nontrivial in the restricted group (the restricted group has class 12, so weight-7 elements survive).

## Assumptions

- The equivalence "B(2,5) infinite ⟺ [x,y,y,y,y,y,y] ∉ N" relies on the Kostrikin-Sanov correspondence: a Burnside group of prime exponent is infinite iff it is not nilpotent.
- The restricted group being finite (5^34) is established in [[havas-wall-wamsley-1974]].

## Limitations / scope

- This note covers the mathematical content of Problem 11.48 only. For the Mixer-attack rationale (why KB mixing is score/3 for this problem), see [[b25-finiteness-11.48-kostrikin]].
- The problem asks about B(2,5). The analogous question for B(m,5), m > 2, is related (4.2b) but separate.
- KB experiments in this vault operate on the **restricted** B(2,5). Their results (identity certificates for specific long words) are evidence about the restricted group's word problem, not a direct attack on whether [x,y,y,y,y,y,y] ∈ N.

## Replication evidence

N/A — open problem; no solution to replicate. The restricted group computation in [[havas-wall-wamsley-1974]] is independently verified by two methods but addresses a different question.

## Why this paper matters

Problem 11.48 is the formal statement of the question that all B(2,5) experiments are ultimately working toward. It translates the abstract "is B(2,5) infinite?" into a concrete free-group element question — the kind of problem that can in principle be attacked algorithmically (prove [x,y,y,y,y,y,y] ∈ N by finding an explicit certificate).

The practical connection: if KB completing a confluent system for B(2,5) would prove finiteness, and finiteness would resolve Problem 11.48 in the negative (no, B(2,5) is not infinite; yes, [x,y,y,y,y,y,y] ∈ N), then the Mixer's KB experiments are a direct algorithmic attack on this open problem.

## Quotes

> "Is the commutator [x, y, y, y, y, y, y] a product of fifth powers in the free group ⟨x, y⟩? If not, then the Burnside group B(2, 5) is infinite." — A.I. Kostrikin, Problem 11.48

## Open questions surfaced

- Is [x,y,y,y,y,y,y] ∈ N in the free group? This IS the open problem.
- For m > 2: does B(m,5) being finite (for any m) imply the analogous weight-7 commutator is in N?
- Can a Certificate be extracted from a confluent KB rewriting system for B(2,5)? (If KB terminates: the normal form of [x,y,y,y,y,y,y] under the confluent system would show it reduces to identity, providing an implicit certificate.)

## Related material in vault

- Extends: (none — foundational problem)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[havas-wall-wamsley-1974]] (the restricted group result), [[kourovka-2022]] (source of Problem 11.48)
- Cited by (in vault): [[b25-finiteness-11.48-kostrikin]], [[b-exponent-5-adian-4.2b]], [[algo-mixing-burnside-slides]]
