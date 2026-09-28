---
name: research
description: "Ingest academic papers into the shared Obsidian vault as structured, queryable summaries. Use when the user asks to summarize a paper, batch-process a list of papers, add a paper to the vault, retag existing summaries, build a connection graph across papers, or tag/link/extract ideas from the user's own notes in Notes/<handle>/. Trigger words: '/research', 'summarize this paper', 'add this to the vault', 'ingest these arxiv papers', 'do a literature pass on...', 'review papers on...'."
---

# /research — Academic Paper Ingestion Skill

## Purpose

Ingest papers from any field into the shared Obsidian Math vault as structured, queryable, connection-graph-rich summaries. The vault is multi-user and multi-domain; this skill produces summaries that scale to thousands of papers without becoming noise.

## Vault location

Find the vault root (the folder containing `_meta/` and `_templates/`) in this order:

1. Your global memory file (`~/.claude/CLAUDE.md` for Claude Code, `~/.codex/AGENTS.md` for Codex) — setup records a `Math vault root: <path>` line there.
2. The workshop default: `~/Desktop/math-agents/obsidian` (Windows: `%USERPROFILE%\Desktop\math-agents\obsidian`).
3. If this skill is installed as a symlink, the vault is the symlink target's `../../..` (the skill lives at `<vault>/_meta/skills/research`).
4. Otherwise ask the user for the local path.

The same memory line records the user's vault handle — use it for `author:` frontmatter and the `#user/*` tag instead of asking every session.

If `obsidian-research` MCP tools are available in this session (Codex, ChatGPT Desktop), prefer them for all vault reads/writes: `load_doctrine`, `fetch_paper`, `search_vault`, `list_tags`, `write_note`, `manage_frontmatter`, `manage_tags`, `lookup_citation`. They already point at the right vault.

## Operating doctrine

Adhere strictly to the **Researcher agent prompt** at:
`<vault>/_meta/agents/researcher.md`

Read it once at the start of every session that uses this skill. It is the source of truth for:
- 6-axis tag taxonomy (`<vault>/_meta/tags.md`)
- Paper summary structure (`<vault>/_templates/paper-summary.md`)
- Concept hubs (`<vault>/_templates/concept-note.md`)
- Multi-paper syntheses (`<vault>/_templates/synthesis.md`)
- Translation discipline (English vault, `[trans.]` convention, no original-language preservation)
- Topic-tagging substance test (4-10 typical, no upper bound, substantive only)
- Citation count discipline (verifiable; no fake quality verdicts)
- Connection-graph frontmatter (`key_concepts`, `extends`, `contradicts`, `replicates`, `cites`, `cited_by`)

## Invocation modes

### 1. Single paper

```
/research <url>
```

Or natural language:
- "Summarize this paper: <url>"
- "Add <arxiv-id> to the vault"

**Workflow**: see [[workflows/single-paper]].

### 2. Batch

```
/research <url1> <url2> <url3>
```

Or natural language:
- "Ingest these papers: <url>, <url>, <url>"
- "Process all five of these arxiv links"

**Workflow**: see [[workflows/batch]]. Each paper gets a separate summary; cross-link them in `extends` / `replicates` / `cites` if relationships are visible.

### 3. No arguments — invoker provides topic or sources interactively

```
/research
```

Or natural language:
- "Help me do a literature pass on B(2,5) reductions"
- "Research the recent work on Buchberger with cooperation"

**Workflow**: see [[workflows/literature-scan]]. Researcher proposes 3-7 candidate sources, the invoker approves, then proceeds.

### 4. Connection-graph pass (re-link existing summaries)

```
/research --reconnect <topic>
```

Or natural language:
- "Re-link all the burnside papers with the new taxonomy"
- "Build connection graph across the recent additions to Research/AI in Math/"

**Workflow**: see [[workflows/connection-pass]]. No new ingest; only retagging + frontmatter updates + concept hub creation across existing notes.

### 5. Personal notes pass (the invoker's own ideas and logs)

```
/research --notes [all|<path>]
```

Or natural language:
- "Tag and link my notes"
- "Pull the ideas out of my B25 log"

**Workflow**: see [[workflows/personal-notes]]. Operates only on `Notes/<invoker>/`. Tags + fills the fenced *Related material* block of `ideas/` and `logs/` notes (never rewrites their body), and extracts ideas / open questions into `Notes/<invoker>/extracted/`. Convention: `_meta/notes-folder-convention.md`.

## What this skill does NOT do

- **Does not propose code.** Researcher never writes implementation.
- **Does not run experiments.** Researcher writes durable understanding; experiments belong to other roles.
- **Does not commit to git without approval.** The vault is under git and shared; propose a commit and wait for the invoker's explicit OK.
- **Does not invent quality verdicts.** `quality_notes` only when there's something specific to say.
- **Does not invent project relevance.** A paper's relevance to any specific project is not part of the default summary. Add project framing only if the invoker provides a brief.
- **Does not preserve original-language source text** in the vault. Translate to English, mark with `[trans.]`, record source language in `language:` frontmatter.
- **Does not create notes with generic filenames.** Every paper gets a uniquely-identifying name: `<first-author>-<year>.md`, `<first-author>-<coauthor>-<year>.md`, or `<arxiv-id>.md`. Never `paper.md`, `note.md`, `summary.md`, `results.md`, `data.md`, or `_overview.md`. See `_meta/naming-conventions.md` for the full rule set.

## Output

For each paper ingested:
- One paper note at `Research/<domain>/<topic-path>/<paper-id>.md` using the [[paper-summary]] template
- Possibly one or more `Concepts/<concept-name>.md` stubs (if concepts appear in 2+ papers and don't yet have hubs)
- Frontmatter updates to other paper notes (for `cited_by`, `extends`, etc. — bidirectional links)

For literature scans:
- One synthesis note at `Research/<domain>/_synthesis-<topic>.md` using the [[synthesis]] template
- All paper notes covered, linked from the synthesis

## Reporting back to the invoker

After completion, tell the invoker:
- Path(s) to the new note(s)
- Key topic tags applied
- Concept hubs created (if any)
- Open questions surfaced
- Any blockers (e.g. PDF was image-only and `nuextract-cli` is unavailable)

Keep the report concise — the durable record is in the vault, not in chat.

## Tooling

- `defuddle <url>` — default for web ingest. Especially good for arxiv.
- `WebFetch` / `WebSearch` — fallback for paywalled or unusual sources.
- `nuextract-cli <pdf> <schema>` — image-only PDFs (flag to user if unavailable; do not load HuggingFace transformers directly).
- `Read` / `Grep` / `Glob` — vault grounding (check for prior coverage, find related notes).
- `Write` / `Edit` — vault writes. Use full vault-relative paths.
- `obsidian` CLI — if available; full vault paths mandatory.

## Multi-user discipline

- The invoking user's handle becomes `author:` in frontmatter.
- If the invoker hasn't registered a `#user/<handle>` in `<vault>/_meta/tags.md`, ask them their handle and register it before tagging the paper.
- Each user has their own `Agents/<user>/Researcher/` home dir (created on first use). Scratch and logs go there.
- Never write into another user's `Agents/<other>/Researcher/` dir or `Notes/<other>/` dir.

## Stop conditions

- Source URL unreachable / paper unavailable → ask the invoker for an alternative source or local PDF.
- PDF is image-only and `nuextract-cli` is unavailable → flag to invoker, ask whether to skip or wait for tool install.
- Vault path doesn't exist on local machine → ask invoker for the correct path before proceeding.
- Domain is brand-new (no `#domain/*` value matches) → register the new domain in `<vault>/_meta/tags.md` first, then tag.
- Paper appears to be a duplicate of an existing summary → flag to invoker, ask whether to update or skip.

## Bottom line

Each summary's value is **retrieval over time**. Topic tags + connection-graph frontmatter + clean Abstract/TL;DR are the high-leverage fields. Everything else is supporting detail.
