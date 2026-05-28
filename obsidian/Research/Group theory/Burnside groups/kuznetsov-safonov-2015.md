---
title: "Hall's polynomials over Burnside groups of exponent three"
authors: A. A. Kuznetsov, K. V. Safonov
year: 2015
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/8/57
url_translated:
language: ru
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
quality_notes: "source-text-incomplete-only-abstract-available. 3-page conference note (Prikl. Diskr. Mat. Suppl. 8, pp. 147–149). Original in Russian. Companion to [[kuznetsov-2015-cayley-exp3]] (same topic, same year, but [[kuznetsov-2015-cayley-exp3]] is the fuller 7-page Sib. El. Math. Izv. paper with complete Cayley graph results). This conference note is likely a preliminary announcement of the results in the full paper. BORDERLINE inclusion: methodology for exponent 3; included because Hall polynomial technology generalizes across odd exponents and underpins the exponent-5 work."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/finite-group-enumeration
  - topic/cayley-graphs
  - paper
  - status/draft
---

# Hall's polynomials over Burnside groups of exponent three

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The research examines Burnside groups of exponent 3, denoted $B_k$. Two arbitrary elements in the group $B_k$ represented as $a_1^{x_1} \cdots a_n^{x_n}$ and $a_1^{y_1} \cdots a_n^{y_n}$ can be multiplied using collection processes or Hall's polynomials. The study demonstrates that Hall's polynomials provide computational advantages over traditional collection methods for group operations. The researchers calculated previously unknown Hall's polynomials of $B_k$ for $k \le 4$ and discuss applications to Cayley graph analysis. The approach is readily implementable in multiprocessor systems. [trans.]

## TL;DR

Conference note computing Hall's polynomials for Burnside groups of exponent 3 ($k \le 4$) and noting their Cayley graph applications. Companion to the fuller treatment in [[kuznetsov-2015-cayley-exp3]]. Methodology directly parallels the exponent-5 work in [[kuznetsov-kuznetsova-2013]].

## Problem

Can Hall's polynomials — the tool used for fast multiplication in the exponent-5 groups [[kuznetsov-kuznetsova-2013]] — be computed for Burnside groups of exponent 3? If so, the same computational framework applies across multiple Burnside families.

## Approach

Extends the Hall polynomial computation from exponent-5 groups (in [[kuznetsov-kuznetsova-2013]]) to exponent-3 Burnside groups $B_k$. Computes polynomial identities for $k \le 4$. Notes multiprocessor applicability. Full details in [[kuznetsov-2015-cayley-exp3]].

## Key result

Hall's polynomials for $B_k$ (exponent-3 Burnside groups) computed for $k \le 4$. Cayley graph applications noted (full Cayley graph analysis in [[kuznetsov-2015-cayley-exp3]]).

## Assumptions

- Exponent-3 Burnside groups are finite for small $k$ (well-established; $|B(2,3)| = 3^3 = 27$, $|B(3,3)| = 3^7 = 2187$, etc.).
- Hall's polynomial framework generalizes from exponent 5 to exponent 3 with appropriate adjustment of the polynomial identities.

## Limitations / scope

- $k \le 4$ only (small nilpotency classes).
- Conference note: algorithm details deferred to [[kuznetsov-2015-cayley-exp3]].
- Exponent 3 specific; not directly about B(2,5).

## Replication evidence

[[kuznetsov-2015-cayley-exp3]] (same authors, same year, fuller paper) provides the main treatment.

## Why this paper matters

Hall's polynomial multiplication is the computational foundation for ALL of Kuznetsov's B(2,5) work. The fact that the same technique works for exponent 3 and exponent 7 ([[kuznetsov-safonov-2014]]) establishes that it is a general odd-exponent Burnside methodology, not an exponent-5 accident. This cross-exponent validation strengthens confidence that the [[kuznetsov-kuznetsova-2013]] implementation is correct and generalizable.

## Quotes

Abstract-only access; no verbatim body-text quotes.

## Open questions surfaced

- Do the Hall polynomials for exponent 3 exhibit simpler structure than those for exponent 5, consistent with the simpler nilpotency? If yes, that could inform a faster algorithm for exponent-5.

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2013]] (same Hall polynomial methodology, exponent 5)
- Cites: [[kuznetsov-kuznetsova-2013]]
- Related: [[kuznetsov-2015-cayley-exp3]] (full paper; same result), [[kuznetsov-safonov-2014]] (same methodology for exponent 7)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
