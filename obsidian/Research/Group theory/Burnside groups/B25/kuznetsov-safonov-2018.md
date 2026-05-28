---
title: "On applications of the Cayley graphs of some finite groups of exponent five"
authors: Alexander A. Kuznetsov, Konstantin V. Safonov
year: 2018
venue: Journal of Siberian Federal University. Mathematics & Physics
url: https://doi.org/10.17516/1997-1397-2018-11-1-70-78
url_translated:
language: en
methodology_type: empirical
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
quality_notes: "Full journal paper (J. Sib. Fed. Univ. Math. Phys. 11:1, pp. 70–78, 9 pages). English language. Only abstract available from mathnet.ru; full text not retrieved. The paper reports |C_{B_0(2,5)}(φ)| = 5^16 for the inversion automorphism φ, which is the same automorphism studied in [[kuznetsov-filippov-2010-sjim]] (generators, order, solvability/nilpotency) — this paper extends that result to Cayley graph geometry."
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

# On applications of the Cayley graphs of some finite groups of exponent five

## Abstract

Let $B_0(2,5)$ be the largest two-generator finite Burnside group of exponent five. It has order $5^{34}$. The authors define an automorphism $\varphi$ which translates generating elements into their inverses. Let $C_{B_0(2,5)}(\varphi)$ be the centralizer of $\varphi$ in $B_0(2,5)$. It is known that $|C_{B_0(2,5)}(\varphi)| = 5^{16}$. The growth functions of the centralizer are computed for some generating sets. As the result the authors obtain diameters and average diameters of corresponding Cayley graphs of $C_{B_0(2,5)}(\varphi)$.

## TL;DR

Computes Cayley graph diameters and average diameters of the centralizer $C_{B_0(2,5)}(\varphi)$ (where $\varphi$ maps generators to inverses, $|C| = 5^{16}$) for multiple generating sets. Extends the 2010 structural work on this centralizer ([[kuznetsov-filippov-2010-sjim]]) to Cayley-graph geometry.

## Problem

Given the centralizer of the inversion automorphism of $B_0(2,5)$, a group of order $5^{16}$ — what are the Cayley graph diameters for various generating sets? Growth functions of subgroups of $B_0(2,5)$ connect to the broader question of the group's word geometry.

## Approach

Uses the known structure of $C_{B_0(2,5)}(\varphi)$ from the 2010 papers (generators, order $5^{16}$, solvability/nilpotency). Computes growth functions (number of elements at each distance from identity in the Cayley graph) for multiple generating sets. Derives diameters (maximum distance) and average diameters. Full computational methodology not available from abstract.

## Key result

- **$|C_{B_0(2,5)}(\varphi)| = 5^{16}$** (quoted as known; established in [[kuznetsov-filippov-2010-sjim]]).
- **Cayley graph growth functions** for $C_{B_0(2,5)}(\varphi)$ computed for several generating sets.
- **Diameters and average diameters** of corresponding Cayley graphs obtained. Specific numerical values not quoted in the abstract.

**Note on automorphism:** $\varphi$ here maps each generator to its inverse ($a_1 \mapsto a_1^{-1}$, $a_2 \mapsto a_2^{-1}$). This is the same inversion automorphism studied in [[kuznetsov-filippov-2010-sjim]]. Compare [[kuznetsov-kuznetsova-2017]], which studies a different automorphism (permutation-type, $|C| = 5^{17}$).

## Assumptions

- Works with $C_{B_0(2,5)}(\varphi)$, a finite group of order $5^{16}$.
- The $|C| = 5^{16}$ result is inherited from the 2010 papers; its correctness is assumed.

## Limitations / scope

- Results are for the centralizer subgroup, not $B_0(2,5)$ itself.
- Does not directly address $B(2,5)$ finiteness.

## Replication evidence

No independent replication known as of 2026-05-28.

## Why this paper matters

The Cayley graph geometry of the centralizer $C_{B_0(2,5)}(\varphi)$ (order $5^{16}$) is a tractable sub-problem: the centralizer is a proper subgroup, so the Cayley graph is smaller and directly enumerable. The diameter and growth function results here serve as:
1. **Subgroup benchmarks** for B(2,5) pipelines — any KB system for B(2,5) must, when restricted to the centralizer, produce consistent diameter bounds.
2. **Scaling indicators** — the centralizer of order $5^{16}$ is roughly the square root of $|B_0(2,5)|$ = $5^{34}$; its Cayley graph diameter gives a lower bound on the diameter of the full group.

## Quotes

No verbatim body-text quotes available (abstract-only access).

## Open questions surfaced

- What are the explicit diameter values for each generating set?
- How do the centralizer diameters scale compared to the full $B_0(2,5)$ diameter estimates from [[kuznetsov-kuznetsova-2018]]?
- Does the centralizer's growth function exhibit any special structure (e.g., polynomial growth) given its nilpotency?

## Related material in vault

- Extends: [[kuznetsov-filippov-2010-sjim]] (structural foundation: generators, order, solvability/nilpotency of same centralizer)
- Cites: [[havas-wall-wamsley-1974]], [[kuznetsov-filippov-2010-sjim]]
- Related (different automorphism): [[kuznetsov-kuznetsova-2017]] (Cayley graph of centralizer of permutation-type φ, |C| = 5^{17})
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]]
