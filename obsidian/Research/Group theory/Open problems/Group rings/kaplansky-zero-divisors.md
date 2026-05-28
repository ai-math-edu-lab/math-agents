---
title: "Kaplansky Zero-Divisors Conjecture (Kaplansky, c.1956)"
authors:
  - "I. Kaplansky"
year_posed: 1956
venue: "Circulated in lectures; no single canonical publication"
url: ""
source_path: ""
language: en
domain: group-theory
methodology_type: theoretical
relevance: 3
key_concepts:
  - "[[Concepts/kaplansky-zero-divisors]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[problems-people]]"
  - "[[grobner]]"
cited_by: []
quality_notes: "No source document in docs/papers/. Content written from general knowledge. Paper acquisition needed: Kaplansky's original (c.1956 lectures, no single paper); Linnell survey 'Zero divisors and group von Neumann algebras'; Gräter et al. for constructive approaches. No dedicated Kourovka entry for the classical conjecture (Kourovka 12.29 and 18.80 are related but different ring-theoretic questions). Old score/1 migrated to relevance: 3 (low) per F4.2 decisions. Source unavailable at 2026-05-28 re-fetch; content preserved from original note."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/group-rings
  - topic/finitely-presented-groups
  - paper
  - status/draft
---

# Kaplansky Zero-Divisors Conjecture (Kaplansky, c.1956)

## Abstract

> No canonical source document — conjecture circulated in Kaplansky's lectures around 1956. Content written from general knowledge. See `quality_notes` for paper acquisition list.

## TL;DR

For a torsion-free group G and a field F, the group ring F[G] has no zero-divisors (is an integral domain). Open in full generality since ~1956; proved for many specific group families (orderable, hyperbolic, one-relator, locally indicable). Named implementer in [[problems-people]]: Winston Lee.

## Problem

**Group ring:** F[G] consists of formal finite sums Σ fᵢgᵢ (fᵢ ∈ F, gᵢ ∈ G) with multiplication extending the group operation. If G has torsion (gⁿ = e for some n), zero-divisors exist trivially: (g−1)(gⁿ⁻¹+...+1) = 0.

**Conjecture:** For **torsion-free** G and field F: F[G] is an integral domain (no non-trivial α, β with αβ = 0).

Companion conjectures (also Kaplansky, also open in general):
- **Units conjecture:** only units in F[G] for torsion-free G are fg (f ∈ F×, g ∈ G).
- **Idempotents conjecture:** no non-trivial idempotents in F[G] for torsion-free G.

## Approach

No constructive attack known for the general case. Proved for specific families:

1. **Orderable groups (Kaplansky, 1948):** If G is totally orderable, F[G] has no zero-divisors (classical).
2. **One-relator groups (Lewin-Lewin, 1978):** Characteristic 0 case proved.
3. **Hyperbolic groups (Delzant-Steenbock, ~2010s):** Characteristic 0 case proved via geometric group theory.
4. **Locally indicable groups:** Proved.

The gap is for torsion-free groups that are not orderable, hyperbolic, or locally indicable.

## Key result

**Partial results (not exhaustive):**

| Group family | Status | Source |
|---|---|---|
| Orderable groups | Proved | Kaplansky (1948) |
| One-relator groups (char 0) | Proved | Lewin-Lewin (1978) |
| Hyperbolic groups (char 0) | Proved | Delzant-Steenbock (~2010s) |
| General torsion-free groups | **Open** | — |

## Assumptions

- G is torsion-free (without this condition, zero-divisors exist trivially).
- F is a field (the conjecture is stated for fields; group rings over more general rings are different).

## Limitations / scope

- **Torsion-freeness required:** Our primary Mixer targets (B(2,5), B(4,3)) are torsion groups (every element has finite order dividing 5 or 3). The Kaplansky conjecture does not apply to them. There is no Mixer path from B(2,5) to Kaplansky without working on torsion-free quotients.
- The Mixer architecture (KB completion, word rewriting) operates on group presentations, not group ring structure. The structural gap between word rewriting and integral domain properties of F[G] is too large for the current Mixer machinery.
- This note is included in the catalog because [[problems-people]] names Winston Lee as implementer — a data point about project scope, not a direct Mixer target.

## Replication evidence

N/A — open problem. The partial results (orderable, hyperbolic, one-relator) are established in the literature but not verified in this vault.

## Why this paper matters

This problem sits at the boundary of the Mixer's scope — the inventory notes it as relevance: 3 (low). Its primary vault value is as context: it shows the project was conceived broadly enough to include group ring problems, not just word problems. Winston Lee's implementation (from [[problems-people]]) may be testing specific torsion-free groups computationally; if so, the Mixer could serve as a preprocessing backend (reducing words to canonical forms before group ring computation), but cannot directly attack the conjecture.

## Quotes

> No verbatim quotes — no source document available.

## Open questions surfaced

- Is there a torsion-free group for which F[G] can be shown to have a zero-divisor? (Counterexample direction — extremely hard.)
- Can the Gröbner basis approach ([[grobner]]) be applied to group rings over specific torsion-free groups? (Indirect connection via the polynomial-ring machinery.)

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[problems-people]] (Winston Lee as implementer), [[grobner]] (adjacent group-ring polynomial machinery)
- Cited by (in vault): [[Concepts/kaplansky-zero-divisors]], [[Research/Group theory/Open problems/open-problems-catalog]]
