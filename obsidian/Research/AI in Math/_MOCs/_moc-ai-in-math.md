---
title: "AI in Math — Map of Content"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/automated-theorem-proving
  - topic/mathematical-discovery
  - topic/moc
  - status/draft
---

# AI in Math — Map of Content

**This MOC is a curated reading path for AI applied to mathematics** — covering formal theorem proving (LLM-based agents), RL training for mathematical reasoning, and ML-guided mathematical discovery. Three sub-areas, 20 papers (2017–2025). Navigate here when you want to understand the state of the art, what's settled, and what remains open.

Cross-cluster: papers in this MOC that are relevant to the Burnside/Mixer program are flagged with ⚡.

---

## Sub-area A — Agents for math

LLM-driven formal theorem provers, agentic proof search, autoformalization scaffolding.

**Synthesis**: [[Agents/_synthesis-agents-for-math]] — three paradigm arcs (LLM proof generation / autoformalization / neuro-symbolic); 6 settled results, 3 contested, 5 open questions; 4 Mixer recommendations.

### Foundational

- [[2009.03393]] — GPT-f (Polu & Sutskever 2020): LLM sampling for MetaMath/Lean proofs; expert iteration; first deep-learning proofs accepted into the Metamath library. The founding paper of the LLM-prover paradigm.

- [[2205.12615]] — Autoformalization with LLMs (Wu et al. 2022, NeurIPS): 25.3% of AMC/AIME problems correctly translated to Isabelle/HOL; starts the informal-to-formal data flywheel.

- [[2205.11491]] — HyperTree Proof Search (Lample et al. 2022, NeurIPS): MCTS + online learning on Lean proof trees; 82.6% on Metamath; establishes MCTS-for-proof-search paradigm.

- [[2210.12283]] — Draft, Sketch, and Prove (Jiang, Welleck et al. 2023, ICLR): informal → sketch → Isabelle verification; 21% → 39% on competition math. ⚡ *Applicable to formalizing Burnside group results in Isabelle.*

### Neuro-symbolic (AlphaGeometry line)

*AlphaGeometry 1 and 2 are one continuous line of work — read together.*

- [[trinh-2024-alphageometry]] — AlphaGeometry 1 (Trinh et al. 2024, Nature): LLM + symbolic deduction engine for IMO geometry; 25/30 problems solved; silver-medalist level. ⚡ *Auxiliary-construction analogy to Mixer rule injection.*

- [[2502.03544]] — AlphaGeometry 2 (Chervonyi et al. 2025): extends AG1; Gemini LM + knowledge-sharing search trees; 84% on 25 years of IMO geometry; gold-medalist level. ⚡ *Knowledge-sharing mechanism = Mixer rule injection architecture.*

- [[alphaproof-2024]] — AlphaProof + AG2 (DeepMind 2024): RL-trained Lean 4 prover + AG2; 4/6 IMO 2024 problems; silver medal. Source: blog + Nature 2025 paper (paywalled). ⚡ *Long-term architecture for formal group theory proofs.*

### Recent SOTA 2025

- [[2504.21801]] — DeepSeek-Prover-V2 (DeepSeek-AI 2025): recursive subgoal decomposition + RL; 88.9% on miniF2F-test; open weights; 2025 formal ATP SOTA. ⚡ *Subgoal decomposition = structured analog of Mixer KB injection.*

- [[2404.12534]] — Lean Copilot (Song et al. 2024): LLMs as real-time tactic suggesters in Lean 4 IDE; human-AI collaboration; 74.2% automation rate. ⚡ *Natural tool for formalizing B(4,3) or B(2,5) computational results in Lean 4.*

---

## Sub-area B — RL for math

Reinforcement-learning-guided tactic selection, value-network proof search, process reward models for mathematical reasoning.

**Synthesis**: [[RL/_synthesis-rl-for-math]] — 3 organizing buckets (RL for formal proof search / PRMs for informal math / RL for algorithm discovery); AlphaZero architectural context; 5 settled results, 2 contested, 3 open; 4 Mixer recommendations including AlphaTensor as injection-heuristic blueprint.

### Foundational

- [[RL/1805.07563]] — RL of Theorem Proving (Kaliszyk et al. 2018, NeurIPS): first large-scale RL for ATP on HOL Light; MCTS + value network; 40% more theorems proved. ⚡ *RL from proof success = Mixer's KB cascade feedback pattern.*

- [[RL/2305.20050]] — Let's Verify Step by Step (Lightman et al. 2023, OpenAI): process reward models (PRMs) outperform outcome reward models for multi-step math; 78% on MATH; PRM800K dataset. ⚡ *Step-level reward vs. outcome reward is applicable to Mixer injection evaluation.*

- [[RL/2312.08935]] — Math-Shepherd (Wang et al. 2024, ACL): auto-generates PRM training data without human annotation; 77.9% → 84.1% on GSM8K. ⚡ *Automatic PRM = template for Mixer injection-step reward labeling.*

- [[RL/2402.03300]] — DeepSeekMath (Shao et al. 2024): GRPO algorithm; 51.7% MATH at 7B; open weights; GRPO underpins DeepSeek-Prover-V2. ⚡ *GRPO = efficient RL training for future Mixer injection policy.*

### RL for algorithm discovery

- [[RL/fawzi-2022-alphatensor]] — AlphaTensor (Fawzi et al. 2022, Nature): AlphaZero-style RL discovers new matrix multiplication algorithms; beats Strassen 4×4 in Z₂. ⚡ **Highest Mixer relevance**: single-player game framing = template for RL-guided Mixer rule injection. The evaluator is "does this injection reduce convergence time?"

---

## Sub-area C — ML for math (non-agent, non-RL)

Equation/conjecture discovery, neural heuristics inside solvers, embeddings-for-math, evolutionary LLM program search.

**Synthesis**: [[ML/_synthesis-ml-for-math]] — 4-paradigm structure; 5 settled, 2 contested, 4 open; 4 Mixer recommendations including AlphaEvolve as injection-heuristic-discovery blueprint.

### Neural heuristics inside existing solvers

- [[ML/1701.06972]] — Deep Network Guided Proof Search (Loos et al. 2017, LPAR-21): first deep-network premise selection inside E theorem prover; 56% → 59% Mizar coverage; foundational "ML as solver heuristic."

- [[ML/2306.15626]] — LeanDojo / ReProver (Yang et al. 2023, NeurIPS): embedding-based premise retrieval for Lean 4; open-source infrastructure; outperforms GPT-4 on hard generalization benchmark. ⚡ *Retrieval of relevant Lean 4 premises = analog of rule retrieval in Mixer KB. Tool for formalizing Burnside results.*

- [[ML/1811.06128]] — Bengio, Lodi, Prouvost (2021, EJOR): survey of ML for combinatorial optimization — honest assessment of what ML has actually shown vs. hype. Key finding: algorithm selection is the most reliable ML-for-CO application. ⚡ *Recommends ML injection policy (algorithm selection) as the most principled next step for the Mixer.*

### Equation and conjecture discovery

- [[ML/2006.11287]] — Discovering Symbolic Models (Cranmer et al. 2020, NeurIPS): GNN + symbolic regression extracts equations from neural networks; discovers new dark matter formula. ⚡ *PySR applicable to $|P_s(2,5)|$ growth function data.*

- [[ML/raayoni-2021-ramanujan]] — Ramanujan Machine (Raayoni et al. 2021, Nature): automated conjecture generation about fundamental constants via MITM-RF; discovers previously-unknown continued fraction formulas.

### Evolutionary LLM program search (FunSearch line)

*FunSearch and AlphaEvolve are one continuous line of work — read together.*

- [[ML/romera-paredes-2023-funsearch]] — FunSearch (Romera-Paredes et al. 2023, Nature): evolutionary LLM-guided program search; discovers new cap set bounds and bin packing heuristics; evaluator filters confabulations. ⚡ *Evaluator-filtered evolutionary search = template for Mixer injection heuristic discovery.*

- [[ML/2506.13131]] — AlphaEvolve (Novikov et al. 2025): FunSearch with Gemini; 67+ mathematical problems; discovers 4×4 complex matrix multiplication with 48 multiplications (first Strassen improvement in this setting). ⚡ *Same template as FunSearch; broader validation.*

---

## Cross-cluster connections to Group Theory / Burnside

Papers with ⚡ above have documented connections to the Burnside / Mixer program. The highest-priority actionable connections are:

1. **[[RL/fawzi-2022-alphatensor]]** (AlphaTensor): single-player RL game framing → Mixer rule injection as RL-optimized algorithm search.
2. **[[ML/romera-paredes-2023-funsearch]]** + **[[ML/2506.13131]]** (FunSearch/AlphaEvolve): evolutionary evaluator-filtered search → Mixer injection heuristic discovery.
3. **[[2404.12534]]** (Lean Copilot) + **[[ML/2306.15626]]** (LeanDojo): Lean 4 infrastructure for formalizing B(4,3)/B(2,5) computational results.
4. **[[2502.03544]]** (AlphaGeometry 2): knowledge-sharing between search trees → multi-agent Mixer architecture.
5. **[[ML/2006.11287]]** (Cranmer/PySR): symbolic regression → closed-form formula for $|P_s(2,5)|$ growth function.

---

## Related MOCs

- [[Research/Group theory/_MOCs/_moc-burnside]] — the Burnside group research cluster; Mixer targets; Kuznetsov computational line.
- [[Research/Group theory/_MOCs/_moc-knuth-bendix]] — the KB completion algorithm cluster; Mixer's core algorithm.
