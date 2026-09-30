---
tags: [meta]
---

# Math vault — Multi-domain research wiki

A shared knowledge base for a computational-mathematics research circle and adjacent research areas. Multi-user and multi-domain — currently centred on group theory (especially B(2,5)), with AI, CS, and methodology papers added by contributors. The `/research` skill ingests papers across any field; the Maestri-canvas agent team handles implementation, experiments, and math validation for whatever projects are active. The agents are tool- and architecture-neutral: each project's repos, tools and commands live in its profile (`_meta/projects/`), and external code and tools in the dependency registry (`_meta/dependencies/`).

## Start here

- [[mission]] — what we're building, research program and active projects, terminology, engineering invariants
- [[projects-and-dependencies-convention]] — project profiles, dependency registry, provenance, tool neutrality
- [[tags]] — 6-axis tag taxonomy (multi-domain, multi-user, multi-topic, optional project)
- [[canvas-setup]] — how to assemble the Maestri canvas (7 persistent agents + on-demand)
- [[experiment-folder-convention]] — how experiments are organized on disk
- [[ocr-tooling|OCR tooling stub]] — `nuextract-cli` for image-only PDFs (not yet implemented)
- `_meta/skills/research/INSTALL.md` — install the `/research` Claude Code skill for paper ingestion

## Two ways to use this vault

- **`/research` slash command in any Claude Code session.** Ingest one or many papers into the vault. Field-agnostic. No project ties by default. Powers the multi-user paper graph. See `_meta/skills/research/SKILL.md` + `_meta/skills/research/INSTALL.md`.
- **Maestri canvas with 7 persistent agents.** For project work: implementation, experiments, math validation, code review, commit ritual. See [[canvas-setup]].

## Agent roster (7 roles, Maestri canvas)

Vault folders marked *(per profile)* come from the active project profile's `vault_docs`.

| Role | Prompt | Owns in vault |
|---|---|---|
| [[lead]] | `_meta/agents/lead.md` | `Agents/<user>/Lead/`, code reviews / overviews / ADRs *(per profile)*, `_meta/projects/`, `_meta/dependencies/` |
| [[researcher]] | `_meta/agents/researcher.md` | `Agents/<user>/Researcher/`, `Research/`, `Concepts/` + **restructure authority** over both. Also powers the `/research` skill (universal, field-agnostic). |
| [[developer]] | `_meta/agents/developer.md` | `Agents/<user>/Developer/`, component docs *(per profile)* |
| [[experimenter]] | `_meta/agents/experimenter.md` | `Agents/<user>/Experimenter/`, `Experiments/**` (except B25) |
| [[experimenter-b25]] | `_meta/agents/experimenter-b25.md` | `Agents/<user>/Experimenter-B25/`, `Experiments/Group Theory/Burnside Group/B25/**` (exclusive) |
| [[validator]] | `_meta/agents/validator.md` | `Agents/<user>/Validator/`, math-validation notes *(per profile)*; **math verdicts override all peers** |
| [[math-expert]] | `_meta/agents/math-expert.md` | `Agents/<user>/MathExpert/`; proposes ideas, never certifies |
| Shared | `_meta/agents/_common.md` | Read by all |

## Vault structure

```
Math/
├── README.md
├── _meta/
│   ├── mission.md
│   ├── tags.md
│   ├── canvas-setup.md
│   ├── experiment-folder-convention.md
│   ├── agents/  (_common, lead, researcher, developer, experimenter, experimenter-b25, validator)
│   └── skills/
│       └── research/  (SKILL.md, INSTALL.md, workflows/*)  ← /research Claude Code skill
├── _templates/  (paper-summary, concept-note, synthesis, code-review, experiment, component-doc, decision, personal-note)
├── Agents/
│   ├── agents/  projects/  dependencies/  skills/  scripts/
├── Agents/
│   ├── maumayma/    ← per-user subtree; each contributor gets their own
│   │   ├── Lead/           (+ scratch/, test-output/, log.md, README.md)
│   │   ├── Researcher/     (+ scratch/, log.md, README.md)
│   │   ├── Developer/      (+ scratch/, test-output/, log.md, README.md)
│   │   ├── Experimenter/   (+ scratch/, output/, log.md, README.md)
│   │   ├── Experimenter-B25/ (+ scratch/, output/, log.md, README.md)
│   │   ├── Validator/      (+ scratch/, log.md, README.md)
│   │   └── MathExpert/
│   └── <colleague-handle>/  ← added when a colleague starts using Maestri canvas
├── Architecture/            ← code docs, one subtree per project/codebase (vault_docs in each profile)
│   └── Mixer/               ← docs for the algo-mixer codebase (project-mixer-core, project-b25)
│       ├── Components/      ← Developer (KBMag, Mixer Core subtrees)
│       ├── Bases/           ← .base dashboards (Components, Experiments, Concepts, Papers)
│       └── Documentation/
│           ├── Code Review/        ← Lead
│           ├── Overview/           ← Lead
│           ├── Requirements/       ← Lead (ocr-tooling stub here)
│           └── Math Validation/    ← Validator
├── Concepts/                ← Researcher (reusable concept hubs, cross-paper anchors)
├── Notes/<handle>/          ← human-owned living notes: ideas/, logs/, extracted/ (see _meta/notes-folder-convention.md)
├── Research/                ← Researcher (with restructure authority)
│   ├── Group theory/
│   ├── Algorithm Cooperation/   ← (renamed from "Mixer Applications" — broader scope)
│   ├── AI in Math/
│   └── (more as needed; new domains registered in _meta/tags.md first)
├── Experiments/             ← Experimenter (+ Experimenter-B25 in B25 subtree)
│   └── Group Theory/
│       ├── Burnside Group/
│       │   ├── B25/         ← Experimenter-B25 exclusive
│       │   ├── B26/, B43/, B53/
│       ├── Grobner/
│       └── Mathieu Group/
└── People/                  ← Human contributors index (README + per-handle notes)
```

## How to use this vault

- **Browse** by directory or follow wikilinks from [[mission]].
- **Open a Base dashboard** (currently at `Architecture/Mixer/Bases/`) for filtered views:
  - `Components.base` — all components, by domain / hot / status
  - `Experiments.base` — all experiments, by project / status / instance, Validator verdicts
  - `Concepts.base` — cross-domain methodology by domain / author / status
  - `Papers.base` — **moved to `Research/Papers.base`** — literature by domain / project / language / read status, plus a topics-per-paper view
- **Search by tag** — every note has minimum `#agent/* #user/* #domain/* #topic/* #status/*` (project optional). See [[tags]] for the 6-axis taxonomy and topic-tagging discipline (substance test, no upper bound on count).
- **Templates** in `_templates/` — K3 pattern (frontmatter = agent layer, body = human layer).
- **Edit anything** — agents respect dir ownership rules.

## Multi-user norms

- Every note carries `author: <handle>` frontmatter + `#user/<handle>` tag (the human who owns it).
- New human contributors get a `People/<handle>.md` note. See [[People/README]].
- When you cite a colleague, link `[[People/<handle>]]` so credit flows.

## Validator's authority

Math correctness verdicts (`#status/proven`, `#status/replicated`, `#status/conjectured`, `#status/disproven`) come from [[validator|Validator]]. Lead can't override on math; only the human can. A `#status/disproven` finding halts dependent work until reformulated.

## Terminology reminder

- **AI agent** = LLM on this canvas (seven roles above).
- **Component / algorithm process** = a program under test. Projects may define their own term in their profile (e.g. "mixer Agent" in the Mixer project).

Don't conflate them.
