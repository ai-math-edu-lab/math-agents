# Workflow — Personal Notes Pass (`/research --notes`)

Use when the invoker wants their own living notes in `Notes/<invoker>/ideas/` and `Notes/<invoker>/logs/` tagged, cross-linked to the vault, and mined for ideas / open questions. Convention: [[notes-folder-convention]].

```
/research --notes            # same as --notes all
/research --notes all        # every changed note under Notes/<invoker>/{ideas,logs}/
/research --notes <path>     # one note (vault-relative path)
```

## Hard rules

- **Only `Notes/<invoker>/`.** Never touch another user's `Notes/<other>/`.
- **Never rewrite the body** of an `ideas/` or `logs/` note. Allowed edits: frontmatter tags, and the text between `<!-- agent:related -->` and `<!-- /agent:related -->`. If the markers are missing, append a `## Related material` section with empty markers at the end of the note — nothing else.
- **Never commit.** Report and wait for the invoker's approval.

## Steps

1. **Find changed notes.**
   - State file: `Agents/<invoker>/Researcher/notes-index.json` (local, gitignored) mapping vault-relative path → `{sha256, last_pass}`.
   - With `all`: hash every `.md` in `Notes/<invoker>/ideas/` and `logs/`; process only notes whose hash differs or which are missing from the index. With `<path>`: process that note unconditionally.
   - List the notes to the invoker before editing. If more than ~10, checkpoint every 5.

2. **Tag.** For each note, check frontmatter against the minimum in [[notes-folder-convention]] (`author`, `#agent/human`, `#user/<invoker>`, `#domain/*`, `#topic/*`, `#status/*`). Add missing tags; reuse registered `#topic/*` values from `_meta/tags.md` before registering new ones (substance test applies). Never remove `author:` or `#user/*`. If `#domain/*` is ambiguous, ask.

3. **Cross-link.** Grep the vault for the note's key terms (concepts, groups, algorithms, paper authors, experiment names). Rewrite the `agent:related` block with a short bullet list of wikilinks, each with a one-line reason:
   - relevant `Research/` paper notes and `_synthesis-*` notes,
   - `Concepts/` hubs,
   - the relevant MOC (`Research/<Domain>/_MOCs/_moc-<topic>.md`),
   - `Experiments/` notes the log refers to,
   - the note's own `extracted/` children.
   Where a note is strongly relevant to a `Concepts/` hub, add the note to that hub's `## Where it appears` (Researcher owns `Concepts/`). Reuse the matching approach in [[connection-pass]].

4. **Extract.** Read the note and pull out each distinct **idea** (proposal, conjecture, approach worth trying) and **open question**. For each one:
   - Look in `Notes/<invoker>/extracted/` for an existing extraction (grep `source:` frontmatter + title). **Update it** if found; create a new one only if none matches.
   - File: `Notes/<invoker>/extracted/<kebab-slug>.md`. Frontmatter:
     ```yaml
     title: <one-line statement>
     author: <invoker>
     language: en
     kind: idea            # idea | question
     source: "[[<source-note>]]"
     source_entry: YYYY-MM-DD   # entry heading date, if from a log
     tags: [agent/research, user/<invoker>, domain/<...>, topic/<...>, status/draft]   # + question for open questions
     ```
   - Body: the idea/question stated in 1-3 sentences (paraphrase faithfully; quote the author where precision matters), *Context* (why it came up), *Next step* if the author stated one. Do not invent assessments.
   - End with `## Related material` — ≥3 wikilinks: the source note, plus Research/Concepts/Experiments/MOC notes.
   - If an idea was dropped by the author (struck through, marked abandoned), set its extraction to `status/superseded`; don't delete.

5. **Update index + log.** Write the new hashes to `notes-index.json`. Append one entry per processed note to `Agents/<invoker>/Researcher/log.md`: tags before → after, links added, extractions created/updated.

6. **Report and wait.** Tell the invoker:
   - notes processed, tags changed, links added,
   - extractions created / updated (paths),
   - any new `#topic/*` registered,
   - ideas that look ready to graduate into `Research/` (see [[notes-folder-convention]]),
   - `git status` of changed files — then **ask** whether to commit. Commit only on explicit approval.

## Stop conditions

- Note has no `author:` or belongs to another handle → skip, flag.
- Body is non-English → don't translate the author's body; tag `language:` and write extractions in English with `[trans.]` on quotes.
- Note contains credentials, tokens, or private personal data → stop, flag to invoker before any commit.
