---
title: "Biasing Knuth-Bendix Completion and Algorithm Mixing in the B(2,5) Problem"
authors: Ethan Kalika
year: 2026
venue: thesis
url: "https://www.proquest.com/docview/3345229960"
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 0
citation_count_date: 2026-06-05
key_concepts:
  - "[[Concepts/kb-mixing-stagnation]]"
  - "[[Concepts/mixable-api]]"
extends:
  - "[[algo-mixing-burnside-slides]]"
  - "[[havas-wall-wamsley-1974]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[epstein-et-al-1992-word-processing]]"
cited_by: []
quality_notes: "Master's thesis, Stevens Institute of Technology, May 2026. Published on ProQuest Dissertations & Theses (doc. 3345229960). Advisor: Alexei Miasnikov; reader: Andrey Nikolaev. No external citations yet. Formalizes the biased KB algorithm developed within the Stevens Lab for AI in Mathematics and Mathematics Education; implementation ongoing as of submission. Bibliography has exactly 3 entries (Epstein et al. 1992, Havas–Wall–Wamsley 1974, Sims 1994). Summary verified against the full thesis PDF (54 pp.) on 2026-06-10."
author: ethan-k
tags:
  - agent/research
  - user/ethan-k
  - domain/group-theory
  - topic/knuth-bendix-completion
  - topic/burnside-groups
  - topic/b25-problem
  - topic/algorithm-mixing
  - topic/rewriting-systems
  - topic/word-problem
  - topic/target-words
  - topic/shortlex-ordering
  - topic/bidirectional-mixing
  - topic/completion-procedures
  - paper
  - status/draft
project: b25
---

# Biasing Knuth-Bendix Completion and Algorithm Mixing in the B(2,5) Problem

## Abstract

This thesis studies computational methods in group theory, with a focus on improving practical approaches to difficult problems involving rewriting systems and word reduction. In particular, we consider the Burnside group B(2,5), whose finiteness is unknown.

The work is based on an algorithm mixing framework, in which multiple instances of algorithms interact and exchange information during execution. Previous work has shown that such methods can effectively compute finite complete rewriting systems for certain group presentations.

The main contribution of this thesis is the development and investigation of a biased variant of the Knuth–Bendix completion algorithm within this mixing framework. The bias is designed to prioritize the generation of rewriting rules that are useful for reducing a set of "special words" associated with B(2,5). The reduction of these words to the identity would provide a proof of the finiteness of B(2,5).

We describe the motivation and design of this biased Knuth-Bendix algorithm, discuss the underlying computational framework, and analyze how targeted rule generation can be used to guide reduction computations toward specific words.

## TL;DR

Standard Knuth-Bendix agents running on B(2,5) rarely produce rules that match substrings of the Havas–Wall–Wamsley target words — this is a bottleneck in the bidirectional mixing strategy. This thesis formalizes a biased KB variant that preferentially generates rules whose right-hand sides contain subwords drawn from partially-reduced target words. This feeds rules that have a higher chance of producing reductions into the mixing framework at the cost that this algorithm no longer targets global completion.

## Problem

Is B(2,5) finite? The approach: if the target words introduced by [[havas-wall-wamsley-1974]] (which normally generate the kernel of B(2,5) → R(2,5)) can all be reduced to the identity using relations that hold in B(2,5), then B(2,5) ≅ R(2,5) and is therefore finite. The computational obstacle is that mixing only instances standard KB completion does not reduce the target words in any reasonable time.

## Approach

**Algorithm mixing framework** (Ch. 3): Multiple KB agents with different reduction orderings run in parallel, periodically exchanging discovered rules through a central mixer. The mixer redistributes rules via injection; agents reinterpret injected rules under their own orderings. Agents are loosely coupled — no shared memory, communication via file-based rule exchange.

**Bidirectional mixing** (§3.4): Adds dedicated *reducer agents* that apply all available rules to partially reduce the target words toward the identity. The completion and reduction goals run simultaneously; termination is declared if target words reach the identity, even without a complete rewriting system.

**Biased Knuth–Bendix algorithm** (Ch. 4): A variant of the Knuth-Bendix algorithm in which a *predicate* R filters which rules enter the biased rule set Ẽ. Overlaps are only computed between biased rules in Ẽ, but all discovered rules are kept in a wider set E for redundancy removal and future injection. The predicate used in practice: a rule u → v is biased if v contains some s ∈ S as a subword, where S is a set of subwords drawn from the partial reductions of the target words and from the original target words themselves.

**Subword selection strategies** (§4.3): S can be chosen by (a) uniform random sampling or (b) most-frequent subwords, across a specified set of lengths (e.g., 10 subwords of length 3, 15 of length 5, 20 of length 7). Multiple biased agents can run simultaneously with different S, all sharing through the mixer.

**Theoretical guarantees**: Lemma 4.1.3 proves that replacing a rule's right-hand side with its biased residue does not change the presented monoid. Propositions 4.2.1 and 4.2.2 give sufficient conditions on the predicate (carry-over properties and alternative carry-over properties) guaranteeing that overlap resolution between biased rules always produces new biased rules. The subword predicate satisfies the carry-over properties but **not** the alternative carry-over properties — it depends only on right-hand sides, so reversing a biased rule can break the explicit-reversibility (third alternative) property (§4.3).

## Key result

**Experimental** (§3.2): Four configurations (shortlex KB, RPO KB, fully-connected mixing, one-time injection) on B(4,3) and M11, three runs each, reported as mean (SD), run on the mixing infrastructure built by Vlad Stepanov and [[People/maumayma|Maria Matveeva]] at the Stevens Lab for AI in Mathematics and Mathematics Education, with support from the Nebius Group. With confluence checking excluded (Table 3.2), the one-time injection configuration found by Vlad Stepanov (shortlex → RPO agent at 20,000 rules, 80 rules injected) achieves 15 (0) s completion for B(4,3) vs. 17 (0) s RPO alone, 19.3 (0.471) s fully-connected, and timeout for shortlex alone — the only configuration that beats both baselines. With confluence checking included (Table 3.1), the RPO baseline wins on B(4,3): 78.8 (0.249) s vs. 82.1 (1.31) s injection and 86.9 (1.88) s fully-connected. The thesis's own reading: "the confluence check dominates the overall runtime" and "in all but one case, the performance of the mixing configurations lies between the two baseline outcomes" — mixing reduces sensitivity to the ordering choice at the cost of communication and rule-set-growth overhead. On M11 the ordering preference reverses (shortlex 0.1 (0) s beats RPO 0.9 (0) s, Table 3.1) — the in-thesis instance of the No-Free-Lunch motivation; all M11 configurations complete in < 0.1 s of computation time (Table 3.2).

**Solution diversity** (§3.2, fourth observation): the two M11 baselines produced *distinct* confluent rewriting systems; in the mixing configurations each agent recovered the system of its own baseline run, so a single mixed execution yielded both — beyond runtime, mixing increases the diversity of discovered solutions.

**Structural** (Proposition 2.8.1, citing Havas et al.): If all target words are trivial in B(2,5), then B(2,5) is finite. Proof: the target words normally generate ker(B(2,5) → R(2,5)); if they vanish in B(2,5), the kernel is trivial and B(2,5) ≅ R(2,5).

**Biased algorithm correctness**: Every rule generated by the biased KB algorithm defines a relation that holds in the presented monoid. The presented monoid is unchanged throughout (Lemma 4.1.3, Proposition 2.6.3).

## Assumptions

- B(2,5) is treated via the KBMAG finite presentation (a subset of exponent-5 relations); relations derived from it hold in B(2,5) but the KBMAG presentation may not present the full B(2,5).
- Reduction orderings are linear (simplifies exposition; not required for KB in general).
- The mixing framework assumes algorithms can be paused to export/consume rules.
- The subword predicate S is drawn from partial reductions of target words at the time biasing is initialized; periodic re-selection is supported but not formally analyzed.

## Limitations / scope

- The biased KB algorithm is **not** designed to produce a complete rewriting system on its own; its output is intended for injection into other agents.
- No target words have yet been reduced to the identity; bidirectional mixing has achieved length reductions but not identity reductions as of submission (May 2026).
- The B(2,5) problem is not resolved.
- Predicate selection remains largely heuristic; the carry-over conditions are sufficient but not necessary for useful biasing.
- No theoretical analysis of how often biased rules are useful for reducers, or of convergence/termination of the biased agent.

## Replication evidence

No external replication. The mixing experiments (§3.2) were conducted by the author on infrastructure developed by Vlad Stepanov and Maria Matveeva at the Lab for AI in Mathematics and Mathematics Education at Stevens Institute of Technology (supported by the Nebius Group). Experimental results are from three runs each, reported as mean (SD). The one-time injection protocol (Experiment 4) was proposed by Vlad Stepanov, tuned for B(4,3), and repeated unchanged on M11 for consistency.

## Why this paper matters

This thesis is the primary technical reference for the biased Knuth-Bendix algorithm and its integration into the algorithm mixing framework at Stevens. It formalizes the observation that in some cases the standard KB agents rarely produce rules that are useful for reducing target words, and turns this into a deliberate mechanism: by restricting overlap computation to rules whose right-hand sides contain current-reduction subwords, the biased agent concentrates rule generation where it matters for the B(2,5) bidirectional strategy.

The theoretical contribution — the carry-over property framework for predicates — is the key insight that makes the biased algorithm principled rather than ad hoc: it gives a checkable condition ensuring that overlap resolution between biased rules always yields biased output, preventing the predicate from "leaking" during the computation.

From a methodology standpoint, the work connects to the broader No Free Lunch framing: no single KB ordering dominates across presentations, and mixing hedges this without requiring a priori knowledge of which ordering is best. The empirical results confirm mixing reduces ordering-sensitivity, at the cost of some overhead.

## Quotes

1. > "The biased Knuth–Bendix algorithm is not designed to produce a complete rewriting system. Its sole purpose is to generate useful rules." — §4.1
2. > "Rather than treating all critical pairs uniformly, the biased procedure attempts to guide the computation toward relations that are more likely to contribute to reductions relevant to the target problem." — Ch. 1

## Open questions surfaced

- Can any target word be reduced to the identity using the biased KB + bidirectional mixing pipeline? (The primary open question of the research program.)
- What is the optimal subword selection strategy (random vs. most-frequent, length distribution)? Is there a theoretical characterization of "useful" subwords?
- Can carry-over properties (or analogues) be used to design predicates that also bias toward rules useful for completeness, not just reduction?
- Can RL or learned heuristics replace the fixed subword predicate with adaptive biasing that updates based on reducer agent feedback?
- Does the biased algorithm terminate on any non-trivial input, and if so under what conditions?
- Can the mixer framework be applied to theorem-proving or SAT-solving with analogous benefit? (Mentioned as future direction in §5.)

## Related material in vault

- Author: [[People/ethan-k|ethan-k]]
- Parent synthesis: [[_synthesis-kuznetsov-b25-algorithmic-line]]
- MOC: [[Research/Group theory/_MOCs/_moc-burnside|_moc-burnside]], [[Research/Group theory/_MOCs/_moc-knuth-bendix|_moc-knuth-bendix]]
- Extends (mixing framework): [[algo-mixing-burnside-slides]]
- Extends (target word strategy): [[havas-wall-wamsley-1974]]
- Cites: [[epstein-et-al-1992-word-processing]] (source of the Ch. 2 KB framework) and Sims 1994, *Computation with Finitely Presented Groups* (third and final bibliography entry; no vault note yet)
- Background: [[knuth-bendix-1970]] — the procedure being biased; not in the thesis bibliography (its KB material is adapted from Epstein et al. and Sims)
- Concepts: [[Concepts/kb-mixing-stagnation]], [[Concepts/mixable-api]]
