---
title: t003-gated-dehn-search-2026-10-14
hypothesis: "A PatternBoost search over ordered factor sequences (r_i, c_i), with the 820 dataset relators (alone or mixed with standard v^5), the F*-based D as objective and the L1 gate, finds certified L1 words with D above the T-002 random-product maximum 0.200; it does not reach L2 (D >= 1)."
status: pending
author: asetlearning
date: 2026-10-14
todo: T-003
project: challenge-gen
instance: B(2,5)
experiment_type: patternboost-generation
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/pending, methodology]
---

# T-003: PatternBoost search maximising D under the L1 gate — pre-registration

> **Phase 1 only.** Written 2026-10-14. Nothing beyond a local smoke run (≤ 10 min) runs until Lead and the owner approve the remote jobs below. TODO item **T-003** ([[todo-challenge-gen]]). The search problem, its objective and its parameters are the owner's: [[project-challenge-gen#The search problem (owner, 2026-10-14) — the crucial part]]. Terms: [[challenge-gen-glossary]] (new terms of this note are added there). Metrics: [[challenge-gen-success-metrics]]. Baseline: [[t002-dataset-relator-products-results]]. Earlier lesson: the 2026-07-23 Dehn run in [[patternboost-generation-results]] (maximising raw D without a gate shrank words to 32 letters, D = 0.344, 0 L1 in 300k).

## Question

Can search over **ordered** factor sequences F = ((r₁,c₁), …, (r_N,c_N)) raise D = N*/|w| on L1 words above what random products reach? T-002 showed that L1 is easy with the 820 dataset relators (94–100% of random pure-dataset products) but D stays near 1/(mean factor length): median ≈ 0.02, maximum 0.200 over 7,550 words, 0 L2. D grows only if conjugated factors cancel heavily against each other under free reduction, and random choices give almost no cancellation. Group: **free B(2,5)** throughout.

## Hypotheses (falsifiable)

Notation: a **certified L1 finalist** is a word from a run's evaluated set ([[#Evaluation of finalists (harness, independent of the search)]]) that passes L0 (independent check) and L1 with ρ_min16 in certify mode. "Novel" is guard G2 (owner decision 2026-10-14).

- **H1 primary (beats the baseline).** In at least one objective variant and relator set, every seed run produces ≥ 1 certified, novel L1 finalist with D > 0.200 (the T-002 maximum over all cells). **Falsified** if no (variant, relator set) pair achieves this in all three seeds.
- **H2 strong form.** For the best (variant, relator set) of H1, the median D of its certified L1 finalists exceeds 0.200 in every seed. **Falsified** otherwise.
- **H3 L2 (prediction, not a goal threshold).** No run produces a certified L1 finalist with D ≥ 1. Reason: the strongest previous search (Dehn run, 20 iterations) reached 0.344 on words that were not even L1. **Falsified (a success)** by any L2 finalist; it would go to Validator for an independent L0 re-check before any claim.
- **H4 gate soundness.** Among words the pool-level gate passes (screen mode, generated word only), ≥ 90% are certified L1 under ρ_min16 in certify mode. **Falsified** below 0.9. This measures how much the cheap screen over-estimates L1.
- **H5 drift.** Without a length floor (variant A) the median |w| of the final pool falls by ≥ 30% from the initial pool; with the floor (variant C) it stays ≥ the floor. Descriptive comparison between A and C; **falsified** if A does not shrink (then the floor is unnecessary) or C violates the floor (a bug).
- **H6 relator set.** The mixed set R-M reaches a higher best certified D than the pure set R-D in each objective variant (median over seeds). Reason: short standard factors add cells at low letter cost, while dataset factors keep the word reducer-resistant. **Falsified** by any variant where R-D ≥ R-M.
- **H7 seeding.** Seeding the pool with T-002 L1 words gives a higher best gated D after 5 iterations than the unseeded control (same variant, relator set and seeds), in ≥ 2 of 3 seeds. **Falsified** otherwise.
- **H8 L0.** 100% of evaluated finalists pass the independent L0 check (re-expansion, every relator a hash-pinned dataset word, its inverse or a literal 5th power, abelianization). **Falsified** by one failure.

Positive control: the seed pool itself (T-002 L1 words, re-evaluated through the same finalist pipeline, must reproduce the T-002 levels exactly). Negative control: not run again. The ungated Dehn run (2026-07-23) is the reference for what happens without the gate; repeating it would cost about 15 h on the Mac and teach nothing new.

## Search parameters (profile table, all recorded per run)

| Parameter | Value | Reason |
|---|---|---|
| Relator set R | **R-D**: the 820 words of [[ds-b25-trivial-2-5reduced-aut8-20261014]] and inverses (1,640). **R-M**: R-D plus the 44 standard relators v⁵, \|v\| ≤ 3 (the 44 already include inverses; 1,684 relators, the T-002 table) | R-D gives L1 for free (T-002) but long factors (32–123 letters) cap D; R-M adds short factors (5–15 letters) that raise N* cheaply. The standard set ⊂ R-M contains every T-002 relator, so every T-002 word can seed R-M. Standard-only is not run: T-001 and T-002 show 0 L1 in 8,100 words, so the gate would score everything 0 |
| N range | initial pool 2–10 factors (seeded words keep their own N, up to 30); local search 1–60 | covers T-002's range; 60 keeps the token stream under `n_positions` 512 (about 7 tokens per factor) |
| Conjugator bound | uniform 0..4 (initial sampling, mutation, insertion: `conj_max_len` 4) | same as T-001/T-002 so the baseline comparison holds; longer conjugators raise \|w\| and lower D |
| Word-length bounds | gate `max_len` 2000 (longer words get score 0); variant C adds a floor \|w\| ≥ 100 (`local_search.min_expanded_len` 100 and `scoring.params.min_len` 100) | 2000 is where certify cost becomes seconds; 100 is below the T-002 pure-dataset median at k = 2 (106) and blocks the drift to short words |
| Move set | replace rᵢ (**sampled**: 20 random relators per factor per step, `local_search.num_relator_samples: 20`, requested, see Code; the current move is exhaustive, N × (\|R\| − 1) neighbours); mutate cᵢ (deterministic, all edit-distance-1); insert a factor (5 samples); delete a factor (exhaustive); **reorder**: swap adjacent factors (`local_search.enable_reorder: true`, exhaustive) and move a factor to another position (`local_search.num_move_samples: 5`) | the owner's move set; reordering is required because factors do not commute. Exhaustive swap over 1,640–1,684 relators would make about 13× the Dehn run's neighbours per step on 2–4× longer words, about 1 h per iteration (see estimate); sampling brings it to about N × 35 neighbours |
| Strategy | PatternBoost: GPT-2 6L/8H/256 (`n_positions` 512), 10 epochs per iteration, `temperature` 1.0, `top_k` 50, `top_p` 0.95; beam local search `beam_width` 1, `max_steps` 10 | the Dehn run's local-search setting, whose cost is known; no tuning in this experiment |
| Pool | `max_pool_size` 2000, `workflow.top_k` 2000, `n_samples` 2200 per iteration, 15 iterations, `n_initial` 20000 (truncated to the pool by gated score) | about a fifth of the Dehn run's pool, to fit the wall-clock below |
| Objective and gate | three variants, below; per-neighbour `scoring.params.l1_prefilter: true` (exact checks only); pool-level `workflow.l1_gate.enabled: true`, `min_rho` 0.5, `gated_score` 0.0, `max_len` 2000 | the owner's objective; gate in screen mode on the pool, ρ_min16 on finalists |

### Objective variants (all on `scoring.type: dehn_minimised`, i.e. D = N*/|w| on F*)

| Variant | Score of a pool word w | Config |
|---|---|---|
| **A gated D** | D(w) if w passes the gate, else 0 | `workflow.l1_gate.enabled: true` |
| **B gated D × ρ** | D(w) · ρ_screen(w) if it passes, else 0 | A + `workflow.l1_gate.multiply_rho: true` |
| **C gated D + floor** | as A, and words with \|w\| < 100 score 0 | A + `local_search.min_expanded_len: 100`, `scoring.params.min_len: 100` |

Baseline for every variant: the T-002 random products over the same relator set (R-D: P100 cells, D max 0.031; R-M: all mixed cells, D max 0.200). Arms: R-D × {A, B, C} and R-M × {A, B, C}, all seeded; plus the **unseeded control** R-M × A (H7). 7 configurations × 3 seeds = **21 runs**.

### Seed pool

The **seed pool** is a JSONL file of factor words given as (relator word, conjugator) pairs, built locally from the stored T-002 samples: for each relator set, all T-002 words that are L1 and expressible with that set, sorted by D, top 2,000 (R-D: 2,376 eligible pure-dataset words with k ≥ 2 plus the one-factor ones; R-M: all 5,221 L1 words). The initial pool is these words plus `n_initial` sampler words, truncated to `max_pool_size` by gated score. Its sha256 is recorded per run.

## Code (agreed with Developer 2026-10-14; final names once the PRs land)

Developer's branches `15-t003-reorder-dehn-min-gate` (tcgraph_agentic and b25):
- `local_search.enable_reorder` (bool, default false): exhaustive swap of adjacent factors, identical pairs skipped. `local_search.num_move_samples` (int, default 0): sampled "move factor i to position j". `local_search.min_expanded_len` (int, default 0): hard floor on |w| inside the search.
- `scoring.type: dehn_minimised`: N*/|w|, 0 if w is empty. A C++ port of the harness's `minimise.loop_erase`, cross-tested against it. Not usable as a hybrid component (needs the factor word).
- `scoring.params.l1_prefilter` (with `min_rho`, `gated_score`, `min_len`): per neighbour, exact checks only, no reducer call. **Correction sent to Developer (2026-10-14):** as first described, a word containing a power ≥ 2.5 would be counted as failing. In T-002, 4,801 of 5,221 L1 words (92%) contain such a power, so that rule would gate almost every real L1 word. Developer's scratch note now has `l1_prefilter_strict` (the strict rule as a separate opt-in). This experiment uses `l1_prefilter: true`, `l1_prefilter_strict: false`: only the exact fail |cyc(w)|/|w| < `min_rho` gates, everything else keeps its base score and is decided by the pool gate. To confirm in Developer's PR.
- `workflow.l1_gate` (`enabled`, `min_rho`, `gated_score`, `max_len`, `max_screen`, `multiply_rho`): pool-level screen gate, applied after local search and at initial pool truncation.

**Needed and not yet agreed** (Developer will ask Lead whether they belong in the same PR; this experiment cannot run without 1, 3, 4 and 5; 2 has a fallback; 4 and 5 are implemented, 1 and 3 are not yet):
1. **Stable relator order** for `relators.relators_file` (opt-in; today the map is built from a Python set, so indices change between runs).
2. **Mixed relator source**: file plus standard v⁵ (e.g. `relators.include_standard`). Fallback without it: a relators file holding the 820 words plus the 44 standard ones.
3. **Seed pool loader**: `initial_sampling.seed_pool_file` (factor words as relator words plus conjugators, mapped to indices at load).
4. **Sampled relator swap**: `local_search.num_relator_samples` (0 = exhaustive, today's behaviour; k > 0 = k random replacement relators per factor per step from the searcher rng). **Implemented** by Developer in tcgraph PR #3 @ dd24bae / b25 PR #5 @ ef3850e (open, 2026-10-14).
5. **Relator table dump**: every run writes `relator_table.json` (table in index order, sha256, source) next to `run.jsonl`. **Implemented** in the same PRs, with a test that re-expands a certificate from the dump alone.

Pool and checkpoint dumps use the existing `workflow.save_every` (set to 5: iterations 0, 5, 10, 14).

## Evaluation of finalists (harness, independent of the search)

Per run: the top 200 words of the final pool by gated D, a uniform random 10% sample of the rest of the final pool (180 words, for H4), and every word that passed the gate during the run with gated D > 0.200 (from the pool dumps at iterations 0, 5, 10, 14; capped at 200 by D). Each goes through the T-002 harness (`experiments/challenge_gen/hardness/`): independent L0 against the dumped relator table, F* by loop erasure, D, certify-mode R₂.₅, ρ_min16 (16 images, certify; power-free shortcut where exact), level, novelty by G2, and canon(R) against the 820. Limits as in T-002: certify for n ≤ 2000, ρ_min16 for n ≤ 2000 on the Mac (at n ≈ 1000 certify costs about 5 s per image on the VM, so ≤ 80 s per word); timeouts are recorded as undecided.

Reported per run: counts of L1 / novel L1 / L2 finalists, best and median D among certified L1 finalists, |w| and N* of the best, screen-to-ρ_min16 agreement (H4), the per-iteration trajectory of best and median gated D and |w| (from `run.jsonl`), and wall-clock per phase.

## Seeds

- PatternBoost workflow seeds **3000001, 3000002, 3000003** (one per run of each configuration). Distinct from T-001 (1000001–5), T-002 (2000001–5) and PatternBoost's earlier range (< 300,000).
- Smoke seed **3000000**, never reported.
- MPS training is not bit-reproducible, so reproducibility is by artifact: every run keeps `run.jsonl`, the pool dumps, the relator table and the seed-pool file (hashed).

## Statistics

Three seeds per configuration: all claims are per seed and descriptive (best and median D, counts with Clopper–Pearson 95% intervals for rates such as H4). No significance test between variants is claimed with n = 3; H6 and H7 are sign comparisons per seed, stated as such.

## Execution split (local VM versus remote)

| Part | Where | Cost |
|---|---|---|
| Seed-pool files, relator files and hashes; harness extension for PatternBoost output (`eval_pb`: reads pool dumps and relator table); unit tests | **local** | small |
| Smoke run: pool 50, 2 iterations, tiny GPT-2 on CPU, both relator sets, all three variants; measures local-search seconds per call and gate cost | **local**, ≤ 10 min, once Developer's branches exist | ≤ 10 min |
| 21 PatternBoost runs (training on MPS, local search on 9 CPU workers) + finalist evaluation in the same job | **remote**, rjob on the owner's Mac, one job at a time | below |
| Analysis, tables, notes | **local** | small |

### Planned rjob jobs (after approval)

One job per run (21 jobs, sequential), each: build b25 at the T-003 experiment branch SHA with `cpp/tcgraph` at Developer's merged SHA; `pattern_boost_main run <config>` (15 iterations); then `eval_pb` on the final pool and the gate-passed high-D words. Stage 1 = the 7 configurations with seed 3000001 (results checked before stage 2); stage 2 = seeds 3000002 and 3000003 (14 jobs). Configs are generated from one template plus the 7 variant overlays, all committed before submission.

### Wall-clock estimate (to be revised by the smoke)

- Dehn run reference: about 15 min per iteration at pool 10,000 and 15,000 samples with 132 relators and words of length 50–400.
- Local search, Dehn run: 15,000 calls × 0.3–0.4 s / 12 workers ≈ 7 min per iteration, at about 1,200–1,740 neighbours per call on words of 50–400 letters.
- Here with **sampled** relator swap: about N × 35 neighbours per step (N ≈ 10: about 350), on words 2–4× longer, so about 0.2–0.4 s per call; 2,200 calls / 9 workers ≈ 1–2 min per iteration. Generation of 2,200 samples (max length 512) and 10 training epochs on 2,000 words: about 5–10 min. Pool gate: 2,000 screens × 1–20 ms, under 1 min. **About 8–15 min per iteration, 2–4 h for 15 iterations.**
- With **exhaustive** relator swap (about N × 1,700 neighbours, about 13× the Dehn run per call on longer words): about 50–60 min per iteration, about 15 h per run. Not planned.
- Finalist evaluation: about 400–600 words × 16 images × certify at n ≈ 300–600 (0.1–1 s per image on the VM) ≈ 0.5–3 core-hours, spread over 9 cores: **under 30 min per run**.
- **Per run about 2.5–4.5 h. Stage 1: 7 runs, about 18–32 h of Mac time. Stage 2: 14 runs, about 35–63 h. Total: about 53–95 h.** The smoke measures seconds per local-search call and per gate screen; the job list goes to Lead with the measured numbers.
- If the smoke shows local search above 20 min per iteration, I will propose `local_search` relator-swap sampling or a smaller pool to Lead before submitting, not change it silently.

## Success criteria (owner's levels)

- **Experiment success:** H1, i.e. certified novel L1 words with D > 0.200 (above the best random product) in all seeds of at least one configuration.
- **L2:** any certified L1 finalist with D ≥ 1 (predicted not to happen, H3).
- **L3** is a family property and is not tested here.

## Anti-pattern check

- *Tuning on the test set:* the search parameters are fixed above, before the smoke. The smoke only measures cost; if it forces a change, Lead is told and the change is recorded as a deviation.
- *Metric gaming:* D is computed on F* (loop erasure removes freely cancelling blocks), the gate blocks the short-word drift, and finalists are re-evaluated by the independent harness with ρ_min16 (all 16 images), not with the screen value the search optimised. Remaining loophole, stated: blocks that cancel only modulo relators stay in F*, so D is an upper bound on area/n.
- *Circularity:* the search's own score is never reported as the result; only harness-certified numbers are.
- *Seeds:* all three listed; every run's artifacts kept; failed runs reported.
- *Necessary versus sufficient:* L1 means "resists the 2.5 reducer", D is an upper-bound proxy; nothing here proves hardness for other solvers.
- *Group named:* free B(2,5) throughout.

## Open questions for Lead

1. Items 1–4 of "Needed and not yet agreed": same PR as Developer's T-003 work, or a separate one? The runs need 1–3.
2. Budget: approve stage 1 (7 runs, about 18–35 h) first, and stage 2 after its results?
3. Sampled relator swap (`num_relator_samples`, 20 per factor): acceptable, and in Developer's PR?
4. Is R-M with the 44 standard relators (\|v\| ≤ 3) acceptable, or does the owner want \|v\| ≤ 2 (16) to match the T-002 cell where D reached 0.200?

## Approval and deviations (2026-10-14)

Owner approval (relayed by Lead, 2026-10-14): (1) the 7 stage-1 configurations as pre-registered, seed 3000001; (2) R-M with the 44 standard relators, \|v\| ≤ 3; (3) per-neighbour filter `l1_prefilter` with the default margin 2 (`l1_prefilter_margin: 2`: fails only if (\|cyc(w)\| + 2)/\|w\| < 0.5), strict off; (4) **reduced stage 2**, recorded here as a deviation:
- **Deviation (stage 2).** After stage 1, only the 2–3 most promising configurations (plus the unseeded control only if H7 is still open) run with seeds 3000002 and 3000003, about 4–6 runs, proposed by me with reasons and approved by the owner. Stage 2 is skipped if no stage-1 run beats D = 0.200. Consequently, the "all three seeds" clauses of H1 and H2 apply only to the configurations that reach stage 2; for the others, stage-1 results are reported for one seed.
- **Code as merged** (b25 main `d21691a`, pins tcgraph `dd24bae`; tcgraph main `2be028d`): every item of "Needed and not yet agreed" was implemented: `relators.file_order`, `relators.include_standard`, `initial_sampling.seed_pool_file` + `mix`, `local_search.num_relator_samples`, `relator_table.json`. Experiment branch `16-t003-gated-dehn-search` (off main, with branch 14 merged for the harness), commit `4ce9704`: `experiments/challenge_gen/t003/` (inputs, configs, smoke, `eval_pb`, job script).
- **Seed pool `mix` 0.9:** 2,000 of the 20,000 initial words come from the seed pool, 18,000 from the sampler.

- **Deviation (owner decision 2026-10-14, option 1, after the smoke): length floor on every R-M configuration.** Evidence: in the smoke (table below), local search on R-M without a floor collapsed words to a median of 10 letters, and the pool gate passed **0 of 40** of them (R-M with the floor: 22 of 40). Change: every R-M configuration uses `local_search.min_expanded_len: 100` and `scoring.params.min_len: 100`. R-M × A is dropped (with the floor it equals R-M × C); R-M × B runs with the floor; the unseeded control is R-M × C instead of R-M × A. **Stage 1 = 6 runs:** R-D × {A, B, C}, R-M × {B + floor, C}, unseeded R-M × C. H7 now compares seeded and unseeded R-M × C; H6 compares R-D and R-M on B and C only (R-M × A no longer exists). Configs: branch `16-t003-gated-dehn-search` @ `c86014e`.
- **Baseline correction (2026-10-14).** The best D among T-002 **L1** words is 0.066 (0.031 for pure-dataset words); the 0.200 maximum came from a non-L1 word. The H1 success bar stays at **0.200** (owner); every report also gives the number of certified L1 finalists (and novel ones) with D > 0.066 (`eval_pb` fields `L1_D_gt_L1_baseline`, `novel_L1_D_gt_L1_baseline`).

- **Deviation (2026-10-14, owner-approved): pool merge by score.** Job 1 (`20261014-110539-4e4d92`, R-M × C) showed that `_merge_pool` (b25 `algorithms/pattern_boost/workflow.py`) keeps the *newest* `max_pool_size` words, not the best: with `top_k` = `max_pool_size` = 2,000, each iteration's outputs replace the whole pool, including words the gate scored 0. Gate passers: initial pool 2,000/2,000; iteration 0 outputs 737/2,180; iteration 1 61/2,178; iteration 2 18/2,185. The model then trains on rejected words. Jobs 2–6 were cancelled before starting. Developer is adding `workflow.pool_merge: newest|score` (score = keep the top by stored gated score, ties newer first); all six stage-1 configurations will be rerun with the score merge (new job ids recorded here). Job 1 runs to completion and is reported separately as the **newest-merge run**, not as a stage-1 result. Fix: b25 PR #6 (main `5e900ee`), `workflow.pool_merge: score`; all six configurations set it (branch `16-t003-gated-dehn-search` @ `86b1672`, main merged in). `eval_pb` now takes finalists from the kept pool (`pool.json`). Local smoke (`smoke_pool_merge`, R-M × C, pool 200, 220 candidates per iteration from local search on pool words as a stand-in for the model, real merge, scorer and gate), pool passers over 5 iterations: **newest** 86 → 99, 104, 72, 65, 51 (output pass 99, 81, 45, 32, 26 of 220); **score** 86 → 185, 200, 200, 200, 200 (output pass 99, 108, 138, 161, 167 of 220); best gated score retained (0.09). Resubmitted stage-1 jobs (seed 3000001): RM-C `20261014-122140-506aac`, RD-C `20261014-122142-4b625c`, RD-A `20261014-122144-8d760b`, RD-B `20261014-122146-d1994d`, RM-B `20261014-122148-7248a7`, RM-C unseeded `20261014-122150-080af8`.

- **Deviation (owner decision 2026-10-14, padding loophole, option 1).** D stays as defined. Every certified finalist and every run additionally reports n_dataset_fstar, n_standard_fstar, padding fraction (1 − ρ_min16), D_dataset and dataset core (definitions: [[challenge-gen-glossary#Padding breakdown (T-003)]]). Code: `experiments/challenge_gen/t003/padding.py`, called by `eval_pb` from `b98c938`; the stage-1 jobs run `86b1672`, so the breakdown is computed locally on their fetched outputs (no resubmission). Whether to tighten the metric (ρ ≥ 0.9 on R-M, or D on dataset factors only) is decided by the owner after stage 1.

## Smoke (local VM, 2026-10-14, seed 3000000)

`smoke_components` (no torch on the VM, so model training and sampling are timed on the first remote job instead):
- Relator tables: R-D = the first 1,640 entries and R-M = all 1,684 entries of the T-002 table, entry for entry. All 2,000 seed words of each pool load and expand identically to the independent expansion. `dehn_minimised` equals the harness D on 300 of 300 seed words.
- Local search (T-003 settings, 40 calls per cell on seed words):

| Set | Variant | s per call (median / max) | neighbours per step | median \|w\| after search | pool gate pass |
|---|---|---|---|---|---|
| R-D | A | 0.002 / 0.43 | 129 | 53 | 37/40 |
| R-D | C | 0.004 / 0.03 | 108 | 103 | 34/40 |
| R-M | A | 0.003 / 0.41 | 145 | 10 | **0/40** |
| R-M | C | 0.005 / 0.40 | 216 | 101 | 22/40 |

- Pool gate: 0.1–1.7 ms per screened word.
- **Finding.** Without the length floor, local search on R-M replaces the dataset factors by short standard relators and collapses words to about 10 letters (D up to 0.23), all of which the gate rejects. The per-neighbour filter cannot see 2.5-reducibility, so in R-M variants A and B (and the unseeded control) the local-search outputs are almost all gated, and the pool can only improve through words the model proposes. This is the drift of H5 in its strongest form; the runs go ahead as approved, queued last.
- **Baseline detail.** Among T-002 L1 words the largest D is 0.066 (R-M seed pool) and 0.031 (R-D); the 0.200 maximum was reached by a word that is not L1. The H1 bar of 0.200 is therefore about 3× the best L1 random product.
- `eval_pb` tested end to end on a synthetic run directory (47 finalists, 47 L0, 47 L1, G2 computed).

## Results
Stage 1 (score merge): running (job ids above).

**Newest-merge run (job 1, `20261014-110539-4e4d92`, R-M × C, seed 3000001; not a stage-1 result).** PatternBoost 82 min (15 iterations), evaluation seconds. Search outputs passing the gate per iteration: 737, 61, 18, 18, 5, 2, 3, 8, 8, 5, 5, 6, 3, 5, 1 (of about 2,200); best gated D 0.08 → 0.17 (iteration 11) → 0.15; mean \|w\| about 150. The final pool held one gate passer: certified L0 and L1 (ρ_min16 = 0.50), D = 0.15, **not novel** (G2). It is one 50-letter dataset factor (inverse of line 35) plus 14 standard v⁵ factors (conjugators of length 0–2) at exactly \|w\| = 100: the reducer removes the standard parts and keeps the relator's 50 letters, so ρ_min16 = 0.5 while all 15 factors count in N*. On R-M, D can therefore be raised by padding one dataset relator with standard factors up to the ρ ≥ 0.5 limit; G2 identifies such words as non-novel.
