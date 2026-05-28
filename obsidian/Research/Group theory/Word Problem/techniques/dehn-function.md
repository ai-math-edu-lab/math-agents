---
title: "Dehn Function and Isoperimetric Inequalities"
author: maumayma
language: en
source: "Bridson & de la Harpe, Metric Spaces of Non-Positive Curvature (1999), Part III; Gersten (1992)"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/finitely-presented-groups
  - status/draft
---

# Dehn Function and Isoperimetric Inequalities

## Overview

The **Dehn function** δ_G(n) measures the worst-case complexity of the word problem in G = ⟨X | R⟩: it is the maximum number of relator applications needed to demonstrate that a word w of length ≤ n is the identity.

Formally, for w representing e in G: there is a van Kampen diagram over G (a planar diagram whose boundary is labeled by w, whose 2-cells are labeled by relators). The Dehn function is the minimal area needed over all such van Kampen diagrams, maximized over all words of length ≤ n.

*Source: Bridson-de la Harpe, Part III; Gersten (1992), "Dehn functions and l₁ norms of finite presentations."*

## Why it matters

The Dehn function is the geometric encoding of the word problem's complexity:

| Dehn function | Class | Word problem |
|---|---|---|
| ≤ n (linear) | Hyperbolic groups | Decidable in O(n) time (Dehn algorithm) |
| ≤ n² (quadratic) | Automatic groups | Decidable in O(n²) time |
| ≤ exp(n) (exponential) | Various FPGs | Still decidable, possibly slow |
| No recursive bound | — | Word problem undecidable |

**Key theorem (Dehn, for surface groups; Gromov for hyperbolic groups):** A finitely presented group has a linear Dehn function iff it is hyperbolic. *Corollary:* hyperbolic groups have decidable word problem solvable in linear time.

## Dehn's algorithm

For a hyperbolic group G with Dehn function ≤ Cn:

1. If |w| = 0: w = e, done.
2. Find a subword u of w such that u is a prefix/suffix of some relator r with |u| > |r|/2.
3. Replace u in w with the remaining part r·u⁻¹ (which is shorter since |r·u⁻¹| < |r|/2 < |u|).
4. Repeat until |w| = 0 or no cancellation applies.

This terminates in O(n) steps for hyperbolic groups.

## Status

This note is a brief overview. Full treatment (van Kampen diagrams, NP-hardness results for specific Dehn functions, the Bridson-Pittet theorem, etc.) is in the references above. See also `Tools/GAP/examples/` for practical word-reduction in specific groups.

## Related material

- [[word-problem-overview]] — parent directory map for Word Problem subtree
- [[_moc-word-problem]] — the word-problem MOC that surfaces this technique
- [[decidability-landscape]] — where Dehn function fits in the full decidability picture (hyperbolic → linear Dehn function)
- [[knuth-bendix]] — sibling technique: KB completion as an alternative word-problem algorithm
- [[automatic-groups]] — sibling technique: automatic structure generalizes Dehn's algorithm to quadratic time
