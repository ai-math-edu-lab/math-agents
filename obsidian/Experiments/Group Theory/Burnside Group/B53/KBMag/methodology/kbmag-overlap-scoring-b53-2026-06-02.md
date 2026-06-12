---
title: KBMag overlap-scored mixing on B(5,3)
domain: group-theory
project: b53
instance: B(5,3)
experiment_type: kbmag
status: inconclusive
reconstructed_on: 2026-06-02
author: maumayma
wall_time_s: 349540 (97.1h, still running at capture)
git_sha_or_local: local/remote (tracking not retrofitted)
experiment_id: b53-kbmag-server-v2
params_kbmag_cn: 5000
params_mixer_threshold: 100000
params_mixer_batch_frac: 0.001
params_mixer_periodic_s: 600
params_mixer_scoring: overlap-count-bisect-cached
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/knuth-bendix, topic/kbmag, topic/mixer, project/b53, status/inconclusive, methodology]
---

# Experiment — KBMag Overlap-Scored Mixing on B(5,3)

## Reconstruction notes

Reconstructed 2026-06-02 from: `experiments/burnside/b53_kbmag_mixing/v10_scored_v2.py` (on-disk driver), `server_logs/b53_scoring_v2.log` (97h scoring log), kbprog log captures at 45h/97h/144h in `server_logs/v10/logs/`, and rule bank snapshots in `server_logs/v10/`. Original run on remote server at `/home/maria/algo_mixing/experiments/b53/runs_v10_v2/`. Local captures are snapshots; the run may still be active.

## Hypothesis

By analogy with B(4,3), injecting overlap-scored shortlex rules into an RPO agent will trigger a KB cascade on B(5,3) — a sustained reduction in rule count — within feasible run time (<100h).

Falsifiable: the RPO agent enters a non-EXPLORATION phase (EXPLOITATION or cascade) at some point in the run.

**Current verdict**: Hypothesis is **not confirmed as of 97h** — both agents are in PLATEAU phase (near-zero growth rate, no rule elimination). The run may still be active.

## Problem set

- Group: B(5,3), free Burnside group on 5 generators of exponent 3
- Presentation: `kbmag_v1/standalone/kb_data/b53_full` (4KB, standard B(5,3))
- Alternative presentations in kb_data: `b53_full_extended` (20KB, more relators), `b53_full_extended_wtlex`, `b53_full_wtlex`, `b53_wtlex`
- No specific target words — goal is global KB confluence

## Mixer agents involved

- **RPO agent**: `kbmag_v1/standalone/bin/kbprog -rec` with b53_full
- **Shortlex agent**: `kbmag_v1/standalone/bin/kbprog -lex` with b53_full as SRC (scoring source)
- Scoring backend: sorted array + bisect (stdlib) + incremental `CachedPreparer` (v10_scored_v2.py)
- Injection via SIGUSR1 to RPO kbprog process

## Scheduler config

- First injection: when RPO crosses `threshold = 100,000` rules
- Batch size: proportional `RPO_rules × batch_frac = 0.001` (no hard cap)
- Periodic: every `max(600s, last_scoring_time × 2)` — slowdown as scoring grows
- Sampling: `batch × 20` candidates scored, top `batch` selected
- Cooldown note: by event #500 (97h), each injection batch was ~11,712 rules with 92.9s scoring time → cooldown ~186s between events

## Termination criteria

- kbprog reports `System is confluent` (desired; unknown if achievable for B(5,3))
- Timeout: none (unlimited server run)

## Baselines

No separate baseline (RPO-only) run found for B(5,3). The comparable baseline inference: B(4,3) RPO-only enters cascade naturally at ~21k rules; B(5,3) RPO grows past 11.7M rules without any cascade, suggesting the natural convergence point (if it exists) is far beyond reach.

## Seeds

Not applicable — KB is deterministic.

## Metric

- **Primary**: time to first cascade (RPO rule count sustained decrease)
- **Secondary**: rule count trajectory and phase (EXPLORATION → PLATEAU → EXPLOITATION?)
- Phase detection: EMA-smoothed net growth rate; PLATEAU iff growth rate near-zero for N consecutive periods

## Setup

- Driver: `experiments/burnside/b53_kbmag_mixing/v10_scored_v2.py`
- Server run command (from log header): `nohup python3 v10_scored_v2.py` on remote server
- kbprog params (RPO): `-v -me 1e9 -ms 1e9 -t 5000 -cn 5000 -rec` (small cn=5000 unlike B43's cn=100k)
- Local capture: `server_logs/v10/` (RPO .kbprog.live 1.2GB, shortlex .kbprog.live 1.2GB)

## Validation

- No convergence achieved — no confluence check possible
- kbprog logs confirm the phase trajectory is consistent (Tidy output format matches expected pattern)
- The 97h rule bank captures are physically present on disk: `server_logs/v10/rpo/input.kbprog.live` (1.2GB), `server_logs/v10/shortlex/input.kbprog.live` (1.2GB)
- Validation: **none** — in-progress experiment

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[B53/_progress]] — B(5,3) umbrella
- [[data/kbmag-data-b53]] — run locations, rule bank sizes
- [[results/kbmag-results-b53]] — trajectory table, PLATEAU analysis
- [[B43/KBMag/methodology/kbmag-overlap-scoring-b43-2026-06-02]] — B(4,3) methodology (successful convergence; contrast)
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §2 B53 forensic provenance
