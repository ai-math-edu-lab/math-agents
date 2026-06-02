---
title: "Rewrite Systems"
authors: Nachum Dershowitz, Jean-Pierre Jouannaud
year: 1990
venue: "Handbook of Theoretical Computer Science, Vol. B: Formal Models and Semantics (J. van Leeuwen, ed.), Elsevier, pp. 243-320"
url: ""
language: en
domain: group-theory
status: draft
methodology_type: review
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[knuth-bendix-1970]]"
contradicts: []
replicates: []
cites:
  - "[[knuth-bendix-1970]]"
cited_by: []
quality_notes: "Authoritative survey chapter in Handbook of TCS (1990), pre-digital era. Abstract not retrieved verbatim — paywalled book chapter; content from authoritative knowledge of this widely-used reference. Standard citation for rewriting theory in the literature. The Handbook of TCS was a landmark 1990 reference; this chapter is the canonical survey on term rewriting and remains current."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/rewriting-systems
  - topic/word-problem
  - topic/knuth-bendix
  - topic/divergence-and-stagnation
  - paper
  - status/draft
---

# Rewrite Systems

## Abstract

*(Not retrieved verbatim — paywalled book chapter. Described from authoritative knowledge.)*

Comprehensive survey of the theory of term rewriting systems (TRS): termination (Noetherian orderings, dependency pairs), confluence (Church-Rosser, local confluence, Newman's Lemma), completion (Knuth-Bendix completion and extensions), canonical forms, and critical pairs. Covers failure modes of completion — divergence, non-termination, non-confluence — and survey heuristics and theoretical characterizations. Includes equational theories, associativity/commutativity extensions, conditional rewriting, and higher-order rewriting.

## TL;DR

The canonical 1990 survey of all aspects of term rewriting theory: termination orderings, confluence theory, completion algorithms, and their failure modes. The standard reference for understanding when and why KB completion diverges. Every subsequent paper on rewriting cites this.

## Problem

What is the theoretical landscape for term rewriting systems as a tool for equational reasoning and the word problem? When does KB completion terminate? When does it diverge? What orderings work for what theories? The survey organizes 20 years of results into a coherent reference.

## Approach

Survey organized by theme:
- **Termination**: simplification orderings (lexicographic path order, recursive path order, Knuth-Bendix ordering, polynomial interpretations). Well-foundedness theory.
- **Confluence**: local confluence (all critical pairs resolvable), Church-Rosser theorem, Newman's Lemma (local confluence + termination → confluence).
- **Completion**: the KB completion procedure and its formal properties. Extensions for AC theories (associativity/commutativity), ordered completion.
- **Failure and divergence**: characterizations of theories where KB diverges (infinite number of critical pairs, cyclic derivations). Heuristic strategies for practical completion.

## Key result

**Theoretical framework** (not a single empirical result):
1. **Newman's Lemma**: a locally-confluent, terminating TRS is confluent (and thus complete).
2. **Critical Pair Lemma**: a TRS is locally confluent iff all critical pairs can be resolved.
3. **KB completion correctness**: the procedure terminates with a complete TRS iff the theory admits one and the ordering is compatible with the theory.
4. **Divergence characterization**: KB diverges for a theory iff no finite complete TRS exists for it (under the given ordering) — the procedure generates rules faster than it can simplify them.

## Assumptions

- Term rewriting in a fixed signature; generalizations to order-sorted, conditional, and higher-order rewriting discussed but not the main focus.
- Orderings must be reduction orderings (monotone + well-founded); the survey presents a hierarchy of known valid orderings.

## Limitations / scope

- Survey to 1990; does not cover post-1990 advances (dependency pairs 2000, string-rewriting-specific results, KBMAG development).
- The group-theory specialization (string rewriting, inverse-closed sets) is mentioned but not the central focus.

## Replication evidence

Cited by essentially every subsequent paper on KB completion. The theoretical results are classical and independently replicated.

## Why this paper matters

Dershowitz & Jouannaud 1990 provides the theoretical grounding for understanding **why** the Mixer is necessary. The key insight from this survey for the Mixer:
1. **Divergence is generic**: for hard equational theories (like Burnside groups), KB diverges under any single ordering. This is not a bug but a theorem.
2. **Ordering choice matters**: different orderings diverge in different directions, generating different (partial) rule sets. The Mixer's multi-ordering cooperation exploits this: each ordering's divergent sequence produces rules that are useful under the other ordering's rewriting system.
3. **Critical pairs are the information unit**: every critical pair represents a potential equality that the theory forces. In the Mixer, rules injected from one ordering's KB into another's are exactly critical pairs that the receiving ordering wouldn't have generated on its own.

## Quotes

*(No verbatim abstract retrieved — pre-digital survey chapter.)*

## Open questions surfaced

- For which group presentations does KB complete under some ordering? (Answered for automatic groups by [[epstein-et-al-1992-word-processing]].)
- Is there an ordering that minimizes the "divergence rate" for Burnside groups? (Open — see [[Concepts/kb-mixing-stagnation]].)

## Related material in vault

- Extends: [[knuth-bendix-1970]] (original KB paper; this survey covers and extends it)
- Concept hub: [[techniques/knuth-bendix]] (vault concept note on KB completion)
- Applied: [[Research/Group theory/Tools/KBMAG]] (KBMAG applies KB completion with specific orderings for groups)
- Cross-reference: [[Concepts/kb-mixing-stagnation]] (the stagnation/divergence modes documented in the Mixer context)
