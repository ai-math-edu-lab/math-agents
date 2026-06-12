---
title: "On the growth functions of finite two generator Burnside groups of exponent five"
authors: A. A. Kuznetsov, S. S. Karchevsky
year: 2016
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/9/52
url_translated:
language: ru
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[kuznetsov-2016]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-2016]]"
cited_by: []
quality_notes: "source-text-incomplete-only-abstract-available. 4-page conference note (Prikl. Diskr. Mat. Suppl. 9, pp. 132–135). Original in Russian. Likely the conference-note companion to [[kuznetsov-2016]] (full journal paper in Prikl. Diskr. Mat. 3(33) by same first author in same year). Both report growth functions for k=15,16,17. Different co-author (Karchevsky here vs. sole author in pdm554); may reflect different experimental contributions or be a split publication."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/growth-functions
  - topic/exponent-5
  - paper
  - status/draft
project: b25
---

# On the growth functions of finite two generator Burnside groups of exponent five

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The researchers examine the largest two-generator Burnside group of exponent 5, denoted $B_0(2,5)$, which has order $5^{34}$. Using a power commutator presentation, each group element is uniquely represented with 34 generators (the first two being standard generators, the remainder being recursively defined commutators). They define quotient groups $B_k$ with order $5^k$ and present a new algorithm for computing the growth function of $B_k$ relative to two different generating sets, calculating growth functions for $k = 15, 16, 17$. [trans.]

## TL;DR

Conference note reporting growth functions of $B_k$ for $k = 15, 16, 17$ (same result as [[kuznetsov-2016]]). Likely a companion publication to the full journal paper; the second author Karchevsky may have contributed the implementation or analysis.

## Problem

Same as [[kuznetsov-2016]]: compute growth functions of $B_k$ quotients of $B_0(2,5)$ for small $k$.

## Approach

Same power commutator representation as [[kuznetsov-2016]]. Growth functions computed for $k = 15, 16, 17$ relative to $\{a_1, a_2\}$ and $\{a_1, a_1^{-1}, a_2, a_2^{-1}\}$.

## Key result

Growth functions of $B_{15}$, $B_{16}$, $B_{17}$ for two generating sets. Same results as [[kuznetsov-2016]] (abstract is identical in substance).

## Assumptions

Same as [[kuznetsov-2016]].

## Limitations / scope

- Conference note (4 pages); algorithm details likely in [[kuznetsov-2016]].
- Same scope limitation: $k \le 17$.

## Replication evidence

[[kuznetsov-2016]] provides the full treatment; this note is a corroborating publication.

## Why this paper matters

This note confirms the $k = 15, 16, 17$ growth function results with a second co-author (Karchevsky), adding slight independent corroboration. For vault purposes, its primary value is that it cites the same method and adds a co-author name that may appear in follow-up work.

## Quotes

Abstract-only access; no verbatim body-text quotes.

## Open questions surfaced

See [[kuznetsov-2016]].

## Related material in vault

- Extends: [[kuznetsov-2016]] (full journal version of the same result)
- Cites: [[havas-wall-wamsley-1974]], [[kuznetsov-2016]]
- Related: [[kuznetsov-kuznetsova-2018]] (resource-efficient extension to k=18,19)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
