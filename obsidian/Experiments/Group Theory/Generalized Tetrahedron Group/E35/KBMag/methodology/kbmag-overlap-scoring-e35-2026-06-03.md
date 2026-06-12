---
title: KBMag overlap-scored mixing on E35
domain: group-theory
project: e35
instance: E35
experiment_type: kbmag
status: inconclusive
reconstructed_on: 2026-06-03
author: maumayma
wall_time_s: 2087
git_sha_or_local: local (tracking not retrofitted)
experiment_id: e35-kbmag-mix-2026-03
params_kbmag_cn: 5000
params_kbmag_ordering_rpo: true
params_kbmag_ordering_shortlex: true
params_mixer_threshold: 100000
params_mixer_batch_frac: 0.001
params_mixer_periodic_s: 600
params_mixer_scoring: overlap-count-bisect-cached
tags: [agent/exp, user/maumayma, domain/group-theory, topic/generalized-tetrahedron-group, topic/knuth-bendix, topic/kbmag, topic/mixer, project/e35, status/inconclusive, methodology]
---

# Experiment — KBMag Overlap-Scored Mixing on E35

## Reconstruction notes

Reconstructed 2026-06-03 from: `experiments/e_kbmag/e35_mix.py` (on-disk driver), `experiments/e_kbmag/runs_e35_mix/logs/rpo_log.txt` and `shortlex_log.txt`, `experiments/e_kbmag/progress_e35_mix.log`, and forensic inventory §5 (2026-06-02). Date of run: approximately 2026-03-03 (from `progress_e35_mix.log` header). Run interrupted by user at ~2087s.

## Group identity (from primary source)

```
E35 = <a, b, c | a² = b³ = c³ = (ac)² = (bc)² = (abababab²abab²ab²)² = 1>
```
Source file: `experiments/_inputs/kbmag/e35` (652 bytes), header comment: "Generalized tetrahedron group (Rosenberger-Scheer). Finiteness is OPEN (one of 5 unsettled cases)."

- 3 generators: a (order 2), b (order 3), c (order 3)
- Inverse expansion in e35_mix.py: A→a (a is self-inverse), B→bb (b³=1 so b⁻¹=b²), C→cc
- Ordering in kb_data: shortlex (default); experiment used RPO for the KB agent

## Hypothesis

By analogy with B(4,3), overlap-scored shortlex→RPO injection will trigger a KB cascade on E35 within feasible runtime, establishing a practical KB completion path for this open-finiteness group.

**Current status**: Hypothesis **not confirmed** in 2087s. Rule banks growing continuously (RPO: 1.18M, shortlex: 1.76M at interrupt). No cascade observed.

## Problem set

- Group: E35, a generalized tetrahedron group in the Rosenberger-Scheer classification
- Presentation: `experiments/_inputs/kbmag/e35` (6 equations)
- Finiteness: OPEN — one of 5 unsettled cases in the Rosenberger-Scheer classification
- If KB terminates: would confirm finiteness (KB completion termination ⟹ group is finite for fp groups)

## Mixer agents

- **RPO agent**: `kbmag_v1/standalone/bin/kbprog -rec` on e35 presentation
- **Shortlex agent**: `kbmag_v1/standalone/bin/kbprog -lex` on e35 (scoring source)
- Injection: overlap-count scoring, bisect + incremental CachedPreparer
- Driver: `experiments/e_kbmag/e35_mix.py`

## Scheduler config

- First injection: when RPO crosses threshold = 100,000 rules
- Batch size: proportional RPO × 0.001
- Periodic: every max(600s, last_scoring_time × 2)
- Sample mult: 20

## Termination criteria

- kbprog reports `System is confluent` (desired; would imply E35 is finite)
- User interruption (actual outcome at ~2087s)

## Baselines

No RPO-only baseline run found for E35. The comparable context: kb_data/e35.kbprog (21MB) represents a standalone KB run state; this was not run to confluence within the archived state.

## Seeds

Not applicable — KB is deterministic.

## Metric

- Primary: time to cascade (RPO rule count sustained decrease)
- Secondary: rule counts at interrupt

## Setup

- Driver: `experiments/e_kbmag/e35_mix.py`
- kbprog params (RPO): `-me 1e9 -ms 1e9 -t 5000 -cn 5000 -rec`
- Note: cn=5000 (same as B53 server, not the cn=100k used in B43)

## Validation

- Not applicable — no convergence achieved
- If KB terminates: proof of finiteness would follow from the KB-completeness theorem (a finitely presented group is finite iff its KB completion terminates and the final rule set determines a finite automaton). Validator review would be required.
- Validation: **none** — inconclusive run

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[E35/_progress]] — E35 umbrella
- [[data/kbmag-data-e35]] — presentation, run location
- [[results/kbmag-results-e35]] — trajectory table
- [[kbmag-tools-overview]] — KBMAG tool
- [[B53/KBMag/methodology/kbmag-overlap-scoring-b53-2026-06-02]] — B(5,3) methodology (structural parallel: PLATEAU, non-convergent)
- [[2026-06-02-non-b25-forensic-inventory]] — §5a forensic provenance
