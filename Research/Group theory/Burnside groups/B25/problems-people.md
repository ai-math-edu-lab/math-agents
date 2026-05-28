---
title: "B(2,5) Problems and People (internal project document)"
authors:
  - "project team (Myasnikov, Stepanov, and others)"
year: 2025
venue: "Internal (algo_mixing project)"
url: ""
source_path: "docs/papers/Problems-people.docx"
language: en
domain: group-theory
methodology_type: methodology
relevance: 1
key_concepts: []
extends: []
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[grobner]]"
cited_by:
  - "[[kaplansky-zero-divisors]]"
  - "[[andrews-curtis-conjecture]]"
  - "[[grobner]]"
quality_notes: "Internal planning document, not a published paper. Undated; year 2025 is best-guess from project context. The list of implementers is a snapshot — team membership may have changed. Content extracted from .docx XML; complex table/column layouts may have been missed."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/word-problem
  - topic/knuth-bendix
  - topic/coset-enumeration
  - topic/mixer
  - topic/finitely-presented-groups
  - paper
  - status/draft
project: b25
---

# B(2,5) Problems and People

Internal project document (Word docx). Lists algorithms being applied to B(2,5) and related problems with named implementers; describes early Mixer architectural constraints.

## Abstract

> Internal document — no published abstract. The document is a project coordination artifact listing algorithm/problem assignments and design assumptions for the algo_mixing B(2,5) effort.

## TL;DR

Names the algorithms and implementers for the algo_mixing project's B(2,5) effort (KB variants, coset enumeration, Andrews-Curtis, Burau₄, Kaplansky) and states the Mixer's founding architectural constraints: API boundary between orchestrator and algorithm agents, no shared internal memory, serialization limitations, and "expertly-defined 'best'" as the transfer primitive.

## Problem

How should a mixed-algorithm system ("Mixer") be designed when the underlying algorithms (KB, Todd-Coxeter, Cayley-graph, Gröbner) have incompatible internal representations, are resource-hungry, and can't share instances?

## Approach

Project planning document, not a research paper. Lists algorithm/problem pairs and implementers:

| Algorithm | Problem | Implementer |
|---|---|---|
| Cayley Graph Approximation Algorithms (Search WP) | B(2,5) | Sasha Ushakov |
| Various Knuth-Bendix algorithms (Search WP) | B(2,5) | Andrey Nikolaev, Brett Berger, Ethan Kalika, Winston Lee |
| Coset Enumeration (Todd-Coxeter) | Burnside groups | Andrew Ginzburg |
| Andrews-Curtis via quotients G₂(q) | AC Conjecture | Vazgen Kirakosyan |
| Andrews-Curtis free group experiments | AC Conjecture | Alex Myasnikov |
| Burau₄ faithfulness | Braid groups | Borys Nolikov |
| Kaplansky zero-divisors | Group rings | Winston Lee |
| Automated theorem provers | B(2,5) + ATP | Alexei Lisitsa |

Mixer building team: Vlad Stepanov, Alex Myasnikov, Max, Masha.

## Key result

**Design constraints (verbatim from document):**

> "Current state might be too big to serialize/transfer as a whole"
> "We need some way to extract what's 'best' from each alg (expertly-defined 'best' for now)"
> "Algorithms can be too resource-hungry to share instances"
> "Central Mixer should not expect to have access to the Algorithm's memory, some API boundary is expected"
> "Different algorithms most likely will have different internal representations"
> "We can start with the ones that have the same reprs"
> "We will need to create some transformation layers"

## Assumptions

- "Expertly-defined 'best'" is a placeholder for a future formal transfer primitive — the document does not specify what this means algorithmically.
- Algorithms have incompatible internal representations; transformation layers are assumed feasible but not yet designed.
- The listed implementers were assigned at time of document creation; current team membership may differ.

## Limitations / scope

- Aspirational/planning document; cannot verify whether implementations were completed, partially done, or abandoned.
- No B(2,5) mathematical content — this is a coordination document, not a paper on the group theory.
- The Andrews-Curtis and Kaplansky entries are listed here without more detail — see [[andrews-curtis-conjecture]] and [[kaplansky-zero-divisors]] for mathematical analysis.

## Replication evidence

N/A — this is an internal planning document, not a reproducible research result.

## Why this paper matters

This document reveals the **scope, team, and architectural philosophy** of the algo_mixing project at its inception. Three things stand out:

1. **Alexei Myasnikov** appears both here (as Mixer builder and A-C implementer) and as co-author of [[grobner]] — confirming the Gröbner basis approach is part of the same intellectual agenda as the Mixer.

2. The **API boundary constraint** ("Central Mixer should not expect to have access to the Algorithm's memory") is the foundational motivation for the `mixer_core.Agent` protocol's design. This document predates the Rust implementation; the current `mixer-core/` codebase is the realization of these constraints.

3. **Multiple algorithm families** are listed as Mixer candidates — KB, coset enumeration, Cayley graph, Gröbner, ATP. The Mixer is not a KB-only tool; it is a generic cooperation framework first deployed with KB variants because those are most mature.

The **Cayley Graph Approximation Algorithms** (Ushakov's approach) and **automated theorem proving** (Lisitsa) are listed here but have no Research/ paper summaries yet — gap for future Researcher follow-up.

## Quotes

> "Central Mixer should not expect to have access to the Algorithm's memory, some API boundary is expected" — verbatim from document

> "We need some way to extract what's 'best' from each alg (expertly-defined 'best' for now)" — verbatim from document

## Open questions surfaced

- What was implemented? Which of the listed algorithm/implementer pairs produced working code? The document is aspirational; the current codebase state is the answer, but a cross-reference is missing.
- Cayley Graph Approximation Algorithms (Ushakov): no Research/ note exists. What is this approach, and does it have a Mixer-relevant formalization?
- "Expertly-defined 'best'": how is this now formalized in the `mixer_core.Agent` protocol?

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[havas-wall-wamsley-1974]] (B(2,5) as primary target), [[grobner]] (Myasnikov connection)
- Cited by (in vault): [[Research/Group theory/Open problems/open-problems-catalog]], [[Research/Group theory/Open problems/Braid groups/burau4-faithfulness]], [[Research/Group theory/Open problems/Free groups/andrews-curtis-conjecture]], [[Research/Group theory/Open problems/Group rings/kaplansky-zero-divisors]], [[grobner]], [[Concepts/burau4-faithfulness]], [[Concepts/kaplansky-zero-divisors]]
