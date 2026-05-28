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
methodology_type: theoretical
relevance: 2
key_concepts:
  - "[[Concepts/burau4-faithfulness]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[braid-b4-membership-6.24-makanin]]"
cited_by: []
quality_notes: "No source document in docs/papers/ for this problem. Content written from general knowledge. Paper acquisition needed: Bigelow 1999 (J. Amer. Math. Soc., proves n≥5 unfaithful); Long-Paton 1993 (proves n≥6); Birman 'Braids, Links, and Mapping Class Groups' for status survey. No Kourovka Notebook problem number identified for Burau₄ faithfulness. Old score/2 migrated to relevance: 2 per F4.2 decisions. Source unavailable at 2026-05-28 re-fetch; content preserved from original note."
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
| 5 | Unfaithful | Bigelow (1999), J. Amer. Math. Soc. |
| ≥ 6 | Unfaithful | Long-Paton (1993) |
| **4** | **Open** | — |

## Assumptions

- Bigelow (1999) and Long-Paton (1993) results assumed established (not independently verified in this vault — paper acquisition listed in `quality_notes`).
- Garside normal form solves the word problem for all Bₙ (established, Garside 1969).

## Limitations / scope

- Proving faithfulness requires a structural theorem; disproving requires finding a kernel element. Neither path is accessible via KB / Garside / search alone without a much deeper structural insight.
- Relationship to membership problem: if ψ₄ is faithful, it directly assists with the membership problem ([[braid-b4-membership-6.24-makanin]]); if unfaithful, the gap remains.

## Replication evidence

N/A — open problem. Bigelow (1999) and Long-Paton (1993) results for n ≥ 5 not verified in this vault.

## Why this paper matters

B₄ faithfulness and the B₄ membership problem ([[braid-b4-membership-6.24-makanin]]) together define the "B₄ frontier": the collection of open questions about the 4-string braid group, where B₄ is the exceptional case lying just below the undecidability threshold (n ≥ 5). The Mixer's Garside + Burau hybrid is directly relevant to B₄ word-problem and membership-problem instances regardless of the faithfulness outcome: Burau as fast-fail filter, Garside as complete oracle.

Named implementer in [[problems-people]]: Borys Nolikov.

## Quotes

> No verbatim quotes — no source document available. See `quality_notes` for paper acquisition list.

## Open questions surfaced

- Does ker(ψ₄) contain any non-trivial element? (If yes: ψ₄ unfaithful; disproof by construction.)
- If ψ₄ is proved faithful: does this directly yield a polynomial-time membership algorithm for B₄?
- Systematic search of short braids in B₄ for kernel elements: feasible computational task.

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[braid-b4-membership-6.24-makanin]] (related open problem, B₄ frontier)
- Cited by (in vault): [[Concepts/burau4-faithfulness]], [[problems-people]] (names implementer)
