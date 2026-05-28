---
title: Growth functions of Burnside group quotients
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/growth-functions
  - topic/cayley-graphs
  - topic/burnside
  - topic/finite-group-enumeration
  - concept
  - status/draft
introduced_in:
  - "[[kuznetsov-2016]]"
related_concepts:
  - "[[Concepts/cayley-graphs-of-burnside-groups]]"
  - "[[Concepts/cayley-table-closure-algorithm]]"
appears_in:
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-karchevsky-2016]]"
  - "[[kuznetsova-kuznetsov-safonov-2013]]"
  - "[[kuznetsov-kuznetsova-2018]]"
  - "[[kuznetsov-2019]]"
  - "[[kuznetsov-safonov-2018]]"
  - "[[kuznetsov-kuznetsova-2017]]"
  - "[[kuznetsov-2015-cayley-exp3]]"
---

# Growth functions of Burnside group quotients

> **Concept hub.** Multiple papers in the Kuznetsov B(2,5) line compute growth functions of the quotient groups $B_k$ of $B_0(2,5)$. This hub gives the shared definition and cross-paper view.

## Definition

For a finitely generated group $G$ with symmetric generating set $S$, the **growth function** (or **spherical growth function**) is:

$$f_S(k) = |\{g \in G : d_S(e, g) = k\}|$$

where $d_S(e, g)$ is the word metric — the minimum length of a word over $S \cup S^{-1}$ representing $g$.

In the Kuznetsov program, $G = B_k = B_0(2,5,k)$ (the $k$-th lower central quotient of $B_0(2,5)$, of order $5^k$), and $S$ is one of two standard generating sets:
- **2-generator**: $\{a_1, a_2\}$
- **4-generator (symmetric)**: $A_4 = \{a_1, a_1^{-1}, a_2, a_2^{-1}\}$

The **Cayley graph diameter** is:

$$D_S(G) = \max_k \{k : f_S(k) > 0\}$$

The **average diameter** is $\bar{D}_S(G) = \frac{\sum_k k \cdot f_S(k)}{|G|}$.

## Why it matters

Growth functions characterize the **word geometry** of the group — how elements spread through the Cayley graph by distance from the identity. For the Mixer's B(2,5) attack:

1. **Diameter bound on KB rules**: a confluent KB system for $B_0(2,5)$ must be able to reduce any word of length $\le D_{A_4}(B_0(2,5))$ to normal form. The estimated diameter ~105 (2-gen) and ~69 (4-gen) from [[kuznetsov-kuznetsova-2018]] bound the word-length horizon the Mixer must reach.
2. **Bidirectional search window**: the optimal meet-in-the-middle window in the Mixer's bidirectional B(2,5) pipeline is approximately $D / 2$ from each end. For $D \approx 69$ (4-gen), the search window is ~35 per direction.
3. **Calibration benchmarks**: growth function values for small quotients ($B_{15}$, $B_{16}$, $B_{17}$, $B_{18}$, $B_{19}$) are verifiable benchmarks for any B(2,5) pipeline — any tool that can enumerate $B_k$ elements should reproduce these values.

Without growth function data, the Mixer team has no quantitative handle on the word-length scale of B(2,5) exploration.

## Where it appears

- Introduced in: [[kuznetsov-2016]] (first systematic BFS growth function algorithm for $B_k$)
- Appears in: [[kuznetsov-karchevsky-2016]], [[kuznetsova-kuznetsov-safonov-2013]], [[kuznetsov-kuznetsova-2018]], [[kuznetsov-2019]], [[kuznetsov-safonov-2018]], [[kuznetsov-kuznetsova-2017]], [[kuznetsov-2015-cayley-exp3]]
- Related concepts: [[Concepts/cayley-graphs-of-burnside-groups]] (the graph-theoretic object whose diameter is measured), [[Concepts/cayley-table-closure-algorithm]] (a different but related enumeration approach)

## Open questions

- **Exact growth function for $B_{34} = B_0(2,5)$**: currently only estimated (~105 and ~69 for the two generating sets). Direct computation would require extending the 2018 algorithm to k=34 — orders of magnitude harder.
- **Growth rate across quotients**: does $D_{A_4}(B_k)$ grow linearly in $k$? If yes, extrapolation to $k=34$ from $k=19$ would give a more precise estimate than the current ~69/105.
- **Exponent-5 vs. exponent-3 comparison**: [[kuznetsov-2015-cayley-exp3]] shows exponent-3 Burnside Cayley graphs beat hypercubes. Does this hold for exponent-5?

## References

1. Kuznetsov, A.A. (2016). *An algorithm for computation of the growth functions in finite two-generated groups of exponent 5*. Prikl. Diskr. Mat. 3(33). See [[kuznetsov-2016]].
2. Kuznetsov, A.A. & Kuznetsova, A.S. (2018). *A resource-efficient algorithm for study the growth in finite two-generator groups of exponent 5*. Prikl. Diskr. Mat. 42. See [[kuznetsov-kuznetsova-2018]]. [Contains the diameter estimates ~105 and ~69.]
