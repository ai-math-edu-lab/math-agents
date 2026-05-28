---
title: "Kaplansky Zero-Divisors Conjecture — Candidate Mixer Domain"
domain: group-theory
project: none
status: draft
author: maumayma
related:
  - "[[problems-people]]"
introduced_in:
  - "[[Research/Group theory/Open problems/Group rings/kaplansky-zero-divisors]]"
appears_in:
  - "[[Research/Group theory/Open problems/Group rings/kaplansky-zero-divisors]]"
related_concepts: []
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/group-rings
  - concept
  - status/draft
---

# Kaplansky Zero-Divisors Conjecture — Candidate Mixer Domain

Flagged as a Mixer candidate in [[problems-people]]. Implementation listed as Winston Lee.

## The conjecture

For a **torsion-free group** G and a **field** F, the group ring F[G] has no zero-divisors.

Formally: if α, β ∈ F[G] with α ≠ 0 and β ≠ 0, then αβ ≠ 0.

Equivalently: F[G] is an **integral domain**.

**Status:** Open for general torsion-free groups. Proved for:
- Torsion-free orderable groups (Kaplansky 1948)
- Groups with a locally indicable subgroup structure (various)
- Torsion-free hyperbolic groups (Delzant-Steenbock, for fields of characteristic 0)
- Torsion-free one-relator groups (Lewin-Lewin 1978, characteristic 0)
- Many specific group families

**Not proved** for general torsion-free groups.

## Connection to word problem / decidability

The zero-divisors conjecture for a group G implies a strong statement about the word problem in G: if you can multiply elements of F[G] without producing spurious zero products, you can use the ring structure as a filter for group equations. This is directly related to:

- **Kaplansky's unit conjecture** (also open): the only units in F[G] for torsion-free G are trivial units fg with f ∈ F×, g ∈ G.
- **Kaplansky's idempotent conjecture**: no non-trivial idempotents in F[G] for torsion-free G.

All three are open in full generality.

## Why Mixer-shaped

Group ring computations over F[G] are a form of symbolic algebra on words. A Mixer could combine:

- KB completion on the group G itself (producing canonical word forms)
- Gröbner basis computation in F[G] (producing canonical polynomial forms)
- Zero-divisor detection as a cross-check between the two

The [[grobner]] paper (Kreuzer-Myasnikov-Rosenberger) already combines group-word rewriting with polynomial ideal theory via linear representations — the Kaplansky framework is the algebraic structure underlying why that approach works or fails.

## What this is NOT

- Not an active Mixer project. The [[problems-people]] listing is an aspirational assignment.
- The conjecture is about abstract group rings; practical Mixer implementations would need a specific group family (likely torsion-free quotients of Burnside groups, or free groups).
- Do not assume B(2,5) is torsion-free (it is not — elements have order 5).

## Open questions for Mixer application

1. Which torsion-free groups appear naturally in our experiment pipeline (e.g., free groups, one-relator groups from quotient tests)?
2. Can zero-divisor tests in group rings be used as word-problem oracles for the groups that appear as "kernels" in the Havas-Robertson quotient-kernel iteration?
3. Are there group ring computations fast enough to serve as Mixer sub-agents (faster than KB in some regime)?

## Source

Surfaced in [[problems-people]] (internal project document). Not yet the subject of a Research/ paper note — no published paper in docs/papers/ covers this topic.

If Lead routes this for deeper research: Kaplansky's original 1948 paper; recent survey by Linnell "Zero divisors and group von Neumann algebras"; Gräter et al. for constructive approaches.
