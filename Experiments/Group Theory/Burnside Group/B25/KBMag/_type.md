---
title: KBMag on B(2,5)
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: kbmag
status: inconclusive
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/word-problem, project/b25, status/inconclusive, experiment-type]
---

# Experiment Type — KBMag on B(2,5)

## What this technique is

KBMag ("Knuth-Bendix on Monoids and Groups") is a C software package implementing the Knuth-Bendix completion algorithm for finitely-presented groups. The standalone binary `kbprog` takes a group presentation (generators + relations) in its own input format and attempts to complete it to a confluent terminating rewriting system. A confluent system would solve the word problem: given any two words, reduce both to their unique normal form and compare.

For B(2,5) the presentation file is `kbmag_v1/standalone/kb_data/b25_full` (59 equations, words up to length 5 raised to the 5th power). `kbmag_v1/` is the **main** KBMag directory across the project — used by the B(2,5) mixing experiments (`experiments/burnside/b25_kbmag/b25_mix.py:54-55`, `b25_mix_v2.py:53-54`), as well as B(4,3) (`ui/scripts/b43_mix.py`, `mixer-core/examples/b43_experiment.rs`), the SL series (`experiments/sl/`), and Gröbner (`experiments/g_kbmag/`). `kbmag_source/` is **barely used** — only by a few narrow B(2,5) biased-KB code paths: `experiments/b25_reduce_core/run_biased_agents.sh:6-7`, `experiments/burnside/b25_bias_bidir/scripts/run_biased_agents.sh`, and `experiments/burnside/burnside_bidirectional/configs/b25/biased_comm_13_10.toml`. Note: `experiments/burnside/b25_kbmag/` is currently untracked in git (working-copy only) — its code may not survive a clean clone; discuss with the human before any work depends on its long-term presence. `kbmag_debug/` has been deleted.

### Word orderings

Two orderings are used in parallel:

- **RPO (recursive path ordering, `-rec`)** — based on a fixed precedence on generators. Tends to orient rules toward larger reductions but produces longer LHS strings. Rule banks grow very large but never cascade to confluence on B(2,5).
- **Shortlex (`-lex`)** — length-lex. Produces shorter LHS strings and a different structural view of the same equations. Also fails to complete B(2,5) but produces complementary rules.

### Mixing strategy (the interesting part)

The B(2,5) KBMag experiments do not just run `kbprog` standalone. They run **RPO + shortlex simultaneously** (two processes) and periodically inject overlap-scored shortlex rules into the RPO process via SIGUSR1. This is the same strategy that achieves 37% speedup for B(4,3).

Scoring: shortlex rules are expanded (uppercase inverses → lowercase power sequences, since a^{-1} = a^4 in B(2,5)), oriented length-decreasing, then scored by the number of prefix/suffix overlaps with RPO's LHS set. Top-K rules are injected. The overlap score captures how useful a rule would be in resolving critical pairs that the RPO system is already working on.

Scoring backends: v1 uses Aho-Corasick automata (fast lookup, high memory ~40–50 GB at 13M rules). v2 uses sorted arrays + binary search (3–5 GB at 13M rules, 15x more frequent injection cadence).

## Why we ran this

The B(4,3) mixing result showed that overlap-scored injection can significantly accelerate KB cascade. B(2,5) is the next harder group: order 5^34 (known finite by Adian–Novikov), but KB completion has never been demonstrated. The question: does mixing show *any* measurable effect (phase change, slowed rule growth, cascade onset) on B(2,5) within hours?

## What "success" means

RPO process reports `confluent: true`, OR rule bank exhibits a clear cascade phase (rules count decreasing toward a stable small set) not seen in the RPO-only baseline.

## Relevant scripts

- `experiments/burnside/b25_kbmag/b25_mix.py` — v1 (Aho-Corasick)
- `experiments/burnside/b25_kbmag/b25_mix_v2.py` — v2 (bisect + cached prep, lower memory)
- `experiments/burnside/b25_kbmag/bench_v3.py` — synthetic benchmark comparing v1 vs v2 at 13M/25M scale
- `experiments/burnside/b25_kbmag/standalone.py` — single-agent baseline runner

## Literature

- [[havas-wall-wamsley-1974]] — provides the B(2,5) presentation file (`kbmag_v1/standalone/kb_data/b25_full`, 59 equations) that `kbprog` reads; the generator ordering determined by this paper governs which rules are "shortlex-small" vs. "RPO-large".
- [[havas-robertson]] — establishes KB completion as a key computational tool for FPGs (§2.9), including Sims's observation that KB sometimes outperforms coset enumeration; the theoretical framework within which kbprog operates.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: KB non-convergence on B(2,5) is expected, but any cascade or phase-change observed would be evidence about the restricted group's word problem structure.
