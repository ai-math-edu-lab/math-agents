---
tags: [agent/lead, log]
---

# Lead — Activity Log (Math)

Append-only. Latest at top.

---

## 2026-05-28 — Phase 11 — pre-commit doctrine consistency audit + 4 Lead fixes

**F11.1 (Lead, read-only audit)**: read-only pass across canonical doctrine files (tags.md, naming-conventions, both convention files, all 7 templates, all 6 agent prompts, SKILL + 4 workflows, README, INSTALL, 4 .base files). Report at `[[2026-05-28-pre-commit-audit]]`. Verdict: 11 minor drift items + 1 clarification needed. No contradictions. Vault internally coherent at the macro level; drift is concentrated in stale template tag examples + deprecated domain enums + one typo.

**Maria's directive (received same turn):**

- Q1 grobner clarification → (a) doctrine stays. Brief was slightly outdated. No fix needed.
- Routing split:
  - **Researcher (6 fixes)**: #2 experiment template, #3 code-review template, #4 decision template, #5 component-doc template (domain enum + tag axes), #10 single-paper.md duplicate step 13, #11 INSTALL.md typo. Routed via `brro9xtw6`.
  - **Lead (4 fixes, done this turn)**:
    - **#6** `_meta/agents/validator.md` L115: stale `domain:` frontmatter example `<group-theory | grobner | sat | biology | ...>` → `<group-theory | ai | cs | methodology>` (matches current registered set).
    - **#7** `_meta/agents/_common.md` L119: K3 templates list expanded — added `[[concept-note]]` + `[[synthesis]]` (both are active templates per `_templates/`; were missing from the listing).
    - **#8** `_meta/agents/developer.md` L78: scratch-plan tag promoted from 2-axis to 6-axis with project-add guidance (`#agent/dev #user/<handle> #domain/cs #topic/<one+> #status/draft` + add `#project/*` when scratch is project-scoped).
    - **#9** `_meta/experiment-folder-convention.md` L55: inline tag example expanded from `[agent/exp, experiment, methodology, domain/group-theory, project/b25, status/validated]` to full 6-axis with topic/burnside + topic/knuth-bendix + user/<handle> + content-type tags last (the Tagging requirements section at L117-137 was already correct; the inline example was lagging).
- #12 (research-folder-convention dir-vs-tag clarification) → deferred. Not drift, not a confusion source today.

**Phase 11 close-out**: Researcher's 6 fixes landed cleanly. Spot-checked #5a (component-doc.md L4 now `<group-theory | ai | cs | methodology>` — matches the 4 registered domains) and #10 (single-paper.md steps 1-17 sequential, no duplicates; step 16 carries Phase 9 + 10 wikilink/placeholder check, step 17 is Report back). Per Maria's directive, no formal code review for surgical text fixes.

**Phase 11 disposition — both passes complete:**

| # | File | Fix | Owner | Status |
|---|---|---|---|---|
| #2 | `_templates/experiment.md` | Tag example → 6-axis with user/topic/project | Researcher | ✅ landed |
| #3 | `_templates/code-review.md` | Tag example → 6-axis with user/topic; review at end | Researcher | ✅ landed |
| #4 | `_templates/decision.md` | Tag example → 6-axis with user/topic | Researcher | ✅ landed |
| #5a | `_templates/component-doc.md` L4 | Domain enum → 4 registered (group-theory/ai/cs/methodology) | Researcher | ✅ landed (verified) |
| #5b | `_templates/component-doc.md` L20 | Tag example → 6-axis | Researcher | ✅ landed |
| #6 | `_meta/agents/validator.md` L115 | Domain frontmatter enum → 4 registered | Lead | ✅ landed |
| #7 | `_meta/agents/_common.md` L119 | K3 templates list → +concept-note +synthesis | Lead | ✅ landed |
| #8 | `_meta/agents/developer.md` L78 | Scratch-plan tag → 6-axis + project guidance | Lead | ✅ landed |
| #9 | `_meta/experiment-folder-convention.md` L55 | Inline tag example → match Tagging requirements section | Lead | ✅ landed |
| #10 | `_meta/skills/research/workflows/single-paper.md` | Renumber duplicate step 13 → 1-17 sequential | Researcher | ✅ landed (verified) |
| #11 | `_meta/skills/research/INSTALL.md` L8 | Backtick/path typo → `~/Documents/Obsidian/Math/` | Researcher | ✅ landed |

**Vault status: ready to commit and push to `github.com/ai-math-edu-lab/math-agents`.** All Phase 11 drift cleared. Positive findings from F11.1 audit (placeholder backticks vault-wide, peer-set consistency across 6 agent prompts + README roster, per-user path discipline, Phase 8/9/10 doctrine integration) preserved.

**INITIAL COMMIT + PUSH LANDED (2026-05-28):**

- **Branch**: `main`
- **SHA**: `66bfcfa` (`66bfcfae737de5116c5be65a1bd276a6c81057f1`)
- **Remote**: `https://github.com/ai-math-edu-lab/math-agents.git`
- **Upstream**: `origin/main`
- **Files**: 172 (16,702 insertions)
- **Commit message**: `chore: initial commit of Math vault doctrine + content`

**Commit ritual notes:**
- Maria authorized `git add .` (first-time bulk; gitignore is the gate).
- Preconditions verified before bulk-add: `git init -b main` done; `.gitignore` matches `.obsidian/workspace.json`; `.obsidian/graph.json` NOT ignored (per Maria's spec); remote `origin` configured at the github.com/ai-math-edu-lab/math-agents URL.
- Staged file breakdown: Research 54, Agents 33, Architecture 28, _meta 21, Experiments 13, Concepts 8, _templates 7, .obsidian 4, People 2, README.md, .gitignore. No `.trash/` or `.DS_Store` leaked. No `.obsidian/workspace.json` leaked.
- Initial `git push -u origin main` REJECTED — remote had been initialized with 2 noise commits (a README create and a `obsidian/Readme.md` delete, netting to empty tree). No common ancestor with our local `main`.
- Maria explicitly authorized force-push (force-push to `main` is in the per-action authorization list per [[lead]] doctrine; her earlier "push" approval did not extend to `--force`).
- `git push --force -u origin main` succeeded. Remote tip now matches local SHA `66bfcfa`. Upstream tracking set.

**Vault now live on GitHub.** Next directive from Maria: draft `CLAUDE.md` + `.claude/commands/setup.md` + repo-root `README.md` against the real repo at `github.com/ai-math-edu-lab/math-agents`. The remote URL + default branch (`main`) confirmed to her in the same turn.

No commit (vault not under git per the standing convention).

---

## 2026-05-28 — Phase 7 + MOC pass complete; small follow-ups routed

**MOC pass (Researcher, before Phase 7 brief arrived — option (b)):** 4 LYT-discipline MOCs at `Research/Group theory/_MOCs/` covering burnside (7 wikilinks), knuth-bendix (10), word-problem (10), presentations-and-orders (11). Total 38 curated annotated wikilinks. Each MOC has substantive one-line "why this is here" annotations on every link (not auto-dumps). Cross-MOC navigation via "Related MOCs" sections. K3 spot-check on `_moc-burnside.md` confirms LYT discipline — Mixer framing appears only as routing to existing Mixer-framed paper notes (`[[algo-mixing-burnside-slides]]`, `[[b25-finiteness-11.48-kostrikin]]`), not introducing new framing.

**Phase 7 (Researcher):**

- **F7.1 — Naming convention doctrine:** Created `_meta/naming-conventions.md` with 5 rules (unique filenames, kebab-case, `_` prefix reserved for index/MOC notes, avoid generic words, paper-note patterns) + CLI wikilink-update procedure. Appended naming section to `_meta/research-folder-convention.md`. K3 read: doctrine is complete, examples table is clear, history line records the trigger (Maria's `_overview` × 10 observation).
- **F7.2 — 14 renames:** 7 `_overview.md` in Research/ → uniquely qualified; 3 `results.md` and 3 `data.md` in Experiments/ → uniquely qualified; 4 MOC files → `_moc-<topic>.md` (per F7.1 rule 4 — underscore prefix for index/MOC notes). Wikilink-grep across vault confirms no stale `[[_overview]]` or `[[results]]/[[data]]` references remain.
- **F7.3 — Domain frontmatter audit:** Surfaced a bigger gap than Maria's initial observation — **all 15 Research/ paper notes were missing the `domain:` frontmatter field** (only had `#domain/*` tag). F4.3 migrated tags but didn't add the frontmatter field that Bases queries. Backfilled all 15 (13 group-theory, 1 methodology, 1 cs for grobner). Papers.base "Domain" column now correctly populated. K3 spot-check on `grobner.md` confirms `domain: cs`, no `#domain/grobner` tag remnants, `quality_notes` explains the migration.
- **F7.4 — `/research` skill update:** `single-paper.md` workflow gets a step on unique filename requirement; `SKILL.md` "What this skill does NOT do" section gets a doctrine line referencing `[[naming-conventions]]`. K3 read confirms both.

**Small follow-ups routed in this turn:**

1. **MOC cross-reference cleanup** (Researcher, `bz18jnh07`, background) — K3 grep found 10 stale wikilinks in MOCs' "Related MOCs" sections still pointing at pre-rename names (`[[burnside-moc]]`, `[[knuth-bendix-moc]]`, etc.). Root cause: F7.2 wikilink update didn't catch the recursive case (renamed files reference each other). ~5 min sed-replace fix. Suggested Researcher add a "check renamed files reference each other" bullet to `[[naming-conventions]]` § Wikilink update on rename.
2. **Architecture/ `_overview.md` rename** (Developer, `bwb1aqfua`, background) — 3 files (`KBMag/_overview.md`, `Mixer Core/_overview.md`, `UI/_overview.md`). Researcher correctly stayed in their lane and flagged this for routing. Brief at `[[2026-05-28-brief-architecture-overview-rename-developer]]`. ~15 min based on Researcher's pacing on Research/ renames.

   **Closed (same day):** Developer landed cleanly. 3 renames + 8 wikilink updates (5 files touched), context-sensitive resolution applied. The cross-area link at `Code Review/2026-05-22-stale-component-inventory.md` L34 was the interesting call — source file lives outside any Component dir so nearest-folder wouldn't apply, Developer disambiguated via parenthetical context (KBMag intent) and used the explicit `[[kbmag-overview]]`. Verification: `grep -rn '_overview' Architecture/ --include='*.md'` → 0 matches. K3 verdict MERGE sent. Out-of-scope flag from Developer: `Agents/maumayma/Researcher/log.md` L288 has a stale `[[_overview]]` reference pointing at Research/Group theory/Open problems/_overview.md (renamed in F7.2). Path-qualified per Rule 2 so Developer didn't touch — but worth Researcher's attention in next cycle.

**Two small caveats noted, non-blocking:**

- `grobner.md` has `methodology_type: empirical` — Kreuzer-Myasnikov-Rosenberger 2025 is a theoretical paper proposing algorithms, not an empirical study. Should be `theoretical` or `tutorial`. Surface to Researcher if it becomes a Bases-query-relevance issue; otherwise let it drift to the next `/research --reconnect`.
- The F6.2 caveats (notation-conventions section in paper-summary template + basics/ tag pass) — those were folded into the MOC pass per Researcher's earlier resolution. Lead hasn't visibly re-verified the basics/ topic-tag drop landed, but Researcher's report claimed Caveat 2 was done. Trust + spot-check next session.

**Phase 5/6/7 + Papers.base saga: vault restructure is largely complete.** Next likely work: experiment program (Experimenter / Experimenter-B25) or new research direction from Maria.

No commit (vault not under git per the standing convention).

---

## 2026-05-28 — Phase 6 complete (F6.1 + F6.2 + F6.3 + F6.2.5) + MOC pass routed

**F6.1 (Researcher):** Dir restructure as briefed — added `_overview.md` at `Research/Group theory/`, restructured `General/` (basics/, presentations-and-relations/, orders-and-finiteness/, synthesis stub), new `Word Problem/` (3 notes + techniques/), new `Tools/` (GAP/ + KBMAG/). `Include.md` deleted. `Burnside groups/B25/` and `Open problems/` untouched.

**F6.2 (Researcher, the bulk):** ~20 new content notes —
- `basics/` × 6 (group, subgroup, homomorphism, normal-subgroup, quotient-group, group-action) citing D&F 3rd ed.
- `presentations-and-relations/` × 5 (free-groups, presentations, tietze-transformations, coset-enumeration, cayley-graphs) — Lyndon-Schupp + D&F
- `orders-and-finiteness/` × 2 (order-exponent, classification-fsg)
- `Word Problem/decidability-landscape` (full Novikov-Boone + decidable cases) + `target-words` (general methodology, no Mixer framing) + `techniques/` × 3 (KB full, Dehn brief, automatic brief)
- `Tools/GAP/examples/` × 5 (group-order, coset-enumeration, word-equality, exponent-subgroups, kbmag-package) — all verified on GAP 4.15.1
- `Tools/KBMAG/examples/` × 2 (S3 shortlex, B(2,3) shortlex) — all verified on kbmag_v1 standalone kbprog
- `Tools/GAP/package-kbmag.md` (verified S3 output: Confluent true, Size 6, 7 rules)
- `Tools/KBMAG/file-formats.md` (`.kbprog` format documented)

**F6.3 (Researcher):** `General/_synthesis-existing-papers.md` at `#status/validated` covering 15 papers — settled results, open/contested, cross-cutting themes, empirical open questions for Experimenter, refresh-trigger notes in frontmatter.

**F6.2.5 (Researcher, parallel cleanup):** 3 commutator-notation fixes (`havas-wall-wamsley-1974`, `kourovka-11.48-kostrikin-1990`, `target-words`). Notation convention appended to `_templates/paper-summary.md` § Notation conventions — covers LaTeX/backtick/escape options + the `[[x,y],z]` edge case (Obsidian sees the `[[x,y]` prefix and creates phantom links even from single-bracket commutators). Vault-wide applicability noted in the convention. Visual orphan-graph verification owed to Maria's Obsidian session.

**3 sourceless drafts (Maria's option-A decision):** `quality_notes:` updated on `burau4-faithfulness`, `andrews-curtis-conjecture`, `kaplansky-zero-divisors` with the 2026-05-28 re-fetch line.

**K3 spot-check verdict: MERGE.** GAP/KBMAG examples produce real verifiable outputs (KBMAG S3 example: 8 rules, `b*a → a*B` is the canonical non-abelian S3 rule, `aba` reduces to `B`, normal forms count to 6 = |S3|). No Mixer framing leaked into standing content. D&F citations consistent throughout basics/. Commutator-notation doctrine is more thorough than the brief asked (in the good way).

**Four small caveats (none blocking, folded into next /research --reconnect):**
1. `01-group-order.md` Method 1 "Output (verbatim)" includes `Print(G)`-style lines not shown in the gap> session above — values correct, formatting block slightly elided.
2. `basics/group.md` carries `topic/finitely-presented-groups` — fails substance test (the note is about groups in general, no presentation discussion). Same probably applies across other `basics/` notes; one focused tag-pass would fix.
3. `#concept` content-type on `basics/group.md` vs. `tags.md` doctrine that scopes `#concept` to `Concepts/` hubs only. Doctrinal ambiguity from F6.2 brief instructing concept-note template usage in `basics/`. Researcher to recommend (a) relax doctrine to allow `#concept` outside `Concepts/`, (b) move basics → `Concepts/`, or (c) drop `#concept` from basics. Lead writes the adjustment.
4. Notation conventions section in `_templates/paper-summary.md` is vault-wide applicable but lives in a paper-template file. Eventual relocation candidate (`_meta/tags.md` § conventions or `_meta/notation-conventions.md`). Not urgent.

**MOC creation pass routed.** Queued brief at `[[2026-05-28-queued-brief-mocs-researcher]]` — covers 4 topics (burnside, word-problem, knuth-bendix, presentations-and-orders) using LYT pattern. Location question (collapse into F6.1's `_overview.md` notes vs. live as siblings in `Research/Group theory/_MOCs/`) deferred to Researcher's call now that dir structure is visible.

No commit (vault not under git per the standing convention).

---

## 2026-05-28 — Phase 4 v2 complete (F4.3 + F4.4) + Papers.base "By topic" fix (Developer, K3-merged)

**F4.3 (Researcher, ~110 min real time across 4 batches):** 15 papers + 1 synthesis (`_overview.md`) migrated to new paper-summary template. All 16 notes connected (zero orphans). Substance test applied throughout — havas-robertson.md dropped `#project/b25` after Lead confirmation; havas-newman-1980 dropped `#project/burnside-other`; grobner.md dropped `#domain/grobner` + `#project/grobner` and moved 3 inline `#concept/*` tags to `key_concepts:` frontmatter pointing at new `Concepts/` stubs. 5 deprecated tag categories cleared per F4.2 verdict (`#project/none`×5 files, `#score/*`×6 files migrated to `relevance:` frontmatter, `#project/burnside-other`×1, `#domain/grobner`+`#project/grobner`×1, `#concept` on paper notes×2). `#paper` content-type added to 3 previously-invisible papers. 6 new topic tags introduced — 4 substance-passed the 2+ paper rule, 2 single-paper seeds justified (`grobner-basis` carries the specificity the dropped domain no longer provides, `group-rings` is primary topic of the kaplansky note). Full per-paper before/after table in `Agents/maumayma/Researcher/log.md`.

**F4.4 (Researcher):** 5 existing `Concepts/` hubs updated with `appears_in:` + 6-axis tags (verification-methods-for-group-equality, kb-mixing-stagnation, mixable-api, burau4-faithfulness, kaplansky-zero-divisors). 3 new concept stubs created from grobner.md extractions (grobner-quotient-filter, grobner-infinitude-probe, representation-variety). 5 papers updated with `key_concepts:` frontmatter. `verification-methods-for-group-equality` confirmed 2+ paper rule (3 papers reference it).

**Re-fetch gap (3 sourceless papers — burau4-faithfulness, andrews-curtis, kaplansky):** Researcher didn't attempt defuddle on these. Defensible — pre-web canonical sources (1936/1956/1965) where finding clean URLs is high-cost low-value. All 3 are now `#status/draft` with `quality_notes:` explaining the citation gap. Surfaced to Maria for her call (accept as drafts / provide URLs / defer).

**Papers.base "By topic" fix (Developer):** routed in parallel with F4.4 once F4.3 landed and real topic data was in place. Developer chose option (ii) — formula `topic_tags: file.tags.filter(value.startsWith("topic/")).map(value.replace("topic/", ""))` with `groupBy.property: formula.topic_tags`. No frontmatter migration; tags remain single source of truth. K3 reviewed clean — surgical (2 added + 1 modified lines), boring code, no userspace break. Initial verdict MERGE sent based on Developer's pre-verification plan.

**Visual verification + REVISED finding (Developer, same day):** Developer ran the verification + a 3-config A/B test, contradicting our shared expectation honestly. **Bases multi-value groupBy (native `file.tags` OR formula-returning-list) does NOT fan out into one-row-per-element in this Obsidian build** — each paper appears as ONE row with its tag-list as a composite group key. Our original "noise" misread: it wasn't multiple rows per paper, it was ONE group header showing chips for ALL tag namespaces. The fix correctly scopes the chips to `#topic/*` only — real improvement, smaller than expected. Option (i) dedicated `topics: []` frontmatter would have hit the same limitation, so no Researcher migration is worth requesting. Bonus findings captured in `project-obsidian-bases-quirks` memory: (a) `file.tags` returns tags WITH `#` prefix — original placeholder `value.startsWith("topic/")` would have matched nothing; corrected to `"#topic/"`. (b) Bases saver strips YAML comments — Phase 5's in-file comment was lost; documentation now lives in sibling `Architecture/Mixer/Bases/_README.md`. (c) `.map(value.replace(...))` was redundant — Bases chip rendering strips the namespace visually anyway.

**Revised K3 verdict:** MERGE stands. The fix delivers the best achievable given the Bases constraint. Developer's honesty (contradicting their own and Lead's prior assumption) is exactly the doctrine pattern wanted. UX-shape decision (accept current cleaner state / re-route to "one view per top-level topic" / drop the view) surfaced to Maria — pending her call. Developer's rationale at `Agents/maumayma/Developer/scratch/papersbase-by-topic-fix-2026-05-28.md`; verification at `Agents/maumayma/Developer/test-output/papersbase-by-topic-2026-05-28.png`.

**Phase 4 v2 fully complete.** Phase 6 (F6.1 → F6.2 → F6.3) starting now per Researcher's sequencing. Post-F4 MOC creation brief queued at `[[2026-05-28-queued-brief-mocs-researcher]]` to route after F6.1 lands so the `_overview.md`-vs-MOC location-overlap question can be resolved with real dir structure visible.

No commit (vault not under git per the standing convention).

---

## 2026-05-28 — Phase 4 v2 — F4.2 taxonomy decisions written to [[tags]]

Task from Maria: based on Researcher's F4.1 inventory ([[2026-05-28-inventory]]), decide and encode the 6 open taxonomy questions in `_meta/tags.md`, then unblock Researcher for F4.3 paper migration.

**Maria's calls (A/A/A on the three research-direction questions):**

- Q2 (`#project/burnside-other`): drop, use `#topic/burnside` + specifics.
- Q3 (`#domain/grobner`): migrate paper to `#domain/cs` + `#topic/grobner-basis`. Defer the SAT/biology/grobner domain-registration question until those have active deliverables.
- Q4 (multi-project): allow with soft cap of 2; substance test enforced; encourage minimization.

**Lead's calls (mechanical):**

- Q1 (`#score/*`): migrated to optional `relevance: 1|2|3` frontmatter. Justification → `quality_notes:` body. Hashtags dropped.
- Q5 (inline `#concept/*` on papers): forbidden. Concept content lives in `Concepts/<name>.md` hubs, linked via `key_concepts:` frontmatter.
- Q6 (multiple content-type): one primary per note. Documented exception: `#paper + #synthesis` allowed for self-contained surveys.

**Edits to `_meta/tags.md`:**

1. § Axis 6 — added three doctrine clauses: "Not a survey bucket", "Don't pre-register future workstreams", "Multi-project tagging — allowed with soft cap of 2".
2. § Content type — added "One primary content-type per note" + "Inline `#concept/*` namespacing on non-concept notes is forbidden" paragraphs.
3. **New subsection** § Paper-evaluation frontmatter — documents optional `relevance: 1|2|3` field, semantics, source of scoring rubric (`Open problems/_overview.md`).
4. **New subsection** § Deprecated / dropped tags — registry of `#score/*`, `#project/none`, `#project/burnside-other`, `#domain/grobner`, `#project/grobner` with migration paths and dropped-on dates.

**Implication of Q4-A + "don't pre-register" for `grobner.md`:** the multi-project allowance does NOT mean keep `#project/grobner` on the paper. Per the new rule, Gröbner has no active workstream — `#project/grobner` is dropped along with `#domain/grobner`. The paper migrates to `#domain/cs` + `#topic/grobner-basis` + (optionally) `#project/b25` if substance test passes for genuine B(2,5) contribution. The multi-project doctrine is forward-looking for cases that arise after F4.3.

**Sent to Researcher** via `maestri ask` (`TYPE: VERDICT`): F4.3 unblocked. Inventory note remains the migration checklist; per-paper log entries go to `Agents/maumayma/Researcher/log.md` with before-tags → after-tags.

**Parked for after F4.3:** Papers.base "By topic" view noise (groupBy on `file.tags` includes all tag namespaces). Route Developer fix once real `#topic/*` data populates so we can choose between (i) dedicated `topics: []` frontmatter property vs (ii) Bases formula scoping groupBy to `topic/*` prefix.

No commit (vault is not under git per the standing convention).

---

## 2026-05-28 — Phase 5: vault-restructure reference propagation

Task from Maria: fix stale "7-axis taxonomy" / mandatory-project doctrine references after the 6-axis (project-optional, topic-multi-tag) taxonomy landed in [[tags]]. Two categories.

**Category A — doctrine prompts and meta files (6 surgical edits across 6 files):**

- `_meta/agents/_common.md` line 90 — "full 7-axis taxonomy. Tag minimum per note: one `#agent/*` + one `#user/*` + one `#domain/*` + one `#project/*` + one `#status/*`" → 6-axis: agent + user + domain + topic (1-many, substantive) + status, project optional.
- `_meta/agents/_common.md` line 101 (Obsidian write rules) — "Tags mandatory per [[tags]] (7-axis minimum)" → "6-axis minimum: agent + user + domain + topic + status; project optional."
- `_meta/agents/lead.md` line 102 (Phase 4 code-review tag template) — "(7-axis minimum): `#agent/lead #user/<...> #domain/<...> #project/<...> #status/<...> #review`" → 6-axis with `#topic/<one+>` substituted in and `#project/<project>` flagged as add-when-project-scoped.
- `_meta/agents/experimenter.md` line 88 (Phase 1 pre-register tag template) — "(7-axis)" → "(6-axis)" + `#topic/<one+>` added + project kept-but-explained as required for experiments specifically.
- `_meta/canvas-setup.md` line 78 (sticky-note context) — "(7-axis taxonomy)" → "(6-axis taxonomy)".
- `People/maumayma.md` line 25 (key contributions list) — "the 7-axis taxonomy" → "the 6-axis taxonomy".

**Category A verification of `_meta/agents/experimenter-b25.md` and `_meta/agents/validator.md`:** neither contained explicit "7-axis" wording, but both had tag examples missing the new `#topic/*` axis. Fixed:

- `_meta/agents/experimenter-b25.md` line 85 (B(2,5) pre-register tag template) — added `#topic/burnside #topic/b25 #topic/<more+>` and rephrased to "(6-axis)" with rationale that B(2,5) experiments always carry the two flagship topic tags and `#project/b25` is required (experiments are intrinsically project-scoped).
- `_meta/agents/validator.md` line 122 (verification-note frontmatter example) — added `topic/<one+>` to the example tags array, kept `project/<...>` (verification notes are typically tied to project-scoped claims).

**Category B — `Architecture/Mixer/Bases/Papers.base`:**

- Added properties: `language` (displayName "Lang"), `methodology_type` (displayName "Type"), `citation_count` (displayName "Cites"). Renamed `project` displayName to "Project (optional)" to surface the optionality. These match the new Phase 4 paper-summary frontmatter schema in `_templates/paper-summary.md`.
- New view **"By topic"** with `groupBy.property: file.tags`. ⚠️ Bases syntax for grouping on individual tag values (specifically only `topic/*` subtags) is unverified — see "Flagged anomaly" below.
- New view **"By language"** with `groupBy.property: language`.
- New view **"Non-English papers (translation review)"** filtered `language != "en"` — useful surface for Phase 4 translation review.
- Updated view **"By project"** to **"By project (project-scoped papers only)"** with filter `project` (truthy check — falsy/null project values excluded). Bases truthy-filter syntax inferred from existing `if(dev_sharpe && ..., ...)` formula in `BOTBOTBOT/Strategies/Future strategies/Experiments.base`; may need to be `project != null` or `project != ""` depending on Bases version.
- Preserved views: "All papers — latest first", "By domain", "Unread (status: draft)", "Synthesized (status: validated)". Added `language` column to each for cross-cutting visibility.

**Flagged anomalies / unverified syntax:**
- `groupBy.property: file.tags` in the "By topic" view: I can't confirm Bases produces one group per tag-list-entry, nor that I can scope the groupBy to only `topic/*` tags. If the view renders empty or noisy (one group per every tag including agent/user/domain), route to Developer to find the correct syntax or to add a `topic_tags` formula filtering only `topic/*` subtags.
- The `project` truthy filter likewise needs visual verification in Obsidian; trivial to swap to `project != null` if Bases prefers explicit null comparison.

**Out of scope (per Phase 5 instructions, NOT touched):**
- `Agents/maumayma/Lead/scratch/`, `Agents/maumayma/Researcher/log.md` — historical record.
- README.md "renamed from Mixer Applications" breadcrumb — intentional.
- Paper notes in `Research/` — Phase 4 (Researcher) scope.

No commit (vault is not under git per the standing convention).
