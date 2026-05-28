---
tags: [agent/lead, user/maumayma, domain/group-theory, topic/onboarding, topic/group-theory, topic/word-problem, topic/kbmag, topic/gap, status/draft]
author: maumayma
project: mixer-core
audience: Researcher
brief_date: 2026-05-28
---

# Brief — Phase 6: Fill `Research/Group theory/` with foundational + tooling content

Sender: Lead (relaying Maria's brief verbatim, with sequencing notes).
Recipient: Researcher.
Sequencing: F6.1 → F6.2 → F6.3. F6.1 ~10 min. F6.2 is the bulk (can split across sessions). F6.3 is light.

## Context

`Research/Group theory/General/Include.md` is currently a one-line scope stub from Maria:

> "Include general postulants, rules, logic of Group Theory, Word Problem, target words calculation, GAP package docs (readable), GAP/KBMAG code examples (how to run groups with gap, how to find group sizes, how to calculate target words)."

The current `Group theory/` subtree only has `Burnside groups/B25/` (papers), `General/Include.md` (this stub), and `Open problems/` (papers). Missing: foundational theory, Word Problem treatment, tooling docs that would let a new colleague onboard without reading the codebase.

## F6.1 — Restructure `Research/Group theory/` (Researcher, restructure authority)

Create the following dirs alongside existing `Burnside groups/` and `Open problems/`:

```
Research/Group theory/
├── _overview.md                              ← NEW: maps where things live
├── General/                                  ← exists; populate per F6.2
│   ├── _overview.md                          ← define scope vs Word Problem/Tools
│   ├── basics/
│   ├── presentations-and-relations/
│   ├── orders-and-finiteness/
│   └── _synthesis-existing-papers.md         ← live synthesis, updateable
├── Word Problem/                             ← NEW
│   ├── _overview.md
│   ├── decidability-landscape.md
│   ├── target-words.md
│   └── techniques/                           ← KB, Dehn function, automatic groups
└── Tools/                                    ← NEW
    ├── _overview.md                          ← decision tree: which tool for which task
    ├── GAP/
    │   ├── _overview.md
    │   ├── examples/                         ← runnable snippets per task
    │   └── package-kbmag.md
    └── KBMAG/
        ├── _overview.md
        ├── file-formats.md
        └── examples/
```

Delete `Research/Group theory/General/Include.md` (its scope is replaced by the new dirs).

## F6.2 — Populate the new dirs (Researcher, no field bias)

For each dir, produce notes that satisfy:

- **`General/basics/`** — definitions of group, subgroup, homomorphism, kernel, normal subgroup, quotient, group action. Each definition gets its own short note (use [[concept-note]] template). Reference textbook source (Rotman, Hungerford, Dummit-Foote — Researcher picks one and cites consistently). Each note: one paragraph definition, one paragraph why it matters, examples, link to related concepts.
- **`General/presentations-and-relations/`** — free groups, presentations <X | R>, Tietze transformations, coset enumeration (Todd-Coxeter), Cayley graphs. Same format.
- **`General/orders-and-finiteness/`** — |G| notation, finite vs infinite, exponent, torsion, classification of finite simple groups (one-pager pointing at the result, not the proof).
- **`General/_synthesis-existing-papers.md`** — cross-paper view of all `Group theory/` papers using [[synthesis]] template. Mark as updateable — Researcher refreshes this on every `/research --reconnect group-theory` pass.
- **`Word Problem/decidability-landscape.md`** — state the word problem, Novikov-Boone undecidability for finitely-presented groups, decidability for free groups / abelian / hyperbolic / automatic. Cite known results verbatim.
- **`Word Problem/target-words.md`** — what a "target word" is in our methodology (B(2,5) context implicit but state it generally), how to construct one, how to verify equality.
- **`Word Problem/techniques/`** — one note per technique (Knuth-Bendix, Dehn function, automatic-groups via finite-state automata). Cross-link to `Tools/GAP/examples/` and `Tools/KBMAG/examples/` where applicable.
- **`Tools/GAP/examples/`** — runnable GAP code per task. Each file = one task. Tasks: compute group order, enumerate cosets, test word equality, present a quotient, compute exponent, list subgroups, work with kbmag package. Format: brief explanation + verbatim code block + expected output (verbatim).
- **`Tools/KBMAG/examples/`** — same pattern for standalone `kbprog` / `autgroup`. File formats note covers `.rws` and the `kbprog` flag conventions.
- **`Tools/_overview.md`** — decision tree: "I want to compute |G| → GAP/`Order(G)`; I want a confluent rewrite system → KBMAG/`kbprog`; I want to test if a word equals identity → GAP if small / KBMAG if large; ..."

### Rules for all notes

- **English** (translate any non-English source, mark `[trans.]`).
- **6-axis tags**: `#agent/research #user/maumayma #domain/group-theory #topic/<specific>+ #status/draft` plus `#concept` or `#convention` as appropriate. **No `#project/*` on these notes** — they are domain-foundational, not project-scoped.
- **No invented citations.** Every claim cites either a textbook section or a runnable tool output.
- **GAP/KBMAG code examples must be ACTUALLY RUN** by Researcher (or routed via Lead to Developer if Researcher can't run them). Expected output must match real output, not best-guess.

### Tooling precondition

- **Probe before assuming** (per [[_common]] § "Probe before assuming"): run `which gap` and `which kbprog` at the start of F6.2 Tools/ work.
- GAP is expected installed (`/opt/homebrew/bin/gap` 4.15.1 per [[canvas-setup]]).
- KBMAG (`kbprog`) is bundled with the algo_mixing repo in `kbmag_v1/` and `kbmag_source/` — check both, find the right binary, document the path you used.
- **If a tool genuinely missing**: do NOT fabricate outputs. Send `TYPE: BLOCKER` to Lead naming the missing tool, the exact example you can't run, and what you'd need.

### New content-type tag — already registered

Lead has registered `#content-type/code-example` in [[tags]] § Content type as a precondition for this work. Use it on every note in `Tools/<tool>/examples/`.

## F6.3 — Wire the updateable synthesis (Researcher)

`General/_synthesis-existing-papers.md` is the cross-paper view that gets refreshed whenever new papers land. Researcher:

- Writes the initial synthesis covering current papers in `Group theory/**`.
- Adds a clear "last updated" timestamp at the top.
- Documents the refresh trigger: "Re-run `/research --reconnect group-theory` after any new paper lands in this subtree."
- Logs the synthesis path in `Agents/maumayma/Researcher/log.md` so future Researchers know it exists.

## Constraints (do NOT violate)

- **No Mixer-specific framing** in any of these notes. Mixer relevance arrives via per-task briefs from Lead, not via the standing content.
- `General/` is for textbook-style group theory. `Word Problem/` and `Tools/` are separate because they're topics + craft, not foundations.
- `Tools/GAP/examples/` and `Tools/KBMAG/examples/` must be **runnable**. If a colleague copies the snippet into a terminal, it should work. Researcher must run each one and paste verbatim output. If Researcher's environment doesn't have GAP/KBMAG installed (`which gap`, `which kbprog`), flag to Lead before fabricating outputs.

## Deliverable on completion

Researcher reports back to Lead with:

- Dir tree before/after.
- List of notes created with one-line summary each.
- Concept hubs created in `Concepts/`.
- Any GAP/KBMAG examples that couldn't be verified (and why).
- Path to `_synthesis-existing-papers.md`.

---

# Phase 4 — Additions to in-flight reprocess (paste into your Phase 4 workflow)

These four additions apply to the 17-paper reprocess already underway. Researcher should fold them into the in-flight work.

1. **Drop `project: none` / `#project/none`.** Wherever they appear, **delete the property and the tag**. Under the new 6-axis taxonomy, project is optional — absent means absent, not literally "none". The "none" string is a stale 7-axis artifact. Just don't write `project:` at all when there's no project.

2. **Substance-test topic tags by reading paper content, not by inferring from directory path.** A paper sitting in `Research/Group theory/Burnside groups/B25/` still needs Researcher to confirm it actually engages with `#topic/burnside` and `#topic/b25` before tagging. Don't auto-tag from path. Every topic tag must answer "would I want this paper to surface when searching for this topic?" — passing mentions don't qualify (per [[tags]] § Axis 4 substance test).

3. **Confirm every paper note has the `#paper` content-type tag.** Some existing notes may be missing it (which is why only 11 of ~17 currently surface in the `Papers.base` "All papers" view — that view filters on `file.hasTag("paper")`).

4. **For Word Problem / Braid-related papers** (e.g. `2-relator-word-problem-9.29-merzlyakov.md`, `braid-b4-membership-6.24-makanin.md`), add the appropriate topic tags (`#topic/word-problem`, `#topic/braid-groups`, etc.) per the substance test. **Don't add `#project/word-problem`** — Word Problem is a topic, not a project.

---

# Coordination + ack expectation

- Phase 5 (Lead) modified 6 doctrine files + `Papers.base` to align with the new 6-axis taxonomy. The "By topic" view in `Papers.base` uses `groupBy.property: file.tags` and is **unverified** — if you see groupings that look noisy (one row per agent/user/domain tag too), tell Lead and we'll route a Developer fix.
- The `Papers.base` "By project (project-scoped papers only)" view uses a truthy filter `- project` (excludes papers without a project). Phase 4 Addition #1 above (drop `project: none`) feeds directly into this — once you strip the "none" strings, that view will be clean.
- Ack on receipt with a short `TYPE: REPORT` saying which phase you're starting first (F6.1 or batch-applying the Phase 4 additions to in-flight work) and your ETA / next checkpoint.
