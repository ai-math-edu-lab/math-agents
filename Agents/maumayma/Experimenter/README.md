---
tags: [agent/exp, meta]
---

# Experimenter — home (Math)

Role definition: `_meta/agents/experimenter.md`.

## What lives here
- [[log]]
- `scratch/` — hypothesis drafts pre-registration, exploratory queries
- `output/` — full captured run outputs
- Pre-registered experiments + results → `Experiments/`
- Reusable pipeline docs → `Architecture/Pipelines/`

## Working state
- Active experiments:
- Awaiting Lead decision:
- Recent rejections (lesson archive):

## Evidence bar (mandatory for every claim)
1. Pre-registration (date earlier than result)
2. Provenance triple: git SHA + uv.lock hash + mixer-core build hash
3. Single-algorithm baselines on same problem + same seeds
4. n≥5 seeds for quantitative claims
5. Statistical test + effect size (not just p-value)
6. Cross-verification for math claims (kbmag_v1 or independent derivation)

Any missing → `#status/inconclusive`.
