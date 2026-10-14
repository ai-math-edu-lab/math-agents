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
status: validated
domain: group-theory
---

# Knuth-Bendix — Map of Content

**This MOC is a curated reading path for Knuth-Bendix completion** in the context of finitely presented group theory — from the algorithmic technique itself, through practical KBMAG usage, to the Mixer's cooperative KB approach and its Gröbner alternative. Navigate here when you want to understand how KB works, which tools to use, and how the Mixer improves on single-ordering KB.

---

## The technique

- [[Research/Group theory/Word Problem/techniques/knuth-bendix]] — Foundational technique note: what KB completion is, how termination and confluence interact, the critical-pair algorithm, ordering choices (shortlex vs. RPO vs. wtlex), and what termination/divergence mean for the word problem. The conceptual starting point.

- [[Research/Group theory/Word Problem/knuth-bendix-1970]] — Knuth & Bendix (1970): the original paper. Defines critical-pair generation as the search operation; proves semi-decidability; shows termination iff a complete rewriting system exists. Every subsequent KB system descends from this.

- [[Research/Group theory/Word Problem/dershowitz-jouannaud-1990]] — Dershowitz & Jouannaud (1990): comprehensive survey of rewriting theory including stagnation modes, divergence characterization, and ordering strategies. The standard reference for understanding when and why KB fails. Cross-link: [[Concepts/kb-mixing-stagnation]].

---

## Practical tools

- [[Research/Group theory/Tools/KBMAG/kbmag-tools-overview]] — Decision tree for which KBMAG tool to use; standalone kbprog vs. GAP package; binary locations.
- [[holt-1995-warwick-ags]] — Holt (1995): "The Warwick Automatic Groups Software" — the source publication for the KBMAG software the tool notes above wrap.
- [[Research/Group theory/Tools/KBMAG/examples/01-s3-shortlex]] — Verified kbprog run on S3 (shortlex, 8 rules). The minimal working example to understand the .kbprog format and read the output.
- [[Research/Group theory/Tools/KBMAG/examples/02-b23-shortlex]] — Verified kbprog run on B(2,3) (fuller presentation, 26 rules). Shows why a complete presentation is needed and what convergence looks like for a Burnside group.
- [[Research/Group theory/Tools/KBMAG/file-formats]] — The .kbprog format, ordering options, and kbprog flag reference.
- [[Research/Group theory/Tools/GAP/examples/05-kbmag-package]] — Using KB via the GAP kbmag package (`KnuthBendix`, `IsConfluent`, `EnumerateReducedWords`). Useful when you want KB integrated with GAP's algebra tools.
- [[package-kbmag]] — Full GAP kbmag package documentation: setup, all key functions, relationship to standalone kbprog.
- [[_synthesis-proof-recording-kb-tools-2026-10-14]] — T-017 survey (2026-10-14): which tools record Knuth–Bendix proofs (logged rewriting, GAP `idrel`, KBCV, provers), why none fits B(2,5) scale, and the recommended `kbprog` fork patch.

---

## The Mixer extension

- [[algo-mixing-burnside-slides]] — The B(4,3) breakthrough: two KB orderings (r2l_rpo_loop + rpo_iter) cooperating via rule injection in 33 minutes, 2,333 rules confluent. Verbatim run logs. The primary evidence that cooperative KB outperforms single-ordering KB on hard Burnside instances.
- [[matveeva-2026-ai-problem-solving]] — The current account (Tbilisi 2026), superseding the 2025 deck's numbers: B(4,3) in 13 s on a single rule-sharing event; B(5,3) word problem in 1.5 s via bidirectional beam search; B(2,5) at 76% best / 28% average reduction on the 119 challenge words. Cite this, not the deck, for current numbers.
- [[kalika-2026]] — 2026 Stevens thesis on biased KB completion and algorithm mixing in B(2,5); the thesis-length treatment of the Mixer extension.
- [[Concepts/kb-mixing-stagnation]] — The stagnation metric and rule-injection protocol extracted from the breakthrough: when and how to inject rules across orderings.
- [[Concepts/mixable-api]] — The mixer_core Agent protocol specification: the interface any KB-variant agent must implement to participate in Mixer cooperation.

---

## Complete rewriting systems and KB in groups (2026-08-09 batch)

- [[le-chenadec-1986]] — Le Chenadec (1986): "A Catalogue of Complete Group Presentations" — the classic monograph of finite complete rewriting systems for standard group families.
- [[gilman-1979]] — Gilman (1979): "Presentations of Groups and Monoids" — early use of rewriting presentations for group computation.
- [[epstein-holt-rees-1991]] — Epstein, Holt & Rees (1991): KB methods to solve the word problem in automatic groups — KB as the workhorse behind automatic-structure computation.
- [[epstein-sanders-2000]] — Epstein & Sanders (2000): KB for groups with infinitely many rules — handling infinite regular families of rules.
- [[hermiller-shapiro-1999]] — Hermiller & Shapiro (1999): rewriting systems and geometric three-manifolds — which 3-manifold groups admit finite complete rewriting systems.
- [[book-otto-1993-string-rewriting]] — Book & Otto (1993): "String-Rewriting Systems" — the standard string-rewriting monograph.
- [[tate-2011-equality-saturation]] — Tate et al. (2011): equality saturation — keep all rewrites in an e-graph rather than committing to one; a counterpoint to KB divergence/stagnation. Cross-link: [[Concepts/kb-mixing-stagnation]].

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
