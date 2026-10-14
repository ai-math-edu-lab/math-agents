---
title: "Synthesis — proof-recording Knuth–Bendix tools, and Dehn functions of B(m,n) (T-017 survey, 2026-10-14)"
author: asetlearning
language: en
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/knuth-bendix
  - topic/rewriting-systems
  - topic/proof-certificates
  - topic/dehn-function
  - topic/burnside
  - topic/b25
  - topic/trivial-words
  - synthesis
  - project/challenge-gen
  - status/draft
papers_synthesized:
  - "[[wagner-2020-torsion-quadratic-dehn]]"
key_concepts:
  - "[[Concepts/complete-rewriting-systems]]"
date_range: 1970 to 2026
project: challenge-gen
status: draft
domain: group-theory
---

# Synthesis — proof-recording Knuth–Bendix tools, and Dehn functions of B(m,n)

> [!info] Plain English
> **Task T-017.** The 820 dataset words in [[ds-b25-trivial-2-5reduced-aut8-20261014]] are rules of a Knuth–Bendix run, and the run kept no record of *why* each rule holds. We want, for each word, an explicit **factor word**: a product of conjugates of the relators `v^(5k)` (|v| ≤ 7) that multiplies out to the word. Its number of factors is an upper bound on the word's **area** over those relators.
> **Answer in one line.** No existing tool does this at our scale. The one proof-recording group tool (GAP `idrel`) failed on 2 of 3 small trials and is a GAP-language implementation; stock `kbprog` records nothing usable; general equational provers solve a different problem. **Recommendation: adapt `kbprog` (our fork) to emit provenance, and build the factor words with an independent Python builder and checker. Rough effort: 1–2 weeks of Developer time.**
> **Dehn function.** For large odd exponent the closest published result is a *linear Dehn spectrum* (Osin–Rybak 2022), which is not the same as a linear Dehn function over the n-th-power presentation. Nothing is known for n = 5.

## Terms (defined once)

- **Knuth–Bendix (KB) completion**: an algorithm that turns a set of relations into a set of rewriting **rules** `l → r` (replace the left side by the right side) by repeatedly resolving **critical pairs** (two rules whose left sides overlap) until the rules agree on every word. Here the relations are the 815 relators `v^(5k) = 1`.
- **Factor word** of a trivial word `w`: a list of pairs `(c_i, ρ_i^±1)` with `w = ∏ c_i ρ_i^±1 c_i⁻¹` in the free group, each `ρ_i` a relator. **Area** (number of relator faces in a *van Kampen diagram*, a planar picture of such a product) is the minimum number of factors over all factor words; any one factor word gives an upper bound.
- **Logged rewriting** (Heyworth–Wensley): KB where every rule carries a **log**, i.e. its own factor word, so that `l r⁻¹` equals the product the log describes.
- **Dehn function** `δ(n)`: the maximum area of a trivial word of length ≤ n.
- **kbprog**: the KB program of KBMAG. **RPO / shortlex**: the two word orderings used in the March 2026 runs.

## Part 1 — Tools

### What T-017 needs from a tool
1. Runs KB on the 815-relator presentation `b25_full` (about 10⁵ rules, RPO or shortlex ordering) and finishes in seconds to minutes, like `kbprog`.
2. For any rule, or any word reduced to the empty word by the final rules, produces a factor word over *only* the 815 relators (so the area is over the right relator set).
3. The factor word can be checked independently of the tool (multiply out, freely reduce, compare with `w`).

Point 3 matters most: with an untrusted producer and a trusted checker, a bug in the producer cannot give a wrong result, only a failed check. This is the design of certified completion (Sternagel–Thiemann, below).

Also note that the original derivation is not required. Any factor word for `w` is as good, so the logged run can be a fresh `kbprog` run (the dataset note says the proof run "takes seconds to reproduce"; 818 of the 820 words already reduce to the empty word under both of the parent run's systems, all 820 under at least one).

### Survey table

| Tool | Records proofs? | Scale | Licence / maintenance | Effort to get factor words | Verdict |
|---|---|---|---|---|---|
| **GAP `idrel` 2.49** (Heyworth–Wensley logged KB) | **Yes.** Each rule is `[lhs, log, rhs]`; a log is a list `[±relator index, conjugator]`. Example from the package tests: `[ b^2, [ [ -4, id ], [ 2, A^2 ] ], a^2 ]` | **Poor** (own tests below): only shortlex, written in the GAP language | GPL-2.0-or-later; release 2.49 dated 2025-10-02; installed locally in `pkg/idrel` | Format is already a factor word. Zero conversion | Right *format*, wrong *engine*. Use as a small-case cross-check and as the specification of the log format |
| **KBMAG `kbprog` (stock)** | **No.** `-ve` prints `New equation number N, from overlap K, L` for each new equation, with the rule numbers of the two parents but not the overlap offset or the reductions. Rule numbers are list positions, which can change when the program tidies and re-sorts (from reading `tidyup()` and `sort_eqns()`, not tested) | Excellent: `b25_full`, `-rec -ve -me 3000` runs in 0.07 s and halts with 743 equations | GPL-2.0-or-later; KBMAG 1.5.11 | A replay of the printed trace is conceivable but fragile (see below) | Producer of the facts, not of the proofs |
| **Our `kbmag_source` fork** (biased fork with rule injection) | No, but rule creation goes through a few places in `lib/kbfns.c`: `insert()`, `consider()` and `consider_special()` (critical pairs), `conf_check()`, `tidyup()` (interreduction), plus `read_inject_rules()` (injection) | Same as stock | GPL (fork of KBMAG); we own it | **Recommended**: add provenance logging (see Recommendation) | Best candidate |
| **MAF** (Alun Williams, C++ re-implementation of KBMAG) | Not documented | Similar to KBMAG; its own docs say it can be slower on some systems | Open source (SourceForge `maffsa`) | Would need the same patch in less familiar code | No advantage over our fork |
| **libsemigroups `KnuthBendix`** (C++, used by GAP `Semigroups` 5.5.4) | **No.** Searched the class header for proof, history, derivation, witness, trace: no hits | Good | GPL-3.0; actively developed (copyright 2025–2026) | Logging would need deep changes inside its rewriters | No |
| **GAP library KB** (`rws`), **GAP `kan`**, **GBNP/IBNP**, **HAP**, **ACE** | No proof output for words. `HAP` computes identities among relations only for finite groups by resolutions | Not applicable | — | — | No |
| **KBCV 2.x / mkbTT** (Innsbruck; "recording completion" with a *history*, certificates checked by CeTA) | **Yes**, with a formally verified certifier (CeTA, Isabelle/HOL) | Aimed at small term-rewriting problems; no evidence of 10⁵ rules | KBCV is LGPL-3 Java | Encode strings as unary terms, convert histories to factor words; the scale gap is the blocker | Useful as a design reference only |
| **Twee**, **Waldmeister**, **Prover9**, **E**, **Vampire** (equational provers) | **Yes**, but a proof of *one goal equation*, not a log per rule (Twee: unfailing KB with human-readable proofs; Waldmeister has a proof mode; the other three are from general knowledge, not tested here) | Each run proves one word; no way to ask for the area over only the 815 relators unless relators are given as ground axioms; unlikely to complete 10⁵-rule runs | Mixed; not checked | Proof steps would have to be turned into positions and conjugators | No |

### Evidence from my own runs (2026-10-14, scratch scripts in `Agents/asetlearning/Researcher/scratch/t017/`)

| Run | Tool | Result |
|---|---|---|
| B(2,3), 21 relators `u³`, |u| ≤ 3 | `idrel` `LoggedKnuthBendix` | 32 rules, 0.21 s |
| B(2,4), 21 relators `u⁴`, |u| ≤ 3 | `idrel` | GAP error in `LoggedRewriteReduce` (a list position is `fail`, `logrws.gi:1057`) |
| B(3,3), 69 relators `u³`, |u| ≤ 3 | `idrel` | GAP error in `LoggedOnePassKB` after about 24 s |
| B(3,3), 47 relators `u³`, |u| ≤ 3 (different dedup) | `kbprog` shortlex | confluent, 1809 equations, 0.034 s |
| `b25_full`, `-rec -ve -me 3000` | `kbprog` | 743 equations, 0.07 s |

Caveats: the two `idrel` failures are not diagnosed and may come from my input (redundant or non-minimal relators, generator labelling). The `idrel` and `kbprog` B(3,3) runs used slightly different relator lists, so this is a rough contrast (seconds versus milliseconds, then a crash), not a benchmark.

### Why not replay the stock trace?
`kbprog -ve` already prints, for every new equation, the numbers of the two parent rules. A script could try to rebuild each rule's derivation offline. Problems: the offset of the overlap is not printed (recoverable by trying every overlap of the two left sides); the interreduction in `tidyup()` creates new equations without a printed parent; rule numbers change when the program sorts. It can be made to work by emulating `kbprog`'s bookkeeping exactly, but then it is a reimplementation, and slow in Python at 10⁵ rules. A one-day feasibility spike on the first few thousand equations is possible; I would not plan on it.

### Rule injection
The March 2026 banks came from RPO and shortlex runs "side by side with rule injection" ([[ds-b25-trivial-2-5reduced-aut8-20261014]] § Origin). An injected rule has no derivation inside the receiving run. For a fresh logged run without injection this does not arise.

## Recommendation

**Adapt our `kbmag_source` fork; do not adopt an external tool; build our own only if the patch fails.**

1. **Patch `kbprog`** (about 300–600 lines of C): give every rule a stable id (not its list position) and a provenance record: initial relator `i`; or critical pair (rule `a`, rule `b`, overlap offset) plus the list of reductions `(rule id, position)` applied to each side; or tidyup reduction. Write the records to a side file. Injected rules are leaf records (or avoided by not injecting).
2. **Python builder**: recursively expand provenance into a factor word only for the rules or words needed (820 words), with memoization. The provenance is a shared graph, so storage is small; the expanded factor word can be long, which is the thing to measure.
3. **Python checker**: multiply out, freely reduce, compare with `w`; independent of `kbprog` (same spirit as Validator's own scripts).
4. **Pilot**: run on the shortest dataset words first (length 32) and report factor-word lengths before and after cancelling adjacent inverse pairs.

Rough effort: patch plus builder plus checker plus validation, **1–2 weeks** for a Developer comfortable with C and with the fork. Own logged KB from scratch (C++ or Rust): about 3–4 weeks and harder to trust. Main risks: the fast reduction tables in `kbmag` hide which rule fired (instrumenting `slow_rws_reduce`-style reduction, which keeps a history of automaton states, is the likely route); memory for the provenance at 10⁵ rules; the expanded factor words may be huge for deep rules.

**What the numbers mean (so the result is not over-read).** A factor word from a KB derivation is an *upper bound* on area, not the minimum area. The metric also depends on the relator set `R`: over the single relators `v^(5k)` (|v| ≤ 7) a dataset word of length 32 can have area well above 1, whereas over the whole word as one relator it has area 1.

## Part 2 — Dehn functions of B(m,n)

**Q (Math Expert): is the Dehn function of the free Burnside group B(m,n), relative to the presentation by all n-th powers, known to be linear for large odd n? Anything for n = 5?**

**Short answer: not as stated. Closest published result is a linear Dehn spectrum (Osin–Rybak 2022). Nothing for n = 5.**

1. **Finite groups have linear Dehn functions (elementary).** Let `G` be finite of order `M`, generated by `X`, and let `R` be any set of relators whose normal closure is the kernel (this includes the infinite set `{u⁵}`). A trivial word `w` of length `n ≥ M` has two equal prefixes among its first `M+1` prefixes, so `w = p s q` with `s` trivial and `|s| ≤ M`. Then `w = (p s p⁻¹)(p q)` in the free group, so area(`w`) ≤ area(`s`) + area(`pq`). Induction gives area(`w`) ≤ `A_M · n`, where `A_M` is the largest area of a trivial word of length ≤ `M` (finite, as there are finitely many such words). This is the statement Math Expert conjectured ("simple pigeonhole") and the argument is sound.
   *Consequence for B(2,5).* If B(2,5) is finite, its order is at least 5³⁴ ≈ 5.8 × 10²³ (the restricted Burnside group RB(2,5) has order 5³⁴ per the `b25_full` header). The bound says nothing for words shorter than `M`, so it is irrelevant at the scale of the dataset (lengths 32–123). Conversely, a family of trivial words whose minimal area grows quadratically would prove B(2,5) infinite.
2. **Large odd exponent: linear Dehn spectrum.** Osin and Rybak ([arXiv:2203.12518](https://arxiv.org/abs/2203.12518), "Isoperimetric inequalities in finitely generated groups") prove: Theorem 1.12(c), "Finitely generated free Burnside groups of sufficiently large odd exponent" have a linear Dehn spectrum; Theorem 5.9, for `r ≥ 1` and sufficiently large odd `N`, B(r,N) is well-approximated by hyperbolic groups, and in particular `f_{B(r,N)}(k,m,n) ∼ n/m`.
   - The **Dehn spectrum** is `f(k,m,n) = max{Area_{S_m}(w) : w ∈ ⟨⟨S_k⟩⟩, ‖w‖ ≤ n}` (their Definition 1.1), where `S_m` is the set of *all* trivial words of length ≤ `m` used as relators. So the relator set grows with `m`, and the bound is `∼ n/m` for `m ≥ Ck`.
   - The tool is Olshanskii's graded small cancellation theory ([Ols91a], Theorem 19.1 gives the presentation `⟨X | ∪ R_i⟩` with `R_i = R_{i-1} ∪ {P^N : P a chosen period of length i}`); the Cayley graph of `G_i = ⟨X | R_i⟩` is `7Ni`-hyperbolic (their Proposition 5.7). Their Lemma 5.1 (from [Ols91a, Cor. 17.1]): a reduced diagram with an R-face `Π` has boundary length `> (1−β) · length(∂Π)`.
   - **What this does not say.** It is not "the Dehn function over the set of all n-th powers is linear". The relators here are selected periods, and the linearity is in a three-parameter family. I found no published statement of linearity relative to the full `{u^N}` presentation, even for large `N`; Math Expert's recollection ("D ≤ ~1") is not supported by what I could read.
   - **Exponent bound.** "Sufficiently large" is inherited from [Ols91a]. For orientation, the paper's introduction quotes the history for infiniteness: Novikov–Adian odd `N ≥ 4381`, Adian `N ≥ 665`, Olshanskii's geometric proof `N > 10¹⁰`.
3. **n = 5.** No result of this kind applies. Even finiteness of B(2,5) is open. The related note [[wagner-2020-torsion-quadratic-dehn]] already records that its exponent condition (n ≥ 2⁴⁸) excludes exponent 5.
4. **Not checked at the primary source (leads only).** A search snippet attributes to Olshanskii–Sapir a *verbal* isoperimetric function `n^(1+ε)` for the variety of Burnside groups of large odd exponent, and says B(m,n) for large n is not finitely presented so "the Dehn function of B(m,n)" does not exist in the classical sense. Both are plausible but I did not read the sources.

## Open questions for Lead
1. Official area over which relator set: `v^(5k)` with |v| ≤ 7 (815 relators), or something else? (also asked by Math Expert)
2. Approve Developer patch of our `kbmag_source` fork (1–2 weeks), or try the 1-day trace-replay spike first?
3. Re-run `kbprog` without injection for the logged run? (fine for triviality; rule identities differ from the March banks)
4. Want me to diagnose the `idrel` crashes (minimal reproducible case, possible upstream bug report)?
5. Should I read Olshanskii's book Ch. 5–6 and Olshanskii–Sapir to settle the two unchecked leads in Part 2?

## Related material
- [[word-problem-overview]]: parent directory map
- [[_moc-knuth-bendix]] · [[_moc-word-problem]]: MOCs that surface this note
- [[knuth-bendix]] · [[dehn-function]]: the technique notes this builds on
- [[knuth-bendix-1970]] · [[complete-rewriting-systems]]: KB background and complete rewriting systems for groups
- [[kbmag-tools-overview]]: KBMAG tool notes in the vault
- [[wagner-2020-torsion-quadratic-dehn]]: Dehn functions and torsion groups, exponent excluded here
- [[project-challenge-gen]] · [[ds-b25-trivial-2-5reduced-aut8-20261014]]: the project and the dataset these words come from
- [[2026-10-14-cancellation-constructions]]: Math Expert proposal, idea 2, that motivated this survey

## Sources
- Heyworth, Wensley, *Logged rewriting and identities among relators*, Groups St Andrews 2001 (LMS Lecture Note Series 304, pp. 256–276); preprint [arXiv:math/9907082](https://arxiv.org/abs/math/9907082); package docs [docs.gap-system.org/pkg/idrel](https://docs.gap-system.org/pkg/idrel/doc/chap0.html); local copy `pkg/idrel` 2.49.
- Sternagel, Winkler, Zankl, *Recording completion for certificates in equational reasoning* (CPP 2015) [PDF](https://profs.scienze.univr.it/winkler/papers/SWZ15.pdf); Sternagel, Thiemann, *Formalizing Knuth-Bendix orders and Knuth-Bendix completion* (RTA 2013) [PDF](https://cl-informatik-new.uibk.ac.at/files/Members/rene/paper/RTA13KBOC.pdf); Sternagel, *KBCV 2.0* [arXiv:1505.01338](https://arxiv.org/abs/1505.01338).
- Smallbone, *Twee: an equational theorem prover* (CADE-28) [Chalmers record](https://research.chalmers.se/en/publication/525501); MPI [Waldmeister primer](https://www.mpi-inf.mpg.de/departments/automation-of-logic/software/waldmeister/primer).
- Williams, [MAF vs KBMAG](https://maffsa.sourceforge.net/manpages/MAF_vs_KBMAG.html).
- libsemigroups [knuth-bendix-class.hpp](https://github.com/libsemigroups/libsemigroups/blob/main/include/libsemigroups/knuth-bendix-class.hpp) (checked for proof or history API: none found).
- Osin, Rybak, *Isoperimetric inequalities in finitely generated groups* [arXiv:2203.12518](https://arxiv.org/abs/2203.12518) (read Theorems 1.12, 5.9, Prop. 5.7, Lemma 5.1, Def. 1.1 in the PDF text).
- Local: `kbprog` runs and `kbmag_source` reading (`lib/kbfns.c`, `lib/rws.h`, `src/kbprog.c`).
