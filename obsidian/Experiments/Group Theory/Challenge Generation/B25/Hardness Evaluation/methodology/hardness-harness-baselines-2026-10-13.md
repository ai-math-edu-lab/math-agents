---
title: hardness-harness-baselines-2026-10-13
hypothesis: "The harness classifies the two baseline sets as predicted: random standard-relator factor words are never L1 (R2.5 = 1, ρ = 0), the 820 kbprog-proved words are L1 with ρ ≈ 1, and the loop-erasure minimiser is sound (expansion unchanged, |F*| ≤ |F|, planted padding removed)."
status: validated
author: asetlearning
date: 2026-10-13
todo: T-001
project: challenge-gen
instance: B(2,5)
experiment_type: hardness-evaluation
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, topic/word-problem, project/challenge-gen, status/pending, experiment, methodology]
---

# Hardness harness and baselines — pre-registration (T-001)

> **Terms.** Project terms are defined once in [[challenge-gen-glossary]] (ρ_min16, screen/certify, aut8 / 16 images, loop erasure, fixed point, pre-check, relator table, controls, cell names, G1/G2 and others); this note links rather than restates them.

> **Phase 1 only.** Written 2026-10-13, before any run beyond reading code. No harness code exists yet. Nothing longer than a smoke test runs until Lead approves this note. TODO item: **T-001** ([[todo-challenge-gen]]). Profile: [[project-challenge-gen]]. Metric definitions: [[challenge-gen-success-metrics]] (not repeated here). Generator context: [[patternboost-generation-methodology]], [[patternboost-generation-results]].

## What this experiment type is

A measuring instrument, not a generator. It takes a word, and where one exists its certificate (a factor word F), and reports four things:
- **L0**: is the certificate valid (independent re-expansion, relators sound, abelianization)?
- **Metric 1**: ρ = |R₂.₅(w)| / |w̄|, how much the heuristic 2.5-reducer shrinks the word.
- **Metric 2**: D = |F*| / |w̄| on the minimised certificate F*.
- the **level** L0 / L1 / L2 (L3 is a family property and is fitted later, not classified per word).

It is validated by running it on two baseline sets whose answer the owner (or the dataset notes) already predicts.

## Why we ran this

The profile's test matrix requires baseline values for any new hardness metric on random (generic) instances. Every later item (T-002 to T-010) will be judged against these numbers. The owner reports that every random factor word 2.5-reduces to the identity; this experiment re-measures that claim with seeds, sizes and counts instead of an anecdote.

## Hypotheses (falsifiable)

Group named in every claim: **free B(2,5)** unless a line says B₀(2,5).

- **H1 (soundness of the instrument).** (a) Loop erasure never changes the freely reduced expansion and never increases the factor count. (b) Planted padding, k blocks `c⁻¹v⁵c · c⁻¹v⁻⁵c` inserted at random positions of a random F, is erased completely: |F*| ≤ |F_original| in 100% of 10³ planted cases. (c) The independent L0 re-expansion agrees with the C++ `RelatorMap.expand` on 100% of all words used. **Falsified by one disagreement.**
- **H2 (random baseline, owner's prediction).** For random factor words over standard relators (cells below), in certify mode: **H2a** every word has R₂.₅(w) = 1 (the owner's claim, ρ = 0); **H2b** no word is L1 (R₂.₅ ≠ 1 and ρ ≥ 0.5). H2a is the stronger claim: it fails if any word survives, even with ρ < 0.5, and the metrics note's threshold rationale rests on it. **Falsified by one surviving word (H2a) or one L1 word (H2b).** Both reported as one-sided Clopper–Pearson 95% bounds per cell (rule of three: 0/1000 gives ≤ 0.30%), plus the ρ distribution of any survivors.
- **H3 (screen versus certify).** Screen mode (shifts {0, 0.5}) never reports a word as L1 that certify mode (all shifts) reduces to 1: false-pass rate of screen = 0 on the random cells. **Falsified by one word.** The reverse direction cannot happen to the harness's detriment, since a screen word that reduces to 1 also reduces under certify.
- **H4 (positive control).** 820/820 words of [[ds-b25-trivial-2-5reduced-aut8-20261007]] are fixed points of the reducer and have ρ_cyc = 1 (cyclic length over cyclically reduced length) and ρ = |cyc(w̄)|/|w̄|; they classify "L1 via external proof" (L0-ext, dataset-note proof by kbprog). **Falsified if any of the 820 is not a fixed point or reduces to 1.**
- **H5 (pre-check).** If the cyclic word has no square ww-window (square of length ≤ n inside the doubled word), `greedy_reduce_cyclic_exhaustive2_5` returns exactly `cyclicallyReduce(w)`. Property test on ≥ 10⁵ words. Code reading supports it (below); the test is the evidence. **Falsified by one counterexample.**
- **H6 (D on random words).** D(F*) < 1 for all random cells, and |F*| = |F| in ≥ 95% of random words (random F contains little freely cancelling padding). No pass/fail claim beyond this; reported as distributions.

Positive/negative structure: random factor words are the negative controls for Metric 1, the 820 are the positive control. A harness that gave ρ = 0 for the 820 would be broken.

## What exists in the code (checked 2026-10-13)

| Need | Exists? | Where (grep-checked) |
|---|---|---|
| 2.5-reduction, three levels | yes | tcgraph `src/greedy_reduction.cpp`: `greedyReduce` (l.291), `greedyReduceCyclic(word, fractions)` (l.299), `greedyReduceCyclicExhaustive` (l.349); Python `tcgraph_ext.greedy_reduce2_5`, `greedy_reduce_cyclic2_5(w, fractions)`, `greedy_reduce_cyclic_exhaustive2_5(w, fractions)` (b25 `cpp/bindings.cpp`), wrappers in b25 `algorithms/word_problem.py` |
| Factor-word type, expansion, JSON | yes | `pattern_boost.FactoredWord`, `RelatorMap.expand`, `to_json` / `from_json` (`bindings_pattern_boost.cpp`); expansion convention is c⁻¹·R·c, freely reduced after each factor (`pb_relator_map.cpp`) |
| D on raw F | yes | `DehnFunctionScorer::scoreSample`, `pb_scoring.cpp:340`: #factors / |expanded, freely reduced| |
| Sampler | yes, with a caveat | `generate_words(rm, cfg, count, seed)`; defaults in `SampleConfig`: 3–8 factors, uniform conjugator length 0–4, `min_expanded_len` 10 |
| Abelianization, cyclic reduction, text-file reduction | yes (scripts) | b25 `experiments/challenge_gen/check_words.py` (untracked, on branch `tools/challenge-gen-datasets`) |
| **Loop erasure (F\*)** | **no** | to write |
| **Independent L0 checker** | **no** | to write |
| **ρ harness (screen/certify, timing, ρ_cyc, caching)** | **no** | to write |
| **Level classification, aggregation, report** | **no** | to write |
| **Built `tcgraph_ext` in the VM** | **no** (not on `PYTHONPATH`, `pybind11` not installed, `cpp/tcgraph` submodule dir empty) | needs the standalone build from `check_words.py`'s README (cmake, pybind11 only, no torch) |

### Findings from reading the code (to be confirmed by tests)

1. **Pre-check ("no power ≥ 2.5 ⇒ `greedyReduce` is a no-op") holds, in the stronger "no square" form.** `greedyReduceImpl` starts each round with `findSquares`; if it is empty the loop `break`s and returns the word unchanged (l.67). A power ≥ 2.5 contains a square, and any rewrite needs `best_power ≥ 2.5` (l.97). `findSquares` compares hashes and then letters, so it is exact. Consequence: "no power ≥ 2.5" alone is not a safe shortcut, because a word can have squares but no power ≥ 2.5 and still be a no-op; "no square" is the safe test. In **linear** mode the pre-check saves nothing, since `findSquares` is the first step anyway. It pays only in **cyclic all-shift** mode: every shift is a length-n window of w·w, so one square scan of w·w (squares of length ≤ n) replaces n scans. Whether to implement it in Python or C++ is decided by the smoke timing. H5 tests it.
2. **Cyclic result is always cyclically reduced.** `greedyReduceCyclic` ends each shift with `cyclicallyReduce()`, and the exhaustive loop returns that. So |R₂.₅(w)| ≤ |cyc(w̄)| ≤ |w̄|, and ρ < 1 for a word that is merely not cyclically reduced, with no rewrite at all. The harness therefore records ρ (the owner's definition, over |w̄|) and ρ_cyc = |R₂.₅|/|cyc(w̄)| (the rewrite effect alone).
3. **Screen mode is a subset of shifts per round**, so it can only miss reductions, never invent them. H3 measures how often it misses.
4. **Sampler is not reproducible from its seed.** `generate_words` seeds an `mt19937` for relator indices and counts, but the conjugator letters come from `Word::random`, which calls libc `rand()` (`src/word.cpp:239`); there is no `srand` anywhere in tcgraph or the b25 bindings (grep-checked). So two runs with the same `seed` can give different conjugators. See Seeds.
5. **`from_json` ignores the stored `word`, `relator_names` and `version`**; it rebuilds only from `relator_indices` and `conjugators`. And the JSON does not contain the relator words: with default names `R<i>`, the indices are meaningless without the RelatorMap that produced them. L0 therefore needs the **relator table** (index → word) as an explicit, hashed input.
6. Beyond this experiment: the 820 words have no stored certificates, so D is undefined for them.

## Problem set

Datasets (sha256 verified before use; a mismatch stops the run):

| Set | Note | File (fork `data/`) | sha256 | Words | Length | Role |
|---|---|---|---|---|---|---|
| 820 | [[ds-b25-trivial-2-5reduced-aut8-20261007]] | `b25_trivial_2_5reduced_unique_aut8_20261007.txt` | `62c6431c…1f11e29` (verified 2026-10-13: yes) | 820 | 32–123 | positive control, L0-ext |


Group status: the 820 are trivial in free B(2,5) (kbprog, per the dataset note).

**Scope change (owner, 2026-10-13, relayed by Lead):** the 118 HWW challenges (reduced [[ds-b25-hww-challenges-2-5reduced-20260319]] and unreduced [[ds-b25-hww-challenges-nonempty-20260930]]) are removed from T-001 entirely. They are known trivial only in B₀(2,5), not in free B(2,5). Finding their certificates (factor representations) is equivalent to solving the open problem, so they are hard by construction and are not hardness baselines. Consequences: former H4(b),(c) dropped; no remote certify jobs for them; the earlier "add unreduced set" question and the greedy-only-origin question are moot.

Random factor words (negative controls), standard relators v⁵ from `build_standard_relators(L, 2)`, all trivial in free B(2,5) (each is a literal 5th power):

| Cell | Relators (L) | Factors | Conjugator length (uniform 0..) | n per seed |
|---|---|---|---|---|
| S1 | L=2 (16) | 3–8 (sampler default) | 4 | 200 |
| S2 | L=2 | 10–20 | 4 | 200 |
| S3 | L=2 | 30–60 | 4 | 200 |
| S4 | L=3 (44) | 3–8 | 4 | 200 |
| S5 | L=3 | 10–20 | 4 | 200 |
| S6 | L=3 | 30–60 | 4 | 200 |
| S7 (sensitivity) | L=3 | 10–20 | 8 | 200 |

`min_expanded_len` = 10 (default) in all cells. 7 cells × 5 seeds × 200 = 7,000 words. The cell grid is fixed now and not tuned after seeing results.

## Components under test

| Component | Repo / version |
|---|---|
| tcgraph reducer, `FactoredWord`, `RelatorMap`, sampler | `tcgraph_agentic@a0d5e92` (main; pinned explicitly, never the stale b25 pin `c093277`) |
| `tcgraph_ext` bindings | `b25_pyproject_agentic@7e50fea` (main), built standalone in the VM |
| New harness (L0, ρ driver, loop erasure, classification, driver) | `b25_pyproject_agentic`, new experiment branch (see Code plan) |

## Configuration

- ρ **screen**: `greedy_reduce2_5(w̄)` then `greedy_reduce_cyclic_exhaustive2_5(·, fractions=[0.0, 0.5])`.
- ρ **certify**: same with `fractions=None` (all shifts).
- Pass for L1: R₂.₅ ≠ empty and ρ ≥ 0.5, certify mode; screen result reported next to it, never in its place.
- D: |F*| / |w̄| with F* by chronological loop erasure on free-reduced prefix words (hash of the free-reduction stack; on a hash hit the prefix content is compared to rule out collisions). Chronological loop erasure gives *a* loop-erased F*, not the minimum over erasure orders, and blocks that cancel only modulo relators stay, so D is an upper bound on area/n on both counts. D_raw = |F|/|w̄| reported next to it.
- Per word record: n = |w̄|, n_cyc, |R₂.₅| (screen, certify), ρ, ρ_cyc, |F|, |F*|, D_raw, D, L0 sub-checks, level, wall-clock per stage, timeout flag, word hash (`sha256` of the letters), seed and cell.

## Termination criteria

- Per word: certify mode capped by a wall-clock timeout (smoke-calibrated; proposed 120 s local, longer remote). A timeout is recorded as `timeout`, never as a pass or a fail, and is counted in every table.
- Experiment done when every word of every set has a recorded status, or is explicitly queued for the remote job.

## Baselines and controls

Negative control: the random cells. Positive control: the 820. Within the harness, the reference implementation of every check is independent of the thing it checks:
- L0 re-expansion: pure Python, written from the definition (c⁻¹ R c, free reduction), compared with C++ `RelatorMap.expand`.
- Loop erasure: compared with a naive O(n²) quadratic reference on small cases.
- The reducer is the unit under study and is taken from tcgraph as it is; its pre-check is tested against it (H5).

## Seeds

- Sampler seeds: **1000001–1000005** (n = 5). They sit far from PatternBoost's `seed + combo·10000 + trial` range (< 300,000), per profile rule 3.
- The brief asks for the **current sampler**, and PatternBoost's initial pool is the C++ `generate_words`, so that is the primary. Conjugators are not controlled by `seed` (finding 4), but libc `rand()` with no `srand` starts from a fixed state, so a **fresh process per (cell, seed)** should reproduce bit for bit on the same host. First smoke step: run `generate_words(seed)` twice in two fresh processes and diff; if they differ, say so and fall back as below.
- **Reproducibility by artifact, not by replay:** every sampled FactoredWord and its expansion is persisted to JSONL (with the relator table hash), and all later analysis reads that file.
- A Python mirror sampler (explicit `random.Random(seed)`, same distributions) is kept **only as a cross-check**: per cell, conjugator-length histogram and expanded-length two-sample Kolmogorov–Smirnov against 1,000 C++ words. It is not used for the reported baseline unless the fresh-process diff fails, in which case Lead decides (question 3).
- Dataset runs are deterministic; no seeds.

## Execution split (local VM versus remote)

| Part | Where | Why |
|---|---|---|
| Harness code, unit tests, H1, H5 (words ≤ 300 letters), `tcgraph_ext` standalone build | **local** | cheap; tcgraph builds locally per the profile |
| Smoke: ≤ 20 words per set, certify timing for n = 100, 500, 2,500 | **local, ≤ 10 min, one process** | calibrates timeouts and the cost model |
| 820 words, ρ screen and certify | local if the smoke shows ≲ 10 min total (n ≤ 123, expected seconds) | small |
| Random cells S1, S4 (short, expected n ≲ 300) screen + certify | local, sequential in one process, capped | small |
| Random cells S2, S3, S5, S6, S7 certify (n up to ~1,000+) | **remote unless the smoke says local fits** | O(n³) worst case; most words are expected to reduce at the first shift, which makes them cheap; the smoke decides |
| 820 words and random cells, as above | see above | the long-word remote certify jobs for the 118 are gone; remote is now only for long random cells, and only if the smoke says they do not fit locally |
| Analysis, tables, plots | local | |

Remote jobs: one `rjob` job per remote part, `[code.submodules."cpp/tcgraph"] sha = "a0d5e92…"`, CPU only (no GPU), 1 job at a time on a single process (the harness runs words sequentially in one process; no per-word processes), host = owner's Mac (M1), expected wall-clock to be estimated from the smoke and sent to Lead before submission. Code is committed on the experiment branch first (Lead commits). Local heavy-process cap respected: one harness process at a time, `pgrep` checked before launch, `timeout` on every run.

## Metric

Per word: level, ρ (screen, certify), ρ_cyc, D (D_raw, D on F*), |F|, |F*|, n, per-stage cost. Per cell or set: counts and rates per level, medians and quartiles of ρ and D, |F| versus |F*|, median and p95 cost. Per report requirement ([[challenge-gen-success-metrics]] § Reporting).

## Statistical treatment

- H2, H3, H4, H1: exact counts with one-sided Clopper–Pearson 95% bounds. No significance test is needed for zero-versus-nonzero claims; the effect is the rate and its bound.
- Descriptive comparison of ρ and D across the 820 and the random cells (Cliff's δ where two samples are compared); no p-value claim, since the sets are not samples of one population.
- Between-seed stability for the random cells: rates per seed are listed; no pooling is hidden.
- **No pre-registered test decides a gain**, because this experiment measures baselines, not an improvement.

## Anti-pattern check

- *Tuning on the test set:* none; the timeouts are set from the smoke on words of a **different** seed (1000000) than the reported ones, and cells are fixed above.
- *Cherry-picked seeds:* all five are listed, every word is recorded, timeouts are counted.
- *Circularity:* the sampler, the L0 checker and the loop eraser are all new or independent of the C++ expansion; the relator table is verified relator-by-relator to be a literal 5th power, not trusted from the generator.
- *Different problem:* the 820 are trivial in free B(2,5) by the dataset's kbprog proof; the harness attributes L0-ext to that proof and does not re-derive it.
- *Necessary versus sufficient:* abelianization passing proves nothing beyond a bug check; L0 is the explicit expansion plus sound relators, and says so in the output.
- *Result-too-good:* ρ = 0 for all random words is the predicted outcome. A 0/N result is cross-checked two ways: the positive control (820 fixed points must come out ρ ≈ 1, so a reducer call that always returns empty would show), and for each random cell a sample of 20 words has the reduction replayed in plain Python (apply `greedy_reduce2_5` once, check the result is shorter and still abelian-trivial) to confirm the empty result is a real reduction and not a binding artefact.

## Cross-verification and the math claims to route

Engineering claims (timings, rates) need no Validator. Math claims to route after the runs: (i) "F* is a valid certificate for the same w̄" is checked by construction by re-expansion; (ii) the statement "every random standard-relator factor word 2.5-reduces to 1" is a heuristic observation about the reducer, not a group-theoretic claim. (iii) The independent soundness argument for the relator table (each relator is a literal 5th power, hence trivial in free B(2,5)) is a short proof; route it to Validator for a verdict. The L0 claim for the 820 depends on the dataset's own kbprog proof and stays attributed to it.

## Code plan

- **Repo / branch:** `b25_pyproject_agentic`, new branch from `main` (`7e50fea`), proposed `hardness-harness` (Lead: the repos use `NN-short-slug`; give me the number or tell me to use a name). Nothing merges to main. The untracked `experiments/challenge_gen/*` scripts belong to branch `tools/challenge-gen-datasets` and are left alone.
- **No tcgraph change planned.** If the smoke shows the Python cyclic pre-check or loop erasure is the bottleneck, a C++ version goes on a tcgraph_agentic branch (separate request, with Developer).
- **New files**, all under `experiments/challenge_gen/hardness/`, each with the Alex Myasnikov header:
  - `certificate.py`: load certificate JSON plus a hashed relator table; independent re-expansion; abelianization; relator-soundness check (cyclically reduced relator is a literal 5th power).
  - `minimise.py`: loop erasure (linear, hash of the free-reduction stack), plus the naive quadratic reference used only in tests.
  - `reduction.py`: ρ in screen and certify modes through `tcgraph_ext`, ρ_cyc, circular-square pre-check, word-hash cache, per-word timeout, stage timing.
  - `classify.py`: L0 / L0-ext / L1 / L2, with the group named in every record.
  - `sampler.py`: C++ sampler wrapper (fresh process per cell and seed, JSONL persistence) plus the Python mirror used for the distribution cross-check.
  - `run_baselines.py`: driver, JSONL output, summary tables.
  - `tests/`: pytest cases for H1 and H5 and for the corner cases below.
- **Tests (run locally):** pytest for the pure-Python parts runs in the VM without torch; tests that need `tcgraph_ext` run against the standalone build. Corner cases: empty certificate, a single factor, conjugator that cancels with the relator, w̄ empty, w̄ not cyclically reduced, a 5-fold relator power, the prefix that returns to the identity in the middle of F.
- **Build:** standalone `cmake --build build --target tcgraph_ext` against `tcgraph_agentic@a0d5e92`; needs `pybind11` in a throwaway venv under the scratchpad (not added to any lockfile). Question 4 asks whether Lead objects.

## Setup

- Runner: `b25_pyproject_agentic:experiments/challenge_gen/hardness/run_baselines.py` (to be written).
- Command (planned): `timeout <cap> python -I -m experiments.challenge_gen.hardness.run_baselines --set <name> --mode screen|certify --out runs/challenge-gen/hardness/<timestamp>/`.
- Outputs: `~/Research/challenge-gen/runs/…` per the profile; remote runs by rjob job id.

### Provenance record (filled at run time)

- Code SHAs: `b25_pyproject_agentic@<experiment-branch sha>`, `tcgraph_agentic@a0d5e92`, `remote-jobs@<sha>`.
- Lock hash: `uv.lock` (b25) for remote runs; standalone local build records the compiler, cmake and pybind11 versions.
- Input hashes: the 820-word dataset file (sha256), the relator tables (sha256 of L=2 and L=3 tables), sampler config.
- Seeds: 1000001–1000005 (plus 1000000 for smoke calibration only).
- Host: VM (2 CPUs, ~3 GB) or rjob host + job id; wall-clock per set.

## Results — Baselines
See [[hardness-baselines-results]] (T-001, run 2026-10-14, all local). H1a, H1c, H2, H3, H5 held; H1b held in the run but not structurally; H4 falsified (818/820); H6 partly falsified.

## Final verdict
`#status/validated` for the engineering claims; math statements routed to Validator (`#status/conjectured` until a verdict).

## Open questions for Lead
See the hand-off message (also recorded in [[Agents/asetlearning/Experimenter/log]]).
