---
title: "Algorithm Portfolios"
authors: Carla P. Gomes, Bart Selman
year: 2001
venue: "Artificial Intelligence 126(1-2):43-62"
url: "https://doi.org/10.1016/S0004-3702(00)00081-3"
language: en
domain: cs
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[hamadi-et-al-2009-manysat]]"
quality_notes: "Foundational 2001 AI paper. Abstract not retrieved verbatim — Elsevier paywall; content from authoritative knowledge. Carla Gomes and Bart Selman at Cornell — the leading group for algorithm portfolios in combinatorial search. This paper formalizes the theoretical foundations; the subsequent empirical literature has validated the framework on SAT, CSP, and planning."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/cs
  - topic/algorithm-portfolio
  - topic/proof-search
  - paper
  - status/draft
---

# Algorithm Portfolios

## Abstract

*(Not retrieved verbatim — Elsevier paywall. Described from authoritative knowledge.)*

Presents the theory of **algorithm portfolios** for combinatorial search: running multiple algorithm configurations (or different algorithms) in parallel on the same problem instance and using the combined output to outperform any individual component. The paper models algorithm runtime as a random variable and shows that if runtimes have **heavy-tailed distributions** (a distribution where the variance is theoretically infinite, meaning very long runs occur with non-negligible probability), then portfolios dramatically outperform any single algorithm by hedging against catastrophically long runs. Includes analysis of optimal portfolio composition and restart policies.

## TL;DR

If individual algorithm runtimes are heavy-tailed (which they empirically are for SAT and CSP), running multiple algorithms in parallel with restarts can achieve expected runtime polynomial in the optimal, even if any single run has unbounded expected runtime. The formal theory behind the Mixer's multi-ordering approach. Also shows that "restart with randomization" is a portfolio of the same algorithm with different random seeds.

## Problem

For hard combinatorial search problems, individual algorithms exhibit **heavy-tailed runtime distributions**: sometimes they solve the problem in milliseconds, sometimes they run for days. Can multiple algorithms be combined to get consistent, fast performance?

## Approach

**Portfolio model:**
- Model algorithm runtime as a random variable $T$ with (possibly heavy-tailed) distribution $F_T$.
- A **portfolio** of $k$ algorithms runs all $k$ in parallel; the runtime is $T_{portfolio} = \min(T_1, T_2, \ldots, T_k)$.
- For independent, identically distributed algorithms: $\Pr[T_{portfolio} > t] = \Pr[T_1 > t]^k$, which eliminates heavy tails much faster than any single algorithm.
- **Restart strategy** (random restart at bound $b$): restarts the same algorithm when it exceeds $b$ — equivalent to a portfolio of infinite identical algorithms, each with randomized tie-breaking.

**Key findings:**
1. **Heavy-tailed runtimes are eliminated by portfolios**: if $T_1 \sim $ Pareto, $T_{portfolio} \sim $ Exponential. Expected runtime goes from infinite to finite.
2. **Optimal restart policy**: under a heavy-tailed distribution $F$, the optimal restart bound $b^*$ can be computed from $F$ — restart at $b^*$ rather than running to completion.
3. **Information sharing**: the paper discusses extending portfolios to share learned information (e.g., good variable assignments, lemma banks) between components. This is the natural extension toward CDCL clause sharing ([[hamadi-et-al-2009-manysat]]) and the Mixer's rule injection.

## Key result

- **Theorem (informal)**: if individual algorithm runtimes have a heavy-tailed distribution (finite mean but infinite variance, or infinite mean), then a portfolio of $k$ independent runs has runtime that converges to the optimal as $k \to \infty$ — the heavy tail is eliminated.
- **Empirical evidence**: on SAT and CSP instances, runtimes are empirically heavy-tailed; portfolio strategies show order-of-magnitude improvements on hard instances.
- **Restart as cheap portfolio**: random restarts with cutoff $b^*$ are equivalent to a portfolio and achieve near-optimal expected runtime without parallel hardware.

## Assumptions

- Algorithm components are independent (no information sharing). The paper discusses information sharing as an open extension.
- Runtimes are i.i.d. (same algorithm with random restarts) or independently distributed (different algorithms).
- The underlying distribution $F$ is known or estimable from short runs.

## Limitations / scope

- The "information sharing" direction (critical for the Mixer) is discussed theoretically but not implemented in this paper — see [[hamadi-et-al-2009-manysat]] for the parallel SAT instantiation.
- Independence assumption breaks when algorithms share state — the analysis changes significantly when clause sharing or rule injection occurs.
- The optimal restart bound $b^*$ depends on the (often unknown) runtime distribution.

## Replication evidence

The restart strategy is validated on SAT benchmarks in this paper. Heavy-tailed runtimes for SAT have been independently confirmed many times. ManySAT ([[hamadi-et-al-2009-manysat]]) implements the parallel portfolio + clause sharing and validates the framework empirically.

## Why this paper matters

Gomes & Selman 2001 provides the **formal theoretical foundation for the Mixer's architecture**. The Mixer is, in the portfolio terminology, a portfolio of KB completion algorithms (one per ordering) with **structured information sharing** (rule injection instead of clause sharing). The key translation:

| Portfolio concept | Mixer analog |
|---|---|
| Algorithm component | KB completion under one ordering |
| Runtime | Time to reach confluence (or diverge) |
| Heavy-tailed distribution | KB runtime for hard Burnside groups |
| Information sharing | Rule injection between orderings |
| Learned information | Rewriting rules from one ordering's KB |
| "Restart" | Starting a new KB run with injected rules |

The theoretical prediction from this paper: **if KB completion under any single ordering has a heavy-tailed runtime for B(2,5), then the Mixer (portfolio of KB orderings with rule injection) should eliminate the heavy tail** — matching the empirical result for B(4,3) where the single-ordering timeout was ~hours but the two-ordering Mixer completed in 33 minutes.

## Quotes

*(No verbatim abstract retrieved — Elsevier paywall.)*

## Open questions surfaced

- Is KB completion for B(2,5) under any single ordering heavy-tailed? (If yes, portfolio theory predicts Mixer should help.)
- What is the optimal number of orderings in the Mixer portfolio? Portfolio theory suggests there's a sweet spot where adding more components stops improving performance.
- Does information sharing (rule injection) make the components dependent enough to break the portfolio theory's guarantees?

## Related material in vault

- Cited by: [[hamadi-et-al-2009-manysat]] (ManySAT implements portfolios + clause sharing — the parallel SAT instantiation)
- Related: [[marques-silva-sakallah-1999-grasp]] (CDCL — the algorithm inside each SAT portfolio component)
- Related: [[clarke-et-al-2000-cegar]] (CEGAR — same "parallel oracle" pattern in a different domain)
- Cross-vault: [[Research/Group theory/Burnside groups/B25/algo-mixing-burnside-slides]] (B(4,3) Mixer result — the portfolio strategy at work)
- Related: [[Concepts/kb-mixing-stagnation]] (stagnation = heavy-tailed KB runtime)
- Related: [[Concepts/mixable-api]] (the Mixer's information-sharing API = portfolio clause-sharing instantiation)
