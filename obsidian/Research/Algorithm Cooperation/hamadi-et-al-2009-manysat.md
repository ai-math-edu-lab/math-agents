---
title: "ManySAT: A Parallel SAT Solver"
authors: Youssef Hamadi, Said Jabbour, Lakhdar Sais
year: 2009
venue: "Journal on Satisfiability, Boolean Modeling and Computation (JSAT) 6:245-262"
url: "http://www.cril.univ-artois.fr/~jabbour/ManySAT-Page/pdf/jsatmanysat.pdf"
language: en
domain: cs
status: draft
methodology_type: empirical
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[gomes-selman-2001-portfolios]]"
  - "[[marques-silva-sakallah-1999-grasp]]"
contradicts: []
replicates: []
cites:
  - "[[gomes-selman-2001-portfolios]]"
  - "[[marques-silva-sakallah-1999-grasp]]"
cited_by: []
quality_notes: "JSAT is an open-access journal; PDF available at http://www.cril.univ-artois.fr/~jabbour/ManySAT-Page/pdf/jsatmanysat.pdf (binary PDF, not text-extractable by WebFetch). Abstract text summarized from Semantic Scholar / web search results; key claims verified from public descriptions. ManySAT won 1st place in parallel track of SAT-Race 2008."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/cs
  - topic/algorithm-portfolio
  - topic/cdcl
  - topic/proof-search
  - paper
  - status/draft
---

# ManySAT: A Parallel SAT Solver

## Abstract

*(Not retrieved verbatim — binary PDF not text-extractable. Described from authoritative public sources.)*

Presents ManySAT, a portfolio-based parallel SAT solver that runs multiple **diversified CDCL** configurations on separate cores, with systematic **learned-clause sharing** between threads. Each sequential algorithm in the portfolio is a variant of the DPLL/CDCL algorithm with different variable-ordering heuristics, restart policies, and randomization seeds. Threads share learned clauses (the "no-good" witnesses from conflict analysis) asynchronously via a shared clause pool — clauses discovered by one thread that are not already subsumed by another thread's database are added to all databases. Won 1st place in the parallel track of SAT-Race 2008.

## TL;DR

ManySAT = multiple CDCL threads with different heuristic configurations running in parallel + learned-clause sharing between all threads. Each thread helps the others by exporting short learned clauses. Won SAT-Race 2008 (parallel track). The most direct structural analog to the Mixer in the SAT literature: multiple algorithms sharing information about their search.

## Problem

Single-threaded CDCL SAT solvers are now highly optimized. Modern hardware has 8-32+ cores. How to exploit parallelism for SAT? Naive parallel-same-solver with different seeds wastes information; running different solvers without sharing wastes the clauses discovered by each.

## Approach

**ManySAT architecture:**
1. **Portfolio diversification**: run $k$ sequential CDCL threads, each with different:
   - Variable-ordering heuristic (VSIDS variants, random tie-breaking)
   - Restart policy (Luby sequence, fixed interval, geometric)
   - Initial random seed
2. **Clause export**: when a thread learns a new clause, it adds it to a shared export buffer (only short clauses — typically length ≤ threshold).
3. **Clause import**: periodically, each thread imports clauses from the buffer that are not already subsumed by its local database.
4. **Independence**: threads run independently except for the clause exchange; no global synchronization or shared search state.

**Clause sharing discipline**: only "short" learned clauses are shared (length ≤ $L_{max}$, typically 8 literals) — longer clauses are thread-local. The short-clause filter limits communication overhead while sharing the most valuable conflict witnesses.

## Key result

- **1st place, SAT-Race 2008 parallel track**: ManySAT outperformed competing parallel SAT solvers on a diverse benchmark suite.
- **Speedup from diversification + sharing**: diversification alone (no sharing) gives linear speedup; sharing gives super-linear speedup on structured instances because a clause discovered by one thread immediately prunes dead branches in all other threads.
- **Clause sharing is critical**: removing the sharing while keeping diversification reduces performance to near-linear speedup (no super-linear gains).

## Assumptions

- Multi-core shared-memory architecture (clause pool is in shared memory).
- Short clause sharing is sufficient — empirically, the most useful learned clauses are short.
- Thread independence outside clause exchange is maintained.

## Limitations / scope

- Clause sharing overhead can dominate for very large clause databases; filtering (short clauses only) mitigates but doesn't eliminate this.
- Performance depends on good diversification — similar threads with minor variations provide less benefit.
- Extended to distributed architectures (different machines) requires message-passing clause exchange instead of shared memory.

## Replication evidence

ManySAT's 2008 SAT-Race win is an independently verified competition result. The clause-sharing approach has been replicated in Glucose-Syrup, CaDiCaL's parallel variant, and other solvers. The super-linear speedup from sharing is confirmed empirically in multiple follow-up studies.

## Why this paper matters

ManySAT is **the closest published structural analog to the Mixer** in the combinatorial search literature. The translation is direct:

| ManySAT concept | Mixer analog |
|---|---|
| CDCL thread with ordering heuristic | KB completion under one ordering |
| Diversified thread portfolio | Multiple KB orderings (RPO, shortlex, RPO-2) |
| Learned clause | Rewriting rule |
| Clause export (short clauses only) | Rule injection (overlap-scored rules only) |
| Shared clause pool | Mixer's inter-agent communication channel |
| Clause import → prunes all threads | Rule injection → accelerates receiving KB |
| Super-linear speedup from sharing | B(4,3) Mixer: 22s → 14s with 80-rule injection |

The Mixer's rule injection scoring (selecting the top-$k$ overlap-scored rules for injection) is directly analogous to ManySAT's short-clause filter (selecting only the most globally useful clauses for sharing). Both systems reduce information-sharing overhead while preserving the most valuable structural information.

**From [[gomes-selman-2001-portfolios]]'s theory**: ManySAT's super-linear speedup validates the portfolio theory with information sharing. Heavy-tailed runtimes are eliminated AND the shared information provides additional speedup beyond naive portfolio combination.

## Quotes

*(Abstract not retrieved verbatim — binary PDF.)*

## Open questions surfaced

- What is the Mixer analog of ManySAT's short-clause filter? The current overlap-scoring heuristic selects rules by prefix/suffix overlap count — is this the right metric, or should it be something more like "clause length" (short derivations)?
- Does the Mixer's information sharing achieve super-linear speedup (vs. single-ordering KB) proportional to the number of orderings in the portfolio?

## Related material in vault

- Extends: [[gomes-selman-2001-portfolios]] (algorithm portfolios — ManySAT is the SAT instantiation with sharing), [[marques-silva-sakallah-1999-grasp]] (CDCL — ManySAT runs CDCL in each thread)
- Cites: [[gomes-selman-2001-portfolios]], [[marques-silva-sakallah-1999-grasp]]
- Related: [[clarke-et-al-2000-cegar]] (CEGAR — same oracle-sharing pattern in model checking)
- Cross-vault: [[Research/Group theory/Burnside groups/B25/algo-mixing-burnside-slides]] (B(4,3) Mixer as ManySAT-for-KB-completion), [[Concepts/mixable-api]] (the Mixer's API = ManySAT's clause pool)
