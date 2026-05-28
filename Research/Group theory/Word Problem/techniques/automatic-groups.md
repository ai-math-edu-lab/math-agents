---
title: "Automatic Groups and Finite-State Automata"
author: maumayma
language: en
source: "Epstein, Cannon, Holt, Levy, Paterson, Thurston, Word Processing in Groups (1992)"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/finitely-presented-groups
  - status/draft
---

# Automatic Groups and Finite-State Automata

## Definition

A group G is **automatic** (with respect to generating set S) if there exists:

1. A **regular language** L ⊆ (S ∪ S⁻¹)* such that the natural map L → G (each word in L maps to an element of G) is surjective (every element of G has at least one representative in L).
2. For each generator s ∈ S ∪ S⁻¹ ∪ {e}, a **finite-state automaton** (the "s-multiplier automaton") that recognizes the set of pairs (u, v) ∈ L × L such that the elements represented by u and v differ by right-multiplication by s.

Informally: L is a "dictionary" of normal forms for G, and the multiplier automata certify that the dictionary is consistent under right-multiplication by generators. The key constraint is that all the multiplier automata must be **finite-state**.

*Source: Epstein et al., Word Processing in Groups (1992), Ch. 2.*

## Why it matters

**Theorem:** Automatic groups have a decidable word problem solvable in O(n²) time (quadratic in the word length).

**Word problem algorithm:** Given w ∈ (S ∪ S⁻¹)*, use the multiplier automata to reduce w to its representative in L; two words represent the same group element iff they have the same representative in L.

The O(n²) bound is nearly optimal for this approach (linear time requires hyperbolicity and Dehn's algorithm).

## Which groups are automatic?

- **All hyperbolic groups** (stronger condition).
- **All abelian groups** (automatic with respect to any generating set).
- **Mapping class groups of surfaces** (Mosher 1995).
- **Artin groups of finite type** (including braid groups Bₙ — automatic via the Garside normal form).
- **Coxeter groups** (Epstein et al.).

**Non-automatic:**
- **ℤ × ℤ × ℤ** is automatic (it's abelian).
- **Certain nilpotent groups of class ≥ 3** — NOT automatic (Bridson-Gersten).
- **Groups with undecidable word problem** — cannot be automatic.

## KBMAG and automatic groups

The KBMAG tool `autgroup` computes the automatic structure (the multiplier automata) for groups where it exists:

```sh
autgroup <groupfile.kbprog>
```

If `autgroup` terminates, it certifies the group is automatic and provides the multiplier automata. If it diverges, the group may still be automatic (but `autgroup` failed to find the structure), or the group may not be automatic.

See `Tools/KBMAG/kbmag-tools-overview.md` for the path to the `autgroup` binary.

## Status

This note is a brief overview. Full treatment of automatic group theory (geodesically automatic, strongly automatic, Cayley graph properties, Bridson-Gersten's non-automatic nilpotent groups) is in Epstein et al. (1992) and the references therein.

## Related material

- [[word-problem-overview]] — parent directory map for Word Problem subtree
- [[_moc-word-problem]] — the word-problem MOC that surfaces this technique
- [[decidability-landscape]] — where automatic groups fit: decidable in O(n²) time
- [[knuth-bendix]] — sibling technique: KB completion produces a canonical system (related to automatic structure)
- [[dehn-function]] — sibling technique: Dehn's algorithm for the special case of hyperbolic groups
- [[kbmag-tools-overview]] — KBMAG's autgroup binary computes automatic structures
