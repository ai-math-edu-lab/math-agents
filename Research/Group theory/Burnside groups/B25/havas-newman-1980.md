---
title: "Application of Computers to Questions Like Those of Burnside"
authors:
  - George Havas
  - M.F. Newman
year: 1980
venue: "Proceedings of the Burnside Workshop, Bielefeld, June–July 1977, pp. 211–230"
url: ""
source_path: "docs/papers/1980hn.pdf"
language: en
domain: group-theory
methodology_type: review
relevance: 1
key_concepts: []
extends:
  - "[[havas-wall-wamsley-1974]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
cited_by:
  - "[[havas-robertson]]"
  - "[[algo-mixing-burnside-slides]]"
quality_notes: "Survey as of 1977; captures the state of computational Burnside group work before modern KB tools. The B(2,5) result (5^34) is cited from [[havas-wall-wamsley-1974]] rather than independently re-derived. Key value: contextualizes B(4,3) and B(7,2) alongside B(2,5) with computing times from 1970s hardware as baseline."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/coset-enumeration
  - topic/word-problem
  - topic/nilpotent-quotient
  - topic/finitely-presented-groups
  - paper
  - status/draft
---

# Application of Computers to Questions Like Those of Burnside

Havas & Newman (1977 lecture, 1980 publication). Survey of computer-assisted results on Burnside groups and related periodic group problems.

## Abstract

> No verbatim abstract available — source is local PDF at `docs/papers/1980hn.pdf`. See TL;DR below.

## TL;DR

Surveys the state of computational Burnside group theory as of 1977: confirms |B(2,5)| = 5^34 from [[havas-wall-wamsley-1974]], establishes |B(4,3)| = 2^69 (class 7), describes the p-quotient algorithm and Todd-Coxeter as the primary computational tools, and frames the project as "applying several different computational techniques to the same problem" — the earliest articulation of what the Mixer does.

## Problem

What can computers tell us about the Burnside groups B(m,n) — their orders, nilpotency classes, and presentations — using 1970s-era programs? And which algorithm is most efficient for which problem?

## Approach

Three main algorithmic approaches surveyed:

1. **Coset enumeration (Todd-Coxeter):** Enumerate cosets of the trivial subgroup in the group; terminates iff group is finite. Used for B(2,4).
2. **p-quotient algorithm (Wamsley-Bayes-Kautsky-Newman-O'Brien):** Compute consistent commutator power presentations of nilpotent quotients class-by-class. Used for B(2,5), B(4,3), B(7,2).
3. **Lie algebra methods (Kostrikin, E(p,r)):** Compute the associated Lie ring; Sanov's correspondence relates it to the group. Faster for partial results (~100x vs. full group), but doesn't give the group directly.

Computing times on 1970s hardware (illustrative only):
- E(5,2) Lie ring: 9 CPU seconds
- B(2,5) full presentation: 15 minutes
- B(2,4) via coset enumeration: ~30 seconds on Univac 1100/42

## Key result

Survey results (as of 1977):

| Group | Order | Class | Method | Source |
|---|---|---|---|---|
| B(2,4) | 2^12 | ≤ 4r (r generators) | Coset enumeration | Todd-Coxeter V2.2 |
| B(2,5) | 5^34 | 12 | Lie algebra + p-quotient | [[havas-wall-wamsley-1974]] |
| B(4,3) | 2^69 | 7 | p-quotient (Bayes-Kautsky-Wamsley) | This paper |
| B(7,2) | Class ≥ 18 | — | Lie algebra | Largest class-14 image: 7^1075 |

**Consistent commutator power presentation (Wamsley's form):**
For generators a₁,...,aₙ with p-power relations:
```
[aⱼ, aᵢ] = a_{j+1}^{α(j,i,j+1)} · ... · aₙ^{α(j,i,n)}   (for i < j)
aᵢ^p = a_{i+1}^{β(i,i+1)} · ... · aₙ^{β(i,n)}
```
"Consistent" = every element has a unique normal form a₁^{m₁}...aₙ^{mₙ} with 0 ≤ mᵢ < p.

**Sanov's correspondence:** The Lie ring of B(p,r) corresponds to E(p,r) up to class 2p−2 (Sanov 1952). Kostrikin extended to class 2p for r=2.

## Assumptions

- p-quotient algorithm correctness assumed (no independent cross-check for B(4,3); B(2,5) has cross-check from [[havas-wall-wamsley-1974]]).
- Lie algebra method relies on Kostrikin's extension of Sanov's correspondence (established separately).
- Results are for the **restricted** Burnside groups only (largest finite quotients of exponent p or prime-power).

## Limitations / scope

- Survey as of 1977; some results (B(4,4), B(5,3)) were noted as "in progress." B(5,3) is now an active target in this vault.
- Computing times are 1970s baselines; modern hardware running the same algorithms is orders of magnitude faster.
- Does not address the unrestricted Burnside groups (whether B(m,5) for m≥2 is infinite — see [[kourovka-11.48-kostrikin-1990]]).
- B(4,3) result (2^69, class 7) cited here appears without independent verification in the survey. See the B(4,3) experiments in this vault for modern verification.

## Replication evidence

The B(2,5) result is independently verified by [[havas-wall-wamsley-1974]] (two independent methods). The B(4,3) result (2^69, class 7) is cited as Bayes-Kautsky-Wamsley without a cross-check in this paper; the vault's B(4,3) mixing experiments (see `experiments/b43_kbmag_mixing/`) now reproduce this on modern hardware.

## Why this paper matters

This survey is the earliest source articulating the multi-algorithm philosophy: "the basic approach is to apply several different computational techniques to the same problem" — which is precisely the Mixer's design. It also provides the 1977 baseline for what was computationally hard (B(4,3) was "in progress"), contextualizing what modern KB mixing achieves.

For B(4,3): the 1977 result |B(4,3)| = 2^69, class 7 is the reference point against which the Mixer's confluent KB completion (reaching exactly 2^69 via a 2,333-rule rewrite system) must be measured.

## Quotes

> No short verbatim quotes extracted — source is local PDF `docs/papers/1980hn.pdf`. See source for Wamsley presentation formulas and Table 1 computing times.

## Open questions surfaced

- What are the orders of B(4,4), B(5,3), B(4,5)? Noted as "in progress" in 1977; B(5,3) is now an active target.
- The p-quotient algorithm described here: can it be reformulated as an agent cooperating with KB within a Mixer framework?

## Related material in vault

- Extends: [[havas-wall-wamsley-1974]] (surveys and contextualizes its B(2,5) result)
- Contradicts: (none)
- Replicates: (none — cites [[havas-wall-wamsley-1974]] rather than re-deriving)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[havas-wall-wamsley-1974]]
- Cited by (in vault): [[havas-robertson]] (as ref [23] context), [[algo-mixing-burnside-slides]]
