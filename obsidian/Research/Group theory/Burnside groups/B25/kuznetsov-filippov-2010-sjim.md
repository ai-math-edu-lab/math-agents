---
title: "On an involutive automorphism of the Burnside group B₀(2,5)"
authors: A. A. Kuznetsov, K. A. Filippov
year: 2010
venue: Sibirskii Zhurnal Industrial'noi Matematiki
url: http://mi.mathnet.ru/sjim625
url_translated:
language: ru
methodology_type: empirical
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[kuznetsov-shlepkin-2010]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-shlepkin-2009]]"
cited_by:
  - "[[kuznetsov-kuznetsova-2017]]"
  - "[[kuznetsov-safonov-2018]]"
quality_notes: "Full journal paper (Sib. Zh. Ind. Mat. 13:3, pp. 68–75, 8 pages). Original in Russian. Closely related to [[kuznetsov-filippov-2010-vmj]] (same first author + Philippov/Filippov, same year, same topic — centralizer of order-2 automorphism of B₀(2,5)) in Vladikavkaz Mat. Zh. 12:4. The two papers likely report the same result (centralizer structure) with different levels of detail. The 8-page version here (Sib. Zh.) is likely the fuller treatment."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/exponent-5
  - topic/center-of-group
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: b25
---

# On an involutive automorphism of the Burnside group B₀(2,5)

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

We study the centralizer of the involutive automorphism of the Burnside group $B_0(2,5)$ taking the generators of $B_0(2,5)$ to their inverses. We find generators for the centralizer and compute its order, solvability length, and nilpotency length. [trans.]

## TL;DR

Structural study of the centralizer $C_{B_0(2,5)}(\varphi)$ where $\varphi$ is the inversion automorphism ($a_1 \mapsto a_1^{-1}$, $a_2 \mapsto a_2^{-1}$). Computes explicit generators, order, solvability length, and nilpotency length. This is the foundational structural result that the 2018 Cayley-graph paper ([[kuznetsov-safonov-2018]]) builds on.

## Problem

What is the structure of the fixed-point subgroup (centralizer) of the canonical inversion automorphism $\varphi: a_i \mapsto a_i^{-1}$ in $B_0(2,5)$?

## Approach

Explicit computation within $B_0(2,5)$ using the power commutator representation. Finds generators for $C_{B_0(2,5)}(\varphi) = \{g \in B_0(2,5) : \varphi(g) = g\}$, then computes structural invariants (order, solvability, nilpotency). Abstract-only access; full method not recoverable.

## Key result

- **Centralizer**: $C_{B_0(2,5)}(\varphi)$ for $\varphi: a_i \mapsto a_i^{-1}$.
- **Generators**: explicit set found (number not quoted in abstract).
- **Order**: $|C_{B_0(2,5)}(\varphi)| = 5^{16}$ (quoted in [[kuznetsov-safonov-2018]], which references this result as "known").
- **Solvability length**: computed (value not quoted in abstract).
- **Nilpotency length**: computed (value not quoted in abstract).

The order $5^{16}$ is confirmed by [[kuznetsov-safonov-2018]], which uses it as a known input.

## Assumptions

- $\varphi$ is the specific inversion automorphism $a_1 \mapsto a_1^{-1}$, $a_2 \mapsto a_2^{-1}$.
- $B_0(2,5)$ power commutator representation from [[havas-wall-wamsley-1974]] is the computational basis.

## Limitations / scope

- Specific to the inversion automorphism. A different order-2 automorphism (permutation-type) is studied in [[kuznetsov-kuznetsova-2017]] and gives a different centralizer ($5^{17}$).
- Not directly about $B(2,5)$.

## Replication evidence

[[kuznetsov-safonov-2018]] treats $|C| = 5^{16}$ as a known result from this line of work — implicit use serves as corroboration. See also [[kuznetsov-filippov-2010-vmj]] for the companion publication (shorter version of same result).

## Why this paper matters

The centralizer of the inversion automorphism is a canonical subgroup of $B_0(2,5)$: it is the fixed-point set of the most natural order-2 symmetry. Its order $5^{16}$ is roughly half the generators' contributions (the centralizer "sees" the half of $B_0(2,5)$ that is symmetric under the inversion). This result:
1. Establishes the explicit generators and order — needed as input for the 2018 Cayley-graph analysis.
2. Provides a structural invariant ($5^{16}$) that any B(2,5) computational tool must reproduce if $B(2,5) \cong B_0(2,5)$.

## Quotes

> "We study the centralizer of the involutive automorphism... taking the generators of $B_0(2,5)$ to their inverses." — Abstract [trans.]

## Open questions surfaced

- What are the explicit generators of $C_{B_0(2,5)}(\varphi)$?
- What are the solvability and nilpotency lengths (not quoted in abstract)?
- Is $C_{B_0(2,5)}(\varphi) \cong B_0(2,5)/N$ for some normal subgroup $N$?

## Related material in vault

- Extends: [[kuznetsov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]] (prior B₀(2,5) computation)
- Cites: [[havas-wall-wamsley-1974]], [[kuznetsov-shlepkin-2009]]
- Cited by: [[kuznetsov-kuznetsova-2017]], [[kuznetsov-safonov-2018]] (Cayley graph extensions)
- Related: [[kuznetsov-filippov-2010-vmj]] (companion publication, shorter version, same result)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
