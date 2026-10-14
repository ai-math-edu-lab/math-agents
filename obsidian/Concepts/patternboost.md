---
title: PatternBoost
author: asetlearning
language: en
tags:
  - agent/lead
  - user/asetlearning
  - domain/ai
  - topic/patternboost
  - topic/hard-instance-generation
  - topic/proof-certificates
  - topic/tokenization
  - topic/trivial-words
  - project/challenge-gen
  - concept
  - status/draft
introduced_in:
  - "[[charton-2024-patternboost]]"
related_concepts:
  - "[[Concepts/certified-instance-generation]]"
appears_in:
  - "[[charton-2024-patternboost]]"
  - "[[patternboost-generation-methodology]]"
  - "[[_synthesis-b25-patternboost-tokenization]]"
---

# PatternBoost

> **Concept hub.** A short anchor for the algorithm. The B(2,5) design details and run results live in [[patternboost-generation-methodology]] and [[patternboost-generation-results]]; this note is the domain-independent view. Source: [[charton-2024-patternboost]] and the owner's design writeup (2026-05).

## Definition

**PatternBoost** ([[charton-2024-patternboost]]) is a search loop that alternates a **local** phase (a cheap local search improves many candidates) and a **global** phase (a transformer trained on the best candidates proposes new ones). At iteration i, with model M_i:

1. **Generate.** S = {M_i^{(k)}(p) | k = 1..N}: N samples from a common prompt p at temperature > 0.
2. **Local search.** S* = {𝓛(c) | c ∈ S}, where 𝓛 : S → 𝒮 maps model output into the search space 𝒮, possibly improving it.
3. **Select.** D̂ = the top-scoring elements of S* under a score R; D_i = τ(D̂), where τ is an optional transform into the model's input format.
4. **Fine-tune.** M_{i+1} = tune(M_i, D_i). Repeat until R ≥ θ or the iteration budget is spent.

The seed set D_0 is typically the best fraction of a large random sample (e.g. the top 50K of 1M).

## The search-space contract (what makes it usable for certified generation)

The model can emit things outside 𝒮. So either membership in 𝒮 is checked and bad outputs rejected, or 𝓛 builds a member of 𝒮 **algorithmically** from the model output, with the guarantee proved once for the construction. For hard instances the check is as hard as the problem itself, so only the second option works: the representation must make every decodable output valid. This is [[Concepts/certified-instance-generation]] — "the proof of the property is in the process itself".

In the B(2,5) generator this is done with **factor words**, w = ∏ cᵢ⁻¹ R_{kᵢ} cᵢ over trivial relators: the model emits only (relator index, conjugator) tokens, local search only makes triviality-preserving moves, and the factor word is the certificate. See [[patternboost-generation-methodology]].

## Design choices that recur

- **Representation / tokenizer** T (word → tokens) and T⁻¹ (tokens → word): letters, n-grams, BPE tokens, or structural tokens (relator, conjugator letter, separators). The representation is usually **not unique** (e.g. aaabb = g₁g₁g₁g₂g₂ = g₁g₃g₄), so scoring and stopping should act on the decoded object.
- **Score R.** Similarity to target instances (frequency distances: cosine, JS, Hellinger, weighted Jaccard; structural: Levenshtein, n-gram), or a direct hardness proxy. The choice decides what the loop converges to: the B(2,5) Dehn-proxy run drifted to short, easy words ([[patternboost-generation-results]]).
- **Local search.** Greedy (beam 1), beam (width k) or exhaustive over a move set; must preserve 𝒮. Typically the cost bottleneck.
- **Cheap invariant check.** A fast necessary condition on every decoded candidate to catch bugs (for B(2,5): exponent sums ≡ 0 mod 5).

## Why it matters

It is a cheap, accessible alternative to FunSearch/AlphaEvolve-style search ([[romera-paredes-2023-funsearch]]) for constructions where a local search exists, and it disproved a 30-year conjecture in its source paper. For [[project-challenge-gen]] it is the first generator family: it can steer certified trivial words onto a target reliably, but so far all generated words are 2.5-reducible to 1 (no L1 hardness, see [[challenge-gen-success-metrics]]).

## Where it appears

- Introduced in: [[charton-2024-patternboost]]
- Implementations: [[Research/AI in Math/Tools/axplorer]] (reference implementation), [[Research/AI in Math/Tools/patternboost-v1-lineage]] (v1 proof of concept), [[dep-b25-pyproject-agentic]] + [[dep-tcgraph-agentic]] (B(2,5) generator)
- Appears in: [[patternboost-generation-methodology]], [[_synthesis-b25-patternboost-tokenization]]
- Related concepts: [[Concepts/certified-instance-generation]]

## Open questions

- When hard instances are exponentially rare, is there any learnable structure that leads the model to them, or does the model learn the generic structure of its seed set?
- Which score gives a usable gradient toward hardness when every early candidate scores the same on the hardness metric (ρ = 0)?
- Does RL fine-tuning with a composite reward beat the select-and-fine-tune loop?

## References

1. F. Charton, J. S. Ellenberg, A. Z. Wagner, G. Williamson, "PatternBoost: Constructions in Mathematics with a Little Help from AI", arXiv:2411.00566 (2024).
2. AxiomMath, axplorer, https://github.com/AxiomMath/axplorer.

## Related material

- [[charton-2024-patternboost]] — the method paper
- [[_moc-ai-in-math]] — MOC
- [[_moc-hard-instance-generation]] — reading path for the project
- [[patternboost-generation-methodology]] — B(2,5) design
- [[patternboost-generation-results]] — B(2,5) runs
- [[Concepts/certified-instance-generation]]
