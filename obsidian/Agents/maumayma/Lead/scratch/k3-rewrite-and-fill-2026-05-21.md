---
tags: [agent/lead, domain/infra, status/draft]
---

# K3 Rewrite + Requirements/Strategies Fill — 2026-05-21

> Tracking note. Three concurrent tasks; one row per planned note/output. Status flips to validated once Lead reviews.

Doctrine link: [[_common]] § K3 pattern. Template: [[component-doc]] (new shape).
Prior bootstrap: [[architecture-bootstrap-2026-05-20]] (these notes are the rewrites).

## Task 1 — K3 rewrite of existing 18 notes

Body must be prose. Frontmatter holds public_api list + invariants (with {id, summary, why}) + related + tests + known_issues. No TypeName(file:line) lists in body. Why-paragraph mandatory for each invariant.

### Lead (me)
| Note | Status |
|------|--------|
| Architecture/Documentation/Overview/00-system-overview.md | rewriting now |

### Developer (delegated)
13 component notes under Architecture/Components/, K3 shape, prose body. Brief sent 2026-05-21.

### Experimenter (delegated)
4 data-pipeline notes under Architecture/Data pipeline/, K3 shape, prose body. Brief sent 2026-05-21.

## Task 2 — Architecture/Documentation/Requirements/ (delegated to Developer)

Five notes:
- runtime-environment.md — OS, Rust toolchain, Python, uv, Docker.
- rust-dependencies.md — major workspace deps grouped by purpose; load-bearing first.
- python-dependencies.md — analytics + scripts pyproject deps.
- environment-variables.md — every env var by component, with default + reader.
- infra-services.md — docker-compose services + dependencies.

All K3 narrative bodies. Sources: root CLAUDE.md, docker-compose.yml, Cargo.toml, pyproject.toml, analytics/.env.example, config.rs.

## Task 3 — Strategies/Existing strategies/ (delegated to Developer)

For each strategy running on the 2 Binance instances: one note in Strategies/Existing strategies/<strategy>.md. K3-style frontmatter with exchange/instance_tag/instance_id/symbols/perf fields. Narrative body explaining what the strategy does and what an operator needs to know. Read-only access to SQLite + ClickHouse.

## Review protocol — K3-specific (strict)

For each note returned, reject (NEEDS WORK) if any of:
- Body is not prose — still has TypeName(file:line) lists.
- Any invariant lacks a why-paragraph in the body.
- public_api list is missing or lives in body instead of frontmatter.
- No wikilinks to neighbors.
- Generic grep-output style anywhere in narrative sections.

No leniency — the K3 shape IS the rewrite.

## Done condition

- 18 K3-validated notes (13 components + 4 data-pipeline + 1 overview)
- 5 Requirements/ notes (validated)
- N Strategies/Existing strategies/ notes — count determined by SQLite inventory
- Tracking note flipped to status/validated