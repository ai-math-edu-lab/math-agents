---
title: "T-020 Peiffer loophole and fix — triage"
status: conjectured
domain: group-theory
project: challenge-gen
claim: "F* misses Peiffer pairs; a pair test fixes it; finite B(2,5) ⇒ linear Dehn function over {u⁵}"
claimant: MathExpert (via Lead)
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/proof-certificates, project/challenge-gen, status/conjectured, triage]
---

# Triage — T-020
Written at task start, filled in after the run (the checks were small, minutes each).
Source: MathExpert proposal 2026-10-14 § Three cautions; [[project-challenge-gen]] § Cautions on D; PR #9 (b25 `17-t020-peiffer-check` @ 9a35fd2).

- **Premise/model:** everything is an identity in the free group F(a,b) (factor words, expansions), plus the definition B(2,5) = F/⟨⟨u⁵⟩⟩. No finite quotient is used. Claim 3 is conditional ("if B(2,5) is finite").
- **Sub-claims:** 1 (pair deletion keeps w; is T-001 an instance), 2a (correct test), 2b (order), 2c (larger blocks), 2d (cheap computation), Lead's extra (loop erasure in the fixpoint), 3 (Dehn argument).
- **Tools:** python3 3.12.3; the harness `certificate.expand`, `loop_erase` (b25 @ b98c938), with `std_table` and the tcgraph_ext table; PR #9 `peiffer_reduce` loaded from 9a35fd2. Free-group equality = exact freely reduced word equality.
- **Methods:** hand proofs (1, 2a, 3); constructive witnesses (2c, extra); exhaustive search over deletion orders on small words (2b); randomised checks against direct re-expansion (criterion, incremental update).
- **Limits:** no lower bound on true area; nothing about how often a search exploits each loophole in T-003 data.
