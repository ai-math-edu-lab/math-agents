---
title: Projects and dependencies convention
status: draft
tags: [meta, convention]
---

# Projects and dependencies convention

The agent roles (`_meta/agents/*`) are **architecture-neutral**. None of them hardcodes a particular algorithm, codebase, build system or machine path. Everything project-specific lives in two registries, which roles read at task start:

| Registry | Folder | One note per | Answers |
|---|---|---|---|
| **Dependency registry** | `_meta/dependencies/` | external code or tool (repo, library, binary, CAS) | What is it? What can it compute or decide (`capabilities`)? How do I get, build, test and pin it? What must never be edited? Which processes are heavy? |
| **Project profiles** | `_meta/projects/` | active `#project/*` workstream | Which repos and dependencies does this project use? What commands run it? Where do runs go? What goes into the provenance record? Which interfaces are protected? Where do its vault docs live? |

The Mixer (`algo-mixer` / `mixer-core`) is **one dependency and one project among many**. It is no longer the frame the roles are written in.

## How roles use them

1. **Lead's task brief names the active project profile**, e.g. "Project: `[[project-b25]]`". If a brief lacks one, the receiving role asks Lead before touching code.
2. The receiving role reads the profile, and then the dependency notes the profile lists, **before** running or editing anything.
3. Commands, paths, protected interfaces, test matrices and provenance fields come from the profile. Role files state only the generic rule ("run the profile's test command", "record the profile's provenance fields").
4. If the profile is silent or wrong about something, the role probes (`which`, `ls`, `grep`), per [[_common]] § Probe before assuming. The role then reports the gap to Lead, who updates the profile.

## Code lives in repos, not in the vault

- **Experiments/algorithms repo(s):** implementations, experiment runners, analysis scripts, `runs/` output.
- **Tools repo(s):** reusable experimental tools, including future MCP compute services that wrap heavy tools.
- **External repos/libraries:** upstream code we depend on but don't own.
- **The vault** documents all of the above and **never** holds code trees. Short inline scripts in verification notes are fine.

Each repo is registered as a dependency note (`kind: our-repo` or `kind: external-repo`), and each project profile says which ones it uses.

## Pinning: in code, not in the vault

The vault records *which* dependencies a project uses and *how* to obtain them. The **exact versions** are pinned in the code repo, using that ecosystem's native mechanism:

| Kind | Pinning mechanism |
|---|---|
| Python package / git dependency | `pyproject.toml` + `uv.lock` (`uv add "git+<url>@<sha>"`) |
| Rust crate | `Cargo.toml` + `Cargo.lock` (git deps with `rev = "<sha>"`) |
| C / standalone binaries, vendored source | vendored pristine source + `patches/` directory, SHA recorded in a manifest |
| System tools (GAP, Sage, Singular, …) and GAP packages | a manifest in the repo (e.g. `deps.lock` / `tools.toml`) listing version and install source; the version is also recorded per run |
| Heavy or cloud runs | a container image; its digest implies all of the above |

## Provenance record (replaces the old "provenance triple")

Every run records:
- the **code SHA** of each of our repos involved (dirty-tree flag if uncommitted);
- the **environment lock hash** of each lock involved (`uv.lock`, `Cargo.lock`, manifest);
- the **version or SHA of every dependency** the run exercised, plus any local patches applied;
- the **tool/binary versions** that produced the math (e.g. `GAP 4.15.1`, `kbprog @ <build hash>`);
- **where it ran**: host or service, relevant hardware (CPU/RAM/GPU), wall-clock time.

A project profile may add fields; e.g. the Mixer profile requires the `mixer-core` build hash. A future MCP compute service must stamp this record automatically.

## Tool neutrality

General roles have **no preferred tools, languages or architectures**. When a role needs a tool, it:
1. uses what the active project profile names; otherwise
2. searches the registry by `capabilities`; otherwise
3. asks Researcher (via Lead) to identify candidates, and Lead registers the chosen one.

What an existing project used is never a default for a new one. Components built for one project (e.g. a reducer inside `algo-mixer`) can be reused standalone by any other project through their dependency note.

## Dependency rules (all roles)

- **Never edit an external dependency in place.** Changes go through a fork/branch or a patch file in our repo, with Lead approval. A profile may declare a narrow accepted local patch; see [[dep-kbmag]] for the biasing-patch example.
- **Adding a new dependency is a human gate** (per [[_common]] § Stop conditions). Adding one means: write a registry note, pin it in the code repo, and get Lead's approval, which Lead gets from the human.
- **Developer owns integration.** Wrappers, adapters and bindings live in our repos, never inside an upstream checkout.
- **Validator independence.** To certify a result, Validator uses a dependency path independent of the one that produced it (e.g. GAP's word problem rather than the same `kbprog` build), and records which one it used.

## Local checkouts are per-user config

Machine paths never go into shared doctrine. Each human maps registry names to local paths in their **own** agent config: `~/.claude/CLAUDE.md` (Claude Code) and/or `~/.codex/AGENTS.md` (Codex), under a heading `## Math vault — local checkouts`:

```markdown
## Math vault — local checkouts
- vault: /path/to/obsidian
- algo-mixer: /path/to/algo-mixer
- runs root: /path/to/runs     # if not inside the repo
```

A dependency note may list *known* checkouts in its `local_checkouts:` frontmatter, keyed by handle. This is a convenience for shared canvases, not the source of truth. If a role can't resolve a path, it asks the human once and then reuses the answer.

## MCP services

A dependency note's `mcp:` field says whether agents reach the tool through an MCP service.
- `none` (the default) means the tool runs on the shell, following the compute rules in [[_common]].
- `{server, tool_id, scope}` names the service backend that wraps the tool.

Rules for services:
- Prefer **one compute-jobs server** with many backends over one server per tool, so a single job cap covers everything.
- Register each server at **project scope**, in a checked-in `.mcp.json` in the code repo, plus a Codex `config.toml` entry. Don't register per user.
- Machine-specific settings (runs root, job cap, tool paths) go in environment variables.
- Quick checks stay on the shell.
- Validator verifies through a different path than the service that produced the result.

## Templates

- Dependency note: `[[dependency-note]]` (in `_templates/`)
- Project profile: `[[project-profile]]` (in `_templates/`)

## Current entries

- Dependencies: [[dep-algo-mixer]], [[dep-kbmag]], [[dep-gap]], [[dep-sage]]
- Projects: [[project-mixer-core]], [[project-b25]]
- The `b43`, `b53` and `b29` projects don't have profiles yet. Until they do, Lead states repo, commands and provenance fields in the brief. The Mixer-based B43/B53 runs can borrow [[project-mixer-core]]. Lead writes the missing profile the next time that project is tasked.

## Related material

- [[_common]]: shared doctrine that defers to these registries
- [[experiment-folder-convention]]: where experiment notes live in the vault
- [[mission]]: research program and invariants
