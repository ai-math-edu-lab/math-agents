---
title: "Do there exist infinite finitely generated groups of exponent 5? (Adian, Kourovka 4.2b)"
authors:
  - "S.I. Adian"
year_posed: 1973
venue: "Kourovka Notebook, 4th Issue (1973)"
url: ""
source_path: "docs/papers/Kourovka 2022.pdf"
language: en
domain: group-theory
methodology_type: theoretical
relevance: 2
key_concepts: []
extends: []
contradicts: []
replicates: []
cites:
  - "[[kourovka-2022]]"
  - "[[havas-wall-wamsley-1974]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
cited_by: []
quality_notes: "Adian's 4.2b and Kostrikin's 11.48 are equivalent questions for m=2: both ask whether B(2,5) is infinite. 4.2b is the more general formulation (does ANY infinite exponent-5 group exist?). Open as of Kourovka 2022. Old score/2 migrated to relevance: 2 (medium) per F4.2 decisions."
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

# Do there exist infinite finitely generated groups of exponent 5? (Adian, Kourovka 4.2b)

## Abstract

> "a) Find an infinite finitely generated group of exponent < 100. b) Do there exist such groups of exponent 5?" — S.I. Adian, Kourovka Notebook, 4th issue (1973)

## TL;DR

Adian's 1973 problem asks whether any finitely generated group of exponent 5 can be infinite. Equivalent (for m=2) to Kostrikin's Problem 11.48. Part (a) was settled by Novikov-Adian (1968) for odd exponents ≥ 665. Part (b) — exponent 5 — remains open.

## Problem

A group has **exponent n** if gⁿ = e for all elements g and n is minimal. The free Burnside group B(m,5) = ⟨a₁,...,aₘ | w⁵ = e for all words w⟩ is the universal finitely generated exponent-5 group on m generators. The problem reduces to: is B(m,5) infinite for some m ≥ 2?

Since B(m,5) surjects onto B(2,5) for m ≥ 2: if B(2,5) is infinite, so is B(m,5) for all m ≥ 2. Conversely, if all B(m,5) are finite for every m, 4.2b is answered negatively.

## Approach

No algorithmic attack is described in the problem statement. Relevant approaches:

- **Novikov-Adian theorem (1968):** B(m,n) infinite for all m ≥ 2, odd n ≥ 665 — does NOT apply to n=5.
- **KB completion:** If KB terminates with a confluent system for B(m,5), the group is finite → 4.2b answered negatively for that m. Non-termination gives no information.
- **Kostrikin's condition (Problem 11.48):** B(2,5) is infinite iff [x,y,y,y,y,y,y] ∉ ⟪w⁵⟫ in F(x,y). See [[kourovka-11.48-kostrikin-1990]].

## Key result

- B(m,n) infinite for odd n ≥ 665 (Novikov-Adian 1968): exponent 5 not covered.
- B(2,5) restricted = 5^34, class 12 ([[havas-wall-wamsley-1974]]): finite QUOTIENT, not B(2,5) unrestricted.
- **Problem 4.2b open** as of Kourovka 2022 (no ∗ marker).

**Equivalence table (m=2 case):**

| Framing | Resolution |
|---|---|
| Adian 4.2b: does an infinite exponent-5 group exist? | Open |
| Kostrikin 11.48: is [x,y,y,y,y,y,y] a product of 5th powers? | Open (same question) |

## Assumptions

- B(m,5) infinite for any m implies infinite exponent-5 groups exist; B(2,5) finite does not resolve 4.2b (B(3,5), B(4,5) etc. remain).

## Limitations / scope

- Even if B(2,5) and B(3,5) are proved finite, B(4,5) could still be infinite.
- KB non-termination does not prove infiniteness.
- Part (a) of Problem 4.2 is settled; only part (b) (exponent 5) is open.

## Replication evidence

N/A — open problem.

## Why this paper matters

This problem provides the broadest framing for the B(2,5) program: not just "is this specific group finite?" but "does any infinite group of this kind exist?" If the Mixer's KB experiments confirm finiteness for B(2,5) and B(3,5) and B(4,5), that constitutes strong computational evidence for a negative answer to 4.2b — a publishable contribution even without a complete proof.

## Quotes

> "Do there exist such groups of exponent 5?" — S.I. Adian, Problem 4.2b

## Open questions surfaced

- Is B(3,5) finite? B(4,5)? Each confirmation strengthens the case against an infinite exponent-5 group.
- Can KB divergence behavior itself prove infiniteness for some B(m,5)? (Not directly with current methods.)

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[kourovka-2022]], [[havas-wall-wamsley-1974]], [[kourovka-11.48-kostrikin-1990]]
- Cited by (in vault): (none currently)
