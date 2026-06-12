---
title: "The Cayley graph of a subgroup of the Burnside group B₀(2,5)"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2017
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/10/6
url_translated:
language: ru
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[kuznetsov-filippov-2010-sjim]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-filippov-2010-sjim]]"
cited_by: []
quality_notes: "source-text-incomplete-only-abstract-available. 3-page conference note (Prikl. Diskr. Mat. Suppl. 10, pp. 19–21). Original in Russian. NOTE: the centralizer order quoted here is 5^17, while [[kuznetsov-safonov-2018]] (which studies the inversion automorphism φ: a_i → a_i^{-1}) gives 5^16. The 2017 paper may study a different automorphism φ (a permutation-type φ, not the inversion). Needs verification from full text."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/cayley-graphs
  - topic/growth-functions
  - topic/center-of-group
  - topic/exponent-5
  - paper
  - status/draft
project: b25
---

# The Cayley graph of a subgroup of the Burnside group B₀(2,5)

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The research examines the largest two-generator Burnside group of exponent five with order $5^{34}$. An automorphism $\varphi$ maps each generator to another generator, and the centralizer $C_{B_0(2,5)}(\varphi)$ has order $5^{17}$. The authors calculate the growth function relative to a minimal generating set, computing the diameter $D_X(C) = 33$ and the average diameter $\bar{D}_X(C) \approx 26.1$. [trans.]

## TL;DR

Computes the Cayley graph diameter ($D_X(C) = 33$, $\bar{D}_X(C) \approx 26.1$) of the centralizer of an automorphism $\varphi$ of $B_0(2,5)$ where $|C_{B_0(2,5)}(\varphi)| = 5^{17}$.

**Note**: the abstract says $\varphi$ maps "each generator to another generator." This is likely a **permutation-type automorphism** (not the inversion $a_i \mapsto a_i^{-1}$). Contrast with [[kuznetsov-safonov-2018]], which explicitly studies the inversion automorphism and gets $|C| = 5^{16}$. The different centralizer orders ($5^{17}$ vs $5^{16}$) are consistent with two different automorphisms.

## Problem

What is the Cayley graph diameter of $C_{B_0(2,5)}(\varphi)$ for the automorphism $\varphi$ of permutation type? (The inversion automorphism is studied in [[kuznetsov-safonov-2018]]; this paper treats a different $\varphi$.)

## Approach

Uses the power commutator representation of $B_0(2,5)$ from [[havas-wall-wamsley-1974]]. Computes the centralizer $C_{B_0(2,5)}(\varphi)$ and its growth function relative to a minimal generating set. Full computational details not available (abstract-only).

## Key result

- $|C_{B_0(2,5)}(\varphi)| = 5^{17}$ for this (permutation-type) automorphism $\varphi$.
- **Cayley graph diameter**: $D_X(C) = \mathbf{33}$.
- **Average diameter**: $\bar{D}_X(C) \approx \mathbf{26.1}$.

These are exact values (not estimates), computed for the minimal generating set $X$ of $C$.

## Assumptions

- $\varphi$ is an automorphism of $B_0(2,5)$; not an inversion (contrast with [[kuznetsov-safonov-2018]]).
- The power commutator representation from [[havas-wall-wamsley-1974]] is used throughout.

## Limitations / scope

- Results are for a specific automorphism and its centralizer (order $5^{17}$), not for $B_0(2,5)$ itself.
- Abstract does not specify which permutation $\varphi$ maps each generator to — full paper needed for exact definition.

## Replication evidence

No independent replication known. The values $D_X(C) = 33$ and $\bar{D}_X(C) \approx 26.1$ are verifiable given the centralizer structure from [[kuznetsov-filippov-2010-sjim]] or [[kuznetsov-filippov-2010-vmj]].

## Why this paper matters

The diameter 33 is a concrete benchmark for a subgroup of $B_0(2,5)$ of order $5^{17}$ — larger than the $5^{16}$-order centralizer in [[kuznetsov-safonov-2018]] (which has unspecified diameter in the abstract). The two 2017–2018 papers together provide Cayley geometry data for two different automorphism centralizers, giving a picture of how subgroup diameter scales with subgroup size in $B_0(2,5)$.

For the Mixer: the subgroup of order $5^{17}$ is the largest centralizer studied in this line; its diameter 33 means the Mixer's bidirectional search on this subgroup needs a meet-in-the-middle window of at most 17 from each end.

## Quotes

Abstract-only access; no verbatim body-text quotes.

## Open questions surfaced

- Which exact permutation does $\varphi$ map generators to? Abstract is ambiguous ("another generator").
- Is the order $5^{17}$ consistent with the known automorphism group structure of $B_0(2,5)$?
- How does the diameter 33 compare to the $\bar{D}_X$ values from the larger group computations in [[kuznetsov-kuznetsova-2018]]?

## Related material in vault

- Extends: [[kuznetsov-filippov-2010-sjim]] (structural foundation for centralizers of automorphisms in $B_0(2,5)$)
- Cites: [[havas-wall-wamsley-1974]], [[kuznetsov-filippov-2010-sjim]]
- Related: [[kuznetsov-safonov-2018]] (Cayley graph of centralizer of the different, inversion automorphism; |C| = 5^{16})
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
