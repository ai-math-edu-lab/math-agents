---
title: Challenge generation — experiment progress
domain: group-theory
project: challenge-gen
instance: B(2,5) (phase 1)
status: pending
author: asetlearning
tags: [agent/human, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, project/challenge-gen, status/pending, experiment]
---

# Challenge Generation — Progress

Project profile: [[project-challenge-gen]]. Goal: generate **hard** problem instances that come with a **certificate** proving they have a solution. These are for benchmarking and training search algorithms. Phase 1 is hard trivial words ("challenges") in **B(2,5)**. Later candidates include Andrews–Curtis.

> Created 2026-10-05. Experiment-type folders go under per-problem instance folders, e.g. `B25/<Experiment type>/{methodology,data,results}/`, per [[experiment-folder-convention]]. Instance folders are created with their first experiment.

## Current question

**Updated 2026-10-14 (owner):** the core task is now the search problem in [[project-challenge-gen#The search problem (owner, 2026-10-14) — the crucial part]]: maximise D = N*/|w| over ordered factor sequences (rᵢ, cᵢ) subject to the L1 gate (terms in [[challenge-gen-glossary]]).

**Updated 2026-10-05:** Can we generate certified trivial words that pass L1 (2.5-reduction resistant), and then L2 (Dehn proxy ≥ 1)? The original question follows.


How can we generate words that are provably trivial in B(2,5), with the proof produced by the generator itself, and that resemble the rare "hard" instances rather than generic random ones?

## Definitions and metrics (owner, 2026-10-05)

See [[challenge-gen-success-metrics]].
- **Challenge:** a word w̄ in free B(2,5) with a certificate F, i.e. a factor word over relators trivial in free B(2,5), with expand(F) = w̄.
- **Hard (L1):** 2.5 reduction leaves ρ = |R₂.₅(w)|/|w̄| ≥ 0.5 and does not reach 1. Every random factor word fails this; it reduces to 1.
- **High filling (L2):** D = |F*|/|w̄| ≥ 1 on the minimised certificate F*. This is an upper-bound proxy for the Dehn function.
- **Great (L3):** a family with |F*| ≈ c·n², i.e. quadratic area.

## Prior work in the vault

- [[2026-09-30-b25-b0-challenge-triviality]]: all 150 human challenge words (118 non-empty, 32 empty) are the identity in the **restricted** B₀(2,5) (5^34, class 12, GAP/Pq). This says nothing about the free B(2,5). It is a natural first benchmark set. Experiment folder: [[B25/B0 Challenge Triviality/_type|B0 Challenge Triviality]] (lives in the `#project/b25` tree).

## Instances and experiment types
- **B25** → [[B25/PatternBoost Generation/_type|PatternBoost Generation]]. A PatternBoost loop over certified factor words. The baseline steers onto random certified targets with up to 100% success, but generates no hard words yet. See [[patternboost-generation-results]].

## Log

### 2026-10-05 — project registered
`#project/challenge-gen` registered, with its profile and this progress note. A literature scan on hard-instance generation is pending. Writeups, plans and the first experiments will follow from asetlearning.

### 2026-10-05 — literature scan
The scan ingested 12 papers: generic-case complexity, certified trivial-word and Andrews–Curtis generators, quiet planting in SAT/CSP, and learned/adversarial instance generators. Synthesis: [[_synthesis-hard-instance-generation]]. Its recommendation has three steps: (1) build a baseline certified generator with an independent checker; (2) fix the hardness metrics on baseline output and on the human challenge words; (3) do adversarial generation over certified moves, rewarded against a solver portfolio. The key open theory question: is the **witness** version of the word problem generically hard ([[kapovich-2003-generic-case-complexity]] §4)?

### 2026-10-05: PatternBoost generator ingested
Ingested the owner's PatternBoost implementation: the design writeup, the baseline sweep dashboard (24 combos × 50 trials), and both code repos.
- The code repos are registered as [[dep-b25-pyproject-agentic]] and [[dep-tcgraph-agentic]], and the profile is updated.
- **Key facts:**
  - Triviality is certified by construction, given trivial relators.
  - Baseline success is driven by local-search steps; the cheapest setting at ≥ 90% is w1.s10.p100 (96%, 96 s).
  - Early candidates were all 2.5-reducible to 1, so hardness is not yet addressed.
- **Known issues, documented, not fixed:**
  - b25's submodule URL points at gt-computations/tcgraph, and the pin is stale.
  - tcgraph_agentic main fails to build `test_pb_local_search`; verified, ctest 8/9.
  - No provenance or seeds are logged.
- Next: the owner will supply new ideas, goals and metrics for actual challenge generation.

### 2026-10-05: new goals and metrics
The owner defined the difficulty metrics: ρ (2.5-reduction resistance, pass at ≥ 0.5) and the Dehn proxy D on a minimised certificate (pass at ≥ 1; quadratic family is the great outcome). Challenge similarity becomes secondary. See [[challenge-gen-success-metrics]].

### 2026-10-05: Dehn-proxy maximisation run analysed (run of 2026-07-23)
PatternBoost maximising the raw D, with 2.5-reduced KB relators, over 20 iterations and about 300k candidates: **every candidate 2.5-reduces to 1** (L1: 0). Best D = 0.344 (11 factors / 32 letters), flat from iteration 3. The search raised D by shrinking words (mean length 1159 → 52) rather than adding factors. Lesson: D alone pushes toward short, easy words, so the objective needs a Metric-1 gate or a length floor. See [[patternboost-generation-results]] § Dehn-proxy run.

### 2026-10-05: remote execution set up (code only; Mac not yet configured)
The VM (2 CPUs, about 3 GB RAM, no GPU) cannot run PatternBoost at scale, so the owner set an execution policy:
- **local:** code, compiling, tests, smoke runs and analysis;
- **remote:** GPU work, and anything expected to exceed 30 min or 2 GB.

New repo [[dep-remote-jobs]] (`rjob`):
- ships exact commits, including the tcgraph submodule, to the host as git bundles;
- builds once per SHA;
- queues jobs on GPU/CPU slots;
- returns results to `~/Research/challenge-gen/runs/<job-id>/` with `provenance.json`.

Decision: Docker is not used on the Mac, because it has no MPS inside containers. Docker becomes the backend for future Linux/CUDA servers. The end-to-end test passes in the VM. Waiting on the Mac admin setup (`docs/mac-setup.md`) and on creation of the GitHub repo.

### 2026-10-07: first registered dataset; datasets convention
The owner's rpo (917) and shortlex (2378) "trivial, no powers" sets of 2026-03-21 were vetted and combined into [[ds-b25-trivial-2-5reduced-aut8-20261007]] (820 words; validated by the owner on 2026-10-07).
- All 3295 words pass abelianization and are trivial in B₀(2,5) (GAP + anupq), in original and reduced form.
- 180 words were not 2.5-reduced; 152 of them reduce to the empty word, which proves them trivial in B(2,5). Those 152 were dropped.
- The rest were deduplicated up to rotation, inversion and the 8 letter automorphisms.
- **All 820 were then proved trivial in B(2,5)** by Knuth–Bendix: kbprog on `b25_full` (815 relators, all 5th powers), capped at 100k rules, with RPO and shortlex orderings. Every word reduces to the identity under at least one system, every parent word under both, and 0/825 negative controls reduce. The parents came from the March 2026 kbprog rule banks.

The HWW challenges are registered too:
- [[ds-b25-hww-challenges-nonempty-20260930]]: 118 non-empty freely reduced words, validated trivial in B₀(2,5).
- [[ds-b25-hww-challenges-2-5reduced-20260319]]: their 2.5-reduced form, copied from the owner's tcgraph checkout.

The non-empty file turned out **not** to be 2.5-reduced; the reduced file is the one to use as targets. A 2026-10-07 GAP rerun found all 236 words (original and reduced) trivial in B₀(2,5).

Datasets are now registered per [[datasets-convention]] (template `dataset-note`, tag `#dataset`, notes in `Datasets/`, files in the repo's `data/`).

### 2026-10-14: T-001 hardness harness and baselines (local runs)
Harness (L0 re-expansion, loop-erased F*, ρ screen/certify, level classification) built on b25 branch `12-hardness-harness`; results in [[hardness-baselines-results]]. Random standard-relator factor words (7,000, L = 2, 3, 3–60 factors): all 7,000 reduce to the empty word under 2.5 reduction (L1 = 0; 95% upper bound 0.043%), D ≤ 0.21. The 820 words: 818 are fixed points, 2 reduce to empty (ρ is not invariant under letter relabelling or inversion). Commutator-product control survives (ρ ≈ 0.89). No remote runs needed. Math statements pending Validator.

### 2026-10-14: T-002 products over the 820 relators (local runs)
Random products of conjugates of the dataset words ([[ds-b25-trivial-2-5reduced-aut8-20261014]]), 7,550 words in 35 cells: 5,221 are L1 (free B(2,5), ρ_min16 ≥ 0.5), 4,012 novel by the refined guard, 0 are L2. Pure-dataset products with 3 or more factors are L1 in 99.7–100% of cases; D stays near 0.02 (max 0.20), so L2 is out of reach for random products. The registered novelty guard misclassified one-factor words (reducer length-neutral rewrites). Results: [[t002-dataset-relator-products-results]].

Decision (owner, 2026-10-14, T-001): any hardness claim uses ρ_min16, the minimum of |R₂.₅| over the 16 letter-relabel/inversion images; screening may use the generated word only, all 16 on finalists. See [[challenge-gen-success-metrics]] § Owner decision 2026-10-14 and the `--min16` option of the harness. Also T-001: D computed by the harness equals the C++ `DehnFunctionScorer` on 7,000/7,000 random words (raw and on F\*).

Decision (owner, 2026-10-14, T-002): novelty guard G2 is the definition of "novel L1" (R is not a conjugate class of a used relator, nor the reducer's output on a single factor c⁻¹rc). G1 is superseded and kept as a historical number. See [[t002-dataset-relator-products-results]] and [[challenge-gen-glossary#novel L1 and the guards G1 and G2]].

### 2026-10-14: T-003 pre-registered (not run)
PatternBoost search over ordered (rᵢ, cᵢ) maximising D on F* under the L1 gate; relator sets R-D (820 dataset words) and R-M (plus 44 standard v⁵); objective variants A (gated D), B (× ρ_screen), C (+ length floor); seeded with T-002 L1 words; 21 remote runs in two stages, awaiting approval. [[t003-gated-dehn-search-2026-10-14]]

## Related material
- [[ds-b25-trivial-2-5reduced-aut8-20261007]]: first registered challenge-gen dataset
- [[project-challenge-gen]]: project profile
- [[B25/_progress]]: B(2,5) progress (the group itself)
- [[andrews-curtis-conjecture]]: candidate phase-2 problem
- [[projects-and-dependencies-convention]]
- [[_synthesis-hard-instance-generation]]
- [[_moc-hard-instance-generation]]
- [[challenge-gen-success-metrics]]
- [[challenge-gen-glossary]]: every project term in one place
