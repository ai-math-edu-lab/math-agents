---
title: "Algorithm Mixing: From Sorting to Burnside Groups (slide deck)"
authors:
  - Vlad Stepanov
  - Maria Matveeva
year: 2025
venue: "Internal slide deck (Gradarius & AI In Math & Math Education Lab)"
source: "docs/slides/algo-mixing-burnside.md"
source_path: "docs/slides/algo-mixing-burnside.md"
related_artifacts:
  - "docs/slides/flamegraph.svg"
url: ""
language: en
domain: methodology
methodology_type: methodology
relevance: 1
key_concepts:
  - "[[Concepts/kb-mixing-stagnation]]"
  - "[[Concepts/mixable-api]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[havas-newman-1980]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
  - "[[grobner]]"
cited_by:
  - "[[b25-finiteness-11.48-kostrikin]]"
quality_notes: "Internal slide deck — not a peer-reviewed paper. Contains verbatim run logs and results for B(4,3) breakthrough (33 min, 2333 rules) and validation experiments (B(2,4), B(3,3)). Key Validator flag: 'witness words' claim (~50 words for B(2,5)) is not sourced to any paper — verify before relying on as a proof strategy. B(4,3) confluence result (1,702,360 pairs, 0 failures) is empirical verification, not a proof of mixed KB soundness. Old content-type tag #concept replaced with #paper per F4.2 decision."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/burnside
  - topic/b25
  - topic/knuth-bendix
  - topic/kbmag
  - topic/mixer
  - paper
  - status/validated
project: mixer-core
---

# Algorithm Mixing: From Sorting to Burnside Groups

Stepanov & Matveeva (2025, internal). Primary public-facing account of the B(4,3) breakthrough and the Mixer methodology. Source: internal slide deck at `docs/slides/algo-mixing-burnside.md`.

**Note on this summary:** introductory pedagogy (group axioms, Rust vs C engineering rationale) is omitted. Math and experiment data are quoted verbatim.

## Abstract

> No verbatim abstract — source is an internal slide deck. TL;DR below summarizes the deck's contribution.

## TL;DR

Presents the Mixer methodology (interleaving KB orderings with rule sharing, analogized to TimSort), validates it on B(2,4) and B(3,3), then reports the **B(4,3) breakthrough**: two KB orderings in 33 minutes produced a 2,333-rule confluent rewriting system for B(4,3) = ⟨a,b,c,d | w³=1⟩, verifying |B(4,3)| = 3^14 = 4,782,969. Frames B(2,5) as the next target.

## Problem

**Why does no single KB ordering succeed on B(4,3)?**

- Pure RPO: stagnates at ~2,000 rules.
- Pure Shortlex: "hopeless — would need ~500k rules."
- GAP's Knuth-Bendix: hours, no completion.

The No Free Lunch framing from the deck:
$$\mathbb{E}[\text{perf} \mid \text{our problems}] \neq \mathbb{E}[\text{perf} \mid \text{all problems}]$$

Our Burnside group problems have structure that neither pure RPO nor pure shortlex exploits alone. The question: can mixing orderings cooperatively exploit this structure?

## Approach

**Mixing strategies taxonomy (from deck):**

| Strategy | Description | Example |
|---|---|---|
| Switching | Choose one algorithm | TimSort's run detection |
| Racing | Run in parallel, take winner | SAT solver portfolios |
| Cascading | Try cheap first, fall back | Database query optimization |
| **Interleaving** | Alternate between algorithms | Our B(4,3) approach |

The B(4,3) solution uses **interleaving with rule injection**: two KB orderings (r2l_rpo_loop and rpo_iter) run simultaneously, sharing discovered rules every 10 iterations. The stagnation metric triggers injection when one agent is "stuck" and the other has new rules.

**Motivating analogy: TimSort (Tim Peters, 2002):**
- Insertion Sort: O(n²) worst case, O(n) on nearly-sorted.
- Merge Sort: O(n log n) always, stable, good for large data.
- TimSort: detect natural runs → extend with insertion sort → merge. Often O(n) on real data.
- KB analogy: no single ordering is always best; combining them exploits input structure.

**B(2,5) attack framing (from deck):**
> "There exist ~50 witness words w₁,...,w₅₀ such that: if wᵢ = e for all i, then B(2,5) is finite. Strategy: Build a rewriting system that can reduce these witnesses to e."

**⚠ Validator flag:** The "~50 witness words" claim is not cited to any source in the deck. Do not rely on this as a proof strategy until Validator verifies the count and originating paper.

## Key result

**Validation experiments (verbatim numbers):**

| Problem | Pure RPO | Pure Shortlex | Mixed | Mixed Time |
|---|---|---|---|---|
| B(2,4) (|G|=4096) | 159 rules, ~2s | 822 rules, ~25s | 159 rules | ~1s |
| B(3,3) (|G|=2187) | 63 rules, ~0.5s | 1,809 rules, ~5min | 63 rules | ~0.3s |

Pattern: Mixed matches the best rule count (RPO's), but faster.

**B(4,3) breakthrough — overnight run (verbatim log, selected):**

```
[22:55:17] B(4,3) Overnight Experiment — Timeout: 12 hours
[23:00:17]  5m | r2l_rpo_loop | rules=160060 | stag=0.03  ← exploding
[23:00:17]  5m | rpo_iter     | rules=  4088 | stag=0.14  ← stagnating
[23:05:18] 10m | rpo_iter     | rules=  2949 | stag=0.04  ← got new blood, shrinking
[23:10:18] 15m | r2l_rpo_loop | rules= 60035 | stag=0.08  ← got rules from rpo!
[23:15:19] 20m | r2l_rpo_loop | rules=  4415 | stag=0.03  ← boiling down
[23:20:19] 25m | rpo_iter     | rules=  2333 | complete=True  ← !!!
[23:28:07] Total time: 0.55 hours | Shares: 54
```

**Final result:** Both agents converged to **2,333 rules** in 33 minutes (0.55 hours). 54 rule-sharing events. Neither had succeeded alone in several days.

**Known orders table (from deck):**

| m\n | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **2** | 1 | 4 | 27 | 4,096 | ? |
| **3** | 1 | 8 | 2,187 | 2^69 | ? |
| **4** | 1 | 16 | **3^14 ✓** | 2^422 | ? |
| **5** | 1 | 32 | 3^25 | 2^2728 | ? |

The ✓ marks our B(4,3) result.

**B(4,3) relators (verbatim):**
$$a^3=b^3=c^3=d^3=e$$
$$[a,b]^3=[a,c]^3=[a,d]^3=[b,c]^3=[b,d]^3=[c,d]^3=e$$
$$[[a,b],c]^3=[[a,b],d]^3=[[a,c],d]^3=[[b,c],d]^3=e$$
$$[[[a,b],c],d]^3=e$$

## Assumptions

- Mixed KB produces correct results (the deck explicitly states: "Our mixed KB said that it was confluent. But no one proved that mixed KB is actually correct."). Correctness is empirically verified, not proved.
- The "~50 witness words" framing for B(2,5) finitude is assumed from an unnamed source — unverified.
- B(4,3) ordering `r2l_rpo_loop` is a standard variation; the deck does not formally define it.

## Limitations / scope

- The deck does NOT claim B(2,5) is finite or infinite.
- The B(4,3) result is not peer-reviewed as of deck date ("TBD" for publication).
- Mixed KB soundness is not proved theoretically — only empirically validated via confluence check.
- The deck's claim "n ≥ 8000: infinite" should be corrected to n ≥ 665 (Adyan's sharpened bound; see [[havas-newman-1980]]).
- The future-work slide lists B(5,3) order as 3^14 — this appears to be an error; 3^14 is B(4,3)'s order. B(5,3)'s order is 3^25 per the order table in the same deck.

## Replication evidence

**Confluence verification (verbatim):**
```
Total critical pairs: 1,702,360
Failed pairs:         0
Time: 3689.00s (≈ 61 min)
RESULT: SUCCESS — System is confluent!
```

**Group enumeration:** BFS from identity, applying generators + reduce → confirmed |B(4,3)| = 3^14 = 4,782,969. Independent cross-validation: separate code confirmed result.

## Why this paper matters

This slide deck is the **founding document** of the Mixer project — the first public description of the B(4,3) breakthrough and the methodology that achieved it. It defines the Mixer's core design principles (interleaving, rule sharing, stagnation-based injection), establishes the B(2,5) target, and provides verbatim run logs and numbers that are the baseline for all subsequent experiments.

The deck also contains the only record of the B(2,4) and B(3,3) validation experiments — these have no dedicated experiment notes in the vault and should be backfilled by Experimenter-B25 (see Open questions below).

## Quotes

> "Our mixed KB said that it was confluent. But no one proved that mixed KB is actually correct." — slide deck, on empirical vs. theoretical validation

> "Cross-pollination: r2l's explosion feeds rpo, rpo's convergence feeds r2l." — slide deck, on the cooperation mechanism

## Open questions surfaced

- **Validator:** Verify the "~50 witness words" claim for B(2,5) finitude — what is the source and exact count?
- **Experimenter-B25:** Backfill experiment notes for B(2,4), B(3,3), and B(4,3) pre-breakthrough stagnation runs (numbers are preserved verbatim above).
- What injection strategy is optimal for B(2,5)? The B(4,3) parameters (80-rule injection at 20k-rule trigger) are the template — but B(2,5) has deeper nilpotency (class 12 vs 7).
- Can RL replace the hand-tuned stagnation metric? The deck proposes RL-based scheduling as future work.

## Related material in vault

- Extends: (none — founding document)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (F4.4 will populate via `key_concepts:`)
- Cites (in vault): [[havas-wall-wamsley-1974]], [[havas-newman-1980]], [[kourovka-11.48-kostrikin-1990]], [[grobner]]
- Cited by (in vault): [[kourovka-11.48-kostrikin-1990]], [[b25-finiteness-11.48-kostrikin]], [[havas-newman-1980]] (cross-referenced), [[Experiments/Group Theory/Burnside Group/B25/_progress]] and multiple B25 methodology notes
- Also see: [[mixable-api]], [[kb-mixing-stagnation]]
