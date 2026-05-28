---
title: "Representation Variety (SL(n,K) representations of a finitely presented group)"
author: maumayma
language: en
introduced_in:
  - "[[Research/Algorithm Cooperation/grobner]]"
appears_in:
  - "[[Research/Algorithm Cooperation/grobner]]"
related_concepts:
  - "[[grobner-quotient-filter]]"
  - "[[grobner-infinitude-probe]]"
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

# Representation Variety

> **Concept hub.** Extracted from inline content in [[Research/Algorithm Cooperation/grobner]] (Kreuzer-Myasnikov-Rosenberger 2025). Singleton for now — hub promoted to avoid content loss during F4.3 migration.

## Definition

The **representation variety** V_R of a finitely presented group G = ⟨X | R⟩ is the algebraic variety of all group homomorphisms φ: G → SL(n,K) for a field K:

$$V_R = \{ (A_1,...,A_s) \in SL(n,K)^s \mid r(A_1,...,A_s) = I_n \text{ for all relators } r \in R \}$$

This is an affine algebraic variety defined by polynomial equations derived from the relators (the same equations that define I_R in the universal linear representation ring Q_R = ℤ[T]/I_R).

The coordinate ring of V_R over K is K[T]/I_R·K[T] — exactly the ring used in the [[grobner-quotient-filter]] construction.

Source: §3-4 in [[Research/Algorithm Cooperation/grobner]]; the universal representation ring Q_R is the coordinate ring of V_R (Proposition 4.2).

## Why it matters

The representation variety provides a **geometric coordinate system** on the group's structure. Points in V_R are representations of G; the Zariski topology on V_R reflects the algebraic relationships between representations.

In the Gröbner-basis approach ([[grobner-quotient-filter]]), working with Gröbner bases of I_R is equivalent to computing algebraic geometry operations on V_R. This gives a structured space of "certificates" for group properties:
- A non-identity certificate (word w ≠ 1) corresponds to a representation where φ(w) ≠ I_n.
- An infiniteness certificate corresponds to a representation with an element of infinite order.

For the **Mixer**, the representation variety is a candidate scoring/ordering space: given a large rule set in KB, the variety provides additional algebraic structure that might inform which rules to prioritize. This is a speculative Mixer integration direction (not yet implemented or tested).

## Where it appears

- Introduced in: [[Research/Algorithm Cooperation/grobner]] (§3-4)
- Appears in: [[Research/Algorithm Cooperation/grobner]]
- Related concepts: [[grobner-quotient-filter]], [[grobner-infinitude-probe]]

## Open questions

- Can the dimension of V_R (over ℚ or ℂ) be used as a proxy for group complexity — and thus as a Mixer scoring function for rule injection?
- For B(2,5): what does V_R look like? (Section 7.5 of [[Research/Algorithm Cooperation/grobner]] is incomplete; this is the key open computational question.)
- Is V_R irreducible for the Burnside groups? Irreducibility might simplify the Gröbner computation.
