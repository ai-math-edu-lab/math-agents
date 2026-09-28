"""Doctrine loader.

The research-handle's *behavior* lives in the vault, not in this code:
- `_meta/agents/researcher.md`     — the agent prompt (source of truth)
- `_meta/agents/_common.md`        — shared multi-user conventions
- `_meta/tags.md`                  — 6-axis taxonomy (registered domains/topics)
- `_meta/naming-conventions.md`    — filename + placement rules
- `_meta/research-folder-convention.md`
- `_templates/paper-summary.md`    — exact output structure
- `_templates/concept-note.md`, `_templates/synthesis.md`
- `_meta/skills/research/SKILL.md` + `workflows/*.md` — the five modes

Loading these at session start is what guarantees ChatGPT produces the *same*
summaries as Claude. If the vault updates its doctrine, this server picks it up
automatically — no code change, mirroring the skill's symlink-propagation.
"""

from __future__ import annotations

from pathlib import Path

# (label, vault-relative path). Missing files are skipped gracefully so the
# server still runs against a vault that hasn't got the full skill installed.
DOCTRINE_FILES: list[tuple[str, str]] = [
    ("Researcher agent prompt", "_meta/agents/researcher.md"),
    ("Shared conventions (_common)", "_meta/agents/_common.md"),
    ("Tag taxonomy", "_meta/tags.md"),
    ("Naming conventions", "_meta/naming-conventions.md"),
    ("Research folder convention", "_meta/research-folder-convention.md"),
    ("Paper-summary template", "_templates/paper-summary.md"),
    ("Concept-note template", "_templates/concept-note.md"),
    ("Synthesis template", "_templates/synthesis.md"),
    ("Skill overview", "_meta/skills/research/SKILL.md"),
    ("Workflow: single paper", "_meta/skills/research/workflows/single-paper.md"),
    ("Workflow: batch", "_meta/skills/research/workflows/batch.md"),
    ("Workflow: literature scan", "_meta/skills/research/workflows/literature-scan.md"),
    ("Workflow: connection pass", "_meta/skills/research/workflows/connection-pass.md"),
    ("Workflow: personal notes", "_meta/skills/research/workflows/personal-notes.md"),
    ("Notes folder convention", "_meta/notes-folder-convention.md"),
]

_TAGS_CAP = 12_000  # tags.md is large; cap to keep the prompt lean


def load_doctrine(vault_root: Path) -> str:
    """Concatenate all available doctrine files into one briefing string."""
    parts: list[str] = [
        "# Research-handle doctrine (loaded from the vault)\n",
        "You are the **Researcher**. Operate under the doctrine below EXACTLY. "
        "It is identical to the Claude `/research` skill. Read it fully before "
        "ingesting any paper. Key non-negotiables: English-only vault with "
        "`[trans.]` for translations; no code; no experiments; no invented "
        "quality verdicts or relevance; unique kebab-case filenames; correct "
        "`Research/<Domain>/<Topic>/` placement; mandatory `domain:` and "
        "`status:` frontmatter *properties* (not just tags); connection-graph "
        "frontmatter with bidirectional links; substance-tested `#topic/*` "
        "tags.\n",
    ]
    missing: list[str] = []
    for label, rel in DOCTRINE_FILES:
        p = (vault_root / rel)
        if not p.is_file():
            missing.append(rel)
            continue
        text = p.read_text(encoding="utf-8")
        if rel.endswith("tags.md") and len(text) > _TAGS_CAP:
            text = text[:_TAGS_CAP] + "\n\n[... tags.md truncated; use search_vault to see all registered tags ...]"
        parts.append(f"\n\n{'=' * 72}\n## {label}  (`{rel}`)\n{'=' * 72}\n\n{text}")

    if missing:
        parts.append(
            "\n\n"
            + "=" * 72
            + "\n## NOTE: some doctrine files were not found in this vault\n"
            + "=" * 72
            + "\nMissing (skipped): "
            + ", ".join(missing)
            + "\nIf these are expected, confirm the vault path is the shared "
            "Math vault root that contains `_meta/` and `_templates/`."
        )
    return "".join(parts)
