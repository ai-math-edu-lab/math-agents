---
title: "Synthesis — Combinatorial and group-theoretic search: methodology landscape and Mixer-shaped patterns (2026)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/word-problem
  - topic/knuth-bendix
  - topic/coset-enumeration
  - topic/automatic-groups
  - topic/cdcl
  - topic/algorithm-portfolio
  - topic/proof-search
  - synthesis
  - status/draft
papers_synthesized:
  - "[[knuth-bendix-1970]]"
  - "[[dershowitz-jouannaud-1990]]"
  - "[[todd-coxeter-1936]]"
  - "[[epstein-et-al-1992-word-processing]]"
  - "[[korf-1985-ida-star]]"
  - "[[marques-silva-sakallah-1999-grasp]]"
  - "[[1811.06128]]"
  - "[[gomes-selman-2001-portfolios]]"
  - "[[hamadi-et-al-2009-manysat]]"
  - "[[clarke-et-al-2000-cegar]]"
key_concepts:
  - "[[Concepts/kb-mixing-stagnation]]"
  - "[[Concepts/mixable-api]]"
date_range: 1936 to 2021
project: mixer-core
---

# Synthesis — Combinatorial and group-theoretic search: methodology landscape and Mixer-shaped patterns (2026)

> **Synthesis note.** Maps the general methodology landscape for taming large combinatorial/group-theoretic search spaces. Organized in five topic areas per Maria's brief. The primary strategic output is **Section 7: Mixer-shaped methods** — which of the surveyed patterns match the Mixer's "cooperating partial oracles" architecture, what they're called in each field, and what the differences are.
>
> **Scope**: methodology paper notes ingested for this synthesis. Existing AI in Math/ notes cross-linked but not re-summarized: see [[Research/AI in Math/ML/_synthesis-ml-for-math]] and [[Research/AI in Math/RL/_synthesis-rl-for-math]] for the ML/RL-for-combinatorics landscape.

## The question

What is the established methodology landscape for searching large combinatorial and group-theoretic spaces, and which methods instantiate the "partial-No oracle running alongside a complete rewriter" structural motif that underlies the Mixer's design?

## Sources reviewed

**Area 1 — Knuth-Bendix completion & rewriting as search:**
1. [[knuth-bendix-1970]] — Knuth & Bendix (1970): defines KB completion; critical-pair generation as the search operation; semi-decidability for word problems.
2. [[dershowitz-jouannaud-1990]] — Dershowitz & Jouannaud (1990): survey of rewriting theory; divergence, ordering strategies, stagnation theory.

**Area 2 — Coset enumeration + automatic groups:**
3. [[todd-coxeter-1936]] — Todd & Coxeter (1936): original TC coset enumeration; coincidence detection as the dual to KB critical pairs.
4. [[epstein-et-al-1992-word-processing]] — Epstein et al. (1992): automatic groups and KBMAG theory; KB terminates iff group is automatic; quadratic-time word problem.

**Area 3 — Modern search heuristics:**
5. [[korf-1985-ida-star]] — Korf (1985): IDA* — bounded depth-first search with admissible heuristic; the template for word-length-bounded combinatorial search.
6. [[marques-silva-sakallah-1999-grasp]] — Marques-Silva & Sakallah (1999): GRASP/CDCL — learned clauses as persistent "partial-No" witnesses; non-chronological backtracking.

**Area 4 — ML/RL for combinatorial search (cross-linked; not re-summarized here):**
7. [[1811.06128]] — Bengio, Lodi, Prouvost (2021): survey of ML for combinatorial optimization; the calibrating lens for what ML has actually shown vs. hype.
*(Existing vault notes: [[RL/fawzi-2022-alphatensor]], [[ML/romera-paredes-2023-funsearch]], [[ML/2506.13131]], [[ML/romera-paredes-2023-funsearch]], [[RL/1805.07563]])*

**Area 5 — The partial-No oracle + complete rewriter pattern:**
8. [[gomes-selman-2001-portfolios]] — Gomes & Selman (2001): algorithm portfolios; heavy-tailed runtimes; why running multiple algorithms in parallel with information sharing outperforms any single algorithm.
9. [[hamadi-et-al-2009-manysat]] — Hamadi, Jabbour, Sais (2009): ManySAT — parallel CDCL portfolio with clause sharing; super-linear speedup; the most direct Mixer analog in the literature.
10. [[clarke-et-al-2000-cegar]] — Clarke et al. (2000): CEGAR — counterexample-guided abstraction refinement; spurious counterexamples as "partial-No witnesses" that guide targeted abstraction refinement.

## Convergence

**On the structure of hard combinatorial search:**
All surveyed methods grapple with the same fundamental difficulty: the search space is intractably large, but it has structure that can be exploited. The structure shows up differently in each framework:
- KB: equational structure → reduction orderings guide search toward canonical forms
- TC: coset structure → coincidence detection eliminates symmetry
- CDCL: clause structure → conflict analysis derives global constraints from local dead-ends
- Portfolios/CEGAR: algorithmic structure → different algorithms expose different parts of the failure space

**On the role of "partial information":**
Every successful method uses partial information — facts about the search space that are definitely true but don't solve the problem — to prune future search. The forms vary (rules, cosets, learned clauses, counterexamples) but the logical role is the same: **a partial-No witness that eliminates a region of search space permanently**.

**On the fundamental trade-off:**
Every semi-decision procedure for the word problem (KB, TC) terminates iff the answer is "yes" (finite group / decidable equality) — but for hard cases (B(2,5)), no single approach terminates. The portfolio insight is: if different approaches have heavy-tailed but independent runtimes, combining them eliminates the heavy tail.

## Disagreement

**KB vs. TC: which is more useful as a partial oracle?**
- KB produces **rewriting rules** (equalities oriented as reductions). These are directly usable by any other rewriting system.
- TC produces **cosets** (elements identified as equal to known elements). These are less directly portable.
- The Mixer uses KB's rules as the unit of information exchange — a principled choice given that rules are the most portable partial information in the word-problem setting.

**ML/RL: effective or oversold?**
Bengio et al. 2021 [[1811.06128]] provides the honest assessment: ML is effective in specific niches (algorithm selection, heuristics inside exact solvers) but end-to-end ML for hard CO is rarely competitive with OR methods. AlphaTensor, FunSearch, and AlphaEvolve are genuine exceptions that work because they have fast formal evaluators (the Lean checker, the cap-set evaluator) — not because ML alone solves hard combinatorics. This is important context for the Mixer: ML-guided injection is plausible (the algorithm-selection niche), but ML-alone KB completion is not.

## What's settled

1. **KB and TC are dual semi-decision procedures** for the finitely presented group word problem: KB discovers equalities (as rules), TC discovers coset structure. Both terminate iff the answer is finite (or in specific tractable subclasses). [[knuth-bendix-1970]], [[todd-coxeter-1936]].
2. **Automatic groups are the exactly characterizable tractable class**: KB terminates iff the group is automatic; the word problem is then quadratic. [[epstein-et-al-1992-word-processing]].
3. **Heavy-tailed runtimes are generic for hard combinatorial search** (SAT, CSP, group word problems). Portfolio strategies eliminate heavy tails. [[gomes-selman-2001-portfolios]].
4. **Clause sharing in parallel SAT (ManySAT) achieves super-linear speedup** beyond naive parallelism — information sharing is qualitatively different from independent parallel search. [[hamadi-et-al-2009-manysat]].
5. **CDCL learned clauses are persistent partial-No witnesses**: once derived, a clause permanently prunes its conflict region from all future search. [[marques-silva-sakallah-1999-grasp]].
6. **CEGAR's abstraction refinement converges monotonically** — the same spurious counterexample cannot recur after refinement. The "partial-No oracle + complete verifier" loop terminates given a faithful abstraction. [[clarke-et-al-2000-cegar]].

## What's contested

1. **Does portfolio theory apply when algorithms share state?** Gomes & Selman's portfolio theory assumes independence between components. ManySAT and the Mixer break this by sharing clauses/rules. The theoretical guarantees may not hold exactly when sharing creates correlations. Empirically, sharing helps — but the theory is less clean.
2. **Is ML for injection selection actually better than heuristic selection?** The Mixer currently uses overlap-score heuristics (hand-designed). Whether an ML-trained injection policy would do better depends on the problem distribution — Bengio et al. [[1811.06128]] shows distribution mismatch is the main failure mode.
3. **What is the right unit of information for cross-ordering sharing?** The Mixer shares rules (oriented equations). ManySAT shares learned clauses (propositional constraints). CEGAR shares counterexamples (path witnesses). These are structurally different; whether rules are the best unit for the group word problem is an open design question.

## What's open

1. **Is KB completion for B(2,5) heavy-tailed under any single ordering?** Portfolio theory predicts Mixer should help iff yes. The empirical evidence from B(4,3) suggests yes (hours vs. 33 minutes), but no formal characterization exists.
2. **Area 3 gap — SAT/beam search for group word problems**: no published paper found on directly encoding finitely presented group word problems in SAT/SMT or applying beam search with group-theoretic heuristics to word normalization. This is a genuine open research direction. The Gröbner-basis approach ([[grobner]]) is the closest existing work; CDCL-based word problem solvers for specific group classes remain unexplored.
3. **Can CEGAR be formalized for the Mixer?** A rigorous "KB system as abstraction of the group" formalization would make the Mixer's injection step a formal CEGAR refinement — with guaranteed convergence properties. This would give the Mixer a formal completeness argument it currently lacks.
4. **Optimal portfolio composition for KB orderings**: Portfolio theory predicts a saturation point where adding more orderings stops helping. What is the optimal number of KB orderings for the Mixer, and how should they be chosen?

## Methodology notes

**The vocabulary problem**: the "partial-No oracle alongside complete rewriter" pattern appears under at least four names in the literature:
- "Algorithm portfolio with clause sharing" (SAT community, [[gomes-selman-2001-portfolios]], [[hamadi-et-al-2009-manysat]])
- "Counterexample-guided abstraction refinement" (model checking, [[clarke-et-al-2000-cegar]])
- "Cooperative proof search" (ATP community, various)
- "Metaheuristic information exchange" (optimization, various)

These are the same structural motif. The Mixer currently has no formal name for its pattern — "Mixer" is the system name, not the paradigm name. Naming the pattern (e.g., "ordering-portfolio completion with rule sharing") would improve literature connectivity.

**Evaluation methodology gap**: all Area 5 papers evaluate on benchmark distributions (SAT-Race, CSP competition, hardware circuits). The Mixer's B(2,5) attack is a single instance, not a distribution. Portfolio theory's statistical guarantees require a distribution of instances — applying them to a single-instance hard problem is valid but needs careful interpretation.

---

## Section 7 — Mixer-shaped methods: cooperating partial oracles

*Maria's specific synthesis ask: which surveyed methods match the "cooperating partial oracles" structural motif behind the Mixer thesis?*

**The Mixer's structural thesis**: two KB completion agents running under different orderings cooperate by sharing rules. The rules discovered by one agent are "partial-No witnesses" for the other: they certify that certain word-reductions are valid (the words are equal), thereby pruning the other agent's search space. Neither agent alone terminates on B(2,5) (KB diverges under any single ordering), but cooperation can either solve specific target words or accelerate convergence enough to reach a complete system.

**Mixer-shaped methods — ranked by structural fidelity:**

**1. ManySAT (highest fidelity)** [[hamadi-et-al-2009-manysat]]
- Structural match: multiple CDCL threads (orderings in the Mixer) sharing learned clauses (rewriting rules in the Mixer).
- Same: parallel independent search; information shared via a common pool; short/high-quality information only; non-chronological effect (injected rules affect all future search, not just the current branch).
- Different: CDCL clauses are constraints (what NOT to do); KB rules are positive facts (what to reduce). The information type differs even though the mechanism is the same.
- Direct translation: Mixer's rule injection = ManySAT's clause sharing. Mixer's overlap-score filter = ManySAT's short-clause filter.

**2. Algorithm Portfolios (theoretical foundation)** [[gomes-selman-2001-portfolios]]
- Structural match: the formal framework that explains WHY the Mixer helps.
- Same: heavy-tailed runtime → portfolio eliminates tails; information sharing → super-linear speedup.
- Different: the theory assumes independence between components; the Mixer creates correlations via shared rules.
- Use: provides the statistical argument for why multiple orderings with injection outperform single-ordering KB.

**3. CEGAR (deepest analogy)** [[clarke-et-al-2000-cegar]]
- Structural match: abstract verifier (KB system = incomplete, fast) + concrete oracle (full group equality = slow, complete) + spurious counterexamples (words not reduced by current KB but reducible in the group) + targeted refinement (rule injection = adding the right rules to eliminate specific stuck words).
- Same: the "partial-No" oracle is imprecise (KB may fail to reduce a word that IS reducible); the precise oracle (the true group equality) generates a witness (a rule from another ordering's KB) that refines the imprecise oracle.
- Different: CEGAR refines ONE abstraction; the Mixer refines TWO KB systems simultaneously, each providing counterexamples for the other.
- Use: the most intellectually precise analogy. A formal CEGAR analysis of the Mixer would prove convergence properties currently lacking.

**4. CDCL (partial-No structure)** [[marques-silva-sakallah-1999-grasp]]
- Structural match: KB rules are CDCL learned clauses — both are persistent, globally-pruning witnesses derived from dead-ends (conflicts = critical pairs that don't resolve; learned clauses = new rules).
- Same: accumulate-and-prune; the information derived from one dead-end applies to all future search.
- Different: CDCL operates in propositional logic; KB operates in term/string rewriting. The structural analogy is at the level of the learning mechanism, not the object language.

**Methods that are NOT Mixer-shaped:**

- **IDA\*** [[korf-1985-ida-star]]: bounded search with no inter-agent sharing. IDA* is the architecture of each Mixer AGENT's internal search, not the inter-agent cooperation. The Mixer's bidirectional word search uses IDA*-like threshold bounding internally.
- **TC coset enumeration** [[todd-coxeter-1936]]: dual to KB but not easily combined (cosets vs. rules are different information types; no published system combines TC and KB sharing).
- **Automatic groups** [[epstein-et-al-1992-word-processing]]: characterizes when KB terminates WITHOUT needing cooperation. If B(2,5) were automatic, the Mixer would be unnecessary. The fact that B(2,5) is unknown forces the Mixer's portfolio approach.

**Summary table:**

| Method | Mixer analog | What transfers |
|---|---|---|
| ManySAT clause sharing | Rule injection | Architecture, filtering, super-linear speedup |
| Algorithm portfolios | Multi-ordering KB | Heavy-tail elimination, theoretical framework |
| CEGAR refinement | Rule injection | Convergence argument, counterexample semantics |
| CDCL learned clauses | KB rules | Persistent global pruning from dead-ends |
| IDA\* | Internal agent search | Threshold bounding within one agent |

---

## Recommendation

1. **Adopt the "portfolio completion with rule sharing" terminology** for the Mixer to anchor it in the established literature. ManySAT and CEGAR are the strongest published analogs.

2. **Formalize the Mixer as CEGAR**: the B(2,5) Mixer's injection loop is structurally a CEGAR refinement where the "abstraction" is a KB system and "counterexamples" are stuck words. A formal CEGAR analysis would provide convergence guarantees and suggest better stopping criteria.

3. **The Area 3 gap is an opportunity**: no published work applies CDCL/SAT encodings directly to finitely presented group word problems. A SAT encoding of the B(2,5) word problem (possibly via the Gröbner-basis framework of [[grobner]]) could complement the Mixer's rule-injection approach with a purely propositional partial-No oracle.

4. **ML injection policy in the algorithm-selection niche** [[1811.06128]]: train an ML model to select injection targets given the current KB state. This is the Bengio et al. "most reliable ML-for-CO niche" — algorithm selection — applied to the Mixer's injection heuristic. The existing overlap-score heuristic is the baseline; an ML model trained on completed B(4,3) KB trajectories could outperform it on B(2,5).

## Related vault material

- Papers: [[knuth-bendix-1970]], [[dershowitz-jouannaud-1990]], [[todd-coxeter-1936]], [[epstein-et-al-1992-word-processing]], [[korf-1985-ida-star]], [[marques-silva-sakallah-1999-grasp]], [[1811.06128]], [[gomes-selman-2001-portfolios]], [[hamadi-et-al-2009-manysat]], [[clarke-et-al-2000-cegar]]
- Concepts: [[Concepts/kb-mixing-stagnation]], [[Concepts/mixable-api]], [[Concepts/cayley-table-closure-algorithm]]
- AI in Math cross-references: [[Research/AI in Math/RL/_synthesis-rl-for-math]], [[Research/AI in Math/ML/_synthesis-ml-for-math]], [[Research/AI in Math/_MOCs/_moc-ai-in-math]]
- Cross-vault: [[Research/Group theory/Burnside groups/B25/algo-mixing-burnside-slides]] (B(4,3) Mixer — the portfolio completion with rule sharing at work), [[grobner]] (Gröbner-basis approach as an alternative partial-No oracle)
