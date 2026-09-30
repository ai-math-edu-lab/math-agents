---
title: SageMath
kind: system-tool
upstream: https://www.sagemath.org
license: GPL-3.0-or-later
ownership: upstream-pristine
obtain: system install; not installed on maumayma's machine as of canvas-setup (probe with `which sage`)
build: none
test: "`sage --version`"
versions_in_use: []
local_patches: []
capabilities:
  - "commutative algebra: Gröbner bases, polynomial ideals (via Singular)"
  - "number theory and general symbolic computation"
  - "group theory: via its bundled GAP"
heavy_processes: [sage]
mcp: none
local_checkouts: {}
docs: ""
used_by: []
tags: [meta, type/reference]
---

# SageMath

## What it is
A general computer algebra system that wraps GAP, Singular and more. Validator uses it for claims outside pure group theory, such as Gröbner bases and polynomial ideals.

## Known pitfalls
It may not be installed, so probe first. If it's missing, escalate the install via Lead; never substitute a hand-rolled implementation.

## Related material
- [[projects-and-dependencies-convention]]
- [[dep-gap]]
- [[validator]]
