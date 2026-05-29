---
tags: [meta, taxonomy]
---

# Tag Taxonomy — Math vault

The Math vault is **multi-user** (you + colleagues) and **multi-domain** (group theory is the current focus, but colleagues bring AI, CS, and methodology papers from their own work). Tags are the cross-cutting index that scales the vault to thousands of papers while keeping retrieval fast and the knowledge graph connected.

**Six tag axes.** A note carries 5+ tags from the mandatory axes, plus content-type and risk markers as relevant. Bases queries combine axes for filtered views.

## Vault language

**All notes are in English.** This includes paper summaries of non-English sources. Non-English source papers get their abstract and quotes translated to English in the body; mark translated text with `[trans.]`. The original-language text is **not** preserved in the vault — `language:` frontmatter records the source language for filtering, and readers needing the original follow the source URL. See `_templates/paper-summary.md` for full convention.

## Tag minimum per note

Every note carries at minimum:

1. One `#agent/*` — who wrote it (AI agent role or human)
2. One `#user/*` — which human contributor it belongs to
3. One `#domain/*` — broad field
4. **One-to-many `#topic/*`** — fine-grained subjects within the domain. Typically 4–10. No upper bound. Substance test: every tag must answer yes to "would I want this paper to surface when searching for this topic?" If the paper only mentions a topic in passing, don't tag it.
5. One `#status/*` — lifecycle

Plus mandatory in frontmatter: `author: <handle>` (the human who owns the note).

Optional but encouraged: `#project/*` (when the note belongs to a named project), content-type tags (`#paper`, `#experiment`, etc.), risk markers.

---

## Axis 1 — `#agent/*` (who wrote it)

- `#agent/lead`
- `#agent/dev`
- `#agent/research`
- `#agent/exp` — general Experimenter
- `#agent/exp-b25` — B(2,5) specialist Experimenter
- `#agent/validator`
- `#agent/human` — written by a human directly, no AI involvement

If a note was AI-written but human-tasked, `#agent/*` records the AI role and `#user/*` records the human who owns it.

## Axis 2 — `#user/*` (which human contributor)

Register a new tag for each new contributor as they join. Every note carries exactly one `#user/*` — the human who owns or commissioned it.

Registered handles:
- `#user/maumayma` — Maria Matveeva (see [[People/maumayma]])

Add new colleagues here as they join. Matching `author: <handle>` frontmatter is queried by Bases for grouping/filtering.

## Axis 3 — `#domain/*` (broad field)

Pick exactly one per note. **Don't add new domain values without registering them here first.** Researcher (with restructure authority) may extend this list when a colleague brings papers from a new field — register first, then tag.

Currently registered:
- `#domain/group-theory` — Burnside groups, KBMAG, finitely-presented groups, word problems, combinatorial algebra
- `#domain/ai` — AI/ML applied to mathematics, automated theorem proving, RL-guided search, learned heuristics
- `#domain/cs` — computer science: algorithms-as-implementation, systems, infrastructure, code-focused papers
- `#domain/methodology` — experimental methodology, benchmark design, statistical analysis, reproducibility (domain-neutral)

When a paper spans two domains (e.g. AI applied to group theory), pick the **primary** one — the field whose methodology the paper contributes to — and link to the other via wikilink. Don't double-tag domains.

## Axis 4 — `#topic/*` (fine-grained subjects, multi-tag)

This is the **connection-graph axis.** Topics are what the paper actually engages with — concrete subjects, named techniques, specific problems. Topics enable cross-domain retrieval ("all papers on `#topic/proof-search` regardless of `#domain/*`") and graph clustering.

Rules:
- **Typically 4–10 per paper.** No upper bound when all tags are substantive.
- **Substance test**: every tag must answer yes to "would I want this paper to surface when searching for this topic?" Passing mentions don't qualify.
- **Naming convention**: lowercase, hyphenated, specific. `#topic/burnside-groups` not `#topic/groups`. `#topic/buchberger-algorithm` not `#topic/algorithm`.
- **Reuse before invent.** Before creating a new topic, scan existing topic tags (Obsidian's tag pane). New topics earn their place when 2+ papers share them.

Initial seed (will grow as papers arrive):
- `#topic/burnside` — Burnside groups in general
- `#topic/b25` — B(2,5) specifically
- `#topic/word-problem` — word-problem decidability + algorithms
- `#topic/mixer` — algorithm-cooperation framework (algo_mixing-specific subject)
- `#topic/knuth-bendix` — KB completion and orderings
- `#topic/kbmag` — KBMAG-specific work
- `#topic/proof-search` — search-based theorem proving (any methodology)
- `#topic/coset-enumeration` — Todd-Coxeter and variants
- `#topic/cayley-table-closure` — Kuznetsov's algorithm family computing $K_s(m,n) = (P_s, A_s, T_s, C_s)$ by iterative Cayley-table closure: build the minimal-word set $P_s$ length-by-length, detect new relations from row collisions in $T_s$, derive a finiteness/infiniteness criterion from the fixed point $K_s = K_{s+1}$. Distinct from Knuth-Bendix and coset enumeration.
- `#topic/restricted-burnside` — the restricted Burnside groups $B_0(m,n)$ (the largest finite quotient of the free Burnside group $B(m,n)$; order computed for specific cases, e.g. $|B_0(2,5)| = 5^{34}$). Tag when a paper engages specifically with $B_0$ vs $B$ (free), Hall's restricted-Burnside theorem, or the $B_0$ vs $B$ comparison. Substance test: the paper must say something non-trivial about the restricted vs free distinction.
- `#topic/growth-functions` — Cayley graph growth functions $f(k) = |B_k|$ for group quotient towers, sphere/ball growth, growth rates, Cayley graph diameters $D_{A_r}(G)$. Tag when a paper computes or studies the word-length distribution of group elements or growth properties of a group.
- `#topic/cayley-graphs` — Cayley graph construction, structural properties (diameter, girth, connectivity, spectrum), and algorithmic applications for finite and infinite groups. Tag when a paper's primary object is the Cayley graph geometry or when graph-diameter arguments drive key results.
- `#topic/finite-group-enumeration` — computational enumeration of elements, conjugacy classes, subgroups, or structural invariants (center, commutator subgroups) of finite groups, typically via Hall polynomial arithmetic or permutation representations. Tag when the paper's core contribution is a computational result about the structure of a specific finite group.
- `#topic/rewriting-systems` — term rewriting systems for groups: confluent and irreducible rewriting systems (string rewriting systems / Thue systems), KB completion, and algorithms for computing or manipulating rewriting systems in finite or infinite groups. Substance test: paper must engage with rewriting systems as a primary concept, not just mention KB in passing.
- `#topic/center-of-group` — center $Z(G)$ of a group, central elements, centralizers $C_G(x)$, and centralizer-based structural arguments (automorphism centralizers, involutive automorphisms). Tag when the paper computes or characterizes the center or a centralizer as a primary result.

### AI-in-math topics (registered 2026-05-28 for Research/AI in Math/ batch)

- `#topic/automated-theorem-proving` — formal theorem proving systems (any methodology: LLM, search, symbolic, hybrid); the overarching field. Tag when the paper's primary contribution is a system that constructs or verifies formal proofs. Distinct from `#topic/proof-search` (which covers the search algorithm aspect) — this tag covers the full ATP system including training, architecture, and benchmark evaluation.
- `#topic/llm-prover` — language models applied to proof generation: LLM sampling over proof tactics or proof steps, fine-tuned LLMs for formal math, LLMs as the policy in proof search. Substance test: the paper must contribute a new LLM-based prover or a new training method for LLM provers.
- `#topic/autoformalization` — translation of informal mathematical statements or proofs to formal specifications (Lean, Isabelle, Coq, etc.): neural autoformalization, LLM-based translation, informal-to-formal pipelines. Tag when formalization of natural-language math is the paper's primary contribution.
- `#topic/agentic-reasoning` — agentic or multi-step reasoning systems for math: LLM agents that decompose problems into subgoals, maintain state across proof steps, call external tools (verifiers, symbolic engines), or self-correct based on feedback. Tag when the agent architecture (not just the model) is a primary contribution.
- `#topic/neuro-symbolic` — hybrid neural-symbolic systems: combining a neural component (language model, embedding, classifier) with a symbolic engine (geometry prover, SAT solver, CAS) in a tightly-integrated pipeline where both components are necessary. Substance test: the paper must use both components non-trivially — pure LLM calling a calculator is not neuro-symbolic; AlphaGeometry's iterative LLM-aux + symbolic-deduction loop is.
- `#topic/lean` — Lean proof assistant (Lean 3 or Lean 4) as the target formalization language or the development environment. Tag when Lean is the primary proof assistant the paper targets, not just mentioned as context. Closely related: `#topic/automated-theorem-proving`, `#topic/llm-prover`.
- `#topic/isabelle` — Isabelle/HOL as the target formalization language. Tag when Isabelle is the primary proof assistant. Distinct from `#topic/lean` (different systems with different type theories).
- `#topic/monte-carlo-tree-search` — MCTS or MCTS-inspired tree search algorithms applied to proof search, game-playing, or combinatorial optimization. Tag when MCTS is a primary algorithmic component, not just cited as background. Will appear in both sub-area A (HyperTree Proof Search) and sub-area B (RL-guided proof search).
- `#topic/reinforcement-learning` — reinforcement learning as the primary training or optimization methodology: policy gradients, value-function learning, PPO, GRPO, reward modeling, or RL-from-verifier-feedback. Tag when RL is the paper's core contribution, not just a minor component. Substance test: the paper must be primarily about how RL enables or improves a mathematical task.
- `#topic/value-network` — neural value functions that estimate the probability of success from a given proof state or search state; typically trained via RL or self-play. Tag when the value network architecture is a primary contribution or when the paper evaluates value networks specifically. Related: `#topic/monte-carlo-tree-search` (value networks typically guide MCTS).
- `#topic/process-reward-model` — reward models that evaluate the correctness or quality of each step of a multi-step mathematical reasoning chain, rather than only the final answer (outcome reward model / ORM). PRMs are used for RL training (step-level PPO) and inference-time verification (reranking). Tag when PRM design, training, or evaluation is the paper's primary contribution.

### ML-for-math topics (registered 2026-05-28 for Research/AI in Math/ML/ batch)

- `#topic/symbolic-regression` — methods that search for mathematical expressions (equations, formulas) fitting observed data or satisfying formal constraints; includes genetic algorithms, neural-guided regression, sparse identification. Tag when the paper's primary contribution is discovering or fitting symbolic mathematical expressions.
- `#topic/premise-selection` — selecting relevant premises (lemmas, axioms) from a library for a given proof goal; neural premise selection, embedding-based retrieval, and feature-based selection for ATP and ITP systems. Tag when the paper primarily addresses the premise selection sub-problem rather than full proof generation.
- `#topic/funsearch` — the FunSearch paradigm: iterative evolutionary LLM-guided program search, where an LLM proposes variants of a program/function and an evaluator scores them for fitness; discovered new solutions to mathematical problems (cap set bounds, bin packing). Tag when a paper uses or directly extends the FunSearch evolutionary-LLM search methodology. Also applies to AlphaEvolve (FunSearch's 2025 successor).
- `#topic/mathematical-discovery` — systems that discover genuinely new mathematical results (new bounds, new conjectures, new algorithms, new identities) not previously known to human researchers. Substance test: the paper must provide experimental evidence of a discovery that extends prior human knowledge, not just solve known problems faster. Applies to FunSearch (cap set bounds), AlphaEvolve (kissing number, matrix multiplication), Ramanujan Machine (new conjectures about mathematical constants).

Grow the list organically. Don't pre-register topics that don't exist yet.

## Axis 5 — `#status/*` (lifecycle)

General lifecycle:
- `#status/draft` — work in progress, not yet reviewed
- `#status/review` — handed to Lead / Validator for review
- `#status/validated` — Lead or Experimenter approved (depending on note type)
- `#status/rejected` — explicitly killed; lessons captured
- `#status/superseded` — replaced by a newer note (link forward)

Experiment-specific:
- `#status/pending` — pre-registered, not yet run
- `#status/baseline` — single-algorithm reference established
- `#status/replicated` — re-run independently and confirmed
- `#status/inconclusive` — needs more seeds / data / parameter sweep

Math-claim-specific (Validator's verdict):
- `#status/proven` — Validator has produced a rigorous proof
- `#status/conjectured` — claimed but not proven; flagged for Validator follow-up
- `#status/disproven` — Validator showed it's false (or counterexample exists)

## Axis 6 — `#project/*` (optional — only when the note belongs to a named project)

Most paper notes won't have a project tag. Add `#project/*` only when the note is scoped to a specific project's workstream (an experiment, a code subsystem, a defined deliverable).

**Not a survey bucket.** Don't create `#project/*` tags for grouping papers by *what they study* (e.g. "all Burnside surveys" or "all Gröbner papers"). That's the job of `#topic/*` tags. Reserve `#project/*` for active named workstreams with concrete deliverables.

**Don't pre-register future workstreams.** A project earns a registered `#project/*` tag when it has active deliverables (code, experiments, a concrete plan). Until then, papers in preparation for that direction use `#topic/*` for retrieval. Pre-registration creates tags that never accumulate notes and pollutes the project pane.

**Multi-project tagging — allowed with soft cap of 2.** A note may carry more than one `#project/*` tag when it genuinely contributes to multiple named workstreams (substance test applies — every project tag must answer "would I want this note to surface when querying that project?"). Soft cap is 2; if you find yourself adding a third, you're probably topic-tagging — use `#topic/*` instead.

Currently registered:
- `#project/mixer-core` — general framework engineering (not specific to any one math problem)
- `#project/b25` — B(2,5), the flagship hard problem
- `#project/b43` — B(4,3)
- `#project/b53` — B(5,3)

Add new `#project/*` tags as new projects start. Discuss in `_meta/canvas-setup.md` before adding to keep them stable.

---

## Optional axes

### Content type

- `#paper` — literature summary (mandatory on every paper note)
- `#experiment` — pre-registered experiment + results
- `#methodology` — methodology subnote inside an experiment folder (notes in `methodology/` subdirs)
- `#results` — results subnote inside an experiment folder (notes in `results/` subdirs — `<technique>-results.md` etc.)
- `#data` — data subnote inside an experiment folder (notes in `data/` subdirs — input dictionaries, raw run capture)
- `#experiment-type` — top-level `_type.md` describing what a methodology family is (e.g. `Rust Bidirectional/_type.md`)
- `#decision` — ADR
- `#review` — Lead's code review
- `#proof` — proof sketch or full proof (with Validator's verdict)
- `#concept` — note in `Concepts/` covering a reusable concept hub. **Not for single-concept definition / reference notes** (e.g. `Research/Group theory/General/basics/group.md`, `presentations-and-relations/free-groups.md`, etc.) — those live in their topic dir and carry **no content-type tag**; `domain/*` + `topic/*` handle retrieval. The `#concept` content-type signals "I am a hub that other notes reference"; standalone definitions are not hubs.
- `#synthesis` — multi-paper synthesis
- `#bug` — known bug, postmortem
- `#question` — open question for the human or for Validator
- `#convention` — meta-document defining how something should be done
- `#content-type/code-example` — runnable code snippet (one task per file, expected output captured verbatim). Used in `Research/Group theory/Tools/<tool>/examples/`.

**One primary content-type per note.** A paper note gets `#paper`; an experiment note gets `#experiment`; a concept hub gets `#concept`. Don't carry both `#paper` + `#concept` on the same note — extract the concept content to a `Concepts/<name>.md` hub and link from the paper via `key_concepts:` frontmatter. Documented exception: a self-contained survey paper may carry `#paper` + `#synthesis` when the same note serves both functions (rare; substance test decides).

**Experiment-tree mapping.** Notes in the `Experiments/` subtree carry exactly one content-type tag matching their subdir role:

| Note location | Content-type tag |
|---|---|
| `<experiment-type>/_progress.md` (umbrella) | `#experiment` |
| `<experiment-type>/_type.md` (root) | `#experiment-type` |
| `<experiment-type>/methodology/<note>.md` | `#methodology` |
| `<experiment-type>/results/<note>.md` | `#results` |
| `<experiment-type>/data/<note>.md` | `#data` |

The experiment as a whole is identified by the umbrella `#experiment` tag on the `_progress.md` (or equivalent top-level summary). Do NOT use bare strings like `data` or `results` as tags — those aren't registered tags, just folder names; the registered tag forms are `#data` and `#results` (with the `#` prefix as Obsidian's tag pane requires).

**Inline `#concept/*` namespacing on non-concept notes is forbidden.** Concept content lives in `Concepts/<name>.md` hubs and links from papers via `key_concepts:` frontmatter (per [[paper-summary]] template). Paper-note tags never namespace into `concept/*` — that's a property of the concept hub, not the paper that references it.

### Paper-evaluation frontmatter (optional, on `#paper` notes)

- `relevance: 1|2|3` — Researcher's judgement of relevance to the active algo_mixing program. 1 = high (paper directly informs current experiments / methodology), 2 = medium, 3 = low. **Optional** — omit if unscored. Justification goes in `quality_notes:` body field (or expanded in the body's "Why this paper matters" section). Scoring rubric source: the originating synthesis note (e.g. `Research/Group theory/Open problems/_overview.md` for the open-problems batch). Queryable from Bases for ranking / filtering.

### Risk markers

- `#risk/high` — touches Mixer protocol, Rust ABI, on-disk format, or a math claim that other work depends on
- `#risk/breaking` — proposes a userspace break
- `#risk/unknown` — author unsure of blast radius

### Deprecated / dropped tags

These tag namespaces appear in historical notes but are dropped from current doctrine. Do not reintroduce. F4.3 migration removes them.

- `#score/1|2|3` — old inline relevance scoring on Open-problems papers. **Migrated** to optional `relevance: 1|2|3` frontmatter (see § Paper-evaluation frontmatter). Dropped 2026-05-28 in F4.2.
- `#project/none` — stale 7-axis escape hatch from when `#project/*` was mandatory. Project is now optional; "none" is not a valid value. Just omit `project:` when there is no project. Dropped 2026-05-28 in F4.2.
- `#project/burnside-other` — was used on one paper (`havas-newman-1980`) as a Burnside-surveys bucket. The project axis is for active named workstreams (b25/b43/b53/mixer-core), not group-family bucketing. Use `#topic/burnside` plus specific topic tags instead. Dropped 2026-05-28 in F4.2.
- `#domain/grobner` — never registered; appeared on one paper (`grobner.md`). Gröbner-basis work is migrated to `#domain/cs` + `#topic/grobner-basis`. The decision to register Gröbner (or SAT, biology) as a first-class `#domain/*` is deferred until that work has active deliverables justifying it. Dropped 2026-05-28 in F4.2.
- `#project/grobner` — appeared on one paper; never registered. Per § Axis 6 "Don't pre-register future workstreams", do not register until Gröbner has active code / experiments. Paper migrates to `#topic/grobner-basis` (+ `#project/b25` if substance test passes for B(2,5) contribution). Dropped 2026-05-28 in F4.2.

---

## Examples

**A B(2,5) paper summary, owned by you:**

```yaml
---
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/word-problem
  - topic/knuth-bendix
  - paper
  - status/validated
project: b25
---
```

**A Russian-source group-theory paper summary (abstract translated to English in body; original Russian not preserved in vault):**

```yaml
---
author: maumayma
language: ru
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/exponent-5
  - paper
  - status/draft
---
```

**An AI-applied-to-math paper a colleague is summarizing:**

```yaml
---
author: <colleague-handle>
language: en
tags:
  - agent/research
  - user/<colleague-handle>
  - domain/ai
  - topic/automated-theorem-proving
  - topic/reinforcement-learning
  - topic/lean
  - paper
  - status/draft
---
```

**A methodology concept note in `Concepts/`:**

```yaml
---
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/benchmark-design
  - topic/statistical-comparison
  - concept
  - status/validated
---
```

**A proof sketch by Validator:**

```yaml
---
author: maumayma
language: en
tags:
  - agent/validator
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - proof
  - status/proven
project: b25
---
```

---

## How to retag existing notes

Researcher has restructure authority over `Research/` and `Concepts/`. When the taxonomy changes or a colleague brings new domains, Researcher may retag existing notes to match. **Log every retag** to `Agents/<user>/Researcher/log.md` with before → after.

Bases queries are the source of truth for "is the taxonomy actually being used consistently." If a Bases view shows orphan tags or untagged notes, that's a retag candidate.
