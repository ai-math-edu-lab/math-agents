---
title: "Knuth-Bendix for Groups with Infinitely Many Rules"
authors: D.B.A. Epstein, Paul Sanders
year: 2000
venue: "International Journal of Algebra and Computation 10 (2000) — arXiv:math/0001035"
url: "https://arxiv.org/abs/math/0001035"
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 3
citation_count_date: 2026-06-11
key_concepts:
  - "[[Concepts/complete-rewriting-systems]]"
extends:
  - "[[epstein-holt-rees-1991]]"
contradicts: []
replicates: []
cites:
  - "[[knuth-bendix-1970]]"
  - "[[epstein-et-al-1992-word-processing]]"
  - "[[holt-1995-warwick-ags]]"
  - "[[epstein-holt-rees-1991]]"
cited_by: []
quality_notes: "Published in IJAC 10 (2000), DOI 10.1142/S0218196700000352; the arXiv version (math/0001035) is the freely available copy. Only 3 citations (Semantic Scholar, 2026-06-11) — low reception despite a strong idea, plausibly because the welding machinery is intricate and the approach was never folded back into the mainstream KBMAG distribution. The paper is the explicit theoretical successor to Epstein-Holt-Rees 1991: it pushes the KB-plus-automata philosophy from finite partial output to a genuinely infinite (but regular) rule set encoded in a single two-variable automaton."
author: ethan-k
tags:
  - agent/research
  - user/ethan-k
  - domain/group-theory
  - topic/knuth-bendix
  - topic/word-problem
  - topic/automatic-groups
  - topic/finite-state-automata
  - topic/rewriting-systems
  - topic/regular-languages
  - topic/shortlex-ordering
  - topic/confluence
  - paper
  - status/draft
---

# Knuth-Bendix for Groups with Infinitely Many Rules

## Abstract

We introduce a new class of groups with solvable word problem, namely groups specified by a confluent set of short-lex-reducing Knuth–Bendix rules which form a regular language. This simultaneously generalizes short-lex-automatic groups and groups with a finite confluent set of short-lex-reducing rules. We describe a computer program which looks for such a set of rules in an arbitrary finitely presented group. Our main theorem is that our computer program finds the set of rules, if it exists, given enough time and space. (This is an optimistic description of our result — for the more pessimistic details, see the body of the paper.) The set of rules is embodied in a finite state automaton in two variables. A central feature of our program is an operation, which we call welding, used to combine existing rules with new rules as they are found. Welding can be defined on arbitrary finite state automata, and we investigate this operation in abstract, proving that it can be considered as a process which takes as input one regular language and outputs another regular language. In our programs we need to convert several non-deterministic finite state automata to deterministic versions accepting the same language. We show how to improve somewhat on the standard subset construction, due to special features in our case. The Knuth–Bendix process normally spends most of its time in reduction, so its efficiency depends on doing reduction quickly. Standard data structures for doing this can become very large, ultimately limiting the set of presentations of groups which can be so analyzed. We are able to give a method for rapid reduction using our much smaller two variable automaton, encoding the (usually infinite) regular language of rules found so far.

## TL;DR

Where Epstein-Holt-Rees 1991 ran Knuth–Bendix, stopped early, and guessed an automatic structure from a *finite* partial rule set, this paper makes the **infinite regular rule set itself** the object of computation: it runs KB directly against a possibly-infinite confluent rule language encoded in one two-variable finite-state automaton. The key new primitive is **welding** — an operation on automata that lets a finite machine generate (and reduce with respect to) infinitely many rules at once, with much smaller space than storing finite rule lists. Main theorem (6.13): if the unique confluent set of short-lex-minimal rules for `(G, A)` is regular, the procedure provably stabilizes to the automaton accepting it — but there is no way to know *when* stabilization has occurred.

## Problem

For infinite finitely-presented groups arising in low-dimensional topology, standard Knuth–Bendix "will run for ever on even the most innocuous hyperbolic triangle groups." For a short-lex-automatic group the minimal set of KB rules may be infinite, yet it is *always a regular language* (Section 2.11) and so encodable by a finite state machine. The prior Warwick strategy (Holt; Epstein-Holt-Rees) was: run KB for a heuristically-chosen time, interrupt, guess an automatic structure from the finite rules collected, then axiom-check. The standard finite-rule data structures consume space that ultimately caps which presentations can be analyzed. The question this paper asks: can one perform the Knuth–Bendix process *directly* against the (usually infinite) regular rule set — represented compactly as a two-variable automaton — so that reduction is fast and space-efficient, rather than ever materializing a finite list of rules?

## Approach

The procedure operates on a **two-variable finite-state automaton** (a "rule automaton" / `WDiff`, the word-difference machine) whose accepted pairs `(u, v)` encode rewrite rules `u → v` with `ū = v̄` in G (Sections 2, 5).

**Welding (Section 3) — the central new idea.** Welding is an operation on an arbitrary finite-state automaton that fuses states/arrows so that a machine which originally accepted only finitely many equalities `(u, v)` comes to accept *infinitely many* distinct equalities, while typically becoming *smaller*. Epstein and Sanders prove welding is well-defined as a map from regular languages to regular languages (Section 3.5), and that welding a rule automaton yields a rule automaton (i.e. it preserves the invariant `ū = v̄`). Welding is "the tool which enables us to perform the apparently impossible task of generating an infinite set of Knuth–Bendix rules from a finite set."

**Our Knuth–Bendix (Sections 4–5).** Section 4 recaps standard string-rewriting KB as a baseline. Section 5 gives the variant: critical-pair analysis, rule minimization, and reduction performed by reading a word into the two-variable automaton encoding the current rule language `Rules[n]`, rather than searching a finite list of left-hand sides. New rules trigger welding and state-amalgamation on `WDiff`.

**Determinization improvement (Section 8).** The procedure repeatedly converts non-deterministic two-variable automata to deterministic ones; the authors axiomatize special features of their setting that let them improve on the textbook subset construction, and present the improvements abstractly in the hope they transfer to other applications.

**Reduction algorithm (Sections 7–8).** A companion word-reduction algorithm designed for space, using the compact automaton rather than a finite rule table. Reduction is the dominant cost in KB, so the data-structure choice is the practical crux.

## Key result

**Theorem 6.13 (Correctness of the procedure).** Let G be a group with a given finite presentation and a given ordering of the generators and their inverses. Suppose the set of U-minimal rules is regular (for example if `(G, A)` is short-lex-automatic). Then the procedure of 5.6 stabilizes at some `n₀` with `Rules[n+1] = Rules[n]` for all `n ≥ n₀`, and the stable language P is that of an explicitly-constructible two-variable finite-state automaton. **Caveat (stated in the theorem itself):** "Unfortunately we do not have a method of knowing when or whether we have reached `n₀`." — Section 6.

- **Convergence is "if and only if" on regularity.** The program finds the finite state machine accepting the unique confluent set of short-lex minimal rules **if and only if** that set is a regular language (Section 1, Section 6).
- **The new group class.** Groups specified by a confluent regular set of short-lex-reducing rules. This **simultaneously generalizes** (a) short-lex-automatic groups and (b) groups with a *finite* confluent short-lex-reducing system (Section 2). All such groups have solvable word problem and (Section 3, end) are finitely presented.
- **U-minimal rule structure (Proposition 2.9).** The set of U-minimal rules is confluent and satisfies the standard assumptions; for a U-minimal rule with `u = u₁…u_{n+r}`, `v = v₁…v_n`, one has `0 ≤ r ≤ 2` with explicit constraints on the boundary letters. The set of U-minimal rules is recursive **iff** G has solvable word problem.
- **Reduction cost (Abstract, Section 9.7).** Reduction with the two-variable automaton is slower than KBMAG's finite-automaton reduction "by a factor of around three, because the word has to be read into two or three different automata" — acceptable given that reduction is against an *infinite* rule set whereas KBMAG reduces against a finite one.

## Assumptions

- **It is a group, not a monoid.** The most important assumption (Section 1): the construction relies on inverses. An involution `ι: A → A` with `ι(x)` representing `x⁻¹` is given, and `x·ι(x)` is Thue-equivalent to the empty word (Standard Assumption 2.2.1).
- **Fixed finite ordered generating set A** closed appropriately under the involution; short-lex order is induced from the total order on A.
- **G is finitely presented** (a finite set of defining relations is given).
- **Effectiveness presupposes short-lex-automaticity.** The procedures "are perhaps unlikely to be of much help unless the group actually is short-lex-automatic" (Section 1). The correctness theorem's hypothesis (U-minimal rules regular) is implied by short-lex-automaticity but is formally weaker.

## Limitations / scope

- **No termination detection.** The fatal practical caveat, stated inside Theorem 6.13: there is no method of knowing whether or when `Rules[n]` has stabilized. The "optimistic" abstract statement ("finds the set of rules, if it exists, given enough time and space") hides this.
- **Short-lex-automaticity is undecidable in general** (Section 1), so no algorithm can certify in advance that the favorable hypothesis holds.
- **Reduction is a constant factor slower** than KBMAG (~3×), and the Section 7.13 method is slower again by a constant factor than reading a word into a single DFA (Section 9.7).
- **Mixed scorecard versus KBMAG (Section 9.7).** KBMAG advantages: faster reduction; it can defer constructing its P-analogue until after KB halts; it has no analogue of the extra automaton `Q(Rules[n])` this method must maintain. This method's advantages: cheap automaton updates as rules are found; a *principled* stopping heuristic (`Rules[n+1] = Rules[n]`) versus KBMAG's "inevitably arbitrary" heuristic; and no indefinite oscillation of the word-difference set (which KBMAG can suffer when redundant rules introduce and later eliminate word differences, requiring interactive user intervention).
- **Largely unvalidated at scale.** The authors state the main advantage "will only become evident (if it exists at all) when looking at very large examples" and only *plan* a systematic comparison over SnapPea-generated groups (Section 9.7) — not carried out in the paper.

## Replication evidence

`partial`. The paper describes a working computer program, but the welding-based approach was not adopted into the distributed KBMAG package (the de-facto standard, [[holt-1995-warwick-ags]] and its successor KBMAG2), which retains finite-rule automaton methods. With only 3 recorded citations there is no independent reimplementation in the vault's literature. The abstract welding result (regular-language → regular-language) is a self-contained formal contribution that stands on its proof regardless of the implementation's adoption.

## Why this paper matters

This is the conceptual end-point of the Warwick "use an automaton to tame Knuth–Bendix" program. Epstein-Holt-Rees 1991 ([[epstein-holt-rees-1991]]) and the *Word Processing in Groups* monograph ([[epstein-et-al-1992-word-processing]]) used finite-state automata to *certify* a guessed automatic structure extracted from finite KB output. This paper inverts the relationship: the infinite regular rule language *is* the primary data structure, and KB is run against it directly via welding. That reframing is what lets the method (in principle) reduce with respect to an infinite rule set in bounded space — the recurring bottleneck documented empirically in the 1991 paper.

For the vault's interest in **algorithm cooperation and stagnation**, the paper is a clean case study in a single-strategy method whose theoretical guarantee (Theorem 6.13) is undercut by an undetectable stopping point: the algorithm provably converges but cannot recognize that it has, so in practice it still depends on heuristics, aborting (Section 9.1), and priority rules (Section 9.2). The honest "optimistic vs. pessimistic" framing of its own main theorem makes it a useful counter-weight to benchmark-optimistic algorithm papers.

The **welding** operation — and the axiomatized improvement to the subset construction (Section 8) — are reusable automata-theoretic contributions that the authors explicitly offer for use beyond group theory.

## Quotes

1. > "Our main theorem ... is that our Knuth–Bendix procedure succeeds in constructing the finite state machine which accepts the (unique) confluent set of short-lex minimal rules describing a group, if and only if this set of rules is a regular language." — Section 1

2. > "Unfortunately we do not have a method of knowing when or whether we have reached n₀." — Theorem 6.13

## Open questions surfaced

- **Detecting stabilization.** Theorem 6.13 guarantees convergence but gives no stopping criterion. Is there a verifiable certificate (analogous to the axiom-checking of automatic groups) that `Rules[n]` has reached the full minimal-rule language, rather than the heuristic `Rules[n+1] = Rules[n]`?
- **Where does welding pay off?** The authors conjecture the advantage shows only on "very large examples" and defer a SnapPea-based comparison. For which families of hyperbolic / 3-manifold groups does the compact two-variable automaton actually beat KBMAG's finite-rule machinery in space?
- **Transfer of the subset-construction improvement.** Section 8 axiomatizes special features enabling a better-than-standard determinization. Which other automata-pipeline applications satisfy those axioms?
- **Cooperation angle.** Given KBMAG's complementary strengths (fast reduction, no `Q` automaton) and this method's (cheap updates, principled stopping, no word-difference oscillation), could a hybrid run both representations and switch — turning the Section 9.7 scorecard into a cooperative strategy?

## Related material in vault

- Parent overview: [[word-problem-overview]]
- MOC: [[Research/Group theory/_MOCs/_moc-knuth-bendix|_moc-knuth-bendix]]
- MOC: [[Research/Group theory/_MOCs/_moc-word-problem|_moc-word-problem]]
- Concept hub: [[Concepts/complete-rewriting-systems]] (this paper is the "infinitely many rules" branch of the complete-rewriting-systems story)
- Extends: [[epstein-holt-rees-1991]] (carries the KB-plus-automata philosophy from finite partial output to an infinite regular rule set)
- Cites: [[knuth-bendix-1970]] (the base procedure), [[epstein-et-al-1992-word-processing]] (automatic-group axiom-checking framework), [[holt-1995-warwick-ags]] (the KBMAG lineage it is compared against in Section 9.7)
- Technique hub: [[Research/Group theory/Word Problem/techniques/knuth-bendix|knuth-bendix]]

---

*Author: [[People/ethan-k|ethan-k]]*
