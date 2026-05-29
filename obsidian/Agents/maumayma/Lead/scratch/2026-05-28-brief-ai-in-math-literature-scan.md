---
tags: [agent/lead, user/maumayma, domain/ai, topic/literature-scan, topic/ai-in-math, status/draft]
author: maumayma
project: mixer-core
brief_date: 2026-05-28
audience: Researcher
---

# Brief — Populate `Research/AI in Math/` via three sub-area literature scan

Sender: Lead (relaying Maria's brief verbatim, with explicit-GO gate discipline).
Recipient: Researcher.

## Goal

`Research/AI in Math/` is currently empty. Populate with a foundational + recent-SOTA snapshot organized into three sub-areas. Scope: medium (5-10 papers per sub-area, 20-30 total). Goal is a populated, queryable, navigable subtree — not exhaustive coverage.

## Three sub-areas

- **Agents for math** — LLM-driven theorem provers, agentic proof search, autoformalization scaffolding
- **RL for math** — reinforcement-learning-guided tactic selection, RLHF on math benchmarks, value-network-guided proof search
- **ML for math** — non-agent non-RL: equation/conjecture discovery, neural heuristic guidance, embeddings-for-math, ML-guided algorithm selection

## Inclusion priority

Current year is **2026**. "Recent" = 2025-2026.

1. **Foundational papers** (the ones every subsequent paper cites — Polu-Sutskever 2020, original AlphaGeometry, original GPT-f, etc.)
2. **Recent SOTA** (2025-2026 — DeepSeek-Prover-V2, Lean Copilot recent versions, AlphaProof, AlphaGeometry 2, current Math-LLM scaffolds, etc.)
3. **Skip the middle stretch** — incremental 2021-2024 papers UNLESS they introduce a genuinely new approach (e.g. the original FunSearch paper if you rate it as a new approach rather than incremental)

## Workflow per sub-area

Each sub-area follows three phases: **A1/A2/A3** (then **B1/B2/B3** for sub-area B, **C1/C2/C3** for C).

### A1 / B1 / C1 — Candidate proposal (no fetching)

Per `[[literature-scan]]` workflow Phase 1 scoping:

- Propose 5-10 candidate sources per sub-area.
- Format: numbered list with author + year + venue + one-line claim.
- Foundational + recent only; skip middle-stretch incremental work.
- **DO NOT FETCH YET.** Surface candidates to Lead. Lead K3-reviews + surfaces to Maria for go/no-go. **WAIT for explicit GO from Lead before starting A2/B2/C2.**

### A2 / B2 / C2 — Ingest (gated on explicit GO from Lead)

Per `[[single-paper]]` workflow per approved candidate:

- **Step 13 structural-placement check** mandatory. Path placement:
  - Sub-area A papers → `Research/AI in Math/Agents/<paper-id>.md`
  - Sub-area B papers → `Research/AI in Math/RL/<paper-id>.md`
  - Sub-area C papers → `Research/AI in Math/ML/<paper-id>.md`
  - Papers genuinely spanning two sub-areas (rare — substance-test first): pick primary, link from the other's synthesis.
- **Create the three subdirs at the start of A2** if they don't exist. Add `_README.md` to each subdir (3-5 lines defining what belongs there) per `[[research-folder-convention]]`.
- **Step 17 outgoing-wikilinks check** (≥3 per note) before save.
- **Register new topic tags in `_meta/tags.md` BEFORE applying them** per `[[researcher]]` doctrine line 93 (lesson from the Kuznetsov R2 K3 NEEDS-WORK).
- arxiv-id filenames where applicable (most of these papers will be on arXiv): `<arxiv-id>.md` (e.g. `2009.03393.md` for Polu-Sutskever 2020). Uniquely identifying + timeless.
- Citation count lookup mandatory per `[[single-paper]]` step 6. Semantic Scholar typically covers AI/ML papers well.

### A3 / B3 / C3 — Sub-area synthesis

Per `[[synthesis]]` template. Paths:

- A3: `Research/AI in Math/Agents/_synthesis-agents-for-math.md`
- B3: `Research/AI in Math/RL/_synthesis-rl-for-math.md`
- C3: `Research/AI in Math/ML/_synthesis-ml-for-math.md`

Cover: settled / contested / open questions in the sub-area.

## Tagging

- **Domain** for all papers: `#domain/ai` (the field whose methodology contributes; the application happens to be math).
- **Topic tags** (substance test mandatory, 4-10 per paper, register in `_meta/tags.md` BEFORE applying). Expected candidates:
  - Sub-area A: `#topic/automated-theorem-proving`, `#topic/lean`, `#topic/llm-prover`, `#topic/autoformalization`, `#topic/agentic-reasoning`
  - Sub-area B: `#topic/reinforcement-learning`, `#topic/monte-carlo-tree-search`, `#topic/proof-search`, `#topic/value-network`, `#topic/rlhf`
  - Sub-area C: `#topic/symbolic-regression`, `#topic/conjecture-generation`, `#topic/neural-symbolic`, `#topic/funsearch`, `#topic/embeddings-for-math`
- **Only register what actually applies.** Don't pre-register the full list.

## Coordination with existing vault

- **Cross-link to `Research/Group theory/`** when an AI-in-math paper applies to or cites group theory work. The B(2,5) cluster will care about Lean-formalized group theory papers, AlphaGeometry-style symbolic-engine work, etc. **Bidirectional cites/cited_by mandatory** (per Phase 8 F8.4 discipline).
- **Concept hubs**: if a concept appears in 2+ papers across sub-areas (e.g. "tactic-level supervised fine-tuning"), create `Concepts/<concept>.md` per the existing pattern.
- **MOC update** (post-final-sub-area): create `Research/AI in Math/_MOCs/_moc-ai-in-math.md` linking all sub-area syntheses + landmark papers per sub-area. Template: use the existing MOCs in `Research/Group theory/_MOCs/` as the pattern.

## Sequencing + gates

1. **A1** (proposal) → maestri ack to Lead → Lead K3 + surface to Maria → **explicit GO** for A2
2. **A2** (ingest) → **A3** (synthesis) → maestri checkpoint to Lead → Lead K3 sample-review (synthesis + 2 papers for discipline compliance) → if clean, **explicit GO** for B1
3. **B1** (proposal) → same gate as A1 → **explicit GO** for B2
4. **B2** → **B3** → checkpoint → **explicit GO** for C1
5. **C1** → same gate → **explicit GO** for C2
6. **C2** → **C3** → checkpoint
7. **Post-all-three**: create `_moc-ai-in-math.md`, run `find-graph-orphans.py` (expect 0), run bidirectional-link verifier. Final report to Lead with counts (papers per sub-area, concept hubs created, cross-cluster links to Group theory).

## Constraints

- **No pre-ingest without explicit GO from Lead.** Per the new `feedback_explicit_go_gates` discipline: completing the prior phase and reporting it is NOT a green-light. Wait for a literal GO/PROCEED/GREEN-LIGHT token from Lead.
- **Translation discipline**: most papers will be English (the field is English-dominant). Any non-English exceptions follow normal `[trans.]` discipline per `[[paper-summary]]`.
- **Token budget**: 20-30 papers across 3 batches is heavy. Checkpoint with Lead after each sub-area (post-A3, post-B3, post-C3). Don't try to do all three in one session. If you hit a token wall mid-A2/B2/C2, save state to log, ping Lead, resume next session.

## Out of scope

- Papers applying **math TO AI** (different direction — "math foundations of ML" is its own area; not this brief).
- Pure benchmark papers (MATH, miniF2F, ProofNet) — those are scaffolding, not contributions. If they're heavily cited by approved candidates, ingest as supporting context only. Otherwise skip.
- Survey papers — include ONLY if foundational (e.g. the original DL-for-math survey) or recent + comprehensive. Default skip.
- Pre-2020 papers UNLESS genuinely foundational (e.g. Polu-Sutskever 2020, GPT-f predecessors). The field's mature output is 2020+.
- Other sub-areas of AI-in-math (e.g. computer vision for math notation OCR, math chatbots for education) — not in the three sub-areas Maria specified.

## Deliverables per phase

- **A1/B1/C1**: candidate list (numbered, with author + year + venue + one-line claim) reported to Lead.
- **A2/B2/C2**: paper notes in the relevant subdir, registered topic tags, concept hub stubs, bidirectional links populated.
- **A3/B3/C3**: synthesis note.
- **Final**: MOC at `Research/AI in Math/_MOCs/_moc-ai-in-math.md` + orphan re-check (expect 0) + final report to Lead with counts.

## Effort estimate

Per sub-area: A1 ~10 min, A2 ~5-10 min per paper × 5-10 papers = 30-90 min, A3 ~20 min. Total per sub-area: ~60-120 min. Three sub-areas: ~3-6 hours total, split across sessions per Maria's token-budget guidance.
