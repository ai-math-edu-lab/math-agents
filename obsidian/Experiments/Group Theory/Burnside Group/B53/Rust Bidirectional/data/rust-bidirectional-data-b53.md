---
title: Rust bidirectional data — B(5,3)
domain: group-theory
project: b53
instance: B(5,3)
experiment_type: bidirectional
status: inconclusive
reconstructed_on: 2026-06-02
author: maumayma
params_bidir_orderings: rpo,shortlex,wtlex,rpo-r2l
params_bidir_target_words: 153
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/bidirectional, project/b53, status/inconclusive, data]
---

# Data — Rust Bidirectional Search on B(5,3)

## Target words

- **File**: `experiments/burnside/b53_bidir/b53_relators.txt`
- **Count**: 153 words — word-equality instances to prove in B(5,3)
- **Format**: one word per line in {a,b,c,d,e,A,B,C,D,E} (generators and inverses)
- **Three hardest** (unproved in v5 at 1733s): `EaceAdBDbaECAecbDBdC`, `ECbcBeadADEbCBcedaDA`, `AbaBEbABaeCAbaBebABaEc`

## Rust source and binary

- **Source**: `experiments/burnside/b53_bidir/src/bin/b53_bidir.rs`
- **Binary**: compiled at `experiments/burnside/b53_bidir/target/release/b53_bidir` (~81MB compiled; dominates disk for this dir)
- **Cargo.toml**: `experiments/burnside/b53_bidir/Cargo.toml`
- **Python orchestration**: `experiments/burnside/b53_bidir/b53_bidir.py` (launch script)

## Rule bank sources

The v5 bidirectional search accumulates rule banks from 4 ordering agents. No pre-built banks on disk for v5 — banks are generated at runtime.

**v1/v2 baseline runs** (on-disk rule banks, shortlex only):

| Run | Path | KB rules | Interrupted at |
|---|---|---|---|
| v1/v2 baseline | `runs/b53/20260320_051415/kb_shortlex/input.kbprog.live` | ~123K rules | 23MB |
| v1/v2 baseline | `runs/b53/20260320_052723/kb_shortlex/input.kbprog.live` | ~123K rules | 24MB |

Both baselines used `run17_shortlex_only.toml` (deleted from disk; was in `experiments/burnside_bidirectional/configs/b53/`).

**Wtlex source note**: Source-3 (wtlex, 2.3M rules) is the key source for the hardest words — proved words 119–144 after its rule bank built. The wtlex bank is not preserved on disk for v5.

## kbprog params (v1/v2 baseline)

```
kbmag_v1/standalone/bin/kbprog -v -me 10000000 -ms 20000000 -t 5000 -cn 100000 -lex input
```

Note: v1/v2 used `-lex` (shortlex only); v5 uses multiple orderings managed by the Rust mixer.

## Run locations

| Run | Path | Size | Status |
|---|---|---|---|
| v1 baseline | `runs/b53/20260320_051415/` | 23MB | Interrupted — shortlex rule bank only |
| v2 baseline | `runs/b53/20260320_052723/` | 24MB | Interrupted — shortlex rule bank only |
| v5 (4 orderings) | No output directory on disk | — | Progress in vault memory only; 144/153 at 1733s |

## Strategy configuration (v5)

The `b53_bidir.rs` driver encodes 4 ordering sources and dynamic conjugation. Details in source at `src/bin/b53_bidir.rs`. No config files on disk for v5 (configs in deleted `burnside_bidirectional/configs/` dir).

## Related material

- [[Rust Bidirectional/_type]] — parent experiment-type
- [[B53/_progress]] — B(5,3) umbrella
- [[methodology/rust-bidirectional-b53-2026-06-02]] — methodology
- [[results/rust-bidirectional-results-b53]] — results table
- [[2026-06-02-non-b25-forensic-inventory]] — §2a–2c forensic provenance
