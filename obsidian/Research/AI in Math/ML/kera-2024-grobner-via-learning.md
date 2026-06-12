---
title: "Gröbner basis computation via learning"
authors: Hiroshi Kera, Yuki Ishihara, Tristan Vaccon, Kazuhiro Yokoyama
year: 2024
venue: "SCSS 2024: 10th International Symposium on Symbolic Computation in Software Science (Works in Progress), CEUR-WS Vol-3754, pp. 51–56, August 28–30, 2024, Tokyo, Japan"
url: https://ceur-ws.org/Vol-3754/paper09.pdf
language: en
domain: ai
status: draft
methodology_type: empirical
citation_count: null
citation_count_date: 2026-06-11
key_concepts:
  - "[[Concepts/grobner-bases]]"
  - "[[Concepts/buchberger-algorithm]]"
  - "[[Concepts/ml-for-symbolic-computation]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[Research/AI in Math/ML/2311.12904|2311.12904]]"
cited_by: []
quality_notes: "Extended abstract / Works-in-Progress companion to the full NeurIPS 2024 paper arXiv:2311.12904 (Kera, Ishihara, Kambe, Vaccon & Yokoyama). This 6-page version omits Kambe as co-author (acknowledged in a footnote: 'not included in the authors due to a technical reason at submission'). Carries the same core ideas as the full paper but with curtailed experimental setup; references [17] = arXiv:2311.12904 for full details. CEUR-WS proceedings are not indexed separately on Semantic Scholar; citation count for this specific proceedings paper is not available — use arXiv:2311.12904 for citation tracking of the research line."
author: ethan-k
tags:
  - agent/research
  - user/ethan-k
  - domain/ai
  - topic/grobner-basis
  - topic/machine-learning-for-mathematics
  - topic/transformers
  - topic/symbolic-computation
  - topic/computer-algebra
  - topic/buchberger-algorithm
  - paper
  - status/draft
---

# Gröbner basis computation via learning

> **Companion note**: this is the 6-page SCSS 2024 Works-in-Progress extended abstract. The full NeurIPS 2024 paper (arXiv:2311.12904) by Kera, Ishihara, **Kambe**, Vaccon & Yokoyama covers the same research with complete experimental setup, full proofs, and extended results. Read that paper for the complete treatment; this note records what this short version specifically contributes and where it differs.

## Abstract

Solving a polynomial system, or computing an associated Gröbner basis, has been a fundamental task in computational algebra. However, it is also known for its notorious doubly exponential time complexity in the number of variables in the worst case. This paper is the first to address the learning of Gröbner basis computation with Transformers. The training requires many pairs of a polynomial system and the associated Gröbner basis, raising two novel algebraic problems: random generation of Gröbner bases and transforming them into non-Gröbner ones, termed as backward Gröbner problem. We resolve these problems with 0-dimensional radical ideals, the ideals appearing in various applications. The experiments show that our dataset generation method is at least three orders of magnitude faster than a naive approach, overcoming a crucial challenge in learning to compute Gröbner bases, and Gröbner computation is learnable in a particular class.

## TL;DR

This short companion paper introduces two novel algebraic sub-problems required for training-data generation — random generation of Gröbner bases and the backward Gröbner problem — and shows that solving both for 0-dimensional radical ideals (using shape-position structure and Bruhat decomposition) enables a dataset pipeline orders of magnitude faster than forward computation. A standard Transformer trained on the resulting data achieves 91–96% accuracy on rational-coefficient instances with up to 5 variables, while finite-field accuracy lags significantly. This 6-page version is distinguished from the full paper mainly by its curtailed experimental reporting and by the omission of co-author Kambe.

## Problem

Computing Gröbner bases is NP-hard with doubly exponential worst-case complexity in the number of variables. Applying machine learning to this task requires large training sets of (non-Gröbner set, Gröbner basis) pairs — but generating such pairs naively requires computing Gröbner bases forward, which is prohibitively expensive at the scale needed for ML training (millions of samples). The paper asks: can a backward generation strategy (generating the Gröbner basis first, then transforming it to a non-Gröbner input) make training-data creation tractable, and if so, does a Transformer actually learn to compute Gröbner bases in a restricted class?

## Approach

Two new algebraic sub-problems are formalized and solved (§2):

**Problem 2.1 — Random generation of Gröbner bases.** For 0-dimensional radical ideals, the reduced lex-Gröbner basis is almost always in shape position (Gianni-Mora 1989; Noro-Yokoyama 1999): $G = \{h, x_1 - g_1, \ldots, x_{n-1} - g_{n-1}\}$ with $h, g_1, \ldots, g_{n-1} \in k[x_n]$ and $\deg(h) > \deg(g_i)$. Sampling $n$ random univariate polynomials satisfying this degree condition gives a valid reduced Gröbner basis efficiently.

**Problem 2.2 / Theorem 2.5 — Backward Gröbner problem.** Given a Gröbner basis $G = (g_1,\ldots,g_t)^\top$, find a matrix $A \in k[x_1,\ldots,x_n]^{s \times t}$ with $F = AG$ and $\langle F \rangle = \langle G \rangle$ but $F$ not a Gröbner basis. Key result: $\langle F \rangle = \langle G \rangle$ iff there exists $B$ such that each row of $BA - E_t$ is a syzygy of $G$. For $s = n$ generators in shape position, any $A$ with $\det(A) \in k \setminus \{0\}$ suffices (Proposition 2.6). Random sampling via Bruhat decomposition $A = U_1 P U_2$ (unimodular upper-triangular $U_1, U_2$ and permutation $P$) resolves the backward problem requiring only $\mathcal{O}(s^2)$ polynomial samples and $\mathcal{O}(n^2 + s^2)$ polynomial multiplications.

**Experiments (§3):** 12 datasets $\mathcal{D}_n(k)$ for $n \in \{2,3,4,5\}$ and $k \in \{\mathbb{F}_7, \mathbb{F}_{31}, \mathbb{Q}\}$. Backward generation benchmarked against three SageMath/libSingular forward-generation algorithms. A standard Transformer (6 encoder/decoder layers, 8 attention heads) trained for 8 epochs on 1M samples (prefix representation), tested on 1K samples.

## Key result

**Dataset generation speed (Table 1):** For 1,000 samples, backward generation times (in seconds): $n=2$: 0.003; $n=3$: 0.005; $n=4$: 0.009; $n=5$: 0.014. Fastest forward method (stdfglm): $n=2$: 5.78; $n=3$: 12.6; $n=4$: 44.2; $n=5$: 360. Best forward alternatives hit timeout (>5s/instance) for >13–24% of runs at $n=4,5$. "Our backward generation is significant orders of magnitude faster than the forward generation."

**Transformer accuracy (Table 2):** Accuracy / support accuracy on $\mathcal{D}^-_n(k)$:

| Ring | $n=2$ | $n=3$ | $n=4$ | $n=5$ |
|------|-------|-------|-------|-------|
| $\mathbb{Q}[x_1,\ldots,x_n]$ | 94.6 / 97.9 | 96.1 / 98.6 | 96.2 / 98.6 | 91.8 / 97.9 |
| $\mathbb{F}_7[x_1,\ldots,x_n]$ | 66.6 / 76.6 | 78.8 / 87.6 | 80.9 / 91.1 | 83.2 / 91.4 |
| $\mathbb{F}_{31}[x_1,\ldots,x_n]$ | 44.7 / 82.7 | 58.5 / 89.3 | 73.9 / 93.9 | 80.0 / 93.4 |

Support accuracy = polynomial support (set of terms) correctly predicted, ignoring coefficient values. "Transformers have difficulty determining the coefficients in finite fields."

**Field-dependence observation:** Higher accuracy on $\mathbb{Q}$ than on $\mathbb{F}_p$ despite $\mathbb{Q}$ having more possible coefficient values. For $\mathbb{F}_{31}$ accuracy is lower than for $\mathbb{F}_7$. Conjectured to reflect modular arithmetic difficulty (cf. Grokking literature).

## Assumptions

- 0-dimensional radical ideals are almost always in shape position over infinite fields or finite fields with large field order (Gianni-Mora 1989 result assumed to hold for sampled instances).
- The reduced input density $\sigma$ (0.2–1.0 per variable count) in the training datasets $\mathcal{D}^-_n$ is representative of practical instances — the paper uses $\sigma = 1.0, 0.6, 0.3, 0.2$ for $n = 2,3,4,5$ respectively to keep sequence length below 5,000.
- Coefficient bounds for $\mathbb{Q}$: numerators/denominators $a, b \in \{-5,\ldots,5\}$ for $G$; $a,b \in \{-100,\ldots,100\}$ for $F$. These restrictions are set by the ML framework, not by the mathematics.
- 48-core CPUs, 768 GB RAM, NVIDIA RTX A6000ada GPU environment; runtime figures are hardware-specific.

## Limitations / scope

- **Restricted polynomial class**: experiments are limited to 0-dimensional radical ideals in shape position with low degree and bounded coefficients. General polynomial systems (non-radical, higher-dimensional, or with large coefficients) are outside scope.
- **No full experimental setup reported**: Section 3 explicitly defers to the full version (reference [17] = arXiv:2311.12904) due to space constraints. Ablations, hyperparameters, and extended learning-curve results are absent from this 6-page version.
- **Accuracy is not 100%**: at $n=5$ over $\mathbb{F}_{31}$, only 80.0% of full Gröbner bases are correctly predicted. The paper acknowledges outputs "may be incorrect" but frames this as yielding "a hint of a solution."
- **Not a replacement for exact computation**: the Transformer is proposed as a complement or heuristic accelerator, not a certified exact algorithm.
- **Overlap with full paper**: this companion and arXiv:2311.12904 share their core contributions. Any literature survey should cite the full NeurIPS version for attribution; this note exists to record that the SCSS companion precedes or coincides with the NeurIPS appearance and targets the symbolic-computation community specifically.

## Replication evidence

No independent replication of the Transformer experiments identified. The dataset generation algorithm is mathematically verifiable (shape-position sampling + Bruhat decomposition are algebraically proven). Full code not released in this proceedings version; see the full paper (arXiv:2311.12904) for any released artifacts.

## Why this paper matters

This extended abstract is historically notable as the first published venue-stamped record of the Kera et al. Gröbner-basis learning approach, predating the NeurIPS 2024 full paper in conference appearance (SCSS August 2024 vs. NeurIPS December 2024). Its primary audience is the symbolic-computation community (ISSAC/SCSS) rather than the ML community (NeurIPS), making it a bridge paper that signals the direction of ML-for-symbolic-computation research to an algebraically-oriented readership.

The **core contribution** — solving the backward Gröbner problem via shape-position structure and Bruhat decomposition — addresses a fundamental dataset-generation bottleneck that had blocked ML approaches to Gröbner computation entirely. The three-to-four orders-of-magnitude speedup in dataset generation is the enabling result; the Transformer accuracy numbers are the proof-of-concept that the approach is worth pursuing.

The finite-field vs. infinite-field accuracy gap surfaces an interesting algebraic question: why does modular arithmetic make polynomial coefficient prediction harder, even when the field is smaller? This connects to the Grokking literature and suggests the phenomenon is not just a dataset-size issue.

For the vault's interests: this paper is a natural companion to the group-theory Gröbner-basis work in [[Research/Algorithm Cooperation/grobner|grobner]] (Kreuzer-Myasnikov-Rosenberger), showing that the same Gröbner basis machinery can be approached from an ML angle — learning to compute what the symbolic algorithm computes exactly.

## Quotes

1. > "To our knowledge, neither a random generation of Gröbner basis nor the backward transform from Gröbner basis to non-Gröbner set has been considered in computational algebra." — §2
2. > "The accuracy shows that the learning is more successful on infinite field coefficients $k \in \{\mathbb{Q}, \mathbb{R}\}$ than finite field ones $k = \mathbb{F}_p$." — §3

## Open questions surfaced

- Why does Transformer accuracy decrease for larger finite fields ($\mathbb{F}_{31}$ worse than $\mathbb{F}_7$), contrary to intuition that smaller fields are harder? Is this a modular-arithmetic generalization phenomenon (Grokking)?
- Can the backward Gröbner approach extend beyond 0-dimensional radical ideals to higher-dimensional or non-radical ideals?
- What is the accuracy on unreduced density ($\sigma = 1.0$) for $n \geq 3$? The paper restricts density to keep sequence length manageable — what accuracy is lost?
- Can a Transformer trained on this restricted class serve as a fast heuristic oracle inside a hybrid exact+learned pipeline (e.g., use the Transformer to propose a candidate Gröbner basis, then verify with a symbolic algorithm)?
- The full paper (arXiv:2311.12904) reports additional results not in this short version — what specific results appear only in the NeurIPS version?

## Related material in vault

- Cites / full version: [[Research/AI in Math/ML/2311.12904|2311.12904]] — Kera, Ishihara, **Kambe**, Vaccon & Yokoyama, "Learning to Compute Gröbner Bases," NeurIPS 2024 — the complete paper this 6-page companion condenses and refers to ([17]) for full details; **primary relationship** (this note = conference companion; 2311.12904 = full paper).
- Cross-domain link: [[Research/Algorithm Cooperation/grobner|grobner]] — Kreuzer, Myasnikov & Rosenberger (2025 draft) applies Gröbner bases to the word problem for finitely presented groups; the two papers address the same mathematical object from opposite directions (symbolic application vs. ML to learn computation).
- MOC: [[Research/AI in Math/_MOCs/_moc-ai-in-math|_moc-ai-in-math]]
- Synthesis: [[Research/AI in Math/ML/_synthesis-ml-for-math|_synthesis-ml-for-math]]
- Author: [[People/ethan-k|ethan-k]]
