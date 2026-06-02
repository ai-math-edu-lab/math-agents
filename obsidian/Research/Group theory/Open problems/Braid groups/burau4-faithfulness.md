---
title: "Is the Burau representation of B₄ faithful? (Open)"
authors:
  - "W. Burau"
year_posed: 1936
venue: "Well-known open problem in braid group theory"
url: ""
source_path: ""
language: en
domain: group-theory
status: draft
methodology_type: theoretical
relevance: 2
key_concepts:
  - "[[Concepts/burau4-faithfulness]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[braid-b4-membership-6.24-makanin]]"
  - "[[bigelow-1999]]"
  - "[[long-paton-1993]]"
  - "[[datta-2022]]"
cited_by: []
quality_notes: "B2 acquisition complete (June 2026). Papers now in vault: [[bigelow-1999]] (Geometry & Topology 3:397-404, 1999; arXiv math/9904100 — VENUE CORRECTED from prior stub which incorrectly listed J. Amer. Math. Soc.), [[long-paton-1993]] (Topology 32(2):439-447, 1993; source-text-incomplete-paywalled-pre-arxiv), [[datta-2022]] (arXiv 2209.10826, 2022 — post-2020 partial result). Bibliographic only: Burau 1936 (German, pre-digital), Birman 1974 textbook. No Kourovka Notebook problem number (confirmed from vault). Old score/2 migrated to relevance: 2 per F4.2."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/braid-groups
  - topic/word-problem
  - paper
  - status/draft
---

# Is the Burau representation of B₄ faithful? (Open)

## Abstract

> No source document — content written from general knowledge. The Burau representation faithfulness question for n=4 is a well-known open problem; no single canonical paper poses it (it arises as the remaining case after Bigelow (1999) resolved n≥5). See `quality_notes` for paper acquisition list.

## TL;DR

The Burau representation ψₙ: Bₙ → GL(n, ℤ[t,t⁻¹]) is faithful for n ≤ 3, unfaithful for n ≥ 5. Whether ψ₄ is injective — the B₄ faithfulness question — is the unique remaining open case, unsolved since Burau defined the representation in 1936.

## Problem

**Burau representation (Burau, 1936):** A family of linear representations of braid groups:
$$\psi_n: B_n \to GL(n, \mathbb{Z}[t, t^{-1}])$$

**Faithfulness question:** Is ψ₄ injective? Equivalently: is the kernel of ψ₄ trivial?

If ψ₄ is faithful: two braids in B₄ are equal iff their Burau matrices are equal — a decidable test (matrix equality over ℤ[t,t⁻¹]).

If ψ₄ is unfaithful: there are distinct braids with equal matrices — Burau cannot detect them (though the word problem in B₄ is already decidable by other means via Garside normal form).

## Approach

No constructive proof in either direction is known. Relevant approaches:

1. **Search for kernel elements:** If a non-trivial element of B₄ is found in ker(ψ₄), faithfulness is disproved. Systematic search is a beam-search / exhaustive-enumeration task.
2. **Structural proof:** Faithfulness would require a structural theorem about the representation — no current approach known.
3. **Mixer hybrid:** Garside reduction + Burau-matrix comparison as concurrent agents. Even without knowing faithfulness, Burau is a useful fast-fail filter (different matrices → certainly different braids).

## Key result

**Known faithfulness status:**

| n | Faithfulness | Source |
|---|---|---|
| 1, 2, 3 | Faithful | Classical |
| 5 | Unfaithful | [[bigelow-1999]] (Geometry & Topology 3:397-404) |
| ≥ 6 | Unfaithful | [[long-paton-1993]] (Topology 32(2):439-447) |
| **4** | **Open** (faithful "almost everywhere" — [[datta-2022]], 2022) | — |

## Assumptions

- Bigelow (1999) and Long-Paton (1993) results assumed established (not independently verified in this vault — paper acquisition listed in `quality_notes`).
- Garside normal form solves the word problem for all Bₙ (established, Garside 1969).

## Limitations / scope

- Proving faithfulness requires a structural theorem; disproving requires finding a kernel element. Neither path is accessible via KB / Garside / search alone without a much deeper structural insight.
- Relationship to membership problem: if ψ₄ is faithful, it directly assists with the membership problem ([[braid-b4-membership-6.24-makanin]]); if unfaithful, the gap remains.

## Post-2020 progress

**Datta (2022)** — [[datta-2022]] arXiv 2209.10826 — "The Burau representation of $B_4$ is faithful almost everywhere." Establishes that any element of $\ker(\beta_4)$ must satisfy strong algebraic constraints on its Burau matrix entries (derived via Garside normal form + matrix cancellation theory). Proves the representation is faithful for "generic" braids. This is the most significant partial result as of 2026. Still open whether $\ker(\beta_4)$ is trivial.

## Replication evidence

Bigelow (1999) [[bigelow-1999]] and Long-Paton (1993) [[long-paton-1993]]: universally accepted, independently cited. Datta (2022) [[datta-2022]]: arXiv preprint, peer-review status TBC as of June 2026.

## Why this paper matters

B₄ faithfulness and the B₄ membership problem ([[braid-b4-membership-6.24-makanin]]) together define the "B₄ frontier": the collection of open questions about the 4-string braid group, where B₄ is the exceptional case lying just below the undecidability threshold (n ≥ 5). The Mixer's Garside + Burau hybrid is directly relevant to B₄ word-problem and membership-problem instances regardless of the faithfulness outcome: Burau as fast-fail filter, Garside as complete oracle.

Named implementer in [[problems-people]]: Borys Nolikov.

## Quotes

> No verbatim quotes — no source document available. See `quality_notes` for paper acquisition list.

## Open questions surfaced

- Does ker(ψ₄) contain any non-trivial element? (If yes: ψ₄ unfaithful; disproof by construction.)
- If ψ₄ is proved faithful: does this directly yield a polynomial-time membership algorithm for B₄?
- Systematic search of short braids in B₄ for kernel elements: feasible computational task.

## Combinatorial search framing (Part A / Part B bridge)

The Burau₄ faithfulness question, when viewed computationally, is a **kernel-element search problem**:

- **Complete oracle**: enumerate braids $b \in B_4$ and check $\beta_4(b) = I_3$ (matrix equality over $\mathbb{Z}[q^{\pm 1}]$; decidable but expensive for long braids).
- **Partial-No oracle (Datta 2022)**: [[datta-2022]] shows that any kernel element must satisfy strong entry constraints. For most short braids, these constraints fail immediately — a fast "No" without computing the full matrix. This is the **partial-No oracle pattern** from [[Research/Algorithm Cooperation/_synthesis-combinatorial-search-methods]] § 7.
- **Garside normal form**: provides a canonical enumeration of braid equivalence classes by length. Search proceeds shortest-first.

The Mixer analog: Datta's filter running alongside the full matrix-equality check is exactly "CEGAR where spurious counterexamples are braids that aren't in the kernel" — see [[Research/Algorithm Cooperation/clarke-et-al-2000-cegar]].

## Related material in vault

- Cites (in vault): [[bigelow-1999]], [[long-paton-1993]], [[datta-2022]], [[braid-b4-membership-6.24-makanin]]
- Concepts: [[Concepts/burau4-faithfulness]]
- Cited by (in vault): [[problems-people]] (names implementer Borys Nolikov)
- Algorithm Cooperation: [[Research/Algorithm Cooperation/_synthesis-combinatorial-search-methods]] (partial-No oracle pattern)
- Synthesis: [[Research/Group theory/Open problems/Braid groups/_synthesis-burau4-faithfulness]] (forthcoming)
