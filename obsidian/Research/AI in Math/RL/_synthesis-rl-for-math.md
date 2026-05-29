---
title: "Synthesis — RL for math: reward-learning and search in formal and informal mathematical reasoning (2018–2024)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/reinforcement-learning
  - topic/process-reward-model
  - topic/value-network
  - topic/automated-theorem-proving
  - topic/proof-search
  - synthesis
  - status/draft
papers_synthesized:
  - "[[1805.07563]]"
  - "[[2305.20050]]"
  - "[[2312.08935]]"
  - "[[2402.03300]]"
  - "[[fawzi-2022-alphatensor]]"
key_concepts: []
date_range: 2018-05 to 2024-02
project:
---

# Synthesis — RL for math: reward-learning and search in formal and informal mathematical reasoning (2018–2024)

> **Synthesis note.** Five papers covering RL applied to mathematical reasoning and algorithm discovery. This synthesis should be read alongside [[_synthesis-agents-for-math]], where AlphaProof ([[alphaproof-2024]]) and DeepSeek-Prover-V2 ([[2504.21801]]) — the two major RL-trained formal provers — are covered as primary notes. This synthesis focuses on the RL training methodology arc, not the prover systems themselves.

> **AlphaZero context** (no separate note per Maria's directive): AlphaZero (Silver et al. 2017-2018, arXiv 1712.01815) is the architectural ancestor of several systems here — its MCTS + value network + policy network + self-play paradigm is directly imported by [[1805.07563]] (theorem proving), [[fawzi-2022-alphatensor]] (algorithm discovery), and [[alphaproof-2024]] (formal proof search). AlphaZero is not ingested as a separate note because it is not math-specific; this paragraph provides the architectural anchor.

## The question

What RL techniques have been developed specifically for mathematical reasoning (formal or informal), and how do they relate to each other and to the broader system-level work in [[_synthesis-agents-for-math]]?

## Sources reviewed

**RL for formal proof search:**
1. [[1805.07563]] — Kaliszyk, Urban et al. (2018, NeurIPS): first RL for theorem proving; MCTS + value network on HOL Light; 40% more problems solved than baseline.

**Process reward models for informal math:**
2. [[2305.20050]] — Lightman et al. (2023, OpenAI): PRMs outperform ORMs for MATH dataset; 78% on MATH with human-labeled step supervision; released PRM800K.
3. [[2312.08935]] — Wang et al. (2024, ACL): Math-Shepherd; automatic PRM training without human annotation; 77.9%→84.1% on GSM8K.
4. [[2402.03300]] — Shao et al. (2024, DeepSeekMath): GRPO algorithm; 51.7% on MATH at 7B parameters; pretraining on 120B math tokens.

**RL for algorithm discovery:**
5. [[fawzi-2022-alphatensor]] — Fawzi et al. (2022, Nature): AlphaTensor; AlphaZero-style RL for discovering faster matrix multiplication algorithms; beats Strassen for 4×4 matrices in Z₂.

## Convergence

**RL is the unifying methodology**: all five papers use reinforcement learning as the primary training or optimization framework. The reward signals differ:
- Kaliszyk: proof success/failure from an ATP checker.
- Lightman: human-labeled step correctness.
- Math-Shepherd: automatic completability labels.
- DeepSeekMath: GRPO with process and outcome rewards.
- AlphaTensor: tensor decomposition success (algorithm correctness).

**MCTS + value network is a recurring pattern**: Kaliszyk (HOL Light) and AlphaTensor both use MCTS guided by a learned value function. This is the AlphaZero paradigm applied to mathematical domains. [[alphaproof-2024]] and [[2205.11491]] (HyperTree) in the Agents synthesis use the same structure.

**Step-level feedback consistently beats outcome-level feedback**: Lightman (2305.20050) proves this formally on MATH; Math-Shepherd (2312.08935) removes the human annotation bottleneck while preserving the finding; DeepSeekMath (2402.03300) builds on it. The pattern: whenever you can decompose a task into steps with evaluable intermediate correctness, step-level RL significantly outperforms outcome-level RL.

## Disagreement

**Formal vs. informal RL**: there is an implicit tension between the two camps:
- Lightman, Math-Shepherd, DeepSeekMath optimize for informal math reasoning (chain-of-thought, GSM8K, MATH) where correctness is approximate.
- Kaliszyk and AlphaTensor (and AlphaProof in the Agents synthesis) optimize for formally verified correctness.

The informal camp achieves high benchmark scores faster (Lightman: 78% MATH, DeepSeekMath: 51.7% MATH). The formal camp achieves provably correct results but is harder to scale (AlphaProof: 4/6 IMO, but only with massive compute).

No direct head-to-head comparison exists in these papers. The convergence point is [[2504.21801]] (DeepSeek-Prover-V2) which uses GRPO (from DeepSeekMath) + Lean 4 verification (formal) in a unified pipeline.

## What's settled

1. **RL outperforms pure supervised learning for math** when applied correctly (Kaliszyk: 40% gain; Lightman: PRM beats ORM; DeepSeekMath: RL fine-tuning materially improves pretrained models).
2. **Step-level rewards are better than outcome rewards** for multi-step mathematical reasoning (Lightman, Math-Shepherd, DeepSeekMath all converge on this).
3. **Automatic PRM training is feasible**: Math-Shepherd removes the human annotation bottleneck — automatic completability labels work as well as human labels for training PRMs.
4. **RL can discover novel mathematical algorithms**: AlphaTensor proves RL can improve on 50-year-old human results in a concrete, formally verified mathematical domain.
5. **MCTS + value network scales across domains**: works for theorem proving (Kaliszyk), game-playing (AlphaZero), algorithm discovery (AlphaTensor), and formal proof search (AlphaProof).

## What's contested

1. **Does process supervision scale to research-level mathematics?** Lightman's PRM800K covers AMC/AIME-level competition problems. Whether step-level supervision works for graduate-level or open research problems is untested.
2. **Is informal RL fine-tuning a stepping stone to formal reasoning, or a different paradigm?** DeepSeekMath targets informal math (MATH, GSM8K); DeepSeek-Prover-V2 targets formal (Lean 4). The relationship between the two is empirically narrowing (DeepSeek-Prover-V2: informal gap from 8→6/15 AIME) but not yet closed.

## What's open

1. **Lean 4 as the perfect PRM**: formal proof assistants provide exact step-level binary rewards for free. Applying the Math-Shepherd methodology at scale to Lean 4 / Mathlib 4 proofs would create the largest automatic PRM dataset for formal mathematics. Not yet published at write time.
2. **RL for algebraic algorithm discovery beyond matrix multiplication**: AlphaTensor's success on matrix multiplication is a template. Can the same approach find faster algorithms for KB completion, Gröbner basis computation, or other algebraic algorithms relevant to the Mixer?
3. **GRPO for formal provers**: DeepSeekMath introduced GRPO for informal math; DeepSeek-Prover-V2 used it for formal proving. A systematic comparison of GRPO vs. PPO for Lean 4 formal proof search is needed.

## Methodology notes

**Benchmark saturation on informal math**: GSM8K and MATH are approaching saturation for large models. New benchmarks (PutnamBench, AIME 2024-25 formalized) are necessary to distinguish the frontier. GRPO's 51.7% on MATH is impressive for a 7B model but not frontier for 70B+ models.

**Open vs. closed**: Lightman's PRM800K is publicly released; Math-Shepherd is reproducible; DeepSeekMath is open-weight. AlphaTensor code is released. This batch has good open-science hygiene relative to sub-area A (where AlphaProof is closed).

## Recommendation

For the Mixer workstream:

1. **AlphaTensor as a Mixer blueprint**: the single-player game framing (state = partial KB, action = inject rule, reward = convergence speed) is a direct template for RL-guided Mixer rule injection. AlphaTensor proves the paradigm works for mathematical algorithm discovery. The Mixer team should study AlphaTensor's reward design and MCTS implementation as a template.

2. **Process reward modeling for KB injection**: the step-level vs. outcome-level insight (Lightman, Math-Shepherd) applies to the Mixer. If each rule injection event is a "step," a PRM that evaluates injection quality at each step (does this rule reduce the number of critical pairs?) would outperform an outcome reward (did we reach confluence?). Math-Shepherd's automatic label generation (completability) can be adapted: a Mixer injection step is "correct" if there exists a confluence path from the resulting KB.

3. **GRPO for Mixer training**: GRPO's efficiency advantage (no separate critic) makes it attractive for Mixer RL fine-tuning if a neural injection policy is developed. Adds to the research agenda post-B(4,3) breakthrough.

4. **Formal RL for group theory proofs**: combining the Lean 4 infrastructure with process reward models (formal step-level RL) is the long-term direction for formalizing B(2,5) structural results. The convergence of AlphaProof (in the Agents synthesis) and the PRM methodology (in this synthesis) points toward a unified formal math RL system.

## Related vault material

- Papers: [[1805.07563]], [[2305.20050]], [[2312.08935]], [[2402.03300]], [[fawzi-2022-alphatensor]]
- RL-trained provers (covered in Agents synthesis, not re-summarized here): [[alphaproof-2024]], [[2504.21801]]
- Cross-vault: [[algo-mixing-burnside-slides]] (AlphaTensor's single-player game = Mixer injection RL blueprint)
- Prior synthesis (Agents arc): [[_synthesis-agents-for-math]]
- Upcoming synthesis: `Research/AI in Math/ML/_synthesis-ml-for-math.md` (sub-area C)
