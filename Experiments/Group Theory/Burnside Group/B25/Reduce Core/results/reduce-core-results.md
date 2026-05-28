---
title: Reduce Core B(2,5) Results
domain: group-theory
project: b25
experiment_type: reduce-core
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, project/b25, status/inconclusive, results]
---

# Reduce Core B(2,5) Results

## Results table — comm_12_9 pipeline

| Run ID | Date | Parameters | Outcome | Wall-clock | Memory peak | Validated by | Notes |
|--------|------|------------|---------|------------|-------------|--------------|-------|
| v1-buggy | ~2026-04-02 | Python pipeline, buggy braid_reduce_fast | 28,652 → 3,707 chars; **INVALID** (abelianization (4,4)) | unknown | unknown | FAILED (self-certified by buggy verify_reduction.py) | Do not use. Chain: 28652→544→15328→10624→8402→4882→3732→3707 (WRONG) |
| v2-corrected | ~2026-05-22 | Python pipeline, FIXED braid_reduce_fast | 28,652 → 7,245 chars; abelianization (0,0) ✓ | unknown | unknown | Abelianization check at each stage | Chain in corrected/README.md. Current best. GAP/Sage verification: open |
| benchmark-v2 | ongoing | lift-first, 25.7M rule bank, 119 words | In progress — best_words/ contains current bests | unknown | unknown | Abelianization check | Benchmark over comm_4_2 to comm_32_2; biased rules pending restart from valid targets |

## Results table — biased KB runs

| Run ID | Date | Parameters | Outcome | Wall-clock | Memory peak | Validated by | Notes |
|--------|------|------------|---------|------------|-------------|--------------|-------|
| biased-word3705 | ~2026-04-02 | kbprog biased on word_3705 (INVALID target) | Rule banks in `b25_bias_bidir/rules/3705_run4_*` etc. — **built on invalid target** | unknown | unknown | none | word_3705 derives from buggy word_3707. Any rules tuned to it are suspect. |
| biased-weq-sl | ~2026-04-02 | word-equality shortlex constraint | Rule banks in `b25_bias_bidir/rules/weq_sl/` — validity unclear (may be built on invalid target) | unknown | unknown | none | Reconstruction limitation: run parameters unknown |
| biased-weq-rpo | ~2026-04-02 | word-equality RPO constraint | Rule banks in `b25_bias_bidir/rules/weq_rpo/` — validity unclear | unknown | unknown | none | |

## Version history

**v1 (BUGGY, pre-2026-05-22)**: Python `braid_reduce_fast` had non-abelian inverse error. Produced word_4882 → word_3732 → word_3707 chain. All output words have abelianization (4,4) mod 5; they are NOT equal to `[c12,c9]`. Bug undetected because `verify_reduction.py` had the identical error.

**v2 (CORRECTED, from 2026-05-22)**: Fixed braid implementation. All 6 affected Python files patched. Corrected chain produces 7,245-char word with abelianization (0,0) at every stage. Documented in `experiments/b25_reduce_core/corrected/README.md`.

**Lift-first benchmark (v2, ongoing)**: `reduce_benchmark_v2.py` runs lift→braid→rule-bank→beam on all 119 words. X-core (35 chars) substitution compresses many words significantly before rule application.

## Main findings

- The pipeline achieves **74.7% length reduction** of comm_12_9 (28,652 → 7,245 chars), all-abelianization-preserving, using only KB rules + braid moves + beam search.
- The braid_reduce_fast bug contaminated all results prior to 2026-05-22. The buggy "3,707-char record" is a word from a different coset. Any experiment building on word_3705, word_3707, or word_4882 must restart from the 7,245-char corrected form.
- The X-core compression (m = X⁻¹bX) compresses comm_12_9 from 28,652 to 544 chars — a 98% compression ratio — at the cost of introducing a new generator m. The resulting {a,b,m} word may be reducible by specialized KB rules that the pure {a,b} bank does not contain.
- The 25.7M rule bank plateaus at 7,245 chars for comm_12_9. Further reduction requires either: larger rule banks (longer KB runs), beam search with more time/width, or new structural insight.

## Open questions

- Can the corrected pipeline reduce comm_12_9 below 7,245 with a larger rule bank or wider beam?
- Do biased KB runs (seeded on 7,245-char word) generate rule banks that improve on the current best?
- Can the same X-core compression generalize to other benchmark words? (Known: it works for comm_13_10.)
- Validator claim: does `corrected/final_beam.txt` represent the same B(2,5) element as `[c12,c9]`?

## Related material

- [[Reduce Core/_type|Reduce Core on B(2,5)]] — parent experiment-type description; includes the critical braid_reduce_fast bug analysis and corrected pipeline stages
- [[_progress|B(2,5) Progress Note]] — umbrella standing progress note; 7,245-char corrected result and the invalidated 3,707 record are both tracked here
- [[reduce-core-data]] — sibling data note: target words, rule bank paths, corrected output artifacts, X core constant
- [[reduce-core-pipeline-b25-2026-05-22]] — methodology note; contains the full corrected reduction chain, validator verdict, and annotated provenance triple
- [[kbmag-tools-overview]] — KBMAG tool reference; `kbprog` generates the 25.7M rule bank that the pipeline applies in the greedy sweep stage
- [[havas-wall-wamsley-1974]] — defines comm_12_9 = [c12, c9] via the generator numbering (generators 1–34); the 59 relators from this presentation are the KB input
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: the 7,245-char corrected reduction is evidence about the B(2,5) word problem connected to open problem 11.48
