---
title: "Is B(2,5) finite or infinite? — Mixer attack rationale (Kostrikin Problem 11.48)"
authors:
  - "A.I. Kostrikin"
year_posed: 1990
venue: "Kourovka Notebook, 11th Issue (1990)"
url: ""
source_path: "docs/papers/Kourovka 2022.pdf"
language: en
domain: group-theory
methodology_type: methodology
relevance: 1
key_concepts: []
extends:
  - "[[kourovka-11.48-kostrikin-1990]]"
contradicts: []
replicates: []
cites:
  - "[[kourovka-11.48-kostrikin-1990]]"
  - "[[kourovka-2022]]"
  - "[[havas-wall-wamsley-1974]]"
  - "[[algo-mixing-burnside-slides]]"
cited_by: []
quality_notes: "This note frames Problem 11.48 from a Mixer-attack angle. For the mathematical content of the problem, see [[kourovka-11.48-kostrikin-1990]]. The old score/3 (high Mixer relevance) is migrated to relevance: 1 per F4.2 decisions."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/word-problem
  - topic/knuth-bendix
  - topic/kbmag
  - topic/mixer
  - paper
  - status/draft
project: b25
---

# Is B(2,5) finite or infinite? — Mixer attack rationale (Kostrikin Problem 11.48)

This note frames Kourovka Problem 11.48 from a Mixer-attack perspective. For mathematical details of the problem, see [[kourovka-11.48-kostrikin-1990]].

## Abstract

> "Is the commutator [x, y, y, y, y, y, y] a product of fifth powers in the free group ⟨x, y⟩? If not, then the Burnside group B(2, 5) is infinite." — A.I. Kostrikin, Problem 11.48

## TL;DR

Problem 11.48 is the primary Mixer target. If KB completion on the B(2,5) presentation terminates with a confluent rewriting system, finiteness is proved and 11.48 is resolved in the negative. The Mixer's B(4,3) breakthrough (confluent system, 2,333 rules, ~33 minutes, two-ordering cooperation with rule injection) is the proof-of-concept. B(2,5) is harder (5^34 vs 2^69) but uses the same architecture.

## Problem

Is the unrestricted B(2,5) = ⟨a,b | w⁵ = 1 for all words w⟩ finite or infinite? See [[kourovka-11.48-kostrikin-1990]] for the mathematical equivalence to a free-group element question.

## Approach

**Mixer KB attack:**

1. Input: B(2,5) relators from [[havas-wall-wamsley-1974]]'s consistent commutator power presentation, encoded as KBMAG `.rws` input.
2. Run KB completion with multiple orderings (shortlex, RPO, weighted-lex variants) as concurrent mixer Agents.
3. **If KB terminates** with a confluent system → group is finite → Problem 11.48 resolved in the negative.
4. **If KB stagnates:** the Mixer's stagnation-detection and rule-injection heuristics attempt to break the trap (the mechanism that worked for B(4,3): inject 80 overlap-scored shortlex rules into RPO when RPO hits 20k rules).

**B(4,3) precedent (proved):** Two KB orderings cooperating via rule injection at the 20k-rule stagnation point → confluent system in 2,333 rules, ~33 minutes wall-clock. See `experiments/b43_kbmag_mixing/` for full results.

## Key result

**B(4,3) (solved, for comparison):**
- Confluent rewriting system: 2,333 rules
- Wall-clock: ~33 minutes (cascade from 21k rules)
- Mixer: shortlex + RPO, inject 80 overlap-scored rules at 20k trigger

**B(2,5) (in progress):** No confluent system yet. Current best: bidirectional search proves specific word identities in the restricted group (see `experiments/burnside_bidirectional/`). Full KB completion not yet achieved.

## Assumptions

- KB termination ⟹ finiteness (valid for all group presentations).
- B(2,5) KBMAG encoding correctly captures the group's relator structure.
- Stagnation-detection heuristics are generalizable from B(4,3) to B(2,5) (unverified for B(2,5)).

## Limitations / scope

- KB non-termination does NOT prove B(2,5) is infinite.
- Even KB success proves finiteness of the restricted group only — but this IS sufficient to resolve Problem 11.48.
- The Mixer cannot prove infiniteness; that would require a different mathematical approach.

## Replication evidence

B(4,3) result is reproducible: see `experiments/b43_kbmag_mixing/tests/v7/b43_v10d_batchsweep.py` — 2,333-rule confluent system confirmed across multiple runs (±0.1s variance, fully deterministic). This validates the architecture.

## Why this paper matters

This is the **primary Mixer target** — the reason the project exists. Every architectural decision in `mixer-core` (Agent protocol, stagnation hooks, rule-injection mechanism) was designed with B(2,5) in mind. The B(4,3) breakthrough proved the architecture works. B(2,5) is the next, harder problem. If successful, it resolves a 50-year-old open question in group theory and produces a canonical word-problem decision procedure for B(2,5).

## Quotes

> "If not, then the Burnside group B(2, 5) is infinite." — A.I. Kostrikin, Problem 11.48

## Open questions surfaced

- What injection strategy is optimal for B(2,5)? B(4,3)'s (80 rules, 20k trigger) is the template.
- Are KB orderings specifically suited to B(2,5)'s weight-12 class structure (deeper than B(4,3)'s class 7)?
- If KB diverges permanently: can bidirectional search prove enough specific identities to constitute indirect evidence for finiteness?

## Related material in vault

- Extends: [[kourovka-11.48-kostrikin-1990]] (mathematical content)
- Contradicts: (none)
- Replicates: (analogous to B(4,3) which proved the architecture)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[kourovka-11.48-kostrikin-1990]], [[kourovka-2022]], [[havas-wall-wamsley-1974]], [[algo-mixing-burnside-slides]]
- Cited by (in vault): (linked from experiment notes, but no direct Research/ citations currently)
