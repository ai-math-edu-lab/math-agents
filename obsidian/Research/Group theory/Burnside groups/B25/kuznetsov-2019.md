---
title: "Computational experiments in finite two generator Burnside groups of exponent five"
authors: A. A. Kuznetsov
year: 2019
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/12/60
url_translated:
language: ru
methodology_type: empirical
citation_count: null
citation_count_date:
key_concepts:
  - "[[Concepts/cayley-table-closure-algorithm]]"
extends:
  - "[[kuznetsov-shlepkin-2009]]"
  - "[[kuznetsov-shlepkin-2010]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-shlepkin-2009]]"
  - "[[kuznetsov-shlepkin-2010]]"
cited_by: []
quality_notes: "source-text-incomplete-only-abstract-available. 3-page conference note (Prikl. Diskr. Mat. Suppl.). Original in Russian; abstract summary from mathnet.ru record. Citation count not retrievable (Semantic Scholar rate-limited; paper not indexed in English-language databases)."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/growth-functions
  - topic/cayley-graphs
  - topic/exponent-5
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: b25
---

# Computational experiments in finite two generator Burnside groups of exponent five

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record. Original text is not preserved; follow `url` for the source.

## Abstract

The paper examines $B_0(2,5)$, the largest two-generator Burnside group of exponent five with order $5^{34}$. Using a power commutator presentation, elements are uniquely represented as $a_1^{\alpha_1} \cdot a_2^{\alpha_2} \cdots a_{34}^{\alpha_{34}}$. The authors define quotient groups $B_k$ and conduct computational experiments, proposing a hypothesis about the diameter $D_{A_4}(B_k)$ relative to symmetric generating set $A_4 = \{a_1, a_1^{-1}, a_2, a_2^{-1}\}$. The hypothesis predicts $D_{A_4}(eN_k) = D_{A_4}(B_k)$ for all $2 \le k \le 34$, where sizes satisfy $|N_k| \sim |Q_k| \sim |B_k|^{1/2}$, verified computationally for $k \le 19$. [trans.]

## TL;DR

Studies the Cayley graph diameters of the 34 quotient groups $B_k$ of $B_0(2,5)$, proposes a half-group-size normal-subgroup diameter hypothesis, and verifies it computationally for the first 19 quotients. A 3-page conference note — hypothesis only, no proof; full paper text unavailable.

## Problem

What is the Cayley graph diameter of the quotient groups $B_k$ (the $k$-th lower central factor quotients of $B_0(2,5)$) relative to the symmetric generating set $A_4 = \{a_1, a_1^{-1}, a_2, a_2^{-1}\}$? And can the diameter $D_{A_4}(B_k)$ be recovered from a normal subgroup $N_k$ whose size is roughly $|B_k|^{1/2}$?

## Approach

Uses the power commutator presentation of $B_0(2,5)$ (33 generators $a_1, \ldots, a_{34}$, each $\alpha_i \in \mathbb{Z}_5$; established by [[havas-wall-wamsley-1974]]) to represent group elements. Defines a tower of quotient groups $B_k$ and a corresponding sequence of normal subgroups $N_k$. Computes $D_{A_4}(B_k)$ via direct Cayley graph construction for $k \le 19$ and compares with $D_{A_4}(eN_k)$ (diameter of the coset $eN_k$ in the full group $B_k$). Full methodology details not available (abstract-only access).

## Key result

**Hypothesis (computationally verified for $2 \le k \le 19$):** $D_{A_4}(eN_k) = D_{A_4}(B_k)$, where $N_k$ is a normal subgroup of $B_k$ with $|N_k| \sim |Q_k| \sim |B_k|^{1/2}$.

If true for all $k \le 34$, this would give a polynomial-in-$|B_k|^{1/2}$ strategy for computing group diameters. The paper reports the hypothesis as unproved at the time of writing.

## Assumptions

- Works with $B_0(2,5)$ (the restricted Burnside group of order $5^{34}$), not the free Burnside group $B(2,5)$ whose finiteness is open.
- Uses the Hall–Wamsley power commutator representation from [[havas-wall-wamsley-1974]]; assumes this is the correct normal form.
- Verification is computational (k ≤ 19 only); the hypothesis is unproven for $k > 19$.

## Limitations / scope

- Hypothesis is stated, not proved. No proof strategy is offered (abstract-only access).
- Results cover $B_k$ for $k \le 19$ of 34 total layers; the full tower is not yet verified.
- Applies to $B_0(2,5)$, not to $B(2,5)$; no direct contribution to finiteness of $B(2,5)$.

## Replication evidence

No independent replication known as of 2026-05-28. Abstract-only source; no published follow-up located in vault.

## Why this paper matters

This is one of Kuznetsov's mid-period papers on the computational geometry of $B_0(2,5)$, bridging the 2009–2010 Cayley-table-closure work ([[kuznetsov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]]) and the 2021–2025 papers on subgroups and the center. The growth-function / diameter thread connects to the broader question of how large the Cayley graph of $B(2,5)$ would be if infinite — a diagnostic relevant to choosing injection targets for the Mixer bidirectional pipeline.

The $|N_k| \sim |B_k|^{1/2}$ hypothesis, if proved, would give a structural shortcut for diameter computation: instead of spanning the full group, the diameter is recoverable from a subgroup of half the order. This kind of "half-group witness" is the sort of sublinear handle that could make Mixer experiments on $B_0(2,5)$ more tractable.

## Quotes

Abstract-only access; no verbatim quotes extracted from body text.

## Open questions surfaced

- Does the hypothesis $D_{A_4}(eN_k) = D_{A_4}(B_k)$ hold for all $2 \le k \le 34$? Computationally verifiable for $20 \le k \le 34$ using the same power commutator multiplication.
- What is the rate of growth of $D_{A_4}(B_k)$ as $k \to 34$? If it grows roughly as $k^c$, that bounds the complexity of generating rules for the full $B_0(2,5)$.
- Does an analogous half-group diameter result hold for the free $B(2,5)$ quotient towers (if $B(2,5)$ is finite)?

## Related material in vault

- Extends: [[kuznetsov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]] (prior computational work on $B_0(2,5)$ by same author)
- Cites: [[havas-wall-wamsley-1974]] (power commutator presentation of $B_0(2,5)$)
- Concepts: [[Concepts/cayley-table-closure-algorithm]] (the same algorithmic line; this paper studies Cayley graph geometry built on top of that representation)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]] (broader context for B(2,5) computational work)
