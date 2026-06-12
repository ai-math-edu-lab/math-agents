---
title: G7 experiment progress
domain: group-theory
project: g7
instance: G7
status: inconclusive
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/g7, project/g7, status/inconclusive, experiment]
---

# G7 Experiments — Progress

**G7**: A KBMAG standard test group, harder than G5. The g_kbmag mixing experiment was run on G7 but **interrupted at 60s** before convergence. One injection of 99 rules fired at ~106k RPO rules; the RPO agent was still growing at 121k rules when interrupted.

## Status

Inconclusive — run interrupted before convergence. No results.json (unlike G5). Outcomes unknown: convergence time, total equation count, whether the injection would have accelerated or decelerated convergence.

## What exists

| Item | Location | Notes |
|---|---|---|
| Driver | `experiments/g_kbmag/g5_mix.py` (same driver; g7 input) | Also used for G5 |
| Run logs | `experiments/g_kbmag/runs_g7_mix/logs/rpo_log.txt`, `shortlex_log.txt` | Interrupted at 60s |
| Rule banks | None on disk for g7_mix | Only logs remain |
| kb_data | `kbmag_v1/standalone/kb_data/g7` (4KB) + `g7.kbprog.live` | g7.kbprog.live committed |

**CWD note**: kbprog logs show `CWD: .../experiments/g5_kbmag/runs_g7_mix/...` (old path before rename).

**Injection fired**: SIGUSR1 received at ~50s (106k RPO rules); 99 rules injected. Run interrupted by Ctrl-C at ~60s with 121k rules. Post-injection trajectory not observed.

## Next steps

1. Re-run G7 experiment to completion (not just 60s)
2. Compare converged equation count to G5 (16 eqns) — G7 is likely much larger
3. Measure whether the 99-rule injection at 106k would have triggered a cascade

## Related material

- [[G5/_progress]] — G5 (converges trivially in 0.5s)
- [[kbmag-tools-overview]] — KBMAG tool
- [[B43/_progress]] — B(4,3) (similar injection-at-threshold experiment that succeeded)
- [[2026-06-02-non-b25-forensic-inventory]] — §6 covers G5/G7 forensic provenance
