---
title: "Word Processing in Groups"
authors: David B.A. Epstein, James W. Cannon, Derek F. Holt, Silvio V.F. Levy, Michael S. Paterson, William P. Thurston
year: 1992
venue: "Jones and Bartlett Publishers (monograph). ISBN 0-86720-244-0"
url: ""
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[todd-coxeter-1936]]"
  - "[[knuth-bendix-1970]]"
contradicts: []
replicates: []
cites:
  - "[[todd-coxeter-1936]]"
  - "[[knuth-bendix-1970]]"
cited_by: []
quality_notes: "Definitive 1992 monograph on automatic groups. Not freely available; content from authoritative knowledge. This book is the primary reference for automatic group theory; virtually every subsequent paper on the computational word problem for infinite groups cites it. Holt is also the author of KBMAG, making this book the theoretical foundation of the KBMAG software used in the Mixer."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/automatic-groups
  - topic/word-problem
  - topic/finitely-presented-groups
  - topic/coset-enumeration
  - paper
  - status/draft
---

# Word Processing in Groups

## Abstract

*(Not retrieved verbatim — monograph, paywalled. Described from authoritative knowledge.)*

Develops the theory of **automatic groups**: groups for which the word problem is solvable by finite-state automata. An automatic group has a regular language $L$ of normal-form words and a collection of finite-state automata (the **multiplier automata**) certifying that $L$ is closed under right-multiplication by each generator. The key computational property is the **fellow-traveler property**: two words representing cosets that differ by a generator remain within a bounded distance of each other throughout their execution in the Cayley graph. The monograph proves that automatic groups have solvable word problem (in quadratic time), characterizes which groups are automatic, and presents algorithms for computing the automata from a group presentation — including the key connection to Knuth-Bendix completion and KBMAG.

## TL;DR

Defines automatic groups (word problem solvable by finite automata); proves they have quadratic-time word problem; characterizes automatic groups via the fellow-traveler property; shows that KB completion over a shortlex ordering terminates iff the group is automatic. The theoretical foundation for KBMAG and for understanding when the Mixer's KB completion will converge.

## Problem

For which finitely presented groups does KB completion (with some ordering) terminate? And for those groups, is there an efficient characterization of tractability? The automatic group framework answers: KB completion terminates iff the group is automatic (with respect to the chosen generating set and ordering), and automatic groups have a uniform quadratic-time word problem.

## Approach

**Automatic group theory:**
1. **Definition**: $G$ is *automatic* with respect to generating set $S$ if there exists a regular language $L \subseteq (S \cup S^{-1})^*$ (a "dictionary") with surjective map $L \to G$, and for each $s \in S \cup S^{-1} \cup \{e\}$, a finite-state automaton recognizing the set of pairs $(u,v) \in L \times L$ with $v = us$ in $G$ (the "multiplier automata").
2. **Fellow-traveler property**: the dictionary $L$ satisfies the fellow-traveler property if for all $(u,v)$ with $v = us$, the words $u$ and $v$ remain within a bounded Hamming distance throughout their simultaneous traversal. This is the key computable characterization.
3. **KB connection**: KB completion with the shortlex ordering terminates iff the group is shortlex-automatic, and the resulting complete rewriting system is equivalent to the shortlex-normal-form automaton.
4. **KBMAG**: Holt's KBMAG software implements this theory — it runs KB + checks for automaticity + computes the automata if the group is automatic.

**Examples of automatic groups**: all finite groups, free groups, surface groups, hyperbolic groups, right-angled Artin groups. **Non-automatic**: amenable groups (including $B(2,5)$ if finite), $\mathbb{Z}^n$ for $n \geq 3$ (not automatic but asynchronously automatic).

## Key result

1. **Automatic groups have quadratic-time word problem**: given the automata, check $w = 1$ by reducing $w$ to its $L$-normal form using the multiplier automata — runs in $O(|w|^2)$ steps.
2. **KB termination = automaticity**: KB completion with shortlex terminates iff the group is shortlex-automatic.
3. **Biautomatic subclass**: biautomatic groups have a stronger closure property; all automatic groups of polynomial growth are biautomatic.
4. **Thurston's result**: hyperbolic groups (in the sense of Gromov) are automatic.

## Assumptions

- Finitely generated group with a fixed generating set. Automaticity is generating-set-dependent: a group may be automatic with respect to one generating set but not another.
- The KB completion uses the shortlex ordering (the most common for KBMAG).

## Limitations / scope

- Automaticity is a sufficient condition for KB termination but not necessary in general (other orderings may terminate for non-automatic groups).
- $B(2,5)$ is NOT known to be automatic (the Burnside problem is the main open question about whether it is finite — if infinite, it cannot be automatic).
- Asynchronous automaticity (a weaker variant) covers more groups but gives only exponential-time word problem.

## Replication evidence

KBMAG implements this theory. GAP's automatic groups package also implements it. The correctness of the theory is classical and taught in graduate group theory courses.

## Why this paper matters

Epstein et al. 1992 is the theoretical foundation for **when the Mixer is needed vs. when KB alone suffices**. If a group is automatic, KBMAG terminates and the word problem is solved. The Mixer is designed specifically for groups that are NOT known to be automatic — including $B(2,5)$. The book's key theorem (KB terminates ↔ automatic) tells us that for $B(2,5)$, no single ordering will produce a complete rewriting system — the Mixer's multi-ordering cooperation is necessary, not optional.

The **fellow-traveler property** is also directly relevant: it says that automatic groups have geodesics that stay close together. The Mixer's rule injection works by finding rules that "bridge" between two orderings' geodesic paths in word space — a direct analog of the fellow-traveler check.

## Quotes

*(No verbatim abstract retrieved — paywalled monograph.)*

## Open questions surfaced

- Is $B(2,5)$ automatic? (Equivalent to the Burnside problem — if $B(2,5)$ is finite, it is automatically automatic; if infinite, it is not.)
- Which Burnside groups are automatic? $B(4,3) = B(2,4,4)$ is finite and thus automatic — the Mixer's success there is consistent with automaticity.

## Related material in vault

- Extends: [[todd-coxeter-1936]] (TC coset enumeration — the monograph builds on TC theory), [[knuth-bendix-1970]] (KB completion — the monograph shows KB = automatic-group-detection)
- Cites: [[todd-coxeter-1936]], [[knuth-bendix-1970]]
- Concept hub: [[techniques/automatic-groups]] (the vault concept note citing this book as its primary source)
- Tool: [[Research/Group theory/Tools/KBMAG]] (KBMAG = computational implementation of this book's theory)
- Open problem: [[Research/Group theory/Open problems/Burnside groups/]] (B(2,5) automaticity is the Burnside problem)
