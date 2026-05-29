---
title: "Mathematical discoveries from program search with large language models"
authors: Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog, M. Pawan Kumar, Emilien Dupont, Francisco J. R. Ruiz, Jordan S. Ellenberg, Pengming Wang, Omar Fawzi, Pushmeet Kohli, Alhussein Fawzi
year: 2023
venue: "Nature 625(7995)"
url: https://www.nature.com/articles/s41586-023-06924-6
url_translated:
language: en
methodology_type: empirical
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[2506.13131]]"
quality_notes: "Published in Nature, December 2023. No separate arXiv preprint identified. Code and discovered programs at https://github.com/google-deepmind/funsearch. Key distinction: FunSearch searches in *function space* (writes Python programs), not in formal proof space — the output is a provably-correct algorithm (in the sense that the evaluator verifies it), not a formal proof. The cap set improvement and bin packing results are genuine mathematical discoveries."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/funsearch
  - topic/mathematical-discovery
  - paper
  - status/draft
---

# Mathematical discoveries from program search with large language models

> **FunSearch paradigm**: this is the foundational FunSearch paper. The 2025 successor [[2506.13131]] (AlphaEvolve) extends FunSearch to a broader range of mathematical and engineering problems. Read both together as one line of work.

## Abstract

Large language models demonstrate strong capabilities in complex problem-solving, yet they suffer from confabulations that hinder scientific discovery applications. This work introduces FunSearch, an evolutionary procedure pairing a pretrained LLM with systematic evaluation. The approach surpasses best-known results on important problems. Applied to the cap set problem in extremal combinatorics, it discovers new constructions exceeding previous best-known results in both finite and asymptotic cases. FunSearch also discovers improved heuristics for online bin packing that outperform established baselines. Unlike most computational search methods that find solutions directly, FunSearch searches for programs describing solution approaches, making discoveries more interpretable and deployable in real-world applications.

## TL;DR

FunSearch: an LLM proposes variants of Python programs, an evaluator scores them for mathematical validity/optimality, the best programs are fed back to the LLM as context for the next generation. Applied to the cap set problem — discovers new cap sets in finite fields exceeding previous records, including asymptotic improvements. Non-RL, non-RL: purely evolutionary + LLM. Discovers interpretable programs, not just solutions.

## Problem

How can LLMs be used for mathematical discovery without hallucination? Direct LLM prompting for mathematical proofs confabulates — the LLM produces plausible-sounding but incorrect statements. Can an evolutionary search loop (with a formal evaluator) use the LLM's generative power while filtering out incorrect outputs?

## Approach

**FunSearch loop:**
1. **Initialization**: seed with a correct but suboptimal program for the target mathematical problem.
2. **LLM sampling**: prompt the LLM with the current best programs as few-shot examples; ask it to generate a variant.
3. **Evaluation**: run the generated program; score it by the mathematical criterion (e.g., size of the cap set it constructs).
4. **Selection**: keep the best programs in a "program bank"; use them as context for the next LLM call.
5. **Repeat**: iterate until performance plateaus.

**Key distinction**: FunSearch searches for *programs that describe solution approaches* (Python functions), not for solutions directly. The programs are:
- Interpretable (humans can read and understand what strategy the discovered program encodes).
- Generalizable (the program works for all inputs, not just the training instances).
- Formally correct (the evaluator verifies every output — no hallucination).

## Key result

**Cap set problem (extremal combinatorics):**
- Finite case: new cap sets found in 8 dimensions with size **512**, surpassing the previous best known.
- Asymptotic: improved lower bound on cap set capacity from 2.2180 to **2.2202** — the first asymptotic improvement in the cap set problem in many years.

**Online bin packing:**
- New heuristics discovered that outperform first-fit and best-fit baselines across all tested datasets.
- 0.03% excess bins on 100,000-item instances (substantially better than human-designed heuristics).

## Assumptions

- The LLM's probability distribution over programs captures useful mathematical strategies (a strong generalization assumption).
- The evaluator is both sound (accepts only correct programs) and fast enough for the evolutionary loop.
- The solution space is navigable by LLM variants without RL.

## Limitations / scope

- Requires a mathematical evaluator that can score candidate programs efficiently. For problems without such an evaluator, FunSearch cannot be applied.
- The search is in *program space*, not *proof space* — FunSearch discovers mathematical constructions, not formal proofs of theorems.
- The LLM's confabulation tendency is controlled by the evaluator but not eliminated — invalid programs are simply discarded; efficiency depends on the ratio of valid to invalid proposals.

## Replication evidence

Open-source code at https://github.com/google-deepmind/funsearch. The cap set improvements are verifiable independently (construct the cap set, check size). The asymptotic lower bound is a mathematical claim that other researchers can verify.

## Why this paper matters

FunSearch establishes the **evaluator-filtered evolutionary LLM search** paradigm for mathematical discovery. Key insights:
1. **Confabulation is controlled by the evaluator**: the LLM can propose anything; only mathematically valid proposals survive. This sidesteps the central LLM hallucination problem.
2. **Programs > solutions**: searching for programs encoding strategies generalizes to all instances, not just the training instances. The discovered cap set program works for any field size, not just the test cases.
3. **Interpretability**: discovered programs can be read by mathematicians, unlike most ML outputs.
4. **Genuine mathematical novelty**: the asymptotic cap set bound improvement is a result that matters to the extremal combinatorics community.

**Relationship to AlphaTensor ([[fawzi-2022-alphatensor]], RL/)**: both systems discover mathematical algorithms (matrix multiplication algorithms, bin packing heuristics) using search guided by ML. AlphaTensor uses RL + MCTS; FunSearch uses evolutionary search + LLM. Both achieve improvements over human-known results. The paradigmatic difference: RL trains a policy that plans ahead; evolutionary search makes local random variations. FunSearch is simpler to implement; AlphaTensor is more principled. [[2506.13131]] (AlphaEvolve) is the 2025 system that further extends FunSearch to harder problems.

**Cross-vault relevance**: the evaluator-filtered evolutionary search is directly applicable to KB completion heuristic discovery. An evaluator that scores a KB rule-injection heuristic by whether it accelerates convergence could run FunSearch over a space of injection strategies — discovering better heuristics than human-designed ones.

## Quotes

> "Unlike most computational search methods that find solutions directly, FunSearch searches for programs describing solution approaches, making discoveries more interpretable and deployable in real-world applications." — Abstract

## Open questions surfaced

- Can FunSearch discover new results in group theory or algebra (e.g., new bounds on subgroup indices, new word-problem instances)?
- Can the FunSearch loop be applied to Lean 4 program search (using Lean's type checker as the evaluator)?

## Related material in vault

- Cited by: [[2506.13131]] (AlphaEvolve — FunSearch extended to 67+ mathematical and engineering problems)
- Related: [[fawzi-2022-alphatensor]] (AlphaTensor in RL/ — parallel paradigm for mathematical algorithm discovery via RL rather than evolutionary search)
- Related: [[2006.11287]] (Cranmer 2020 — equation discovery; different methodology for mathematical discovery)
- Related: [[raayoni-2021-ramanujan]] (conjecture generation; same "AI discovers math" paradigm class)
- Cross-vault: evaluator-filtered search = template for Mixer injection heuristic search; see [[algo-mixing-burnside-slides]]
- MOC: `Research/AI in Math/ML/_synthesis-ml-for-math` (forthcoming)
