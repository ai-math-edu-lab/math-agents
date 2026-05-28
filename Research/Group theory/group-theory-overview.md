---
title: "Research/Group theory — Directory Map"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - convention
  - status/validated
---

# Research/Group theory — Directory Map

This directory holds all group theory research for the Math vault. Updated by Researcher when new subtrees are added (restructure authority).

## Subtree structure

| Directory | Scope |
|---|---|
| `Burnside groups/` | Paper summaries and notes on the Burnside group family (B(m,n)), with `B25/` for the 2-generator exponent-5 case |
| `Open problems/` | Open problem notes from the Kourovka Notebook and related sources, organized by problem domain (Burnside groups/, Braid groups/, Free groups/, Group rings/) |
| `General/` | Foundational group theory: definitions, presentations, finiteness. Textbook-level content, domain-foundational (no project scoping). See `General/general-group-theory-overview.md` for scope vs Word Problem vs Tools. |
| `Word Problem/` | The word problem in finitely presented groups: decidability landscape, target word methodology, algorithmic techniques (KB, Dehn function, automatic groups) |
| `Tools/` | Tooling docs for GAP and KBMAG: runnable code examples, file format references, decision tree for which tool to use |

## Scope rules

- `General/` is for textbook-style group theory (definitions, theorems, constructions) — NOT project-specific, NOT algorithmic methodology.
- `Word Problem/` is for the word problem as a topic: decidability, specific algorithms, the concept of "target words."
- `Tools/` is for tooling: how to run GAP/KBMAG for specific tasks, with verbatim verified code.
- Paper summaries go under the topically correct subfolder (Burnside groups/, Open problems/). NOT in General/, Word Problem/, or Tools/.

## Last restructured

2026-05-28 by Researcher (F6.1 Phase 6). Added `General/` subdirs, `Word Problem/`, `Tools/`, deleted stub `General/Include.md`.

## Related material

- [[_moc-burnside]] — curated reading path for Burnside groups and the B(2,5) program
- [[_moc-knuth-bendix]] — curated reading path for Knuth-Bendix completion and tooling
- [[_moc-word-problem]] — curated reading path for word problem decidability and techniques
- [[_moc-presentations-and-orders]] — curated reading path for group presentations and order computation
- [[_synthesis-existing-papers]] — cross-paper synthesis of all Research/Group theory/ papers (updateable)
- [[group-theory-tools-overview]] — decision tree for which tool (GAP / KBMAG) for which task
- [[word-problem-overview]] — directory map for Word Problem subtree
