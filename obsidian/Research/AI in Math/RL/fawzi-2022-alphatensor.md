---
title: "Discovering faster matrix multiplication algorithms with reinforcement learning"
authors: Alhussein Fawzi, Matej Balog, Aja Huang, Thomas Hubert, Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Francisco J R Ruiz, Julian Schrittwieser, Grzegorz Swirszcz, David Silver, Demis Hassabis, Pushmeet Kohli
year: 2022
venue: "Nature 610(7930):47-53"
url: https://www.nature.com/articles/s41586-022-05172-4
url_translated:
language: en
methodology_type: empirical
domain: ai
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[2506.13131]]"
quality_notes: "Published in Nature October 2022. No separate arXiv preprint identified; open-access via PMC (PMC9534758). Code at https://github.com/deepmind/alphatensor. AlphaZero architects (Silver, Hassabis, Schrittwieser) are co-authors — this is the direct application of AlphaZero's RL paradigm to mathematical algorithm discovery. Placed in Research/AI in Math/RL/ per Maria's directive (RL as primary contribution); structurally proof-search-shaped even though the output is an algorithm rather than a proof."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/reinforcement-learning
  - topic/value-network
  - topic/monte-carlo-tree-search
  - paper
  - status/draft
---

# Discovering faster matrix multiplication algorithms with reinforcement learning

## Abstract

"Improving the efficiency of algorithms for fundamental computations can have a widespread impact, as it can affect the overall speed of a large amount of computations. Matrix multiplication is one such primitive task, occurring in many systems—from neural networks to scientific computing routines. The automatic discovery of algorithms using machine learning offers the prospect of reaching beyond human intuition and outperforming the current best human-designed algorithms. However, automating the algorithm discovery procedure is intricate, as the space of possible algorithms is enormous. Here we report a deep reinforcement learning approach based on AlphaZero for discovering efficient and provably correct algorithms for the multiplication of arbitrary matrices. Our agent, AlphaTensor, is trained to play a single-player game where the objective is finding tensor decompositions within a finite factor space. AlphaTensor discovered algorithms that outperform the state-of-the-art complexity for many matrix sizes. Particularly relevant is the case of 4 × 4 matrices in a finite field, where AlphaTensor's algorithm improves on Strassen's two-level algorithm for the first time, to our knowledge, since its discovery 50 years ago. We further showcase the flexibility of AlphaTensor through different use-cases: algorithms with state-of-the-art complexity for structured matrix multiplication and improved practical efficiency by optimizing matrix multiplication for runtime on specific hardware. Our results highlight AlphaTensor's ability to accelerate the process of algorithmic discovery on a range of problems, and to optimize for different criteria."

## TL;DR

AlphaTensor applies AlphaZero-style RL (value network + policy + MCTS) to discover faster matrix multiplication algorithms by framing the problem as a single-player game over tensor decompositions. Beats Strassen's 50-year-old record for 4×4 matrices in finite fields. Demonstrates that RL can discover provably correct mathematical algorithms in domains where human search has stalled.

## Problem

Matrix multiplication complexity is a foundational open problem in computer science (the ω exponent). Strassen's O(n^{2.81}) algorithm from 1969 is still the practical standard for small matrices. Can RL discover tighter tensor decompositions that yield faster algorithms, outperforming the best human-designed ones?

## Approach

**Tensor decomposition as a game**: matrix multiplication of n×n matrices corresponds to finding a rank-r decomposition of a specific tensor T_{n,n,n}. AlphaTensor frames this as a single-player game: state = current (partially completed) decomposition, action = adding one new rank-1 component, reward = success (correct full decomposition) or failure. The game ends when a complete decomposition is found (algorithm discovered) or resources run out.

**AlphaZero-style RL**:
- **Value network**: estimates the probability of finding a valid decomposition from the current partial decomposition.
- **Policy network**: suggests which rank-1 component to add next.
- **MCTS**: explores the space of partial decompositions guided by value + policy.
- **Self-play**: the agent generates its own training data by playing the game.

**Multiple target criteria**: the agent can be directed toward minimizing arithmetic operations (complexity) OR minimizing actual runtime on specific hardware (GPU/TPU) — different objective functions over the same search space.

## Key result

- **4×4 matrices over Z₂**: AlphaTensor uses **47 multiplications**, vs. Strassen's two-level algorithm requiring 49. First improvement on Strassen for this case in 50 years.
- **Thousands of algorithms**: AlphaTensor discovered thousands of distinct algorithms for each matrix size, revealing that the algorithm space is far richer than previously known.
- **Hardware-optimized**: algorithms discovered that run 10-20% faster than Strassen on actual GPU/TPU hardware.
- **Structured matrices**: improved complexity for skew-symmetric and other structured matrix types.

## Assumptions

- Tensor decomposition over finite fields (Z₂, Z₃) is the right formalization of matrix multiplication algorithm discovery.
- The single-player game formulation adequately captures the structure of the search space.
- AlphaZero's RL paradigm generalizes from two-player games to this single-player combinatorial setting.

## Limitations / scope

- **Small matrix sizes**: results focus on n=4,5 matrices. Scaling to large matrices (the asymptotic problem) is a different challenge.
- **Finite fields**: results primarily over Z₂; generalization to real/complex arithmetic is different.
- **Provably correct but not human-interpretable**: the discovered algorithms are formally correct but not necessarily comprehensible.

## Replication evidence

Open-source code released. Community has reproduced and extended results (e.g., ArXiv 2405.20748 "OpenTensor" replicates and validates). Nature peer review.

## Why this paper matters

AlphaTensor demonstrates that **RL can discover genuinely novel mathematics** — not just improve existing methods. The key structural insight: any discrete combinatorial optimization problem over a finite factor space can potentially be framed as a single-player game and solved by RL. This is a template applicable far beyond matrix multiplication:

1. **Algorithm discovery in combinatorics**: the same template could apply to finding optimal combinatorial algorithms (sorting, graph algorithms, scheduling).
2. **Mathematical structure discovery**: tensor decomposition is a general framework; similar RL approaches could search for fast algorithms in other linear algebra domains.
3. **Relationship to proof search**: the single-player game over partial decompositions is structurally similar to proof search (partial proof → next tactic → check correctness). AlphaTensor validates that the AlphaZero paradigm works in single-player mathematical settings.

**Cross-vault connection**: the Mixer's KB rule injection problem can be framed similarly — the "state" is the current KB (set of rules), the "action" is injecting a rule from another ordering, and the "reward" is whether confluence is reached faster. AlphaTensor demonstrates that RL can optimize such mathematical algorithm search effectively. The Mixer's rule injection heuristics could be learned by RL rather than hand-designed.

## Quotes

> "AlphaTensor discovered algorithms that outperform the state-of-the-art complexity for many matrix sizes. Particularly relevant is the case of 4 × 4 matrices in a finite field, where AlphaTensor's algorithm improves on Strassen's two-level algorithm for the first time, to our knowledge, since its discovery 50 years ago." — Abstract

## Open questions surfaced

- Can the same single-player game formulation be applied to KB completion or word-problem algorithms in formal group theory?
- Does RL discover algorithms that are 50+ years faster for other mathematical primitives?
- Can AlphaTensor's hardware-optimization approach be extended to other computational kernels (FFT, convolutions)?

## Related material in vault

- Related: [[1805.07563]] (Kaliszyk 2018 — RL for theorem proving; same paradigm applied to math proof rather than algorithm discovery), [[alphaproof-2024]] (AlphaZero RL applied to formal theorem proving; direct architectural ancestor)
- Cross-vault: Mixer rule injection as RL-optimized algorithm search; see [[algo-mixing-burnside-slides]]
- MOC: `Research/AI in Math/RL/_synthesis-rl-for-math` (forthcoming)
