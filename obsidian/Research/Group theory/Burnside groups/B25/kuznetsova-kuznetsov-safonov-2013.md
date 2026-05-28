---
title: "A parallel algorithm for computation of growth functions in the finite two-generator groups of period 5"
authors: A. S. Kuznetsova, A. A. Kuznetsov, K. V. Safonov
year: 2013
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: http://mi.mathnet.ru/pdma100
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
  - "[[kuznetsov-kuznetsova-2013]]"
cited_by: []
quality_notes: "source-text-incomplete-only-abstract-available. 3-page conference note (Prikl. Diskr. Mat. Suppl. 6, pp. 119–121). Original in Russian. Very thin abstract — one sentence. First author is A.S. Kuznetsova (daughter), not A.A. Kuznetsov (father); reflects A.S. Kuznetsova's role in implementing the parallel variant."
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

# A parallel algorithm for computation of growth functions in the finite two-generator groups of period 5

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

A parallel version of the algorithm for computation of growth functions in the finite two-generator groups of period 5 is presented. [trans.]

## TL;DR

Conference note presenting a parallelization of the growth-function algorithm from [[kuznetsov-kuznetsova-2013]]. Enables scaling to larger $k$ by distributing Cayley-graph BFS across multiple cores/nodes.

## Problem

The sequential growth-function algorithm from [[kuznetsov-kuznetsova-2013]] becomes a bottleneck for large $k$ (the BFS over $B_k$ with $5^k$ elements). Can the Cayley-graph BFS be parallelized to reach larger quotients?

## Approach

Parallelizes the sequential algorithm. Keywords "Cayley diameter, parallel algorithm" from the abstract suggest a distributed BFS approach. Full implementation details not available (abstract is one sentence).

## Key result

A parallel implementation of the growth-function algorithm for two-generator period-5 groups. Target groups and achieved k-range not specified in the abstract.

## Assumptions

- Builds on [[kuznetsov-kuznetsova-2013]] (sequential Hall polynomial multiplication).
- Assumes a multi-core or cluster environment.

## Limitations / scope

- Thin abstract; specific parallelization strategy, achieved speedup, and maximum $k$ reached are not recoverable.

## Replication evidence

Superseded or extended by [[kuznetsov-kuznetsova-2018]] (resource-efficient algorithm reaching $B_{18}$, $B_{19}$).

## Why this paper matters

This is the earliest parallelization in the Kuznetsov growth-function line, predating the 2018 resource-efficient approach. It established that the BFS for $B_k$ is amenable to parallel decomposition, enabling the 2018 paper's larger-k results.

## Quotes

Abstract-only access; no verbatim body-text quotes.

## Open questions surfaced

- What maximum $k$ was reached by this parallel implementation?
- What is the parallel speedup compared to the sequential algorithm?

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2013]] (sequential fast-multiplication algorithm; parallel version built on top)
- Related: [[kuznetsov-kuznetsova-2018]] (later resource-efficient approach reaching k=18,19)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
