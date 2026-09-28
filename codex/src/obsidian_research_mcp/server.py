"""obsidian-research-mcp — MCP server.

Gives any MCP client (ChatGPT desktop, Claude, etc.) the same "research handle"
as the Claude `/research` skill:

  * full vault CRUD (read/list/write/append/replace/frontmatter/tags/search),
    matching the cyanheads tool surface but over the filesystem (no Node, no
    Obsidian Local REST API plugin);
  * paper fetching (`fetch_paper`) and citation lookup (`lookup_citation`),
    the extras generic Obsidian servers lack;
  * a `load_doctrine` tool + `research` prompt that inject the vault's own
    Researcher doctrine, so behavior is identical to the Claude skill.

Config via env:
  OBSIDIAN_VAULT_PATH   (required) absolute path to the Math vault root
  OBSIDIAN_READ_ONLY    (optional) "1"/"true" to disable all write tools
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from .doctrine import load_doctrine as _load_doctrine
from .fetch import fetch_paper as _fetch_paper
from .fetch import lookup_citation as _lookup_citation
from .vault import Vault, VaultError

mcp = FastMCP("obsidian-research")


def _vault() -> Vault:
    root = os.environ.get("OBSIDIAN_VAULT_PATH")
    if not root:
        raise VaultError(
            "OBSIDIAN_VAULT_PATH is not set. Point it at the shared Math vault "
            "root (the folder that contains `_meta/` and `_templates/`)."
        )
    return Vault(Path(root))


def _read_only() -> bool:
    return os.environ.get("OBSIDIAN_READ_ONLY", "").lower() in {"1", "true", "yes"}


def _guard_write() -> None:
    if _read_only():
        raise VaultError("Server is in read-only mode (OBSIDIAN_READ_ONLY set).")


def _ok(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Reader tools
# ---------------------------------------------------------------------------

@mcp.tool()
def get_note(path: str) -> str:
    """Read a vault note. Returns its frontmatter and markdown body.

    `path` is vault-relative, e.g. "Research/Group theory/Burnside groups/B25/havas-1980.md".
    """
    note = _vault().read(path)
    return _ok({"path": note.rel_path, "frontmatter": note.frontmatter, "body": note.body})


@mcp.tool()
def list_notes(subdir: str = "") -> str:
    """List all `.md` note paths in the vault, or within `subdir` if given."""
    return _ok(_vault().list_notes(subdir))


@mcp.tool()
def search_vault(query: str, subdir: str = "", limit: int = 50) -> str:
    """Case-insensitive full-text search across notes.

    Use this before ingesting a paper (check for prior coverage) and to find
    citation relationships and reusable topic tags. Returns ranked matches with
    snippets.
    """
    return _ok(_vault().search(query, subdir=subdir, limit=limit))


@mcp.tool()
def list_tags() -> str:
    """Return all tags in the vault with usage counts (frontmatter + inline).

    Use this to reuse existing `#topic/*`/`#domain/*` tags before inventing new
    ones, per doctrine.
    """
    return _ok(_vault().list_tags())


# ---------------------------------------------------------------------------
# Writer tools
# ---------------------------------------------------------------------------

@mcp.tool()
def write_note(path: str, content: str, overwrite: bool = True) -> str:
    """Create or overwrite a note. `content` is the full file text (frontmatter + body).

    Follow the paper-summary template and naming/placement rules from
    `load_doctrine`. Verify the target path and filename uniqueness first with
    `search_vault`/`list_notes`.
    """
    _guard_write()
    written = _vault().write(path, content, overwrite=overwrite)
    return _ok({"written": written})


@mcp.tool()
def append_to_note(path: str, content: str) -> str:
    """Append markdown to an existing note (e.g. an agent log entry)."""
    _guard_write()
    return _ok({"appended_to": _vault().append(path, content)})


@mcp.tool()
def replace_in_note(path: str, find: str, replace: str) -> str:
    """Replace all occurrences of `find` with `replace` in a note. Errors if not found."""
    _guard_write()
    n = _vault().replace_in_note(path, find, replace)
    return _ok({"path": path, "replacements": n})


@mcp.tool()
def manage_frontmatter(path: str, updates_json: str) -> str:
    """Merge a JSON object of frontmatter keys into a note's frontmatter.

    Use for connection-graph updates (cites/cited_by/extends/...), and the
    mandatory `domain:`/`status:` properties. `updates_json` example:
    '{"cited_by": ["[[havas-1980]]"], "status": "review"}'
    """
    _guard_write()
    try:
        updates = json.loads(updates_json)
        if not isinstance(updates, dict):
            raise ValueError("updates_json must be a JSON object")
    except (json.JSONDecodeError, ValueError) as e:
        raise VaultError(f"Bad updates_json: {e}")
    fm = _vault().manage_frontmatter(path, updates)
    return _ok({"path": path, "frontmatter": fm})


@mcp.tool()
def manage_tags(path: str, add_json: str = "[]", remove_json: str = "[]") -> str:
    """Add/remove tags in a note's frontmatter `tags` array.

    `add_json`/`remove_json` are JSON arrays of tag strings (with or without a
    leading '#'), e.g. '["topic/burnside-groups","status/draft"]'.
    """
    _guard_write()
    try:
        add = json.loads(add_json)
        remove = json.loads(remove_json)
    except json.JSONDecodeError as e:
        raise VaultError(f"Bad tag JSON: {e}")
    tags = _vault().manage_tags(path, add, remove)
    return _ok({"path": path, "tags": tags})


# ---------------------------------------------------------------------------
# Research-handle extras
# ---------------------------------------------------------------------------

@mcp.tool()
def fetch_paper(url: str) -> str:
    """Fetch a paper or web page as clean text (defuddle if available, else HTTP).

    First step of ingest. If it returns little/nothing (image-only PDF, login
    wall), tell the user and ask for an alternative source, per doctrine.
    """
    return _ok(_fetch_paper(url))


@mcp.tool()
def lookup_citation(url_or_id: str) -> str:
    """Best-effort citation count (Semantic Scholar / arXiv). Record with today's date."""
    return _ok(_lookup_citation(url_or_id))


@mcp.tool()
def load_doctrine() -> str:
    """Load the vault's Researcher doctrine (agent prompt, templates, taxonomy, workflows).

    CALL THIS FIRST in any research session. It returns the exact rules the
    Claude `/research` skill follows, read live from the vault so it stays in
    sync. Follow it verbatim.
    """
    return _load_doctrine(_vault().root)


# ---------------------------------------------------------------------------
# Prompt — the entry point users invoke, analogous to `/research`
# ---------------------------------------------------------------------------

@mcp.prompt()
def research(request: str = "") -> str:
    """The /research entry point. Injects doctrine and states the task."""
    doctrine = _load_doctrine(_vault().root)
    task = request.strip() or (
        "No specific request provided. Ask the user for a paper URL/ID, a list "
        "of URLs, a literature-scan topic, a --reconnect scope, or --notes."
    )
    return (
        f"{doctrine}\n\n{'=' * 72}\n## Your task\n{'=' * 72}\n\n{task}\n\n"
        "Proceed per the matching workflow (single-paper / batch / "
        "literature-scan / connection-pass / personal-notes). Use the tools: `fetch_paper`, "
        "`search_vault`, `list_tags`, `write_note`, `manage_frontmatter`, "
        "`manage_tags`, `lookup_citation`. Always check for prior coverage "
        "before writing, verify unique filename + correct placement, and "
        "populate connection-graph frontmatter with bidirectional links."
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
