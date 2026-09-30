---
tags: [meta, mission]
---

# Math vault — Mission

> The North Star. Every agent reads this each session. If the mission changes, edit here first; everything else follows.

## What this vault is

**A multi-domain research wiki** for a computational-mathematics research circle that grew out of various computational experiments. Contributors come from different fields (group theory, biology, SAT, Gröbner bases, AI, more) and share:

1. **Code**: several repos and libraries. These include our experiments/algorithms repo(s), a tools repo (reusable experimental tools, including MCP compute services for heavy runs), and external libraries and tools. Each is registered in `_meta/dependencies/`.
2. **This Obsidian vault**: durable knowledge across all those domains, organized for both humans and AI agents.

The AI roles are **architecture-neutral**. A workstream's repos, commands, protected interfaces and provenance fields live in its **project profile** (`_meta/projects/`), not in the role prompts. See [[projects-and-dependencies-convention]].

## The research program

The circle attacks hard problems in mathematics (currently mostly combinatorial group theory, especially Burnside groups) and methodology questions in computational mathematics. It does this through **pre-registered computational experiments** and **independently verified results**.

**No algorithm, architecture, language or tool is privileged.** Each workstream is a **project** with its own profile (`_meta/projects/project-<name>.md`), and the approach is chosen for that project on evidence. It might be a CAS computation, a rewriting system, search, learning, a portfolio of cooperating algorithms, or something nobody here has used yet. Tools that one project built can be reused standalone by any other project, through the dependency registry (`_meta/dependencies/`).

### Active projects
Profiles hold the details. The `#project/*` tags are listed in [[tags]] § Axis 6.
- **B(2,5)**, the free Burnside group on two generators of exponent 5. It is the hardest open problem here and has a dedicated specialist, **Experimenter-B25**. Profile: [[project-b25]].
- **Mixer framework**: cooperating algorithm processes that share intermediate results. Profile: [[project-mixer-core]].
- **Other Burnside instances** (B(4,3), B(5,3), B(2,9)). They don't have profiles yet; Lead writes each one when the project is next tasked.
- **New projects** start by Lead writing a profile. They don't have to use any existing project's code.

### Cross-domain work
**Researcher** scans literature across domains (group theory, Gröbner bases, SAT, biology, AI, …) for problems and techniques worth testing. When a candidate looks viable, Lead opens a project for it with its own profile, and a per-domain **Experimenter** runs it. Cross-domain work both validates techniques and exposes their limits.

## Terminology disambiguation

The word **"agent"** is overloaded:

- **AI agent**: an LLM on the Maestri canvas (Lead, Researcher, Developer, Experimenter, Experimenter-B25, Validator, Math Expert). Seven roles.
- **Algorithm process / component**: a program under test (a solver, a rewriting engine, a search process, a model). Projects may define their own term in their profile.

Throughout this vault, **"agent" with no qualifier means the AI agent on the canvas**. When referring to the code-level concept, write **component**, **algorithm process**, or the project's qualified term.

## Engineering invariants

- **Every repo builds from a clean clone** with its documented build command, and its **smoke test passes**. Both are listed in the project profile. Breaking either is a regression.
- **Protected interfaces** listed in a project profile or dependency note (protocols, ABIs, public APIs, on-disk formats): backwards-compatible additions are OK; breaking changes are userspace breaks and need a Lead-approved migration plan plus the human's approval.
- **Dependencies are pinned in code** (lockfiles/manifests) and registered in the vault. External code is never edited in place.

## What "good" looks like

Across all three layers:

- **Pre-registered** experiments with falsifiable hypotheses and termination criteria, *before* runs.
- **Provenance record** on every `runs/` output: code SHA(s), lock hash(es), versions of every dependency and tool exercised, and where it ran. See [[projects-and-dependencies-convention]].
- **Baselines** for every improvement claim (each component alone, or the reference method). No baseline, no claim.
- **n ≥ 5 seeds** for any quantitative claim.
- **Independent verification** of math results, via a tool path different from the one that produced the result: established tools chosen from the dependency registry, property tests for code that implements math, and hand proofs where rigor is needed. **Validator owns this layer.**

## Hot paths and compute

- Each project profile lists its hot paths: solver inner loops that run for hours, per-tick orchestration, serialization on every transfer, GPU kernels. On those, constant factors matter. Not hot (clean readable code wins): orchestration, experiment harnesses, analytics, one-shot scripts.
- **Compute is shared and finite.** Heavy runs obey the global cap in [[_common]] § Compute budget. The direction of travel is to move long, memory-hungry or GPU runs behind **MCP compute services** (local or cloud) that enforce the cap and stamp provenance, and to keep the shell for small runs and development.

## Roles on the canvas

Seven AI agents. [[lead|Lead]] is your interface and the only agent that commits code. See `_meta/agents/` for each role's prompt and `_meta/canvas-setup.md` for canvas assembly.

- **[[lead|Lead Dev]]** — orchestrator, validator (code quality), only agent that commits code.
- **[[researcher|Researcher]]** — literature scan across domains, paper summaries, OCR of old papers (via `nuextract-cli` when image-only), restructure-authority over `Research/` and `Concepts/`.
- **[[developer|Developer]]**: implementation in whatever stack a project uses, with framework and performance expertise. Ships algorithms, harnesses, library integrations and reusable experimental tools (including MCP compute services) in whatever repo the project profile names.
- **[[experimenter|Experimenter]]** — general experimenter for non-B(2,5) work and cross-domain explorations. Owns autoresearch.
- **[[experimenter-b25|Experimenter-B25]]** — B(2,5) specialist. Standing focus. Owns `Experiments/Group Theory/Burnside Group/B25/**`.
- **[[math-expert|Math Expert]]**: idea-generator and advisor. It proposes mathematically grounded ideas and never certifies them.
- **[[validator|Validator]]** — independent math oracle. Proves theorems, catches math bugs (like the abelianization bug), writes property tests and proof sketches. Verdict on math correctness overrides everyone except the human.

## Decision-making

The **human** is the final authority on:
- Research direction
- Algorithm / approach choices
- Commits to `main`
- Dependency additions
- Changes to public APIs, protected interfaces or on-disk formats

**Lead Dev** is the final authority on:
- Code quality (`MERGE` / `NEEDS WORK` / `REJECT`)
- Routing work between peers

**Validator** is the final authority on:
- Whether a math result is sound (`#status/proven`, `#status/conjectured`, `#status/disproven`)
- Even Lead defers to Validator on math correctness. Only the human can override Validator.

## Multi-user, multi-domain norms

This vault is shared. Norms:

- **Every note carries `#user/<handle>` + `author: <handle>`** (the human who owns it, even if AI-written). See [[tags]].
- **`#domain/*` and `#project/*` are orthogonal**: a single note can be `#domain/group-theory + #project/b25` (group-theory note about B(2,5) project work), or `#domain/group-theory` with no project tag (general group-theory knowledge unrelated to any project).
- **Cross-domain shared knowledge lives in `Concepts/`**: methodology, cooperation/scheduling theory, reusable patterns. Don't duplicate it into each domain.
- **People** get a `People/<handle>.md` note: who they are, what they work on, key contributions. The wiki has a human index.
- **Researcher may retag/move any note in `Research/` or `Concepts/`** when a better organization emerges. Logs every restructure. This authority is unique to Researcher; other agents only touch their own home dirs.
