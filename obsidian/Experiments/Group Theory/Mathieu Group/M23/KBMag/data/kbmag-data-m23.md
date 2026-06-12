---
title: KBMag data — M23
domain: group-theory
project: m23
instance: M23
experiment_type: kbmag
status: replicated
reconstructed_on: 2026-06-02
author: maumayma
params_kbmag_cn: 5000
params_kbmag_final_eqns: 863186
tags: [agent/exp, user/maumayma, domain/group-theory, topic/mathieu, topic/m23, topic/knuth-bendix, topic/kbmag, project/m23, status/replicated, data]
---

# Data — KBMag on M23

## Input presentation

| File | Size | Description |
|---|---|---|
| `kbmag_v1/standalone/kb_data/m23` | 4KB | M23 shortlex presentation |
| `kbmag_v1/standalone/kb_data/m23_rpo` | 4KB | M23 RPO ordering variant |

**Presentation derivation**: The M23 presentation was derived from the ATLAS via GAP scripts in `experiments/e_kbmag/m23_atlas.gap`, `m23_pres.gap`, `m23_fromperm.gap`, `m23_to_kbmag.gap`. The derivation is documented in those scripts.

## Driver scripts

- `experiments/m23_kbmag/m23_mix.py` — primary mixing driver
- `experiments/m23_kbmag/tests/m23_sweep.py` — parameter sweep driver for tests/results_archive/ variants
- `experiments/m23_kbmag/analyze_rules.py`, `deep_analysis.py`, `timeline_analysis.py`, `param_divergence.py` — post-hoc analysis scripts (not drivers)

## Result JSON locations

**Primary results** (11 files):

| File | Strategy | Total injected |
|---|---|---|
| `results_archive/runs_m23_baseline_results.json` | baseline | 0 |
| `results_archive/runs_baseline_v2_results.json` | baseline v2 | 0 |
| `results_archive/runs_m23_mix_results.json` | mix v1 (threshold=100k, periodic=900s) | 9,568 |
| `results_archive/runs_m23_mix_v2_results.json` | mix v2 (threshold=100k, periodic=10s) | 76,650 |
| `results_archive/runs_mix_aggressive_results.json` | aggressive injection | varies |
| `results_archive/runs_mix_dual_orient_results.json` | dual-orientation scoring | varies |
| `results_archive/runs_mix_kill_after_1_results.json` | kill shortlex after 1 inject | varies |
| `results_archive/runs_mix_same_len_results.json` | same-length rule injection | varies |
| `results_archive/runs_mix_seq_30s_results.json` | sequential 30s interval | varies |
| `results_archive/runs_mix_single_inject_results.json` | single injection event | varies |
| `results_archive/runs_mix_single_samelen_results.json` | single injection, same-len | varies |

**Test sweep results** (18 files in `tests/results_archive/`):

v1, v2, v5, v10a–v10f7 (incl. sub-variants), v10h, v10i, v13. Each 24-line JSON with strategy name, timing, injection history.

## Converged rule bank

- **File**: `experiments/m23_kbmag/converged_rpo_rules.live`
- **Size**: 71.5MB
- **Description**: RPO rule bank at convergence (863,186 rules). Post-convergence snapshot.
- **Status**: Untracked large artifact — routes to W3 storage spec

## Large COMMITTED artifacts in kb_data (WARNING)

Five M23 KB artifact files are committed to git — see W3 spec:

| File | Size | Status |
|---|---|---|
| `kbmag_v1/standalone/kb_data/m23_rpo.kbprog` | 173MB | **COMMITTED — should be gitignored** |
| `kbmag_v1/standalone/kb_data/m23_rpo.kbprog.live` | 72MB | **COMMITTED — should be gitignored** |
| `kbmag_v1/standalone/kb_data/m23_rpo.reduce` | 98MB | **COMMITTED — should be gitignored** |
| `kbmag_v1/standalone/kb_data/m23.kbprog.live` | 86MB | **COMMITTED — should be gitignored** |
| `kbmag_v1/standalone/kb_data/m23.kbprog.live.tmp` | 59MB | **COMMITTED — should be gitignored** |

**Total committed artifact size: 488MB.** Routed to Developer (W3 brief).

## kbprog command (inferred from m23_mix.py)

RPO agent: `kbmag_v1/standalone/bin/kbprog -rec input` with m23_rpo presentation; cn=5000.

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[M23/_progress]] — M23 umbrella
- [[methodology/kbmag-mixing-m23-2026-06-02]] — methodology
- [[results/kbmag-results-m23]] — results table
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §4 M23 forensic provenance
