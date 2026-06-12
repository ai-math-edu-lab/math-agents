---
title: "A practical method for enumerating cosets of a finite abstract group"
authors: J.A. Todd, H.S.M. Coxeter
year: 1936
venue: "Proceedings of the Edinburgh Mathematical Society 5 (1936), pp. 26-34"
url: ""
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[epstein-et-al-1992-word-processing]]"
  - "[[le-chenadec-1986]]"
quality_notes: "Foundational 1936 paper, pre-digital era. Abstract not retrieved verbatim — paywalled historical journal; content from authoritative knowledge. The paper predates the modern notion of 'algorithm' in the computational sense, but describes a concrete enumeration procedure. The method described is now universally known as the Todd-Coxeter algorithm; modern treatments (Havas et al., Sims 1994) greatly improve efficiency without changing the core coincidence-detection mechanism."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/coset-enumeration
  - topic/word-problem
  - topic/finitely-presented-groups
  - paper
  - status/draft
---

# A practical method for enumerating cosets of a finite abstract group

## Abstract

*(Not retrieved verbatim — pre-digital journal, 1936. Described from authoritative knowledge.)*

Presents a systematic method for enumerating the cosets of a subgroup $H$ in a finitely presented group $G = \langle X | R \rangle$. The method builds a **coset table**: rows index cosets, columns index generators, and entries give the action of each generator on each coset. The table is completed by a process of **scanning** relators across rows (each relator, applied as a sequence of generator actions to a coset, should return to the same coset) and **coincidence detection** (when two table entries are forced to represent the same coset, they are merged). If the group $G$ is finite with $|G:H|$ cosets, the procedure terminates with a complete coset table; otherwise it may diverge.

## TL;DR

Introduces the Todd-Coxeter coset enumeration algorithm: build a partial coset multiplication table for a group presentation, fill it in by scanning relators, detect coincidences, merge them, and repeat. Terminates with the coset index $|G:H|$ if $G$ is finite (or $H$ has finite index). The dual procedure to KB completion: TC enumerates elements (cosets = elements of $G$ acting on $G/H$) while KB enumerates rules (equations = pairs of equal words). Both are semi-decision procedures for the word problem.

## Problem

Given $G = \langle X | R \rangle$ (a finitely presented group) and a subgroup $H$ (given by a generating set), compute the **coset index** $|G:H|$ — or equivalently, determine whether $G$ is finite and compute $|G|$ when $H = \{e\}$. The word problem for $G$ is equivalent: $w = 1$ in $G$ iff the coset of $H$ containing $w$ is $H$ itself.

## Approach

**Todd-Coxeter enumeration:**
1. Initialize the coset table: one known coset (coset 1 = $H$); columns for each generator $x_i$ and its inverse $x_i^{-1}$.
2. **Definition**: when an entry is needed but unknown, define a new coset.
3. **Scanning**: for each relator $r \in R$ and each coset $c$, the sequence of generator actions $r$ on $c$ should return to $c$ (since $r = 1$ in $G$). Whenever the sequence can be partially traced from both ends, infer unknown entries.
4. **Coincidence detection**: when two table positions are forced to be the same coset, record the coincidence; merge all subsequent references.
5. **Repeat** until the table closes (all entries filled) or forever.

**Termination**: guaranteed iff $|G:H| < \infty$. Practical efficiency depends on strategy choices (which relators to scan first, when to define new cosets, etc.) — no optimal strategy is known in general.

## Key result

- **Correctness**: if TC terminates, the coset table correctly computes $|G:H|$ and gives a complete description of the action of $G$ on $G/H$.
- **Semi-decidability**: same as KB — terminates iff the relevant quantity is finite, diverges otherwise.
- **Dual to KB**: TC and KB are the two classical semi-decision procedures for the word problem in finitely presented groups. They make different information-sharing tradeoffs (TC discovers cosets; KB discovers equations).

## Assumptions

- $G$ is finitely presented; $H$ is finitely generated.
- The relators $R$ generate the normal closure of $H$ in $G$.

## Limitations / scope

- Practical performance depends heavily on enumeration strategy; theoretical worst-case is exponential in $|G:H|$.
- For large or infinite groups, TC diverges without producing useful partial information (unlike KB, which produces usable rewriting rules as partial output).

## Replication evidence

TC coset enumeration is implemented in GAP, Magma, KBMAG. Theoretical correctness is classical (proved in every modern group theory computation textbook).

## Why this paper matters

Todd & Coxeter 1936 defines the **second classical semi-decision procedure** for the word problem. For the Mixer:
1. **TC and KB are complementary**: TC succeeds where KB fails (when the group has finite index subgroups but no finite complete rewriting system), and vice versa.
2. **Coincidence detection = "partial-No oracle"**: when TC detects a coincidence (two cosets forced equal), it effectively generates a short proof that a certain word reduces to a shorter one — the same information KB produces via critical pairs. The coincidences ARE the KB critical pairs, viewed from the coset perspective.
3. **Information sharing opportunity**: in principle, coincidences discovered by TC during coset enumeration could be injected into a KB run as new rules, and KB-derived equalities could be used to close coset table rows faster. This cross-pollination is not standard in KBMAG but is a potential Mixer extension.

## Quotes

*(No verbatim abstract retrieved — pre-digital journal, 1936.)*

## Open questions surfaced

- Can TC-discovered coincidences be used as new rules in an ongoing KB run? (The reverse is standard — KB rules can accelerate TC via reduced scanning — but not the forward direction.)
- For which classes of groups does TC terminate faster than KB, or vice versa?

## Related material in vault

- Cited by: [[epstein-et-al-1992-word-processing]] (automatic groups — builds on TC and explains when TC terminates efficiently)
- Concept: [[Research/Group theory/General/presentations-and-relations/coset-enumeration.md]] (the vault concept note on coset enumeration methods)
- Related: [[knuth-bendix-1970]] (dual procedure — KB rules vs. TC cosets)
- Tools: [[Research/Group theory/Tools/GAP]] (GAP includes TC coset enumeration)
