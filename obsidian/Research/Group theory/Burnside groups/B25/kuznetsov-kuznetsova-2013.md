---
title: "Fast multiplication in finite two-generated groups of exponent five"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2013
venue: Prikladnaya Diskretnaya Matematika
url: http://mi.mathnet.ru/pdm397
url_translated:
language: ru
methodology_type: methodology
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[havas-wall-wamsley-1974]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
cited_by:
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-karchevsky-2016]]"
  - "[[kuznetsova-kuznetsov-safonov-2013]]"
  - "[[kuznetsov-kuznetsova-2018]]"
  - "[[kuznetsov-safonov-2015]]"
  - "[[kuznetsov-2015-cayley-exp3]]"
  - "[[kuznetsov-safonov-2014]]"
quality_notes: "Full journal paper (Prikl. Diskr. Mat. 1(19), pp. 110–116, 7 pages). Original in Russian. Only abstract available from mathnet.ru. This paper is the computational foundation for all subsequent Kuznetsov growth-function papers — efficient Hall polynomial multiplication is the core oracle for group element computation in B₀(2,5) quotients."
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
  - paper
  - status/draft
project: b25
---

# Fast multiplication in finite two-generated groups of exponent five

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

An algorithm for fast multiplication of elements in finite two-generated groups of exponent five based on Hall's polynomials is described. [trans.]

## TL;DR

Presents a fast Hall-polynomial multiplication algorithm for elements of the two-generator exponent-5 groups $B_k$ (quotients of $B_0(2,5)$). This is the computational foundation that all subsequent Kuznetsov growth-function and Cayley-graph papers depend on.

## Problem

The power commutator representation of $B_0(2,5)$ (from [[havas-wall-wamsley-1974]]) expresses elements as $a_1^{\alpha_1} \cdots a_{34}^{\alpha_{34}}$ with $\alpha_i \in \mathbb{Z}_5$. Multiplication of two such elements requires applying the Hall polynomial identities to bring the product back to normal form — a non-trivial computation for 34-generator groups. Can this be done efficiently?

## Approach

Uses Hall's polynomial identities — the core combinatorial tool of the power commutator method — to implement group multiplication. "Fast" here likely means: rather than applying all $\binom{34}{2}$ polynomial identities sequentially, a structured evaluation order or memoization reduces the number of operations. Full algorithm details not available (abstract is two sentences).

## Key result

An efficient algorithm for Hall-polynomial multiplication in $B_k$ groups. Specific speedup factor over naive implementation not quoted.

## Assumptions

- $B_0(2,5)$ power commutator presentation from [[havas-wall-wamsley-1974]] is the working basis.
- Hall polynomial identities are precomputed or efficiently evaluated.

## Limitations / scope

- Applies to finite quotients $B_k$ of $B_0(2,5)$; not applicable to the free $B(2,5)$ unless finite.
- "Fast" is relative; no benchmark comparison against alternative multiplication methods is quoted.

## Replication evidence

The algorithm is used in [[kuznetsov-2016]], [[kuznetsov-karchevsky-2016]], [[kuznetsov-kuznetsova-2018]], [[kuznetsova-kuznetsov-safonov-2013]], and all other Kuznetsov growth-function papers — serving as implicit replication through usage.

## Why this paper matters

Fast element multiplication is the rate-determining step in all $B_0(2,5)$ computational experiments. Without efficient Hall polynomial evaluation, the Cayley graph BFS needed for growth functions would be impractically slow. This paper is the computational foundation of the entire Kuznetsov B(2,5) line: every subsequent growth-function, Cayley-graph, and subgroup paper in this vault depends on the multiplication oracle developed here.

## Quotes

Abstract-only access; no verbatim body-text quotes.

## Open questions surfaced

- What is the complexity of this multiplication algorithm (in terms of $k$ and the element representation)? Is it $O(k^2)$? $O(k \log k)$?
- Does the same algorithm extend to other Hall-polynomial groups (e.g., exponent 3 or 7 groups)?

## Related material in vault

- Extends: [[havas-wall-wamsley-1974]] (power commutator presentation; Hall polynomial framework)
- Cites: [[havas-wall-wamsley-1974]]
- Cited by: [[kuznetsov-2016]], [[kuznetsov-karchevsky-2016]], [[kuznetsova-kuznetsov-safonov-2013]], [[kuznetsov-kuznetsova-2018]]
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
