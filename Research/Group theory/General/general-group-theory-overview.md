---
title: "General Group Theory — Scope and Map"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - convention
  - status/draft
---

# General Group Theory — Scope and Map

## What lives here

Foundational group theory: definitions, constructions, and structural theorems at textbook level. Content is **domain-foundational** — not scoped to any project or algorithm.

| Subdir | Contents |
|---|---|
| `basics/` | Core definitions: group, subgroup, homomorphism, kernel, normal subgroup, quotient, group action. One short note per concept. |
| `presentations-and-relations/` | Free groups, presentations ⟨X \| R⟩, Tietze transformations, coset enumeration (Todd-Coxeter overview), Cayley graphs. |
| `orders-and-finiteness/` | Order notation, finite vs infinite groups, exponent, torsion, classification of finite simple groups (one-page pointer). |
| `_synthesis-existing-papers.md` | Cross-paper synthesis of all Group theory papers in this vault (updateable — refresh on every `/research --reconnect group-theory` pass). |

## What does NOT live here

- Algorithmic word problem approaches → `Word Problem/techniques/`
- Tool-specific content (GAP/KBMAG) → `Tools/`
- Paper summaries → `Burnside groups/`, `Open problems/`
- Project-scoped notes → stay in their project's experiment folders

## Status

Content under `basics/`, `presentations-and-relations/`, and `orders-and-finiteness/` is populated in F6.2. This overview defines scope.

## Related material

- [[group-theory-overview]] — parent: top-level Research/Group theory/ directory map
- [[_moc-presentations-and-orders]] — the MOC covering group presentations, coset enumeration, and order computation
- [[_synthesis-existing-papers]] — cross-paper synthesis of all Research/Group theory/ papers
- [[word-problem-overview]] — the Word Problem subtree (scope complementary to General/)
