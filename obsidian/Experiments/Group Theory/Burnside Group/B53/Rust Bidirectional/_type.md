---
title: Rust Bidirectional on B(5,3)
domain: group-theory
project: b53
instance: B(5,3)
experiment_type: bidirectional
status: inconclusive
reconstructed_on: 2026-06-02
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/bidirectional, topic/knuth-bendix, project/b53, status/inconclusive, experiment-type]
---

# Rust Bidirectional Search on B(5,3)

Bidirectional KB-rule word-equality search on B(5,3), implemented in Rust (`experiments/burnside/b53_bidir/`). Uses multiple term orderings simultaneously (RPO, shortlex, wtlex, reverse variants) with dynamic conjugation. More tractable than full KB completion for proving specific word-equality instances.

## Experiment subtree

- [[methodology/rust-bidirectional-b53-2026-06-02|Methodology]] — approach, orderings, dynamic conjugation
- [[data/rust-bidirectional-data-b53|Data]] — target words, run locations, rule bank sources
- [[results/rust-bidirectional-results-b53|Results]] — 144/153 words proved; 3 hardest named

## Related material

- [[B53/_progress]] — B(5,3) umbrella
- [[KBMag/_type]] — KBMag approach (contrast: global completion vs. per-word equality)
- [[B25/Rust Bidirectional/_type]] — B(2,5) analog
