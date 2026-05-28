---
title: "Gröbner Infinitude Probe"
author: maumayma
language: en
introduced_in:
  - "[[Research/Algorithm Cooperation/grobner]]"
appears_in:
  - "[[Research/Algorithm Cooperation/grobner]]"
related_concepts:
  - "[[grobner-quotient-filter]]"
  - "[[representation-variety]]"
tags:
  - agent/research
  - user/maumayma
  - domain/cs
  - topic/grobner-basis
  - topic/word-problem
  - topic/finitely-presented-groups
  - concept
  - status/draft
---

# Gröbner Infinitude Probe

> **Concept hub.** Extracted from inline content in [[Research/Algorithm Cooperation/grobner]] (Kreuzer-Myasnikov-Rosenberger 2025). Singleton for now — hub promoted to avoid content loss during F4.3 migration.

## Definition

A **Gröbner infinitude probe** is a test for whether a finitely presented group G is infinite, using the minimal polynomial of a matrix image of an element.

Given G = ⟨X | R⟩ and a matrix W = μ(w) ∈ Mat(n, K) for some element w ∈ G (where K = F[y₁,...,yₘ]/I is an affine algebra over a field F):

1. Form the module U from W − z·Iₙ and I·Kⁿ.
2. Compute the annihilator of U in F[y₁,...,yₘ, z] using Gröbner methods.
3. Restrict to F[z] to get the minimal polynomial of W.
4. **If minimal polynomial is 0:** W has infinite order in GL(n,K) → G is infinite.

Source: Algorithm 6.2 in [[Research/Algorithm Cooperation/grobner]] (§6). A faster heuristic version (Algorithm 6.4) checks whether diagonal entries of W^N generate a non-nilpotent ideal.

## Why it matters

Proving that a finitely presented group is infinite is fundamentally harder than proving finiteness (KB completion proves finiteness; nothing proves infiniteness directly via KB). The Gröbner infinitude probe provides a **positive infiniteness certificate** for specific elements, without requiring KB to run.

In Mixer terms: if the probe detects an infinite-order element early, a KB Mixer agent can be abandoned before wasting resources on a non-terminating run. This is the Gröbner analog of "early stopping" in KB.

The probe is most useful when the group is suspected to be infinite (e.g., during experiments that run KB for a long time without convergence) — it provides a definitive answer in the other direction.

## Where it appears

- Introduced in: [[Research/Algorithm Cooperation/grobner]] (§6, Algorithm 6.2)
- Appears in: [[Research/Algorithm Cooperation/grobner]]
- Related concepts: [[grobner-quotient-filter]], [[representation-variety]]

## Open questions

- For B(2,5): if KB diverges, can the infinitude probe confirm that B(2,5) is infinite? (This would resolve Kourovka Problem 11.48.)
- What is the computational cost of the minimal polynomial computation for large groups at n=2?
- Can the probe be combined with KB in a Mixer to provide early stopping: run KB until a threshold, then run the probe?
