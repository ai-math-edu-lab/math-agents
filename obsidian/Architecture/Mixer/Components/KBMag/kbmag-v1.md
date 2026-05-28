---
title: kbmag-v1
path: kbmag_v1/standalone/
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "kbprog (kbmag_v1/standalone/bin/kbprog) — Knuth-Bendix completion engine binary"
  - "kbmag_v1/standalone/kb_data/ — group presentation files for all active experiments"
invariants:
  - id: project-wide-main
    summary: "kbmag_v1/ is the canonical KBMag installation for all new and active experiments. Do not direct new callers to kbmag_source/."
    why: "kbmag_source/ is an older installation kept for one specific legacy workflow (b25_reduce_core biased-KB runs via run_biased_agents.sh). For every other experiment — B(4,3) mixing, B(5,3) bidir, SL series, G5/E35/M23, and B(2,5) mixing — kbmag_v1/ is the binary in use."
  - id: kb-data-read-only
    summary: "kbmag_v1/standalone/kb_data/ presentation files are read-only input. Callers must never mutate them in-place; create a per-run copy if the ordering must change."
    why: "Multiple experiments run concurrently against the same presentation files. Mutating a file in-place would corrupt another running job. The correct pattern (seen in run_biased_agents.sh and KbmagLegacyTransport) is to copy the file to a per-agent run directory and modify the copy."
  - id: ordering-in-config
    summary: "kbprog ordering is controlled by the presentation file's `ordering := ...` field or a command-line ordering flag. It is not a property of the binary."
    why: "The binary supports shortlex, recursive (RPO), wtlex, wreath, rtrec orderings. Callers select ordering by either editing the presentation copy or passing the appropriate flag (-lex, -rec, -wtlex, -wreath, -rtrec). A mismatch between presentation and flags silently overrides the presentation."
related:
  - kbmag-overview
  - kbmag-source
  - mixer-core-engine
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# kbmag-v1 — KBMag project-wide main installation

## What it is

`kbmag_v1/standalone/` is the current KBMag installation used by all active experiments. The compiled binary lives at `kbmag_v1/standalone/bin/kbprog`. Group presentation files for all experiments live in `kbmag_v1/standalone/kb_data/`. The package directory also contains `gap/`, `doc/`, and `tst/` — the GAP interface, documentation, and test suite for KBMag.

This is not the same installation as `kbmag_source/`, which is an older version retained for one narrow workflow. See [[kbmag-overview]] for the full two-installation picture.

## Why it exists

All experiment scripts and Rust binaries that run Knuth-Bendix completion reference `kbmag_v1/standalone/bin/kbprog`. The installation is kept in-repo (as a compiled binary in a version-controlled directory) so that experiment results are reproducible — any checkout of the branch sees the same binary. The `kb_data/` presentations define the group structure and are similarly committed.

## How it fits in the system

`kbmag_v1/kbprog` is the Knuth-Bendix engine used by mixer-core's `KbmagLegacyTransport` (Rust) and by all Python experiment scripts that manage kbprog subprocesses directly:

```
Caller (Python script or Rust KbmagLegacyTransport)
 → spawns kbprog with kb_data/<group> + ordering flags
 → kbprog writes rules to <run_dir>/<group>.kbprog.live while running
 → caller reads .kbprog.live live; injects rules to the other agent
```

## Confirmed callers (grepped 2026-05-22)

| Experiment | File |
|---|---|
| B(4,3) bidirectional | `experiments/burnside/b43_bidirectional/b43_bidir.py`, `b43_bidir_kb_only.py`, `b43_rpo_to_reducers.py` |
| B(4,3) bidirectional (Rust) | `experiments/burnside/b43_bidirectional/src/bin/b43_rpo_to_reducers.rs` |
| B(4,3) KB mixing | `experiments/burnside/b43_kbmag_mixing/b43_mix.py` |
| B(5,3) bidir (Python) | `experiments/burnside/b53_bidir/b53_bidir.py` |
| B(5,3) bidir (Rust) | `experiments/burnside/b53_bidir/src/bin/b53_bidir.rs` |
| B(5,3) KB mixing | `experiments/burnside/b53_kbmag_mixing/v10_scored.py`, `v10_scored_v2.py` |
| B(2,5) mixing (untracked) | `experiments/burnside/b25_kbmag/b25_mix.py`, `b25_mix_v2.py` |
| B(2,5) bidirectional (Rust) | `experiments/burnside/burnside_bidirectional/src/bin/b25_rpo_to_reducers.rs`, `b43_rpo_to_reducers.rs`, `b53_async.rs`, `b53_multi_ordering.rs`, `b53_rpo_to_reducers.rs`, `kb_mixer.rs` |
| SL series | `experiments/sl/experiments/sl_bidir.py` |
| G5/G7 | `experiments/g_kbmag/g5_mix.py` |
| E35 | `experiments/e_kbmag/e35_mix.py` |
| M23 | `experiments/m23_kbmag/*.py` |
| UI scripts | `ui/scripts/b43_mix.py` |
| Mixer Core example | `mixer-core/examples/b43_experiment.rs` |

Note: `experiments/burnside/b25_kbmag/` is intentionally untracked in git — code is still dirty. Do not commit it.

## kb_data presentations

Key presentations confirmed in `kbmag_v1/standalone/kb_data/`:
- **B(4,3):** `b43`, `b43_full`
- **B(5,3):** `b53_full`, `b53_full_extended`, `b53_full_wtlex`, `b53_full_extended_wtlex`, `b53_wtlex`
- **B(2,5):** `b25_full`, `b25_gen`, `b25_gen_bBaA`, `b25_gen_wtlex`, `b25_lifted`, `b25_lifted_rpo`
- **SL series:** `sl311`, `sl35`, `sl43`, `sl44`, `sl45`, `sl52`, `sl53`, `sl62`, `sl72`, `sl37`
- **Other groups:** `m23`, `g5`, `g7`, `e35` (and more)

The `b25_lifted` and `b25_lifted_rpo` here are used by the untracked b25 mixing scripts; the `b25_lifted` used by `kbmag_source/` (for b25_reduce_core biased agents) is a separate copy in `kbmag_source/standalone/kb_data/`.

## Public surface — what callers pass to kbprog

Flags used by the Rust `KbmagLegacyTransport` (see `transport/kbmag_legacy.rs`):

```
kbprog [-lex | -rec | -wtlex | -wreath | -rtrec]
       -t <tidyint> -me <maxeqns> -ms <maxstates> -cn <confnum>
       [extra_flags...] <input_dir>
```

Additional flags used by Python scripts for biased completion:
```
kbprog ... -sw <target_word_file> -sp <prob> -sk <k>
```
(`-sw`, `-sp`, `-sk` are KBMag modifications for special-word biasing — see [[kbmag-source]] for the B(2,5) usage; the same flags apply to other groups.)

## Related

- [[kbmag-overview]] — two-installation split: kbmag_v1 vs. kbmag_source
- [[kbmag-source]] — the narrow secondary installation for b25_reduce_core biased-KB
- [[mixer-core-engine]] — `KbmagLegacyTransport` in transport/kbmag_legacy.rs is the Rust wrapper that spawns kbprog from mixer-core

## Known issues

- `experiments/burnside/b25_kbmag/` is the most active B(2,5) mixing codebase using kbmag_v1, but it is intentionally untracked. Its presentations and flag patterns are not documented here.
- kbmag_v1 has no tracked build system in CI — the binary is committed. A clean rebuild requires running `./configure && make` inside `kbmag_v1/`. The precompiled binary may not match the current platform if moved to a different machine.
