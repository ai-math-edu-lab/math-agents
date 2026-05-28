---
title: reduce-core-pipeline-b25-2026-05-22
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: reduce-core
status: conjectured
reconstructed_on: 2026-05-22
validator_verdict: conjectured
validator_verdict_date: 2026-05-22
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, project/b25, status/conjectured, methodology]
---

# Experiment — Reduce Core Pipeline on B(2,5)

## Reconstruction notes

This experiment was performed prior to the K3 documentation convention. Reconstructed from code in `experiments/b25_reduce_core/` (reduce_coreless.py, verify_reduction.py, benchmark_run/, corrected/README.md), `experiments/burnside/b25_bias_bidir/` (README.md, scripts/, targets/), project memory notes, and repo commit history on 2026-05-22. The corrected/ subfolder contains the definitive output record for comm_12_9. Biased KB runs in b25_bias_bidir have surviving targets and rules but no dated run logs. Seeds: not applicable (greedy pipeline is deterministic; beam search seeds unknown — reconstruction limitation).

## Hypothesis

Applying the multi-stage reduction pipeline (power reduction → fixed braid reduction → rule bank application → Rust beam search) to comm_12_9 will reduce its length below 8,000 characters while preserving abelianization (0,0) mod 5. The corrected pipeline achieves this: 28,652 → 7,245 chars (74.7% reduction).

## Problem set

- Group: B(2,5)
- Primary target: `comm_12_9` = `[c12, c9]` where `c_k = [[a,b], a^{k-1} b a^{-(k-1)}]` (weight-12 and weight-9 commutators). Original length: 28,652 chars in {a,b,A,B}.
- Benchmark: 119 commutator words `comm_{n}_{k}` for various n, k. Located in `benchmark_run/words/`.
- Range spans from `comm_4_2` (shallow) to `comm_32_2` (deep).

## Mixer agents involved

The pipeline does not use a mixer in the KB sense — it applies already-accumulated rules greedily.

- Python pipeline (`reduce_coreless.py`): free reduction → power reduction → **fixed** braid reduction → greedy rule-bank sweep
- Rule banks: 17 `.live` files from separate `kbprog` runs (3 shortlex + RPO + wtlex orderings, multiple sessions in March 2026):
  - `runs/b25/20260320_054109/kb_{shortlex,wtlex,rpo}/input.kbprog.live`
  - `runs/b25/20260320_054957/kb_{shortlex,wtlex,rpo}/input.kbprog.live`
  - `runs/b25/20260320_055128/kb_{shortlex,wtlex,rpo}/input.kbprog.live`
  - `runs/b25/20260320_055557/kb_shortlex/input.kbprog.live`
  - `runs/b25/20260320_065252/kb_shortlex/input.kbprog.live`
  - `runs/b25/20260320_065653/kb_shortlex/input.kbprog.live`
  - Biased runs: `experiments/b25_reduce_core/runs/{rpo_core_a,sl_boundary,sl_core_a,sl_core_a_plus_a,sl_prefix}/input.kbprog.live`
  - Merged: `benchmark_run/rule_banks/mega_ab_rules.live` (25.7M rules)
- Rust beam search: `experiments/burnside_bidirectional/target/release/braid_reduce` (correct braid implementation)
- Benchmark runner: `benchmark_run/reduce_benchmark_v2.py` (lift-first strategy)

## The critical bug and its fix (braid_reduce_fast)

**Bug (pre-correction)**: In `braid_reduce_fast`, the replacement for `(gh)^{k mod 5}` used `(G+H)*k_mod` where G=g⁻¹, H=h⁻¹. But `(gh)⁻¹ = h⁻¹g⁻¹ = HG`, not GH. This flips the order in a non-abelian group.

**Concrete example**: `babababababa = (ba)^6`. Correct: `(ba)^6 = (ba)^5 · ba = ba` (identity-expand, keep). Bug: emits `BA = (ba)^{-1}`. Each wrong application shifts abelianization by (3,3) mod 5.

**Detection**: abelianization (a-exp, b-exp) mod 5. A genuine reduction of `[c12,c9]` must have (0,0); the buggy chain produced (4,4).

**Why undetected**: `GH` and `HG` have identical *commutative* exponents, so an abelianization check passes after any single application. The divergence accumulated over multiple applications. `verify_reduction.py` had the identical bug, so it self-certified the error.

**Files fixed** (6 total): `experiments/b25_reduce_core/reduce_coreless.py`, `verify_reduction.py`, `runs_4882/beam_4882.py`, `experiments/burnside/b25_bias_bidir/scripts/{reduce_coreless,verify_reduction,beam_4882}.py`.

**Invalidated artifacts**: word_4882, word_3732, word_3707, all rule banks keyed to these words, `ui/comm_12_9_reduced_data.json#final_word`, all beam/bidir results derived from the buggy chain. See `experiments/b25_reduce_core/corrected/README.md`.

## Scheduler config

Not applicable (pipeline, not scheduler-driven). The benchmark script `reduce_benchmark_v2.py` runs the pipeline sequentially on all 119 words.

Lift-first strategy (v2 benchmark):
1. Python: free + power + fixed braid
2. Lift: `X⁻¹bX → m`, `X⁻¹BX → M` (X = `ABabAbabABaBAbabABABabAbaBABaBAbabb`, 35 chars)
3. Rust braid_reduce on lifted form using `b25_lifted` rule bank
4. Expand: `m → X⁻¹bX`, free reduce
5. Rust braid_reduce with master rules
6. Record shortest of lifted vs {a,b} forms

## Termination criteria

- Greedy phase: no rule applies (fixed point)
- Beam search: beam_time_budget_secs or beam_max_steps exhausted (params from Rust config)
- Benchmark: run on all 119 words, keep best per word in `benchmark_run/best_words/`

## Baselines

- No baseline without braid reduction (braid reduction is always applied first)
- Pre-fix "baseline" (v1 buggy): see Invalidated artifacts above — not a valid comparison

## Seeds

- Greedy pipeline: fully deterministic, no seeds
- Beam search seeds: unknown — reconstruction limitation

## Metric

- Length of reduced word (chars in {a,b,A,B})
- Abelianization invariant (a-exp, b-exp) mod 5 must be (0,0) for reductions of `[c12,c9]`
- Secondary: fraction of 119 benchmark words improved vs their initial KB-reduced length

## Anti-pattern check

- Biased KB runs were seeded on specific target words (word_3705 etc.) and then the SAME words were scored against those rule banks. This is tuning on the test target — per [[_type.md]], cherry-picking on a single word is not progress unless it also generalizes. The benchmark run (119 words, unbiased) partially addresses this.
- Note: word_3705 is **INVALID** (derived from buggy chain). Any biased-KB rules tuned on word_3705 scored against word_3705 represent work on the wrong group element.

## Setup

- Runner: `experiments/b25_reduce_core/reduce_coreless.py` (main pipeline)
- Benchmark: `experiments/b25_reduce_core/benchmark_run/reduce_benchmark_v2.py`
- Command: `python3 reduce_benchmark_v2.py` from b25_reduce_core directory
- Provenance triple: git SHA unknown (reconstruction limitation). Two-stage provenance: (a) Rust `braid_reduce` binary at `experiments/burnside_bidirectional/target/release/braid_reduce`, invoked via `subprocess.run` by `reduce_benchmark_v2.py:91, 108`. (b) Pre-built `.live` rule banks loaded by the benchmark (`/tmp/b25_master_rules.live` and `experiments/b25_lifted_kb/filtered_rules.live`, per `reduce_benchmark_v2.py:31-32`); these were generated upstream by `kbprog` runs whose outputs live in `runs/b25/20260320_{054109,054957,055128,055557,065252,065653}/` and `runs/b25/20260328_143533/`, each with `kb_rpo/`, `kb_shortlex/`, `kb_wtlex/` subdirectories containing `input` and `input.kbprog.live`. The biased-KB phase that produced some of these calls `kbmag_source/standalone/bin/kbprog` per `experiments/b25_reduce_core/run_biased_agents.sh:6-7`. Which kbprog build produced the unbiased orderings (kb_rpo / kb_shortlex / kb_wtlex) is not determined — reconstruction limitation.

## Results — comm_12_9 corrected reduction chain

| Stage | Length | Abel (a,b) | (mod 5) | Note |
|-------|-------:|------------|---------|------|
| Original `[c12, c9]` | 28,652 | (0, 0) | (0,0) ✓ | |
| Lifted to {a,b,m} | 544 | (0, 0) | (0,0) ✓ | m = X⁻¹bX |
| Coreless {a,b} | 15,328 | (9600, 5280) | (0,0) ✓ | X substitution expanded |
| After power reduction | 10,624 | (960, 4800) | (0,0) ✓ | aaaaa→ε etc. |
| After fixed braid | 8,402 | (5, 1925) | (0,0) ✓ | braid_reduce_fast FIXED |
| After Python KB rules | 8,394 | (5, 1925) | (0,0) ✓ | greedy rule-bank sweep |
| After Rust braid_reduce | 8,388 | (5, 1915) | (0,0) ✓ | Rust binary (always correct) |
| **After Rust beam search** | **7,245** | **(5, 0)** | **(0,0) ✓** | **CURRENT BEST** |

Source: `experiments/b25_reduce_core/corrected/README.md`

## Results — Buggy chain (INVALIDATED — do not use)

| Stage (BUGGY) | Length | Abel (mod 5) | Status |
|---------------|-------:|--------------|--------|
| result_coreless_reduced.txt | 4,882 | (4,4) ✗ | INVALID |
| word_4882.txt | 4,882 | (4,4) ✗ | INVALID |
| word_3732.txt | 3,732 | (4,4) ✗ | INVALID |
| word_3707.txt | 3,707 | (4,4) ✗ | INVALID |

These words represent different group elements than `[c12,c9]`. Do not use for further reduction or as targets.

## Results — Benchmark (119 words, reconstruct status)

Best words per target are stored in `benchmark_run/best_words/`. Benchmark covers words from `comm_4_2` to `comm_32_2`. Current best forms use the lift-first v2 pipeline with 25.7M merged rule bank.

Detailed per-word results: see `benchmark_run/best_words/` (surviving artifacts). No summary table reconstructable without running the benchmark — reconstruction limitation.

## Validation

- Abelianization check: abelianization (a-exp mod 5, b-exp mod 5) = (0,0) is a necessary condition (not sufficient) for all reductions. Tracked at each stage in the pipeline.
- Cross-verification: Validator returned `#status/conjectured` on 2026-05-22. See [[Architecture/Mixer/Documentation/Math Validation/2026-05-22-comm-12-9-7245-final]].
- The corrected chain has been manually verified to preserve abelianization at each stage. Sub-claim A (input is B(2,5) identity) verified; Sub-claim B (chain soundness) partially verified; Sub-claim C (element equality) not reachable — GAP kbmag does not complete KB on B(2,5).

## Final verdict

**`#status/conjectured`** (Validator final verdict — 2026-05-22)

### Why

Available evidence is consistent with the claim. Sub-claim A (input is identity in B(2,5)) verified by Havas relator byte match. Sub-claim B (chain soundness) partially verified: abelianization (0,0) preserved at all stages; KB rule m→m_pure supports the expansion step. Sub-claim C (element equality in B(2,5)) not reachable: GAP kbmag does not complete KB on B(2,5)'s full Havas presentation — a settled fact in the group theory literature. This is the tooling ceiling for any B(2,5) word equality claim, not specific to this word.

Remaining open items: (1) comm_12_9 = identity in B(2,5) is not proved; (2) benchmark over 119 words not run to completion with the corrected pipeline; (3) biased-KB work needs to restart from word_7245 (previous runs targeted invalid word_3707).

### What I'd do next

1. **HIGHEST**: Run biased kbprog on word_7245 (pipeline-verified target) to generate new specialized rule banks; then re-apply pipeline.
2. Run overnight benchmark with corrected pipeline on all 119 words; update best_words/.
3. Investigate whether the X-core compression generalizes: does comm_13_10 compress similarly?

### Math claim status

- CLAIM: the word at `experiments/b25_reduce_core/corrected/final_beam.txt` (7,245 chars) represents the same element of B(2,5) as `[c12, c9]`.
- **`#status/conjectured` — Validator final verdict, 2026-05-22.** See [[Architecture/Mixer/Documentation/Math Validation/2026-05-22-comm-12-9-7245-final]].

Verified by [[2026-05-22-comm-12-9-7245-final]]

### Lead notified

- Date: unknown — reconstruction limitation

---

## Literature

- [[havas-wall-wamsley-1974]] — source of the generator numbering convention: generator 9 = [2,1,2,1,1] (weight 5), generator 12 = [2,1,2,1,1,2] (weight 6), defining `comm_12_9 = [c₁₂, c₉]` as the primary target word; the 59 relators used by `kbprog` to build the rule banks come from this presentation.
- [[havas-robertson]] — KB completion as a computational tool for FPGs (§2.9); the greedy rule-bank sweep phase of this pipeline applies rules generated by kbprog following this methodological tradition.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: the 7,245-char reduced form of comm_12_9 and any identity certificate produced here are evidence about the restricted B(2,5) word problem, whose structure connects to the open question of whether B(2,5) is infinite.
