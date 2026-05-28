---
title: KBMag — directory overview
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
related:
  - kbmag-source
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# KBMag — directory overview

Two KBMag directories live in the repo. They are not interchangeable.

## kbmag_v1/ — the project-wide main installation

`kbmag_v1/` is the **current, actively maintained KBMag installation** used across the project. It is the KBMag version used in:

- Bidirectional search experiments (alongside the Rust engine)
- B(4,3) and B(5,3) mixing experiments
- SL series experiments
- Gröbner basis experiments
- B(2,5) KBMag mixing scripts (`experiments/burnside/b25_kbmag/`, intentionally untracked in git — code is still dirty; do not commit)

`kbmag_v1/standalone/bin/kbprog` is the binary for all of the above. Package directory contains `standalone/`, `gap/`, `doc/`, `tst/`.

This is the primary KBMag component. Any new experiment that needs kbprog should use `kbmag_v1/`.

## kbmag_source/ — narrow secondary (biased-KB B(2,5) only)

`kbmag_source/` is an older KBMag installation retained specifically for the `experiments/b25_reduce_core/` biased-agent workflow. It is the installation that `run_biased_agents.sh` directly references:

```
KBPROG="…/kbmag_source/standalone/bin/kbprog"
KB_DATA="…/kbmag_source/standalone/kb_data"
```

Its scope is narrow: it exists to serve one shell script and the rule banks that script generates. It is not the installation of choice for new work. See [[kbmag-source]] for the component-level detail: what `kbprog` does, the `b25_lifted` presentation format, the command-line flags `run_biased_agents.sh` actually passes, and the `.kbprog.live` output format.

## kbmag_debug/ — deleted

A third directory, `kbmag_debug/`, existed in a prior commit and has since been deleted. It is mentioned here only so future readers don't expect to find it.

## Scope note

The component note [[kbmag-source]] documents what `kbmag_source/` does within `b25_reduce_core`. There is no separate component note for `kbmag_v1/` at this time because the `b25_reduce_core` dependency trace (Phase 1, [[b25-reduce-core-deps-2026-05-22]]) does not touch it. Documentation of `kbmag_v1/` usage belongs with the experiments that use it (bidirectional search, B(4,3)/B(5,3) mixing, etc.).
