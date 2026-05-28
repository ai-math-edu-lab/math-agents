# Math vault — Claude Code context

This file is auto-loaded by Claude Code in any session inside this repo. It tells you what this repo is, where the vault lives, and what conventions to follow.

## What this is

This repo contains the **Math** Obsidian vault — a shared multi-user, multi-domain research wiki for the algorithmic-mixing research circle and adjacent fields (group theory, AI, CS, methodology). The vault lives at `obsidian/`. The repo root holds colleague-onboarding files only.

## Vault location

`<repo-root>/obsidian/`

When operating on the vault, use this path. Never write to the repo root except for the onboarding files (`README.md`, `CLAUDE.md`, `.claude/commands/*`, `.gitignore`).

## First-time users

If a user invokes Claude Code in this repo and they have NOT yet been registered in the vault (no `#user/<handle>` in `obsidian/_meta/tags.md` matching them, no `obsidian/People/<handle>.md`), suggest they run:

```
/setup
```

That command installs the required Claude Code skills (kepano's obsidian-skills + this repo's `/research` skill), registers the user's handle, and creates their People page. After setup they can ingest papers via `/research <url>`.

If a user asks "how do I add a paper to the vault?" — the answer is `/research <url>` (after setup). If they haven't run `/setup` yet, route them there first.

## After setup — what's available

- **`/research <url>` or `/research <url1> <url2> ...`** — ingest one or many papers into the vault. Powered by the universal Researcher prompt at `obsidian/_meta/agents/researcher.md` and the workflows at `obsidian/_meta/skills/research/workflows/`.
- **`/research` with no args** — prompt the user for a topic; do a literature scan (propose candidates, get approval, batch-ingest, write a synthesis).
- **`/research --reconnect <topic>`** — re-link existing papers in `Research/` using current taxonomy. Researcher's restructure authority pass.
- **kepano's obsidian-skills** (5 skills): `obsidian-markdown`, `obsidian-bases`, `obsidian-cli`, `json-canvas`, `defuddle`. Use as needed.

## Conventions to follow when operating on the vault

### Tag taxonomy (6 axes, minimum 5 mandatory + 1 optional)

Every vault note carries at minimum:
- One `#agent/*` (who wrote it — `agent/research`, `agent/lead`, `agent/human`, etc.)
- One `#user/<handle>` (the human who owns the note)
- One `#domain/*` (registered values only: `group-theory`, `ai`, `cs`, `methodology`)
- One-to-many `#topic/*` (substantive subjects; 4-10 typical, no upper bound, substance test mandatory)
- One `#status/*` (`draft`, `review`, `validated`, `rejected`, `superseded`; plus experiment-specific values)

Optional sixth axis: `#project/*` (when scoped to a named workstream — currently `b25`, `b43`, `b53`, `mixer-core`).

Full taxonomy: `obsidian/_meta/tags.md`. Don't invent new domain values; register first.

### Vault language is English

Translate non-English source content to English. Mark translated abstracts and quotes with `[trans.]`. Source language goes in `language:` frontmatter. Don't preserve original-language text in the vault — readers needing it follow the source URL.

### Per-user `Agents/` subtrees

The `obsidian/Agents/` tree is divided by user handle. Maria's is at `obsidian/Agents/maumayma/`. When a new user runs `/setup`, they get their own subtree at `obsidian/Agents/<handle>/`. **Never write into another user's `Agents/<other>/` subtree.**

### Cross-linking discipline (Phase 9 doctrine)

Every content note in `Research/` ends with a `## Related material` section containing **at least 3 substantive wikilinks**:
- Parent overview (the `<subject>-overview.md` for the note's subdir)
- Relevant MOC (`Research/<Domain>/_MOCs/_moc-<topic>.md`)
- One or more substantive siblings/concepts/papers

A note with zero outgoing wikilinks is incomplete. Full rules at `obsidian/_meta/research-folder-convention.md` § "Cross-linking discipline."

### Wikilink-like placeholders must be backticked

In example/template content, write `` `[[<placeholder>]]` `` not bare `[[<placeholder>]]`. The bare form creates phantom orphan nodes in Obsidian's graph view. Applies to templates, agent prompts, scratch briefs, conventions.

### Naming conventions

Public-facing notes have uniquely-identifying filenames (no `_overview.md`, `results.md`, `data.md` alone — qualify with subject). Internal housekeeping files (`log.md`, `README.md` in agent dirs) keep generic names because they're path-qualified. Full rules at `obsidian/_meta/naming-conventions.md`.

### No commits without explicit human approval

If you're operating on the vault and a change feels commit-worthy, ASK the human first. The vault is shared; uncoordinated commits are bad. The exception is the once-only `/setup` registration commit, which is pre-authorized in that command's flow.

## Repo structure

```
<repo-root>/
├── README.md                      ← colleague-facing walkthrough (read this if unsure what this repo is)
├── CLAUDE.md                      ← this file
├── .claude/commands/setup.md      ← the /setup ritual
├── .gitignore                     ← repo-root gitignore (defensive)
└── obsidian/                      ← THE VAULT — operate here
    ├── README.md
    ├── _meta/                     ← doctrine: taxonomy, agent prompts, conventions, /research skill
    ├── _templates/                ← paper-summary, concept-note, synthesis, etc.
    ├── Agents/<handle>/           ← per-user agent home dirs
    ├── Architecture/Mixer/        ← code architecture + Bases dashboards
    ├── Concepts/                  ← reusable concept hubs
    ├── Experiments/               ← pre-registered experiments
    ├── People/                    ← contributor index
    ├── Research/                  ← paper summaries + MOCs + syntheses
    └── .obsidian/                 ← Obsidian config (shared via git; per-machine state is gitignored)
```

## Two ways to use this repo

1. **`/research` skill** (most contributors): just ingest papers. Setup once, then `/research <url>` per paper. The skill handles everything.
2. **Maestri canvas with 6 persistent agents** (Maria + Mixer codebase work): a heavier workflow for implementation, experiments, math validation, code review, and the commit ritual. Documented at `obsidian/_meta/canvas-setup.md`. You probably don't need this.

## Where to look first

- **For doctrine questions**: `obsidian/_meta/` (mission, tags, conventions, agent prompts)
- **For templates**: `obsidian/_templates/` (paper-summary, concept-note, synthesis, experiment, code-review, component-doc, decision)
- **For the `/research` skill internals**: `obsidian/_meta/skills/research/{SKILL.md,INSTALL.md,workflows/}`
- **For the Maestri agents' role prompts**: `obsidian/_meta/agents/`
- **For existing content**: `obsidian/Research/`, `obsidian/Concepts/`, `obsidian/Experiments/`

## Bottom line

If you're not sure what the user wants, point them at `/setup` if they're new, or `/research <url>` if they have a paper in hand. Most other vault operations should happen through the `/research` skill workflows. Direct vault writes outside the skill should be rare and surgical.

Welcome.
