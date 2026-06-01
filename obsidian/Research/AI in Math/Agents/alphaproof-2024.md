---
title: "AI achieves silver-medal standard solving International Mathematical Olympiad problems (AlphaProof + AlphaGeometry 2)"
authors: Google DeepMind
year: 2024
venue: DeepMind blog post + Nature (November 2025, doi:10.1038/s41586-025-09833-y)
url: https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
url_translated:
language: en
methodology_type: empirical
domain: ai
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[trinh-2024-alphageometry]]"
contradicts: []
replicates: []
cites:
  - "[[trinh-2024-alphageometry]]"
cited_by: []
quality_notes: "source-text-incomplete-tech-report-and-blog-only. Primary source is the DeepMind blog post (July 2024) and Nature news coverage. The AlphaProof methodology was later published in Nature as 'Olympiad-level formal mathematical reasoning with reinforcement learning' (doi:10.1038/s41586-025-09833-y, November 2025) — that full paper is behind a paywall and not retrieved. Summary in this note is from the blog post only. DO NOT fabricate methodology details beyond what the blog explicitly states. AlphaGeometry 2 (the geometry component) has a separate full paper at [[2502.03544]]. Landmark IMO 2024 result: 4/6 problems solved, silver-medal equivalent."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/automated-theorem-proving
  - topic/llm-prover
  - topic/lean
  - topic/proof-search
  - topic/monte-carlo-tree-search
  - topic/agentic-reasoning
  - topic/neuro-symbolic
  - paper
  - status/draft
---

# AI achieves silver-medal standard solving International Mathematical Olympiad problems

> **Note on sources**: This summary is based on the DeepMind blog post (July 2024) and public reporting. The full AlphaProof technical paper was published in Nature (November 2025, doi:10.1038/s41586-025-09833-y) but is paywalled and not retrieved. AlphaGeometry 2 (the geometry sub-component) has a full arXiv paper at [[2502.03544]] — see that note for AG2's technical details. This note covers the combined IMO 2024 system and AlphaProof's architecture at the blog-description level.

> **AlphaGeometry research line**: AlphaGeometry 2 (AG2) is the geometry component of this IMO system; it is the successor to [[trinh-2024-alphageometry]] (AG1). The AI-achieves-silver-medal result is the culmination of both lines (AlphaProof + AG2). Read this note alongside [[trinh-2024-alphageometry]] and [[2502.03544]].

## Abstract / description

Google DeepMind's AlphaProof (RL-trained Lean 4 prover) and AlphaGeometry 2 (neuro-symbolic geometry prover) together solved **4 of 6 problems** at IMO 2024, scoring 28/42 points — equivalent to a silver medal. Solutions verified by Fields Medal winner Timothy Gowers and IMO gold medalist Joseph Myers. The 4 solved problems included IMO 2024's hardest problem (solved by only 5 human contestants). Two combinatorics problems were not solved.

## TL;DR

AlphaProof = AlphaZero-style RL + Lean 4 formal proofs + Gemini language model. AlphaGeometry 2 = enhanced AG1. Together: 4/6 IMO 2024 problems solved, silver-medal level. Landmark that established AI as reaching IMO performance on algebra, number theory, and geometry.

## Problem solved

IMO 2024: 6 problems across algebra, combinatorics, geometry, and number theory. Goal: solve as many as possible within competition time limits (actually extended to allow for compute budget). Context: Prior AI could not solve more than 1-2 IMO problems; human silver medalists solve ~4-5.

## Approach (as described in blog — methodology details from full Nature paper not retrieved)

**AlphaProof:**
- Combines a **pre-trained Gemini language model** with **AlphaZero reinforcement learning** for formal proof search in **Lean 4**.
- Process: Gemini translates informal problem statement to Lean 4. AlphaProof then searches for a formal proof using RL-trained policy + value network (AlphaZero style). Successful proofs reinforce the model.
- Trained on "millions of problems" across diverse mathematical topics in Lean 4 for weeks before the competition, with continued RL during the competition.
- **Solved**: Problems 1 (algebra), 2 (number theory), 6 (hardest problem — algebra/number theory).

**AlphaGeometry 2** (full details in [[2502.03544]]):
- Neuro-symbolic: Gemini-based LM + improved symbolic engine.
- **Solved**: Problem 4 (geometry) — in **19 seconds**.

**Unsolved**: Problems 3 and 5 (combinatorics).

## Key result

- **4/6 IMO 2024 problems solved** (28/42 points = silver medal equivalent).
- **Problem 6** (hardest): solved by AlphaProof; only 5 human contestants solved it.
- **Problem 4** (geometry): solved by AG2 in 19 seconds.
- **Two combinatorics problems**: unsolved. Combinatorics remains the hardest domain for AI.
- Solutions verified by human IMO experts.

## Assumptions

- The Lean 4 formal framework is expressive enough to encode all solved problems.
- RL from formal proof verification provides a sufficient training signal for deep mathematical reasoning.
- The combination of informal (Gemini) and formal (Lean 4 RL) is necessary — neither component alone would have solved all 4.

## Limitations / scope

- **Combinatorics gap**: both combinatorics problems remained unsolved. The combinatorics domain lacks the efficient formal verification loops that algebra/number theory have in Lean 4.
- **Time budget extended**: the system ran for longer than competition time (necessary for the RL search).
- **Problem formalization required**: Gemini must correctly translate problems to Lean 4 before proof search begins; errors here propagate.
- Source limitation: this summary is from the blog; the full Nature methodology paper is paywalled.

## Replication evidence

IMO 2024 is a live, independently verified competition. The 4/6 result is confirmed by IMO jury members (Gowers, Myers). AG2's sub-component is confirmed in [[2502.03544]]. This is the most externally validated AI math result to date.

## Why this paper matters

AlphaProof + AG2's IMO 2024 performance is the clearest demonstration that:
1. **RL from formal verification** (AlphaZero paradigm applied to Lean 4 proofs) can solve problems at human-expert mathematical competition level.
2. **The informal-to-formal bridge** (Gemini translating to Lean 4) is mature enough to handle IMO-level problem statements.
3. **Formal verification enables hard AI problems**: the RL signal comes from Lean 4's proof checker — no human reward necessary. This makes the system self-improving given compute.

This is the 2024 ceiling for AI in formal mathematics. [[2504.21801]] (DeepSeek-Prover-V2, 2025) is the next major SOTA result — on benchmarks rather than competition, but with quantified improvements.

**Cross-vault connection**: the AlphaProof architecture (RL + formal Lean prover) is the natural long-term successor for the Mixer B(2,5) pipeline. If KB completion for B(2,5) proves intractable by direct search, an AlphaProof-style RL system trained on Lean 4 group theory proofs is the natural alternative. The Lean 4 Mathlib includes substantial group theory infrastructure.

## Quotes

> "AlphaProof solved problems 1 and 2 and the extremely challenging problem 6, which only 5 contestants solved correctly at this year's competition." — DeepMind blog

## Open questions surfaced

- Can AlphaProof solve combinatorics IMO problems with architectural modifications?
- What is the full methodology for the AlphaZero-style RL training (available in the Nature paper, not retrieved here)?
- How does AlphaProof's Lean 4 formal proof system compare with Lean Copilot ([[2404.12534]]) for interactive human assistance?

## Related material in vault

- Extends: [[trinh-2024-alphageometry]] (AlphaGeometry 1 is the predecessor to the geometry component)
- Cites: [[trinh-2024-alphageometry]]
- Related: [[2502.03544]] (AlphaGeometry 2 full paper — the geometry sub-component of this system)
- Cross-vault: architecture analogy with [[algo-mixing-burnside-slides]]; future Lean 4 group theory applications would connect to `Research/Group theory/Burnside groups/B25/`
- MOC: `Research/AI in Math/Agents/_synthesis-agents-for-math` (forthcoming)
