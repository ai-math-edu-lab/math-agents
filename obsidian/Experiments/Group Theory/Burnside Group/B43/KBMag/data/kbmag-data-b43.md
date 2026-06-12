---
title: KBMag data — B(4,3)
domain: group-theory
project: b43
instance: B(4,3)
experiment_type: kbmag
status: validated
reconstructed_on: 2026-06-02
author: maumayma
params_kbmag_cn: 100000
params_kbmag_me: 1000000
params_kbmag_ms: 5000000
params_mixer_batch_size: 80
params_mixer_threshold: 20000
params_mixer_scoring: overlap-count
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b43, topic/knuth-bendix, topic/kbmag, project/b43, status/validated, data]
---

# Data — KBMag on B(4,3)

## Input presentation

- **File**: `kbmag_v1/standalone/kb_data/b43_full`
- **Size**: 6,287 bytes
- **Description**: Full B(4,3) presentation — free group on 4 generators {a,b,c,d} with inverses {A,B,C,D}, exponent-3 relators (a^3=b^3=c^3=d^3=ε), and commutator relations. Standard presentation from the KBMAG distribution.
- **Alternative**: `kbmag_v1/standalone/kb_data/b43` (smaller relator set; produces `b43.kbprog` in kb_data but not used in `b43_mix.py`)

## Driver scripts

- **Primary**: `experiments/burnside/b43_kbmag_mixing/b43_mix.py` (v10d optimal params; threshold=20000, batch=80)
- **Sweep scripts (archived)**: `tests/v7_archive.zip` contains `b43_v9_bruteforce.py` (static overlap-scored), `b43_v10c_live.py` (trigger threshold sweep), `b43_v10d_batchsweep.py` (batch size sweep, definitive)
- Do not copy scripts into vault; repo is source of truth

## Run locations on disk

| Run ID | Path | Size | Status |
|---|---|---|---|
| baseline_t0 (RPO only) | `experiments/burnside/b43_kbmag_mixing/runs_mix/baseline_t0/` | ~300KB | Converged — full KBMAG tree |
| mixed_t0 (RPO+shortlex, b80_at20k) | `experiments/burnside/b43_kbmag_mixing/runs_mix/mixed_t0/` | ~68MB | Converged — full KBMAG tree |
| v7–v10d sweep | `experiments/burnside/b43_kbmag_mixing/tests/v7_archive.zip` | **2.4GB** | Archived — all runs inside zip |

## kbprog command lines

**RPO agent (both runs)**:
```
kbmag_v1/standalone/bin/kbprog -v -me 1000000 -ms 5000000 -t 1000 -cn 100000 -rec input
```

**Shortlex agent (mixed_t0 only)**:
```
kbmag_v1/standalone/bin/kbprog -v -me 1000000 -ms 5000000 -t 1000 -cn 100000 -lex input
```

**Parameter table**:

| kbprog flag | Value | Meaning |
|---|---|---|
| `-me` | 1,000,000 | Max equations (tidy threshold) |
| `-ms` | 5,000,000 | Max equation string length |
| `-t` | 1,000 | Tidying batch size |
| `-cn` | **100,000** | Confnum — tidy interval; optimal value (phase transition at cn≤50k → ~90s; cn=100k → ~22s) |
| `-rec` | — | RPO (recursive path ordering) |
| `-lex` | — | Shortlex ordering |

## Mixer injection parameters

| Parameter | Value | Source |
|---|---|---|
| Threshold | 20,000 RPO rules | Optimal (v10c sweep; 19k–21k tested) |
| Batch size | 80 rules | Optimal (v10d sweep; 50–300+ tested) |
| Scoring | Overlap-count (Rust-side) | `b43_mix.py` line 78 comment |
| Rule source | Shortlex → RPO | Overlap with RPO LHS prefix/suffix sets |

## V10d batch sweep — raw results (from project memory)

| Batch | Cascade time | Notes |
|---|---|---|
| 50 | 17.0s | Underperforms |
| **80** | **13.7s ±0.1s** | **Best** |
| 100 | 15.6s | Variance |
| 120 | 16.9s | Worse |
| 150 | 13.7s ±0.5s | Good, more variance |
| 200 | ~100s (2/3 trials) | **Death zone** |
| 250 | 13.9s ±0.2s | Safe zone |
| 300+ | No improvement | — |

## V10c trigger threshold sweep — raw results (from project memory)

| RPO trigger | Cascade time | Notes |
|---|---|---|
| 15k | 30.0s | Too early |
| 18k | bimodal | Borderline |
| **19k** | 13.7s (batch=150) | Also good |
| **20k** | 14.0s | Optimal |
| 21k | 21.2s | Too late |

## Output artifact sizes

| Artifact | Path | Size | Disposition |
|---|---|---|---|
| baseline RPO .kbprog.live | `baseline_t0/rpo/input.kbprog.live` | 76KB | Tiny — convergent system; safe to keep |
| mixed RPO .kbprog.live | `mixed_t0/rpo/input.kbprog.live` | 76KB | Same convergent state |
| mixed shortlex .kbprog.live | `mixed_t0/shortlex/input.kbprog.live` | 10MB | Mid-run snapshot; not convergent |
| mixed shortlex .kbprog | `mixed_t0/shortlex/input.kbprog` | 23.9MB | Large shortlex state file |
| mixed shortlex .reduce | `mixed_t0/shortlex/input.reduce` | 32.8MB | Shortlex reduce file |
| v7–v10d archive | `tests/v7_archive.zip` | **2.4GB** | All sweep run artifacts; see W3 spec |

## RPO cascade trajectory (B(4,3), cn=100k)

The RPO rule bank follows a consistent trajectory regardless of mixing:
- **Growth phase**: 0 → ~21k rules in ~2–3s
- **Cascade trigger point**: ~20–23k rules (natural if no injection; injected at 20k in v10d)
- **Cascade**: ~21k → 16k → 10k → 6.8k → 5k → 3.5k → 4354 → **2333** (convergent)
- **Bottleneck**: 4354 → 2333 eliminates 2021 equations; takes ~17s in baseline, ~7s post-injection

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[B43/_progress]] — B(4,3) umbrella
- [[methodology/kbmag-overlap-scoring-b43-2026-06-02]] — methodology note (hypothesis, sweep design)
- [[results/kbmag-results-b43]] — results table
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §1 B43 forensic provenance
