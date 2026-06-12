---
title: KBMag data — E35
domain: group-theory
project: e35
instance: E35
experiment_type: kbmag
status: inconclusive
reconstructed_on: 2026-06-03
author: maumayma
params_kbmag_cn: 5000
params_mixer_threshold: 100000
params_mixer_batch_frac: 0.001
tags: [agent/exp, user/maumayma, domain/group-theory, topic/generalized-tetrahedron-group, topic/knuth-bendix, topic/kbmag, project/e35, status/inconclusive, data]
---

# Data — KBMag on E35

## Input presentation

- **File**: `experiments/_inputs/kbmag/e35` (652 bytes)
- **Group**: E35 = <a,b,c | a²=b³=c³=(ac)²=(bc)²=(abababab²abab²ab²)²=1>
- **Relators**: 6 equations (power relations + two commuting-pair relations + one long product relation)
- **Ordering in file**: shortlex (default); experiment uses RPO for the KB agent

## Driver script

- `experiments/e_kbmag/e35_mix.py` (on-disk)
- Also: `experiments/e_kbmag/e35_check.gap` (GAP verification script)
- Do not copy into vault

## Run location

| Item | Path | Size | Status |
|---|---|---|---|
| RPO live rule bank | `experiments/e_kbmag/runs_e35_mix/rpo/input.kbprog.live` | ~350MB est. | Untracked large artifact |
| Shortlex live rule bank | `experiments/e_kbmag/runs_e35_mix/shortlex/input.kbprog.live` | ~380MB est. | Untracked large artifact |
| RPO log | `experiments/e_kbmag/runs_e35_mix/logs/rpo_log.txt` | ~200KB | Keep |
| Shortlex log | `experiments/e_kbmag/runs_e35_mix/logs/shortlex_log.txt` | ~200KB | Keep |
| Progress log | `experiments/e_kbmag/progress_e35_mix.log` | ~50KB | Keep |

Total e_kbmag/ dir: 383MB (live rule banks dominate).

## Committed kb_data artifacts (WARNING)

| File | Size | Notes |
|---|---|---|
| `kbmag_v1/standalone/kb_data/e35.kbprog` | 21MB | Committed KB state file — should be gitignored per W3 spec |
| `kbmag_v1/standalone/kb_data/e35.kbprog.live` | 8.4MB | Committed live rule bank |
| `kbmag_v1/standalone/kb_data/e35.reduce` | 26MB | Committed reduce file |

These 55MB of committed artifacts are from a prior standalone KB run, not the mixing experiment.

## kbprog params

**RPO agent**: `-me 1000000000 -ms 1000000000 -t 5000 -cn 5000 -rec input`

## Rule bank growth (from progress_e35_mix.log and rpo_log.txt)

| Time | RPO rules | Shortlex rules | Phase | Injections |
|---|---|---|---|---|
| t=0 | 0 | 0 | — | — |
| t=100k threshold | ~100k | growing | EXPLORATION | #1 |
| t=2036s | 1,167,039 | 1,738,606 | EXPLORATION | ~471 |
| t=2087s (interrupted) | **1,180,332** | **~1,760,000** | EXPLORATION | ~476 |

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[E35/_progress]] — E35 umbrella
- [[methodology/kbmag-overlap-scoring-e35-2026-06-03]] — methodology
- [[results/kbmag-results-e35]] — results table
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §5 forensic provenance
