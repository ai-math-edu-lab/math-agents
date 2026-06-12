---
title: KBMag overlap-scored mixing on M23
domain: group-theory
project: m23
instance: M23
experiment_type: kbmag
status: replicated
reconstructed_on: 2026-06-02
author: maumayma
wall_time_s: 1103
git_sha_or_local: local (tracking not retrofitted)
experiment_id: m23-kbmag-sweep
params_kbmag_cn: 5000
params_kbmag_ordering_rpo: true
params_kbmag_ordering_shortlex: true
params_mixer_threshold: 100000
params_mixer_batch_frac: 0.001
params_mixer_scoring: overlap-count-bisect-cached
tags: [agent/exp, user/maumayma, domain/group-theory, topic/mathieu, topic/m23, topic/knuth-bendix, topic/kbmag, topic/mixer, project/m23, status/replicated, methodology]
---

# Experiment — KBMag Overlap-Scored Mixing on M23

## Reconstruction notes

Reconstructed 2026-06-02 from: `experiments/m23_kbmag/m23_mix.py` (on-disk driver), 11 result JSON files in `results_archive/`, 18 result JSON files in `tests/results_archive/`, `experiments/m23_kbmag/converged_rpo_rules.live` (71.5MB converged rule bank), analysis scripts (`analyze_rules.py`, `deep_analysis.py`, `timeline_analysis.py`), and project memory notes. Validator independently re-verified all result JSONs 2026-06-02; see [[2026-06-02-m23-mixing-negative-result]].

## Hypothesis

Overlap-scored shortlex→RPO rule injection (same strategy that accelerates B(4,3) convergence by 37%) will reduce M23 KB convergence time from the RPO-only baseline.

**Verdict**: Hypothesis **refuted**. All 18 mixing variants are slower than baseline. The shortlex→RPO injection strategy that helps B(4,3) harms M23 convergence.

## Problem set

- Group: Mathieu group M23, one of the 26 sporadic simple groups, order 10,200,960
- Presentation: `kbmag_v1/standalone/kb_data/m23` (4KB) + `kbmag_v1/standalone/kb_data/m23_rpo` (4KB, RPO ordering variant)
- KB terminates for M23 (unlike B(2,5)/B(5,3)): RPO baseline converges to **863,186 equations**
- GAP presentation derivation scripts: `experiments/e_kbmag/m23_atlas.gap`, `m23_pres.gap`, `m23_to_kbmag.gap` (verified against ATLAS presentation)

## Mixer agents involved

- **RPO agent**: `kbmag_v1/standalone/bin/kbprog -rec` on `m23_rpo`
- **Shortlex agent**: `kbmag_v1/standalone/bin/kbprog -lex` on `m23` (scoring source)
- Injection via SIGUSR1; scoring: overlap-count with bisect + incremental CachedPreparer
- Driver: `experiments/m23_kbmag/m23_mix.py`

## Scheduler config (primary variants tested)

| Variant | Threshold | Batch | Periodic | total_injected |
|---|---|---|---|---|
| baseline | — | — | — | 0 |
| mix v1 | 100k | RPO×0.001 | 900s | 9,568 (2 events) |
| mix v2 | 100k | proportional | 10s | 76,650 (many events) |
| v10a–v10i, v13 | various | various | various | 55–4981 |

See the `tests/results_archive/*.json` files for per-variant parameters; driver encodes strategy type as command-line flag or script variant.

## Termination criteria

- kbprog reports `System is confluent` (achievable for M23; both baseline and all mixing variants converge)

## Baselines

- **baseline (primary)**: RPO only, no injection → **1,103.8s**
- **baseline_v2**: RPO-only variant → **1,023.0s**
- Both converge to identical final state: **863,186 equations**
- Timing variance across two baselines: ±80.8s

## Seeds

Not applicable — KB is deterministic.

## Metric

- Total wall-clock from kbprog start to `System is confluent`
- Secondary: `phase1_time` (single-agent convergence time) and `phase2_time` (incremental mixing phase)
- All 19 runs terminate at same final equation count (863,186), so timing is the sole differentiator

## Statistical treatment

Timing variance across two baselines is ±80s. Best mixing variant (v10f7 at 1,409.2s) is 305s above the primary baseline — **3.8× baseline variance**. The mixing slowdown is robust to baseline variance, supporting the negative result.

## Validation

- **Validator verdict** (2026-06-02): `#status/replicated` — Validator independently verified all 19 result JSONs. Same M23 presentation MD5 (05b90894…) confirmed across all runs. Same kbprog binary. RPO_CONFNUM=5000 uniform. All 19 runs terminate at 863,186 equations. See [[2026-06-02-m23-mixing-negative-result]] for full verification details.
- Validation: **Validator independent re-verification** of 19 JSON results

## Why mixing slows M23

The mechanism is not fully understood, but a working hypothesis:

The B(4,3) cascade (from 23k → 2333 rules) is triggered because the injected shortlex rules happen to cover the exact "bottleneck" critical pairs needed for the RPO cascade. In M23, which converges at 863k rules via a much longer accumulation path, there is no analogous bottleneck. The injection adds rules that create *new* critical pairs in the RPO agent, forcing it to process more equations before confluence — hence the slowdown. The injection does work, but it works against convergence rather than toward it.

This interpretation is consistent with the v10f7 result (fewer rules injected = less slowdown) and v10f6 (many rules injected quickly = most slowdown).

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[M23/_progress]] — M23 umbrella
- [[data/kbmag-data-m23]] — presentation, result JSON locations
- [[results/kbmag-results-m23]] — full 18-variant table
- [[kbmag-tools-overview]] — KBMAG tool
- [[B43/KBMag/methodology/kbmag-overlap-scoring-b43-2026-06-02]] — B(4,3) methodology (mixing helps; contrast)
- [[2026-06-02-m23-mixing-negative-result]] — Validator verdict
- [[2026-06-02-non-b25-forensic-inventory]] — §4 M23 forensic provenance
