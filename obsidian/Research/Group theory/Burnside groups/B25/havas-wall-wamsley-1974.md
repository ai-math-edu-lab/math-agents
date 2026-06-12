---
title: "The two generator restricted Burnside group of exponent five"
authors:
  - George Havas
  - G.E. Wall
  - J.W. Wamsley
year: 1974
venue: "Bull. Austral. Math. Soc. 10, 459–470"
url: ""
source_path: "docs/papers/1974hww.pdf"
language: en
domain: group-theory
methodology_type: empirical
key_concepts:
  - "[[Concepts/verification-methods-for-group-equality]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[havas-newman-1980]]"
  - "[[havas-robertson]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
  - "[[kourovka-2022]]"
  - "[[problems-people]]"
  - "[[b25-finiteness-11.48-kostrikin]]"
  - "[[b-exponent-5-adian-4.2b]]"
  - "[[algo-mixing-burnside-slides]]"
  - "[[kuznetsov-shlepkin-2009]]"
  - "[[kuznetsov-shlepkin-2010]]"
  - "[[kuznetsov-tarasov-shlepkin-2009]]"
  - "[[kuznetsov-2019]]"
  - "[[kuznetsov-2020]]"
  - "[[kuznetsov-kuznetsova-2025]]"
  - "[[kuznetsov-kuznetsova-2021]]"
  - "[[kuznetsov-safonov-2018]]"
  - "[[kuznetsov-kuznetsova-2018]]"
  - "[[kuznetsov-kuznetsova-2017]]"
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-karchevsky-2016]]"
  - "[[kuznetsov-kuznetsova-2013]]"
  - "[[kuznetsov-2011]]"
  - "[[kuznetsov-filippov-2010-sjim]]"
  - "[[kuznetsov-filippov-2010-vmj]]"
  - "[[_synthesis-kuznetsov-b25-algorithmic-line]]"
  - "[[kalika-2026]]"
quality_notes: "Foundational — cited by every subsequent B(2,5) computation in this vault. Two independent methods (Lie algebra and nilpotent quotient) converge on the same result; the generator numbering 1–34 from this paper is the source of the comm_X_Y naming convention used throughout all B(2,5) experiments."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/word-problem
  - topic/coset-enumeration
  - topic/nilpotent-quotient
  - paper
  - status/draft
project: b25
---

# The two generator restricted Burnside group of exponent five

Havas, Wall & Wamsley (1974). The foundational B(2,5) paper.

## Abstract

> No verbatim abstract available — source is local PDF at `docs/papers/1974hww.pdf`. See TL;DR below.

## TL;DR

Proves |B(2,5)| = 5^34 and nilpotency class = 12 using two fully independent computational methods; delivers the complete consistent commutator power presentation in 34 generators whose numbering defines the `comm_X_Y` target words used in all subsequent B(2,5) experiments.

## Problem

Is the free restricted Burnside group on 2 generators of exponent 5 finite, and if so, what is its exact order and nilpotency class? Prior bounds from Kostrikin (1955): 5^31 ≤ |B(5,2)| ≤ 5^34.

## Approach

Two independent methods, both converging on 5^34, class 12.

**1. Lie-algebraic (Kostrikin-Wall-Wamsley):** Sanov's correspondence maps periodic groups of prime period to Lie rings. Kostrikin extended this to class 2p for r=2. The associated Lie ring E(5,2) is computed to class 12 via Wamsley's algorithm. Wall's additional relations at class 9 (involving a weight-8 polynomial on 70 monomials in GF(5)[x,y]) complete the proof that L(5,2) = E(5,2). Computing time: 9 CPU seconds.

**2. Nilpotent group computation (Wamsley-Bayes-Kautsky):** p-quotient algorithm iterates class by class, adding generators for each non-defining relation and enforcing consistency via collection equations. Full output: a presentation with generators 1–34 and exhaustive commutator relations. Computing time: 15 minutes.

## Key result

- **|B(2,5)| = 5^34** — exact, closing the Kostrikin gap of 5^31–5^34
- **Nilpotency class: 12** — exact
- All generators 3–34 have order 5 (power relations omitted in the table for brevity)
- Commutator relations among all 34 generators are listed exhaustively

**Generator table (using 1=a, 2=b):**

| Generator | Commutator | Weight |
|---|---|---|
| 1, 2 | free generators | 1 |
| 3 | [2,1] | 2 |
| 4 | [2,1,1] | 3 |
| 5 | [2,1,2] | 3 |
| 6 | [2,1,1,1] | 4 |
| 7 | [2,1,2,1] | 4 |
| 8 | [2,1,2,2] | 4 |
| 9 | [2,1,2,1,1] | 5 |
| 10 | [2,1,2,2,1] | 5 |
| 11 | [2,1,2,1,1,1] | 6 |
| 12 | [2,1,2,1,1,2] | 6 |
| 13 | [2,1,2,2,1,1] | 6 |
| 14 | [2,1,2,2,1,2] | 6 |
| ... | ... through weight 12 | ... |
| 34 | [2,1,2,2,1,2,1,2,2,1,1,1] | 12 |

**Target words derived from this table:**
- `comm_12_9` = [c₁₂, c₉] = `[[2,1,2,1,1,2], [2,1,2,1,1]]` (weight 12, maximum class depth)
- `comm_13_10` = [c₁₃, c₁₀] = `[[2,1,2,2,1,1], [2,1,2,2,1]]` (weight 12)

**Wall's additional relations at class 9 (key step):** three nontrivial relations involving a weight-8 associative polynomial f(x,y) ∈ GF(5)[x,y] on 70 monomial terms — these are the conditions needed for L(5,2) = E(5,2).

## Assumptions

- **Kostrikin (1959):** B(p,r) is finite for prime p — guarantees the restricted group exists and is finite; this paper pins down exact order.
- **Wall's additional relations:** stated as verified computationally at time of publication; the relations themselves were then unpublished (appeared in Wall 1974 conference proceedings).
- **Wamsley p-quotient algorithm correctness:** assumed; mutual verification from both independent approaches.
- **Sanov-Kostrikin correspondence:** that B(p,r) restricted ↔ the Lie ring E(p,r), extended to class 2p by Kostrikin.

## Limitations / scope

- Addresses the **restricted** B(2,5) only — the largest finite quotient. The **unrestricted** B(2,5) (whether infinite) is NOT addressed; see [[kourovka-11.48-kostrikin-1990]].
- B(r,5) for r > 2 not covered.
- Does not address the word problem complexity for the restricted group — only that a canonical presentation exists.

## Replication evidence

**Within-paper:** Two independent methods (Lie algebra + nilpotent quotient) both produce 5^34, class 12. This constitutes mutual verification.

[[havas-newman-1980]] surveys this result in 1980 and contextualizes it alongside other Burnside computations without re-deriving it. No independent external replication identified in this vault beyond the within-paper cross-check.

## Why this paper matters

This is the **primary source** for all B(2,5) computational work in this vault. Every experiment using `comm_12_9`, `comm_13_10`, or the generator numbering 1–34 derives from this paper's presentation. The fact that two fully independent methods converge on the same 5^34, class 12 gives high confidence in the result.

The paper also establishes the computational tradition — multiple independent algorithm types applied cooperatively to the same hard group-theory problem — that is precisely the philosophy behind the Mixer architecture, nearly 50 years later.

For KB experiments: the relators derived from this presentation's commutator table are the direct input to KBMAG for all B(2,5) computations. The abelianization check (exponents of generators 1 and 2 mod 5) grounded in this paper's generator structure is also the primary sanity-check in the B(2,5) reduction pipeline.

## Quotes

> No short verbatim quotes extracted — source is local PDF `docs/papers/1974hww.pdf`. See source for specific theorem statements and the full commutator relation table.

## Open questions surfaced

- What is |B(r,5)| for r > 2? B(3,5), B(4,5) are open.
- Is the **unrestricted** B(2,5) finite or infinite? This is Kourovka Problem 11.48 — see [[kourovka-11.48-kostrikin-1990]].
- What is the word problem complexity for the restricted B(2,5)? The paper provides a canonical presentation but not an efficient decision procedure.

## Related material in vault

- Extends: (none — foundational paper; no prior vault notes on B(2,5))
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (upstream, outside vault): Kostrikin (1959), Sanov (1952), Wamsley p-quotient algorithm
- Cited by (in this vault): [[havas-newman-1980]], [[havas-robertson]], [[kourovka-11.48-kostrikin-1990]], [[kourovka-2022]], [[problems-people]], [[b25-finiteness-11.48-kostrikin]], [[b-exponent-5-adian-4.2b]], [[kuznetsov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]], [[_synthesis-kuznetsov-b25-algorithmic-line]]
