---
title: "Word Problem — Directory Map"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - convention
  - status/draft
---

# Word Problem — Directory Map

This directory covers the word problem in finitely presented groups as a topic: decidability, specific algorithmic techniques, and target word methodology.

## Contents

| File | Scope |
|---|---|
| `decidability-landscape.md` | The word problem statement; Novikov-Boone undecidability for FPGs; decidability results for specific families (free, abelian, hyperbolic, automatic). Verbatim theorem citations. |
| `target-words.md` | What a "target word" is in our methodology (stated generally); how to construct one; how to verify equality. |
| `techniques/` | One note per technique: Knuth-Bendix completion, Dehn function, automatic groups via finite-state automata. Cross-linked to `Tools/GAP/examples/` and `Tools/KBMAG/examples/` where applicable. |

## What does NOT live here

- Tool-specific code → `Tools/GAP/` or `Tools/KBMAG/`
- Foundational group definitions → `General/basics/`
- Paper summaries about specific word-problem results → `Open problems/` or `Burnside groups/`

## Status

Content populated in F6.2.

## Related material

- [[group-theory-overview]] — parent: Research/Group theory/ directory map
- [[_moc-word-problem]] — the word-problem MOC (this overview is the entry point; MOC is the reading path)
- [[decidability-landscape]] — core content: what's decidable and what's not
- [[target-words]] — core content: what target words are and how to verify them
- [[knuth-bendix]] — main technique: KB completion as word-problem algorithm
- [[dehn-function]] — technique: Dehn function and hyperbolic groups
- [[automatic-groups]] — technique: automatic group structure
