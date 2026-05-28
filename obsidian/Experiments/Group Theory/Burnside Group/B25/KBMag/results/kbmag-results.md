---
title: KBMag B(2,5) Results
domain: group-theory
project: b25
experiment_type: kbmag
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/mixer, project/b25, status/inconclusive, results]
---

# KBMag B(2,5) Results

## Results table

| Run ID | Date | Parameters | Outcome | Wall-clock | Memory peak | Validated by | Notes |
|--------|------|------------|---------|------------|-------------|--------------|-------|
| v1-baseline | ~2026-03-20 | RPO only (`--baseline`) | EXPLORATION phase throughout; no cascade observed | unknown | unknown | none | Reconstruction: no surviving log; RPO alone expected to diverge |
| v1-mixed-server | ~2026-03-20 | threshold=20k, batch_frac=0.001, periodic=600s, sample_mult=20 | EXPLORATION throughout; RPO reached ~1.6M rules at 0.5h; 3 injections (22 + 922 + 1319 rules); no phase change | >1,900s (log cut off) | unknown | none | Surviving log: `server_logs/b25_scoring.log`. Run on remote `/home/maria/` |
| v2-bench | ~2026-03-20 | Same strategy, bisect+cached-prep instead of Aho-Corasick | Equivalent results; 15x more frequent injection; ~10x memory reduction | unknown | 3–5 GB (vs 40–50 GB for v1) | none | bench_v3.py ran at synthetic 13M RPO / 25M slex scale; not a full B(2,5) run |
| v1-mixed-overnight | unknown | unlimited timeout; other params default | Unknown — reconstruction limitation | unknown | unknown | none | Long-running server run implied by v2 development motivation |

## Version history

**v1** (b25_mix.py): Direct port of the B(4,3) mixing strategy to B(2,5). Aho-Corasick prefix/suffix index for overlap scoring. At 13M rules, index build takes 655s and prep takes 449s — injection cadence ~1,100s, too slow for meaningful periodic re-injection.

**v2** (b25_mix_v2.py): Replaced Aho-Corasick with sorted-array bisect index and incremental ("cached") shortlex preparation. Index build: 20s vs 655s. Prep: 20s after warmup vs 449s. Injection cadence: ~65s vs ~1,100s. Memory: 3–5 GB vs 40–50 GB. Results identical (same top-K rules selected). This makes sustained long runs feasible.

**bench_v3.py**: Synthetic benchmark comparing v1 vs v2 at realistic B(2,5) 60h scale (13M RPO rules, 25M shortlex rules, avg LHS ~90 chars). No actual B(2,5) groups run.

## Main findings

- The B(4,3) mixing parameters (threshold=20k, batch_frac=0.001) transferred directly to B(2,5), but produced no phase change. Both RPO and shortlex agents stayed in EXPLORATION throughout the observed 30-minute window.
- RPO growth rate: +1.3% → +0.2% (declining gently with time, not cascading).
- Injected rules (22, 922, 1,319) represent 0.001% of RPO rules each time — much smaller relative impact than the 80-rule B(4,3) cascade trigger.
- The v2 memory improvement is the key enabler for long runs: 10h+ runs are now feasible without running out of memory.

## Open questions

- Is there a cascade threshold for B(2,5) at all? At what rule count might cascade begin?
- Does more frequent injection (v2 cadence, 15x) change outcomes over 10h+ runs?
- Route to Researcher: is there theory (e.g., termination criteria for KB on finite Burnside groups) predicting whether RPO can cascade for B(2,5)?

## Related material

- [[KBMag/_type|KBMag on B(2,5)]] — parent experiment-type description; includes the theoretical motivation for mixing RPO and shortlex on B(2,5)
- [[_progress|B(2,5) Progress Note]] — umbrella standing progress note; KBMag outcome summarised in the "What's been tried" table
- [[kbmag-data]] — sibling data note: input presentation, script paths, surviving run log references
- [[kbmag-overlap-scoring-b25-2026-05-22]] — methodology note for these runs; contains full scheduler config, batch-frac parameters, and the surviving server log analysis
- [[kbmag-tools-overview]] — KBMAG tool reference; describes the EXPLORATION/EXPLOITATION phase detection used in these result rows
- [[havas-wall-wamsley-1974]] — provides the B(2,5) presentation (59 equations) used as KB input; the generator ordering determines which rules are "shortlex-small" vs "RPO-large"
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: whether any cascade is possible on B(2,5) under RPO connects to the open question this problem 11.48 poses
