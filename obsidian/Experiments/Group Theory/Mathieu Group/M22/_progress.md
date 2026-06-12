---
title: M22 experiment progress
domain: group-theory
project: m22
instance: M22
status: pending
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/mathieu, topic/m22, project/m22, status/pending, experiment]
---

# M22 Experiments — Progress

The **Mathieu group M22**: sporadic simple group, order 443,520.

## Status

Exploratory. A completed KB run (`m22_rpo.kbprog.live`, 2.4MB) exists in `kbmag_v1/standalone/kb_data/`, along with GAP verification scripts in `experiments/e_kbmag/`. No mixing experiment is documented. The driver script that produced the KB run is **missing**.

## What exists

| Item | Location | Status |
|---|---|---|
| M22 presentation | `kbmag_v1/standalone/kb_data/m22` (4KB) | Input |
| M22 RPO presentation | `kbmag_v1/standalone/kb_data/m22_rpo` (4KB) | Input |
| Completed KB run | `kbmag_v1/standalone/kb_data/m22_rpo.kbprog` (5.6MB) | Generated — driver unknown |
| Rule bank | `kbmag_v1/standalone/kb_data/m22_rpo.kbprog.live` (2.4MB) | Generated |
| Reduce file | `kbmag_v1/standalone/kb_data/m22_rpo.reduce` (3.8MB) | Generated |
| GAP scripts | `experiments/e_kbmag/m22_kbmag.gap`, `m22_setup.gap` | Verification only — no mixing |

## Gaps

- Driver script for the KB run is missing (flag (a) in [[2026-06-02-non-b25-forensic-inventory]] §3)
- No mixing experiment exists for M22
- Full experiment-type docs deferred until mixing experiment is run

## Related material

- [[M23/_progress]] — M23 (same subject family; richer experiment)
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §3 covers M22 forensic provenance
