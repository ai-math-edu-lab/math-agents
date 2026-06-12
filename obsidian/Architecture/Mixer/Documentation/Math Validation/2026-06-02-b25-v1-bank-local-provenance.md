---
title: B(2,5) v1 Rule Bank — Local Provenance Check
status: replicated
domain: group-theory
project: b25-comm12-9-reduction
claim: "The v1 KBMag server run rule banks (rpo/input.kbprog.live, shortlex/input.kbprog.live) are physically preserved on the local disk — not only on the remote server at /home/maria/algo_mixing/"
claimant: B25 Forensic Inventory §1 (Experimenter-B25, 2026-06-02); disputed reading: B25 said 'partial', Maria's correction said 'local'
verification_method: direct filesystem check + byte-count comparison against inventory claims
tools_used: [ls -lh, stat -f%z, wc -l, git cat-file, git show HEAD]
author: aksimemor
tags:
  - agent/validator
  - user/aksimemor
  - domain/group-theory
  - project/b25
  - status/replicated
  - proof
---

# Verification — B(2,5) v1 Rule Bank Local Provenance

## The claim

The W2 forensic inventory §1 states: "v1 rule banks ARE preserved locally at `server_logs/rpo/input.kbprog.live` (7.09M rules, 1.2GB) and `server_logs/shortlex/input.kbprog.live` (13.1M rules, 971MB)."

A reading dispute existed between B25 Experimenter ("partial": only input presentations committed, not banks) and Maria's correction ("local": banks physically present on this machine). This is an independent verification of Maria's correction.

## Method

1. Checked filesystem for `.kbprog.live` files under `experiments/burnside/b25_kbmag/server_logs/`.
2. Measured file sizes with `stat -f%z` (exact bytes) and `wc -l` (rule count = line count).
3. Compared to inventory claims.
4. Checked git tree to understand what is vs. is not committed.

## Evidence

### Filesystem check

```
Path: experiments/burnside/b25_kbmag/server_logs/rpo/
  input              3.1K   (committed presentation — same as server_logs/rpo/input in git)
  input.kbprog.live  1176.5M (displayed) / 1,233,626,531 bytes exact
  input.kbprog.live.zip  78.0M

Path: experiments/burnside/b25_kbmag/server_logs/shortlex/
  input              3.1K   (committed presentation)
  input.kbprog.live  927M (displayed) / 971,794,954 bytes exact
  slexinput.kbprog.live.zip  119M
```

Both files **exist on disk**. Files found; no missing-file errors.

### Rule count check

```
RPO:      wc -l → 7,091,183 lines = 7.09M rules   (inventory claims 7.09M) ✓
Shortlex: wc -l → 13,121,209 lines = 13.12M rules  (inventory claims 13.1M) ✓
```

### Size check

```
RPO:      1,233,626,531 bytes = 1.23 GB (SI)  ≈  1176 MiB (binary)
          Inventory: "1.2GB"  → ✓ (rounded)

Shortlex: 971,794,954 bytes = 971.8 MB (SI)  ≈  927 MiB (binary)
          Inventory: "971MB"  → ✓ exact in SI
          ls -lh shows "927M" (binary MiB) — same file, different unit
```

The apparent "927M vs 971MB" discrepancy is a units artifact: `ls -lh` on macOS uses binary MiB (1M = 1,048,576 bytes), while the inventory uses SI MB (1MB = 1,000,000 bytes). Both refer to the same 971,794,954-byte file.

### Git tracking status

```
Committed (tracked in git HEAD):
  experiments/b25_kbmag/server_logs/rpo/input        (27a54cbd, 3134 bytes)
  experiments/b25_kbmag/server_logs/shortlex/input   (27a54cbd, same file — identical hash)
  experiments/b25_kbmag/server_logs/b25_scoring.log
  experiments/b25_kbmag/server_logs/logs/shortlex_log.txt

Not committed (untracked, gitignored — on disk only):
  experiments/burnside/b25_kbmag/server_logs/rpo/input.kbprog.live       (1.23GB)
  experiments/burnside/b25_kbmag/server_logs/shortlex/input.kbprog.live  (972MB)
```

**Structural note**: The committed tracked files are under `experiments/b25_kbmag/` (being deleted in the cleanup), while the actual working data is under `experiments/burnside/b25_kbmag/`. These are separate directories. The scripts in `experiments/b25_kbmag/` were likely the development copies; the live run data accumulated under `experiments/burnside/b25_kbmag/`. The forensic inventory correctly references the `burnside/` path.

### Session attribution cross-check

`b25_scoring.log` (from git): lines confirm v1 session ran at remote path `/home/maria/algo_mixing/experiments/b25/runs_b25_mix/`, threshold=20k, batch_frac=0.001, periodic=600s. The local `input` files are the starting presentations that were copied TO the remote server. The `.kbprog.live` files are the SNAPSHOTS of the remote session's rule banks that were copied BACK locally.

`server_logs/logs/shortlex_log.txt` (from git): `CWD: /home/maria/algo_mixing/experiments/b25/runs_b25_mix/shortlex` — confirms remote origin of the shortlex agent. At 60s in scoring log: shortlex=560,619 rules, consistent with shortlex_log tidy cycle growth sequence.

## Verdict

**#status/replicated** — Maria's correction ("local") is confirmed correct.

### Why this verdict

Both `.kbprog.live` files exist on the local disk at `experiments/burnside/b25_kbmag/server_logs/`. Rule counts and sizes match the forensic inventory precisely. The "local vs. partial" dispute arose from a framing issue:

- B25's "partial": technically correct in a git sense — the input presentations ARE committed, but the large rule banks are NOT committed (they're gitignored/untracked on disk).
- Maria's "local": correct in the physically-relevant sense — the ~2.2GB of rule banks are on this machine's disk, not exclusively on the remote server.

For storage/backup purposes, **Maria's framing is the operationally important one**: the 2.2GB banks are local (backed up here), not remote-only. The "partial" framing is misleading in that context.

#status/replicated because this is a filesystem check (existence + byte count), not a mathematical proof. The files exist and match; no theoretical verification of their mathematical content was performed.

## Notes for downstream agents

- **For Lead**: §1 of the W2 inventory is correct. Size measurements match (SI vs MiB units explain the apparent shortlex discrepancy). Path note: live banks are at `experiments/burnside/b25_kbmag/`, not `experiments/b25_kbmag/` — Developer's storage spec should target the `burnside/` path.
- **For Developer**: The `.zip` companions exist (`input.kbprog.live.zip` at 78MB for RPO; `slexinput.kbprog.live.zip` at 119MB for shortlex) — already compressed. Storage spec should note these zip companions.
- No math correctness issue found. This is a provenance/bookkeeping verdict only.
