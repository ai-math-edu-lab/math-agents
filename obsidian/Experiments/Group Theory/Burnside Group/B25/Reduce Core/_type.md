---
title: Reduce Core on B(2,5)
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: reduce-core
status: inconclusive
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, project/b25, status/inconclusive, experiment-type]
---

# Experiment Type — Reduce Core on B(2,5)

## What this technique is

A multi-stage word reduction pipeline for B(2,5) commutator words. The goal is NOT to prove words equal to the identity, but to find the *shortest word* in the same coset — i.e., a word that equals the original in B(2,5) but is as short as possible. This is meaningful progress even without proving identity: shorter words are easier to further reduce, and extreme length reduction could eventually reach the identity.

The pipeline exploits:
1. **Lifting (optional)**: the core X = `ABabAbabABaBAbabABABabAbaBABaBAbabb` (35 chars) appears repeatedly in B(2,5) commutator words. Substituting `m = X⁻¹bX` compresses the word dramatically (comm_12_9: 28,652 → 544 chars), changing the alphabet from {a,b} to {a,b,m}.
2. **Power reduction**: replace `aaaaa→ε`, `aaaa→A`, `aaa→AA` etc. (B(2,5) has exponent 5, so w^5=1).
3. **Braid reduction** (FIXED, see below): detect alternating runs `(gh)^k` and replace with `(gh)^{k mod 5}`. This exploits the braid-like structure of B(2,5) relations.
4. **Rule bank application**: greedily apply rewriting rules from accumulated KB runs. Rule banks from ≥12 separate `kbprog` runs (shortlex + RPO + wtlex orderings) are merged into a master bank of ~25.7M rules.
5. **Rust beam search**: bounded-width beam using forward (shrinking) and inverse (expanding) rules + braid moves, run from `experiments/burnside_bidirectional/target/release/braid_reduce`.
6. **Biased KB generation**: run `kbprog` seeded with a specific target word (core_a, core_b, word_544, word_coreless) to generate rule banks specialized for that word's structure, then re-apply the pipeline.

### The braid_reduce_fast bug (critical)

The Python `braid_reduce_fast` function in all pre-correction scripts had a sign error for the non-abelian inverse case. For `(gh)^k mod 5`, the replacement was computed as `(G+H)*k_mod` (where G=g⁻¹, H=h⁻¹), but the correct inverse is `(gh)⁻¹ = h⁻¹g⁻¹ = HG`, not `GH`. This is a non-abelian error: B(2,5) is non-abelian, so `GH ≠ HG`.

Effect: each wrong application shifts abelianization by (3,3) mod 5. Words produced by the buggy pipeline have abelianization ≠ (0,0) mod 5 and do NOT represent the same group element as the original commutator.

The bug affected 6 Python files (all fixed in the corrected pipeline). The Rust `braid_reduce` binary was always correct. See `experiments/b25_reduce_core/corrected/README.md` for the full analysis.

## Why we ran this

Proving comm_12_9 = identity in B(2,5) is the primary B(2,5) goal. The current KB and bidirectional approaches cannot do it directly: the rule banks are too small and the word is too long. By first reducing the word's length as far as possible, we shorten the gap. This experiment measures how far greedy rule application + braid + beam can reduce B(2,5) commutator words given a large (25.7M rule) bank.

## What "success" means

Progressive: any length reduction is progress. The current record is 7,245 chars for comm_12_9 (74.7% reduction from 28,652). The ultimate goal is reducing to the empty string (proving identity).

## Results

**`comm_12_9: 28,652 → 7,245 chars (74.7%), 119/119 reduced`**

Run `b25-reduce-core-benchmark-0001` (4-pass Rust beam, `braid_reduce` binary, `mega_ab_rules.live` ~25.7M rules, beam-width 16384, beam-secs 300/pass):

![[b25-benchmark-snapshot-2026-06-09#Snapshot stats]]

Full 119-row table: [[b25-benchmark-snapshot-2026-06-09#Complete 119-row results table|→ complete 119-row table]]

**Provenance gap disclosure (42/119 rows)**: For 42 targets, `ui/benchmarks_data.json` holds a better all-time best from prior runs. Methodology now identified for all 42 via JSON `comment` field — Cat A (8): Python power+braid+greedy, no beam; Cat B (30): Rust beam + 7M historical rules, run directory gone from disk; Cat C (3): `reduce_benchmark_v2.py` lift-first; Cat D (1): biased 25M rules, comm_16_2 only. The Cat B run and its outputs are unrecoverable from disk. See [[b25-benchmark-snapshot-2026-06-09#Provenance gap NOT closed for 42 rows|→ 42-row gap table]].

---

## Relevant scripts

- `experiments/b25_reduce_core/script/reduce_coreless.py` — main pipeline (FIXED braid)
- `experiments/b25_reduce_core/script/verify_reduction.py` — verification tool (FIXED)
- `experiments/b25_reduce_core/script/reduce_benchmark_v2.py` — lift-first benchmark over 119 words (Cat C source)
- `experiments/b25_reduce_core/script/overnight_4pass_smallfirst.sh` — 4-pass overnight beam script (benchmark-0001 source)
- `experiments/b25_reduce_core/script/collect_best.sh` — post-run collector; reads `benchmark_run/overnight_results/`, updates `ui/benchmarks_data.json`
- `experiments/burnside/b25_bias_bidir/script/` — biased KB generation + reduction

## Literature

- [[havas-wall-wamsley-1974]] — provides the B(2,5) presentation (59 equations, generators 1–34) that the reduction pipeline operates on; source of target-word naming (generator 9 = weight-5 commutator, generator 12 = weight-6 commutator → `comm_12_9`).
- [[havas-robertson]] — KB completion (§2.9) and Tietze transformation (§2.3): the technique classes that the rule-bank application and pipeline stages instantiate; specifically notes KB sometimes outperforms coset enumeration for the kind of large-word problems we face.
- [[kourovka-11.48-kostrikin-1990]] — theoretical motivation: identity certificates produced by the reduce-core pipeline (the 7,245-char reduced form of comm_12_9) are evidence about the restricted B(2,5) word problem, whose structure connects to the open question of whether B(2,5) is infinite.
