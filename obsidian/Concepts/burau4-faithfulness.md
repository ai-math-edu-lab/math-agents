---
title: "Burau₄ Faithfulness — Candidate Mixer Domain"
domain: group-theory
project: none
status: draft
author: maumayma
related:
  - "[[problems-people]]"
introduced_in:
  - "[[Research/Group theory/Open problems/Braid groups/burau4-faithfulness]]"
appears_in:
  - "[[Research/Group theory/Open problems/Braid groups/burau4-faithfulness]]"
  - "[[Research/Group theory/Open problems/Braid groups/braid-b4-membership-6.24-makanin]]"
  - "[[Research/Group theory/Open problems/Braid groups/bigelow-1999]]"
  - "[[Research/Group theory/Open problems/Braid groups/long-paton-1993]]"
  - "[[Research/Group theory/Open problems/Braid groups/datta-2022]]"
related_concepts: []
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/braid-groups
  - topic/word-problem
  - concept
  - status/draft
---

# Burau₄ Faithfulness — Candidate Mixer Domain

Flagged as a Mixer candidate in [[problems-people]]. Implementation listed as Borys Nolikov.

## The problem

The **Burau representation** is a family of linear representations of the braid groups B_n over ℤ[t, t⁻¹]:

```
β_i ↦ (n×n matrix over ℤ[t,t⁻¹])
```

The **faithfulness question** asks: is the map B_n → GL(n,ℤ[t,t⁻¹]) injective? I.e., does the matrix image determine the braid?

**Known status:**
- B_2, B_3: Burau representation is faithful.
- B_n for n ≥ 5: Burau representation is **not faithful** (Bigelow 1999, Long-Paton 1993).
- **B_4: open.** This is the only remaining case.

The faithfulness of Burau₄ would imply the word problem in B_4 is decidable via matrix equality over ℤ[t,t⁻¹] — already decidable, but Burau₄ faithfulness would give a clean structural proof.

## Why Mixer-shaped

The word problem in braid groups B_n is decidable (Garside normal form, among others), but the algorithmic complexity varies by approach. This mirrors the KB / coset enumeration / Gröbner landscape for group-word problems. A Mixer could:

- Run Garside-form reduction and Burau-representation check in parallel.
- Use the Burau check as a fast-fail filter: if matrices differ, the words differ (regardless of faithfulness).
- If faithfulness holds, Burau is a complete filter — the equivalence oracle.

This is structurally identical to the quotient-test framework in [[grobner]]: a partial "No" oracle running alongside a complete rewriter.

## What this is NOT

- This is not an active project (no experiment note exists, no B25/B43/B53 connection).
- The Burau₄ faithfulness question is independent of the Burnside problem.
- Do not conflate braid groups with Burnside groups despite both being "word problem + group theory."

## Open questions for Mixer application

1. What representation of braid words makes them compatible as Mixer input alongside KB-style rules?
2. Can a Burau-based filter be made fast enough to be useful (matrix multiplication over polynomial rings)?
3. Does unfaithfulness of Burau₄ (if proved) close off this approach entirely, or do other braid-group representations remain useful?

## Sources (acquired in B2 — June 2026)

The stub ("written from general knowledge") has been replaced with verbatim cites:

- **[[bigelow-1999]]** — Bigelow (1999), *Geometry & Topology* 3:397-404 (arXiv: math/9904100). Proves $\psi_5$ unfaithful ("not faithful for $n > 4$"). Abstract retrieved verbatim. **Note**: the original vault stub incorrectly listed the venue as J. Amer. Math. Soc. — correct venue is Geometry & Topology.
- **[[long-paton-1993]]** — Long & Paton (1993), *Topology* 32(2):439-447. Proves $\psi_n$ unfaithful for $n \geq 6$. Source paywalled (pre-arXiv); content from authoritative knowledge.
- **[[datta-2022]]** — Datta (2022), arXiv:2209.10826. Proves $\beta_4$ is "faithful almost everywhere" — partial result, not a proof of faithfulness. The most significant post-2020 progress. Abstract retrieved verbatim.
- Bibliographic only (no standalone note): Burau (1936), German, *Abh. Math. Sem. Univ. Hamburg* 11:179-186 — original definition; Birman (1974) textbook "Braids, Links, and Mapping Class Groups" — survey status.

**Kourovka Notebook**: No problem number assigned to Burau₄ faithfulness (confirmed from vault note `open-problems-catalog.md`).

## Combinatorial search framing (Part A / Part B bridge)

The Burau₄ faithfulness question can be attacked as a **combinatorial-search problem**:

1. **Kernel search**: enumerate short words in $B_4$ and check whether $\beta_4(b) = I_{3\times 3}$ (the identity matrix). This is decidable (matrix equality over $\mathbb{Z}[q^{\pm 1}]$). If any short word gives identity, faithfulness is disproved.

2. **Datta's filter as partial-No oracle**: [[datta-2022]] proves that any kernel element must satisfy strong algebraic constraints on its Burau matrix entries. This is a fast "partial-No" oracle — for most braids, one can quickly certify they are NOT in the kernel without full matrix computation.

3. **Garside normal form as the search basis**: the braid word enumeration proceeds through Garside normal form, giving a canonical short-form for each braid equivalence class. This makes the search space tractable for short braids.

This framing connects directly to [[Research/Algorithm Cooperation/_synthesis-combinatorial-search-methods]] § 7: the Datta filter is a "partial-No oracle" in the same architectural sense as CEGAR counterexamples or ManySAT learned clauses — it prunes the search space without solving the full problem.
