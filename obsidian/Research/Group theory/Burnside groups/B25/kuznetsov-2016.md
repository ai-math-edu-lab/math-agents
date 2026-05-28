---
title: "An algorithm for computation of the growth functions in finite two-generated groups of exponent 5"
authors: A. A. Kuznetsov
year: 2016
venue: Prikladnaya Diskretnaya Matematika
url: https://doi.org/10.17223/20710410/33/10
url_translated:
language: ru
methodology_type: methodology
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[kuznetsov-kuznetsova-2013]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-kuznetsova-2013]]"
cited_by: []
quality_notes: "Full journal paper (Prikl. Diskr. Mat. 3(33), pp. 116–125, 10 pages). Original in Russian. Abstract available from mathnet.ru. Closely related to [[kuznetsov-karchevsky-2016]] (conference note by same first author + Karchevsky in the same supplement issue), which presents the same k=15,16,17 growth function results. The full journal version likely contains the algorithm details; the conference version likely summarizes results."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/growth-functions
  - topic/exponent-5
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: b25
---

# An algorithm for computation of the growth functions in finite two-generated groups of exponent 5

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The paper presents a computational method for analyzing the largest 2-generator Burnside group of exponent 5, denoted $B_0(2,5)$, which has order $5^{34}$. Using a power commutator representation where elements are expressed uniquely as products of 34 generators and commutators, the author develops an algorithm to compute growth functions for quotient groups $B_k$ (having order $5^k$). The growth functions of $B_k$ relative to generating sets $\{a_1, a_2\}$ and $\{a_1, a_1^{-1}, a_2, a_2^{-1}\}$ for $k = 15, 16, 17$ were calculated using this new approach. [trans.]

## TL;DR

Presents an algorithm for computing Cayley graph growth functions of $B_0(2,5)$ quotients $B_k$ via the power commutator representation; applies it for $k = 15, 16, 17$ under two generating sets. This is the full journal version of the method whose results are also reported as a conference note in [[kuznetsov-karchevsky-2016]].

## Problem

How can one compute the growth function $f_k(s) = |\{g \in B_k : d(e, g) = s\}|$ for the quotient groups $B_k$ of $B_0(2,5)$, given their power commutator representation? The naive approach requires building the full Cayley table of $B_k$ (order $5^k$), which is memory-intensive.

## Approach

Uses the Hall polynomial power commutator representation from [[havas-wall-wamsley-1974]] to represent elements of $B_k$ and perform multiplication. Develops a BFS/BFS-variant on the Cayley graph of $B_k$ to compute growth functions. Applied to $k = 15, 16, 17$ (orders $5^{15}$, $5^{16}$, $5^{17}$) for two generating sets. Full algorithmic details in the paper; not recoverable from abstract.

## Key result

Growth functions of $B_k$ for $k = 15, 16, 17$ computed relative to:
- 2-generator set $\{a_1, a_2\}$
- 4-generator symmetric set $\{a_1, a_1^{-1}, a_2, a_2^{-1}\}$

Specific function values (sphere sizes at each distance) not quoted in the abstract. The diameter values derivable from these growth functions were extended in [[kuznetsov-kuznetsova-2018]] (resource-efficient variant reaching $B_{18}$, $B_{19}$).

## Assumptions

- $B_0(2,5)$ finite (established), quotients $B_k$ well-defined.
- Power commutator representation from [[havas-wall-wamsley-1974]] assumed correct.
- Hall polynomial multiplication (from [[kuznetsov-kuznetsova-2013]]) used as the group oracle.

## Limitations / scope

- Applied only to $k = 15, 16, 17$; full $B_0(2,5)$ ($k = 34$) not reached.
- Memory constraints likely prevent direct extension to large $k$ without the resource-efficient variant in [[kuznetsov-kuznetsova-2018]].

## Replication evidence

No independent replication known. Growth function values for $B_{15}, B_{16}, B_{17}$ are verifiable benchmarks.

## Why this paper matters

This paper provides the growth function algorithm that all subsequent Kuznetsov growth-function papers extend. The fast Hall polynomial multiplication from [[kuznetsov-kuznetsova-2013]] is the computational foundation; this paper builds the BFS/growth-function layer on top. The k=15,16,17 results are the seed data for the diameter extrapolations in [[kuznetsov-kuznetsova-2018]].

## Quotes

Abstract-only access; no verbatim body-text quotes.

## Open questions surfaced

- What are the exact growth function values for $B_{15}$, $B_{16}$, $B_{17}$? These are the seed benchmarks.
- Does the growth function exhibit polynomial or exponential growth in $s$ for these $B_k$?
- Can the algorithm be parallelized directly (vs. the separate parallel version in [[kuznetsova-kuznetsov-safonov-2013]])?

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2013]] (fast Hall polynomial multiplication enabling efficient group arithmetic)
- Cites: [[havas-wall-wamsley-1974]], [[kuznetsov-kuznetsova-2013]]
- Related: [[kuznetsov-karchevsky-2016]] (conference version of same result), [[kuznetsov-kuznetsova-2018]] (resource-efficient extension to k=18,19)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
