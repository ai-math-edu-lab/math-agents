---
title: "PatternBoost Generation — experiment type"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: patternboost-generation
author: asetlearning
status: pending
tags: [agent/human, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/trivial-words, topic/hard-instance-generation, project/challenge-gen, status/pending, experiment-type]
---

# PatternBoost Generation (B(2,5))

**Generate words that are trivial in the free B(2,5) by construction**, steered toward target words by a PatternBoost loop ([[charton-2024-patternboost]]). A transformer proposes *factor words* (products of conjugates of relators w⁵). C++ beam local search improves them, a scorer ranks them against target "challenge" words, and the best re-train the model. The factor word is the triviality certificate, so no word-problem solver is needed.

This is the **generation** use of PatternBoost. Do not confuse it with the `#project/b25` PatternBoost line in `Experiments/Group Theory/Burnside Group/B25/PatternBoost/` (maumayma), which uses PatternBoost to *reduce* challenge words.

- Methodology: [[patternboost-generation-methodology]]
- Data and constants: [[patternboost-generation-data]], [[patternboost-generation-constants]]
- Results: [[patternboost-generation-results]]
- Project: [[project-challenge-gen]] · Progress: [[Challenge Generation/_progress]]

## Terms
Project terms (defined once in [[challenge-gen-glossary]], not restated): [[challenge-gen-success-metrics#Notation|certificate, factor word, n, R₂.₅]], [[challenge-gen-glossary#factor, conjugator and relator index|factor, conjugator, relator index]], [[challenge-gen-glossary#standard relators and dataset relators|standard and dataset relators]], [[challenge-gen-glossary#relator map, relator table and relator file|relator map / relator file]], [[challenge-gen-glossary#screen mode and certify mode|screen / certify mode]], [[challenge-gen-glossary#seeds and calibration seed|seeds]], [[challenge-gen-glossary#positive and negative control|controls]], [[challenge-gen-success-metrics]] (D and the levels).

Type-local terms (source: [[patternboost-generation-methodology]], [[patternboost-generation-constants]]):
- **Token stream.** The model's representation of a factor word: `[BOS] ([REL_i] ([CONJ_±k]+ | [CONJ_EMPTY]) [SEP])+ [EOS]`; one `[REL_i]` per relator, one `[CONJ_±k]` per conjugator letter. Optionally compressed with a trained BPE.
- **Pool.** The current set of best factor words, capped at `max_pool_size`; the model is trained on it and local search starts from it.
- **top_k (workflow).** Number of best-scored local-search outputs merged into the pool each iteration (derived: equals `max_pool_size`). Not the sampling `top_k` below.
- **top_k / top_p / temperature (generation).** Standard transformer sampling controls (50, 0.95, 1.0 in the base config).
- **Iteration / epochs.** One iteration = generate, local search, select, fine-tune; `num_iterations` of them. `epochs` = training epochs per fine-tune (10 in the sweep).
- **Local search, beam_width, max_steps.** Beam search over triviality-preserving edits of a factor word (relator swap, conjugator mutation, factor insertion and deletion). `beam_width` = frontier size N (1 = greedy); `max_steps` = number of expansion rounds.
- **num_insert_samples, num_conj_samples, conj_max_len.** Samples tried per insertion move, per conjugator-mutation move, and the maximal conjugator length (5, 5, 4).
- **Challenge / target.** The random factor word's expansion that a trial tries to hit (baseline success = equal up to cyclic rotation within the iteration budget). Not the real HWW challenge words.
- **Sweep, combo, trial.** A sweep is a grid over `beam_width`, `max_steps` and `max_pool_size`; each combination (combo) runs 50 trials, one target per trial.
- **Scorer.** The objective ranking candidates: `hellinger`, `edit`, `dehn_function`, `length_range`, `hybrid`, etc.
- **Generator compression / BPE relators.** Each learned BPE token becomes a new generator g, with g⁵ as a relator; the scorer decodes back to a and b.
