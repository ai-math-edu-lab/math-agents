# math-agents

A shared **Obsidian research vault** with an AI **research handle**: tell
Claude Code or Codex to add a paper, and it lands in the vault as a
structured, tagged, cross-linked summary.

> 🤖 **For AI agents:** if a user asked you to clone this repo and start the
> setup — open **[`SETUP.md`](SETUP.md)** and execute it top to bottom.

## Setup

1. Install [Claude Code](https://docs.claude.com/en/docs/claude-code/overview)
   and/or [Codex](https://developers.openai.com/codex/), plus
   [Obsidian](https://obsidian.md).
2. Open Claude Code or Codex anywhere and paste:

   ```
   Clone https://github.com/ai-math-edu-lab/math-agents repo, start the setup
   ```

   The agent clones the repo to `Desktop/math-agents/`, asks your name, and
   installs the research handle for both tools.
3. Restart Claude Code / Codex, and open the vault in Obsidian:
   File → Open folder as vault → `Desktop/math-agents/obsidian`.

Then, in either tool:

```
/research https://arxiv.org/abs/<some-id>
```

…or just say *"add this paper to the vault: \<url\>"*.

## What's inside

```
math-agents/
├── README.md      ← this file
├── SETUP.md       ← the setup ritual (executed by your AI agent)
├── claude/        ← Claude Code context
├── codex/         ← Codex context + the obsidian-research MCP server
└── obsidian/      ← THE VAULT (open this folder in Obsidian)
```

Inside `obsidian/`:

- **`Research/`** — paper summaries, organized `Research/<Domain>/<Topic>/`,
  plus Maps of Content (`_MOCs/`), syntheses, and the `Papers.base` dashboard
- **`Concepts/`** — reusable concept hubs that many papers link to
- **`Experiments/`** — pre-registered experiments
- **`People/`** — contributor index (one page per handle)
- **`Agents/<handle>/`** — per-user working dirs (private to each user)
- **`Architecture/`** — code docs per project (currently Mixer) + Bases dashboards
- **`_meta/`** — the doctrine: tag taxonomy (`tags.md`), conventions, agent
  prompts, and the research skill itself (`_meta/skills/research/`)
- **`_templates/`** — paper-summary, concept-note, synthesis, …

Every note is English-only and carries `author: <handle>` plus five tag axes
(`#agent/*`, `#user/*`, `#domain/*`, `#topic/*`, `#status/*`) — that's what
makes the vault searchable and the graph view useful. Full rules:
`obsidian/_meta/tags.md`.

## Help

Questions → Maria (`#user/maumayma` in the vault, `@maumayma` on GitHub).
Bugs in the skill/server/doctrine → open an issue here.
