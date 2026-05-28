---
author: maumayma
recipient: researcher
sent: 2026-05-22
tags:
  - agent/lead
  - user/maumayma
  - domain/methodology
  - project/b25
  - project/mixer-core
  - status/draft
  - delegation
---

# Brief — Researcher Part 2 — Synthesize slide deck content into wiki

Sent to **Researcher** on 2026-05-22 (released after Part 1 + corrections settled). Tracked from [[backfill-2026-05-22]].

## Message (verbatim, with parallel-task note added)

> TYPE: REQUEST
> TOPIC: Synthesize slide deck content into wiki (Part 2 — cleared to proceed)
> CONTEXT: `docs/slides/algo-mixing-burnside.md` is the markdown source of an internal slide deck about the Mixer approach to Burnside problems. The HTML and PDF versions are derived; ignore them. `docs/slides/flamegraph.svg` is a performance profile artifact — note its existence but don't analyze the SVG content (that's Validator/Developer territory for performance work).
>
> Part 1 is fully landed: paper notes restructured under `Research/Group theory/Burnside groups/B25/`, Kourovka 11.48 written, Burau₄ + Kaplansky as Concepts/ notes. You're cleared to proceed with Part 2.
>
> ASK: Read the slide deck. Decide what's durable knowledge worth wiki preservation. Then write notes into the appropriate sub-locations.
>
> Likely outputs (your judgment based on actual content):
>
> - A summary of the slide deck itself at `Research/Mixer Applications/algo-mixing-burnside-slides.md`. Frontmatter: `source: docs/slides/algo-mixing-burnside.md`, `domain: methodology`, `project: b25` (if predominantly about B(2,5)) or `mixer-core` (if more general), `status: validated`, `author: maumayma`. Tags `#agent/research #user/maumayma #domain/methodology #project/<...> #status/validated #concept`. Body: narrative summary of the deck's argument and main claims, with section headings matching the deck where useful.
> - Cross-domain methodology concepts extracted into `Concepts/` if the deck makes claims about Mixer methodology that aren't B(2,5)-specific (cooperation patterns, scheduler design, transfer between algorithms). One concept note per distinct idea. Each tagged `#concept #domain/methodology`.
> - Experiment-history notes if the deck describes specific experiments that were run. Don't duplicate Experimenter-B25's work; just point at the deck's account and link to whichever experiment notes exist. If experiments mentioned in the deck don't have corresponding notes in `Experiments/Group Theory/Burnside Group/B25/`, list them in your hand-off message so Experimenter-B25 can backfill.
>
> Critical rules:
>
> - Don't paraphrase math. If the deck shows a formula or commutator, quote it exactly with the same notation.
> - Don't restate the entire deck. Your job is curation: what's durable knowledge worth wiki preservation, versus what's transient slide-deck-only content. Be explicit about what you chose to include and what you chose to skip.
> - Cross-link aggressively. Every claim in the deck that overlaps with a paper from Part 1 should link to that paper note. Every reference to an experiment should link to the experiment note (or flag missing experiments to the hand-off).
> - Reference the flamegraph existence: include a frontmatter `related_artifacts: [docs/slides/flamegraph.svg]` in the slide-summary note so future agents know there's a performance artifact alongside.
>
> Parallel-task note: backward cross-links from experiment notes to paper notes are being added concurrently by Experimenter-B25 (see their task brief). If your slide-deck note needs to wikilink to an experiment note that hasn't yet had its `## Literature` section added, that's fine — link forward only, and Experimenter-B25's backward-link pass will close the loop later. No file conflict (Researcher writes in `Research/Mixer Applications/` and `Concepts/`; Experimenter-B25 writes in `Experiments/.../B25/`).
>
> Report back with wikilinks to each note created and an explicit list of any experiments mentioned in the deck that don't yet have notes.
>
> NO code changes. Vault writes only.
>
> DEADLINE: none.
