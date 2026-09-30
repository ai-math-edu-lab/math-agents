---
title: <dependency name>
kind: <our-repo | external-repo | python-package | rust-crate | c-binary | gap-package | system-tool>
upstream: <URL or "system package">
license: <license>
ownership: <we-own | upstream-pristine | upstream-with-accepted-patch>
obtain: <package-manager command pinned to a version / git dependency at a SHA / system install / vendored under <path>>
build: <build command, or "none">
test: <test command, or "none">
versions_in_use:
  - "<version or SHA> — <which project / since when>"
local_patches:
  - "<path of patch> — <what it changes, who approved, when>"
capabilities:
  - "<domain>: <what it can compute or decide, and in which object/model>"
heavy_processes: [<binary names that count toward the compute cap>]
mcp: none   # or {server: <mcp server name>, tool_id: <backend id>, scope: <local | cloud>} once a service wraps this tool
local_checkouts:
  <handle>: <path>
docs: "`[[<vault doc overview>]]`"
used_by: ["`[[<project-profile>]]`"]
tags: [meta, type/reference]
---

# <dependency name>

## What it is
<One paragraph: what it computes / provides, and why we depend on it.>

## How we use it
<Which projects, which parts (binaries, APIs), and through which wrapper in our repos.>

## Protected surfaces
<What must not be changed or broken: file formats, APIs, pristine source trees. Why each one matters.>

## Known pitfalls
<Version quirks, the model it actually computes in (e.g. quotient vs free group), performance traps.>

## Related material
- `[[projects-and-dependencies-convention]]`
- `[[<project-profile>]]`
- `[[<docs overview>]]`
