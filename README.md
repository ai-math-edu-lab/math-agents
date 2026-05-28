# math-agents

A shared **Obsidian vault** + **Claude Code skill** + **Maestri canvas** for the algorithmic-mixing research circle and adjacent research areas. Multi-user, multi-domain — currently centred on group theory (especially B(2,5)), with AI, CS, and methodology papers added by contributors.

This repo gives you two ways to contribute:

1. **`/research` slash command** in any Claude Code session → ingest papers into the shared vault as structured, queryable, connection-graph-rich summaries. Field-agnostic.
2. **Maestri canvas with 6 persistent AI agents** → for the algo_mixing project: implementation, experiments, math validation, code review, commit ritual. Heavier setup; only needed if you're working on the codebase.

Most contributors only need (1). Continue reading for first-time setup.

---

## First-time setup

### Prerequisites (you install these manually, ~5 minutes)

1. **Claude Code** — install from https://docs.claude.com/en/docs/claude-code/overview
2. **Obsidian** — install from https://obsidian.md
3. **Git** — already on your machine if you can read this clone

### Step 1: Clone this repo

```bash
git clone https://github.com/ai-math-edu-lab/math-agents.git
cd math-agents
```

Anywhere on your machine. The path doesn't matter as long as you remember it. A common choice is `~/Documents/Obsidian/math-agents/`.

### Step 2: Open the vault in Obsidian

The vault lives at `<repo>/obsidian/`. Open Obsidian → "Open vault" → "Open folder as vault" → navigate to `<wherever-you-cloned>/math-agents/obsidian/` → Open.

You should see the vault file tree: `_meta/`, `_templates/`, `Agents/`, `Architecture/`, `Concepts/`, `Experiments/`, `People/`, `Research/`.

### Step 3: Start Claude Code in the repo

```bash
cd <wherever-you-cloned>/math-agents
claude
```

Claude Code auto-loads `CLAUDE.md` from the repo root — that file tells it where the vault is and what conventions to follow.

### Step 4: Run `/setup`

In the Claude Code session, type:

```
/setup
```

The setup command:

1. Asks for your full name and a kebab-case handle (e.g. `Anna Petrova` / `anna-p`)
2. Installs the [`obsidian-skills`](https://github.com/kepano/obsidian-skills) collection from kepano (5 skills: obsidian-markdown, obsidian-bases, obsidian-cli, json-canvas, defuddle)
3. Installs this repo's `/research` skill (symlinked from the vault)
4. Registers `#user/<your-handle>` in `obsidian/_meta/tags.md`
5. Creates `obsidian/People/<your-handle>.md` from Maria's template
6. Prints a welcome summary with what's where and what to do next

Restart Claude Code after setup so the skills load.

### Step 5: Try ingesting a paper

```
/research https://arxiv.org/abs/<some-id>
```

The skill fetches the paper, extracts a structured summary using the field-agnostic researcher prompt, tags it with the 6-axis taxonomy, and saves it to `obsidian/Research/<domain>/<topic>/<paper-id>.md`. Open the vault in Obsidian to see it land.

---

## How the vault works

Read these in Obsidian to understand the structure:

- `obsidian/README.md` — vault-internal walkthrough (start here once you've opened the vault)
- `obsidian/_meta/mission.md` — what we're building, three-layer research program
- `obsidian/_meta/tags.md` — 6-axis tag taxonomy (agent + user + domain + topic + status + optional project)
- `obsidian/_meta/research-folder-convention.md` — how `Research/` is organized + cross-linking rules
- `obsidian/_meta/skills/research/SKILL.md` — what `/research` actually does

### The 6-axis tag system in 60 seconds

Every note carries a minimum of 5 tags:

- `#agent/*` — who wrote it (AI agent role or human)
- `#user/<handle>` — which human owns it (always)
- `#domain/*` — broad field (currently: `group-theory`, `ai`, `cs`, `methodology` — Researcher registers new ones as needed)
- `#topic/*` — one to many fine-grained subjects (`burnside`, `word-problem`, `knuth-bendix`, etc.) — this is the connection-graph axis
- `#status/*` — lifecycle (`draft` / `review` / `validated` / `rejected` / `superseded`, plus experiment-specific statuses)

Optional sixth axis: `#project/*` (only for notes scoped to a named workstream).

### How `/research` makes papers searchable

Each paper summary has structured frontmatter (`key_concepts`, `extends`, `contradicts`, `replicates`, `cites`, `cited_by`) that powers Obsidian's graph view and the Bases dashboards at `obsidian/Architecture/Mixer/Bases/`. Once you've ingested a few papers, open **Papers.base** in Obsidian for filtered views by topic / domain / language / status.

For navigation, **Maps of Content (MOCs)** live at `obsidian/Research/<domain>/_MOCs/_moc-<topic>.md` — curated wikilink lists you land on instead of graph view. Currently four MOCs cover Burnside groups, Knuth-Bendix, word problem, and presentations/orders.

---

## Vault language

**English-only.** If your source paper is non-English, the `/research` skill translates the abstract and quotes to English (marked `[trans.]`); original-language text is not preserved in the vault. Source language is recorded in `language:` frontmatter for filtering.

---

## Multi-user norms

- **Every note** has `author: <handle>` frontmatter + `#user/<handle>` tag
- **When citing a colleague**, link `[[People/<their-handle>]]` so credit flows
- **Don't restructure shared dirs** (`Research/`, `Concepts/`) unilaterally — that's Researcher's restructure authority, exercised via `/research --reconnect`. If you think something should move, raise it with Maria
- **Per-user `Agents/<handle>/` subtrees** are private to each user — don't write into someone else's subtree

---

## The Maestri canvas (advanced, optional)

If you're working on the `algo_mixing` codebase, you'll want the 6-agent canvas (Lead, Researcher, Developer, Experimenter, Experimenter-B25, Validator). Setup is documented in `obsidian/_meta/canvas-setup.md`. This is separate from `/research` and you don't need it just to add papers.

---

## Repo structure

```
math-agents/
├── README.md                      ← this file (colleague-facing)
├── CLAUDE.md                      ← per-session context for Claude Code in this repo
├── .claude/
│   └── commands/
│       └── setup.md               ← the /setup slash command
├── .gitignore                     ← defensive (also one inside obsidian/)
└── obsidian/                      ← THE VAULT
    ├── README.md                  ← vault-internal walkthrough
    ├── _meta/                     ← taxonomy, agent prompts, conventions, /research skill
    ├── _templates/                ← paper-summary, concept-note, synthesis, etc.
    ├── Agents/<handle>/           ← per-user agent home dirs
    ├── Architecture/Mixer/        ← code architecture docs + Bases dashboards
    ├── Concepts/                  ← reusable concept hubs (multiple papers link here)
    ├── Experiments/               ← pre-registered experiments
    ├── People/                    ← contributor index
    ├── Research/                  ← paper summaries + MOCs + syntheses
    └── .obsidian/                 ← Obsidian config (graph view settings, plugins, etc.)
```

---

## Getting help

- **Questions about the vault or `/research`**: ping Maria (`#user/maumayma` in the vault, `@maumayma` on GitHub).
- **Bug in the skill or doctrine**: open an issue on this repo.
- **Adding a new domain or topic that doesn't fit existing taxonomy**: read `obsidian/_meta/tags.md` § "Axis 3 — `#domain/*`" and § "Axis 4 — `#topic/*`" first. Researcher registers new domains; topics grow organically.

---

## Contributing

For the casual case (adding papers via `/research`): just `/setup` once, then `/research <url>` per paper. The skill handles tagging, structure, and connection-graph wiring.

For deeper contributions (writing new templates, adding new conventions, modifying agent prompts): the changes go via PR on this repo. Read `obsidian/_meta/agents/_common.md` for shared agent doctrine first.

Welcome aboard.
