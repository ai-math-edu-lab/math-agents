---
title: KBMag results — B(4,3)
domain: group-theory
project: b43
instance: B(4,3)
experiment_type: kbmag
status: validated
reconstructed_on: 2026-06-02
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b43, topic/knuth-bendix, topic/kbmag, topic/mixer, project/b43, status/validated, results]
---

# Results — KBMag on B(4,3)

## Results table

All runs use `kbmag_v1/standalone/bin/kbprog` on `b43_full` (6,287 bytes). cn=100,000 throughout. Cascade time = time from peak rule count to first reach of 2333 equations.

| Run ID | Date | Parameters (changed from baseline) | Outcome | Cascade time | Total wall-clock | Final eqns | Validated by |
|---|---|---|---|---|---|---|---|
| baseline | 2026-03-07 | RPO only, no injection | Converged | **22.0s ±0.1s** | ~91s | 2333 | kbmag_v1 conf_check (1671454 overlaps) |
| v10d-b80-t20k | 2026-03-07 | batch=80, threshold=20k | Converged | **13.7s ±0.1s** | ~96s | 2333 | kbmag_v1 conf_check (1671454 overlaps) |
| v10d-b150-t19k | (in archive) | batch=150, threshold=19k | Converged | 13.7s ±0.5s | ~97s | 2333 | kbmag_v1 conf_check |
| v10d-b250-t20k | (in archive) | batch=250, threshold=20k | Converged | 13.9s ±0.2s | ~96s | 2333 | kbmag_v1 conf_check |
| v10d-b200-t20k | (in archive) | batch=200, threshold=20k | Converged (2/3 trials) | ~100s (2/3 fail) | ~175s avg | 2333 | kbmag_v1 conf_check |
| v10d-b100-t20k | (in archive) | batch=100, threshold=20k | Converged | 15.6s | ~96s | 2333 | kbmag_v1 conf_check |
| v10d-b50-t20k | (in archive) | batch=50, threshold=20k | Converged | 17.0s | ~93s | 2333 | kbmag_v1 conf_check |
| v10c-t15k | (in archive) | batch=80, threshold=15k | Converged | 30.0s | ~106s | 2333 | kbmag_v1 conf_check |
| v10c-t18k | (in archive) | batch=80, threshold=18k | Bimodal | varies | varies | 2333 | kbmag_v1 conf_check |
| v10c-t21k | (in archive) | batch=80, threshold=21k | Converged | 21.2s | ~97s | 2333 | kbmag_v1 conf_check |

**Archived runs** (v7–v10d sweep): all in `experiments/burnside/b43_kbmag_mixing/tests/v7_archive.zip` (2.4GB); only summary metrics in this table. Individual run logs and rule banks are inside the archive.

## Cascade log — baseline vs v10d (selected tidy lines)

**Baseline** — natural cascade from `baseline_t0/logs/rpo_log.txt`:
```
#Tidy: 4354->2333 eqns (-2021 elim, 2021 lhs-red, 4 rhs-red); len: 24175,45149; 2334 st; 21s
#conf_check: completed, 1671454 overlaps checked, system is confluent (70s)
```

**v10d injection** — cascade from `mixed_t0/logs/rpo_log.txt`:
```
#SIGUSR1 received, will check inject file at next tidy          ← at ~23k rules, ~2s
#Injected 80 rules (0 parse-skipped)
#Tidy: 23457->21473 eqns (-1984 elim, ...)                      ← cascade begins
...
#Tidy: 4354->2333 eqns (-2021 elim, 2021 lhs-red); 13s          ← bottleneck ~7s faster
#conf_check: ... system is confluent (76s)
```

The injection fires when RPO reaches ~23k rules (SIGUSR1 at next tidy after INJECT_THRESHOLD=20k crossed), triggering an immediate cascade down to 2333. The 4354→2333 bottleneck step (which takes ~17s in baseline) takes ~7s post-injection.

## Version history

**v9 (static overlap-scored)**: First version using overlap scoring to select injection candidates from a static pre-computed rule bank. Established that overlap scoring outperforms naive injection.

**v10c (trigger threshold sweep)**: Swept RPO trigger thresholds 15k–21k. Found 20k uniquely optimal: 15k injects too early (RPO not sufficiently built), 21k is too late (natural cascade already beginning).

**v10d (live batch-size sweep)**: Swept batch sizes 50–300+ with live scoring. Found non-monotone response. 80 and 250 are "safe zones"; 200 is a probabilistic "death zone" that pushes the post-injection equation count to 2334–2340 (vs. the target 2333), triggering a premature confluence check with ~100s overhead.

## Main findings

1. **Mixing works on B(4,3)**: Injecting 80 well-chosen shortlex rules at the 20k-rule threshold reduces cascade time from 22s to 13.7s — a **37% speedup** in the cascade phase.

2. **The speedup is rule-cascade acceleration, not total speedup**: Total wall-clock changes from ~91s (baseline) to ~96s (v10d) because the confluence check takes ~76s in both cases (same 1,671,454 overlaps). The cascade phase gain is real but the confluence check dominates total time.

3. **Non-monotone batch sensitivity**: Batch size response is not monotone. The 200-rule "death zone" near the target equation count (2333) makes injection dangerous at certain batch sizes. The underlying mechanism: 200 rules push the active equation count above 2333, triggering a premature confluence check mid-cascade.

4. **Threshold sensitivity is unimodal**: Only the 20k injection point triggers a fast cascade. Earlier (15k) is too weak; later (21k) is too slow because the natural cascade is already beginning.

5. **cn=100k is critical**: The confnum parameter (tidy interval) is a previously known parameter with a phase transition at cn≤50k → ~90s cascade. This experiment uses cn=100k throughout; mixing gains are measured against that already-tuned baseline.

## Open questions

1. Can the confluence check time (~76s) be reduced? It dominates total wall-clock. A multi-threaded or incremental confluence check would reduce total time more than further cascade optimization.

2. Does the cascade mechanism generalize to B(5,3)? The B53 KBMag server run (97h+) suggests B(5,3) does not converge under this approach — the RPO rule bank reached PLATEAU at 11.7M rules. See [[B53/_progress]].

3. Is the 2333 final equation count the minimal confluent system for B(4,3)? The `b43_full.reduce` file in kb_data (76KB) encodes the completed reduction system; this question is answered there.

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[B43/_progress]] — B(4,3) umbrella
- [[data/kbmag-data-b43]] — parameter details, run locations
- [[methodology/kbmag-overlap-scoring-b43-2026-06-02]] — hypothesis, sweep design, validation
- [[kbmag-tools-overview]] — KBMAG tool
- [[B25/KBMag/results/kbmag-results]] — B(2,5) KBMag results (no convergence; contrast with B43)
- [[2026-06-02-non-b25-forensic-inventory]] — §1 forensic provenance
