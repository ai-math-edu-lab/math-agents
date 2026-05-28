---
author: maumayma
recipient: researcher
sent: 2026-05-22
tags:
  - agent/lead
  - user/maumayma
  - domain/group-theory
  - project/b25
  - project/grobner
  - status/draft
  - delegation
---

# Brief — Researcher Part 1 — Parse `docs/papers/` and populate `Research/`

Sent to **Researcher** on 2026-05-22. Tracked from [[backfill-2026-05-22]]. Sequential — Part 2 follows once Part 1 reports back.

## Message (verbatim)

> TYPE: REQUEST
> TOPIC: Parse `docs/papers/` and populate `Research/` with K3 paper summaries
> CONTEXT: [[_common]] § K3 pattern, [[paper-summary]] template, [[tags]] 7-axis taxonomy. The repo at `/Users/maumayma/Desktop/reps/algo_mixing/docs/papers/` has six papers actively used by the project. None are summarized in the vault yet.
>
> ASK: For each paper, read it with defuddle (PDFs that are text-extractable) or by reading the file directly if defuddle fails. Write one paper summary note per paper, using the [[paper-summary]] template in K3 pattern (frontmatter = agent layer, body = human narrative).
>
> File placement:
>
> - `Research/Group theory/Burnside groups/B25/havas-robertson.md` — Havas-Robertson (the commutator paper that defines B(2,5) target words). **This is the highest-priority summary.**
> - `Research/Group theory/Burnside groups/havas-wall-wamsley-1974.md` — `1974hww.pdf`
> - `Research/Group theory/Burnside groups/havas-newman-1980.md` — `1980hn.pdf`
> - `Research/Group theory/General/kourovka-2022.md` — Kourovka 2022 (open problems index; many groups, not just Burnside)
> - `Research/Group theory/General/problems-people.md` — `Problems-people.docx` (read with defuddle if it handles docx; otherwise note as "requires manual OCR/extraction" in `known_issues` and flag to me)
> - `Research/Mixer Applications/grobner.md` — Gröbner paper. Tag `#project/grobner` because it's a cross-domain Mixer candidate.
>
> Per-note required content:
>
> - Frontmatter with: `title` (paper title verbatim), `authors` (list), `year`, `domain`, `project` (`b25` for Havas-Robertson if it's specifically about B(2,5) commutators, otherwise `burnside-other` or none; `grobner` for the Gröbner paper; etc.), `status: validated` only after you've defended the synthesis to me, `validated`, `author: maumayma`, `source_path: docs/papers/<file>`, `tags`.
> - Body sections (narrative, human-readable):
>   - **What this paper claims** — 1–2 paragraphs. The main result(s) in plain English, no jargon dump.
>   - **Why we care** — explicit connection to our work. If it's Havas-Robertson, list the target words / commutator structures it defines and which `experiments/b25_reduce_core/` artifacts use them. If it's Kourovka, list which open problems are relevant to our research (B(2,5) being the obvious one). If it's the Gröbner paper, explain whether the algorithm has Mixer-shaped subproblems and tag candidate aspects with `#concept` references.
>   - **Key formulas / definitions** — the math objects defined or used. Where applicable, give the exact LaTeX or symbolic representation; don't paraphrase math into ambiguous prose.
>   - **Methods used** — what techniques the paper uses (KB, computer algebra, structural induction, etc.).
>   - **Findings we should remember** — the load-bearing numerical or structural facts. Sharpe-style: cite exact numbers.
>   - **Caveats / limitations** — what the paper does not claim, where it might be wrong, what's known to be superseded since.
>   - **Cross-references** — wikilinks to other paper notes that this one discusses; wikilinks to experiments that use this paper.
> - Multi-axis tags mandatory: `#agent/research #user/maumayma #domain/<area> #project/<...> #status/<...> #paper`.
>
> Special handling per paper:
>
> - **Havas-Robertson is the critical one.** Pay attention to: which commutators are listed as targets, how target words are constructed, what "corrected" words look like (re: `experiments/b25_reduce_core/corrected/`), and any reduction strategies the paper proposes. Cite specific target words with their commutator names (the b25 work uses `comm_12_9`, `comm_13_10`, etc. — try to identify these in the paper).
> - **Kourovka 2022** is huge (it's an open-problems index). Don't summarize the whole thing. Focus on B(2,5)-relevant entries, Gröbner-relevant entries, and any other Mixer-shaped problems. State the scope of your summary explicitly: "Sections covered: <list>; sections skipped: <list because not directly relevant>."
> - **Problems-people.docx** — the Word doc. Try `defuddle docs/papers/Problems-people.docx`. If defuddle can't handle .docx, fall back to whatever you can: `Read` directly may work if Word saved with embedded text. If you can't extract content, write a stub note with `status: draft` and `known_issues: ['extraction failed: <reason>, requires manual transcription']` and flag it to Lead for a human to handle. Do not invent content.
> - **1974hww.pdf and 1980hn.pdf** — older papers; may be image-only scans. If defuddle returns garbage / no text, mark `known_issues: ['image-only PDF, requires nuextract-cli (not yet installed)']` and write a stub with just title + authors + year, `status: draft`. Don't make up content from the filename.
>
> Report back with: wikilinks to each summary, and an explicit list of any that hit extraction failures (so I can route them to Lead for human intervention).
>
> NO restructuring of `Research/` during this task (your restructure authority is for later). Just write the new notes in the paths above.
> NO code changes. Vault writes only.
>
> DEADLINE: none.
