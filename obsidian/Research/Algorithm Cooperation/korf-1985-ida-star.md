---
title: "Depth-first iterative-deepening: An optimal admissible tree search"
authors: Richard E. Korf
year: 1985
venue: "Artificial Intelligence 27(1):97-109"
url: "https://doi.org/10.1016/0004-3702(85)90084-0"
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
cited_by: []
quality_notes: "Classic AI paper (1985). Abstract not retrieved verbatim — paywalled journal; content from authoritative knowledge. IDA* is the standard reference for bounded depth-first search. The algorithm is independently rediscovered many times; this paper is the definitive published treatment. Widely used in puzzle-solving, game playing, and combinatorial optimization."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/cs
  - topic/proof-search
  - topic/word-problem
  - paper
  - status/draft
---

# Depth-first iterative-deepening: An optimal admissible tree search

## Abstract

*(Not retrieved verbatim — paywalled AI journal, 1985. Described from authoritative knowledge.)*

Presents **IDA\*** (Iterative Deepening A*): a tree search algorithm that combines the optimal solution quality of A* (using an admissible heuristic) with the memory efficiency of depth-first search. Rather than storing a frontier (as A* does), IDA\* performs repeated depth-first searches with increasing depth bounds, using the heuristic $f(n) = g(n) + h(n)$ (cost-so-far + estimated cost-to-go) as the pruning criterion. Each iteration visits nodes with $f \leq$ threshold; the threshold increases to the minimum $f$ value of any pruned node.

## TL;DR

IDA*: depth-first search with an f-value threshold, iteratively increased until the solution is found. Uses O(d) memory (depth d) while achieving the same optimality as A*. The canonical reference for bounded search over combinatorial spaces — directly applicable to word-length-bounded search in group Cayley graphs.

## Problem

A* achieves optimal heuristic search but requires memory proportional to the frontier (exponential in solution depth). Depth-first search uses linear memory but is not optimal without a bound. Can bounded depth-first search achieve A*-quality solutions in linear memory?

## Approach

**IDA\* algorithm:**
1. Set initial threshold $t = h(s)$ (heuristic of the start state).
2. Perform depth-first search, pruning branches where $f(n) = g(n) + h(n) > t$.
3. If the goal is found, return. If not, set $t = \min\{f(n) : n \text{ pruned in this iteration}\}$.
4. Repeat until goal found.

**Optimality**: if $h$ is admissible (never overestimates true cost), IDA* finds an optimal-cost solution. Memory: $O(d)$ where $d$ is solution depth.

**Completeness**: guaranteed if the branching factor is finite and the cost function is strictly positive.

## Key result

- **Optimality with linear memory**: IDA* finds minimum-cost solutions using $O(d)$ memory, vs. A*'s exponential memory.
- **Compared to IDDFS** (iterative deepening without heuristic): IDA* visits the same nodes but prunes more aggressively using the heuristic.
- **Puzzle performance**: IDA* solves 15-puzzle instances that were intractable for A* (memory-limited) and much faster than depth-limited DFS.

## Assumptions

- Search space is a tree (or DAG with acyclic paths). Cycles require additional bookkeeping.
- Heuristic $h$ is admissible ($h(n) \leq h^*(n)$ for all $n$).
- Solution cost is bounded below by a positive constant (prevents zero-cost cycles).

## Limitations / scope

- On graphs with many repeated states, IDA* may re-expand states many times; its advantage over A* assumes tree-structured search.
- Requires a good admissible heuristic — without it, degenerates to iterative deepening DFS.
- For group word problems: the natural "length-of-word" heuristic is admissible (words can only get longer in a group with generators), but the branching factor (size of the generator set) is typically small, making IDA* competitive.

## Replication evidence

IDA* is reproduced in every AI textbook (Russell & Norvig). Independently rediscovered many times.

## Why this paper matters

IDA* is the **bounded search template** that the Mixer's bidirectional word-length search instantiates. For the B(2,5) bidirectional proof search (experiments in `experiments/burnside/b53_bidir/`):
- The "search from both ends" approach is a variant of bidirectional IDA*, where each direction applies IDA*-style threshold pruning.
- The "beam width" parameter in the Mixer's B(2,5) beam search corresponds to IDA*'s threshold.
- The meet-in-the-middle scheme (two IDA* runs from start and goal, meeting at threshold/2 depth) is the standard bidirectional extension of IDA*.

IDA* also characterizes the **space of possible search strategies**: any admissible bounded search is a specialization of IDA*. The SAT-based approaches (CDCL, see [[marques-silva-sakallah-1999-grasp]]) can be viewed as IDA* where the "heuristic" is the clause-propagation lookahead.

## Quotes

*(No verbatim abstract retrieved — paywalled AI journal.)*

## Open questions surfaced

- What is the right admissible heuristic for word-length search in Burnside groups? The word length itself is admissible but weak — a better heuristic using the known relator structure could dramatically improve search.
- Can IDA*'s threshold schedule be adapted for the Mixer's injection timing?

## Related material in vault

- Related: [[knuth-bendix-1970]] (KB completion is also a bounded search — each round of critical-pair generation is one IDA* iteration over the space of possible rule additions)
- Related: [[marques-silva-sakallah-1999-grasp]] (CDCL = sophisticated IDA* with learned pruning constraints)
- Cross-vault: [[Research/Group theory/Burnside groups/B25/algo-mixing-burnside-slides]] (bidirectional B(4,3) search; IDA*-like structure)
