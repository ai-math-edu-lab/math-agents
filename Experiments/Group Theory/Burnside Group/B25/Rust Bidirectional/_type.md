---
title: Rust Bidirectional Search on B(2,5)
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: rust-bidirectional
status: inconclusive
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, project/b25, status/inconclusive, experiment-type]
---

# Experiment Type — Rust Bidirectional Search on B(2,5)

## What this technique is

A Rust implementation of config-driven KB-based word proving. Unlike the Python KBMag experiments (which try to reach *global* confluence), Rust Bidirectional targets a small set of specific relator words: it asks whether each word can be proved equal to the identity using the rules accumulated by running KB.

The binary is `src/bin/kb_mixer.rs` in the `experiments/burnside_bidirectional/` subtree (now deleted from disk; B(4,3) variant lives at `experiments/burnside/b43_bidirectional/`). It reads a TOML config specifying KB agent parameters and a `relators_file` listing target words, then runs KB + tiered reduction simultaneously.

### Architecture

1. **KB agents** (`kbprog` subprocess): 1–4 instances with different orderings. For B(2,5) the two distinct RPO orderings used were a-first (`[a,A,b,B]`) and b-first (`[b,B,a,A]`). The two RPO orderings are genuinely distinct for B(2,5) (swapping a generator with its inverse is equivalent, but swapping the two generators is not).
2. **Rule reorientation**: RPO produces length-increasing rules. On incorporation, these are flipped (`long → short`) since both directions hold as group equations, converting RPO's expanding rules into big-jump shrinking rules for the reducer.
3. **Tiered reducer**: applied per target word until proved or exhausted:
   - Tier 1a: greedy leftmost Aho-Corasick match, repeated to fixed point
   - Tier 1b: single-character braid moves `(gh)^n = 1`
   - Tier 1c: generalized braid (LCE-based, O(n log²n), finds `(xy)^n` patterns)
   - Tier 2a: multi-start (try each overlapping AC match as first application)
   - Tier 2b: multi-start random
   - Tier 3: random with stuck-counter bailout
   - Tier 4: beam search (bounded heap, forward + inverse rules)
4. **Beam search** (`src/reduce/beam.rs`): bounded heap (evict longest candidates), hash-only seen set (`RapidHashSet<u64>`), both forward (shrinking) and inverse (expanding) rules, plus braid moves at each step.

### Sanity check: random identities

The `b25_random_identities.txt` file contains words that are provably the identity in B(2,5) (constructed from the presentation relators). These serve as a lower bound: any correct reducer must prove all of them. Added in commit `bc3cba2` (2026-03-19) as "random identities as sanity check".

## Why we ran this

KB alone cannot complete B(2,5). But KB rule banks are useful: they encode structural reductions that might reduce a target word to the identity even if the full rewriting system is not confluent. Bidirectional means we attack from both ends — forward (reduce the word using KB rules) and backward (expand from identity using inverse KB rules). The B(4,3) variant of this approach succeeded (153/153 relators proved in ~3s). B(2,5) is the next target.

## What "success" means

The reducer proves that a target word is equal to the identity: the word reduces to the empty string under accumulated KB rules + braid moves + beam search. Primary target: `comm_12_9` (the specific B(2,5) commutator that is the main benchmark word). Secondary: all 119 benchmark commutator words.

## Relevant scripts

Deleted from disk. Recoverable from git at commit `bc3cba2`:
- `experiments/burnside_bidirectional/src/bin/kb_mixer.rs` — main binary
- `experiments/burnside_bidirectional/src/reduce/` — reducer implementation
- `experiments/burnside_bidirectional/configs/b25/` — B(2,5) TOML configs (dual_rpo_11_1, dual_rpo_12_7, dual_rpo_random, rpo, rpo_shortlex)

## Literature

- [[havas-wall-wamsley-1974]] — provides the B(2,5) presentation (59 equations, generators 1–34) used as the KB input for both RPO and shortlex agents; the dual-RPO config was built on this presentation's generator ordering.
- [[havas-robertson]] — KB completion framework (§2.9): the KB agents (RPO, shortlex) in the bidirectional runs generate rules within this tradition; the paper's discussion of iterative quotient-kernel strategies is analogous to how the tiered reducer chains reduction attempts.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: proving any B(2,5) commutator equal to identity via the tiered reducer would constitute an identity certificate directly relevant to the restricted-group word problem.
