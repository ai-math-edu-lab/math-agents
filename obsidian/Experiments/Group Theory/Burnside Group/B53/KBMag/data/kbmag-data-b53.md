---
title: KBMag data — B(5,3)
domain: group-theory
project: b53
instance: B(5,3)
experiment_type: kbmag
status: inconclusive
reconstructed_on: 2026-06-02
author: maumayma
params_kbmag_cn: 5000
params_mixer_threshold: 100000
params_mixer_batch_frac: 0.001
params_mixer_periodic_s: 600
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/knuth-bendix, topic/kbmag, project/b53, status/inconclusive, data]
---

# Data — KBMag on B(5,3)

## Input presentations

| File | Size | Description |
|---|---|---|
| `kbmag_v1/standalone/kb_data/b53_full` | 4KB | Standard B(5,3) — used in all server runs |
| `kbmag_v1/standalone/kb_data/b53_full_extended` | 20KB | Extended relator set |
| `kbmag_v1/standalone/kb_data/b53_full_extended_wtlex` | 20KB | Extended + wtlex ordering variant |
| `kbmag_v1/standalone/kb_data/b53_full_wtlex` | 4KB | Standard + wtlex ordering |
| `kbmag_v1/standalone/kb_data/b53_wtlex` | 4KB | Wtlex alternative |

## Driver scripts

- **Primary**: `experiments/burnside/b53_kbmag_mixing/v10_scored_v2.py` (on-disk)
- **Previous version**: `experiments/burnside/b53_kbmag_mixing/v10_scored.py` (also on-disk)
- **Archive**: `experiments/burnside/b53_kbmag_mixing/old/v7_v8.zip` (728KB — earlier strategy versions)

## Run locations

| Run ID | Path | Size | Status |
|---|---|---|---|
| b53-server-v2 (live banks at 97h+) | `experiments/burnside/b53_kbmag_mixing/server_logs/v10/` | 2.3GB | In-progress; snapshot only |
| Scoring log (97h) | `server_logs/b53_scoring_v2.log` | 1.6MB | 97h of injection events |
| kbprog log captures | `server_logs/v10/logs/45h_rpo_log.txt`, `97h_rpo_log.txt`, `144h_rpo_log.txt` | ~1MB each | 3 captures |

## kbprog command lines (from log headers)

**RPO agent**:
```
kbmag_v1/standalone/bin/kbprog -v -me 1000000000 -ms 1000000000 -t 5000 -cn 5000 -rec input
```

**Note**: cn=5000 (vs B43's cn=100000). The smaller tidy interval means more frequent tidy cycles but each cycle is smaller. The B53 run does NOT use the cn=100000 optimization that was key for B43.

## Rule bank snapshots

| Capture | Path | RPO rules | Shortlex rules | Elapsed | Size |
|---|---|---|---|---|---|
| 45h snapshot (kbprog log only) | `v10/logs/45h_rpo_log.txt` | ~8M | ~8M | ~162000s | Log only |
| 97h snapshot (log + live banks) | `v10/logs/97h_rpo_log.txt` + `v10/rpo/input.kbprog.live` | **11,714,026** | **41,846,556** | 349,540s | 1.2GB + 1.2GB |
| 144h snapshot (kbprog log only) | `v10/logs/144h_rpo_log.txt` | ~14,450,000 | — | 501,400s | Log only |

## Injection trajectory (from b53_scoring_v2.log)

| Event # | Elapsed | Reason | n_injected | RPO rules | Shortlex rules |
|---|---|---|---|---|---|
| #1 | 10s | THRESHOLD (101,550 ≥ 100,000) | 101 | 101,550 | 360,577 |
| #2 | 908s | PERIODIC (900s cooldown) | 8,584 | 858,420 | 1,601,251 |
| ... | ... | PERIODIC | ... | ... | ... |
| #500 | 349,107s (97h) | PERIODIC (600s cooldown) | 11,712 | 11,712,048 | 41,838,286 |

**Total injected at 97h**: 3,875,321 rules across 500 events.

## Output artifact sizes

| Artifact | Path | Size | Disposition |
|---|---|---|---|
| RPO .kbprog.live (97h snapshot) | `server_logs/v10/rpo/input.kbprog.live` | **1.2GB** | Untracked large artifact — W3 spec |
| Shortlex .kbprog.live (97h snapshot) | `server_logs/v10/shortlex/input.kbprog.live` | **1.2GB** | Untracked large artifact — W3 spec |
| Scoring log | `server_logs/b53_scoring_v2.log` | 1.6MB | Keep |
| Logs zip | `server_logs/logs.zip` | 754KB | Keep |
| v7/v8 archive | `old/v7_v8.zip` | 728KB | Keep |

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[B53/_progress]] — B(5,3) umbrella
- [[methodology/kbmag-overlap-scoring-b53-2026-06-02]] — methodology
- [[results/kbmag-results-b53]] — results table
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §2b B53 forensic provenance
