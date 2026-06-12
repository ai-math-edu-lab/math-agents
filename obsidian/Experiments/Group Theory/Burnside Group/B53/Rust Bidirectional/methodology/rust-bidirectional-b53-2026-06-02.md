---
title: Rust bidirectional search on B(5,3)
domain: group-theory
project: b53
instance: B(5,3)
experiment_type: bidirectional
status: inconclusive
reconstructed_on: 2026-06-02
author: maumayma
wall_time_s: 1733
git_sha_or_local: local (tracking not retrofitted)
experiment_id: b53-bidir-v5
params_bidir_orderings: rpo,shortlex,wtlex,rpo-r2l
params_bidir_dynamic_conj: true
params_bidir_target_words: 153
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/bidirectional, topic/knuth-bendix, project/b53, status/inconclusive, methodology]
---

# Experiment — Rust Bidirectional Search on B(5,3)

## Reconstruction notes

Reconstructed 2026-06-02 from: `experiments/burnside/b53_bidir/src/bin/b53_bidir.rs` (Rust source), `experiments/burnside/b53_bidir/b53_relators.txt` (153 target words), `runs/b53/20260320_051415/trace.json` (Rust mixer trace), kbprog log at `runs/b53/20260320_051415/logs/kb_shortlex_log.txt`, and project memory notes on B53 bidir v5 progress (144/153 at 1733s). The compiled binary is present but no output run directories for v5 are on disk — v5 results are from vault memory records.

## What this experiment does

Standard KB completion on B(5,3) (the KBMag approach) shows no convergence after 97h. A more targeted alternative: instead of trying to prove the whole group presentation is confluent, prove specific word-equality instances — that a given word `w` equals the identity in B(5,3). This is the **bidirectional search** approach.

The experiment runs multiple KB agents with different term orderings simultaneously. Each ordering produces a different rule bank that is good at reducing different word shapes. A greedy reducer tests each target word against the accumulated rule banks. When a target word reduces to the empty word under some combination of rules, it is proved.

**Bidirectional** means the reducer tries both forward-application (reduce `w` to `ε`) and backward-application (reduce `ε` toward `w` form, i.e. apply rules in reverse), providing more paths to proof.

## Hypothesis

Running 4 term orderings simultaneously with dynamic conjugation will prove all (or most) of the 153 B(5,3) target words within a feasible wall-clock budget (~30 min).

## Problem set

- Group: B(5,3), free Burnside group on 5 generators of exponent 3
- Target words: 153 words from `experiments/burnside/b53_bidir/b53_relators.txt` — word-equality instances to prove
- Presentation: `kbmag_v1/standalone/kb_data/b53_full` (same as KBMag)

## Mixer agents involved

**Four KB sources** (orderings) in v5:
1. **RPO** — recursive path ordering; good at long chains of reduction
2. **Shortlex** — shortlex; good at length reduction
3. **Wtlex** — wreathprod ordering; good at specific commutator patterns; **key source** for the hard words (proved 119–144 after wtlex source built, at ~2.3M rules)
4. **RPO r2l** — RPO right-to-left (or reverse variant)

Plus **dynamic conjugation**: during reduction, when a word is stuck, the reducer conjugates it (multiplies by a generator and its inverse) and re-attempts reduction. This expands the search space without requiring additional KB agents.

## Strategy effectiveness (from project memory, v5)

| Strategy | % of proofs |
|---|---|
| greedy (direct rule application) | 68% |
| focus-conj (focused conjugation) | 13% |
| conj (conjugation) | 8% |
| dfs (depth-first search) | 5% |
| other | 6% |

## Scheduler config

- KB agents (per ordering): started in parallel; rule banks accumulated incrementally
- Each time a KB agent reaches a checkpoint (rule bank size threshold), it transfers its rules to the reducer
- Reducer tests all unproved target words against the new rules
- No injection between orderings — each ordering runs independently; reducer merges their output

## Termination criteria

- All 153 target words proved (desired)
- User interruption / time limit (v5 was running at 1733s when memory records were made)

## Baselines

- v1/v2 runs (`runs/b53/20260320_051415`, `runs/b53/20260320_052723`): shortlex only; first KB→reducer transfer at 98K rules; proved 0 words (reducer received 98K rules, 0 proved on first pass); interrupted at 123K rules
- The v1/v2 baselines establish that shortlex alone is insufficient for B(5,3) word equality

## Metric

- Primary: number of target words proved out of 153, at a given wall-clock
- Secondary: which strategy proves which words (greedy vs. conjugation)
- Hardest words: the 9 remaining after 1733s in v5

## Validation

- Proof of word `w` = identity in B(5,3): `w` reduces to `ε` under the accumulated rules. This is a valid proof in B(5,3) because the rules are KB-derivable from the presentation relators — each rule is a consequence of the axioms.
- No independent validator used. Math validation for the 144 proved words: **none formally recorded** (routes to Validator for coverage if needed)
- The 9 remaining unproved words are believed to require rules not yet in any of the 4 ordering banks

## Three hardest words (unproved as of v5 at 1733s)

From project memory:
1. `EaceAdBDbaECAecbDBdC`
2. `ECbcBeadADEbCBcedaDA`
3. `AbaBEbABaeCAbaBebABaEc`

These are 20–21 character words. Their hardness suggests they require highly specific reduction sequences that no single-ordering KB bank has generated yet.

## Related material

- [[Rust Bidirectional/_type]] — parent experiment-type
- [[B53/_progress]] — B(5,3) umbrella
- [[data/rust-bidirectional-data-b53]] — target words, run locations
- [[results/rust-bidirectional-results-b53]] — 144/153 table, hard-word analysis
- [[KBMag/methodology/kbmag-overlap-scoring-b53-2026-06-02]] — KBMag approach (contrast)
- [[2026-06-02-non-b25-forensic-inventory]] — §2c B53 bidir forensic provenance
