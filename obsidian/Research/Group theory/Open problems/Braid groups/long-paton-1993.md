---
title: "The Burau representation is not faithful for n ≥ 6"
authors: D.D. Long, M. Paton
year: 1993
venue: "Topology 32(2):439-447"
url: "https://www.sciencedirect.com/science/article/pii/004093839390030Y"
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
cites: []
cited_by:
  - "[[bigelow-1999]]"
quality_notes: "source-text-incomplete-paywalled-pre-arxiv. Topology (Elsevier, 1993) — paywalled. PDF found at https://web.math.ucsb.edu/~long/pubpdf/Burau_n6.pdf but not text-extractable (binary PDF). Content summarized from authoritative knowledge of this widely-cited paper + Bigelow (1999) abstract which describes the approach. This paper is immediately superseded in scope by [[bigelow-1999]] (which proves n=5 unfaithful, giving n≥5 together with this paper). Both are cited together in all subsequent literature."
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
---

# The Burau representation is not faithful for n ≥ 6

## Abstract

*(Not retrieved verbatim — paywalled pre-arXiv paper. Content from authoritative knowledge + Bigelow's description.)*

Proves that the Burau representation $\psi_n : B_n \to \mathrm{GL}(n-1, \mathbb{Z}[t,t^{-1}])$ is NOT faithful for $n \geq 6$, by improving on Moody's earlier result (which proved unfaithfulness for $n > 8$). The proof constructs an explicit **simple closed curve on the 6-punctured disc** with specific homological properties that yield a non-trivial element in $\ker(\psi_6)$. By the inclusion $B_n \hookrightarrow B_{n+1}$ (braid subgroup embedding), unfaithfulness for $n=6$ implies unfaithfulness for all $n \geq 6$.

## TL;DR

Proves Burau unfaithful for $n \geq 6$ by constructing a kernel element in $B_6$ using a closed curve on the 6-punctured disc. Improved on Moody's (n > 8) bound. Immediately superseded in scope by [[bigelow-1999]] (n=5). Historical stepping stone to Bigelow's result.

## Problem

Same as [[bigelow-1999]]: for which $n$ is the Burau representation faithful? This paper addresses the boundary case after Moody established $n > 8$.

## Approach

**Geometric / homological** (same framework as [[bigelow-1999]]): construct a simple closed curve on the 6-punctured disc $D_6$ with certain homological properties. The Burau representation acts on $H_1$ of the $n$-punctured disc with local $\mathbb{Z}[t,t^{-1}]$-coefficients. A braid that fixes such a curve up to isotopy but whose Burau matrix is non-identity gives a kernel element.

The key technical contribution: Long and Paton's specific curve for the 6-punctured disc (as opposed to Bigelow's later 5-punctured disc construction).

## Key result

**Theorem**: The Burau representation $\psi_n$ is NOT faithful for all $n \geq 6$.

**Historical chain:**
- Moody: unfaithful for $n > 8$
- **Long-Paton 1993**: unfaithful for $n \geq 6$ ← this paper
- Bigelow 1999: unfaithful for $n \geq 5$ ← [[bigelow-1999]]
- **Open**: $n = 4$

## Assumptions

- Standard topological interpretation of the Burau representation via $H_1(D_n, \mathbb{Z}[t,t^{-1}])$.
- The braid subgroup embedding $B_6 \hookrightarrow B_n$ (for $n > 6$) propagates unfaithfulness upward.

## Limitations / scope

- Proves unfaithfulness for $n=6$ (and thus $n \geq 6$ by subgroup embedding).
- Does not address $n=4$ or $n=5$.

## Replication evidence

Cited in [[bigelow-1999]] as immediate predecessor. The framework (closed-curve approach) is the same in both papers. Long-Paton's result is universally accepted.

## Why this paper matters

Long-Paton 1993 is the **predecessor to Bigelow's keystone result**. It introduced the closed-curve / 6-punctured-disc approach that Bigelow adapted to the 5-punctured disc. For the current vault:

1. **Historical context**: establishes the chain of improvements that isolates $n=4$ as the last open case.
2. **Methodology**: the closed-curve approach is explicitly cited by Bigelow — understanding it helps understand Bigelow's proof.
3. **Combinatorial search framing**: Long-Paton's kernel element in $B_6$ is an explicit braid word — it IS a combinatorial object. The search for an analogous kernel element in $B_4$ is the combinatorial-search formulation of the open problem. [[_synthesis-combinatorial-search-methods]] covers the search methodology for finding such witnesses.

## Quotes

*(Abstract not retrieved verbatim — paywalled pre-arXiv source.)*

## Open questions surfaced

- Can Long-Paton's 6-punctured-disc construction be adapted to the 4-punctured disc? (Bigelow succeeded for the 5-punctured disc; the 4-punctured disc may be harder or impossible due to fewer topological degrees of freedom.)

## Related material in vault

- Concept hub: [[Concepts/burau4-faithfulness]]
- Cited by: [[bigelow-1999]] (which improves this result from n≥6 to n≥5)
- Post-2020 progress: [[datta-2022]]
- Synthesis: [[Research/Group theory/Open problems/Braid groups/_synthesis-burau4-faithfulness]] (forthcoming in B3)
