---
tags: [agent/lead, user/maumayma, domain/methodology, topic/vault-tooling, topic/doctrine-consistency, status/draft]
author: maumayma
project: mixer-core
audit_date: 2026-05-28
audit_kind: pre-commit doctrine consistency
out_of_scope: orphan-detection re-run, content review, structure changes
---

# Pre-commit doctrine consistency audit (F11.1)

**Scope**: read-only pass across canonical doctrine files — tag taxonomy, templates, agent prompts, conventions, skill workflows, README, INSTALL, Bases dashboards. **No edits made.**

**Audit method**: read each file in full, check against the source-of-truth `_meta/tags.md`, check for stale doctrine references, check for `[[<placeholder>]]` phantom-source patterns, verify per-user-path discipline, verify peer-set consistency.

---

## Summary verdict

**Status**: nearly ready-to-commit, with 11 minor drift items worth fixing first and 1 clarification needed from Maria. **No contradictions.** The vault's doctrine is internally coherent at the macro level — the drift is concentrated in stale template examples (tag-axis count, deprecated domain enum) and one stray typo. All fixes are surgical.

**Recommended pre-commit fix order** (smallest-first):
1. **Q1 clarification from Maria** — is `#project/grobner` to be registered or to stay deprecated? (5 min answer, gates Fix #1)
2. **Fix 4 template tag-axis gaps** (decision, code-review, experiment, component-doc) — add missing `#user/`, `#topic/`. ~10 min.
3. **Fix component-doc.md stale domain enum** — replace `combinatorics | numerical | algorithms | infra | api` with the 4 registered domains. ~2 min.
4. **Fix validator.md L115 stale domain enum** — same drift as #3, in a different file. ~2 min.
5. **Fix `_common.md` L119 templates list** — add `[[concept-note]]` and `[[synthesis]]`. ~1 min.
6. **Fix developer.md L78 partial tag example** — expand to 6-axis. ~1 min.
7. **Fix experiment-folder-convention.md L55 inline tag example** — bring in line with the Tagging requirements section that follows. ~2 min.
8. **Fix single-paper.md duplicate step 13** — renumber. ~1 min.
9. **Fix INSTALL.md L8 backtick/path typo**. ~1 min.
10. **Optionally**: clarify research-folder-convention.md L13 dir-name vs tag-value relationship. ~2 min.

**Total fix time estimate**: ~30 min if Maria clears Q1.

**After fixes**: ready-to-commit. The vault's structure, conventions, and inter-doc references are otherwise consistent.

---

## Per-doc verdicts

### Source-of-truth files

| File | Verdict | Notes |
|---|---|---|
| `_meta/tags.md` | ✅ consistent, **1 clarification** | 6-axis, 4 domains, 4 projects (mixer-core/b25/b43/b53), content-type tags including Phase 8 additions (#results/#data/#experiment-type). Experiment-tree mapping table present. Deprecated section explicit. **Clarification: Maria's brief mentions registered projects "mixer-core/b25/b43/b53/grobner" — but tags.md explicitly dropped `#project/grobner` in F4.2 per the "don't pre-register future workstreams" rule. Either Maria's brief is slightly outdated OR she's signaling she wants grobner re-registered now (which would change tags.md and impact `grobner.md` paper's project tag). Needs her call before commit.** |
| `_meta/naming-conventions.md` | ✅ consistent | 5 rules + Step 4 (post-Phase-7 follow-up) + Wikilink update CLI procedure + History. Clean. |
| `_meta/research-folder-convention.md` | ⚠️ minor drift | L13 ASCII structure says dir names match `#domain/*` values (e.g. "group-theory"), but actual dir names are human-readable ("Group theory", "AI in Math"). Could clarify: dir names readable; tag values kebab-case. Phase 7 + 9 + 10 doctrine sections all landed correctly. |
| `_meta/experiment-folder-convention.md` | ⚠️ minor drift | L55 inline tag example missing `#user/<handle>` and `#topic/<one+>` — but the comprehensive Tagging requirements section at L117-137 is correct 6-axis. Inline example needs update to match. Phase 8 content-type table + Phase 9 cross-linking + Phase 10 backtick rule all landed correctly. |

### Templates (`_templates/`)

| File | Verdict | Notes |
|---|---|---|
| `paper-summary.md` | ✅ consistent | 6-axis tag example complete. Phase 10 doctrine bullet added to Notation conventions. All `[[...]]` examples backtick-wrapped. |
| `concept-note.md` | ✅ consistent | 6-axis tag example complete. Frontmatter has `introduced_in`/`related_concepts`/`appears_in` per concept-hub doctrine. No placeholder phantoms. |
| `synthesis.md` | ✅ consistent | 6-axis tag example complete. Phase 10 `[[<paper-note>]]` backtick fix landed. |
| `experiment.md` | ⚠️ drift | Tag example `[agent/exp, experiment, domain/<...>, status/pending]` MISSING `user/<handle>` and `topic/<one+>` — 6-axis violation. Phase 10 backtick fix on `[[<output-note>]]` landed (L87-88). Need: add user + topic to the tag example array. |
| `code-review.md` | ⚠️ drift | Tag example `[agent/lead, review, domain/<...>, status/<verdict>]` MISSING `user/<handle>` and `topic/<one+>` — 6-axis violation. Body sections doctrine-aligned with Lead's review workflow. Need: add user + topic. |
| `decision.md` | ⚠️ drift | Tag example `[agent/<author>, decision, domain/<...>, status/<proposed\|accepted\|rejected\|superseded>]` MISSING `user/<handle>` and `topic/<one+>` — 6-axis violation. Need: add user + topic. |
| `component-doc.md` | ⚠️ drift (2 items) | (i) L4 `domain` enum says `<group-theory \| combinatorics \| numerical \| algorithms \| methodology \| infra \| api>` — only `group-theory` and `methodology` are registered; `combinatorics`, `numerical`, `algorithms`, `infra`, `api` are NOT registered per current `_meta/tags.md` § Axis 3 (the 4 registered are group-theory/ai/cs/methodology). (ii) L20 tag example `[agent/dev, domain/<…>, status/<production\|paper\|deprecated>]` MISSING `user/<handle>` and `topic/<one+>`. Both Phase 10 `[[<...>]]` backtick fixes landed correctly. |

### Agent prompts (`_meta/agents/`)

| File | Verdict | Notes |
|---|---|---|
| `_common.md` | ⚠️ minor drift | L119 templates list shows `[[component-doc]], [[experiment]], [[paper-summary]], [[decision]], [[code-review]]` but MISSING `[[concept-note]]` and `[[synthesis]]` — both are real templates per `_templates/` and used by Researcher. Phase 5 6-axis update + L94 per-user-path discipline + L101 6-axis minimum reminder all correct. |
| `lead.md` | ✅ consistent | 6-axis at L102 with `#topic/<one+>` + project conditional. Phase 5 per-user paths. Phase 10 backtick fix on L127. 5-peer cross-agent integration (Developer/Researcher/Experimenter/Experimenter-B25/Validator) + Human. Obsidian Write Scope matches README's roster table row for Lead. |
| `developer.md` | ⚠️ minor drift | L78 says "Tag `#agent/dev #status/draft`" for the scratch plan — only 2 axes; should be 6-axis (add user/domain/topic). Phase 10 backtick fixes on L116 + L120 landed. 5-peer cross-agent listing correct. Phase 5 per-user paths consistent. |
| `experimenter.md` | ✅ consistent | L88 pre-register tag is full 6-axis with project (required for experiments). Phase 8 content-type tag addition in Phase 4. Phase 10 backtick fixes throughout. 5-peer cross-agent listing correct. Write scope matches README. |
| `experimenter-b25.md` | ✅ consistent | L85 pre-register tag full 6-axis with mandatory `#topic/burnside #topic/b25`. Phase 7 `<technique>-results.md` filename reference. Phase 8 content-type tag note. Phase 10 backtick fixes. Write scope matches README. |
| `validator.md` | ⚠️ drift | L115 `domain:` frontmatter example says `<group-theory \| grobner \| sat \| biology \| ...>` — `grobner`, `sat`, `biology` are NOT registered domains (and per F4.2 doctrine should not be pre-registered). Should be `<group-theory \| ai \| cs \| methodology>`. L122 tags example correctly shows 6-axis. Phase 10 backtick fixes throughout. Cross-agent integration + write scope correct. |
| `researcher.md` | ✅ consistent | 6-axis tag minimum (L70-79) lists all 5 mandatory + content-type. Domain list at L74 matches current 4 registered. Phase 10 backtick fixes (L158). Description correctly excludes Mixer-specific bias from standing prompt (Phase 6 brief compliance). Cross-agent integration + Write scope match README. |

### Skill workflows (`_meta/skills/research/`)

| File | Verdict | Notes |
|---|---|---|
| `SKILL.md` | ✅ consistent | References [[paper-summary]], [[concept-note]], [[synthesis]]. 4 invocation modes documented. Phase 7 generic-filename rule in "What this skill does NOT do". Tag conventions correctly described. |
| `workflows/single-paper.md` | ⚠️ minor drift (1 item) | Step 13 appears TWICE: once as "Write the note", once as "Apply 6-axis tags". Subsequent steps renumber correctly through 14, 15, 16. The second 13 should be 14, then 14 → 15, etc. Phase 9 step 15 (verify ≥3 outgoing wikilinks) + Phase 10 placeholder check both landed. |
| `workflows/batch.md` | ✅ consistent | 8 steps. Relies on single-paper for per-paper discipline (including the Phase 9 ≥3 wikilinks check + Phase 10 placeholder check). Step 5 cross-batch connection sweep + step 6 concept hub sweep. |
| `workflows/literature-scan.md` | ✅ consistent | Phase 1-4 (Scoping with invoker, Read & extract via batch, Synthesize, Report). Anti-patterns section (scope creep, padding, sales prose). Stop conditions. |
| `workflows/connection-pass.md` | ✅ consistent | 7 steps. Step 5 explicit bidirectional repair sweep. Restructure authority noted. Per-user log path. |

### Vault-root + install docs

| File | Verdict | Notes |
|---|---|---|
| `README.md` | ✅ consistent | "6-axis tag taxonomy" + 6-role agent roster table + per-user `Agents/<user>/<role>/` structure + vault dir structure + Bases dashboard list (Components/Experiments/Concepts/Papers) + "renamed from Mixer Applications" breadcrumb + Validator authority + mixer-Agent-vs-AI-agent terminology. All `[[...]]` are real wikilinks (no placeholders). |
| `_meta/skills/research/INSTALL.md` | ⚠️ minor drift | L8 has a typo: "Default path: Documents/Obsidian/Math/`" — stray closing backtick, missing leading `~/` or other path prefix. Should read something like "Default path: `~/Documents/Obsidian/Math/`". Otherwise install procedure is correct (symlink pattern, verification, troubleshooting). |

### Bases dashboards (`Architecture/Mixer/Bases/`)

| File | Verdict | Notes |
|---|---|---|
| `Papers.base` | ✅ consistent | Phase 5 build + Phase 8 fix; queries language/methodology_type/citation_count/relevance/domain/project/author. All fields match `paper-summary.md` frontmatter schema. `_README.md` documents the Bases multi-value-groupBy limitation + the Maria-Option-A decision log. |
| `Concepts.base` | ✅ consistent (per Phase 5 read) | Properties status/domain/project/author + status-icon formula. Status values include validated/draft/review/superseded — match `_meta/tags.md` lifecycle values. Domain values constrained to current registered set via the underlying concept-note frontmatter. |
| `Experiments.base` | ✅ consistent | Phase 8 build by Developer. Adds `By experiment-type`, `Methodology inventory`, `Results inventory`, `Data inventory` filtered on `#methodology`/`#results`/`#data`. Global filter refactor preserves pre-existing view semantics (verified via Developer's base:query). `_README.md` documents the global-filter refactor + `and:`/`or:` nesting gotcha. |
| `Components.base` | ⚠️ inherited drift | The base's properties + groupBy/filter shape are correct, BUT the base reads the `domain:` frontmatter from component notes, and `component-doc.md` template's domain enum is stale (see Templates table above). Fixing `component-doc.md` resolves this — no Bases edit needed. |

---

## All Phase-10-era placeholder backtick fixes verified

Spot-checked across templates, agent prompts, and Lead scratch — no bare `[[<placeholder>]]` remains in body text. Verified via `grep -rn '\[\[<' _meta/agents/ Agents/maumayma/Lead/scratch/ _templates/ | grep -v '`\[\[<'` returning empty (all instances are inside backticks).

## All Phase-9-era cross-linking discipline rules referenced

`research-folder-convention.md` § Cross-linking discipline + `experiment-folder-convention.md` § Cross-linking discipline + `single-paper.md` step 15 all spell out the same 3+ wikilink minimum + bidirectional reciprocation + substance test + housekeeping exemption rules. Consistent.

## All per-user-path references consistent

`Agents/<your-user>/<your-role>/` pattern used in `_common.md` § Obsidian write rules, all six agent prompts' Obsidian Write Scope sections, README's vault structure, INSTALL.md's per-user log reference. No stale flat `Agents/<role>/` patterns remain.

## All cross-agent integration peer sets consistent

Every agent prompt lists its 5 peers + Human:
- lead.md: Developer / Researcher / Experimenter / Experimenter-B25 / Validator / Human
- developer.md: Lead / Validator / Researcher / Experimenter / Experimenter-B25 / Human
- researcher.md: Lead / Experimenter / Experimenter-B25 / Developer / Validator / Human
- experimenter.md: Lead / Validator / Experimenter-B25 / Researcher / Developer / Human
- experimenter-b25.md: Lead / Validator / Researcher / Experimenter / Developer / Human
- validator.md: Lead / Experimenter / Experimenter-B25 / Researcher / Developer / Human

Matches README's 6-role roster table.

---

## Hard constraint compliance

This audit is read-only. **No edits made to any file.** All findings above are reports of state, not actions taken. Maria reviews this report, decides which fixes to route + to whom, then commits.
