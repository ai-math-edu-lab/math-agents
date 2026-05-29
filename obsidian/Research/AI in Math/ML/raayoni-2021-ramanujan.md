---
title: "Generating conjectures on fundamental constants with the Ramanujan Machine"
authors: Gal Raayoni, Shahar Gottlieb, Yoav Manor, George Pisha, Yahel Manor, Uri Mendlovic, Doron Haviv, Yaron Hadad, Ido Kaminer
year: 2021
venue: "Nature 590:67-73"
url: https://www.nature.com/articles/s41586-021-03229-4
url_translated:
language: en
methodology_type: empirical
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Published in Nature 590:67-73 (2021). Earlier arXiv preprint: 1907.00205 (2019, 'The Ramanujan Machine: Automatically Generated Conjectures on Fundamental Constants'). Both the preprint and Nature paper cover the same core system; the Nature publication is the peer-reviewed version. Code and discovered conjectures available at https://ramanujanmachine.com/. Generates conjectures but proving them requires separate human/automated verification — the system is a conjecture *generator*, not a *prover*."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/mathematical-discovery
  - topic/symbolic-regression
  - paper
  - status/draft
---

# Generating conjectures on fundamental constants with the Ramanujan Machine

## Abstract

The Ramanujan Machine is a system that uses algorithms to find mathematical conjectures in the form of formulas involving fundamental constants (π, e, Catalan's constant, values of the Riemann zeta function, etc.). The system discovers conjectures in the form of continued fraction representations and other symbolic expressions. The algorithms find dozens of well-known formulas as well as previously unknown ones. Some conjectures remain unproved — the system generates them for human mathematicians to then attempt to prove. The core algorithm is MITM-RF (Meet In The Middle for Rational Functions), which searches for polynomial continued fractions matching fundamental constants.

## TL;DR

Automated mathematical conjecture generator: exhaustive/heuristic search over the space of polynomial continued fractions to find new formulas relating them to fundamental constants (π, e, Catalan's constant, ζ values). Discovers both known and previously unknown formulas. Generates conjectures; humans prove (or fail to prove) them. Named after Ramanujan, who famously produced remarkable conjectures without proofs.

## Problem

Can an algorithm discover new mathematical conjectures about fundamental constants without human intuition? Specifically: are there polynomial continued fraction representations of π, e, and other constants that are both exact and previously unknown?

## Approach

**MITM-RF (Meet In The Middle for Rational Functions)**: searches the space of polynomial continued fractions $\cfrac{a_0}{b_0 + \cfrac{a_1}{b_1 + \cdots}}$ where $a_i$, $b_i$ are polynomials in the integer index. The algorithm:
1. Partially expands continued fractions from the "top" (partial numerator direction) to get a set of intermediate values.
2. Independently computes from the "bottom" (truncated convergents).
3. Matches when the two meet within numerical tolerance of a known constant.

Matches are conjectures — they suggest (but don't prove) that the continued fraction equals the constant.

The system also uses enumeration-based and RL-guided search variants for other conjecture types.

## Key result

- **Known formulas recovered**: dozens of known formulas for π, e, Catalan's constant, ζ values rediscovered — validating the search methodology.
- **New formulas discovered**: several previously unknown continued fraction representations discovered, including new representations of ζ(3) (Apéry's constant) and ζ(5).
- **Unproved conjectures**: some discovered formulas remain unproved as of the publication date — the system generates more conjectures than humans can currently prove.
- **Ramanujan Machine website**: https://ramanujanmachine.com/ — interactive platform for exploring discovered conjectures.

## Assumptions

- Polynomial continued fractions are a productive search space for conjectures about fundamental constants.
- Numerical matching within high-precision tolerance implies genuine mathematical equality (working hypothesis; not always true, but failures are rare for high-precision matches).
- The MITM approach efficiently covers the combinatorial search space.

## Limitations / scope

- Generates conjectures, does not prove them. The bottleneck has shifted from discovery to proof.
- Search space limited to polynomial continued fractions (PCFs) — other formula types (infinite series, nested radicals) require different algorithms.
- Some discovered formulas may be mathematical curiosities without deep structural meaning.

## Replication evidence

The Ramanujan Machine website allows public exploration of discovered conjectures. Several conjectures have been independently verified numerically by the community. The known-formula recovery results are independently checkable.

## Why this paper matters

The Ramanujan Machine demonstrates that **ML/algorithmic search can generate genuine mathematical conjectures** that human mathematicians then try to prove — shifting the bottleneck from "discovering what to prove" to "proving what the machine found." This is a qualitative change in the mathematician-AI collaboration model:
- Classical ATP (Loos, Kaliszyk, HyperTree) helps prove things humans already know.
- Ramanujan Machine proposes things humans didn't know to ask.

This conjecture-generation paradigm is distinct from both the formal proof search arc (Agents synthesis) and the algorithm-discovery arc (FunSearch). It's the purest example of "ML discovers new mathematics" in this vault.

**Connection to mathematical constant structure**: the Ramanujan Machine's focus on ζ values and Catalan's constant is relevant to number theory. These constants appear in infinite group-theory computations as well (e.g., the volume of arithmetic lattices involves ζ(3)). A machine that generates ζ-value conjectures could, in principle, be trained to probe group-theoretic constants.

## Quotes

> "The algorithms find dozens of well known formulas as well as previously unknown ones... some of which remain unproved." — (from Nature paper summary)

## Open questions surfaced

- Can the Ramanujan Machine be extended to generate conjectures about mathematical objects in abstract algebra (group orders, dimension formulas)?
- How many of the discovered unproved conjectures have since been proved? The publication date (2021) leaves 4+ years of potential follow-up.
- Can the MITM-RF technique be applied to find formulas for specific combinatorial sequences relevant to B(2,5) (e.g., is there a closed-form formula for $|P_s(2,5)|$)?

## Related material in vault

- Related: [[2006.11287]] (Cranmer 2020 — equation discovery via GNN + SR; different methodology for mathematical discovery), [[romera-paredes-2023-funsearch]] (FunSearch — algorithm discovery via evolutionary search; different domain)
- Cross-vault: B(2,5) growth function $|P_s(2,5)|$ (from [[kuznetsov-shlepkin-2009]]) — candidate for SR/conjecture-generation approach
- MOC: `Research/AI in Math/ML/_synthesis-ml-for-math` (forthcoming)
