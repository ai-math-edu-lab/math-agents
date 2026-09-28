---
tags: [meta, convention]
---

# Notes folder convention

`Notes/` holds **human-authored living notes** — idea notes and experiment logs that their author keeps editing over time. It is committed to git (shared), unlike the gitignored `Agents/` tree.

## Layout

```
Notes/
└── <handle>/
    ├── ideas/       ← idea notes (human-owned)
    ├── logs/        ← experiment / work logs (human-owned; dated `### YYYY-MM-DD` entries)
    └── extracted/   ← agent-written: ideas and open questions pulled out of ideas/ and logs/
```

Template: `_templates/personal-note.md`.

## Ownership

- `Notes/<handle>/` belongs to that user. Nobody — human or agent — writes into another user's `Notes/<other>/`.
- **Bodies of `ideas/` and `logs/` notes are mutable only by their author.** Agents may edit only:
  - frontmatter tags (add/fix; never strip `author:` or `#user/*`),
  - the fenced block between `<!-- agent:related -->` and `<!-- /agent:related -->`.
- `extracted/` is agent-written (`#agent/research`) on the author's behalf; the author may edit or delete these freely.

## Tagging

- `ideas/` and `logs/`: `#agent/human`, `#user/<handle>`, one `#domain/*`, one+ `#topic/*`, `#status/draft` (or `review` / `validated` / `superseded`). `#project/*` when scoped to a workstream.
- `extracted/`: `#agent/research`, `#user/<handle>`, `#domain/*`, `#topic/*`, `#question` for open questions, `#status/draft`.

## Naming

Globally unique kebab-case filenames per [[naming-conventions]] Rule 1 — e.g. `b25-kbmag-run-log.md`, `wqo-termination-idea.md`. Never `ideas.md`, `log.md`, `notes.md`.

## Cross-linking

- Every `extracted/` note ends with `## Related material` carrying ≥3 substantive wikilinks: its source note (with entry date), plus relevant `Research/`, `Concepts/`, MOC, or `Experiments/` notes.
- `ideas/` and `logs/` notes get their links inside the agent-maintained block; the ≥3-link rule is a target, not a blocker, for raw logs.

## Agent support

`/research --notes [path|all]` — see `_meta/skills/research/workflows/personal-notes.md`. Tags, cross-links, and extracts; never commits without the author's approval.

## Graduating an idea

When an idea matures into something colleagues should build on, promote it into `Research/<Domain>/` as a `_synthesis-<topic>.md` (see `_templates/synthesis.md`), keeping `author:`, and link back to the source note. The original stays in `Notes/`, status `superseded` if fully absorbed.

## Related material

- [[naming-conventions]]
- [[research-folder-convention]]
- [[tags]]
