---
title: kbmag-overlap-scoring-b25-2026-05-22
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: kbmag
status: inconclusive
reconstructed_on: 2026-05-22
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/mixer, topic/word-problem, project/b25, status/inconclusive, methodology]
---

# Experiment — KBMag Overlap-Scored Mixing on B(2,5)

## Reconstruction notes

This experiment was performed prior to the K3 documentation convention. Reconstructed from code in `experiments/burnside/b25_kbmag/` (b25_mix.py, b25_mix_v2.py, bench_v3.py, standalone.py), surviving server log in `experiments/burnside/b25_kbmag/server_logs/b25_scoring.log`, rule bank timestamps in `experiments/b25_reduce_core/reduce_coreless.py` (path prefixes `runs/b25/20260320_*`), repo commit history (commits `e8a9d20`, `ee949cc` and later), and project memory notes on 2026-05-22.

Date of original runs: approximately 2026-03-20 (inferred from `runs/b25/20260320_*` path timestamps in reduce_coreless.py). The server log is from a run on `/home/maria/algo_mixing/` (a remote machine). Exact date of server run: unknown — reconstruction limitation. Seeds: not applicable (KB is deterministic given same ordering and input file).

## Hypothesis

Overlap-scored shortlex→RPO rule injection will produce a measurable phase change (onset of rule cascade or nonzero rate decrease) in the B(2,5) RPO rule bank within a 1-hour mixed run, compared to an RPO-only baseline that shows no cascade.

This is falsifiable: the RPO-only baseline stays in pure EXPLORATION indefinitely, while the mixed run shows EXPLOITATION or MILD_SHRINK phase within 1 hour.

## Problem set

- Group: B(2,5), the free Burnside group on 2 generators of exponent 5
- Presentation: `kbmag_v1/standalone/kb_data/b25_full` (59 equations)
- Generators: {a, b}; inverses expanded as A→aaaa, B→bbbb (since a^5=1)
- No specific target words — the goal is global KB confluence

## Mixer agents involved

- `KBMAGAgentV2` (RPO): `kbmag_v1/standalone/bin/kbprog -rec`, confnum=5000, tidyint=5000, maxeqns=∞
- `KBMAGAgentV2` (shortlex): `kbmag_v1/standalone/bin/kbprog -lex`, confnum=5000, tidyint=5000, maxeqns=∞
- Injection via SIGUSR1 to kbprog process
- Scoring: Aho-Corasick (v1) or bisect (v2)

## Scheduler config

- Type: threshold (first injection) + periodic (subsequent)
- First injection: when RPO reaches `threshold` rules (default 20,000 for the server run; default 100,000 in code)
- Batch size: `int(rpo_rules × batch_frac)` — proportional to RPO rule count, no hard cap
- batch_frac default: 0.001 (0.1% of RPO rules per injection)
- Periodic: every `max(periodic, 2 × last_scoring_time)` seconds; default periodic=600s
- sample_mult: score batch × 20 candidates, select top batch

Server run actual params (from b25_scoring.log): threshold=20000, batch_frac=0.001, periodic=600s, sample_mult=20.

## Termination criteria

- RPO reports confluent (ideal but not expected)
- Timeout (server run: unlimited; default scripts: --timeout hours)

## Baselines

- RPO-only baseline: `python3 standalone.py --baseline` (or `b25_mix.py --baseline`)
- Neither baseline has a surviving result file; outcome inferred from general KB behavior on B(2,5): monotonic rule growth, no cascade.

## Seeds

Not applicable — Knuth-Bendix is deterministic given the same input file, ordering, and kbprog binary.

## Metric

- Primary: first time (seconds) RPO enters a non-EXPLORATION phase (EXPLOITATION, MILD_SHRINK, or convergence)
- Secondary: rule count at termination (lower = more reduction)
- Phase detection: EMA-smoothed net growth rate; EXPLOITATION iff net_growth_ema < −1.0%

## Anti-pattern check

- Tuning on test set: N/A (no "test set" for global confluence)
- The B(4,3) parameters (batch 80, threshold 20k) were applied directly without B(2,5)-specific tuning; this is a legitimate transfer test

## Setup

- Runner: `experiments/burnside/b25_kbmag/b25_mix.py`
- Server run command: `nohup python3 b25_mix.py --threshold 20000 --batch-frac 0.001 --periodic 600` (inferred from log header)
- v2 runner: `experiments/burnside/b25_kbmag/b25_mix_v2.py`
- Provenance triple: git SHA unknown (reconstruction limitation), kbprog binary from `kbmag_v1/` build

## Results — Baseline

No surviving result file. Outcome: monotonic rule growth in EXPLORATION phase, no confluence observed.

## Results — Mixed (v1 server run, b25_scoring.log)

Key observations from surviving log:
- First injection at t≈4s: RPO had 22,859 rules; injected 22 rules from 98,275 shortlex rules
- Second injection at t≈606s: RPO at 922,466 rules; injected 922 rules from 1,681,956 shortlex rules. Scoring took 40.3s (27.4s index build)
- Third injection at t≈1,916s: RPO at 1,319,306 rules; injected 1,319 rules from 2,350,127 shortlex rules. Index: 22.5M prefixes, 18.3M suffixes (42.2s)
- Phase throughout: EXPLORATION (never left); net growth rate stayed +0.2–1.3%
- RPO at 1,805s: 1,579,415 rules; shortlex: 2,797,018 rules
- Rule growth rate declining gently (net EMA falling from +1.3% to +0.2%) but no cascade

## Statistical analysis

Only one run surviving. No statistical test applicable. Observation: injections did not trigger a phase change in either agent.

## Validation

None. Neither agent reached confluence. Rule banks (surviving in `runs/b25/20260320_*`) are valid as reduction tools but cannot be validated against a known B(2,5) word problem answer.

## Final verdict

**`#status/inconclusive`**

### Why

Both RPO and shortlex agents remained in pure EXPLORATION phase for the full observed duration (~30min logged). Injections did not trigger a cascade. This is consistent with B(2,5) being structurally harder than B(4,3): the rule bank never reached a critical density for cascade onset. The v2 improvement (15x more frequent injection, 10x lower memory) may enable longer runs and more injections before a cascade could occur — but the fundamental question of whether any cascade is possible within feasible time remains open.

### What I'd do next

- Run v2 (b25_mix_v2.py) for 60h+ on the server to check whether cascade onset occurs at larger rule counts
- Investigate whether there is a natural "cascade threshold" for B(2,5) analogous to B(4,3)'s ~21k-rule cascade
- Route to Researcher: is there theory predicting whether KB cascade can occur for B(2,5) under RPO?

### Lead notified

- Date: unknown — reconstruction limitation

---

## Literature

- [[havas-wall-wamsley-1974]] — provides the B(2,5) presentation (59 equations) used as KB input; the generator convention from this paper determines which rules are "shortlex-small" vs. "RPO-large" in the overlap-scoring scheme.
- [[havas-newman-1980]] — survey contextualizing the B(2,5) KB program historically; the p-quotient algorithm that generated our presentation is part of the same computational tradition, and the 1977 observation that "the basic approach is to apply several different techniques" anticipates the mixing strategy directly.
- [[havas-robertson]] — KB completion framework (§2.9); the overlap-scored injection strategy operates within this framework by steering which critical pairs the RPO agent resolves first.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: whether any KB mixing can trigger a cascade on B(2,5) is an open engineering question connected to the open math problem.
- [[problems-people]] — names "Various Knuth-Bendix algorithms" (Nikolaev, Berger, Kalika, Lee) as one of the listed B(2,5) algorithm approaches in the algo_mixing project, establishing KBMag mixing as part of the original project scope.
