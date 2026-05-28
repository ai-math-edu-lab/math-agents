---
title: "Target Words in Group Theory Computation"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/finitely-presented-groups
  - status/validated
---

# Target Words in Group Theory Computation

## What is a target word?

A **target word** is a specific element of a finitely presented group G — expressed as a word in the generators — whose identity or non-identity in G is the object of a computation. The term is used in computational group theory to distinguish specific elements of interest (which may be complex commutators, products of conjugates, or other algebraically natural elements) from generic word-problem instances.

**Typical questions about a target word w:**
1. Does w = e in G? (Word problem)
2. What is the minimal-length word representing the same element as w? (Compression / normal form)
3. Is w in a specific subgroup H ≤ G? (Membership problem)

## How to construct a target word

### From the lower central series (commutators)

The most common target words in Burnside group computation come from the **lower central series** γᵢ(G).

**Left-normed commutator notation:**
- [x, y] = x⁻¹y⁻¹xy
- $[x, y, z] = [[x, y], z]$
- $[x_1, x_2, ..., x_n] = [[x_1, x_2, ..., x_{n-1}], x_n]$

In a free group F = F(a,b), the basic commutators are canonically ordered by weight. The Hall basis elements of weight k are the building blocks of γₖ(F)/γₖ₊₁(F).

**Example (B(2,5) generator 12):** In the standard Havas-Wall-Wamsley 1974 presentation of B(2,5) (using generators 1=a, 2=b):

```
Generator 12 = [2, 1, 2, 1, 1, 2]     (weight 6)
             = `[[[[[[2,1], 2], 1], 1], 2]]`
```

Generator 9 = [2,1,2,1,1] (weight 5). Then:

```
comm_12_9 = [generator_12, generator_9]   (weight 12 = maximum class of B(2,5))
          = [c₁₂, c₉]
```

This is the target word in the B(2,5) bidirectional search experiments.

### From a group presentation

Given G = ⟨X | R⟩ and a specific algebraic property of interest, a target word is typically constructed by:
1. Writing down the element in terms of generators.
2. Expanding all commutators and conjugations into products.
3. Reducing freely (canceling xx⁻¹ pairs).

## How to verify equality

### Method 1: Confluent KB rewriting system (KBMAG)

If a complete rewriting system for G is available, reduce w to its normal form. The normal form is e iff w = e in G.

```sh
# Reduce a word using a confluent kbprog output:
kbprog -wr <confluent-system.kbprog> <word>
```

**Advantage:** Exact, fast for systems with a manageable number of rules.
**Limitation:** Requires KB to terminate — not available for all groups.

See `Tools/KBMAG/examples/` for concrete usage.

### Method 2: GAP oracle (for small groups)

For finite groups of order computable by GAP:

```gap
gap> F := FreeGroup("a", "b");;
gap> G := F / [relator1, relator2, ...];;  # your group presentation
gap> ga := G.1;; gb := G.2;;
gap> w := ga*gb*ga;;                        # your target word in G
gap> w = Identity(G);                       # test for identity
```

**Advantage:** No KB required; GAP handles the computation internally.
**Limitation:** Only feasible for groups where `Order(G)` terminates (small finite groups).

See `Tools/GAP/examples/03-word-equality.md`.

### Method 3: Abelianization check (necessary condition only)

The abelianization G/[G,G] is a quotient; equality in G implies equality in G/[G,G]. For elements of interest, compute the exponent vector modulo n (for groups of exponent n). If the abelianization of w is non-zero, then w ≠ e.

**This is a necessary condition, not sufficient.** Non-identity abelianization → w ≠ e. Zero abelianization → w may or may not equal e.

**Example (B(2,5)):** Every element has an "abelian vector" (a-exponent mod 5, b-exponent mod 5). Target words like comm_12_9 (a weight-12 commutator) have abelian vector (0,0) — they are in the kernel of abelianization, so the abelianization check cannot distinguish them from e.

## Compression and normal-form length

For long target words (tens of thousands of characters), compression before reduction is essential:

1. **Identify repetitive structure:** Look for long repeated subwords (e.g., the X-core in comm_13_10: X = `ABabAbabABaBAbabABABabAbaBABaBAbabb` appears 34 times).
2. **Introduce a substitution:** Let m = X⁻¹bX (if meaningful in G). The target word 2500 chars compresses to 260 chars.
3. **Reduce in the compressed alphabet:** Rules from the KB system may apply more efficiently in the compressed form.

## Cross-references

- `Tools/GAP/examples/03-word-equality.md` — GAP word equality testing
- `Tools/KBMAG/examples/` — KBMAG word reduction
- [[Research/Group theory/Burnside groups/B25/havas-wall-wamsley-1974]] — source of the B(2,5) generator numbering
- [[Research/Group theory/Word Problem/decidability-landscape.md]] — when word equality is decidable
