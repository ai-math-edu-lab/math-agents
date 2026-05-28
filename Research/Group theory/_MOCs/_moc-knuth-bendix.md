---
title: "Knuth-Bendix — Map of Content"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/knuth-bendix
  - topic/kbmag
  - topic/moc
  - status/validated
---

# Knuth-Bendix — Map of Content

**This MOC is a curated reading path for Knuth-Bendix completion** in the context of finitely presented group theory — from the algorithmic technique itself, through practical KBMAG usage, to the Mixer's cooperative KB approach and its Gröbner alternative. Navigate here when you want to understand how KB works, which tools to use, and how the Mixer improves on single-ordering KB.

---

## The technique

- [[Research/Group theory/Word Problem/techniques/knuth-bendix]] — Foundational technique note: what KB completion is, how termination and confluence interact, the critical-pair algorithm, ordering choices (shortlex vs. RPO vs. wtlex), and what termination/divergence mean for the word problem. The conceptual starting point.

---

## Practical tools

- [[Research/Group theory/Tools/KBMAG/kbmag-tools-overview]] — Decision tree for which KBMAG tool to use; standalone kbprog vs. GAP package; binary locations.
- [[Research/Group theory/Tools/KBMAG/examples/01-s3-shortlex]] — Verified kbprog run on S3 (shortlex, 8 rules). The minimal working example to understand the .kbprog format and read the output.
- [[Research/Group theory/Tools/KBMAG/examples/02-b23-shortlex]] — Verified kbprog run on B(2,3) (fuller presentation, 26 rules). Shows why a complete presentation is needed and what convergence looks like for a Burnside group.
- [[Research/Group theory/Tools/KBMAG/file-formats]] — The .kbprog format, ordering options, and kbprog flag reference.
- [[Research/Group theory/Tools/GAP/examples/05-kbmag-package]] — Using KB via the GAP kbmag package (`KnuthBendix`, `IsConfluent`, `EnumerateReducedWords`). Useful when you want KB integrated with GAP's algebra tools.
- [[package-kbmag]] — Full GAP kbmag package documentation: setup, all key functions, relationship to standalone kbprog.

---

## The Mixer extension

- [[algo-mixing-burnside-slides]] — The B(4,3) breakthrough: two KB orderings (r2l_rpo_loop + rpo_iter) cooperating via rule injection in 33 minutes, 2,333 rules confluent. Verbatim run logs. The primary evidence that cooperative KB outperforms single-ordering KB on hard Burnside instances.
- [[Concepts/kb-mixing-stagnation]] — The stagnation metric and rule-injection protocol extracted from the breakthrough: when and how to inject rules across orderings.
- [[Concepts/mixable-api]] — The mixer_core Agent protocol specification: the interface any KB-variant agent must implement to participate in Mixer cooperation.

---

## Historical context

- [[havas-robertson]] — 1994 survey noting KB "has gradually been playing a more important role in computational group theory" (§2.9), citing Sims (1991) showing KB sometimes outperforms coset enumeration. The academic framing for what the Mixer exploits.

---

## Gröbner alternative

- [[grobner]] — Kreuzer-Myasnikov-Rosenberger (2025 draft): Gröbner basis as a fast-fail "No" oracle for the word problem in FPGs. Structurally a different solver for the same search space. Relevant to KB because the two can cooperate: Gröbner filter eliminates dead-end words before KB explores them.
- [[Concepts/grobner-quotient-filter]] — The SL(n, Q_R) quotient test: use as a fast pre-filter alongside KB. The "Gröbner agent" role in a Mixer.
- [[Concepts/grobner-infinitude-probe]] — The minimal-polynomial test: detect infinitude of a group early, allowing KB to abort before diverging.

---

## Related MOCs

- [[_moc-burnside]] — The Burnside problem that motivates all KB mixing work; navigate there for the open question and historical context.
- [[_moc-word-problem]] — KB as a word-problem algorithm; navigate there for the full decidability landscape and alternative approaches (Dehn function, automatic groups).
