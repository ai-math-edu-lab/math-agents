---
title: "Synthesis — The Kuznetsov line on B(2,5): Cayley-table closure as a third algorithmic family"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/word-problem
  - topic/cayley-table-closure
  - topic/finite-group-enumeration
  - topic/mixer
  - synthesis
  - status/draft
papers_synthesized:
  - "[[kuznetsov-shlepkin-2009]]"
  - "[[kuznetsov-tarasov-shlepkin-2009]]"
  - "[[kuznetsov-shlepkin-2010]]"
key_concepts:
  - "[[Concepts/cayley-table-closure-algorithm]]"
  - "[[Concepts/verification-methods-for-group-equality]]"
date_range: 2009-01 to 2010-06
project: b25
---

# Synthesis — The Kuznetsov line on B(2,5): Cayley-table closure as a third algorithmic family

> **Status: partially superseded.** This 3-paper synthesis (2009–2010) focuses on the Cayley-table-closure algorithm specifically. The broader 20-paper synthesis is now at [[_synthesis-kuznetsov-b25-publications]]. This note is retained as the authoritative deep-dive on the algorithm mechanics and the $|P_s(2,5)|$ baseline data — read it alongside the new synthesis, not instead of it.

> **Synthesis note.** Three papers from the Krasnoyarsk school (Kuznetsov, Tarasov, Shlepkin; 2009–2010) develop a Cayley-table-closure algorithm for word-problem computation in finitely-presented periodic groups, and apply it to push the comparison of $B(2,5)$ with the restricted $B_0(2,5)$ from length-27 coincidence (2009) to length-29 coincidence + length-30–35 candidate divergence relations (2010). This synthesis is the cross-paper picture, with explicit framing for the Mixer attack on Problem 11.48.

## The question

Does the Kuznetsov line of work give the Mixer B(2,5) attack ([[b25-finiteness-11.48-kostrikin]]) anything that the Knuth-Bendix and bidirectional pipelines do not already provide?

## Sources reviewed

1. [[kuznetsov-shlepkin-2009]] — Trudy IMM 15(2), 125–132. Introduces Algorithm I (row-collision-based Cayley-table closure) for free Burnside groups. Computes $K_{27}(2,5)$ on a personal computer. Proves $B(2,5)$ and $B_0(2,5)$ have identical minimal-word relations up to length 27. $|P_{27}(2,5)| = 92{,}228{,}348$, $|C_{27}(2,5)| = 3{,}995$.
2. [[kuznetsov-tarasov-shlepkin-2009]] — Vestnik NSU 9(2), 47–54. Generalizes Algorithm I from free Burnside groups to arbitrary finitely-presented periodic groups (drop the $n$-aperiodicity step, seed $C_1$ with input relators). Worked example: $S_3$ computed by hand to $|S_3| = 6$. Positions Algorithm I as a complement to coset enumeration.
3. [[kuznetsov-shlepkin-2010]] — Trudy IMM 16(2), 133–138. Refines the detection step from row-collisions to associativity-test failures. Proves a clean finite/infinite dichotomy from $K_s$ stabilization. Cluster-scale ($125$ nodes, ~104 hours wall-clock) computation of $K_{35}(2,5)$: $|P_{35}(2,5)| \approx 5^{14}$, $|C_{35}| = 104{,}409$. Pushes the $B(2,5) \sim B_0(2,5)$ minimal-word coincidence to length 29 (Theorem 3). Exhibits **973 candidate-divergence relations** at lengths 30–35, **failure of any one of which in $B(2,5)$ would prove $B(2,5)$ infinite** (Theorem 4).

## Convergence

- **All three papers** rely on the same Cayley-table-closure algorithm family (see [[Concepts/cayley-table-closure-algorithm]]). The technical core is unchanged: build $P_s$ length-by-length, detect new relations from table collisions, fold each new relation into the reduction algorithm $A_s$, iterate until stable.
- **All three papers** treat the algorithm as **fundamentally different from KB completion and Todd-Coxeter coset enumeration**. The 2009 general-algorithm paper makes this comparison most explicitly (introduction); the two B(2,5)-specific papers inherit the framing.
- **Papers 1 and 3** ([[kuznetsov-shlepkin-2009]] and [[kuznetsov-shlepkin-2010]]) both use the $\psi: B(2,5) \to B_0(2,5)$ homomorphism construction with the [[havas-wall-wamsley-1974]] commutator basis. The 2009 paper introduces it; the 2010 paper extends the empirical comparison via $\psi$ from length 27 to length 29 (proven coincidence) and 30–35 (candidate divergence).
- **Within-paper sanity checks** in [[kuznetsov-shlepkin-2009]] reproduce known finite Burnside orders ($|B(2,3)| = 3^3$, $|B(3,3)| = 3^7$, $|B(2,4)| = 2^{12}$) — consistent with the consensus values in [[havas-newman-1980]] and Vaughan-Lee 1993. No discrepancy with prior literature is reported in any of the three papers.

## Disagreement

The three papers are internally consistent and do not disagree with each other or with [[havas-wall-wamsley-1974]] (the foundational result $|B_0(2,5)| = 5^{34}$).

**Potential tension with KB-style results in this vault:**

- [[algo-mixing-burnside-slides]] (the Mixer's B(4,3) breakthrough) frames B(2,5) as a problem to attack via KB completion with multiple cooperating orderings. The Kuznetsov line offers an alternative attack via Cayley-table closure. Neither paper explicitly engages with the other family; the question of whether a KB approach is intrinsically better-suited to B(2,5) than a Cayley-closure approach (or vice versa) is **unresolved**.
- KB termination implies finiteness; Kuznetsov's $K_s = K_{s+1}$ stabilization also implies finiteness — but they detect it via structurally different witnesses (a confluent rewriting system vs. an invariant Cayley table). For B(2,5) as of now, **neither has triggered.**
- For infiniteness, the two methods diverge: KB non-termination is silent on infiniteness; Kuznetsov's strictly-growing $|P_s|$ is a positive witness (Theorem 2 of [[kuznetsov-shlepkin-2010]]). However, the cluster-scale run only reaches $s = 35$, and $|P_{35}| \approx 5^{14} < 5^{34} = |B_0(2,5)|$, so the strict-growth observation through $s = 35$ is consistent with $B(2,5) \cong B_0(2,5)$ as well as with $B(2,5)$ being strictly larger. **Strict $|P_s|$ growth does not prove infiniteness until $|P_s| > |B_0(2,5)|$ is reached.**

## What's settled

- **Algorithm I is a sound word-problem decision procedure** for finite finitely-presented periodic groups. Theorem 2 of [[kuznetsov-tarasov-shlepkin-2009]] and Theorem 1 of [[kuznetsov-shlepkin-2010]] together establish: if $K_s = K_{s+1}$ at finite $s$, then $G$ is finite with $|G| = |P_s|$.
- **$B(2,5)$ and $B_0(2,5)$ have identical minimal-word relations up to length 29.** Proven by direct computation in [[kuznetsov-shlepkin-2010]] (Theorem 3), extending the length-27 result of [[kuznetsov-shlepkin-2009]] (Theorem 2). This is a hard empirical fact about B(2,5).
- **A concrete list of 973 candidate-divergence relations** at lengths 30–35 exists in $B_0(2,5)$. Failure of any one of them in $B(2,5)$ would prove $B(2,5)$ infinite ([[kuznetsov-shlepkin-2010]] Theorem 4). The relations are derived via the $\psi$ homomorphism in the [[havas-wall-wamsley-1974]] commutator basis and are length-30 through length-35 $\{1,2\}$-words.
- **The cluster-scale $|P_s|$ data is verifiable.** Any other tool that can enumerate $B(2,5)$ minimal words up to length 35 should produce the same counts ($|P_{27}| = 92{,}228{,}348$ exact; $|P_{35}| \approx 5^{14}$ stated as approximate). These are **ground-truth benchmark numbers** for the Mixer B(2,5) pipeline.

## What's contested

- **None within the three papers.** The Kuznetsov line is self-consistent and internally validated through known-finite sanity checks.
- **Approximate vs exact $|P_{35}|$.** The 2010 paper reports $|P_{35}(2,5)| \approx 5^{14}$, not an exact integer. This is mildly concerning for a computation that should produce exact counts (and which produces exact counts for $|C_{35}| = 104{,}409$ and for the lower-$s$ values in the 2009 paper). Possible explanations: a typesetting choice to give a memorable round figure; a memory-pressure approximation in the cluster run; or a genuine implementation precision limit. **Unresolved**; would need to consult the authors' raw output or independent replication.
- **The 2010 cluster outputs may not be preserved.** The paper lists only a few of the 973 candidate relations per length; recovering the full list may require contacting the authors. **Vault has neither the full list nor a confirmed channel to obtain it as of this synthesis.**

## What's open

- **Has any of the 973 candidate-divergence relations been refuted in $B(2,5)$ since 2010?** Either resolution settles Problem 11.48. Vault grep confirms no Research/ or Experiments/ note references the specific relations.
- **At what length does $|P_s(2,5)|$ first exceed $|B_0(2,5)| = 5^{34}$?** Rough extrapolation from the $\approx 1.9$ growth ratio: $s \approx 45$–55. Reaching that empirically would prove $B(2,5)$ infinite outright, no candidate relations needed.
- **Can Algorithm I and Knuth-Bendix be combined in a Mixer-style cooperative scheme?** The two produce complementary witnesses: KB produces oriented rewrite rules; Algorithm I produces an enumeration plus a Cayley table. A multi-Agent architecture running both could cross-check at each level: KB-derived canonical forms should agree with Algorithm I's minimal-word set $P_s$. This is **not investigated** in either family of papers.
- **Is the associativity-test detection of [[kuznetsov-shlepkin-2010]] strictly more efficient than the row-collision detection of [[kuznetsov-shlepkin-2009]], or are they detecting the same relation set with different runtime profiles?** Not benchmarked in the published papers.
- **What modern hardware can do.** The 2010 run took 104 hours on a 125-node cluster of 3 GHz CPUs (~13,000 core-hours). Modern hardware (GPU acceleration, optimized symbolic algebra) could plausibly push this to $s \ge 45$ — the threshold where strict $|P_s|$ growth becomes a proof of infiniteness. **Not attempted in this vault.**

## Methodology notes

- All three papers are in Russian; their content is not easily discoverable to non-Russian-speaking searches in English-language databases. The vault summaries here are the first English-language treatment of the Kuznetsov line in this project.
- Citation counts could not be located via standard channels for any of the three papers at write time — this is typical for Russian-language journal papers from the 2009–2010 timeframe, which often have weak English-indexed citation profiles.
- **Verification opportunity:** the candidate-divergence relations at lengths 30 (only 2 of them — quoted verbatim in [[kuznetsov-shlepkin-2010]] Key result table) are the **easiest to test independently**. They can be passed through any existing $B(2,5)$ word-equality test (KBMAG, Rust bidirectional, GAP's KBMAG package) without any new tooling.
- The 2009 paper's table of $|P_s(2,5)|$ for $s = 1, \ldots, 27$ is **verifiable independently** by any tool that enumerates $B(2,5)$ minimal words. **This is the cheapest benchmark check available and should be added to the B(2,5) experiment validation suite.**

## Recommendation

For Lead and Experimenter-B25 (B(2,5) workstream):

1. **Verification of the 2009 baseline.** Add the $|P_s(2,5)|$ values for $s = 1, \ldots, 27$ (from [[kuznetsov-shlepkin-2009]] §3 Table 2) to the verification suite for any B(2,5) enumeration Agent. Reproducing these counts is a cheap correctness check and may surface bugs in current pipelines.
2. **Direct test of the 2 length-30 candidate relations.** Take the two relations from [[kuznetsov-shlepkin-2010]]'s Key result table and run both sides through the KBMAG and Rust-bidirectional B(2,5) pipelines. If either pair reduces to **distinct** canonical forms, **Problem 11.48 is resolved in the negative**. This is the highest-leverage single experiment derivable from this paper batch.
3. **Pre-register a Kuznetsov-Algorithm-I Agent for the Mixer.** Element-enumeration as a complement to rule-derivation (KB) gives a multi-witness architecture: the Mixer Agents would cross-check $|P_s|$ growth against rewriting-system canonical forms. This is a natural extension of the Mixer's algorithm-cooperation pattern documented in [[algo-mixing-burnside-slides]] and could give B(2,5) the same kind of empirical handle that two-ordering cooperation gave B(4,3).
4. **Attempt to obtain the full 973-relation list.** If only the table excerpts in [[kuznetsov-shlepkin-2010]] are available, the verification scope is bounded; with the full list, the Mixer's bidirectional Agent has a concrete finite test set whose complete success (no relations falsified) would constitute strong empirical evidence for $B(2,5) \cong B_0(2,5)$, while any single failure resolves the problem outright.

## Related vault material

- Papers: [[kuznetsov-shlepkin-2009]], [[kuznetsov-tarasov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]]
- Concepts: [[Concepts/cayley-table-closure-algorithm]], [[Concepts/verification-methods-for-group-equality]]
- Prior syntheses: [[_synthesis-existing-papers]] (broader Group theory synthesis; this synthesis is a focused complement on the Kuznetsov line specifically)
- MOCs: [[_moc-burnside]] (this synthesis registered there; see new "Cayley-table-closure attack" section)
- Foundational paper: [[havas-wall-wamsley-1974]] (the commutator basis 1–34 powering ψ)
- Open problem: [[b25-finiteness-11.48-kostrikin]] (Mixer attack rationale)
- Open problem: [[kourovka-11.48-kostrikin-1990]] (mathematical statement)
- Mixer artifact: [[algo-mixing-burnside-slides]] (B(4,3) breakthrough; structural precedent for the multi-algorithm cooperation framing recommended above)
- Experiments to engage: `experiments/burnside_bidirectional/` and the KBMAG-based pipelines in the B(2,5) workstream
