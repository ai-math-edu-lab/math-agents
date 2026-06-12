---
title: Biased KB Agents B(2,5) Results
domain: group-theory
project: b25
experiment_type: biased-kb-agents
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/word-problem, topic/proof-search, project/b25, status/inconclusive, results]
---

# Biased KB Agents B(2,5) Results

> **All runs in this table targeted INVALID words** (word_3705 or word_3707, both derived from the buggy `braid_reduce_fast` chain). Rule counts and bank sizes are reported for completeness and because the rules themselves are valid B(2,5) KB rules — but downstream reduction results built on these targets are not meaningful comparisons against the current best (word_7245). See [[biased-kb-agents-b25-2026-06-03]] § Invalidation.

## Results table — rule bank generation

| Run ID | Date | Ordering | sk | sp | Mode | Target | Rule count | Size | Wall-clock | Validated by | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| run4-sl-k12 | ~2026-04-06 | shortlex | 12 | ~0.5 | biased | word_3705 (INVALID) | 1,798,675 | 154MB | >6,758s (running at log cutoff) | none | Longest-running run4 agent; sp inferred |
| run4-sl-k16 | ~2026-04-06 | shortlex | 16 | ~0.5 | biased | word_3705 (INVALID) | 633,337 | 52MB | unknown | none | Fewer rules at higher sk — expected |
| run4-sl-k20 | ~2026-04-06 | shortlex | 20 | ~0.5 | biased | word_3705 (INVALID) | 434,633 | 32MB | unknown | none | |
| run4-rpo-k14 | ~2026-04-06 | RPO | 14 | ~0.5 | biased | word_3705 (INVALID) | 1,113,892 | 93MB | unknown | none | |
| run4-rpo-k20 | ~2026-04-06 | RPO | 20 | ~0.5 | biased | word_3705 (INVALID) | 417,447 | 32MB | unknown | none | |
| run4-wt-k16 | ~2026-04-06 | wtlex | 16 | ~0.5 | biased | word_3705 (INVALID) | 673,675 | 66MB | unknown | none | `.tmp` file present — may have been running |
| run5-sl-k0-sp50 | ~2026-04-07 | shortlex | 0 | 0.50 | biased | word_3705 (INVALID) | 1,352,697 | 118MB | unknown | none | sk=0 = random substring sampling |
| run5-sl-k3-sp99 | ~2026-04-07 | shortlex | 3 | 0.99 | biased | word_3705 (INVALID) | 2,317,435 | 133MB | unknown | none | `.tmp` file present |
| run5-sl-k4-sp95 | ~2026-04-07 | shortlex | 4 | 0.95 | biased | word_3705 (INVALID) | 2,282,905 | 133MB | unknown | none | |
| run5-weq-cn100k | ~2026-04-07 | shortlex | 6 | ~1.0 | word-equality | word_3705 (INVALID) | 3,220,901 | 212MB | >21,685s | none | 99.9% special eqns; largest bank |
| weq-rpo | ~2026-04-06 | RPO | 6 | 0.70 | word-equality | word_3707 (INVALID) | 893,692 | 52MB | ~518s (interrupt) | none | Killed by interrupt signal |
| weq-sl | ~2026-04-06 | shortlex | 6 | 0.70 | word-equality | word_3707 (INVALID) | 974,337 | 57MB | unknown | none | `.tmp` file present |

## Version history

**weq series (pre-run4)**: The `weq_rpo` and `weq_sl` banks are an earlier, unnamed batch targeting word_3707. They use a shorter naming scheme (no run number, no k/sp in name) and slightly different parameters (sp=0.70, sk=6 from kbprog.log headers). Word_3707 is the end of the buggy chain (28652→544→15328→10624→8402→4882→3732→3707); word_3705 is a further reduction.

**run4 batch (~2026-04-06)**: Six agents, varied orderings and sk values, fixed sp (~0.5). Produced the largest rule banks of any single biased session for shortlex (1.8M). Driver script missing from disk — params reconstructed.

**run5 batch (~2026-04-07)**: Four agents exploring sp and word-equality mode. The `weq_cn100k` agent produced the largest bank (3.2M rules) via word-equality mode with high sp.

## Main findings

- **Rule counts**: Higher sp (more aggressive bias) tends to produce more rules at fixed wall-clock time (run5 sp0.99 at 2.3M vs. run5 sp0.50 at 1.4M). The word-equality mode (run5-weq) produces the most rules (3.2M) because kbprog is essentially solving for rules that equate the target word, which is a rich source of critical pairs.
- **sk parameter**: Higher sk (longer k-grams) produces fewer rules (run4-sl-k20 at 435K vs. run4-sl-k12 at 1.8M). Longer k-grams are rarer matches, so fewer equations qualify as "special."
- **Downstream reduction**: No documented improvement over the master bank (25.7M rules). All tests were on INVALID targets — so even a measured "improvement" would be meaningless.
- **Missing runs**: The X-core targeted agents (intended to produce rules aligned with the dominant structural pattern in comm_12_9) never produced surviving output — these would have been the most scientifically interesting runs.

## Open questions

- Do biased agents on word_7245 improve reduction beyond 7,245 chars? This is the primary outstanding question.
- Which parameter configuration is best for word_7245? The run5 sweep (varied sp, sk, weq) provides a parameter grid to replicate on the valid target.
- Do X-core targeted agents (sk tuned to 35-char core pattern) outperform full-word targeted agents?

## Related material

- [[Biased KB Agents/_type|Biased KB Agents on B(2,5)]] — parent experiment-type description
- [[_progress|B(2,5) Progress Note]] — umbrella progress note
- [[biased-kb-agents-data]] — sibling data note: full path table, script inventory
- [[biased-kb-agents-b25-2026-06-03]] — methodology note
- [[reduce-core-results]] — downstream consumer; applying these banks to targets
- [[kbmag-tools-overview]] — KBMAG tool reference
- [[2026-06-02-b25-forensic-inventory]] — W2 inventory source for this reconstruction
