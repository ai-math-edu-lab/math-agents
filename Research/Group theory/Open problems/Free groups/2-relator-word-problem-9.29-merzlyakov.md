---
title: "Do 2-relator groups with insoluble word problem exist? (Merzlyakov, Kourovka 9.29)"
authors:
  - "Yu.I. Merzlyakov"
year_posed: 1984
venue: "Kourovka Notebook, 9th Issue (1984)"
url: ""
source_path: "docs/papers/Kourovka 2022.pdf"
language: en
domain: group-theory
methodology_type: theoretical
relevance: 3
key_concepts: []
extends: []
contradicts: []
replicates: []
cites:
  - "[[kourovka-2022]]"
cited_by: []
quality_notes: "Merzlyakov calls this a 'well-known problem' in 1984, suggesting it was circulating before the 9th issue. No solution in Kourovka 2022. The old score/1 (low Mixer relevance) is migrated to relevance: 3 (low) per F4.2 decisions. Included in the catalog because it defines a decidability-landscape boundary, not because the Mixer can attack it."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/decidability
  - topic/finitely-presented-groups
  - paper
  - status/draft
---

# Do 2-relator groups with insoluble word problem exist? (Merzlyakov, Kourovka 9.29)

## Abstract

> "(Well-known problem). According to a classical theorem of Magnus, the word problem is soluble in 1-relator groups. Do there exist 2-relator groups with insoluble word problem?" — Yu.I. Merzlyakov, Kourovka Notebook, 9th issue (1984)

## TL;DR

Magnus (1932) proved all 1-relator groups have decidable word problem. General finitely presented groups can have undecidable word problem (Novikov-Boone 1955–57). Whether the threshold is 1 or 2 relators is unknown. Open as of Kourovka 2022.

## Problem

The **word problem** for a finitely presented group G = ⟨X | R⟩: given a word w in X ∪ X⁻¹, decide if w =_G e. Equivalently: is w in the normal closure of R?

**Known boundary:**
- 1-relator groups: word problem always **decidable** (Magnus 1932, using Freiheitssatz + induction on word length).
- General finitely presented groups: word problem **undecidable** in general (Novikov 1955, Boone 1957).
- **2-relator groups: unknown.** The simplest open case.

## Approach

No constructive attack in the problem. Relevant methods:

- **KB completion:** If KB terminates for a 2-relator group → word problem decidable for that group. Non-termination → inconclusive.
- **Magnus's Freiheitssatz:** The proof strategy for 1-relator groups depends on structural properties (Freiheitssatz) that do not obviously extend to 2 relators.
- **Undecidability constructions:** To disprove — construct a specific 2-relator group with undecidable word problem. Requires a novel computability-theory argument; no current avenue.

## Key result

- **1-relator groups decidable:** Magnus (1932). Foundational.
- **General FPGs undecidable:** Novikov (1955), Boone (1957).
- **2-relator case open** as of Kourovka 2022.

## Assumptions

- Magnus's theorem is assumed established (1932).
- Novikov-Boone undecidability is assumed established.

## Limitations / scope

- KB non-termination is not equivalent to word problem undecidability.
- The Mixer has essentially no attack vector on this problem:
  - KB can confirm decidability for specific 2-relator groups (finite sample, not general).
  - Proving decidability for ALL 2-relator groups requires extending Magnus's structural argument — not a search or verification task.
  - Proving undecidability requires constructing a counterexample — requires deep computability theory, not Mixer machinery.
- This note is included in the catalog to define a decidability landscape boundary, not because the Mixer can attack it.

## Replication evidence

N/A — open problem.

## Why this paper matters

This problem sets a boundary on what KB-based tools can claim: the Mixer can prove decidability for specific groups it solves but cannot answer the general question about 2-relator groups. Understanding this boundary prevents overclaiming — any Mixer result that successfully solves a 2-relator group's word problem is a specific instance contribution, not a resolution of 9.29.

## Quotes

> "According to a classical theorem of Magnus, the word problem is soluble in 1-relator groups." — Merzlyakov, Problem 9.29 (framing)

## Open questions surfaced

- Does Magnus's Freiheitssatz extend to 2-relator groups? (Key structural question for proving decidability.)
- Are there 2-relator groups where KB consistently diverges across all orderings? (A dataset of such divergence behavior, while not proving undecidability, would be suggestive negative evidence.)

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[kourovka-2022]]
- Cited by (in vault): (none currently)
