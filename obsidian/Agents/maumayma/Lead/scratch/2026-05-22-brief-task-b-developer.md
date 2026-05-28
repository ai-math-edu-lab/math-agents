---
author: maumayma
recipient: developer
sent: 2026-05-22
tags:
  - agent/lead
  - user/maumayma
  - domain/infra
  - project/mixer-core
  - status/draft
  - delegation
---

# Brief — Task B — Backfill `Architecture/Mixer/Components/` (in-use + stale inventory + test methodologies)

Sent to **Developer** on 2026-05-22. Tracked from [[backfill-2026-05-22]].

## Message (verbatim)

> TYPE: REQUEST
> TOPIC: Document only components currently used by `experiments/b25_reduce_core/`; code-review pass identifies what's stale; separate notes document test methodologies
> CONTEXT: [[_common]] § K3 pattern, [[mission]], [[component-doc]] template. The `Architecture/Mixer/Components/` subtree has `KBMag/` and `Rust Mixer/` folders but no content.
>
> "Currently in use" = touched by `experiments/b25_reduce_core/` directly or transitively. Anything not touched is presumed stale until proven otherwise.
>
> Four phases. **Show me the Phase 1 trace before proceeding to Phase 2+.**
>
> ### Phase 1 — Dependency trace from `b25_reduce_core/`
>
> 1. Read `experiments/b25_reduce_core/README.md` first.
> 2. Read every Python file in `experiments/b25_reduce_core/` (`reduce_coreless.py`, `verify_reduction.py`, `analyze_rules.py`, `trace_reduction.py`) and in `experiments/b25_reduce_core/benchmark_run/` (`reduce_benchmark.py`, `reduce_benchmark_v2.py`, `run_full_logged.py`).
> 3. Read every shell script there (`run_biased_agents.sh`, `overnight_*.sh`, `collect_best.sh`, `retry_failed.sh`, `run_logged.sh`, `run_traced.sh`, `remaining_4pass.sh`).
> 4. Build a list of every:
>    - External binary invoked via `subprocess.run` / shell call (likely `kbprog` from `kbmag_v1/`, possibly others)
>    - Python module imported from elsewhere in the repo (NOT third-party packages)
>    - Data file or rule bank referenced from elsewhere in the repo
> 5. Write the trace to `Agents/Developer/scratch/b25-reduce-core-deps-<YYYY-MM-DD>.md`. Tag `#agent/dev #user/maumayma #domain/infra #project/b25 #status/draft`. **Show me before proceeding.**
>
> ### Phase 2 — Document only the in-use components
>
> For each component the trace identifies as actually used, write a K3 component note. Likely scope based on a quick prior look (YOUR trace is authoritative):
>
> - `Architecture/Mixer/Components/KBMag/_overview.md` — explains the two-way split: `kbmag_v1/` is used (called via `subprocess` from `b25_reduce_core` scripts); `kbmag_source/` is original upstream and NOT used (note as deprecated in body). The previous `kbmag_debug/` has been deleted.
> - `Architecture/Mixer/Components/KBMag/kbmag-v1.md` — what `kbprog` is, the input file format (presentation files), output (rules, reductions), the command-line flags `b25_reduce_core` actually passes to it. Reference specific Python scripts that call it.
> - One note per other in-use component your trace surfaces.
>
> K3 pattern (frontmatter agent layer, body human narrative). Status starts at `#status/draft`. Tags: `#agent/dev #user/maumayma #domain/<area> #project/b25` (project is `b25` because that's what's exercising them). `author: maumayma`.
>
> ### Phase 3 — Stale-component inventory (code-review pass)
>
> For each meaningful subsystem **NOT** in your Phase 1 trace, classify as:
>
> - **Stale-but-might-revive** — was used, may come back when cross-domain work picks up
> - **Genuinely dead** — superseded, broken, no plan to revive (e.g. `legacy/` is obvious)
> - **Unknown** — can't tell from code alone whether stale or dormant
>
> Write the verdict into a single code-review note at `Architecture/Mixer/Documentation/Code Review/<YYYY-MM-DD>-stale-component-inventory.md` using [[code-review]] template. Frontmatter `author: maumayma`, `status: draft`, tags `#agent/dev #user/maumayma #domain/infra #project/mixer-core #status/draft #review`.
>
> Body has three sections matching the three categories. For each subsystem:
>
> - Path (relative to repo root)
> - One-line description (from code, not invention)
> - Evidence it's not currently used: what `b25_reduce_core` doesn't touch
> - Recommendation: revive / archive / delete / ask human
>
> Candidates to assess (your trace is authoritative; this is where to start):
>
> - `mixer-core/` Rust engine and its subsystems (`mixer/`, `scheduler/`, `transport/`, `protocol/`, `kbmag/`, `pyo3_bindings/`, top-level files)
> - `api/` (3 files: `agent.py`, `burnside_rules.py`, `kbmag_agent.py`)
> - `orchestrator/` (`v2/` and `old_rl/`)
> - `legacy/` (`b43_kbmag_mixing_old`, `b53_kbmag_mixing_old`, `kbmag_debug`, `old_kb`, `_junk`, `old`, `orchestrator`)
> - `patterns/` (analysis scripts: `kb_dynamics.py`, `rule_graph_3d.py`, `deep_dive.py`, etc.)
> - `ui/` (HTML dashboards)
> - `kbmag_source/`
> - `checkpoints/`, `docs/`, `examples/`, `tests/`, `runs/` — assess whether they support `b25_reduce_core` directly or are orphaned
>
> ### Phase 4 — Document test methodologies (scattered)
>
> Tests live in many places; they're conceptually distinct methodologies, not files. Document by methodology under `Architecture/Mixer/Components/Tests/`. One K3 note per methodology — `Components.base` will pick them up automatically.
>
> For each methodology:
>
> - K3 [[component-doc]] template.
> - Frontmatter: `domain: methodology`, `hot_path: false`, `status: draft`, `author: maumayma`, `project: mixer-core` (test methodologies are framework-level even when applied to specific problems).
> - Tags: `#agent/dev #user/maumayma #domain/methodology #project/mixer-core #status/draft #convention`.
> - Body: **What it is** (the math question this methodology answers), **Why it exists** (what bug class it catches), **How it fits** (when to invoke it during an experiment), **Critical invariants** (the assumptions the test depends on — k-gram size, ordering choice, etc., each with WHY paragraph), **Public surface** (the script file(s) implementing it, the input format, the output format), **Related** (which Validator concerns it overlaps with, which experiments use it).
>
> Initial scope to produce (based on a quick prior look; verify and expand as you find more):
>
> - **k-gram overlap verification** — `tests/verify_kgram_special.py`. Verifies that "special" rules overlap with a target word's k-grams (k=8 matching the modified KBMag). The math question: *does a rule actually act on this word?*
> - **Special-rule overlap verification** — `tests/verify_special_rules.py`. Checks four overlap types (RHS-as-substring, LHS-as-substring, prefix/suffix overlap, factor containment). The math question: *in what ways does a rule relate to a target word?*
> - **GAP word-equality check** — `check_word.g` at repo root. Uses GAP's KBMag package to verify a specific word equality in B(4,3). The math question: *does my reduction chain actually compute an equal element in the group?*
> - **GAP confluence verification** — `verify_confluence.g` at repo root. Uses GAP's KBMag package to verify that a rewriting system is confluent. The math question: *does my rule set make a confluent reduction system?*
> - **Traced braid reduction verification** — `experiments/b25_reduce_core/verify_reduction.py`. Step-by-step reduction trace with braid moves. The math question: *does each step of my reduction chain follow a valid rewrite rule?*
> - **Containment verification** — `experiments/burnside/b25_bias_bidir/archive/verify_containment.py` and `experiments/b25_reduce_core/archive/scripts/verify_containment.py` (note: archived). The math question: *is the reduced word contained in some target equivalence class?*
> - **KBMag ordering-sweep runs** — `tests/` subdirectories (`l2r_rpo_*`, `r2l_rpo_*`, `shortlex_*`, `*_kgram*`, `*_30min`). Not Python tests; KBMag runs with different ordering parameters as a methodological sweep. The math question: *which ordering produces the smallest / most useful rule set on B(4,3)?*
>
> For each methodology, note explicitly in `known_issues` whether the test file(s) are in archived locations or active locations. Archived tests are documented because the methodology still matters even if those specific files are deprecated.
>
> If you find additional test/verification scripts not in the list above, add notes for them. If you find scripts that look like tests but you can't tell what they verify, list them in `known_issues` with `TODO: clarify <script> purpose with author` — don't invent.
>
> ### Critical rules across all phases
>
> - **Do NOT invent intent.** If you read code and can't tell what it does, that's the report. Don't write hypothesis as fact.
> - **Do NOT document anything as "in use" that you didn't trace from `b25_reduce_core`.** Honesty about what's load-bearing right now is the whole point.
> - **Do NOT delete or move files.** Documentation only.
> - NO code changes. NO new dependencies. Vault writes only.
>
> **Out of scope** — do not document as their own components: internals of `legacy/`, internals of `patterns/`, internals of `ui/`. They appear in the Phase 3 inventory note as paths + description + recommendation, not as their own pages.
>
> When done:
>
> Report back with:
>
> - Wikilink to Phase 1 dependency-trace
> - Wikilink to each Phase 2 component note
> - Wikilink to Phase 3 stale-component inventory
> - Wikilink to each Phase 4 test-methodology note
> - **Explicit list of questions for the human** about "Unknown" category items and any unclear test scripts
>
> I'll review for K3 compliance and honesty. NEEDS WORK on any note that documents something not in the dependency trace as "in use", or invents purpose for unread code.
>
> DEADLINE: none.
