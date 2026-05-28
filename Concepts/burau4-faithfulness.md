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

## Source

Surfaced in [[problems-people]] (internal project document listing algorithm-implementer assignments). Not yet the subject of a Research/ paper note — no published paper in docs/papers/ covers this topic.

If Lead routes this for deeper research, relevant papers include: Bigelow (1999) "The Burau representation is not faithful for n=5"; Long-Paton (1993) for n≥6; open question status confirmed in e.g. Birman "Braids, Links, and Mapping Class Groups" (textbook).
