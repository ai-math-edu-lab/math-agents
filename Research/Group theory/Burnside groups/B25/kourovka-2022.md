---
title: "Unsolved Problems in Group Theory: The Kourovka Notebook No. 20"
authors:
  - "E.I. Khukhro (ed.)"
  - "V.D. Mazurov (ed.)"
year: 2022
venue: "Sobolev Institute of Mathematics, Novosibirsk; arXiv:1401.0300v20"
url: ""
source_path: "docs/papers/Kourovka 2022.pdf"
language: en
domain: group-theory
methodology_type: review
relevance: 1
key_concepts: []
extends: []
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
cited_by:
  - "[[kourovka-11.48-kostrikin-1990]]"
  - "[[b25-finiteness-11.48-kostrikin]]"
  - "[[b-exponent-5-adian-4.2b]]"
  - "[[braid-b4-membership-6.24-makanin]]"
  - "[[2-relator-word-problem-9.29-merzlyakov]]"
  - "[[andrews-curtis-conjecture]]"
  - "[[grobner]]"
quality_notes: "This note covers only the Burnside-relevant and Gröbner-relevant entries in the 2,200+ problem notebook. For the full notebook, see arXiv:1401.0300v20. No resolution note on Problem 11.48 in the 2022 edition — this problem remains open."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/word-problem
  - topic/braid-groups
  - topic/finitely-presented-groups
  - paper
  - status/draft
project: b25
---

# Unsolved Problems in Group Theory: The Kourovka Notebook No. 20

Khukhro & Mazurov, eds. (2022). The 20th edition of the running compendium of open problems in group theory, maintained since 1965. This note covers only the entries relevant to this vault's research.

## Abstract

> **Scope of this note:** Only problems relevant to this vault — Burnside groups (Problems 11.48, 11.36, 11.37, 12.32, 4.2b), Braid groups (6.24), and Gröbner-relevant problems (7.25, 11.10b). The full notebook (arXiv:1401.0300v20) contains 2,200+ problems spanning all of group theory.

## TL;DR

The 20th edition of the standard reference for open group theory problems. The primary entry for this vault is Problem 11.48 (Kostrikin, 1990): whether B(2,5) is infinite, phrased as a free-group element condition. **Open as of 2022.**

## Problem

The Kourovka Notebook collects open problems rather than proving them. The problems relevant to this vault:

- **11.48** (Kostrikin, 1990): Is [x,y,y,y,y,y,y] a product of fifth powers in the free group ⟨x,y⟩? If not, B(2,5) is infinite.
- **4.2b** (Adian, 1973): Do infinite finitely generated groups of exponent 5 exist?
- **6.24** (Makanin, 1980): Is the membership problem for the braid group B₄ decidable?
- **9.29** (Merzlyakov, 1984): Do 2-relator groups with insoluble word problem exist?
- **7.25** and **11.10b**: Used as worked examples in [[grobner]] (Kreuzer-Myasnikov-Rosenberger) for the Gröbner quotient test.

## Approach

N/A — the Kourovka Notebook is an open-problems compendium. Problems are submitted by researchers, collected by the editors, and updated with partial-solution notes across editions. No algorithmic approach is described; sources are editorial annotations.

## Key result

**Per-problem status (2022 edition):**

| Problem | Poser | Status (2022) |
|---|---|---|
| 11.48 | Kostrikin (1990) | **Open** — no ∗ marker |
| 4.2b | Adian (1973) | **Open** |
| 11.36 | Zalesski | Partial — proved for large prime n (Cherepanov 2006, n > 1009) |
| 11.37 | S.V. Ivanov | Partial — true for odd n > 665 and n > 248 divisible by 29 |
| 12.32 | S.V. Ivanov | **Proved** (Olshanskii, J. Algebra 560 (2020), 960–1052) |
| 6.24 | Makanin (1980) | **Open** for B₄ (undecidable for Bₙ, n ≥ 5: T.A. Makanina 1981) |
| 9.29 | Merzlyakov (1984) | **Open** |

**Problem 11.48 verbatim (the stake of all B(2,5) experiments):**

> "Is the commutator [x, y, y, y, y, y, y] a product of fifth powers in the free group ⟨x, y⟩? If not, then the Burnside group B(2, 5) is infinite."

**Logical structure:** B(2,5) is infinite ⟺ [x,y,y,y,y,y,y] ∉ ⟪w⁵ | w ∈ F(x,y)⟫ in the free group.

## Assumptions

- The restricted B(2,5) is finite (|B(2,5)_restricted| = 5^34, class 12 — [[havas-wall-wamsley-1974]]) — this is assumed known and used as context.
- Problem status (open/closed) is accurate as of the 20th edition (2022). Editions are updated periodically; check arXiv:1401.0300v20 for the current version.

## Limitations / scope

- This note covers a narrow selection of the 2,200+ problems. The bulk of the notebook (p-groups, representation theory, finite simple groups, etc.) is not summarized here.
- Problem numbers differ between editions. Numbers here are from Edition 20 (2022). The [[grobner]] paper references an earlier edition (its "[4]"); problem numbers may differ.
- "Word does not appear in the Kourovka Notebook" observation (confirmed for "Gröbner" by search): the grobner.md connection to Kourovka 7.25 and 11.10b is via the Kreuzer-Myasnikov-Rosenberger paper citing specific Kourovka problems, not the Kourovka Notebook citing Gröbner methods.

## Replication evidence

N/A — this is an editorial compendium. The problem statements are the authoritative source; their status ("open," "∗ proved," partial comment) is the editors' assessment.

## Why this paper matters

This notebook is the canonical reference for open problems in group theory. Problem 11.48 is the formal statement of the question that all B(2,5) experiments in this vault are working toward — either directly (proving a specific word equals identity in the restricted group) or indirectly (gathering evidence about the word problem structure). No B(2,5) research program should proceed without consulting this source for the current status.

For cross-domain extension: Problems 7.25 and 11.10b (used as Gröbner worked examples in [[grobner]]) show the Kourovka Notebook as a natural source of hard-instance benchmarks for any FPG algorithm, including future Mixer targets.

## Quotes

> "Is the commutator [x, y, y, y, y, y, y] a product of fifth powers in the free group ⟨x,y⟩? If not, then the Burnside group B(2, 5) is infinite." — Problem 11.48 (A.I. Kostrikin, 11th issue, 1990)

## Open questions surfaced

- Has Problem 11.48 been resolved since the 2022 edition? Check arXiv:1401.0300v20 for the latest.
- Problems 4.2b and 11.48 are equivalent for m=2: does the same equivalence hold for B(m,5), m > 2?
- Can the Kourovka Notebook be used systematically as a benchmark source for new Mixer experiments beyond the problems already cataloged here?

## Related material in vault

- Extends: (none — foundational problem collection)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[havas-wall-wamsley-1974]] (B(2,5) = 5^34 is the result Problem 11.48 builds on)
- Cited by (in vault): [[kourovka-11.48-kostrikin-1990]], [[b25-finiteness-11.48-kostrikin]], [[b-exponent-5-adian-4.2b]], [[braid-b4-membership-6.24-makanin]], [[2-relator-word-problem-9.29-merzlyakov]], [[andrews-curtis-conjecture]], [[grobner]]
