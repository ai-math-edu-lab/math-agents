---
title: "T-001 L0 soundness and words 13/14 — triage"
status: conjectured
domain: group-theory
project: challenge-gen
claim: "(1) L0 (literal-5th-power relators + re-expansion) proves w trivial in free B(2,5); (2) words idx 13, 14 of ds-b25-trivial-2-5reduced-aut8-20261007 are trivial in free B(2,5) and are not 2.5-fixed points"
claimant: Experimenter
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, project/challenge-gen, status/conjectured, proof, triage]
---

# Triage — T-001 math claims
Source: [[hardness-baselines-results]] § Math claims routed to Validator.

## Sub-claims
- **P (premise/model).** Target is free B(2,5) = F(a,b)/⟨⟨x⁵ : x∈F⟩⟩ (definition). No finite quotient, no relator file stands in for it. Nothing here is circular: (1) is a proof from the definition; (2) is an explicit rewriting trace whose every step is justified by v⁵=1.
- **1a.** A literal u⁵ is a relation of B(2,5): by definition.
- **1b.** c⁻¹u⁵c is a conjugate of u⁵, hence in the normal closure.
- **1c.** Product of such = w̄ in F(a,b) (free reduction, checked by independent expansion) ⇒ w̄ ∈ normal closure.
- **2a.** idx 13, 14 reduce to empty by a trace of valid steps (self-written trace checker, rule justified by lemma below).
- **2b.** Dataset's "every word is a fixed point" claim fails on these strings.

## Tools (probed)
python3 (/usr/bin/python3), GAP 4.15.1 (~/Research/mixer/gap-4.15.1/gap). Producing path = tcgraph C++ reducer; my trace checker is independent of it and of kbprog.

## Methods
- 1: hand proof (sufficient).
- 2a: step-checked rewriting trace. Each step sound by the lemma: for a word v and L≤5m with u = prefix of v^∞ of length L, m=|v|: u·(rest of v⁵)=v⁵=1 so u = (V[L:5m])⁻¹. Sufficient for triviality in free B(2,5) (not a finite-quotient argument).
- 2a cross-check: GAP free-group word equality of trace endpoints is not needed; abelianization/B₀ quotient checks are necessary-only and will be labelled so.

## Limits
Does not re-derive the dataset's kbprog proof for the other 818. Does not assess whether the reducer is complete.

## Recommendation
Full verification path.
