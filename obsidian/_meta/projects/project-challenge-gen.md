---
title: Project profile — challenge-gen
project: challenge-gen
owner: asetlearning
repos:
  - "[[dep-b25-pyproject-agentic]] — main experimental repo (Python/uv): PatternBoost generator, configs, sweeps, dashboards; all new experimental code on branches, merge to main only with owner approval"
  - "[[dep-tcgraph-agentic]] — C++ core (submodule cpp/tcgraph of b25): Word, TC graph, 2.5-reduction, pattern_boost engine; exposed to Python via tcgraph_ext"
dependencies:
  - "[[dep-tcgraph-agentic]] — may-modify (on branches; bump the b25 submodule pin to the right tcgraph_agentic commit when bindings change)"
  - "[[dep-gap]] — read-only; oracle and validator (word problem in finite / polycyclic quotients, e.g. B₀(2,5) via ANUPQ)"
  - "[[dep-remote-jobs]] — infrastructure; every remote (GPU / long / >2 GB) run goes through rjob (see Execution policy)"
  - "[[dep-kbmag]] — read-only; validator (Knuth-Bendix / rewriting), run as the GAP package or standalone kbprog — an independent path from GAP's word problem"
build: "b25: git submodule init && git config submodule.cpp/tcgraph.url https://github.com/asetlearning/tcgraph_agentic.git && git submodule update && uv sync  (C++ rebuild: uv sync --reinstall-package b25-pyproject). tcgraph standalone: cmake -B build && cmake --build build"
test: "uv run pytest tests/ -v (b25); cd build && ctest (tcgraph). Plus, for any generator change: certificate check on a regression sample (see Test matrix)"
smoke: "uv run python -m experiments.pattern_boost.pattern_boost_main run configs/pattern_boost_smoke.yaml — NOTE: its challenges path is hard-coded to /media/psf/b25_pyproject/...; point it at a local sample first"
lint: "C++: clang-format -style=file (tcgraph CODE_GUIDELINES.md); Python: none configured"
languages: [Python 3.12, C++20, GAP]
run_pattern: "remote (default for real runs): rjob submit <job.toml> → rjob wait <id> → rjob fetch <id> (examples: ~/Research/remote-jobs/examples/pb-smoke). Local (smoke only): timeout <cap> uv run python -m experiments.pattern_boost.pattern_boost_main run|sweep configs/<x>.yaml   (baseline challenges: experiments.pattern_boost.experiment_local_search sample configs/generate_sample.yaml)"
runs_dir: "~/Research/challenge-gen/runs/<rjob-job-id>/ (outputs/, provenance.json, manifest.json, log.txt); full copy stays on the host in ~gpuworker/rjob/jobs/<id>/ until cleanup. Inside a run, b25 layout: <output_dir>/run.jsonl, run.matches.jsonl, iter_NNNN/; sweeps <output_dir>/sweep_<ts>/combo_NNNN_<slug>/trial_NNNN/ + sweep_summary.json. Legacy sweeps: data/pattern_boost_experiments/pb_sweep/ (outside git)"
provenance_fields: [rjob job id + host (provenance.json records the next three automatically), b25 git SHA, tcgraph_agentic SHA actually checked out in cpp/tcgraph, uv.lock hash, config YAML (as run), relator source + hash, challenge file + hash, sweep/run seeds, torch/transformers versions, GAP version + kbmag build if validation ran, certificate (FactoredWord JSON) format version, host (CPU/GPU/RAM), wall-clock — NOTE: b25 itself logs only the config; runs through rjob get SHAs, uv.lock hash, input hashes, host and device in provenance.json]
heavy_processes: [pattern_boost_main, pb.local_search, "2.5-power reduction of long words (tcgraph greedyReduce*; also inside scorers with reduce2_5)", attempt_to_decide_if_trivial, gap, kbprog]
protected_interfaces:
  - "FactoredWord JSON {word, relator_indices, relator_names, conjugators, version} — the triviality certificate"
  - "relator JSON schema {\"R1\": {version, word, details?}}"
  - "tokenizer stream format [BOS] ([REL_i] ([CONJ_±k]+ | [CONJ_EMPTY]) [SEP])+ [EOS] — trained checkpoints depend on it"
  - "sweep_summary.json + run.matches.jsonl layout — dashboard and vault results tables read them"
  - "tcgraph_ext binding API — b25 scripts depend on it"
hot_paths:
  - "LocalSearcher::search — O(beam × ~250+ neighbours × steps × score cost); no visited set; neighbours expanded twice"
  - "scorers with reduce2_5 / length_range reduce_before_scoring — greedyReduceCyclicExhaustive, findSquares O(n²)"
  - "edit-distance scorer — O(|w|·|c|) per challenge"
vault_docs:
  components: TBD
  code_reviews: TBD
  math_validation: Architecture/Mixer/Documentation/Math Validation/   # shared location until the project has its own
  experiments: Experiments/Group Theory/Challenge Generation/
  progress: Experiments/Group Theory/Challenge Generation/_progress.md
  todo: Agents/<handle>/Lead/todo/todo-challenge-gen.md   # private, gitignored — [[project-todo-convention]]
  todo_published: Experiments/Group Theory/Challenge Generation/_todo-challenge-gen.md
  datasets: Datasets/Group Theory/B25/   # files in the fork's data/ (never the original math-agents), per [[datasets-convention]]
tags: [meta, convention, project/challenge-gen]
---

# Project profile — challenge-gen

## Goal

**Challenge generation.** Build ways to generate *hard* problem instances that come with a proof that they have a solution. The instances serve as benchmarks and training sets for new search algorithms, including ML, LLM and RL approaches. Phase 1 is **hard trivial words ("challenges") in B(2,5)**. If that works, the project extends to other problems, e.g. searching for counterexamples to Andrews–Curtis. The standing state is in [[Challenge Generation/_progress|the progress note]].

## Difficulty metrics and success criteria (owner, 2026-10-05)

Full definitions are in [[challenge-gen-success-metrics]]. In short, generate words **provably trivial in free B(2,5)** (certificate or construction) that are **hard to decide**:
- **Metric 1, 2.5-reduction resistance.** ρ = |R₂.₅(w)| / |w̄|, where R₂.₅ is greedy then cyclic-exhaustive 2.5 reduction. Pass: R₂.₅(w) ≠ 1 and ρ ≥ 0.5. Every random factor word reduces to 1 (owner's experiments), so this separates hard from generic. The reduction costs O(n²) to O(n³), so screen with shifts {0, 0.5} on the pool and certify with all shifts on finalists. Never run it per neighbour.
- **Metric 2, Dehn proxy.** D = |F*| / |w̄| on the **minimised** certificate F*: freely cancelling factor blocks are removed by loop erasure. It is an upper bound on area, and it counts only for words passing Metric 1. Good: D ≥ 1. Great: a family with |F*| ≈ c·n², i.e. quadratic area.
- **Success levels:** L0 valid (certified), L1 hard (Metric 1), L2 L1 + D ≥ 1, L3 quadratic family.
- **Similarity** to the 150 challenge words is now secondary and optional.

## The search problem (owner, 2026-10-14) — the crucial part

Every generator in this project is a **search over factor words**, and the goal of the search is to **maximise D** while keeping the word hard to reduce.

**Search space.** A candidate is an *ordered* sequence of N pairs

$$F = \big((r_1, c_1), (r_2, c_2), \dots, (r_N, c_N)\big), \qquad F \mapsto \prod_{i=1}^{N} r_i^{\,c_i} = \prod_{i=1}^{N} c_i^{-1} r_i\, c_i ,$$

- rᵢ ∈ R^± : a relator from the chosen relator set R, or its inverse;
- cᵢ ∈ F(a,b) : an arbitrary freely reduced conjugator;
- N : variable.

All three choices are search variables: **which relators**, **which conjugators**, and **in what order**. The factors do not commute, so reordering the same pairs gives a different word. Every such F lies in the normal closure ⟨⟨R⟩⟩, so its expansion is trivial in B(2,5) by construction (given relators trivial in free B(2,5)); the search never has to prove triviality.

**Objective.** Let w = the freely reduced expansion of F, and F* the minimised certificate (freely cancelling factor blocks removed, see [[challenge-gen-success-metrics]]). Maximise

$$D(F) = \frac{|F^*|}{|w|} = \frac{N^*}{|w|}$$

**subject to** the L1 gate: R₂.₅(w) ≠ 1 and ρ_min16(w) ≥ 0.5 ([[challenge-gen-glossary]]). D is large only when the conjugated factors **cancel heavily against each other under free reduction**: many relator cells, short boundary word. With random choices there is almost no cancellation, so |w| ≈ Σ(|rᵢ| + 2|cᵢ|) and D ≈ 1/(mean factor length) — this is why T-000 to T-002 never approached D ≥ 1. Finding pairs and orders that cancel heavily while the result still resists 2.5-reduction is what makes the problem hard.

**What must not count as progress.** Padding that cancels to nothing — e.g. adjacent factors r^c (r^c)⁻¹ — is removed by the F* minimisation, so it cannot inflate D. Shrinking |w| by making the word easy is blocked by the L1 gate (the 2026-07-23 Dehn run drifted to 32-letter words with D = 0.34 when the gate was missing).

**Search parameters** (record all of them in every run):

| Parameter | Meaning | Examples so far |
|---|---|---|
| Relator set R | Where the rᵢ come from; must be certified trivial in free B(2,5) | standard v⁵ with \|v\| ≤ L (L = 1, 2, 3); the 820 dataset words [[ds-b25-trivial-2-5reduced-aut8-20261014]]; mixes |
| N range | Number of factors (before and after minimisation) | 1–60 (T-001/T-002) |
| Conjugator bound | Maximum \|cᵢ\| and its distribution | uniform 0..8, 0..20 |
| Word-length bounds | Floor/cap on \|w\| (blocks the "short and easy" drift) | `min_expanded_len`, `length_range` |
| Move set | Local-search moves on F | replace rᵢ; mutate cᵢ; insert / delete a factor; *reorder* (swap adjacent factors) |
| Search strategy | How candidates are proposed | random sampling; beam local search; PatternBoost model; later RL / evolution |
| Objective and gate | Score the search maximises | D with the L1 gate (screen ρ on the pool, ρ_min16 on finalists) |

## Idea & motivation

Many hard open problems in mathematics reduce to search problems. Often the task is to find a connection between two vertices in a search space, or a path in a large (possibly infinite) group. For open problems it is usually not known whether such a path exists: the instances in question are potential counterexamples. So if we want to develop new algorithms, in particular with machine learning (LLMs, RL, …), how do we test their performance, and where do training sets come from?

The counterexamples themselves are one option. But there are usually few of them, and any real progress on them is almost equivalent to solving the problem. That leaves very little signal for evaluation and training.

Random samples are another option, generated by some procedure or picked as random vertices of the search-space graph. Here a solution is known to exist, so algorithm performance can be measured. Random instances are a good baseline. However, most random generation procedures produce *generic* (uniformly distributed) instances. In many settings, solving a random instance is known to be much easier than solving the special "hard" instances we care about, and those are very rare.

We need a way to sample instances that share properties with the hard ones. This is not trivial. A "hard" instance is one where checking the required property is as hard as solving the problem on that instance. So the generation process must be organised so that **the proof of the property is part of the process itself**: it can be attached to the instance, or the process reversed, as evidence.

## Problem instances

| Phase | Problem | Instance property | Status |
|---|---|---|---|
| 1 | B(2,5): free Burnside group, 2 generators, exponent 5 | word is trivial in B(2,5), and hard to reduce | active |
| later (candidate) | Andrews–Curtis conjecture ([[andrews-curtis-conjecture]]) | balanced presentation is AC-trivial, and hard to trivialise | not started |
| later (candidate) | other search-reducible open problems | TBD | not started |

For B(2,5), triviality in the restricted quotient B₀(2,5) is **necessary but not sufficient** for triviality in the free B(2,5) (see [[B25/_progress]]). A certificate must prove triviality in the group the experiment claims.

**Registered datasets** ([[datasets-convention]]):
- [[ds-b25-hww-challenges-nonempty-20260930]]: the 118 HWW challenges (non-empty, freely reduced, not 2.5-reduced). Trivial in B₀(2,5), replicated; open in B(2,5).
- [[ds-b25-hww-challenges-2-5reduced-20260319]]: the same 118 after greedy 2.5-reduction (≈32% shorter). Trivial in B₀(2,5); validated 2026-10-07.
- [[ds-b25-trivial-2-5reduced-aut8-20261007]]: 820 candidate trivial words, 2.5-reduced, unique up to rotation, inversion and the 8 letter automorphisms. Proved trivial in B(2,5) by Knuth–Bendix reduction (kbprog on `b25_full`), also trivial in B₀(2,5); validated 2026-10-07. No per-word certificates stored.

## Components under test

See *Current implementation* below. Record the component actually used in each experiment: the scorer type, the relator source, and the local-search strategy.

## Current implementation — PatternBoost generator (B(2,5))

Design and results: [[B25/PatternBoost Generation/_type|PatternBoost Generation]] (methodology, data, results). The loop follows [[charton-2024-patternboost]]:

```
initial sample (C++ generator: random products of conjugates of relators)
   → score → keep top max_pool_size                         ┐
   → train GPT-2 on factor-word token streams  (model.py)    │ repeat
   → sample n_samples streams → decode to FactoredWords      │ num_iterations
   → C++ beam local search per candidate (LocalSearcher)     │ (stop on match)
   → score → merge top_k into pool                           ┘
```

| Component | Where |
|---|---|
| Loop | `b25:algorithms/pattern_boost/workflow.py:run_pattern_boost` |
| Model | `model.py` (GPT-2) |
| Token stream | `tokenizer.py` |
| Scorers | `common.py:make_scorer` → C++ `pb_scoring` |
| Relator sets | `relators.py` + C++ `pb_relator_map` |
| Local search | C++ `pb_local_search`. Moves: relator swap, conjugator mutation (deterministic edit-distance-1 or random), factor insertion, factor deletion |
| Sweeps and dashboard | `sweep.py`, `experiments/dashboards/sweep_dashboard.py` |

## Certificate model

The certificate is the **factor word**: w = ∏ cᵢ⁻¹ R[idxᵢ] cᵢ. It is checked by re-expanding it and comparing with w, which is cheap and needs no word-problem solver. It is sound **only if every relator in the RelatorMap is trivial in the group claimed**:
- **Standard relators** v⁵ (|v| ≤ L) are trivial in free B(2,5). This is safe.
- **File relators** (`relators.relators_file`, e.g. 2.5-reduced shortlex KB rules) and **BPE-token relators** (g⁵ for compressed generators g) are trusted without verification. They need their own provenance, and they must be certified trivial in free B(2,5), not just in B₀(2,5), before the "certified in free B(2,5)" claim holds.
- The abelianization check (exponent sums ≡ 0 mod 5) is a cheap necessary condition, used to catch bugs.

The model never emits letters directly, so malformed generations decode to `None` and are dropped. Every candidate in the pool is a product of conjugates by construction.

## Execution policy — local VM vs remote (owner, 2026-10-05)

The agents' VM is restricted: 2 CPUs, about 3 GB RAM, no GPU. Experiments are therefore split, and the plan for each experiment says which part runs where.

| Where | What |
|---|---|
| **Local (VM)** | Code generation and edits, compiling, unit tests (`pytest`, `ctest`), smoke runs (≲ 10 min, ≲ 2 GB), analysis of fetched results, cheap checks on small sets (certificate re-expansion, abelianization, ρ/D on up to a few hundred short words) |
| **Remote ([[dep-remote-jobs]])** | Anything needing a GPU (PatternBoost training and sampling, sweeps); anything expected to run > 30 min, use > 2 GB, or want > 2 cores (2.5-reduction in certify mode on large or long-word sets, TC experiments, local-search sweeps) |

- **Host.** For now it is the owner's Mac (M1, 8 cores, 64 GB, MPS), with 1 GPU slot and 7 CPU slots. Later hosts are Linux/CUDA servers using a container backend. Docker is not used on the Mac, because it has no MPS inside containers.
- **Code reaches the host only as committed SHAs** from an experiment branch; dirty trees are refused. The tcgraph submodule commit is explicit per job, and the `[code.submodules."cpp/tcgraph"]` override sets it when the b25 pin is stale.
- **Each result directory is cited by its job id.** `provenance.json` supplies most of the provenance fields above.

## Agent assignment and Experimenter rules

- **Who runs experiments.** The general Experimenter, or a spawned **`Experimenter-ChallengeGen`** terminal ([[canvas-setup]] Step 6), runs challenge-gen experiments with this profile. It is not Experimenter-B25: that role owns the B(2,5) finiteness program in `Burnside Group/B25/`, and challenge-gen lives in `Experiments/Group Theory/Challenge Generation/`.
- **Rules for every challenge-gen run:**
  1. **Remote by default for PatternBoost.** Follow the execution policy above and the remote-jobs workflow in [[experimenter]].
  2. **Pin tcgraph explicitly** in every job (`[code.submodules."cpp/tcgraph"]`). Since 2026-10-14 (b25 PR #3, merge `9eb98c6`) b25 main pins tcgraph `1b52b4d` (seeded sampler, T-011), which builds; still pin explicitly so the job records the SHA.
  3. **Seeds must not collide.** Target-sampling seeds must differ from PatternBoost's pool seeds; in sweeps these are `seed + combo·10000 + trial`. Otherwise targets sit in the initial pool and the run measures nothing.
  4. **Same-distribution targets test steering, not hardness.** Any hardness claim uses the metrics in [[challenge-gen-success-metrics]]: ρ in certify mode, and D on the minimised certificate F*. Report baselines on random factor words from the same sampler.
  5. **L0 before anything else.** Re-expand stored certificates independently, and use only standard relators or relators certified in free B(2,5).
  6. **Name the group.** Never call a word "trivial in B(2,5)" on B₀(2,5) or finite-quotient evidence. Route such claims to Validator.
  7. **Record the scorer and full config.** The 2026-05 baseline lost its scorer because `pattern_boost_sweep_1.yaml` was never kept. Keep the job directory, which rjob also records by hash.
  8. **Tests are not results.** Clean up test and aborted runs, and keep them out of results notes.
  9. **Define every term once.** A new metric, level, guard, mode or naming scheme is defined in the same change that introduces it: project-wide terms in [[challenge-gen-glossary]] (one line + origin + link; the owner's metric definitions stay normative in [[challenge-gen-success-metrics]]), type-local terms in the `## Terms` section of the experiment type's `_type.md`. Reports to Lead use only defined terms or define them inline. Lead checks this before relaying a report to the owner.

## Developer notes

- **Where builds and tests run.**
  - **tcgraph:** builds and tests locally (`cmake -B build && cmake --build build -j`, then `ctest`), C++ only.
  - **b25:** its full build (`uv sync`) and `pytest` must run **remotely**. On linux/aarch64 the locked torch pulls several GB of NVIDIA wheels, which the VM cannot hold.
  - Use an rjob job modelled on `~/Research/remote-jobs/examples/b25-build-tcgraph-main`, with `argv = ["python", "-m", "pytest", "tests/", "-v"]` for tests. See [[developer]] § Builds and tests that cannot run locally.
- **Changes spanning b25 and tcgraph** (a public C++ signature used by the bindings, a new scorer, etc.):
  1. tcgraph change on a tcgraph_agentic branch, with a C++ test and local `ctest`.
  2. The matching change in b25 `cpp/bindings*.cpp` (and the Python callers) on a b25 branch.
  3. A remote build and test job of the b25 branch with `[code.submodules."cpp/tcgraph"] sha = "<tcgraph branch>"`.
  4. After both merges (owner approval), bump b25's submodule pin to the merged tcgraph commit.
  - The committed `.gitmodules` URL (gt-computations/tcgraph) is unreachable: use the local `submodule.cpp/tcgraph.url` override ([[dep-b25-pyproject-agentic]]). Fixing the URL needs owner approval.
- **Branch naming.** These repos (b25_pyproject_agentic, tcgraph_agentic, remote-jobs) use `NN-short-slug` (issue-numbered), or `docs/…` / `fix/…`. Nothing merges to `main` without the owner's approval.
- **Changes to `remote-jobs`** go live only after the owner re-runs `host/install.sh` on the Mac. The job contract and the SSH verb boundary are protected; see [[dep-remote-jobs]].

## Known issues (as of 2026-10-05; documented, not fixed)
- **Submodule.** b25's `.gitmodules` points `cpp/tcgraph` at `gt-computations/tcgraph`, not `asetlearning/tcgraph_agentic`. Pin fixed 2026-10-14: b25 main now pins `1b52b4d` (was `c09327705a`, which predated the scorers b25 binds). The URL still needs the local override; see [[dep-b25-pyproject-agentic]].
- **tcgraph_agentic main** fails to build `test_pb_local_search`, which uses the removed `scoreWord`; see [[dep-tcgraph-agentic]].
- **No provenance or seeds** are logged: no SHAs or data hashes, and model init and training are unseeded. The C++ factor-word sampler is seeded since 2026-10-14 (T-011; reproducible per standard library, Linux vs macOS may differ). Data files are not in git.
- **Pool merge** keeps the newest entries, not the best, by default. Fixed opt-in 2026-10-14 (b25 PR #6, merge 5e900ee): set `workflow.pool_merge: score` to keep the top entries by their entry-time (gated) score; required for any gated objective (T-003 job 1 lost all but 18 of 2,000 L1 passers in 3 iterations with the default). Sweep-level logs land in trial logs.
- **Which group.** "Match" means exact cyclic equality with a target and says nothing about hardness. The challenge words are known trivial only in B₀(2,5).

## Core requirement — certificates

Every generated instance ships with a **certificate**, e.g. a generation trace or an explicit derivation from relators, from which the property can be checked mechanically and cheaply. Validator checks certificates. Where possible, it also cross-checks the property through a path independent of the generator, such as GAP's word problem in a finite quotient or kbmag rewriting, and records which path it used.

## Test matrix

| Change kind | Required |
|---|---|
| New or changed generator | certificate check on a regression sample (all certificates verify) + independent property check on a subsample (GAP/B₀ or kbmag) |
| New or changed certificate format | Validator review of the format's soundness + re-verification of existing benchmark sets |
| New hardness metric | documented definition + baseline values on random (generic) instances and on the 150 human challenge words |

## Protected interfaces — why each one exists

- **Challenge + certificate format.** Benchmarks, training pipelines and validators all consume it. Once defined, changes need a version bump and Lead approval.
- **`~/Research/challenge-gen/runs/<job-id>/` layout** (from [[dep-remote-jobs]]). Results tables and the progress note link into it by job id.

## Experiment template fields

In [[experiment]], also fill:
- **Target property**: what each generated instance is claimed to satisfy (e.g. "trivial in free B(2,5)").
- **Group computed in**: free B(2,5), restricted B₀(2,5), or a named finite quotient. Mandatory for Burnside instances.
- **Generation procedure**: the algorithm and parameters, plus the seed.
- **Certificate type**: what is attached and how it is checked.
- **Hardness metric(s)**: how "hard" is measured, e.g. performance of reference solvers or length/structure statistics, and the baseline it is compared with.

## Related material
- [[myasnikov-ushakov-2011-random-van-kampen]]: theory anchor for the metrics: random diagrams are hyperbolic and shallow
- [[projects-and-dependencies-convention]]
- [[Challenge Generation/_progress]]: progress note
- [[project-b25]]: sibling project on B(2,5) itself
- [[B25/_progress]]
- [[dep-b25-pyproject-agentic]], [[dep-tcgraph-agentic]]: code
- [[dep-gap]], [[dep-kbmag]]
- [[B25/PatternBoost Generation/_type|PatternBoost Generation]]: first experiment type
- [[challenge-gen-success-metrics]]: difficulty metrics and success levels
- [[challenge-gen-glossary]]: project glossary (all terms, one place)
- [[andrews-curtis-conjecture]]
- [[_synthesis-hard-instance-generation]]: literature scan of 2026-10-05 (12 papers)
- [[_moc-hard-instance-generation]]: reading path
- [[Concepts/certified-instance-generation]]: concept hub for the core requirement
