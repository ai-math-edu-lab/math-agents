---
title: Rust Bidirectional B(2,5) Results
domain: group-theory
project: b25
experiment_type: rust-bidirectional
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, project/b25, status/inconclusive, results]
reconstructed_on: 2026-05-22
---

# Rust Bidirectional B(2,5) Results

## Reconstruction notes

Trace files surviving in `runs/b25/` (6 directories) and `runs/b25_lifted/` (2 directories) were re-read on 2026-05-22 to reconstruct this table. One directory (`20260320_054957`) had an empty trace (aborted run). Evidence for a third direct-target benchmark pass (targeting comm_12_9 non-lifted) comes from commit 9116709 adding `b25_only_comm_12_9.txt`; no trace files for that pass survived.

The three benchmark passes are distinguished by run date and target strategy:
- **Pass 1** (2026-03-20): multiple configs targeting comm_22_3 and comm_11_1_kyr
- **Pass 2** (2026-03-28): 4-ordering config targeting comm_13_10
- **Pass 3** (2026-03-30): lifted-alphabet config targeting lifted comm_12_9 (w0)

## Results table

| Run ID | Date | Config file | Orderings | Bootstrap | Target | Input len | Best len | Wall-clock | Notes |
|--------|------|-------------|-----------|-----------|--------|----------:|----------:|------------|-------|
| p1-comm22-3-no-bootstrap | 2026-03-20 | `wtlex_rpo_shortlex_comm_22_3.toml` | wtlex + rpo + shortlex (3) | none (99k shortlex accumulated during run) | comm_22_3 | 4,162 | 4,156 | ~452s | not proved; 3-ordering baseline |
| p1-comm22-3-aborted | 2026-03-20 | `wtlex_rpo_shortlex_comm_22_3.toml` | wtlex + rpo + shortlex (3) | unknown | comm_22_3 | 4,162 | unknown | unknown | empty trace — aborted or crashed |
| p1-comm22-3-bootstrap-3ord | 2026-03-20 | `wtlex_rpo_shortlex_comm_22_3.toml` | wtlex + rpo + shortlex (3) | 13.1M rules | comm_22_3 | 4,162 | 4,156 | ~262s | not proved; same result as no-bootstrap |
| p1-comm22-3-slex-bootstrap | 2026-03-20 | `bootstrap_shortlex_comm_22_3.toml` | shortlex only (1) | 13.1M rules | comm_22_3 | 4,162 | 4,156 | ~656s | not proved; shortlex-only ablation |
| p1-comm11-1-kyr | 2026-03-20 | `bootstrap_shortlex_comm_22_3.toml` (exp: b25_bootstrap_shortlex_comm_11_1) | shortlex (1) | 13.1M rules | comm_11_1_kyr | 164 | 164 | ~236s | not proved; beam explored 12.8M states |
| p1-comm11-1-long | 2026-03-20 | same as above | shortlex (1) | 13.1M rules | comm_11_1_kyr + word (3,698 chars) | 164 / 3,698 | not proved | ~1,142s | tier2_random timed out |
| p2-comm13-10-4ord | 2026-03-28 | `biased_comm_13_10.toml` | rpo_l2r + rpo_r2l + slex_l2r + slex_r2l (4) | none at start; 10M rules accumulated (rpo_l2r: 2.29M, slex_r2l: 2.85M, rpo_r2l: 2.30M, slex_l2r: 2.76M) | comm_13_10 | 2,500 | 2,494 | ~12,983s (~3.6h) | not proved; 0.2% reduction |
| p3-lifted-12-9-short | 2026-03-30 | `bootstrap_lifted_comm_12_9.toml` | shortlex + rpo (2) | 14.2M lifted rules (`experiments/b25_lifted_kb/all_rules_combined.live`) | lifted comm_12_9 (w0) | 1,772 | 544 (gen_braid only) | ~237s | not proved; cut off before beam search; gen_braid reduces 1772→544 |
| p3-lifted-12-9-long | 2026-03-30 | `bootstrap_lifted_comm_12_9.toml` | shortlex + rpo (2) | 14.2M lifted rules | lifted comm_12_9 (w0) | 1,772 | not proved | 7,200s (timeout) | RPO reached 798k rules; result still 544 (no improvement over braid phase) |
| p3-comm12-9-direct | unknown (post-2026-04) | unknown | unknown | unknown | comm_12_9 (direct) | unknown | unknown | unknown | **no surviving trace** — reconstruction limitation; evidence: commit 9116709 adding `b25_only_comm_12_9.txt` |

## Pass summaries

### Pass 1 — 2026-03-20 (comm_22_3 + comm_11_1_kyr)

Six run directories. Three configs tested on comm_22_3 (4,162 chars): no-bootstrap 3-ordering, bootstrap 3-ordering, bootstrap shortlex-only. All return best_len=4,156 — minor reduction, not proved. Two runs then shifted to comm_11_1_kyr (164 chars, Kyr's word). Beam explored 12.8M states on comm_11_1_kyr without proving it. The 13.1M-rule bootstrap (loaded from prior `kbmag_v1/` or `kbmag_source/` runs) shortened wall-clock from 452s to 262s on comm_22_3 without changing the result.

### Pass 2 — 2026-03-28 (comm_13_10, 4 orderings)

Single 3.6-hour run using 4 orderings (two RPO, two shortlex, bidirectional pairing). Accumulated 10M rules across all agents. comm_13_10 (2,500 chars) reduced to 2,494 — barely improved. Not proved. The 4-ordering design (two genuinely distinct orderings for the 2-generator group) was the B(2,5)-specific feature added in bc3cba2.

### Pass 3 — 2026-03-30 (lifted comm_12_9)

Two runs with 14.2M lifted rules pre-loaded (bootstrap_lifted_comm_12_9.toml). The gen_braid phase reduces the lifted word from 1,772 to 544 chars immediately in both runs. The short run (~237s) cuts off before beam search can run. The long run (7,200s) runs RPO to 798k rules but cannot improve beyond 544. The lift-and-reduce idea compresses the input dramatically but the rule bank in {a,b,m} alphabet does not have enough coverage to advance further.

A third direct-comm_12_9 attempt (no lift) is evidenced by commit 9116709 but left no surviving trace.

## Version history

**v1** (bidirectional-search branch, merged PR #18 on 2026-04-02): Initial B(2,5) bidirectional configuration. Added dual-RPO (two genuinely distinct orderings for 2 generators), generalized braid (LCE-based, O(n log²n)), and random-identity sanity check. The `bc3cba2` commit added random identities and significantly extended `braid.rs` (367 → ~730 lines).

The B(2,5) experiment directory (`experiments/burnside_bidirectional/`) was subsequently deleted from disk. Configs survive in git at `bc3cba2` under `experiments/burnside_bidirectional/configs/b25/`. Run outputs survive in `runs/b25/` and `runs/b25_lifted/`.

## Main findings

- The tiered reducer (gen_braid + beam) provides meaningful reduction for comm_13_10 and comm_12_9 in lifted form, but plateaus quickly.
- Bootstrap with 13.1M–14.2M rules does not meaningfully change final outcomes — only wall-clock.
- No B(2,5) words proved across any surviving run.
- The 4-ordering config (Pass 2) offers richer rule coverage but still does not prove comm_13_10 in 3.6h.
- The lift + gen_braid trick (1772→544 for lifted comm_12_9) is the most dramatic single-step reduction observed in these runs.

## Open questions

- Were any B(2,5) words proved during the direct-comm_12_9 Pass 3 run (no trace)?
- With the corrected 7,245-char comm_12_9 as starting word (rather than the 28,652-char original), would Pass 3 produce a better result?
- Should we restore the TOML configs from git and re-run targeting the 7,245-char starting word? Route to Lead.

## Related material

- [[Rust Bidirectional/_type|Rust Bidirectional on B(2,5)]] — parent experiment-type description; explains the tiered reducer stages (greedy AC → braid → beam) and how RPO rules are reoriented
- [[_progress|B(2,5) Progress Note]] — umbrella standing progress note; these run outcomes are summarised in the "What's been tried" table
- [[rust-bidirectional-data]] — sibling data note: TOML configs, input presentations, surviving rule bank paths, beam constants
- [[rust-bidirectional-b25-2026-05-22]] — methodology note; full experiment pre-registration including dual-RPO hypothesis and reconstruction notes from git bc3cba2
- [[kbmag-tools-overview]] — KBMAG tool reference; `kbprog` runs as KB agent subprocess in all three passes recorded here
- [[havas-wall-wamsley-1974]] — source of all target words (comm_22_3, comm_11_1_kyr, comm_13_10 named via the 1974 generator numbering); also provides the KB input relators
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: each "not proved" outcome in the results table establishes an empirical lower bound for identity certificates relevant to problem 11.48
