---
title: "Algorithm Cooperation — Map of Content"
author: maumayma
language: en
domain: methodology
status: draft
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/algorithm-portfolio
  - topic/cdcl
  - topic/knuth-bendix
  - topic/moc
  - status/draft
---

# Algorithm Cooperation — Map of Content

**This MOC covers the "cooperating partial oracles" paradigm** — the structural motif behind the Mixer's architecture. Navigate here when you want to understand how multiple incomplete algorithms can cooperate to outperform any single algorithm, and what the theoretical and empirical literature says about when this works, why, and how to engineer it.

⚡ marks papers/notes with documented **Mixer-shaped relevance** (partial-No oracle + complete rewriter pattern). See [[_synthesis-combinatorial-search-methods]] § 7 for the full ranked comparison.

---

## The Mixer breakthrough (primary motivation)

- ⚡ [[algo-mixing-burnside-slides]] — B(4,3) solved in 33 minutes via two KB orderings cooperating: RPO + shortlex, 80-rule injection at 20k rules triggers a cascade from 22s to 14s. The proof-of-concept for cooperative KB completion.

---

## Synthesis

- [[_synthesis-combinatorial-search-methods]] — The full methodology landscape (5 areas: KB/rewriting, coset enumeration + automatic groups, IDA*/CDCL search heuristics, ML/RL for combinatorial search, partial-No oracle pattern). **Section 7** provides the Mixer-shaped-methods ranking: ManySAT > Portfolios > CEGAR > CDCL by structural fidelity. Also flags the Area 3 gap (no SAT/beam-search paper for FPG word problems).

---

## The partial-No oracle + complete rewriter pattern (Area 5)

Three instantiations of the same structural motif, named differently in each community:

- ⚡ [[gomes-selman-2001-portfolios]] — **Algorithm Portfolios** (Gomes & Selman 2001): formal theory; heavy-tailed runtimes → portfolio eliminates the tail; information sharing → super-linear speedup. The theoretical framework. Predicts the Mixer should work for B(2,5) IF KB has heavy-tailed runtimes (empirically likely from B(4,3) data).

- ⚡ [[hamadi-et-al-2009-manysat]] — **ManySAT** (Hamadi, Jabbour, Sais 2009): parallel CDCL portfolio with learned-clause sharing. Won SAT-Race 2008 parallel track. The most direct structural analog to the Mixer: diverse threads + clause sharing = diverse KB orderings + rule injection. **Super-linear speedup from sharing validated experimentally.**

- ⚡ [[clarke-et-al-2000-cegar]] — **CEGAR** (Clarke et al. 2000): counterexample-guided abstraction refinement. Spurious counterexamples from a fast incomplete verifier drive targeted refinement of the abstraction. Recommendation in synthesis: formalize Mixer injection as a CEGAR refinement for convergence guarantees.

---

## General search heuristics (Area 3)

- [[korf-1985-ida-star]] — **IDA\*** (Korf 1985): depth-first iterative-deepening with admissible heuristic. The bounded search template used inside individual Mixer agents (the Mixer's bidirectional word-length search is a bidirectional IDA* variant).

- [[marques-silva-sakallah-1999-grasp]] — **GRASP / CDCL** (Marques-Silva & Sakallah 1999): conflict-driven clause learning. Learned clauses = persistent partial-No witnesses. The architectural core of ManySAT and all modern SAT solvers.

---

## ML/RL for combinatorial search (Area 4)

- [[Research/AI in Math/ML/1811.06128]] — **Bengio, Lodi, Prouvost (2021)** survey: ML for combinatorial optimization — honest assessment of what's shown vs. hype. The calibrating lens. Key finding: algorithm selection (choosing which solver/ordering to use) is the most reliable ML-for-CO application. Direct recommendation: ML injection policy for the Mixer is the algorithm-selection niche.
- ⚡ Cross-links to existing AI in Math notes: [[RL/fawzi-2022-alphatensor]] (AlphaTensor — RL for algorithm discovery; Mixer analog), [[ML/romera-paredes-2023-funsearch]] (FunSearch — evaluator-filtered evolutionary search; direct template for injection policy discovery), [[ML/2506.13131]] (AlphaEvolve — FunSearch extended).

---

## Concept hubs

- ⚡ [[Concepts/kb-mixing-stagnation]] — The stagnation metric: when KB diverges vs. produces useful rules; the injection-trigger conditions observed in B(4,3) experiments.
- ⚡ [[Concepts/mixable-api]] — The Mixer's agent protocol: what any KB-variant agent must implement to participate in rule injection. The "shared clause pool" equivalent for KB.
- [[Concepts/grobner-quotient-filter]] — Gröbner-basis partial-No oracle for word problems in FPGs: the SL(n, Q_R) quotient test as a fast-fail complement to KB.
- [[Concepts/grobner-infinitude-probe]] — Minimal-polynomial test for group infinitude: detects infinite groups early, allowing KB to abort.

---

## Gröbner alternative (a different partial-No oracle)

- [[grobner]] — Kreuzer, Myasnikov, Rosenberger (2025 draft): Gröbner basis as a complementary word-problem oracle. Structurally a partial-No oracle for the same FPG word problem that KB searches. Cross-links [[Concepts/grobner-quotient-filter]] and [[Concepts/grobner-infinitude-probe]].

---

## Related MOCs

- [[Research/Group theory/_MOCs/_moc-knuth-bendix]] — KB completion technique depth; KBMAG tools; the Gröbner alternative. Navigate there for KB-specific implementation.
- [[Research/Group theory/_MOCs/_moc-word-problem]] — Word problem decidability landscape; KB + TC + automatic groups as the algorithmic toolkit. Navigate there for the broader decidability context.
- [[Research/AI in Math/_MOCs/_moc-ai-in-math]] — Full AI-in-math subtree: formal theorem proving, RL for math, ML for combinatorial discovery. Navigate there for the AI dimension of cooperative search.
