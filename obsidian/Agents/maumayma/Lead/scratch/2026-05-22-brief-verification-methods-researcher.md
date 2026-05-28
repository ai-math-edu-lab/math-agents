---
author: maumayma
recipient: researcher
sent: 2026-05-22
tags:
  - agent/lead
  - user/maumayma
  - domain/methodology
  - project/none
  - status/draft
  - delegation
---

# Brief — Researcher Verification Methods — Canonical Concepts note for Validator

Sent to **Researcher** on 2026-05-22. Tracked from [[backfill-2026-05-22]]. Triggered by Validator spending ~38 minutes on a verdict that conflated two question shapes; this note becomes the standing reference.

## Triggering context

Validator's in-flight 7,245-char `final_beam.txt` verdict has been paused by Human. Issue: the verdict conflated (a) whether the input word matches a known relator with (b) whether the reduction chain preserves group equality — two different questions. Researcher's Concepts note gives a decision-tree taxonomy Validator consults before deep verifications.

## Message (verbatim — see full brief in delegated maestri message)

> TYPE: REQUEST
> TOPIC: Write Concepts note on group-equality verification methods
> CONTEXT: [[_common]] § Dual-audience writing convention (K3 pattern), [[validator]] role file. Validator currently lacks a shared reference for choosing among verification methods. This note becomes the canonical reference Validator consults on every routed claim.
>
> ASK: Write `Concepts/verification-methods-for-group-equality.md`. K3 pattern. Frontmatter: `domain: methodology`, `project: none` (cross-domain), `status: draft`, `author: maumayma`. Tags `#agent/research #user/maumayma #domain/methodology #project/none #concept #status/draft`.
>
> Body sections cover: question shapes (element equality, trivial-element, chain soundness, confluence, order), the methods (KB completion, Todd-Coxeter, Tietze, abelianization, partial-rule application, GAP, Sage, hand proofs) — each with what it PROVES (necessary / sufficient / both), cost, assumptions, when to use; a decision tree (concrete B(2,5) example: GAP not installed → reduces to abelianization + lifted-KB + hand proofs + structural analysis); escalation rules for missing tools; references to Sims, Havas, KB original, KBMag manual without manufactured citations.
>
> NO code. Vault writes only. Restructure authority allows later refinement.
>
> Report back when done.
>
> DEADLINE: none. Estimated effort: 1-2 hours.

## Downstream chain

Once delivered → Lead routes Validator: "Read `[[verification-methods-for-group-equality]]` before resuming the 7,245-char verdict; use the decision tree to scope your verdict honestly." → Validator revisits → final verdict returns → B25 Experimenter updates `_progress.md` accordingly.

## Status

- Sent 2026-05-22.
- Parallel to: Researcher Part 2 (slide deck — done), B25 backward-links (done), Developer Phase 2-4 (in progress).
