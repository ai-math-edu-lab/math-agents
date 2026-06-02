---
title: "GRASP: A Search Algorithm for Propositional Satisfiability"
authors: João P. Marques-Silva, Karem A. Sakallah
year: 1999
venue: "IEEE Transactions on Computers 48(5):506-521"
url: "https://doi.org/10.1109/12.769433"
language: en
domain: cs
status: draft
methodology_type: empirical
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[korf-1985-ida-star]]"
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[hamadi-et-al-2009-manysat]]"
quality_notes: "Foundational CDCL paper (1999). Abstract not retrieved verbatim — IEEE paywall; content from authoritative knowledge. GRASP introduced Conflict-Driven Clause Learning (CDCL) — the core paradigm of every modern SAT solver (MiniSAT, Glucose, ManySAT, CaDiCaL, etc.). Citation count estimated 3000+ as of 2026."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/cs
  - topic/cdcl
  - topic/proof-search
  - topic/word-problem
  - paper
  - status/draft
---

# GRASP: A Search Algorithm for Propositional Satisfiability

## Abstract

*(Not retrieved verbatim — IEEE paywall. Described from authoritative knowledge.)*

Presents GRASP (Generic seaRch Algorithm for the Satisfiability Problem), a search algorithm for propositional satisfiability (SAT) incorporating several search-pruning techniques. The key innovation is **Conflict-Driven Clause Learning (CDCL)**: when a search path leads to a contradiction (conflict), GRASP performs **conflict analysis** to identify the minimal subset of assignments that caused the conflict, derives a new **clause** (the negation of that subset) that prunes this conflict permanently, and **backtracks non-chronologically** (to the decision level where the conflict first became inevitable). The learned clause is added to the clause database and prevents the same conflict from being re-visited in future search.

## TL;DR

GRASP introduces CDCL: when a dead-end (conflict) is reached, analyze the conflict to extract a short blocking clause, add it to the clause database, and backtrack non-chronologically. Learned clauses are permanent "partial-No" witnesses — they encode dead-ends so the solver never revisits them. Transforms SAT from blind backtracking to directed search with accumulating knowledge. The architecture of every modern SAT solver.

## Problem

Boolean SAT is NP-complete, but heuristic backtracking solvers can be practical for structured instances. Standard DPLL (Davis-Putnam-Logemann-Loveland) backtracks chronologically and re-visits failed branches. Can conflict information be exploited to prune the search space globally?

## Approach

**GRASP = DPLL + CDCL:**
1. **Assignment**: choose an unassigned variable; assign it a value (True or False).
2. **Unit propagation**: any clause with all but one literal falsified forces the remaining literal true (Boolean Constraint Propagation, BCP).
3. **Conflict detection**: if a clause becomes empty, all literals false — a conflict.
4. **Conflict analysis** (GRASP's key contribution): trace the **conflict graph** (the implication graph of forced assignments) to find the **first-unique implication point (1-UIP)** — the minimal set of decision assignments that forced the conflict. This set is the **learned clause** (its negation is added to the database).
5. **Non-chronological backtracking**: backtrack to the decision level of the second-highest decision variable in the learned clause — may jump back many levels, skipping explored territory that cannot yield solutions.
6. Repeat until satisfying assignment found (SAT) or all possibilities exhausted (UNSAT).

## Key result

- **GRASP outperforms DPLL** by orders of magnitude on structured SAT instances (circuit verification, AI planning).
- **Learned clauses as "no-good" witnesses**: every learned clause is a proof that no satisfying assignment containing those literals exists. The clause database accumulates permanently — a form of persistent memory across search branches.
- **Non-chronological backtracking**: can jump back across multiple decision levels in a single step when a conflict implicates a decision made far back in the search.

## Assumptions

- Propositional logic (Boolean variables, clauses in CNF form).
- Unit propagation is complete (every forced assignment is made before proceeding).
- The implication graph is maintained during BCP.

## Limitations / scope

- The learned clause database grows; memory management (clause deletion) is needed for long runs.
- Performance depends on variable selection heuristic (VSIDS in modern solvers).
- Not directly applicable to group word problems without explicit SAT encoding — but the CDCL paradigm is applicable to any search-with-constraints.

## Replication evidence

CDCL is reproduced in all modern SAT solvers (MiniSAT, Glucose, ManySAT, CaDiCaL, etc.). The correctness of the CDCL approach is proven by a large body of follow-up work. ManySAT ([[hamadi-et-al-2009-manysat]]) directly extends GRASP's architecture to parallel clause sharing.

## Why this paper matters

GRASP's CDCL architecture IS the "partial-No oracle" pattern in its most developed form:

1. **Learned clauses = persistent partial-No witnesses**: each conflict generates a clause that permanently prunes that region of search space. The clause is a witness that "no satisfying assignment containing these literals exists." This is the same structure as KB rewriting rules: each rule $l \to r$ is a persistent witness that "any word containing $l$ is equal to $r$" — a proof that those states are equivalent, pruning the search permanently.

2. **Non-chronological backtracking = global not local pruning**: the backjump in CDCL goes to the earliest relevant decision level, avoiding redundant re-exploration. This is analogous to how a KB rule derived at one stage of the Mixer can immediately prune candidate words in all other orderings' rule banks.

3. **The connection to KB**: KB completion and CDCL are both "accumulate-and-prune" search strategies. KB accumulates rules (oriented equations); CDCL accumulates clauses (constraint witnesses). Both are complete (terminate iff the problem has a solution / is unsatisfiable) but with very different problem representations.

## Quotes

*(No verbatim abstract retrieved — IEEE paywall.)*

## Open questions surfaced

- Can word problems for specific groups be efficiently encoded in SAT/CNF and solved by CDCL?
- Does the CDCL paradigm (conflict analysis, learned clauses, non-chronological backtracking) have a direct analog in KB completion for group presentations?

## Related material in vault

- Extends: [[korf-1985-ida-star]] (IDA* is the general admissible bounded search; CDCL is IDA* with learned clauses as global constraints)
- Cited by: [[hamadi-et-al-2009-manysat]] (ManySAT extends GRASP to parallel clause sharing)
- Related: [[gomes-selman-2001-portfolios]] (algorithm portfolios running multiple CDCL solvers in parallel)
- Cross-vault: [[Concepts/kb-mixing-stagnation]] (KB's "learned rules" are structurally analogous to CDCL's learned clauses)
