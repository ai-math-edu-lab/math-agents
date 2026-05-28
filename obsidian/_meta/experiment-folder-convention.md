---
title: Experiment folder convention
status: validated
tags: [meta, convention, agent/human]
author: <human>
---

# Experiment folder convention

This document defines how experiment results are organized on disk in the Math vault. **Every AI agent that creates or updates content under `Experiments/` reads this first.** The Researcher's restructure authority extends to enforcing this convention on existing notes.

## Hierarchy

Three nested levels, deepest level being the experiment-type folder:

```
Experiments/
└── <Domain>/                       e.g. Group Theory, SAT, Biology, Grobner
    └── <Subject>/                  e.g. Burnside Group, Mathieu Group, 3-SAT, Protein folding
        └── <Instance>/             e.g. B25, B43, M22, sat-uf50
            └── <Experiment type>/  e.g. KBMag, Rust Bidirectional, Beam Search, Compression
                ├── methodology/
                ├── data/
                └── results/
```

- **Domain** — the broad field (Group Theory, SAT, Biology, etc.). Mirrors `#domain/*` tag axis.
- **Subject** — the family within the domain (Burnside Group is one family; Mathieu Group is another).
- **Instance** — the specific problem (B(2,5), M(22), a specific SAT benchmark).
- **Experiment type** — the methodology applied to that instance (KBMag, Rust Bidirectional, etc.). Each experiment type is one folder *no matter how many parameter-variant runs are performed inside it*.

## Per experiment-type folder — three required subfolders

### `methodology/`

Human-readable description of what the experiment is and how it's run. **Plain English first, technical details second.** Must include:

- **What this experiment type is**: one paragraph explaining the algorithm/approach in language a colleague from a different domain could understand.
- **Why we ran this**: one paragraph on the hypothesis or curiosity being tested.
- **How we ran it**: step-by-step from the operator's perspective. What command, what config, what inputs.
- **How it was validated**: dedicated section. What independent check confirms the result? (Cross-verification against another tool? Property tests? Hand proof? Comparison to a published result?) **If there is no validation, say so explicitly — `Validation: none yet` is honest; missing the section entirely is a defect.**
- **What "success" means for this experiment**: the falsifiable criterion that decides pass/fail.

Use frontmatter for searchable structure:

```yaml
---
title: <experiment type> on <instance>
domain: group-theory                    # or whichever
project: b25                            # or whichever
instance: B(2,5)
experiment_type: kbmag                  # short identifier
status: validated                       # see _meta/tags.md
author: <handle>
tags: [agent/exp, user/<handle>, domain/group-theory, topic/burnside, topic/knuth-bendix, project/b25, status/validated, experiment, methodology]
---
```

### `data/`

Inputs and artifacts the experiment consumes or produces. Subfolders/files as appropriate:

- **Scripts**: location reference (link to `algo_mixing` repo path, e.g. `experiments/burnside/run.py`). **Do not copy scripts into the vault** — the source of truth is the repo. Vault links to repo paths.
- **Constants** (`constants.md`): a markdown table listing fixed parameters used across runs (problem size, alphabet, fixed seeds if any, bounded resources).
- **Data used** (`data.md`): description of input data — where it lives (path), what it contains, summary statistics. If the data is a presentation (group theory) or a benchmark file (SAT), include or link the canonical reference.
- **Logs**: link to log paths in the repo (`runs/<project>/<experiment>/<timestamp>/`). **Do not paste full logs into the vault.** Paste excerpts only when illustrating a specific finding.

### `results/`

Outcomes. **One results table per experiment type, listing every parameter-variant run as one row.** Not one folder per run.

Required: a results table with these minimum columns:

| Run ID | Date | Parameters | Outcome | Wall-clock (ms) | Memory peak | Validated by | Notes |
|---|---|---|---|---|---|---|---|

- **Run ID**: short tag (`v1`, `v2-compression`, `v3-multipass-shortlex`). Stable identifier across documents.
- **Date**: `YYYY-MM-DD`.
- **Parameters**: the parameters that *changed from the baseline*. The baseline run gets `baseline` here.
- **Outcome**: short verdict (`completed`, `failed: rule explosion`, `proved 47/50 target words`, etc.).
- **Wall-clock (ms)**: the script time. If multi-run, the median + range.
- **Memory peak**: if measured.
- **Validated by**: `kbmag_v1 standalone`, `GAP`, `proptest`, `none` (be honest).
- **Notes**: one sentence pointing to what's interesting about this run.

In addition to the table:

- **Version history**: short prose section narrating what changed between runs and *why*. ("v1 used naive enumeration; v2 added shortlex ordering after Hall reduction failed; v3 added multi-pass beam search.")
- **Main findings** in plain English: what we learned, what was surprising, what didn't replicate.
- **Open questions** for the next iteration.

## Example (per the existing B(2,5) work)

```
Experiments/Group Theory/Burnside Group/B25/
├── KBMag/
│   ├── methodology/  ← description of running KBMag standalone on B(2,5)
│   ├── data/         ← presentation file, run commands, log paths
│   └── results/      ← table: KBMag-v1 (no completion, rule explosion), …
└── Rust Bidirectional/
    ├── methodology/  ← description of bidirectional KB with beam search
    ├── data/         ← presentation, target words, code paths
    └── results/      ← table: v1 (proved few words, no shortlex), v2 (proved many, with shortlex), …
```

Each experiment type lives in its own subtree. Each subtree's `results/` contains all the parameter variants in one table.

## What goes here vs in the repo

- **In the vault**: methodology prose, validation arguments, results tables with verdicts, version-history narrative, links to repo paths and run timestamps.
- **In the `algo_mixing` repo**: scripts, configs, raw output, log files. The repo is the source of truth for *what was run*; the vault is the source of truth for *what it meant*.

Never copy raw scripts or large log files into the vault.

## Tagging requirements (from `_meta/tags.md`)

Every note in `Experiments/**` carries minimum (6-axis per [[tags]]):

- `#agent/<who-wrote-it>` (e.g. `#agent/exp-b25`)
- `#user/<human-who-tasked-it>` (e.g. `#user/<handle>`)
- `#domain/<broad-field>` (e.g. `#domain/group-theory`)
- `#topic/<one+>` (substance test; e.g. `#topic/burnside`, `#topic/knuth-bendix`)
- `#project/<mixer-subproject>` (e.g. `#project/b25`) — **required for experiments specifically** (experiments are intrinsically project-scoped, even though `#project/*` is optional in the general taxonomy)
- `#status/<lifecycle>` (e.g. `#status/validated`)

Plus exactly **one** content-type tag matching the note's subdir role (see [[tags]] § Content type — Experiment-tree mapping):

| Note location | Content-type tag |
|---|---|
| `<experiment-type>/_progress.md` (umbrella) | `#experiment` |
| `<experiment-type>/_type.md` (root) | `#experiment-type` |
| `<experiment-type>/methodology/<note>.md` | `#methodology` |
| `<experiment-type>/results/<note>.md` | `#results` |
| `<experiment-type>/data/<note>.md` | `#data` |
| Proof sketches | `#proof` |

Do **not** use bare strings like `data` or `results` as tags — those aren't registered (only `#data` and `#results` with the `#` prefix are). Bare strings show up in Obsidian's tag pane as ambiguous, polluting the taxonomy.

## Cross-linking discipline (added 2026-05-28, Phase 9)

**Every content note in the experiment subtree must end with a `## Related material` section containing at least 3 substantive wikilinks.** A note with zero outgoing wikilinks is incomplete — empirical artifacts left graph-dead break the connection between methodology, data, results, and the papers/tools that informed them.

Minimum link set per note in `Experiments/<...>/<experiment-type>/`:

- **Parent `_type.md`**: every note in `methodology/`, `data/`, or `results/` subdirs links up to its parent `_type.md` (the methodology family root). Mandatory.
- **Project umbrella `_progress.md`**: every note links to the project-level umbrella (`Experiments/<...>/<project>/_progress.md`). Mandatory.
- **Sibling cross-link `data` ↔ `results`**: within the same experiment-type, the data note and the results note reference each other. Mandatory.
- **Tooling cross-link**: when the experiment used a named tool (KBMAG, GAP, Sage, kbprog), link to the relevant tool overview in `Research/Group theory/Tools/<tool>/<tool>-overview.md`. Mandatory when the tool is named.
- **Methodology cross-link**: when data/results were produced by a specific methodology note, link to it.
- **Paper-bridging**: link to specific papers in `Research/` that informed the methodology, substance test applies.

**Bidirectional discipline**: every wikilink added is reciprocated on the target end. `_progress.md` and `_type.md` notes maintain inventory lists of their child experiments and methodology family.

**Substance test** (mandatory on every link): the same substance bar as Research/ — "would a reader following this link land somewhere genuinely relevant?" Aspirational or generic-courtesy links are rejected.

**Exemption**: housekeeping notes (logs, READMEs, scratch entries — anything under [[naming-conventions]] § Rule 2) are not required to carry a Related material section.

**Wikilink-like syntax in example/template content** (`[[<placeholder>]]`, `[[<experiment-note>]]`, `[[<output-capture>]]`, etc.) **must be wrapped in backticks**. Bare `[[<...>]]` in body text is treated as a real wikilink by Obsidian's parser and creates phantom orphan nodes (same root cause as the commutator-bracket issue in [[paper-summary]] § Notation conventions). Applies to experiment templates, methodology prose, results narratives, and message-form scaffolds in agent prompts.

## Status conventions for experiments

- `#status/pending` — pre-registered, not yet run.
- `#status/baseline` — single-algorithm reference established (use this for the first run of any new experiment type).
- `#status/validated` — Experimenter scored against gates, passed.
- `#status/rejected` — failed the gates; lessons captured in the postmortem section.
- `#status/inconclusive` — needs more seeds / data / parameter sweep.
- `#status/replicated` — re-run independently and confirmed.
- `#status/proven` — Validator has produced a rigorous proof of the result (rare; usually applies to math claims that emerged from experiments, not the experiments themselves).
