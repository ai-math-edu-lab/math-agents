---
title: kbmag (Knuth-Bendix on monoids and automatic groups)
kind: c-binary
upstream: https://github.com/gap-packages/kbmag
license: GPL-2.0-or-later
ownership: upstream-with-accepted-patch
obtain: "vendored in [[dep-algo-mixer]] as kbmag_source/ (pristine upstream + accepted biasing patch) and kbmag_v1/ (editable working copy); also available as the GAP package `kbmag`"
build: make (inside the vendored standalone tree)
test: none upstream; use GAP `kbmag` package as cross-check
versions_in_use:
  - "vendored copies in algo-mixer — record build hash per run"
local_patches:
  - "kbmag_source/standalone/lib/kbfns.c biasing patch (consider_special, special_rws_reduce, injection path, k-gram machinery) — ACCEPTED local modification, Maria 2026-06-23"
capabilities:
  - "group theory: Knuth-Bendix completion for monoid/group presentations (kbprog); confluent rewriting system if it completes"
  - "group theory: automatic-structure computation (autgroup) for automatic groups"
  - "group theory: word reduction/equality in the group given by the presentation — only when a confluent system exists"
heavy_processes: [kbprog]
mcp: none
local_checkouts: {}
docs: "[[kbmag-overview]]"
used_by: ["[[project-mixer-core]]", "[[project-b25]]"]
tags: [meta, type/reference]
---

# kbmag

## What it is
Derek Holt's Knuth-Bendix / automatic-groups package. Its standalone `kbprog` binaries are the most heavily used compute tool in the Burnside experiments.

## How we use it
- As standalone `kbprog` runs, including as Mixer agents via `KbmagLegacyTransport`.
- Through the GAP `kbmag` package, as an oracle for cross-checks (see [[dep-gap]]).

## Protected surfaces
- **`kbmag_source/` stays bytewise pristine upstream, WITH ONE EXCEPTION.** The biased-agents patch inside `kbmag_source/standalone/lib/kbfns.c` (`consider_special`, `special_rws_reduce`, the injection path, the k-gram machinery) is an accepted local modification (Maria, 2026-06-23). Fixes to that patch are allowed via branch + regression test (fail-before / pass-after) + Lead review + the human's commit gate. Nothing else under `kbmag_source/` is edited, moved or deleted.
- **`kbmag_v1/`** is the editable working copy for non-biasing needs. Edits still require Lead approval.
- **KBMAG file formats** (rewriting-system files, `.kbprog` outputs) are userspace. Don't break them.

## Known pitfalls
- A `kbprog` run that doesn't complete proves nothing about the group. A confluent system for a *finite quotient* is not a result about the free Burnside group; see [[validator]] Step 2.5.
- Record which tree (`kbmag_source` vs `kbmag_v1`) and which build produced a result.

## Related material
- [[projects-and-dependencies-convention]]
- [[dep-algo-mixer]]
- [[dep-gap]]
- [[kbmag-overview]]
