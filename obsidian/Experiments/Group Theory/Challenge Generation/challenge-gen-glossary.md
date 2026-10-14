---
title: "Challenge generation: glossary (B(2,5))"
domain: group-theory
project: challenge-gen
instance: B(2,5)
status: draft
author: asetlearning
date: 2026-10-15
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, topic/word-problem, project/challenge-gen, status/draft, convention]
---

# Challenge generation: glossary (B(2,5))

> **One place for every project term** (profile rule 9, [[project-challenge-gen]]). Owner-defined metric terms get a one-line summary and a link only; the definition stays in [[challenge-gen-success-metrics]] and is not restated or changed here. Terms without another home are defined in full in Part B, precisely enough to implement. Group: **free B(2,5)** (letters a, A = a⁻¹, b, B = b⁻¹; in code 1, −1, 2, −2) unless a line says B₀(2,5). Written 2026-10-15 by the Experimenter from the T-001 and T-002 notes ([[hardness-baselines-results]], [[t002-dataset-relator-products-results]]).

Notation used in the definitions: |u| is word length, w̄ the freely reduced expansion of a certificate, n = |w̄|, R₂.₅(w) the 2.5-reduction of w. Dates are ISO.

## Part A: alphabetical index

| Term | One-line definition | Origin | Full definition |
|---|---|---|---|
| 2.5-power | A subword uᵠ of exponent q = (window length)/(period \|u\|) ≥ 2.5; the only thing the reducer rewrites | owner 2026-10-05; made exact in T-001 | [[#2.5-power and the reducer rewrite]] |
| aut8 / 16 images | The 8 letter automorphisms of F(a,b) (generator swap × sign of each generator), times word inversion = 16 images of a word | owner decision 2026-10-14 (T-001); dataset name from 2026-10-07 | [[#aut8 and the 16 images]] |
| canon | Shortlex-least string over the 16 images and all rotations of a cyclic word | T-002, 2026-10-15 | [[#canon (canonical class)]] |
| cell | One (sampler setting × seed) group of words in a sampling grid; T-001: S1–S7, T-002: P·K·subset names | T-001 2026-10-13, T-002 2026-10-15 | [[#cell and cell names]] |
| certificate | Factor word F = list of (relator index, conjugator) pairs whose expansion is w̄ | owner 2026-10-05 | [[challenge-gen-success-metrics#Notation]] |
| certify mode | 2.5-reduction with all cyclic shifts; used for reported ρ and level | owner 2026-10-05 | [[#screen mode and certify mode]] |
| conjugator | The word c in the factor c⁻¹ R c | PatternBoost design, 2026 | [[#factor, conjugator and relator index]] |
| control (positive / negative) | A set whose metric value is known in advance, used to check the harness | T-001 2026-10-13 | [[#positive and negative control]] |
| cyc(w̄), n_cyc | Cyclic reduction of w̄ and its length | T-001 2026-10-13 | [[#rho_cyc and the cyclic reduction]] |
| D | \|F*\|/\|w̄\|, Dehn-function proxy on the minimised certificate | owner 2026-10-05 | [[challenge-gen-success-metrics#Metric 2: Dehn-function proxy (theoretical difficulty)]] |
| D_raw | \|F\|/\|w̄\| on the unminimised certificate | T-001 2026-10-13 | [[#D_raw]] |
| dataset relators (820) | The 820 proved-trivial, 2.5-reduced words used as relators in T-002 | dataset 2026-10-14 (T-012) | [[#standard relators and dataset relators]] |
| empty-word (R = 1) | R₂.₅(w) is the empty word; the word is not L1 | owner 2026-10-05 | [[#screen mode and certify mode]] |
| F* | Minimised certificate (loop-erased F) | owner 2026-10-05 | [[challenge-gen-success-metrics#Metric 2: Dehn-function proxy (theoretical difficulty)]] |
| factor word | See certificate | owner 2026-10-05 | [[challenge-gen-success-metrics#Notation]] |
| fixed point (of the reducer) | A word on which R₂.₅ returns the word itself up to rotation | T-001 2026-10-13 | [[#fixed point of the reducer]] |
| G1, G2 | Novelty guards for L1 words; G2 is THE definition of novel (owner decision 2026-10-15); G1 (registered in T-002) is superseded, historical only | T-002 2026-10-15; adopted by owner decision 2026-10-15 | [[#novel L1 and the guards G1 and G2]] |
| L0, L0-ext, L1, L2, L3 | Success levels | owner 2026-10-05 | [[challenge-gen-success-metrics#Success levels]]; L0-ext in [[#L0-ext]] |
| L1 gate | The constraint every search candidate must pass: R₂.₅(w) ≠ 1 and ρ_min16(w) ≥ 0.5 (screen ρ on the pool, ρ_min16 on finalists) | owner 2026-10-15 | [[project-challenge-gen#The search problem (owner, 2026-10-15) — the crucial part]] |
| loop erasure | Chronological deletion of freely cancelling blocks of F; gives F* | owner 2026-10-05, made exact in T-001 | [[#loop erasure]] |
| move set | Local-search moves on F: replace a relator rᵢ, mutate a conjugator cᵢ, insert or delete a factor, reorder (swap adjacent factors) | owner 2026-10-15 | [[project-challenge-gen#The search problem (owner, 2026-10-15) — the crucial part]] |
| n | \|w̄\|, length of the freely reduced expansion | owner 2026-10-05 | [[challenge-gen-success-metrics#Notation]] |
| novel L1 | An L1 word whose reduced form is not just a relator (or a reduction of a single factor) | T-002 2026-10-15 | [[#novel L1 and the guards G1 and G2]] |
| p (dataset share), n_dataset | Probability that a sampled factor is a dataset relator; the realised count is stored per word | T-002 2026-10-15 | [[#cell and cell names]] |
| positive / negative control | See control | T-001 2026-10-13 | [[#positive and negative control]] |
| power-free shortcut | Exact test: no power ≥ 2.5 in w̄ (linear) and in cyc(w̄) (cyclic) implies the reducer is a no-op | T-001 (no-square form), T-002 (exact form) | [[#pre-check: no square and power-free]] |
| pre-check (no square) | No square in the cyclic word implies R₂.₅ = cyc(w̄) up to rotation | T-001 2026-10-13 | [[#pre-check: no square and power-free]] |
| relator map / relator table / relator file | Index to word table used to expand a certificate; its hashed form; and the file a table can be loaded from | T-001 2026-10-13 | [[#relator map, relator table and relator file]] |
| rotation-invariant | The reducer's result does not depend on the cyclic rotation of its input (but does on relabelling and inversion) | T-001 2026-10-14 | [[#aut8 and the 16 images]] |
| R₂.₅ | `greedyReduceCyclicExhaustive(greedyReduce(w̄))` | owner 2026-10-05 | [[challenge-gen-success-metrics#Notation]] |
| screen mode | 2.5-reduction with cyclic shifts {0, 0.5} only; cheap, may miss reductions | owner 2026-10-05 | [[#screen mode and certify mode]] |
| search objective | Maximise D = N*/\|w\| (factors of the minimised certificate over freely reduced length) subject to the L1 gate | owner 2026-10-15 | [[project-challenge-gen#The search problem (owner, 2026-10-15) — the crucial part]] |
| search parameters | What every search run must record: relator set R, N range, conjugator bound, word-length bounds, move set, search strategy, objective and gate | owner 2026-10-15 | [[project-challenge-gen#The search problem (owner, 2026-10-15) — the crucial part]] |
| search space | Ordered sequences F = ((r₁,c₁),…,(r_N,c_N)), rᵢ a relator or its inverse, cᵢ a freely reduced conjugator, N variable; order matters (factors do not commute) | owner 2026-10-15 | [[project-challenge-gen#The search problem (owner, 2026-10-15) — the crucial part]] |
| seeds, calibration seed | Sampler seeds reported per task, plus one unreported seed for timing | T-001, T-002 | [[#seeds and calibration seed]] |
| short100, S1–S4 (T-002 strata), S1–S7 (T-001 cells) | Dataset subsets by length rank in T-002; the unrelated T-001 sampling cells | T-001, T-002 | [[#cell and cell names]] |
| standard relators | All cyclically reduced v⁵ with \|v\| ≤ L, trivial in free B(2,5) by construction | PatternBoost design 2026 | [[#standard relators and dataset relators]] |
| timeout | A reducer call exceeding the per-call wall-clock cap; recorded, never counted as pass or fail | T-001 2026-10-13 | [[#undecided, timeout]] |
| undecided (`L0?`) | A word the harness did not classify (size limit or timeout) | T-002 2026-10-15 | [[#undecided, timeout]] |
| w̄ | Freely reduced expansion of F | owner 2026-10-05 | [[challenge-gen-success-metrics#Notation]] |
| ρ | \|R₂.₅(w)\|/\|w̄\| | owner 2026-10-05 | [[challenge-gen-success-metrics#Metric 1: resistance to 2.5 reduction (heuristic difficulty)]] |
| ρ_cyc | \|R₂.₅(w)\|/\|cyc(w̄)\|, the rewrite effect alone | T-001 2026-10-13 | [[#rho_cyc and the cyclic reduction]] |
| ρ_min16 | min over the 16 images of \|R₂.₅(image)\|/\|w̄\|; the representative convention for any hardness claim | owner decision 2026-10-14 (T-001) | [[#rho_min16]] |

## Part B: full definitions of terms not defined elsewhere

### 2.5-power and the reducer rewrite
A **maximal power** in a word is a window u^q: a stretch of length ℓ that has period h = |u| (letters repeat with shift h), with exponent q = ℓ/h. The tcgraph reducer (`greedy_reduction.cpp`, `findSquares`, then the best-power selection) rewrites a power only when q ≥ 2.5; at exactly q = 2.5 the rewrite is **length-neutral** (so it can change the cyclic word without shortening it). A word with no square (window of exponent 2) is never rewritten. Used in: [[#pre-check: no square and power-free]], [[#fixed point of the reducer]].

### aut8 and the 16 images
- **8 letter automorphisms.** The maps of the alphabet {a, A, b, B} to itself that send generators to generators or their inverses: choose whether to swap a and b (2 ways) and the sign of each of the two generators (2 × 2 ways). They are the 8 signed permutations of the two generators; each is an automorphism of F(a,b) and of B(2,5). In code: `images16` in `experiments/challenge_gen/hardness/reduction.py`.
- **16 images.** For a word w, apply each of the 8 maps to get an image word f(w), and also take its inverse f(w)⁻¹ (reverse the letters and invert each). That is 16 words, all of length |w|.
- **Why it matters.** The reducer is **rotation-invariant** (it works on cyclic words) but **not** invariant under these maps: R₂.₅(f(w)) can have a different length than R₂.₅(w), because greedy tie-breaking depends on the letter order. T-001 found two dataset words that reduce to the empty word in 13 of 16 and 15 of 16 images but not in the stored one. Hence [[#rho_min16]].
- **aut8 in dataset names** (`…aut8…`): the 820 words are pairwise distinct up to rotation × inversion × these 8 maps ("unique"), i.e. one word per orbit ([[ds-b25-trivial-2-5reduced-aut8-20261014]]).

### canon (canonical class)
canon(w) = the lexicographically smallest string (shortest first, then alphabetical on the letter characters produced by `to_str` in `certificate.py`) among all rotations of all 16 images of w. Two words have equal canon exactly when they are the same cyclic word up to the 8 letter maps and inversion. Computed with Booth's least-rotation algorithm. Code: `canon.py`. Used by the novelty guards ([[#novel L1 and the guards G1 and G2]]).

### cell and cell names
A **cell** is one sampler setting. Two unrelated naming schemes exist, so always cite the task:
- **T-001 cells S1–S7** ([[hardness-harness-baselines-2026-10-13]]): random factor words over standard relators; S1–S3 use L = 2 (16 relators) with 3–8, 10–20, 30–60 factors; S4–S6 use L = 3 (44 relators) with the same factor ranges; S7 is L = 3, 10–20 factors, conjugator length up to 8. Conjugators are uniform in length 0..4 otherwise.
- **T-002 cells** ([[t002-dataset-relator-products-2026-10-15]]): `P<pct>-K<k>-<subset>[-L2]`.
  - `P<pct>`: the **dataset share p** in percent; each factor is independently a dataset relator with probability p (a uniform word of the subset, word or inverse equally likely), otherwise a uniform standard relator. The realised number of dataset factors is stored per word as `n_dataset`.
  - `K<k>`: the number of factors (`K1`, `K2`, `K3-5`, `K6-10`, `K11-30`; a range means uniform in that range).
  - `<subset>`: `short100` = the 100 shortest dataset words (ranks 1–100 of the length-sorted file; lengths 32 to 55). **Strata S1–S4** (T-002) = dataset ranks 1–205, 206–410, 411–615, 616–820 (length quartiles).
  - suffix `-L2`: standard relators restricted to |v| ≤ 2 (16 relators) instead of |v| ≤ 3 (44).
  - Conjugators: uniform length 0..4, non-backtracking; a word is resampled if its freely reduced length is below 10.
- Each cell is run for each seed ([[#seeds and calibration seed]]); the word id is `<cell>-<seed>-<index>`.

### D_raw
D_raw = |F| / |w̄| on the certificate as sampled, before [[#loop erasure]]. D (owner) is the same ratio on F*. D_raw ≥ D always; it is reported next to D to show how much padding the sampler produced.

### factor, conjugator and relator index
A **factor** is one pair (k, c): relator index k into the relator table and conjugator word c. Its expansion is c⁻¹ R_k c, freely reduced. The conjugator is c (any word in the free group, here of length 0..4 or 0..8). The certificate F is the ordered list of factors; the product convention is left to right with free reduction after each factor (`pb_relator_map.cpp`). A factor is called "one-factor" when F has exactly one pair.

### fixed point of the reducer
A word w with R₂.₅(w) equal to cyc(w) up to rotation, i.e. the reducer changes nothing except cyclic reduction. For the 820 dataset relators, "fixed point" means: both the screen-mode and the certify-mode results have the same length and the same cyclic word as the stored string. Fixed-point-ness of the stored string does not imply it for the other 15 images ([[#aut8 and the 16 images]]): 818 of the 820 have all 16 images fixed; for the other two only the stored representative is.

### L0-ext
Level L0 where triviality of the relators rests on an **external proof** (the dataset's Knuth–Bendix proof for the 820 relators, plus Validator's certificates for the replaced words), not on the relators being literal 5th powers. The word is trivial in free B(2,5) but F is not independently checked beyond re-expansion. T-001 labels the 820 words themselves "L0-ext" because they have no stored certificate (D undefined).

### loop erasure
The method used to compute F* from F. Track the freely reduced prefix words P_j = expand(f₁ … f_j). Process the factors in order with a stack of the current freely reduced prefix. If the prefix after factor j equals an earlier prefix state P_i (i < j), delete factors i+1 … j and continue from state P_i. Equality is tested by a polynomial hash of the free-reduction stack and, on a hit, by comparing the prefix content to exclude collisions. Properties: expansion unchanged; |F*| ≤ |F| in the sampled cases; the result is *a* chronologically loop-erased F*, not the minimum over all erasure orders; blocks that cancel only modulo the relators are not removed, so D on F* is an upper bound on area/n. In an exploratory case |F*| exceeded |F_orig| for planted padding ([[hardness-baselines-results]], H1b). Code: `minimise.py` (linear) and a naive quadratic reference for tests.

### novel L1 and the guards G1 and G2
A word that passes L1 only because a single relator survives is not an interesting challenge. A **novel** L1 word is an L1 word whose reduced form is not explained by one input relator.
- **G1 (registered in T-002; superseded by G2 on 2026-10-15, kept only as a historical number).** Let R = the certify result of w. R is **non-novel** if canon(R) equals canon(r) for some relator r used in F (word or inverse); otherwise novel. **Flaw:** the reducer applies length-neutral rewrites (q = 2.5) and a greedy-first step on a non-cyclically-reduced word, so R of a one-factor word is often a different cyclic class than r. In the one-factor cell G1 called 91 of 285 L1 words novel.
- **G2 (refined post hoc in T-002; ADOPTED by owner decision 2026-10-15 as the definition of "novel L1").** R is **non-novel** if canon(R) equals canon(r) for a used relator r, **or** canon(R) equals canon(R₂.₅(c⁻¹ r c)) for one of the single factors of F (the reducer's own output on one factor); otherwise novel. G2 gives 0 novel for one-factor words, as it must. Also recorded in the data: whether canon(R) matches *any* of the 820 words.
- Both are in [[t002-dataset-relator-products-results]]; T-002 headline: 4,012 novel by G2, 4,335 by G1, of 5,221 L1 words. **Decision (owner, 2026-10-15): G2 is the definition of "novel L1" from now on.** Quote G1 only when comparing with the T-002 registered numbers.

### positive and negative control
- **Positive control** for a metric: a set where the metric must come out at its extreme in the *passing* direction, so that a harness that never passes would show. T-001: the 820 dataset words (ρ ≈ 1, fixed points). T-002: the one-factor cell P100-K1-short100 (L1 rate ≥ 0.93).
- **Negative control**: a set that must come out in the *failing* direction, so that a harness that always passes would show. T-001: random standard-relator factor words (ρ = 0, 7,000/7,000). T-002: the all-standard cells P0-* (L1 = 0). T-001 also ran an **added control**: commutator products (abelianization-trivial but not certified trivial) which survive the reducer with ρ ≈ 0.89, showing that ρ = 0 is a property of the words and not a reducer artefact.

### pre-check: no square and power-free
Two cheap tests that avoid the expensive reducer; both rest on code reading plus a property test ([[#2.5-power and the reducer rewrite]]).
- **Pre-check (no square)** (T-001, H5). If the cyclic word cyc(w̄) contains no square window (a window of length 2h with period h, inside the doubled word, window length ≤ n), then R₂.₅(w̄) equals cyc(w̄) up to rotation. Tested on 100,000 words: 0 violations (20 returned another rotation). Sufficient, not necessary.
- **Power-free shortcut** (T-002, exact form). If w̄ has no window of exponent ≥ 2.5 (linear windows), **and** the doubled cyclic word has none of length ≤ n (cyclic windows), the reducer is a no-op in every shift. Then R₂.₅(w̄) = cyc(w̄) up to rotation, and the same for all 16 images, so ρ_min16 = ρ. Code: `powerfree.py`. Agreed with the reducer on 420 of 420 words it applied to.
- Note the older text in the metrics note ("no subword power with exponent ≥ 2.5 ⇒ `greedyReduce` cannot rewrite", flagged there as needing verification) is the linear half of the power-free shortcut; the cyclic half is what makes it sufficient for R₂.₅.

### relator map, relator table and relator file
- **Relator map** (tcgraph `RelatorMap`): the object that maps relator index k to its word and expands factors. It stores indices and conjugators only; the relator words live in the map.
- **Relator table**: the explicit index to word list used by the independent Python expander (`certificate.py`). It is identified by its **sha256** (of the ordered list of words); the hash is stored in every sample record and verified at load, because a JSON certificate with default names `R<i>` is meaningless without it. T-002 table: indices 1–820 dataset words in file order, 821–1640 their inverses, 1641–1684 standard relators with |v| ≤ 3.
- **Relator file** (`relators.relators_file` in the PatternBoost config): a text file of words loaded into a relator map instead of the standard v⁵ set. Its words are trusted, not verified, so the certificate is only as good as the file.

### rho_cyc and the cyclic reduction
cyc(w̄) is w̄ with matching first and last letters cancelled repeatedly (cyclic reduction); n_cyc = |cyc(w̄)|. The reducer's output is always cyclically reduced, so |R₂.₅(w)| ≤ n_cyc ≤ n, and ρ < 1 for a word that is merely not cyclically reduced even if no rewrite happened. **ρ_cyc = |R₂.₅(w)| / n_cyc** isolates the effect of the rewrites. The owner's ρ is over n; both are recorded.

### rho_min16
**Owner decision 2026-10-14 (T-001)**, recorded in [[challenge-gen-success-metrics#Owner decision 2026-10-14: representative convention for ρ (T-001)]]. For a word w with n = |w̄|:

ρ_min16(w) = min over the 16 images x of w ([[#aut8 and the 16 images]]) of |R₂.₅(x)| / n,

where R₂.₅ is computed in **certify** mode on each image (images have the same length n). Any hardness claim (L1, L2) uses ρ_min16 ≥ 0.5 and R₂.₅(x) ≠ empty for the minimising image; a word is *not* L1 if any image reduces to the empty word. Screening may use the generated word only; all 16 images are computed for finalists. Shortcut: if the word is power-free ([[#pre-check: no square and power-free]]), ρ_min16 = ρ with no reducer call. Implementation: `--min16` in `run_baselines.py`, record fields `min16_lens`, `min16_len`, `rho_min16`.

### screen mode and certify mode
Both run `greedy_reduce2_5(w̄)` first and then `greedy_reduce_cyclic_exhaustive2_5(·, fractions)`.
- **Screen mode**: `fractions = [0.0, 0.5]`. In each round only the cyclic shifts at 0 and half the length are tried. It can miss reductions that other shifts would find, never invent one; a word screen reduces to the empty word also reduces to it in certify mode (measured 0 exceptions in both directions, T-001 H3; 176/176 in T-002 H7). Used inside loops and for fast triage; screen-empty words are classified "not L1".
- **Certify mode**: `fractions = None`, all shifts. Used for every reported ρ, ρ_min16 and level.
- A word whose result is the empty word is "R = 1" (ρ = 0, not L1).

### seeds and calibration seed
Every task lists its sampler seeds up front: T-001 uses 1000001–1000005, T-002 2000001–2000005. A **calibration seed** (1000000, 2000000) is used only to time the reducer and to set size limits and per-cell counts; its numbers are never reported as results. Seeds of different tasks and of PatternBoost (< 300,000) do not overlap (profile rule 3). T-002's sampler is pure Python (`random.Random("T002-<seed>-<cell>")`), so the seed determines the words on any machine; every sampled word is also stored in JSONL.

### standard relators and dataset relators
- **Standard relators**: all cyclically reduced words v⁵ with |v| ≤ L (`build_standard_relators(L, 2)`): 4, 16, 44 relators for L = 1, 2, 3. Trivial in free B(2,5) because each is a literal 5th power. L0 holds automatically.
- **Dataset relators**: the 820 words of [[ds-b25-trivial-2-5reduced-aut8-20261014]] (corrected T-012 version; the 20261007 version is superseded). Lengths 32 to 123. Each is 2.5-reduced and trivial in free B(2,5) by the dataset's Knuth–Bendix proof (kbprog), not by being a 5th power. Fixed points of the reducer in both modes. L0 for products rests on that external proof ([[#L0-ext]]).
- Use "relators" for either; say which.

### undecided, timeout
A word is **undecided** (recorded `L0?`) if the harness did not classify it, e.g. n exceeds a configured limit (T-002: certify only if n ≤ 2000, ρ_min16 only if n ≤ 800 locally) or a reducer call exceeds its timeout (120 s). **Timeout**: the child reducer process is killed and restarted, the word is recorded as timed out. Undecided and timed-out words are listed in every table and never counted as L1 or as failures.

## Related material
- [[challenge-gen-success-metrics]]: owner definitions (certificate, ρ, D, levels) and the ρ_min16 decision
- [[project-challenge-gen]]: project profile, rule 9
- [[Challenge Generation/_progress]]: progress note
- [[B25/Hardness Evaluation/_type|Hardness Evaluation]]: experiment type; type-local terms
- [[B25/PatternBoost Generation/_type|PatternBoost Generation]]: experiment type; type-local terms
- [[hardness-harness-baselines-2026-10-13]] · [[hardness-baselines-results]] · [[t002-dataset-relator-products-2026-10-15]] · [[t002-dataset-relator-products-results]]
- [[ds-b25-trivial-2-5reduced-aut8-20261014]]
