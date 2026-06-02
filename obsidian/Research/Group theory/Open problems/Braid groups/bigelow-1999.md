---
title: "The Burau representation is not faithful for n = 5"
authors: Stephen Bigelow
year: 1999
venue: "Geometry & Topology 3 (1999), pp. 397-404"
url: https://arxiv.org/abs/math/9904100
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date:
key_concepts:
  - "[[Concepts/burau4-faithfulness]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[long-paton-1993]]"
cited_by: []
quality_notes: "Published in Geometry & Topology (NOT J. Amer. Math. Soc. — the vault's prior stub had the wrong venue; this note corrects it). arXiv preprint math/9904100. Open access at https://projecteuclid.org/euclid.gt/1513883152. Abstract retrieved verbatim from arXiv. This paper settles n=5; together with [[long-paton-1993]] (n≥6) it gives unfaithfulness for all n≥5. The n=4 case remains open."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/braid-groups
  - topic/braid-representations
  - topic/word-problem
  - paper
  - status/draft
project: b25
---

# The Burau representation is not faithful for n = 5

## Abstract

"The Burau representation is a natural action of the braid group $B_n$ on the free $\mathbb{Z}[t,t^{-1}]$-module of rank $n-1$. It is a longstanding open problem to determine for which values of $n$ this representation is faithful. It is known to be faithful for $n=3$. Moody has shown that it is not faithful for $n>8$ and Long and Paton improved on Moody's techniques to bring this down to $n>5$. Their construction uses a simple closed curve on the 6-punctured disc with certain homological properties. In this paper we give such a curve on the 5-punctured disc, thus proving that the Burau representation is not faithful for $n>4$."

## TL;DR

Proves the Burau representation $\psi_n : B_n \to \mathrm{GL}(n-1, \mathbb{Z}[t,t^{-1}])$ is NOT faithful for $n=5$, by constructing an explicit element in $\ker(\psi_5)$: a simple closed curve on the 5-punctured disc satisfying required homological conditions. Together with Long-Paton's result ($n \geq 6$ unfaithful), this gives unfaithfulness for all $n \geq 5$. The $n=4$ case ([[Concepts/burau4-faithfulness]]) remains the unique open case.

## Problem

The Burau representation $\psi_n : B_n \to \mathrm{GL}(n-1, \mathbb{Z}[t,t^{-1}])$ assigns to each braid a matrix over the Laurent polynomial ring. Is $\psi_n$ injective (faithful)? Known: faithful for $n \leq 3$; unfaithful for $n \geq 6$ (Long-Paton 1993). The case $n=5$ was open before this paper.

## Approach

**Geometric approach** (following the Moody / Long-Paton framework):

The Burau representation can be interpreted topologically: $\psi_n$ acts on the homology of the $n$-punctured disc (with a local coefficient system). An element $\beta \in B_n$ is in $\ker(\psi_n)$ iff it acts trivially on this homology.

Bigelow constructs a specific **simple closed curve $\gamma$** on the 5-punctured disc $D_5 = D^2 \setminus \{p_1, p_2, p_3, p_4, p_5\}$ with the property that certain homological conditions force a braid $\beta \in B_5$ to fix $\gamma$ (up to homotopy) while $\psi_5(\beta) \neq I$. This gives a non-trivial kernel element.

The construction for $n=5$ is more delicate than Long-Paton's $n=6$ case because the disc has fewer punctures and fewer degrees of freedom in the homological argument.

## Key result

**Theorem**: The Burau representation $\psi_5 : B_5 \to \mathrm{GL}(4, \mathbb{Z}[t,t^{-1}])$ is NOT faithful.

**Consequence**: Combined with [[long-paton-1993]] (which proves $\psi_n$ unfaithful for $n \geq 6$), this gives:

$$\psi_n \text{ is faithful for } n \leq 3, \quad \psi_n \text{ is NOT faithful for } n \geq 5.$$

The case $n = 4$ is the **unique remaining open case**.

## Assumptions

- The topological interpretation of the Burau representation via the homology of the $n$-punctured disc (with local coefficients) is standard.
- The specific curve construction is verified in the paper.

## Limitations / scope

- Proves unfaithfulness for $n=5$ only; the paper does not address $n=4$.
- The proof constructs an element in $\ker(\psi_5)$ but does not explicitly compute it as a braid word (the construction is geometric, not algorithmic).

## Replication evidence

Published in Geometry & Topology (peer-reviewed). The result is universally accepted and cited. The Lawrence-Krammer-Bigelow representation (which Bigelow later proved faithful for all $n$) provides a complete word-problem solution, further validating the framework.

## Why this paper matters

Bigelow 1999 is the **keystone of the Burau₄ faithfulness open problem** — it resolves all cases except $n=4$, making the B₄ case the unique remaining question. For the vault:

1. **Problem scope**: confirms the current open problem is exactly $\ker(\psi_4) = ?$. Any kernel-element search over short braids in $B_4$ is a direct combinatorial-search attack on this problem.

2. **Combinatorial search framing** (Part A / Part B bridge): the proof for $n=5$ used a geometric construction, not a brute-force search. For $n=4$, both approaches are conceivable — a geometric/theoretical argument OR an exhaustive/heuristic search over short $B_4$ words to either find a kernel element or accumulate evidence of faithfulness. Datta 2022 ([[datta-2022]]) represents the "accumulate evidence" approach; Bigelow's 1999 approach represents the "construct a witness" approach.

3. **Venue correction**: the prior vault stub (`burau4-faithfulness.md`) listed the venue as "J. Amer. Math. Soc." — this is INCORRECT. The correct venue is **Geometry & Topology** 3 (1999). The paper is open-access via Project Euclid.

## Quotes

> "In this paper we give such a curve on the 5-punctured disc, thus proving that the Burau representation is not faithful for $n>4$." — Abstract

## Open questions surfaced

- Does a similar geometric construction exist for the 4-punctured disc? (If yes, Burau₄ is unfaithful; if provably impossible, it provides evidence for faithfulness.)
- Is there a braid word of bounded length in $B_4$ that lies in $\ker(\psi_4)$? (Computational search approach.)
- Can the Mixer's parallel search paradigm be used to search for kernel elements in $B_4$?

## Related material in vault

- Concept hub: [[Concepts/burau4-faithfulness]] (the open n=4 question this paper resolves for n=5)
- Predecessor: [[long-paton-1993]] (proved n≥6 unfaithful; Bigelow's paper improves to n=5)
- Post-2020 progress: [[datta-2022]] (proves B₄ "faithful almost everywhere" — partial result)
- Related problem: [[braid-b4-membership-6.24-makanin]] (B₄ membership as related hard problem)
- Synthesis: [[Research/Group theory/Open problems/Braid groups/_synthesis-burau4-faithfulness]] (forthcoming in B3)
