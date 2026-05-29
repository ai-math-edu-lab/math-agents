---
title: "Synthesis — ML for math (non-agent, non-RL): neural heuristics, equation discovery, and mathematical algorithm search (2017–2025)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/premise-selection
  - topic/symbolic-regression
  - topic/funsearch
  - topic/mathematical-discovery
  - topic/proof-search
  - synthesis
  - status/draft
papers_synthesized:
  - "[[1701.06972]]"
  - "[[2006.11287]]"
  - "[[raayoni-2021-ramanujan]]"
  - "[[2306.15626]]"
  - "[[romera-paredes-2023-funsearch]]"
  - "[[2506.13131]]"
key_concepts: []
date_range: 2017-01 to 2025-06
project:
---

# Synthesis — ML for math (non-agent, non-RL): neural heuristics, equation discovery, and mathematical algorithm search (2017–2025)

> **Synthesis note.** Six papers covering ML applied to mathematics without the RL training loop or the fully-agentic formal proof search paradigm. Four organizing paradigms: (i) neural heuristics inside solvers, (ii) equation and conjecture discovery, (iii) evolutionary LLM program search, and (iv) embeddings + retrieval for formal proof assistants. Cross-references to [[_synthesis-agents-for-math]] (neuro-symbolic arc) and [[_synthesis-rl-for-math]] (AlphaTensor, algorithm discovery via RL).

## The question

What has ML contributed to mathematics outside the RL training loop and formal proof search — in the areas of discovering equations, finding new algorithms, guiding symbolic reasoning, and representing mathematical objects?

## Sources reviewed

**Paradigm 1 — Neural heuristics inside existing solvers:**
1. [[1701.06972]] — Loos, Irving, Szegedy, Kaliszyk (2017, LPAR-21): first deep-network-guided proof search in E theorem prover; premise selection from Mizar proofs; 7.36% of previously-unproved theorems now proved; foundational "ML as heuristic inside existing solver" paper.

**Paradigm 2 — Equation and conjecture discovery:**
2. [[2006.11287]] — Cranmer et al. (2020, NeurIPS): GNN + symbolic regression extracts symbolic equations from trained neural networks; discovers new analytic formula for dark matter concentration.
3. [[raayoni-2021-ramanujan]] — Raayoni et al. (2021, Nature): Ramanujan Machine; MITM-RF algorithm generates new polynomial continued fraction conjectures about π, e, ζ values; some previously unknown; proves conjecture generation is automatable.

**Paradigm 3 — Evolutionary LLM program search (FunSearch line):**
4. [[romera-paredes-2023-funsearch]] — Romera-Paredes et al. (2023, Nature): FunSearch; LLM-guided evolutionary search over Python programs; discovers new cap set bounds and bin packing heuristics; evaluator filters LLM confabulations.
5. [[2506.13131]] — Novikov et al. (2025, arXiv): AlphaEvolve; FunSearch extended with Gemini; 67+ mathematical and engineering problems; discovers 4×4 complex matrix multiplication with 48 multiplications (first Strassen improvement in this setting after 56 years).

**Paradigm 4 — Embeddings + retrieval for formal math:**
6. [[2306.15626]] — Yang et al. (2023, NeurIPS): LeanDojo / ReProver; open-source Lean 4 infrastructure + retrieval-augmented prover; embeddings of Mathlib 4 premises for premise selection; outperforms GPT-4 on a challenging hard-generalization benchmark.

## Convergence

**ML improves guided search across scales**: whether the search is inside an existing clause-selection loop (Loos 2017), in the space of symbolic expressions (Cranmer 2020, Ramanujan Machine), in a program-function space (FunSearch, AlphaEvolve), or in a tactic-proof space via retrieval (LeanDojo), the pattern is the same: ML provides a learned prior that guides combinatorial search toward promising regions.

**Evaluator + generator separation**: all three recent systems (FunSearch, AlphaEvolve, LeanDojo/ReProver) maintain a strict separation between:
- **Generator** (LLM or SR): proposes candidates.
- **Evaluator** (formal verifier or mathematical scorer): filters/ranks proposals.
This separation eliminates confabulation at the output level — the evaluator ensures formal correctness even when the generator hallucinates.

**Mathematical novelty is the differentiator**: the most impactful papers in this batch make claims of genuine mathematical novelty:
- Cranmer 2020: new dark matter concentration formula.
- FunSearch 2023: new cap set bounds (asymptotic improvement).
- AlphaEvolve 2025: new matrix multiplication algorithm for 4×4 complex matrices.
- Ramanujan Machine: new conjectures about mathematical constants.
None of the five "genuinely novel mathematics" papers are in the RL or Agents sub-areas — mathematical discovery is primarily a sub-area C contribution.

## Disagreement

**Proof generation vs. mathematical discovery**: the Loos/Kaliszyk/LeanDojo papers improve performance on proving things humans already formalized. The FunSearch/AlphaEvolve/Ramanujan Machine papers discover mathematical content that humans haven't previously worked out. These are different problem classes; the paradigms don't compete, they complement.

**Formal vs. informal mathematical knowledge**: Cranmer 2020 and Ramanujan Machine work with informal mathematical objects (physical laws, number constants) and don't produce formal proofs. LeanDojo and Loos 2017 work with formal proof systems. FunSearch and AlphaEvolve are intermediate — they produce formally-verified programs, but not Lean 4 / Isabelle proofs.

## What's settled

1. **Neural premise selection outperforms handcrafted heuristics** for ATP (Loos 2017, LeanDojo both demonstrate this in different prover ecosystems).
2. **GNN + symbolic regression can extract interpretable equations from neural networks** (Cranmer 2020 — demonstrated on physics examples; dark matter formula is independently useful).
3. **Evolutionary LLM search can discover new mathematical constructions** (FunSearch and AlphaEvolve both demonstrate this on open mathematical problems — not just solving known problems faster).
4. **Retrieval-augmented generation improves LLM theorem proving** significantly (LeanDojo/ReProver vs. non-retrieval baseline and GPT-4).
5. **Combinatorics and combinatorial optimization are tractable for ML discovery** (cap set, bin packing in FunSearch; matrix multiplication in AlphaEvolve and AlphaTensor).

## What's contested

1. **Does ML-guided mathematical discovery scale to research-level open problems?** FunSearch found cap set improvements; AlphaEvolve found a Strassen improvement. But these are specific, well-defined optimization problems with fast evaluators. Most research-level math doesn't have an evaluator. Whether the paradigm generalizes is untested.
2. **Is symbolic regression a general equation-discovery tool or just a physics tool?** Cranmer 2020 applies SR to physics; Ramanujan Machine applies it to mathematical constants via continued fractions. No paper tests SR on pure algebraic structures (group theory, number theory beyond constants).

## What's open

1. **ML-guided KB completion**: AlphaEvolve's evaluator-filtered evolutionary search is a direct template for discovering better Mixer rule-injection heuristics. Not yet attempted in the Mixer domain.
2. **Symbolic regression for Burnside group data**: the growth function $|P_s(2,5)|$ from [[kuznetsov-shlepkin-2009]] and [[kuznetsov-shlepkin-2010]] is a finite series with known values ($s = 1, \ldots, 35$). Applying Cranmer's pipeline (or PySR directly) could reveal whether there's a closed-form expression.
3. **Ramanujan Machine for group theory**: the MITM-RF algorithm generates conjectures about number-theoretic constants. Whether the same algorithmic approach generates useful conjectures about group-theoretic quantities (e.g., subgroup indices of B(2,5)) is untested.
4. **Formal ML-guided mathematical discovery**: all current ML discovery papers work with informal verifiers (evaluators score correctness numerically/heuristically). Combining formal verification (Lean 4) with evolutionary/SR search would give provably-correct discovered results — not yet published.

## Methodology notes

**Open-source hygiene**: this batch is notably open-source — LeanDojo is MIT-licensed with all data + models; PySR (Cranmer) is publicly available; FunSearch and AlphaEvolve code released. Contrast with some Agents papers (AlphaProof is closed). Better infrastructure for community replication.

**The AlphaTensor/AlphaEvolve matrix multiplication overlap**: both find faster matrix multiplication algorithms in different mathematical settings (AlphaTensor: 4×4 real-valued over Z₂ via RL; AlphaEvolve: 4×4 complex-valued via evolutionary search). These are not contradictory — they improve different problem variants. Both are relevant to the Mixer because KB rule databases use similar combinatorial structures.

## Recommendation

For the Mixer workstream:

1. **Highest-priority experiment (ML for math → Mixer)**: implement an AlphaEvolve/FunSearch-style evolutionary LLM loop for Mixer rule injection policy discovery. The evaluator is KB convergence speed. The generator proposes Python injection policies (e.g., scoring functions for rule overlap). The evolutionary loop discovers injection heuristics better than human-designed ones.

2. **Low-cost experiment (symbolic regression)**: apply PySR (Cranmer 2020) to the $|P_s(2,5)|$ data points from Kuznetsov's papers ([[kuznetsov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]]). This is a weekend experiment that could reveal the asymptotic structure of the minimal-word growth function.

3. **Lean 4 infrastructure for formal verification**: LeanDojo/ReProver ([[2306.15626]]) + Lean Copilot ([[2404.12534]]) together form the Lean 4 ecosystem infrastructure for formalizing Mixer results. If B(4,3) finiteness (from [[algo-mixing-burnside-slides]]) is to be formally verified, start with these tools.

4. **Ramanujan Machine for conjecture scoping**: the Ramanujan Machine approach (exhaustive search over a structured formula space) could be applied to generate candidate formulas for B(2,5) structural invariants — a low-cost experiment for conjecture generation in the algebraic setting.

## Related vault material

- Papers: [[1701.06972]], [[2006.11287]], [[raayoni-2021-ramanujan]], [[romera-paredes-2023-funsearch]], [[2306.15626]], [[2506.13131]]
- Cross-sub-area: [[fawzi-2022-alphatensor]] (RL/ — algorithm discovery via RL, structurally adjacent to FunSearch), [[trinh-2024-alphageometry]] and [[2502.03544]] (Agents/ — neuro-symbolic overlap with Agents arc 3)
- Cross-vault: [[kuznetsov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]] (target for SR experiment), [[algo-mixing-burnside-slides]] (target for evolutionary search experiment)
- Prior syntheses: [[_synthesis-agents-for-math]], [[_synthesis-rl-for-math]]
