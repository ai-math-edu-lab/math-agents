---
name: math-common
description: Shared conventions for every agent on the Math (algo_mixing) canvas. Read first, every session.
---

# Common Conventions (all roles)

## Project context

- **Vault root:** `/Users/maumayma/Documents/Obsidian/Math`
- **Repo root:** `/Users/maumayma/Desktop/reps/algo_mixing`
- **Mission & invariants:** [[mission]]
- **Tag taxonomy:** [[tags]]
- **Canvas setup:** [[canvas-setup]]
- **Experiment folder convention:** [[experiment-folder-convention]]

## No unsolicited initiative

On wake (any new session, "run protocol", any vague greeting): perform the **Cold-Start Handshake** in your role file. That is the entire wake-up routine.

You do **not** on wake:
- write to any log
- send `maestri ask` messages to peers (other than the single ack the human asked for, if any)
- read the repo, scan the vault beyond what your role file says, or pre-load context speculatively
- offer status updates, plans, or "here's what I noticed" reports

You wait. The human tasks you. Then you act.

## Probe before assuming

Setup docs (canvas-setup, role files, mission) describe the intended tooling state at some prior moment. They can drift. Before declaring a tool unavailable, run `which <tool>` or the tool's `--version` check. Before declaring a directory absent, `ls` it. Before declaring a file's contents stale, `grep` for current usage. The vault is durable; the world isn't. Trust verification over assertion.

**Grep-before-cite.** Before including any `file:line` reference in a note, message, or doctrine edit, run `grep -rn "<path-or-symbol>" <repo-root>` (or equivalent) to confirm it exists and matches what you claim. A citation in a vault note or commit message is a fact-claim; unverified, it is invention. If grep returns no results, do not include the citation. If you have a hypothesis but can't verify it, mark it `(unverified)` or `(TODO: verify file:line)` and route it back to Lead for confirmation. This applies to all roles, including Lead.

## Verification ≠ experiment

Some kinds of "verification" tasks are actually experiment-shaped. Distinguishing them matters because the experiment program owns the open research questions; Validator (or any other role) attempting to solve them via "verification" would scoop the experiment.

- **Verification**: takes a *pre-existing artifact* (a claimed reduction chain, a specific group-equality assertion between two given words, a documented invariant) and checks whether it is sound, using available tools as oracles. Does not generate new mathematical content.
- **Experiment**: takes an *open question* (e.g. "is `comm_12_9` equal to identity in B(2,5)?") and tries to answer it. Generates new mathematical content.

Concrete examples for the B(2,5) program:
- ✅ Verifying that the 7,245-char reduced word equals the 28,652-char input under the rules Experimenter-B25 documented — **verification**.
- ✅ Running GAP's kbmag as a black-box oracle on a specific word-equality check — **verification**.
- ❌ Attempting to prove a B(2,5) target word equals identity — **experiment** (this is the open research question of the entire B(2,5) program).
- ❌ Searching for new (unknown) reductions, running beam search on a target — **experiment**.
- ❌ Reimplementing GAP semantics in pure Python because GAP isn't installed (or believed not to be installed) — **brute-force tool substitution**, forbidden; escalate the install request instead.

If a routed task, when scoped honestly, would require solving an open research question, send it back to Lead with the boundary stated: "this is the experiment program's job, not mine."

## Terminology — "agent" is overloaded

- **mixer Agent** (lowercase + qualifier) = a subprocess implementing the `mixer_core.Agent` protocol (an algorithm instance).
- **AI agent** (default meaning) = an LLM agent on this canvas. **Six roles**: Lead, Researcher, Developer, Experimenter, Experimenter-B25, Validator.

When in doubt, qualify.

## Topology — hub-and-spoke through Lead, with one exception

- **Lead Dev** is the human's interface and the *only* AI agent that runs `git commit` / `git push`.
- Researcher, Developer, Experimenter, Experimenter-B25 route work-changing requests through Lead.
- Read-only peer Q&A allowed.
- **Exception — Validator's math verdicts**: when Validator says a math result is `#status/disproven` or otherwise wrong, that verdict overrides any other agent's claim *immediately*, without waiting for Lead routing. The other agent must freeze any work building on that result and surface to Lead. Lead can't override Validator on math correctness; only the human can.

## Communication protocol (inter-AI-agent handoff)

When messaging a peer via `maestri ask "<Name>" "..."`:

```
TYPE: <REQUEST | REPORT | QUESTION | BLOCKER | VERDICT>
TOPIC: <one line>
CONTEXT: <wikilink>
ASK: <what you need, or "FYI">
DEADLINE: <none | needed by <event>>
```

`VERDICT` is reserved for Lead's code reviews and Validator's math verdicts. Long context in linked vault notes, not in the message.

## Multi-user authorship

This vault is shared across multiple humans (you + colleagues). Every note carries:

- **`#user/<handle>` tag** — the human who owns or commissioned this note. Always present, even if the note was AI-written.
- **`author: <handle>` frontmatter property** — same value, queryable by Bases.

If you're writing on behalf of a human who tasked you, `author` is that human's handle, not yours. AI authorship is recorded separately via `#agent/<role>` tag.

When you cite a colleague's note, use `[[People/<handle>]]` to link to their People entry alongside the note wikilink.

See [[tags]] for the full 6-axis taxonomy. Tag minimum per note: one `#agent/*` + one `#user/*` + one `#domain/*` + one-to-many `#topic/*` (substantive, typically 4–10) + one `#status/*`. `#project/*` is optional — add it only when the note belongs to a named project's workstream (experiments and code-reviews of project-scoped patches typically do; paper summaries usually don't).

## Obsidian write rules

- **Your home dir is `Agents/<your-user>/<your-role>/`** where `<your-user>` is the human handle who owns this canvas session (typically `maumayma`, but the vault is multi-user — other contributors get their own `Agents/<their-handle>/` subtree). That is the *only* directory you write to in `Agents/`. **Never touch another user's `Agents/<other-user>/` subtree, and never touch another role's dir within your own user subtree** — not their `log.md`, not their scratch, nothing. If you have something for them, send via `maestri ask`; they own deciding whether to log it.
- **Path qualification with obsidian-cli is mandatory.** When using `obsidian append/edit/create`, pass the **full vault-relative path** (e.g. `Agents/maumayma/Experimenter/log.md`), not just `log` — multiple `log.md` files exist and name-resolution will pick the wrong one. Read the result back to confirm.
- **Researcher has restructure authority** over `Research/` and `Concepts/`: may retag/move any note in those subtrees when a better organization emerges. Must log every restructure in `Agents/<owning-user>/Researcher/log.md` with before/after. This authority is unique to Researcher. Other agents only touch their own home dirs.
- **Validator may add tests** to the codebase (`mixer-core/tests/proptest_*.rs`, `tests/property_*.py`) and write proof sketches to `Architecture/Mixer/Documentation/Math Validation/`. Doesn't touch other Architecture areas.
- Keep your `log.md` append-only.
- Templates in `_templates/`. Use them.
- Wikilinks > paths.
- Tags mandatory per [[tags]] (6-axis minimum: agent + user + domain + topic + status; project optional).
- Frontmatter mandatory on templated notes.
- Prefer the `obsidian` CLI (requires Obsidian open + CLI enabled) — *with full paths*. Or use the `Write`/`Edit` tools directly.
- Never paste >50 lines of logs into chat — save to a vault note and link.

## Dual-audience writing convention (K3 pattern)

Architecture / Components / Experiments / Research / Concepts notes serve **two readers**: humans (you + colleagues) and AI agents. Both need different things from the same file. We use the **K3 pattern**:

- **Frontmatter is the agent layer.** Structured properties — `public_api`, `invariants` (list of `{id, summary, why}`), `hot_path`, `domain`, `project`, `status`, `related`, `tests`, `author`. Agents and Bases read frontmatter directly.
- **Body is the human layer.** Pure narrative — **What it is**, **Why it exists**, **How it fits**, **Critical invariants — why each one exists**, **Public surface** (plain English), **Hot path?**, **Tests**, **Related**, **Recent changes**.
- **No `TypeName (file:line)` lists in body.** That goes in frontmatter `public_api`.
- **Why-paragraphs mandatory for invariants.** Bare invariant statements without rationale teach nothing.
- **Upstream code (mixer-core/CLAUDE.md, KBMAG docs) is canonical for full API surface.** Vault links to it; doesn't duplicate.

Dashboards built with **Obsidian Bases** (`.base` files) in `Architecture/Mixer/Bases/`. Bases queries frontmatter for filtered/sorted views.

### Templates following K3
- [[component-doc]], [[experiment]], [[paper-summary]], [[concept-note]], [[synthesis]], [[decision]], [[code-review]]

When in doubt: **structured data in frontmatter, prose in body, never both in body**.

## Validator's verdict layers

When Validator returns a verdict on a math claim:

- `#status/proven` — rigorous proof exists (link to it). Code or experiment building on this can proceed with confidence.
- `#status/replicated` — empirically confirmed (multiple seeds, multiple runs); not proven theoretically.
- `#status/conjectured` — claimed without verification; flagged for Validator follow-up.
- `#status/disproven` — Validator found a counterexample or contradiction. **All work depending on this stops until the underlying claim is reformulated.**

Other agents respect these labels. If you find a claim tagged `#status/disproven`, you may not cite it as evidence.

## Token discipline

- `defuddle <url>` for web reads (especially math papers — defuddle handles arxiv well).
- `nuextract-cli <pdf> <schema>` for image-only / scanned PDFs (when available — see [[ocr-tooling]]).
- RTK auto-rewrites `git`, `cargo`, `ls`, `find`, test runners.
- `Read` with `offset`/`limit` for huge files. `Grep` with context.

## Git safety

- Vault NEVER committed to git. No `git init` in `/Users/maumayma/Documents/Obsidian/`.
- Only Lead commits. Others never run `git commit`, `git push`, `git rebase`, `git config`.
- Working branches: `feat/<topic>`, `fix/<topic>`, `chore/<topic>`. Never `main` directly.
- Forbidden: `git push --force`, `git reset --hard` on shared branches, `--no-verify`, `git config --global`.

## Test discipline (mandatory)

- New algorithm / mixer Agent → tests showing it runs end-to-end on a small problem.
- Bug fix → regression test that fails before / passes after.
- mixer-core Rust changes → `cargo test -p mixer-core` + a Python smoke test (`uv run python examples/sorting/run.py` minimum).
- New scheduler / transform → unit test + an experiment showing the expected behavior.
- **Math layer changes** → Validator owns testing this layer. Developer ships behavior tests; Validator ships property/cross-verification tests.
- "Not testable" must be argued explicitly to Lead.

## Reproducibility (specific to experiments)

- Every experiment run produces output in **`runs/<project>/<experiment>/<timestamp>/`** (project-scoped to avoid clobber between Experimenters). **Never delete `runs/`** without explicit human approval.
- Provenance triple = (git SHA, `uv.lock` hash, mixer-core build hash). Record in every experiment note.
- Random seeds: log them. If an experiment isn't deterministic, document the noise floor.

## Done = verifiable

- Claims of "faster", "converges", "scales" → numbers, not adjectives.
- Cross-verification when claiming a math result: GAP/Sage for group theory (GAP is the canonical tool; kbmag is a GAP package and also the name of standalone `kbprog` binaries in this repo — `kbmag_v1/` and `kbmag_source/` are both in active use for different code paths, see canvas-setup), property tests, hand proofs. **Validator owns this layer.**
- Unknown? Ask via Lead. Don't invent.

## Stop conditions

Escalate to Lead (Lead escalates to the human as needed) when:

- About to modify the mixer protocol (JSON-lines schema, pyo3 ABI) → escalate immediately, breaking change.
- About to add a dependency → human gate, no exceptions.
- Tests fail unexpectedly for >20 min.
- An experiment produces a result that contradicts a published theorem → triple-check, then surface to Validator first, then Lead.
- A note you're about to write conflicts with a note tagged `#status/disproven` → stop, surface to Lead.
- About to touch a file outside your declared scope.
