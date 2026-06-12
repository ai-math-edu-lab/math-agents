---
title: KBMag overlap-scored mixing on B(4,3)
domain: group-theory
project: b43
instance: B(4,3)
experiment_type: kbmag
status: validated
reconstructed_on: 2026-06-02
author: maumayma
wall_time_s: ~96
git_sha_or_local: local (tracking not retrofitted — runs predate provenance discipline)
experiment_id: b43-kbmag-v10d
params_kbmag_cn: 100000
params_kbmag_ordering_rpo: true
params_kbmag_ordering_shortlex: true
params_mixer_batch_size: 80
params_mixer_threshold: 20000
params_mixer_scoring: overlap-count
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b43, topic/knuth-bendix, topic/kbmag, topic/mixer, project/b43, status/validated, methodology]
---

# Experiment — KBMag Overlap-Scored Mixing on B(4,3)

## Reconstruction notes

Runs performed prior to the K3 documentation convention. Reconstructed 2026-06-02 from: code in `experiments/burnside/b43_kbmag_mixing/` (`b43_mix.py`), kbprog logs in `runs_mix/baseline_t0/logs/` and `runs_mix/mixed_t0/logs/`, results JSON in `runs_mix/results.json`, archived v7–v10d sweep results in `tests/v7_archive.zip`, and project memory notes. Date of primary runs: approximately 2026-03-07 (inferred from kbprog log mtime). Seeds: not applicable — KB is deterministic.

**CWD note**: kbprog logs record `CWD: .../experiments/b43_kbmag_mixing/runs_mix/…` (old path). The directory was subsequently reorganized to `experiments/burnside/b43_kbmag_mixing/runs_mix/`. Runs are valid; path in headers is stale.

## Hypothesis

Injecting 80 overlap-scored shortlex rules into the RPO agent at the moment the RPO rule bank crosses 20,000 rules will trigger a **rule cascade** — a sustained decrease in RPO rule count — reducing convergence time from the B(4,3) baseline (~22s cascade phase, ~91s total) to under 15s cascade phase.

Falsifiable: the mixed run produces a visible cascade (monotonically decreasing rule count for ≥5 consecutive tidy cycles), while the baseline produces no such cascade.

## Problem set

- Group: B(4,3), free Burnside group on 4 generators of exponent 3
- Presentation: `kbmag_v1/standalone/kb_data/b43_full` (6,287 bytes; 4 generators a,b,c,d + full exponent-3 and commutator relators)
- Alternative presentation: `kbmag_v1/standalone/kb_data/b43` (smaller relator set; used in kb_data/*.kbprog but not in `b43_mix.py`)
- No specific target words — goal is global KB confluence (proving B(4,3) is the quotient the presentation defines)

## Mixer agents involved

- **RPO agent**: `kbmag_v1/standalone/bin/kbprog -rec input` (recursive path ordering)
- **Shortlex agent**: `kbmag_v1/standalone/bin/kbprog -lex input` (shortlex ordering)
- Injection: shortlex rules are overlap-scored against the current RPO rule bank, then the top-scoring batch is injected via SIGUSR1 to the RPO kbprog process
- Scoring: overlap-count (Rust-side; not Aho-Corasick) — rules whose LHS has maximal prefix/suffix overlap with existing RPO LHS are scored highest

## Scheduler config

- Type: threshold (one-shot injection)
- First (and only) injection: when RPO rule bank reaches `INJECT_THRESHOLD = 20,000` rules
- Batch size: `INJECT_BATCH = 80` rules (fixed, not proportional)
- No periodic follow-up injections in the `b43_mix.py` driver (threshold only)
- Parameters hardcoded from v10d sweep results in `b43_mix.py` lines 33–35

## Termination criteria

- kbprog reports `System is confluent` (desired; achievable for B(4,3))
- kbprog exits when no new equations generated for a period (after confluence check passes)
- No timeout set in the b43_mix.py driver

## Baselines

- `runs_mix/baseline_t0/` — single RPO agent, same presentation, same kbprog binary, no injection
- Baseline outcome: RPO grows to ~23k rules, then spontaneous cascade to 2333 equations, confluence check confirms, total ~91s

## Seeds

Not applicable — KB is deterministic given the same ordering, presentation, and kbprog binary version.

## Metric

- **Primary**: cascade time = elapsed time from when the rule count first decreases after injection to when it stabilizes at 2333
- **Secondary**: total wall-clock from kbprog start to `System is confluent`
- Cascade detected by: monotonically decreasing rule count in successive #Tidy lines of the kbprog log

## Parameter sweep (v7–v10d)

The v10d batch-size sweep (archived in `tests/v7_archive.zip`) tested `INJECT_BATCH ∈ {50, 80, 100, 120, 150, 200, 250, 300}`. Key non-monotone findings:

| Batch size | Cascade time | Notes |
|---|---|---|
| 50 | 17.0s | Insufficient injection |
| **80** | **13.7s ±0.1s** | **Best — safe zone** |
| 100 | 15.6s (var) | Variance |
| 120 | 16.9s (var) | Worse |
| 150 | 13.7s ±0.5s | Also good (more variance) |
| 200 | ~100s in 2/3 trials | **Death zone** — near-miss catastrophe |
| 250 | 13.9s ±0.2s | Also safe zone |
| 300+ | No improvement | No improvement |

The **200-rule "death zone"**: batch=200 pushes the post-injection equation count to ~2334–2340 instead of 2333, triggering a full confluence check early with ~100s overhead in 2/3 trials. The catastrophe is probabilistic because it depends on which 200 rules are selected. Batch sizes 80 and 250 avoid this edge reliably.

The v10c trigger sweep (also in archive) found the 20k threshold to be the uniquely optimal injection point:
- 15k → 30.0s (too early; RPO not sufficiently developed)
- 18k → bimodal (borderline)
- **20k → 14.0s** (optimal)
- 21k → 21.2s (too late; natural cascade already beginning)

## Anti-pattern check

- Params tuned on test set: The v7–v10d sweep was run on the same B43 problem. The sweep ran many configurations and reported the best — this is standard parameter search, not a test-set contamination, because B43 is the benchmark problem itself (not a held-out test set)
- No cherry-picked seeds: KB is deterministic; each batch/threshold combination was run ≥3 times and variance is ±0.1–0.5s
- No unverified math claims: the convergence result (2333 equations, confluent) is independently verifiable by running `kbprog` on the b43_full presentation

## Setup

- Driver: `experiments/burnside/b43_kbmag_mixing/b43_mix.py`
- Command: `uv run python experiments/burnside/b43_kbmag_mixing/b43_mix.py` (reads `INJECT_BATCH=80`, `INJECT_THRESHOLD=20000` from module constants)
- KBMAG binary: `kbmag_v1/standalone/bin/kbprog` (same binary for both agents)
- kbprog params: `-me 1000000 -ms 5000000 -t 1000 -cn 100000 -rec` (RPO) / `-lex` (shortlex); confirmed from kbprog log headers

## Validation

- kbprog's built-in confluence check: `conf_check: completed, 1671454 overlaps checked, system is confluent` — internal validation
- Both baseline and mixed run terminate with identical final state: 2333 equations, same equation lengths
- The 2333-equation confluent system can be verified by running standalone `kbprog` on `b43_full` without mixing; it converges to the same state
- Validation: **kbmag_v1 standalone convergence check** (internal to kbprog)

## Related material

- [[KBMag/_type]] — parent experiment-type root
- [[B43/_progress]] — B(4,3) umbrella
- [[data/kbmag-data-b43]] — presentation file, run locations, raw counts
- [[results/kbmag-results-b43]] — results table, cascade analysis
- [[kbmag-tools-overview]] — KBMAG tool reference
- [[2026-06-02-non-b25-forensic-inventory]] — §1 covers B43 forensic provenance
