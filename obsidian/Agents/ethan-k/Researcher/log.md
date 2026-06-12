---
tags:
  - agent/research
  - user/ethan-k
---

# Researcher log — ethan-k

## 2026-06-10 — Full-text verification pass on [[kalika-2026]]

Source: local PDF (54 pp., `MastersThesisDocs/Biasing_Knuth_Bendix_Completion_and_Algorithm_Mixing_in_the_B_2_5_Problem.pdf`), text extracted in full via pypdf. Existing summary (created 2026-06-05) checked line-by-line; invoked via `/research <pdf>`, invoker chose "update in place" over skip/re-ingest.

Changes to [[kalika-2026]]:

- `cites`: removed `[[knuth-bendix-1970]]` — not in the thesis bibliography (exactly 3 entries: Epstein et al. 1992, Havas–Wall–Wamsley 1974, Sims 1994). Kept as a "Background" link in the body. Sims 1994 has no vault note; recorded in body text only.
- Key result: added confluence-included timings (Table 3.1 — RPO baseline beats both mixing configs on B(4,3)), the "all but one case in-between" observation, the M11 ordering reversal (No-Free-Lunch instance), and the solution-diversity finding (distinct M11 rewriting systems recovered in one mixed run).
- Approach: subword set S also draws from the original target words; subword predicate fails the *alternative* carry-over properties (RHS-only dependence breaks explicit reversibility).
- Replication evidence / quality_notes: full lab name (Lab for AI in Mathematics and Mathematics Education) + Nebius Group support; reader Andrey Nikolaev; verification provenance line.

Bidirectional fixes (missed by the 2026-06-05 ingest):

- [[epstein-et-al-1992-word-processing]]: `cited_by` was empty → added `[[kalika-2026]]`
- [[havas-wall-wamsley-1974]]: `cited_by` += `[[kalika-2026]]`
- [[kb-mixing-stagnation]], [[mixable-api]]: `appears_in` += kalika-2026
