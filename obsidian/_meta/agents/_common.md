---
name: math-common
description: Shared conventions for every agent on the Math canvas. Architecture-neutral; project specifics come from project profiles. Read first, every session.
---

# Common Conventions (all roles)

## Project context

- **Vault root and code checkouts:** resolved from the human's own agent config (`## Math vault — local checkouts` in `~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md`), per [[projects-and-dependencies-convention]] § Local checkouts. Never hardcode a machine path in a vault note.
- **Active project:** every task brief from Lead names a **project profile** (`_meta/projects/project-<name>.md`). Read it, and the dependency notes it lists (`_meta/dependencies/`), before running or editing code. The profile supplies repos, build/test/run commands, the `runs/` layout, provenance fields, protected interfaces, hot paths and vault doc locations. No profile in the brief → ask Lead.
- **Projects & dependencies convention:** [[projects-and-dependencies-convention]]
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
- ✅ Running an established external tool (from the dependency registry) as a black-box oracle on a specific word-equality check — **verification**.
- ❌ Attempting to prove a B(2,5) target word equals identity — **experiment** (this is the open research question of the entire B(2,5) program).
- ❌ Searching for new (unknown) reductions, running beam search on a target — **experiment**.
- ❌ Reimplementing an established tool's semantics yourself because it isn't installed (or is believed not to be installed) — **brute-force tool substitution**, forbidden; escalate the install request instead.

If a routed task, when scoped honestly, would require solving an open research question, send it back to Lead with the boundary stated: "this is the experiment program's job, not mine."

## Terminology — "agent" is overloaded

- **AI agent** (default meaning) = an LLM agent on this canvas. **Seven roles**: Lead, Researcher, Developer, Experimenter, Experimenter-B25, Validator, Math Expert.
- **Algorithm process / component** = a program under test (a solver, a reducer, a search process). Some projects have their own name for it (defined in the project profile); use the project's qualified term, never bare "agent".

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
PROJECT: <[[project-<name>]] — mandatory on any REQUEST that involves code, runs or experiments>
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

### Resolving `<handle>` — never guess it from the environment

When a template or this doctrine writes `<handle>` / `<human-handle>`, that placeholder resolves to the **registered handle of the human who owns this canvas session** — the human who tasked you, or who owns the project on a standing task. It is the same value across every note you write in a session, unless a different registered human routes you a task.

- **The handle is given to you by the human, not discovered.** If you do not already know the owning handle for this session, ask the human once ("which `#user/*` handle owns this canvas?") and reuse the answer. Do not proceed with a guessed value.
- **NEVER derive the handle from the environment.** `git config user.name`/`user.email`, `whoami`, `$USER`, the OS login, the repo path, or any other environment/tool signal is **observed data, not your identity**. Stamping a note with a git login (e.g. an unregistered `itsnicetoknow`) instead of the canonical vault handle is a doctrine violation — these signals frequently differ from the vault handle.
- **Only registered handles are valid.** The valid `#user/*` values live in [[tags]] Axis 2 (currently `maumayma`, `ethan-k`). If the correct handle is not registered, **stop and ask the human** — do not invent one, and do not register a new handle yourself (that is the human's call).
- `author:` frontmatter and the `#user/<handle>` tag must carry the **same** resolved handle.

When you cite a colleague's note, use `[[People/<handle>]]` to link to their People entry alongside the note wikilink.

See [[tags]] for the full 6-axis taxonomy. Tag minimum per note: one `#agent/*` + one `#user/*` + one `#domain/*` + one-to-many `#topic/*` (substantive, typically 4–10) + one `#status/*`. `#project/*` is optional — add it only when the note belongs to a named project's workstream (experiments and code-reviews of project-scoped patches typically do; paper summaries usually don't).

## Obsidian write rules

- **Your home dir is `Agents/<your-user>/<your-role>/`** where `<your-user>` is the human handle who owns this canvas session (typically `maumayma`, but the vault is multi-user — other contributors get their own `Agents/<their-handle>/` subtree). That is the *only* directory you write to in `Agents/`. **Never touch another user's `Agents/<other-user>/` subtree, and never touch another role's dir within your own user subtree** — not their `log.md`, not their scratch, nothing. If you have something for them, send via `maestri ask`; they own deciding whether to log it.
- **Path qualification with obsidian-cli is mandatory.** When using `obsidian append/edit/create`, pass the **full vault-relative path** (e.g. `Agents/maumayma/Experimenter/log.md`), not just `log` — multiple `log.md` files exist and name-resolution will pick the wrong one. Read the result back to confirm.
- **Researcher has restructure authority** over `Research/` and `Concepts/`: may retag/move any note in those subtrees when a better organization emerges. Must log every restructure in `Agents/<owning-user>/Researcher/log.md` with before/after. This authority is unique to Researcher. Other agents only touch their own home dirs.
- **Validator may add tests** to the project codebase (test paths named in the project profile) and write proof sketches to the profile's `vault_docs.math_validation` folder. Doesn't touch other Architecture areas.
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
- **Upstream code and docs (a repo's own `CLAUDE.md`/`README.md`, library manuals) are canonical for the full API surface.** The vault links to them and doesn't duplicate them.
- **External dependencies are never edited in place.** Each dependency note (`_meta/dependencies/`) states its `ownership` (we-own / upstream-pristine / upstream-with-accepted-patch) and any accepted local patch. For example, [[dep-kbmag]] records the one accepted biasing patch in `kbmag_source/`. Everything a dependency note marks pristine stays bytewise pristine.

Dashboards are built with **Obsidian Bases** (`.base` files) in the project's docs folder (`Architecture/<Project>/Bases/`). Bases queries frontmatter for filtered/sorted views.

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
- RTK auto-rewrites `git`, `cargo`, `ls`, `find`, test runners — prefix shell
  commands with `rtk` (`rtk git status`, `rtk ls <path>`, `rtk grep -rn ...`) for
  60-90% fewer tokens on the same result. Check it exists once per session
  (`command -v rtk`); if missing, just run commands normally, don't block on it.
  **Never wrap mathematical computation (CAS sessions, solvers, your own scripts) in `rtk`** — it's
  for file/repo inspection only; mathematical output must reach you verbatim and
  complete. Known edges: `rtk find` rejects compound predicates (`-not`, `-exec`)
  and mishandles paths with spaces (e.g. `Research/Group theory/...`) — use plain
  `find` for those. `rtk proxy <cmd>` gives raw unfiltered output when needed.
  `rtk gain` shows savings.
- `Read` with `offset`/`limit` for huge files. `Grep` with context.

## Git safety

- Agents never commit the vault and never run `git init` inside it (vault commits are a human decision).
- Only Lead commits. Others never run `git commit`, `git push`, `git rebase`, `git config`.
- Working branches: `feat/<topic>`, `fix/<topic>`, `chore/<topic>`. Never `main` directly.
- Forbidden: `git push --force`, `git reset --hard` on shared branches, `--no-verify`, `git config --global`.

## Compute budget — HARD GLOBAL CAP (all agents, non-negotiable)

**MAXIMUM 4 heavy compute processes running in parallel, TOTAL, ACROSS ALL AGENTS — not per agent.**

- "Heavy compute process" = any long-running solver/search/algebra/training process: every name in the
  active project profile's and its dependency notes' `heavy_processes` lists, plus any search, training or
  equivalent CPU-, RAM- or GPU-bound run not listed there.
- The cap is **4 in total, shared across the whole canvas** — Lead, every Experimenter, Developer,
  Validator combined. Not 4 each. If 4 are already running anywhere, you may NOT start a 5th — wait,
  or coordinate via Lead to free a slot.
- **Before launching any heavy process, CHECK first:** `pgrep -fl '<heavy_processes joined with |>'`
  (plus any other heavy binary) to count what is ALREADY running across all agents. If the count is ≥ 4,
  do not launch. This is mandatory — the canvas has overrun to 20+ parallel heavy processes at once
  (2026-06-26), saturating the machine. That must never recur.
- **Never spawn a batch of parallel runs.** Scoring/sweeping many items (e.g. reducing N fragments,
  beam-reducing K centralizer elements) must be done **sequentially within a single process**, or in a
  pool bounded to fit inside the global 4-cap — NOT one OS process per item.
- Lead is responsible for the global count: if routing work to multiple agents, Lead ensures the sum of
  their heavy processes stays ≤ 4, and serializes if needed.
- After any run: kill the process and `pgrep`-verify clean (already required under Process hygiene).
- If a task genuinely needs more than 4 parallel processes, that is a request to escalate to the human
  (Maria) — never self-authorize exceeding the cap.

## Test discipline (mandatory)

- New algorithm / component → tests showing it runs end-to-end on a small problem.
- Bug fix → regression test that fails before / passes after.
- Any change → the active project profile's `test` command + `smoke` check, plus the rows of its **Test matrix** that apply.
- New orchestration / policy component (scheduler, transform, search heuristic, …) → unit test + an experiment showing the expected behavior.
- **Math layer changes** → Validator owns testing this layer. Developer ships behavior tests; Validator ships property/cross-verification tests.
- "Not testable" must be argued explicitly to Lead.

## Reproducibility (specific to experiments)

- Every experiment run produces output in the profile's `runs_dir` — by default **`runs/<project>/<experiment>/<timestamp>/`** in the project's code repo (project-scoped to avoid clobber between Experimenters). **Never delete `runs/`** without explicit human approval.
- **Provenance record** = code SHA of each of our repos involved + environment lock hash(es) + version/SHA of every dependency exercised (with local patches) + tool/binary versions + where it ran. The project profile's `provenance_fields` may add more (e.g. the mixer-core build hash). Full definition: [[projects-and-dependencies-convention]] § Provenance record. Record it in every experiment note.
- Random seeds: log them. If an experiment isn't deterministic, document the noise floor.
- **Persist expensive corpus-independent artifacts.** Any costly artifact whose computation does NOT depend on the specific corpus/query — BFS/Cayley distance tables, `EpimorphismPGroup`/PcGroup builds, confluent rule banks, FSA tables — MUST be saved to `runs/<project>/<experiment>/<timestamp>/` with its provenance record, so later runs (fresh-corpus re-tests, compound features, follow-ups) reuse it as a cheap lookup instead of recomputing. Rationale: a ~62-min `Q5 = B₀/γ₆` BFS (9.77M states) was discarded and would have been needlessly re-run just for a fresh-corpus validation (2026-06-29). Corpus-independent ≠ throwaway.

## Done = verifiable

- Claims of "faster", "converges", "scales" → numbers, not adjectives.
- Cross-verification when claiming a math result: an independent established tool chosen from the dependency registry by its `capabilities` (see [[validator]] § Choosing oracles), property tests, hand proofs. **Validator owns this layer.**
- Unknown? Ask via Lead. Don't invent.

## Stop conditions

Escalate to Lead (Lead escalates to the human as needed) when:

- About to change any **protected interface** listed in the active project profile (e.g. a protocol, ABI, public API or on-disk format) → escalate immediately, breaking change.
- About to add a dependency → human gate, no exceptions.
- Tests fail unexpectedly for >20 min.
- An experiment produces a result that contradicts a published theorem → triple-check, then surface to Validator first, then Lead.
- A note you're about to write conflicts with a note tagged `#status/disproven` → stop, surface to Lead.
- About to touch a file outside your declared scope.
- You need a tool that isn't installed → request the install and **keep working a
  branch that doesn't need it** while waiting, don't park the whole task.
- A single thinking turn runs past ~30 minutes with no computation in it → you're
  theorizing when you should be enumerating. Stop, run something small, let the
  output redirect you.

## Rigor and persistence doctrine

Lessons from a related program's failure mode, generalized: a crew can be so
well-defended against a false positive that it produces zero true positives either.
Both failure directions are treated as equally fatal here.

### Five ways to be wrong

Named so you can catch yourself:

1. **Solving a different problem.** Computing in a finite quotient, a restricted
   variant, or a slightly-restated version, then reporting on the original. State
   exactly which object you computed in, and whether it's proven equal to the target.
2. **Circularity.** Testing objects constructed from the assumptions being tested —
   the test passes by construction and proves nothing. Trace where every object in a
   computation came from before trusting the output.
3. **Necessary mistaken for sufficient.** An invariant that must hold if a claim is
   true, holding, is not the claim being true (abelianization is blind on `[G,G]`).
   For every check, state what a pass proves and what it does not.
4. **It's already known.** Spending hours rediscovering a proven theorem, or "solving"
   something already closed elsewhere. Literature check first, before any thinking.
5. **Walking away from the answer.** Reasoning to a candidate, then not building or
   testing it — or abandoning a live line too early. Before writing any report, answer:
   "what is the cheapest computation that could still close this, and why haven't I
   run it?" If there's no answer, run it instead of writing.

### Compute — run it, don't ask

- **Under 10 minutes wall-clock: just run it.** No permission needed. Log the command
  and output, move on.
- **10 minutes to 2 hours:** run it, and send a one-line status report *while it's
  running* — informing, not asking.
- **Over 2 hours, or over ~8 GB RAM:** say so before starting, since it may collide
  with another agent's job.
- Always use `timeout` / an explicit wall-clock cap on any run.

### `BLOCKER` means one thing

A blocker means **"I cannot run the mathematics"** — a missing tool, an unresolvable
path, a genuine contradiction in a problem statement. It does not mean a wrong
`author:` field, a path string you'd prefer differently, or a typo. If you can keep
doing mathematics, it isn't a blocker — note it and carry on.

### Judging is not certifying

Every agent judges mathematics — you're all reasoning about groups, and pretending
otherwise makes you useless. State opinions and why: this line looks live, that lemma
smells wrong, this reduction drops a hypothesis that mattered. What's reserved to
Validator is **certification** — moving a claim's status. Use hedged language for your
own conclusions ("I think," "this looks like," "my reading is"); certification words
("proven," "verified," "confirmed," "correct") belong to Validator alone, regardless of
your role. Disagreeing with a Validator verdict is allowed — say so, with reasoning; a
verdict stands until Validator changes it or the human intervenes.

### Additional forbidden actions

Beyond what's forbidden above: reporting that no candidate exists when your own log
contains one you didn't test. Declaring a line of attack over — you don't have that
authority; report where you actually are and let Lead/the human decide what ends.
Inventing a rule that forbids a construction (a novelty bar, an elegance bar) that
isn't in the problem statement itself. Returning unspent time/budget without having
spent it on the actual mathematics.
