---
tags: [meta]
---

# Math vault — Multi-domain research wiki

A shared knowledge base for the algorithmic-mixing research circle and adjacent research areas. Multi-user and multi-domain — currently centred on group theory (especially B(2,5)), with AI, CS, and methodology papers added by contributors. The `/research` skill ingests papers across any field; the Maestri-canvas agent team handles project-specific implementation, experiments, and math validation for the `algo_mixing` codebase.

## Start here

- [[mission]] — what we're building, three-layer research program, terminology, engineering invariants
- [[tags]] — 6-axis tag taxonomy (multi-domain, multi-user, multi-topic, optional project)
- [[canvas-setup]] — how to assemble the Maestri canvas (6 persistent agents + on-demand)
- [[experiment-folder-convention]] — how experiments are organized on disk
- [[ocr-tooling|OCR tooling stub]] — `nuextract-cli` for image-only PDFs (not yet implemented)
- `_meta/skills/research/INSTALL.md` — install the `/research` Claude Code skill for paper ingestion

## Two ways to use this vault

- **`/research` slash command in any Claude Code session.** Ingest one or many papers into the vault. Field-agnostic. No project ties by default. Powers the multi-user paper graph. See `_meta/skills/research/SKILL.md` + `_meta/skills/research/INSTALL.md`.
- **Maestri canvas with 6 persistent agents.** For the algo_mixing project: implementation, experiments, math validation, code review, commit ritual. See [[canvas-setup]].

## Agent roster (6 roles, Maestri canvas)

| Role | Prompt | Owns in vault |
|---|---|---|
| [[lead]] | `_meta/agents/lead.md` | `Agents/<user>/Lead/`, `Architecture/Mixer/Documentation/Code Review/`, Overview, ADRs |
| [[researcher]] | `_meta/agents/researcher.md` | `Agents/<user>/Researcher/`, `Research/`, `Concepts/` + **restructure authority** over both. Also powers the `/research` skill (universal, field-agnostic). |
| [[developer]] | `_meta/agents/developer.md` | `Agents/<user>/Developer/`, `Architecture/Mixer/Components/` |
| [[experimenter]] | `_meta/agents/experimenter.md` | `Agents/<user>/Experimenter/`, `Experiments/**` (except B25), `Architecture/Mixer/Pipelines/` |
| [[experimenter-b25]] | `_meta/agents/experimenter-b25.md` | `Agents/<user>/Experimenter-B25/`, `Experiments/Group Theory/Burnside Group/B25/**` (exclusive) |
| [[validator]] | `_meta/agents/validator.md` | `Agents/<user>/Validator/`, `Architecture/Mixer/Documentation/Math Validation/`; **math verdicts override all peers** |
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
│   ├── maumayma/    ← per-user subtree; each contributor gets their own
│   │   ├── Lead/           (+ scratch/, test-output/, log.md, README.md)
│   │   ├── Researcher/     (+ scratch/, log.md, README.md)
│   │   ├── Developer/      (+ scratch/, test-output/, log.md, README.md)
│   │   ├── Experimenter/   (+ scratch/, output/, log.md, README.md)
│   │   ├── Experimenter-B25/ (+ scratch/, output/, log.md, README.md)
│   │   └── Validator/      (+ scratch/, log.md, README.md)
│   └── <colleague-handle>/  ← added when a colleague starts using Maestri canvas
├── Architecture/
│   └── Mixer/
│       ├── Components/      ← Developer (KBMag, Rust Mixer subtrees)
│       ├── Pipelines/       ← Experimenter
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
- **Open a Base dashboard** at `Architecture/Mixer/Bases/` for filtered views:
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

- **mixer Agent** = algorithm subprocess (the `mixer_core.Agent` ABC).
- **AI agent** = LLM on this canvas (six roles above).

Don't conflate them.
