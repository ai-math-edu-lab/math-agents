---
title: Biased KB Agents on B(2,5)
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: biased-kb-agents
status: inconclusive
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/word-problem, project/b25, status/inconclusive, experiment-type]
---

# Experiment Type — Biased KB Agents on B(2,5)

## What this technique is

Biased KB Agents are `kbprog` processes run with the `-sw` (special word), `-sp` (special probability), and `-sk` (kgram length) flags from `kbmag_source` (the modified kbprog binary with biasing extensions). Unlike standard KB runs that treat all equations equally, biased agents are seeded with a specific target word and preferentially generate equations whose LHS or RHS contain k-grams drawn from that word.

The effect: the rule bank grows denser with rules that are locally useful for rewriting the target word, at the cost of broader global coverage. For B(2,5), where no completion is expected, biased agents produce **specialized rule banks** that are more likely to reduce a specific target than general-purpose KB runs at the same rule count.

### Two operating modes

1. **Biased mode** (`-sw target.txt -sp P -sk K`): kbprog runs standard KB but marks a fraction P of tidy equations as "special" if they contain k-grams from target.txt. Special equations are prioritised in further tidy cycles. Varies P (bias strength) and K (kgram length).

2. **Word-equality mode** (`-sw target.txt -sp ~1.0 -sk 6`): extreme bias where nearly all selected equations must contain target k-grams. Effectively: kbprog tries to find rules that equate subwords of the target to shorter forms. Produces very high special-equation percentages (~99%+).

### Key parameter encoding (folder names)

See W2 forensic inventory [[2026-06-02-b25-forensic-inventory]] § Folder-name parameter decoding for the full table. Short version: `sl`/`rpo`/`wt` = ordering, `k<N>` = sk param, `sp<NN>` = sp param × 100, `weq` = word-equality mode, `cn100k` = confnum=100k.

## Why we ran this

The standard KB rule banks (KBMag experiment type) grow monotonically and show no cascade for B(2,5). But the Reduce Core pipeline (rules + braid + beam) shows that existing rule banks DO reduce comm_12_9 from 28,652 to 7,245 chars. The hypothesis: biased rule banks tuned to the specific structural patterns in comm_12_9 (X-core pattern, boundary words, prefix) will provide additional reduction beyond what general-purpose banks achieve.

## What "success" means

A biased rule bank that, when merged with the master bank and applied to the target word, reduces it below the current best (7,245 chars for comm_12_9). Success does not require KB confluence — just better reduction on the specific target.

## Relevant scripts

- `experiments/burnside/b25_bias_bidir/scripts/run_biased_agents.sh` — biased agents targeting X-core patterns; outputs to `b25_reduce_core/runs/` (currently missing from disk)
- `experiments/burnside/b25_bias_bidir/scripts/launch_agents.sh` — biased agents targeting word_4882; outputs to `b25_reduce_core/runs_4882/agents/` (currently missing from disk)
- Driver script for run4/run5 batches: **missing from disk** — see results note

## Relationship to other B25 experiment types

- **Reduce Core**: the consumer. Biased rule banks are merged into the master bank and fed to the Reduce Core pipeline. Biased KB Agents is the rule-generation step; Reduce Core is the reduction step.
- **KBMag**: uses general-purpose (unbiased) `kbprog` via `kbmag_v1`. Biased KB Agents uses `kbmag_source` (modified binary) for biased runs.

## Literature

- [[havas-robertson]] — KB completion framework (§2.9); the `-sw`/`-sp`/`-sk` biasing flags in `kbmag_source` are extensions of standard kbprog that steer which critical pairs are prioritised — within the same computational tradition.
- [[havas-wall-wamsley-1974]] — provides the B(2,5) presentation (59 equations, standard b25_full) used as input for all runs in this experiment type.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes: if biased rule banks can reduce comm_12_9 to the empty word, that constitutes an identity certificate relevant to problem 11.48.
