---
title: "Word Problem — Map of Content"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/decidability
  - topic/moc
  - status/validated
---

# Word Problem — Map of Content

**This MOC is a curated reading path for the word problem in finitely presented groups** — from the decidability landscape, through specific algorithms, to open boundary cases. Navigate here when you want to know what's decidable, which algorithm to choose, or how to construct and verify a target word.

---

## Decidability landscape

- [[Research/Group theory/Word Problem/decidability-landscape]] — The complete picture: word problem statement, Novikov-Boone undecidability for general FPGs, decidability results for free / abelian / 1-relator / hyperbolic / automatic groups with verbatim theorem citations and complexity bounds. Start here for an overview.

---

## Algorithmic techniques

### Foundational papers

- [[Research/Group theory/Word Problem/knuth-bendix-1970]] — Knuth & Bendix (1970): the original KB completion paper; critical-pair generation as search. Start here for the KB paradigm.
- [[Research/Group theory/Word Problem/todd-coxeter-1936]] — Todd & Coxeter (1936): the original coset enumeration paper; coincidence detection as the dual to KB critical pairs.
- [[Research/Group theory/Word Problem/epstein-et-al-1992-word-processing]] — Epstein et al. (1992) "Word Processing in Groups": automatic groups and the KBMAG theory. KB terminates ↔ group is automatic; quadratic-time word problem.
- [[Research/Group theory/Word Problem/dershowitz-jouannaud-1990]] — Dershowitz & Jouannaud (1990): rewriting theory survey including stagnation and divergence characterization.

### Technique concept notes

- [[Research/Group theory/Word Problem/techniques/knuth-bendix]] — Knuth-Bendix completion as a word-problem algorithm: when it terminates, it gives a canonical decision procedure. See [[_moc-knuth-bendix]] for full depth.

- [[Research/Group theory/Word Problem/techniques/dehn-function]] — The Dehn function as a complexity measure; Dehn's algorithm for hyperbolic groups (linear time); the connection between linear Dehn function and hyperbolicity.

- [[Research/Group theory/Word Problem/techniques/automatic-groups]] — Automatic group structure via finite-state automata; O(n²) word problem; which groups are automatic (hyperbolic, abelian, braid groups via Garside normal form).

---

## Target words

- [[Research/Group theory/Word Problem/target-words]] — What a target word is (a specific group element whose identity is being computed), how to construct one (from lower central series, commutator notation), and how to verify equality (confluent KB rewriting, GAP oracle, abelianization as necessary condition only).

---

## Open boundary cases

- [[2-relator-word-problem-9.29-merzlyakov]] — Kourovka 9.29 (Merzlyakov, 1984): 1-relator groups are decidable (Magnus); general FPGs are undecidable (Novikov-Boone); the 2-relator case is open. Included here to define the undecidability boundary adjacent to all our computational work.

- [[braid-b4-membership-6.24-makanin]] — Kourovka 6.24 (Makanin, 1980): the membership problem for B₄ is the boundary case between decidable (n≤3) and undecidable (n≥5). Relevant because membership is strictly harder than the word problem and our braid-group work lives at this boundary.

---

## Practical reference

- [[havas-robertson]] — 1994 survey illustrating the KB + coset-enumeration + Reidemeister-Schreier pipeline for computing derived series of unknown FPGs. The computational toolchain that all subsequent KB work builds on.

---

## Tools (word-problem in practice)

- [[Research/Group theory/Tools/GAP/examples/03-word-equality]] — GAP word equality testing for small groups.
- [[Research/Group theory/Tools/KBMAG/examples/01-s3-shortlex]] — Standalone kbprog for a group small enough to complete.
- [[Research/Group theory/Tools/group-theory-tools-overview]] — Decision tree: which tool for which word-problem task.

---

## Related MOCs

- [[_moc-burnside]] — The Burnside word problem (B(2,5) target words) as the primary open application.
- [[_moc-knuth-bendix]] — KB completion as the word-problem algorithm of choice for our groups.
- [[_moc-presentations-and-orders]] — How group presentations define the word problem in the first place.
