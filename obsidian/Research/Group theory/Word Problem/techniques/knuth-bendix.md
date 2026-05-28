---
title: "Knuth-Bendix Completion"
author: maumayma
language: en
source: "Knuth & Bendix (1970); Sims, Computation with Finitely Presented Groups (1994), Ch. 2; KBMAG Manual (Holt)"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/knuth-bendix
  - topic/kbmag
  - topic/word-problem
  - topic/finitely-presented-groups
  - status/validated
related:
  - "[[coset-enumeration]]"
---

# Knuth-Bendix Completion

## Overview

**Knuth-Bendix (KB) completion** is an algorithm that, given a term rewriting system (a set of equations E over an ordered set of terms), attempts to produce a **complete** (confluent and terminating) rewriting system E* equivalent to E. In group theory, the input is a group presentation G = ⟨X | R⟩ viewed as a rewriting system over words in X ∪ X⁻¹.

A **complete (confluent + terminating) rewriting system** for G:
- Assigns a canonical (normal) form to every word.
- Two words represent the same group element iff they have the same normal form.
- Gives a **decision procedure for the word problem** of G.

*Historical source: Knuth & Bendix, "Simple word problems in universal algebras" (1970).*

## Rewriting systems for groups

**Ordering:** A **reduction ordering** ≻ on words in X ∪ X⁻¹ that is well-founded and compatible with concatenation. Common choices:
- **Shortlex:** shorter words first; ties broken lexicographically.
- **Recursive path ordering (RPO):** based on a total order on generators; shorter results preferred.
- **Weighted lex (wtlex):** like shortlex but generators have weights.

**Rewriting rule:** A pair (l, r) with l ≻ r (l rewrites to r — the "larger" word rewrites to the "smaller"). Applied left-to-right, anywhere in a word.

**Confluence:** The system is **confluent** if whenever w rewrites to u and w rewrites to v (by different rules), u and v both reduce to the same word. Equivalently, every word has a unique normal form.

**Termination:** The system **terminates** if no word can be rewritten infinitely. This follows from the well-foundedness of ≻.

## The algorithm

1. **Initialize:** Convert each relator r ∈ R into a rewriting rule: orient as (l, r) with l ≻ r. If l = r, discard (the relator is trivially satisfied).

2. **Critical pairs:** For each pair of rules (l₁, r₁), (l₂, r₂), compute overlaps — subwords where l₁ and l₂ can be simultaneously applied. Each overlap produces a "critical pair" (two normal forms that should be equal).

3. **Reduce critical pairs:** Reduce both sides of each critical pair to normal form (by the current rules). If they are different, add a new rule orienting the difference. If equal, the critical pair is "resolved."

4. **Interreduce:** Simplify existing rules using newly added rules. Discard redundant rules.

5. **Repeat** until no new critical pairs are generated (system is complete) or until a resource bound is exceeded.

## Termination and completeness

- **If KB terminates:** The output is a complete rewriting system for G. The word problem for G is now decidable: reduce any word to normal form and check if it is the empty word.
- **If KB diverges:** Either the system generates infinitely many rules, or rules grow unboundedly. This can happen even for finite groups (with a bad ordering) or always happens for infinite groups that lack a finite complete rewriting system.

**Key theorem (Knuth-Bendix completeness theorem):** If a complete rewriting system exists for G under ordering ≻, and if KB terminates, then KB produces it.

## Orderings — practical notes

- **Shortlex:** safe (well-founded, easy to implement), tends to produce small rules but can diverge on groups with exponential growth.
- **RPO:** better at handling non-abelian groups; may produce larger rules but converge more often.
- **Mixing orderings (the Mixer approach):** run both shortlex and RPO simultaneously, sharing discovered rules between agents — see [[Research/Algorithm Cooperation/algo-mixing-burnside-slides]] for the B(4,3) breakthrough.

## In practice

- **KBMAG standalone:** `kbprog <inputfile.kbprog>` — see `Tools/KBMAG/examples/01-s3-shortlex.md` for a verified example.
- **KBMAG via GAP:** `LoadPackage("kbmag"); KnuthBendix(R)` — see `Tools/GAP/examples/05-kbmag-package.md`.

## Related concepts

- [[coset-enumeration]] — an alternative approach; KB is sometimes faster (especially for infinite groups where coset enumeration diverges).
- [[Research/Group theory/Burnside groups/B25/havas-wall-wamsley-1974]] — source of the B(2,5) relators that KB operates on.
