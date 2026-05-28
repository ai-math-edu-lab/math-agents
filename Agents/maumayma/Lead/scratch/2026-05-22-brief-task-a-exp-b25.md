---
author: maumayma
recipient: experimenter-b25
sent: 2026-05-22
tags:
  - agent/lead
  - user/maumayma
  - domain/group-theory
  - project/b25
  - status/draft
  - delegation
---

# Brief — Task A — Backfill B(2,5) experiment documentation

Sent to **Experimenter-B25** on 2026-05-22. Tracked from [[backfill-2026-05-22]].

## Message (verbatim)

> TYPE: REQUEST
> TOPIC: Backfill B(2,5) experiment documentation from prior runs
> CONTEXT: [[experiment-folder-convention]], [[tags]], [[mission]]. The `Experiments/Group Theory/Burnside Group/B25/` subtree has `KBMag/` and `Rust Bidirectional/` folders in place but their `methodology/`, `data/`, `results/` subfolders are empty. Prior B(2,5) work has been performed but never documented in K3 format.
>
> ASK: Document each B(2,5) experiment type actually run. For each:
>
> 1. Read relevant code in `/Users/maumayma/Desktop/reps/algo_mixing/`: `experiments/b25_reduce_core/` (current active work — read its `README.md` and the scripts), `kbmag_v1/` for KBMag work, `mixer-core/` for the Rust Bidirectional implementation, `runs/` for surviving outputs, `legacy/` for older B(2,5) work. Do not modify code.
> 2. `experiments/b25_reduce_core/` is the current active experiment type — call it "Reduce Core" (or similar following the existing folder shape). Create `Experiments/Group Theory/Burnside Group/B25/Reduce Core/methodology/`, `data/`, `results/`. The `corrected/` and `benchmark_run/` subfolders in the repo are evidence of prior runs.
> 3. Create `_type.md` at each experiment-type level (`B25/KBMag/_type.md`, `B25/Rust Bidirectional/_type.md`, `B25/Reduce Core/_type.md`) explaining the technique in plain English, citing relevant papers from `Research/Group theory/Burnside groups/B25/` if any exist.
> 4. For each parameter-variant run performed, add one row to the experiment-type's `results/results.md` table per [[experiment-folder-convention]] (Run ID / Date / Parameters / Outcome / Wall-clock / Memory / Validated by / Notes).
> 5. Write a methodology note for each experiment type using [[experiment]] with explicit reconstruction marker:
>    - Frontmatter `status:` reflects actual outcome (`replicated`, `inconclusive`, `rejected`).
>    - Frontmatter field `reconstructed_on: <YYYY-MM-DD>` so future agents see this wasn't pre-registered.
>    - Body section `## Reconstruction notes`: "This experiment was performed prior to the K3 documentation convention. Reconstructed from {code in `<path>`, prior runs in `<path>`, memory, repo commit history} on `<date>`."
>    - `author: maumayma`, `#user/maumayma`.
> 6. Create or update `Experiments/Group Theory/Burnside Group/B25/_progress.md` — the standing progress note. Reflect what's been done, what worked, what's stuck, what's next.
> 7. KBMAG context (encode in your notes when touching KBMag): we use `kbmag_v1/` only. `kbmag_source/` is unused. The previous `kbmag_debug/` is deleted.
> 8. Where you can't reconstruct details honestly (e.g. exact seed unknown), say so: `Seed: unknown — reconstruction limitation`. Don't guess.
>
> NO new experiments. NO code changes. Vault writes only. Tag every note with `#agent/exp-b25 #user/maumayma #domain/group-theory #project/b25` plus the appropriate `#status/*` and `#experiment` / `#methodology` content tag.
>
> When done: report back with wikilinks to every note created and the updated `_progress.md`. Flag experiments where reconstruction was impossible (need human input).
>
> DEADLINE: none.
