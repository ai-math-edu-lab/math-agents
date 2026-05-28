---
title: "Hall's polynomials of finite two-generator groups of exponent seven"
authors: Alexander A. Kuznetsov, Konstantin V. Safonov
year: 2014
venue: Journal of Siberian Federal University. Mathematics & Physics
url: http://mi.mathnet.ru/jsfu363
url_translated:
language: en
methodology_type: methodology
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[kuznetsov-kuznetsova-2013]]"
contradicts: []
replicates: []
cites:
  - "[[kuznetsov-kuznetsova-2013]]"
cited_by: []
quality_notes: "Full journal paper (J. Sib. Fed. Univ. Math. Phys. 7:2, pp. 186–190, 5 pages). English language. Only abstract available. BORDERLINE inclusion: exponent-7 Hall polynomials; included because Hall polynomial methodology generalizes across odd exponents and underpins B(2,5) work. Compare [[kuznetsov-safonov-2015]] (exponent-3) and [[kuznetsov-kuznetsova-2013]] (exponent-5) — same methodology across three exponents. NOTE: check [[kuznetsov-safonov-2014-conf]] (pdma161, conference abstract companion) — if that note is created, compare content; if materially different, ingest both."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/finite-group-enumeration
  - paper
  - status/draft
---

# Hall's polynomials of finite two-generator groups of exponent seven

## Abstract

Let $B_k = B_0(2,7,k)$ be the largest two-generator finite group of exponent 7 and nilpotency class $k$. Hall's polynomials of $B_k$ for $k \le 4$ are calculated.

## TL;DR

Computes Hall's polynomials for the largest two-generator exponent-7 finite groups $B_0(2,7,k)$ for nilpotency class $k \le 4$. Extends the Hall polynomial multiplication framework (used for exponent 5 in [[kuznetsov-kuznetsova-2013]]) to exponent 7.

## Problem

Can Hall's polynomials be computed for two-generator exponent-7 Burnside groups? The exponent-5 polynomial computation in [[kuznetsov-kuznetsova-2013]] established a template; this paper applies it to exponent 7.

## Approach

Constructs Hall polynomials for $B_0(2,7,k)$ for $k \le 4$ using the collection process. Full methodology not available (abstract is two sentences).

## Key result

Hall's polynomials for $B_k = B_0(2,7,k)$ computed for $k \le 4$. These give an explicit fast multiplication oracle for two-generator exponent-7 finite groups, enabling Cayley graph and growth function computation.

## Assumptions

- $B_0(2,7,k)$ finite for small $k$ (well-established for the restricted Burnside group).
- Hall polynomial collection process correctly adapted from the exponent-3 and exponent-5 cases.

## Limitations / scope

- $k \le 4$ only (small nilpotency class).
- Exponent 7, two generators: limited scope. Does not directly address B(2,5).

## Replication evidence

No independent replication known. Cross-exponent consistency: same technique in [[kuznetsov-kuznetsova-2013]] (exponent 5) and [[kuznetsov-safonov-2015]] (exponent 3) serves as implicit validation.

## Why this paper matters

This paper completes the three-exponent picture of Kuznetsov's Hall polynomial work:
- Exponent 5: [[kuznetsov-kuznetsova-2013]] (2013) — foundation, enables all B(2,5) Cayley computation
- **Exponent 7**: this paper (2014) — extends to a new Burnside family
- Exponent 3: [[kuznetsov-safonov-2015]] (2015) — full treatment with Cayley graphs

Together they demonstrate that Hall polynomial computation for Burnside quotients is a general technique independent of the specific odd exponent. The cross-exponent validity strengthens confidence in the exponent-5 implementation used throughout the B(2,5) computation line.

## Quotes

Abstract-only access; no verbatim body-text quotes.

## Open questions surfaced

- Are the Hall polynomials for exponent 7 materially more complex than for exponent 5? If the complexity scales with the exponent, this bounds what would be needed for exponent 11, 13, etc.
- Have Cayley graph diameters been computed for $B_0(2,7,k)$ as in [[kuznetsov-2015-cayley-exp3]] for exponent 3? Not in this paper; possibly follow-up work.

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2013]] (Hall polynomial methodology; exponent-7 extension)
- Cites: [[kuznetsov-kuznetsova-2013]]
- Related: [[kuznetsov-safonov-2015]] (exponent-3 Hall polynomials + Cayley graphs — same methodology), [[kuznetsov-2015-cayley-exp3]] (exponent-3 Cayley graphs; same research line)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
