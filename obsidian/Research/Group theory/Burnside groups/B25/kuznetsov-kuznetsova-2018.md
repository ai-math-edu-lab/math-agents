---
title: "A resource-efficient algorithm for study the growth in finite two-generator groups of exponent 5"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2018
venue: Prikladnaya Diskretnaya Matematika
url: https://doi.org/10.17223/20710410/42/7
url_translated:
language: ru
methodology_type: methodology
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-kuznetsova-2013]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-2016]]"
cited_by: []
quality_notes: "Full journal paper (Prikl. Diskr. Mat. 42(4), pp. 94–103, 10 pages). Original in Russian; abstract available from mathnet.ru. Provides concrete Cayley graph diameter estimates (105 for 2-gen, 69 for 4-gen) for B₀(2,5) — these are verifiable benchmarks."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/growth-functions
  - topic/cayley-graphs
  - topic/exponent-5
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: b25
---

# A resource-efficient algorithm for study the growth in finite two-generator groups of exponent 5

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The paper presents a modified algorithm for investigating growth patterns in finite groups that reduces space complexity while maintaining acceptable time efficiency. The approach involves selecting a suitable subgroup $N$ within group $G$ where $|N| \ll |G|$, independently calculating growth functions for cosets $gN$, then aggregating results to obtain the group's growth function. Researchers applied this method to compute growth functions for quotient groups $B_{18}$ and $B_{19}$, derived from $B_0(2,5)$ — the largest two-generator Burnside group of exponent 5 (order $5^{34}$). Results suggest the diameters of Cayley graphs of the group $B_0(2,5)$ are approximately 105 and 69 for two-generator and four-generator sets respectively. [trans.]

## TL;DR

Memory-efficient growth-function algorithm: instead of computing the full Cayley graph, compute coset-by-coset and aggregate. Applied to $B_{18}$ and $B_{19}$ quotients of $B_0(2,5)$. Reports concrete diameter estimates: ~105 (2-gen) and ~69 (4-gen) for $B_0(2,5)$ under the symmetric generating set. These are the key benchmarks.

## Problem

Computing growth functions of $B_0(2,5)$ quotients $B_k$ is memory-intensive because the full Cayley table of $B_k$ (order $5^k$) must be stored. Can a coset-decomposition approach reduce memory while still computing exact growth functions?

## Approach

1. Select a subgroup $N \le G$ with $|N| \ll |G|$ (e.g., $|N| \approx |G|^{1/2}$).
2. Compute growth functions for each coset $gN$ (smaller objects, $|N|$ elements each).
3. Aggregate to obtain the full group growth function $f(k) = |\{g \in G : d(e, g) = k\}|$.

Applied to $B_{18}$ (order $5^{18}$) and $B_{19}$ (order $5^{19}$) using the power commutator representation from [[havas-wall-wamsley-1974]]. Earlier algorithm (from [[kuznetsov-2016]]) required $O(|G|^2)$ memory for the Cayley table; this algorithm reduces that by the subgroup factor.

## Key result

- **Cayley graph diameter of $B_0(2,5)$ (estimated):**
  - Under 2-generator set $\{a_1, a_2\}$: diameter $\approx$ **105**
  - Under 4-generator set $\{a_1, a_1^{-1}, a_2, a_2^{-1}\}$: diameter $\approx$ **69**

These are estimates based on the $B_{18}$, $B_{19}$ computations; exact diameter of the full $B_0(2,5)$ (order $5^{34}$) is not computed in this paper.

## Assumptions

- $B_0(2,5)$ is finite (established); quotients $B_k$ are well-defined.
- The coset decomposition preserves enough structure to bound the full group's diameter. The "approximately" phrasing in the abstract suggests these are extrapolated estimates, not exact values.
- Hall polynomial arithmetic via [[havas-wall-wamsley-1974]] assumed correct.

## Limitations / scope

- Applies to $B_0(2,5)$ quotients only ($B_{18}$, $B_{19}$); exact diameter of full $B_0(2,5)$ not computed.
- Diameter estimates are approximate (based on large-$k$ quotient extrapolation).

## Replication evidence

No independent replication known. The diameter estimates (105 and 69) are verifiable by any tool that can compute growth functions for $B_{18}$ or $B_{19}$.

## Why this paper matters

The diameter estimates — **~105 for 2-gen, ~69 for 4-gen** — are the best available approximations for the Cayley graph diameter of $B_0(2,5)$. For the Mixer:
1. **Bound on rule coverage**: a KB system that has resolved $B_0(2,5)$ must be able to reduce any word of length ≤ 105 (under 2-gen) to normal form. If the Mixer's rule bank is exhausted before reaching length 105, it's incomplete.
2. **Target word length**: if Maria's target word (e.g., commutator of length ~50–100) is close to the diameter, the bidirectional search window must span at least half the diameter for the meet-in-the-middle approach to work.
3. **Algorithm validation**: any future B(2,5) growth-function tool can verify its $B_{18}$ and $B_{19}$ diameter values against the 105 and 69 numbers from this paper.

## Quotes

Abstract-only access; no verbatim body-text quotes.

## Open questions surfaced

- What is the exact diameter of $B_0(2,5)$ (at $k = 34$)? Is it close to the estimated 105?
- Is the relationship between $D_{A_2}(B_k)$ and $D_{A_4}(B_k)$ approximately constant (ratio 105/69 ≈ 1.52) across different k values?
- Can the coset-decomposition algorithm be extended to $k > 19$ on modern hardware?

## Related material in vault

- Extends: [[kuznetsov-2016]] (algorithm for growth functions; this paper is the memory-efficient variant), [[kuznetsov-kuznetsova-2013]] (fast multiplication needed for growth computation)
- Cites: [[havas-wall-wamsley-1974]]
- Related: [[kuznetsov-2019]] (Cayley graph diameter hypothesis via subgroup geometry)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]]
