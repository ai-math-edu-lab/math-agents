---
title: "Computation of the center of the Burnside group B₀(2,5)"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2025
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/18/58
url_translated:
language: ru
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts:
  - "[[Concepts/cayley-table-closure-algorithm]]"
extends:
  - "[[kuznetsov-shlepkin-2010]]"
  - "[[kuznetsov-shlepkin-2009]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-shlepkin-2009]]"
  - "[[kuznetsov-shlepkin-2010]]"
cited_by: []
quality_notes: "source-text-incomplete-only-abstract-available. 4-page conference note (Prikl. Diskr. Mat. Suppl. 18, pp. 270–273). Original in Russian; abstract summary from mathnet.ru record. Citation count not retrievable. Uses supercomputer resources — compute scale not specified in abstract."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/exponent-5
  - topic/finite-group-enumeration
  - topic/center-of-group
  - paper
  - status/draft
project: b25
---

# Computation of the center of the Burnside group B₀(2,5)

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record. Original text is not preserved; follow `url` for the source.

## Abstract

The paper examines $B_0(2,5) = \langle a_1, a_2 \rangle$, described as the largest two-generator Burnside group of exponent five with order $5^{34}$. Using a power commutator presentation, elements are uniquely represented as products with exponents in $\mathbb{Z}_5$. The authors have calculated the elements of the center of $B_0(2,5)$ in the form of group words of the smallest length for the symmetric generating set, using supercomputer resources. [trans.]

## TL;DR

Computes the explicit center of $B_0(2,5)$ (supercomputer run), expressing each central element as the shortest group word over the symmetric generating set $\{a_1, a_1^{-1}, a_2, a_2^{-1}\}$. The center is a concrete structural invariant of $B_0(2,5)$; its elements are potential relators or verification anchors for B(2,5) experiments.

## Problem

What are the explicit central elements of $B_0(2,5)$, expressed as group words of minimum length over the symmetric generating set? The center $Z(B_0(2,5))$ is non-trivial (since $B_0(2,5)$ has nilpotency class 12, the class-12 lower central factor is central), but the explicit minimal-length words representing central elements were not previously computed.

## Approach

Uses the power commutator presentation of $B_0(2,5)$ (generators $a_1, \ldots, a_{34}$, each $\alpha_i \in \mathbb{Z}_5$; from [[havas-wall-wamsley-1974]]). Computes the center by finding all elements that commute with every generator $a_1, a_2$ — equivalently, elements $g$ such that $a_i g = g a_i$ for $i = 1, 2$. Reports results as shortest words over $A_4 = \{a_1, a_1^{-1}, a_2, a_2^{-1}\}$. Uses supercomputer resources (infrastructure not specified). Full algorithmic details not available (abstract-only access).

## Key result

**Main result**: the center $Z(B_0(2,5))$ has been explicitly computed; each central element is expressed as a group word of minimal length over the symmetric generating set $A_4$.

Specific details (center size, element list, word lengths) are not available from the abstract. $B_0(2,5)$ has nilpotency class 12, so the center contains (at minimum) the commutator weight-12 subgroup; the paper likely gives the full center as a subgroup of $B_0(2,5)^{34}$.

## Assumptions

- Works with $B_0(2,5)$ (finite, order $5^{34}$), not the free $B(2,5)$.
- Power commutator presentation from [[havas-wall-wamsley-1974]] assumed correct (well-established).
- Supercomputer computation assumed correct; no independent verification known.

## Limitations / scope

- Applies to $B_0(2,5)$ only. Not directly applicable to $B(2,5)$ if $B(2,5) \ncong B_0(2,5)$.
- "Smallest length for the symmetric generating set" — results depend on the generating set choice $A_4 = \{a_1, a_1^{-1}, a_2, a_2^{-1}\}$; different generating sets would give different word-length optimal expressions.
- Full center enumeration may require full group arithmetic — resource-intensive; exact compute cost not reported.

## Replication evidence

No independent replication known as of 2026-05-28. Supercomputer run; verification would require comparable resources.

## Why this paper matters

The center of $B_0(2,5)$ is a concrete structural invariant. For the Mixer B(2,5) attack, central elements have a specific property: they commute with everything, so their normal form under KB reduction must be the same regardless of the ordering used. This means:

1. **Cross-ordering consistency test**: a central element of $B_0(2,5)$ should, if B(2,5) ≅ B₀(2,5), reduce to the same normal form under both RPO and shortlex orderings in the Mixer. Failure indicates either a bug or a witness that B(2,5) ≠ B₀(2,5).
2. **Verification anchors**: the minimal-length central words are the cheapest elements to test in any B(2,5) pipeline — they're provably equal to 1 in $B_0(2,5)$ (as group words), so the KB system or bidirectional search must reduce them to the empty word.
3. **Structural data**: the center's size and generator words add to the known structural data about $B_0(2,5)$, complementing the 973 candidate-divergence relations from [[kuznetsov-shlepkin-2010]].

This is the most recent Kuznetsov paper in the vault (2025); it represents the current frontier of supercomputer-scale computation on $B_0(2,5)$.

## Quotes

Abstract-only access; no verbatim quotes extracted from body text.

## Open questions surfaced

- What is $|Z(B_0(2,5))|$? The class-12 lower central factor is central; the full center may be strictly larger.
- What are the minimal word lengths for the central elements? If the words are long (e.g., length ≥ 30), they overlap with the 973 candidate-divergence length range ([[kuznetsov-shlepkin-2010]]) — potentially useful cross-checks.
- Do any central elements of $B_0(2,5)$ reduce to the identity in $B(2,5)$'s KB pipeline, but NOT in $B_0(2,5)$'s? If so, that would distinguish the two groups.
- Can the central elements be obtained from the Mixer's B(2,5) pipeline without a separate supercomputer run, using the rule banks already generated?

## Related material in vault

- Extends: [[kuznetsov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]] (foundational B₀(2,5) computation by same first author)
- Cites: [[havas-wall-wamsley-1974]] (power commutator presentation)
- Concepts: [[Concepts/cayley-table-closure-algorithm]], [[Concepts/verification-methods-for-group-equality]]
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Complementary data: [[kuznetsov-shlepkin-2010]] (973 candidate-divergence relations at lengths 30–35; the center elements from this paper are a different but complementary set of structural anchors)
- Open problem: [[b25-finiteness-11.48-kostrikin]]
