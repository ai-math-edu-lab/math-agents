---
author: maumayma
recipient: researcher
sent: 2026-05-22
tags: [agent/lead, user/maumayma, domain/group-theory, project/none, status/draft, delegation]
---

# Brief — Researcher Open-Problems Catalog — Unsolved group theory + Mixer/AI feasibility scoring

Sent to **Researcher** on 2026-05-22. Tracked from [[backfill-2026-05-22]].

## Task summary

Build a canonical, K3-structured catalog of unsolved problems in group theory at `Research/Group theory/Open problems/`. Score each problem 1-3 on AI/Mixer feasibility with explicit reasoning. Use existing Research/ infrastructure (Kourovka 2022, Havas papers, Problems-people, the Concepts notes already in place). NO invented problems or citations.

## Scoring rubric (Researcher uses; Lead K3-reviews)

- **score/1** — low probability of Mixer/AI contribution; requires deep structural / nilpotency / classification arguments.
- **score/2** — medium; partial computational evidence; Mixer might contribute a step.
- **score/3** — high; concrete computational instance, Mixer's specific machinery directly applies, output is verifiable artifact.

## Doctrine pinned into the brief

- Sourcing rule: every problem must trace to a canonical reference. NO invented problems.
- Authorship: `author: maumayma` only (lesson from Validator's `heypidor` fabrication earlier this session).
- Tag format: canonical inline-array (lesson from Developer's quoted-`#tag` format being invisible to Obsidian).
- Probe-before-assume on tools (lesson from Validator's GAP assumption).
- Restructure authority granted for `Research/Group theory/Open problems/` family.

## New tag axis

`score/{1,2,3}` is a new tag axis introduced by this catalog. After delivery, Lead queues `_meta/tags.md` update via commit ritual.

## Initial expected problems to score

- Kourovka 11.48 (Kostrikin 1990) — B(2,5) finiteness
- Burau faithfulness for n=4
- Kaplansky zero-divisors
- 3-5 additional Kourovka-sourced problems of Researcher's selection

## Hand-off expected

- Catalog `_overview.md` with scope statement + score distribution + per-family directory list
- Per-problem K3 notes
- Restructure log entries in `Agents/Researcher/log.md`
- Hand-off list: problems needing paper acquisition; problems needing Validator input on algorithmic angle

## Estimated effort

2-4 hours, substantial literature triage. No deadline.
