---
title: rust-bidirectional-b25-2026-05-22
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: rust-bidirectional
status: inconclusive
reconstructed_on: 2026-05-22
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, project/b25, status/inconclusive, methodology]
---

# Experiment — Rust Bidirectional KB Word Proving on B(2,5)

## Reconstruction notes

This experiment was performed prior to the K3 documentation convention. Reconstructed from git history (commits `af1b6cb`, `e90ec26`, `bc3cba2`, `b73fb6a`, `b2094fd`; branch `bidirectional-search`), the README at `experiments/burnside_bidirectional/README.md` (read from git object `bc3cba2`), TOML config `configs/b25/dual_rpo_11_1.toml` (read from git), repo directory listing from deleted files, and project memory notes on 2026-05-22.

The `experiments/burnside_bidirectional/` directory was deleted from disk (visible as `D` entries in git status). The code is recoverable via `git show bc3cba2:experiments/burnside_bidirectional/...`. The B(4,3) variant migrated to `experiments/burnside/b43_bidirectional/`; no equivalent B(2,5) migration occurred. Date of primary development: 2026-03-19 (commit `bc3cba2`). Exact run dates: unknown — reconstruction limitation. Seeds: unknown — reconstruction limitation.

## Hypothesis

Running dual-RPO KB agents on B(2,5) and applying the tiered reducer (greedy AC → braid → beam) will prove a nonzero fraction of the target relator words (comm_11_1, comm_12_7, and random identities) equal to the identity within a 10-hour timeout.

Specifically: the braid and generalized-braid tiers should at minimum prove the random identities (sanity check); the harder commutator targets may require more KB rules.

## Problem set

- Group: B(2,5)
- Three target sets (inferred from TOML configs and file names):
  1. `b25_comm_11_1_kyr.txt` — commutator `comm_11_1` (target words via Kyr-style construction)
  2. `b25_only_comm_12_7.txt` — only `comm_12_7`
  3. `b25_random_identities.txt` — 4 random identity words (sanity check, added `bc3cba2`)
  4. `b25_relators_havas_verified.txt` — standard B(2,5) relators (Havas-verified presentation)

## Mixer agents involved

- 2 `kbprog` KB agents with RPO:
  - `kb_rpo_aAbB`: ordering `[a,A,b,B]` (a-first)
  - `kb_rpo_bBaA`: ordering `[b,B,a,A]` (b-first)
- maxeqns=50,000,000, maxstates=200,000,000
- `GreedyReducerTransport` with rule reorientation (RPO expanding rules flipped to shrinking)

## Scheduler config

- Tiered reducer applied periodically as KB agents accumulate rules
- Beam width: 16,384
- beam_max_steps: 20,000
- beam_fwd_overlapping: 1,024; beam_inv_overlapping: 512
- beam_time_budget_secs: 600
- Tier2/Tier3 budgets: 60s each
- Threads: 8
- max_braid_shortenings: 200

## Termination criteria

- Per word: reducer proves word = identity, or all tiers exhausted
- Global: timeout_secs=36,000 (10 hours) per config (inferred from dual_rpo_11_1.toml)

## Baselines

Single RPO run: `configs/b25/rpo.toml`. Single shortlex run: `configs/b25/rpo_shortlex.toml`. Outcomes: unknown — reconstruction limitation.

## Seeds

Seeds: unknown — reconstruction limitation (Rust runner uses thread-based random, seed may not have been fixed).

## Metric

- Fraction of target words proved equal to identity
- Wall-clock to first proof per word
- Ultimate goal: prove comm_12_9 (or comm_12_7, comm_11_1) = identity

## Anti-pattern check

- Random identities were added as sanity check to verify the reducer is correct; these should always be proved quickly. Any failure on random identities is a correctness bug, not a hard problem.
- The main targets (comm_11_1, comm_12_7) are genuine unknowns.

## Setup

- Runner: `experiments/burnside_bidirectional/src/bin/kb_mixer.rs` (Rust binary, now deleted from disk)
- Command (reconstructed from README): `cargo run --release --manifest-path experiments/burnside_bidirectional/Cargo.toml --bin kb_mixer -- experiments/burnside_bidirectional/configs/b25/dual_rpo_11_1.toml`
- Provenance triple: git SHA `bc3cba2` (last known B(2,5) development commit); exact build hash unknown.

## Results — Baseline

Unknown — reconstruction limitation. Single-ordering baseline runs (`configs/b25/rpo.toml`) were referenced but no surviving output.

## Results — Mixed

Unknown — reconstruction limitation. No surviving run output found on disk. The `runs/b25/` directory contains KB rule bank outputs from March 2026 but no reducer proof logs linking to this binary. It is unclear whether the dual-RPO runs ever completed or whether the target words were proved.

**Sanity check (random identities)**: These must have been proved correctly by design (the braid tiers suffice for products of relators). No surviving log to confirm — reconstruction limitation.

## Validation

None documented. The Rust braid.rs implementation was verified correct (separate from the Python bug — see [[reduce-core-pipeline-b25-2026-05-22]]).

## Final verdict

**`#status/inconclusive`**

### Why

No surviving run outputs. The experiment infrastructure (KB + tiered reducer) is sound (proven for B(4,3) and B(5,3): 153/153 words at ~3s). For B(2,5), whether the tiered reducer ever proved comm_11_1 or comm_12_7 is unknown. The code was subsequently deleted from disk without a documented result. This represents a gap in provenance.

### What I'd do next

- Recover run outputs from `runs/b25/` if any reducer logs survive in that directory
- Restore the B(2,5) configs and re-run on current hardware with the corrected Python pipeline as a cross-check
- Route to Lead: should we restore the B(2,5) bidirectional Rust binary from git?

### Lead notified

- Date: unknown — reconstruction limitation

---

## Literature

- [[havas-wall-wamsley-1974]] — source of all target words: `comm_11_1` (Kyr's word convention), `comm_13_10`, `comm_12_9` and the rest are named via the 1974 generator numbering (generators 1–34); the 59 relators from this presentation are the KB input.
- [[havas-robertson]] — KB completion (§2.9); the KB agents (RPO, shortlex) in the bidirectional runs generate rules within this methodological tradition.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: each "not proved" result establishes an empirical length lower bound for the identity certificate; the corrected 7,245-char target from Reduce Core is the best starting point for a future restart of these runs.
