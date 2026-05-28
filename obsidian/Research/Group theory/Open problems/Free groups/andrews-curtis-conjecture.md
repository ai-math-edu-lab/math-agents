---
title: "The Andrews-Curtis Conjecture (Andrews-Curtis, 1965)"
authors:
  - "J.J. Andrews"
  - "M.L. Curtis"
year_posed: 1965
venue: "Proc. Amer. Math. Soc. 16, 192–195"
url: ""
source_path: ""
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
  - "[[problems-people]]"
cited_by: []
quality_notes: "No source document in docs/papers/ — content written from general knowledge. Paper acquisition needed: Andrews-Curtis 1965 (Proc. Amer. Math. Soc. 16, 192–195); Akbulut-Kirby for potential counterexamples AK(n); Bridson examples. No classical Kourovka entry identified (18.89 is a related but different meta-question about ACₙ finitely presented?). Old score/2 migrated to relevance: 2 per F4.2 decisions. Source unavailable at 2026-05-28 re-fetch; content preserved from original note."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/finitely-presented-groups
  - paper
  - status/draft
---

# The Andrews-Curtis Conjecture (Andrews-Curtis, 1965)

## Abstract

> No source document available — content written from general knowledge. Paper acquisition needed: Andrews-Curtis 1965 (Proc. Amer. Math. Soc. 16, 192–195). See `quality_notes`.

## TL;DR

Every balanced presentation of the trivial group can be AC-reduced to the trivial presentation using a specific set of elementary moves. Open since 1965 and widely believed true; no counterexample has been found, but no general proof exists.

## Problem

A **balanced presentation** is ⟨x₁,...,xₙ | r₁,...,rₙ⟩ where #generators = #relators. A **balanced presentation of the trivial group** is one where every element equals e. **AC moves:**
1. Replace rᵢ with rᵢ⁻¹.
2. Replace rᵢ with rᵢrⱼ (j ≠ i).
3. Replace rᵢ with grᵢg⁻¹ for any word g.
4. Replace xᵢ with xᵢxⱼ (Nielsen move), simultaneously updating relators.

**Conjecture:** Starting from any balanced presentation of {e}, finitely many AC moves reduce it to ⟨x₁,...,xₙ | x₁,...,xₙ⟩ (the trivial presentation).

**Motivation:** Topological — an affirmative answer implies certain 4-dimensional handlebody equivalences. A counterexample would be a "trapped" presentation, revealing a topological obstruction.

## Approach

Computational search for AC-reduction sequences:
- **BFS/DFS over AC moves:** enumerate AC-move sequences, check whether each leads toward the trivial presentation.
- **Length-reduction heuristics:** AC-reducibility proofs often proceed by reducing total relator word length.
- **Mixer analogy:** Parallel search agents with different AC-move orderings + sharing of "useful intermediate states" — structurally identical to KB rule injection.

Named implementers in [[problems-people]]: Vazgen Kirakosyan (via quotients G₂(q)) and Alex Myasnikov (free group experiments).

## Key result

**Known:**
- AC conjecture open since 1965. Major candidate counterexamples: Akbulut-Kirby presentations AK(n) = ⟨x,y | x^{n+1} = y^n, xyx = yxy⟩, Bridson examples.
- Each time a researcher finds an AC-reduction for a candidate counterexample, the conjecture survives. No reduction has failed.
- Kourovka 18.89 (Swan, Lisitsa): related meta-question "Is ACₙ finitely presented?" — different from the classical conjecture.

## Assumptions

- AC-reducibility of a specific presentation is decidable (the question of decidability of AC-equivalence is itself open, but for fixed candidates, exhaustive search terminates if the conjecture holds for that instance).

## Limitations / scope

- Proving the conjecture for ALL balanced presentations of {e} is out of Mixer reach (requires a structural theorem).
- Proving a specific presentation is NOT AC-reducible requires exhaustive search over an infinite move space — in general not feasible.
- The Mixer can demonstrate specific reductions (if found) but cannot prove non-existence.

## Replication evidence

N/A — open problem. Computational searches have found reductions for many candidate counterexamples without disproving the conjecture.

## Why this paper matters

The AC conjecture is a natural search problem with a well-defined move set and a Mixer-friendly structure: multiple search agents can work in parallel on a shared presentation, sharing useful partial move sequences. The structural analogy to KB mixing (length-reducing vs. non-length-reducing moves, analogous to shortlex vs. RPO in KB) makes this a direct cross-domain test case for the Mixer methodology.

The connection to group theory is direct: the AC conjecture is about whether two presentations of the same (trivial) group can always be connected by elementary moves. It lives at the intersection of combinatorial group theory and low-dimensional topology.

## Quotes

> No verbatim quotes — no source document available.

## Open questions surfaced

- Are AK(1), AK(2), AK(3) AC-reducible? Systematic Mixer search over these specific presentations is a well-defined computational task.
- Is there a Mixer-style cooperation benefit for AC-move search analogous to KB rule injection?

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[kourovka-2022]] (Kourovka 18.89 related), [[problems-people]] (lists as Mixer candidate)
- Cited by (in vault): (none currently)
