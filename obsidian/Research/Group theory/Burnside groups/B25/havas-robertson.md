---
title: "Application of Computational Tools for Finitely Presented Groups"
authors:
  - George Havas
  - Edmund F. Robertson
year: 1994
venue: "DIMACS Series in Discrete Mathematics and Theoretical Computer Science, Vol. 00"
url: ""
source_path: "docs/papers/Havas-Robertson.pdf"
language: en
domain: group-theory
methodology_type: review
relevance: 2
key_concepts:
  - "[[Concepts/verification-methods-for-group-equality]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[havas-newman-1980]]"
cited_by:
  - "[[grobner]]"
  - "[[kreuzer-et-al-2010]]"
quality_notes: "Survey of FPG computational methods via three worked examples. Not specific to B(2,5) — B(2,5) is mentioned only via ref [23] (havas-newman-1980). The KB section (§2.9) is the most directly relevant passage: cites Sims (1991) showing KB sometimes outperforms coset enumeration, which is the regime the Mixer exploits."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/coset-enumeration
  - topic/knuth-bendix
  - topic/finitely-presented-groups
  - paper
  - status/draft
---

# Application of Computational Tools for Finitely Presented Groups

Havas & Robertson (1994, DIMACS). Survey of computational methods for finitely presented groups, illustrated on three worked examples. **Not specific to B(2,5).**

## Abstract

> No verbatim abstract available — source is local PDF at `docs/papers/Havas-Robertson.pdf`. See TL;DR below.

## TL;DR

Describes a general strategy for unknown finitely presented groups — abelianize, iterate through the derived series, apply Reidemeister-Schreier to get kernel presentations, simplify with Tietze — using Todd-Coxeter, Knuth-Bendix, and Reidemeister-Schreier as interchangeable sub-tools; demonstrated on three worked examples, all resolved by 1993-era workstation.

## Problem

Given an unknown finitely presented group G = ⟨g₁,...,gd | R₁,...,Rn⟩, how can one determine its structure (order, derived series, quotients) using only stand-alone programs running on a workstation?

## Approach

General strategy: compute G/G′ (abelianization via Smith normal form). If nontrivial, iterate through the derived series. If trivial (G perfect), find finite quotients by adding low-power relations and running coset enumeration. In both cases, once a quotient G/H is found, apply Reidemeister-Schreier to get a presentation for H, simplify with Tietze, and repeat. The algorithm terminates when all factors are identified.

Key tools (per section):
- §2.1 Todd-Coxeter coset enumeration — enumerate cosets of subgroup H in G
- §2.3 Tietze transformation — simplify presentations without changing the group
- §2.7 Reidemeister-Schreier — derive a presentation for a subgroup from a presentation of G
- §2.9 Knuth-Bendix completion — complete rewriting system (sometimes outperforms coset enumeration for infinite groups where Todd-Coxeter diverges; cites Sims (1991) for this observation)

Programs ran on Sun workstations; outputs piped between them.

## Key result

Three worked examples fully resolved:

1. **G(2) = ⟨a,b | a⁶=b⁶=1, ab²=ba²⟩** — soluble of derived length 3; derived factors C₆, C₄², C₃^∞.
2. **G = ⟨a,b | a³=b⁵=(aba⁻¹b⁻¹ab²)²=1⟩** — proved infinite via abelian invariants of a subgroup.
3. **G = ⟨a,b | a³=b³¹=(...)²=...=1⟩** — identified as C₃ × SL(2,32) × SL(2,32).

Iterative quotient-kernel strategy works to index "well into the hundreds" for kernel subgroups.

KB (Sims 1991 [45]) noted as sometimes outperforming coset enumeration — especially for infinite groups where coset enumeration diverges.

## Assumptions

- Group is finitely presented (explicit generators and relators are known).
- Stand-alone programs are correct (Cayley, GAP, Magma existed but couldn't handle the full workflow at the time; paper uses custom stand-alone tools).
- Derived series terminates (applies when G is soluble or can be reduced to finite quotients).

## Limitations / scope

- Does not address B(2,5) specifically; B(2,5) is mentioned only via ref [23] ([[havas-newman-1980]]).
- For B(2,5), coset enumeration over the trivial subgroup requires 5^34 cosets — beyond this paper's regime.
- Written 1991/revised 1993; examples reflect 1990s computing constraints. Modern KB (kbmag, GAP) is substantially faster.
- Isomorphism testing described (Holt-Rees combining KB + structural difference detection) is noted as promising but not the primary focus.

## Replication evidence

Three worked examples are fully resolved within the paper by the described methodology. No independent external replication identified in this vault; the techniques are standard and in wide use.

## Why this paper matters

The iterative quotient-kernel approach describes the conceptual framework within which our B(2,5) work operates: applying multiple algorithm types (KB, coset enumeration, Reidemeister-Schreier) cooperatively on nested subproblems. Section §2.9 is the most directly relevant: KB cited as sometimes outperforming coset enumeration — exactly the regime where Mixer adds value by choosing between KB variants.

The paper's pipeline (abelianize → quotient → Reidemeister-Schreier → Tietze → repeat) is analogous to how Mixer chains algorithm agents on nested subproblems, though the Mixer's cooperation is finer-grained (rule injection at the sub-completion level, not just at the quotient-group level).

## Quotes

> No short verbatim quotes extracted — source is local PDF `docs/papers/Havas-Robertson.pdf`. See §2.9 for the KB vs. coset enumeration comparison (Sims citation).

## Open questions surfaced

- When exactly does KB outperform coset enumeration, and vice versa? The paper notes KB wins for some groups where Todd-Coxeter diverges, but the boundary is not characterized.
- Can the iterative quotient-kernel strategy be automated end-to-end? The paper describes it as requiring expert judgment at each step; automation is an open engineering problem.

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[havas-wall-wamsley-1974]] (as ref [23] via [[havas-newman-1980]]), [[havas-newman-1980]]
- Cited by (in vault): [[havas-wall-wamsley-1974]] (cross-referenced), [[havas-newman-1980]], [[grobner]] (lists as background)
