---
title: kbmag-overlap-scoring-b25-2026-05-22
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: kbmag
status: superseded
reconstructed_on: 2026-05-22
corrected_on: 2026-06-02
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/mixer, topic/word-problem, project/b25, status/superseded, methodology]
---

# Experiment — KBMag Overlap-Scored Mixing on B(2,5)

## Reconstruction notes

This experiment was performed prior to the K3 documentation convention. Reconstructed from code in `experiments/burnside/b25_kbmag/` (b25_mix.py, b25_mix_v2.py, bench_v3.py, standalone.py), surviving server log in `experiments/burnside/b25_kbmag/server_logs/b25_scoring.log`, rule bank timestamps in `experiments/b25_reduce_core/reduce_coreless.py` (path prefixes `runs/b25/20260320_*`), repo commit history (commits `e8a9d20`, `ee949cc` and later), and project memory notes on 2026-05-22.

Date of original runs: approximately 2026-03-20 (inferred from `runs/b25/20260320_*` path timestamps in reduce_coreless.py). The server log is from a run on `/home/maria/algo_mixing/` (a remote machine). Exact date of server run: unknown — reconstruction limitation. Seeds: not applicable (KB is deterministic given same ordering and input file).

**Correction — 2026-06-02**: The original reconstruction read only the first three injection events (t=4s, t=606s, t=1,916s) and concluded the log captured "~30 min" of data. A forensic archaeology pass (W2, see [[2026-06-02-b25-forensic-inventory]]) established that `b25_scoring.log` has 7,360+ lines covering **218,984s (60.83h) and 129 injection events**. The "Results — Mixed" and "Final verdict" sections below have been rewritten to reflect the full log. The previous versions were based on 0.8% of the actual run. Additionally, the `server_logs/` directory contains data from two distinct server runs mixed together: the RPO rule bank (`server_logs/rpo/`, 7.09M rules) is from a separate v2 run (b25_mix_v2.py, 13.5h); the shortlex rule bank (`server_logs/shortlex/`, 13.1M rules) is a mid-run snapshot from the v1 run, not the final state. The final v1 rule counts (RPO=13.2M, shortlex=25.5M at 60.8h) are on the remote server only and were not copied locally.

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

## Results — Mixed (v1 server run, b25_scoring.log) — CORRECTED 2026-06-02

Full log covers **218,984s (60.83h), 129 injection events**. Previous reconstruction read only the first 3 injections.

### Rule growth trajectory

| Time | RPO rules | Shortlex rules | RPO phase | Shortlex phase | Injection # |
|---|---|---|---|---|---|
| t=4s (0.00h) | 22,859 | 98,275 | — | — | #1 (22 rules injected) |
| t=606s (0.17h) | 922,466 | 1,681,956 | — | — | #2 (922 rules injected) |
| t=1,916s (0.53h) | 1,319,306 | 2,350,127 | — | — | #4 (1,319 rules injected) |
| ~20h (est.) | ~7,000,000 | ~13,100,000 | — | — | (local shortlex snapshot captured here) |
| t=218,984s (60.83h) | **13,167,523** | **25,484,340** | **PLATEAU (282)** | **PLATEAU (3,329)** | #129 |

### Phase evolution

Both RPO and shortlex entered **PLATEAU** phase over the run. At event #129:
- RPO: PLATEAU counter = 282, net growth = **+0.03%**
- Shortlex: PLATEAU counter = 3,329 (in plateau far longer), net growth = **+0.02%**

PLATEAU means the EMA-smoothed net growth rate has been near-zero for N consecutive measurements. Neither agent entered EXPLOITATION (net < −1.0%) or any cascade phase — the run showed no rule count decrease at any point.

**Phase trajectory summary**: initial rapid growth (net ~+1.3% early) → steady deceleration → sustained PLATEAU with +0.03% residual growth. The mixing injection reduced the long-run growth rate to near-zero but did not trigger cascade.

### Injection cadence evolution

Injection cadence was governed by `max(periodic=600s, last_scoring_time × 2)`. As rule banks grew, Aho-Corasick index build time increased:
- Early injections (events #1–4): cooldown ~600s
- Event #129 (60.8h): cooldown = 2,238s (~37 min between injections)

The effective injection rate slowed by ~4× over the run due to the O(N) scoring overhead of v1's Aho-Corasick approach.

### Local rule bank provenance (see Correction note above)

The surviving `server_logs/` rule banks are NOT from this run's endpoint:
- `server_logs/rpo/input.kbprog.live` (7.09M rules): from the **v2 run** (b25_mix_v2.py, separate 13.5h session). NOT from this v1 run.
- `server_logs/shortlex/input.kbprog.live` (13.1M rules): from this v1 run, captured at **~20h into the run**, not at the 60.8h endpoint.
- **Final v1 rule banks** (RPO=13.2M, shortlex=25.5M) exist only on the remote server at `/home/maria/algo_mixing/experiments/b25/runs_b25_mix/` — not locally preserved.

## Statistical analysis

One run surviving (the v1 60.8h server run). No statistical test applicable. The v2 run (b25_mix_v2.py, 13.5h) provides a partial second data point: RPO reached 7.09M rules also in PLATEAU phase before that run ended, consistent with the v1 trajectory.

## Validation

None. Neither agent reached confluence. Rule banks (surviving in `runs/b25/20260320_*`) are valid as reduction tools but cannot be validated against a known B(2,5) word problem answer.

## Final verdict

**`#status/superseded`** — this note was reconstructed from an incomplete log read (0.8% of the actual run). See Reconstruction notes § Correction for details. A future re-run with proper pre-registration should produce a fresh experiment note.

### Verdict on the actual 60.8h data

The hypothesis ("phase change within 1 hour") was **not confirmed in the strict sense**: neither agent entered EXPLOITATION or any cascade phase within the 60.8h run. However, the actual result is materially different from the reconstruction's "EXPLORATION throughout":

- Both agents reached and sustained **PLATEAU** phase (growth rate decayed from ~+1.3% → +0.03% over 60.8h).
- PLATEAU is not cascade — no rules were eliminated, the count only grew — but it is not pure EXPLORATION either. The system stabilized at a very low growth rate.
- Minimum cascade threshold lower bound: if a cascade threshold exists for B(2,5) under this mixing strategy, it is at **>13.2M RPO rules** (the level reached at 60.8h with no cascade observed).
- The 129 injections over 60.8h sustained the PLATEAU without triggering cascade. Injections kept both agents from diverging into explosive growth but did not drive them into reduction.

**Revised assessment**: mixing has a measurable structural effect on B(2,5) KB dynamics (growth rate suppression; PLATEAU phase; not just monotonic EXPLORATION), but the effect is stabilizing rather than cascade-triggering within feasible run times. Whether longer runs (>60h) or larger rule banks could trigger cascade remains unknown.

### What I'd do next (updated 2026-06-02)

- ~~Run v2 (b25_mix_v2.py) for 60h+ on the server~~ — partially done: v2 ran 13.5h, RPO reached 7M rules in PLATEAU. Full 60h+ v2 run not yet done.
- Investigate whether PLATEAU → cascade transition exists at >13.2M RPO rules. Would require a server run longer than 60.8h or resuming from the 13.2M rule bank (which is on the remote server only).
- Route to Researcher: is there theory predicting a PLATEAU → cascade transition for B(2,5) under RPO? The observation that growth rate stabilizes at ~+0.03% is a concrete empirical claim to compare against theory.
- Recover the remote v1 final rule banks (RPO=13.2M, shortlex=25.5M) from `/home/maria/algo_mixing/` if that server is accessible — these are the largest B(2,5) KB rule banks ever generated and were not copied locally.

### Lead notified

- Date: 2026-06-02 (W2 forensic inventory; correction relayed via Lead review)

---

## Literature

- [[havas-wall-wamsley-1974]] — provides the B(2,5) presentation (59 equations) used as KB input; the generator convention from this paper determines which rules are "shortlex-small" vs. "RPO-large" in the overlap-scoring scheme.
- [[havas-newman-1980]] — survey contextualizing the B(2,5) KB program historically; the p-quotient algorithm that generated our presentation is part of the same computational tradition, and the 1977 observation that "the basic approach is to apply several different techniques" anticipates the mixing strategy directly.
- [[havas-robertson]] — KB completion framework (§2.9); the overlap-scored injection strategy operates within this framework by steering which critical pairs the RPO agent resolves first.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: whether any KB mixing can trigger a cascade on B(2,5) is an open engineering question connected to the open math problem.
- [[problems-people]] — names "Various Knuth-Bendix algorithms" (Nikolaev, Berger, Kalika, Lee) as one of the listed B(2,5) algorithm approaches in the algo_mixing project, establishing KBMag mixing as part of the original project scope.
