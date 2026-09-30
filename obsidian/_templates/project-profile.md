---
title: Project profile — <project>
project: <project tag value, e.g. b25>
owner: <handle>
repos:
  - "`[[<dep-note for our repo>]]` — <role: experiments / tools / implementation>"
dependencies:
  - "`[[<dep-note>]]` — <read-only | may-modify | accepted-patch-only>"
build: <command(s)>
test: <command(s) — the minimum suite any patch must pass>
smoke: <cheap end-to-end check>
lint: <lint / static-check command(s)>
languages: [<languages / stacks this project uses>]
run_pattern: <exact command pattern, incl. timeout>
runs_dir: runs/<project>/<experiment>/<timestamp>/
provenance_fields: [code SHA, env lock hash, <project-specific extras>]
heavy_processes: [<names beyond the dependency notes' lists>]
protected_interfaces:
  - "<API / protocol / file format> — <why>"
hot_paths:
  - "<code path> — <why it is hot>"
vault_docs:
  components: <vault folder for component docs>
  code_reviews: <vault folder>
  math_validation: <vault folder>
  experiments: <vault folder>
tags: [meta, convention, project/<project>]
---

# Project profile — <project>

## Goal
<What this workstream is trying to establish or build. Link the progress note if there is one.>

## Components under test
<The algorithms, tools and pipelines the project experiments with, and where each lives.>

## Test matrix
| Change kind | Required |
|---|---|
| <kind> | <tests> |

## Protected interfaces — why each one exists
<One paragraph per interface in `protected_interfaces`.>

## Experiment template fields
<Any extra pre-registration fields this project requires on top of `[[experiment]]`.>

## Related material
- `[[projects-and-dependencies-convention]]`
- `[[<dep-note>]]`
- `[[<progress note / overview>]]`
