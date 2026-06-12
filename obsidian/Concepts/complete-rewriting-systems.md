---
title: Complete Rewriting Systems
author: ethan-k
language: en
tags:
  - agent/research
  - user/ethan-k
  - domain/group-theory
  - topic/complete-rewriting-systems
  - topic/knuth-bendix
  - topic/confluence
  - topic/word-problem
  - concept
  - status/draft
introduced_in:
  - "[[Research/Group theory/Word Problem/knuth-bendix-1970]]"
related_concepts:
  - "[[kb-mixing-stagnation]]"
appears_in:
  - "[[Research/Group theory/Word Problem/le-chenadec-1986]]"
  - "[[Research/Group theory/Word Problem/gilman-1979]]"
  - "[[Research/Group theory/Word Problem/hermiller-shapiro-1999]]"
  - "[[Research/Group theory/Word Problem/epstein-holt-rees-1991]]"
  - "[[Research/Group theory/Word Problem/epstein-sanders-2000]]"
  - "[[Research/Group theory/Word Problem/knuth-bendix-1970]]"
  - "[[Research/Group theory/Word Problem/epstein-et-al-1992-word-processing]]"
---

# Complete Rewriting Systems

> **Concept hub.** Multiple paper summaries link here via their `key_concepts` frontmatter. Keep it short and authoritative; detailed discussion belongs in the paper notes.

## Definition

A rewriting system $E$ over an alphabet $A$ is **complete** (a.k.a. confluent + terminating) if every string has a *unique* irreducible residue under $E$ — equivalently, $E$ is both terminating (relative to a reduction ordering, so every reduction sequence halts) and confluent (any two reduction paths from a word can be brought back together). When $E$ is complete, its normal forms are canonical representatives of the elements of the presented monoid/group, so the word problem is solved by reduce-and-compare.

## Why it matters

A complete rewriting system turns the word problem from an undecidable-in-general question into a finite computation: reduce both words to normal form and check equality. The Knuth–Bendix procedure ([[Research/Group theory/Word Problem/knuth-bendix-1970]]) is the standard method for *trying* to build one by resolving overlaps (critical pairs) until local confluence holds — but it may diverge, and a finite complete system need not exist for a given presentation/ordering. Whole research lines turn on (a) cataloguing groups that *do* admit finite complete systems ([[Research/Group theory/Word Problem/le-chenadec-1986]], [[Research/Group theory/Word Problem/hermiller-shapiro-1999]]), (b) characterizing when the procedure terminates ([[Research/Group theory/Word Problem/gilman-1979]]), and (c) coping with the cases where it produces infinitely many rules ([[Research/Group theory/Word Problem/epstein-sanders-2000]]) or must be paired with automata ([[Research/Group theory/Word Problem/epstein-holt-rees-1991]]).

## Where it appears

- Introduced in: [[Research/Group theory/Word Problem/knuth-bendix-1970]]
- Appears in: see `appears_in` frontmatter
- Related concepts: [[kb-mixing-stagnation]] (the practical failure mode — stagnation/divergence of completion)

## Open questions

- For which presentations does a finite complete rewriting system exist (independent of ordering)?
- When it does not, what is the right weaker target (e.g. an automatic structure, or an infinite but regular rule set)?

## References

1. Sims, C.C. (1994). *Computation with Finitely Presented Groups*. Cambridge University Press.
2. Epstein et al. (1992). *Word Processing in Groups*. Jones and Bartlett.
