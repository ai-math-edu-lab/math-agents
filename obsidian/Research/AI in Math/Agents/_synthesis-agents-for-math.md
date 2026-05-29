---
title: "Synthesis — Agents for math: LLM-driven theorem proving and autoformalization (2020–2025)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/automated-theorem-proving
  - topic/llm-prover
  - topic/autoformalization
  - topic/agentic-reasoning
  - topic/proof-search
  - synthesis
  - status/draft
papers_synthesized:
  - "[[2009.03393]]"
  - "[[2205.11491]]"
  - "[[2205.12615]]"
  - "[[2210.12283]]"
  - "[[trinh-2024-alphageometry]]"
  - "[[alphaproof-2024]]"
  - "[[2504.21801]]"
  - "[[2404.12534]]"
  - "[[2502.03544]]"
key_concepts: []
date_range: 2020-09 to 2025-04
project:
---

# Synthesis — Agents for math: LLM-driven theorem proving and autoformalization (2020–2025)

> **Synthesis note.** Nine papers (2020–2025) covering the emergence of LLMs as formal theorem provers and autoformalization systems. Organized into three paradigmatic arcs: (1) LLM-based proof generation, (2) autoformalization, and (3) neuro-symbolic systems. Each arc represents a distinct approach to the same problem: how do you connect informal mathematical reasoning (what humans do) with formally verified proofs (what computers can check)?

## The question

What have LLM-based agents and neuro-symbolic systems achieved in formal theorem proving and mathematical autoformalization as of 2025, and where do the open frontiers lie?

## Sources reviewed

**Arc 1 — LLM-based proof generation:**
1. [[2009.03393]] — GPT-f (Polu & Sutskever 2020): LLM sampling for MetaMath/Lean proofs; expert iteration; first deep-learning proofs adopted by Metamath library.
2. [[2205.11491]] — HyperTree (Lample et al. 2022, NeurIPS): MCTS over proof trees + online training from failed searches; 56.5%→82.6% on Metamath, 31%→42% on miniF2F.
3. [[2504.21801]] — DeepSeek-Prover-V2 (DeepSeek-AI 2025): recursive subgoal decomposition + RL; 88.9% on miniF2F-test; current (2025) SOTA; open weights.

**Arc 2 — Autoformalization:**
4. [[2205.12615]] — Wu et al. (2022, NeurIPS): LLMs translate informal competition math to Isabelle/HOL; 25.3% direct translation rate; data flywheel improves prover (29.6%→35.2% on MiniF2F).
5. [[2210.12283]] — DSP (Jiang, Welleck et al. 2023, ICLR): informal proof → formal sketch → Isabelle verification; 21%→39% on competition math; foundational scaffolding pipeline.

**Arc 3 — Neuro-symbolic systems:**
6. [[trinh-2024-alphageometry]] — AlphaGeometry 1 (Trinh et al. 2024, Nature): LLM + symbolic deduction engine for IMO geometry; 25/30 problems solved; silver-medalist level; synthetic data only.
7. [[2502.03544]] — AlphaGeometry 2 (Chervonyi et al. 2025): extends AG1; Gemini LM; knowledge-sharing search trees; 54%→84% solving rate; gold-medalist level.
8. [[alphaproof-2024]] — AlphaProof + AG2 (DeepMind 2024): RL-trained Lean 4 prover + AG2; 4/6 IMO 2024 problems; silver-medal equivalent; hardest problem solved.

**Human-AI collaboration:**
9. [[2404.12534]] — Lean Copilot (Song et al. 2024, NeurIPS 2025): LLMs as real-time tactic suggesters in Lean 4 IDE; human-AI collaboration; 74.2% automation rate; 85% better than aesop.

## Convergence

**On the core paradigm:**
All arc 1-3 systems converge on **sample-then-verify**: generate a proof candidate (via LLM sampling or symbolic search), verify formally (MetaMath checker / Lean 4 / Isabelle), and use the verification outcome as a training signal. GPT-f introduced this in 2020; HyperTree upgraded the search; DeepSeek-Prover-V2 upgraded the training curriculum. AlphaProof applies the same paradigm with RL.

**On the training data bottleneck and the data flywheel:**
All papers struggle with the same problem: there is too little formally verified math relative to informally written math. All resolve this via data augmentation:
- GPT-f: expert iteration on model-discovered proofs.
- HyperTree: online learning from failed search traces.
- Wu et al.: autoformalize informal math → training data.
- DSP: use informal proofs as structural guides to generate formal sketches.
- AlphaGeometry: synthesize millions of theorems with a symbolic engine.
- DeepSeek-Prover-V2: recursive decomposition generates sub-lemma training data.

The pattern is universal: the systems that do best generate their own training data rather than relying only on existing formal libraries.

**On benchmarks**: MiniF2F is the standard benchmark across arc 1. Progress: GPT-f → ~35%, HyperTree → ~42%, Wu et al. → 35.2% (different approach), DeepSeek-Prover-V2 → **88.9%** (2025 SOTA). The benchmark is approaching saturation.

## Disagreement

**Formal vs. informal reasoning gap:**
[[2504.21801]] reports that DeepSeek-V3 (informal) solves 8/15 AIME problems vs. DeepSeek-Prover-V2 (formal) solving 6/15 — formal is still *harder* than informal on competition math. However, the paper argues the gap is "substantially narrowing." Whether this narrowing continues or stalls is contested.

**Autonomy vs. collaboration:**
[[2404.12534]] (Lean Copilot) implicitly argues against full autonomy: "human insights may be critical" for genuinely novel theorems. Papers [[alphaproof-2024]] and [[2504.21801]] implicitly argue that sufficient scale (RL at 671B parameters) approaches autonomy. The disagreement is real: Lean Copilot targets tasks where autonomous provers fail; autonomous provers target tasks where human assistance is too slow.

**Neuro-symbolic vs. pure LLM:**
AlphaGeometry (arcs 3) is neuro-symbolic: the symbolic engine enforces deductive validity. Pure LLM provers (arc 1) rely on the formal language checker for correctness. For geometry, neuro-symbolic wins decisively (AlphaGeometry >> any pure LLM on olympiad geometry). For algebra/number theory, pure LLM + RL (AlphaProof) is SOTA. The right architecture may be domain-dependent.

## What's settled

1. **LLMs can generate formally correct proofs** for a wide range of Lean/Isabelle problems (MiniF2F ~89%). This was uncertain in 2020 (GPT-f was promising but limited); it is settled in 2025.
2. **MCTS + online learning outperforms linear beam search** (HyperTree established this, replicated and extended by subsequent systems).
3. **Autoformalization is practical**: LLMs can translate 25%+ of competition math problems correctly to Isabelle/HOL (Wu et al.); with sketch decomposition, this rises to 39% proving rate (DSP).
4. **Neuro-symbolic systems reach gold-medalist level on geometry** (AG2: 84% on 25 years of IMO geometry).
5. **RL from formal verification scales**: AlphaProof + DeepSeek-Prover-V2 both use RL with Lean 4 as the reward signal and achieve SOTA results.
6. **Combinatorics remains the hardest domain**: AlphaProof solved 0/2 combinatorics IMO problems; this is a consistent finding across all systems.

## What's contested

1. **Whether current systems have crossed into genuine mathematical reasoning or sophisticated pattern matching.** AlphaGeometry discovers a "generalized" IMO theorem (suggests reasoning); IMO Problem 6 (hardest problem, solved by AlphaProof) strongly suggests reasoning capability. But the underlying mechanism is not yet understood theoretically.
2. **Whether MiniF2F at 89% is meaningful.** The benchmark may be saturated; [[2504.21801]] introduces ProverBench and AIME formalization to address this. But ProverBench was created by the same team — potential benchmark bias.
3. **Whether formal proofs can be generated for research-level mathematics** (not competition problems). DeepSeek-Prover-V2 solves 7.5% of Putnam (graduate-level competition); research math remains open.

## What's open

1. **Combinatorics for AI**: no system has cracked olympiad combinatorics. This is the next major frontier.
2. **Research-level mathematics**: all systems are evaluated on competition benchmarks. Can LLM provers help with open research problems (e.g., Burnside group finiteness, Riemann hypothesis)?
3. **Lean 4 Mathlib as training ground**: Mathlib 4 contains 100k+ formalized theorems in diverse areas (including group theory). Systematic training on Mathlib 4 could yield a prover specialized for research-level algebra.
4. **The formal-informal gap at scale**: DeepSeek-Prover-V2 narrows but doesn't close the gap. Is there a scale at which formal provers equal informal reasoners on competition math?
5. **Burnside group formalization**: Lean 4 Mathlib includes some group theory. Can AlphaProof or Lean Copilot help formalize B(4,3) results from `algo-mixing-burnside-slides` or word problem decision procedures?

## Methodology notes

**Benchmark saturation**: MiniF2F went from 31% (2022) to 88.9% (2025) in 3 years. The field is creating new harder benchmarks (ProverBench, PutnamBench) to keep evaluation meaningful. Any SOTA claim from 2022-2024 is likely already superseded.

**Open vs. closed systems**: AlphaProof is closed-source; DeepSeek-Prover-V2 is open-weight. The field benefits most from open systems where methods can be studied and replicated.

**Cross-domain vs. domain-specific**: AlphaGeometry is geometry-specific; AlphaProof and DeepSeek-Prover-V2 are general. The tradeoff: domain-specific systems reach higher performance (AG2 gold-medalist on geometry); general systems scale to broader problems.

## Recommendation

For the Mixer workstream:

1. **Immediate cross-domain relevance: formal verification of Mixer results.** If the Mixer proves B(4,3) or B(2,5) computational results, [[2404.12534]] (Lean Copilot) is the natural tooling for formalizing those results in Lean 4. The Lean 4 Mathlib group theory infrastructure is the starting point.

2. **AlphaGeometry's knowledge-sharing mechanism** ([[2502.03544]]) is worth reading for the Mixer's parallel agent design: AG2's mechanism for sharing discovered lemmas across parallel search trees is the architecture-level analog of rule injection between Mixer Agents.

3. **The informal-to-formal flywheel** (Wu et al. → DSP → DeepSeek-Prover-V2) is applicable to any domain where informal mathematical work exists. If informal proofs of B(2,5) structural results are available (from algebraist collaborators), DSP-style autoformalization could convert them to Lean 4 proofs with human-AI collaboration via Lean Copilot.

4. **Combinatorics gap = the hard part**: the Burnside finiteness problem involves combinatorial structure (word combinator growth in free groups). Systems that struggle with combinatorics IMO problems will likely struggle with Burnside problems too. AlphaProof-style RL on group theory proofs in Lean 4 is the longer-term bet.

## Related vault material

- Papers: [[2009.03393]], [[2205.11491]], [[2205.12615]], [[2210.12283]], [[trinh-2024-alphageometry]], [[alphaproof-2024]], [[2504.21801]], [[2404.12534]], [[2502.03544]]
- Cross-vault: [[algo-mixing-burnside-slides]] (analog: rule injection = auxiliary construction), `Research/Group theory/Burnside groups/B25/` (domain where formal proofs would be most valuable)
- Upcoming syntheses: `Research/AI in Math/RL/_synthesis-rl-for-math.md` (sub-area B), `Research/AI in Math/ML/_synthesis-ml-for-math.md` (sub-area C)
