#!/usr/bin/env python3
"""
find-graph-orphans.py
Reports notes with zero wikilinks in the vault.

Default (strict): zero incoming AND zero outgoing — fully isolated notes.
--loose: zero incoming OR zero outgoing — partially isolated (one-way).

Exclusions: _meta/skills/, .obsidian/, Agents/<user>/<role>/log.md, README.md files.

Run:
  python3 _meta/scripts/find-graph-orphans.py           # strict (both-way orphans)
  python3 _meta/scripts/find-graph-orphans.py --loose   # loose (either-way)

Exit 0 = no orphans found. Exit 1 = orphans found.

Last updated: 2026-05-28 — added --loose flag per Lead recommendation (Phase 9 close).
"""
import os, re, glob, sys

VAULT = "/Users/maumayma/Documents/Obsidian/Math"

EXCLUDE_DIRS = {
    "_meta/skills",
    ".obsidian",
}

EXCLUDE_PATTERNS = [
    r"/Agents/.+/log\.md$",
    r"/README\.md$",
    r"/_placeholder\.md$",
    r"/INSTALL\.md$",   # skills install docs — housekeeping, exempted per naming-conventions Rule 2
]

def is_excluded(path):
    rel = path.replace(VAULT + "/", "")
    for excl in EXCLUDE_DIRS:
        if rel.startswith(excl):
            return True
    for pat in EXCLUDE_PATTERNS:
        if re.search(pat, path):
            return True
    return False

def extract_wikilinks(content):
    """Extract all [[...]] wikilink targets from a file's body (skip frontmatter)."""
    # Remove frontmatter
    body = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    # Find all [[link]] or [[link|alias]] or [[link#heading]]
    links = re.findall(r'\[\[([^\]|#\n]+?)(?:[|#][^\]\n]*)?\]\]', body)
    # Also check frontmatter for wikilinks (cites:, cited_by:, key_concepts:, etc.)
    fm_match = re.match(r'^---\n(.*?\n)---', content, re.DOTALL)
    if fm_match:
        links += re.findall(r'\[\[([^\]|#\n]+?)(?:[|#][^\]\n]*)?\]\]', fm_match.group(1))
    # Normalize: take filename stem from path-style links
    stems = set()
    for link in links:
        stem = link.strip().split('/')[-1]
        stems.add(stem.lower())
    return stems

def main():
    loose = "--loose" in sys.argv

    all_files = {}  # stem (lower) -> full path
    for fpath in glob.glob(f"{VAULT}/**/*.md", recursive=True):
        if is_excluded(fpath):
            continue
        stem = os.path.splitext(os.path.basename(fpath))[0].lower()
        all_files[stem] = fpath

    # Build outgoing links per file
    outgoing = {}
    for stem, fpath in all_files.items():
        with open(fpath, 'r', errors='replace') as f:
            outgoing[stem] = extract_wikilinks(f.read())

    # Build incoming links per file
    incoming = {stem: set() for stem in all_files}
    for citing_stem, linked_stems in outgoing.items():
        for linked in linked_stems:
            if linked in incoming:
                incoming[linked].add(citing_stem)

    # Find orphans
    orphans = []
    for stem, fpath in sorted(all_files.items()):
        out = outgoing[stem] - {stem}
        inc = incoming[stem] - {stem}
        if loose:
            # Loose: zero in OR zero out
            if not out or not inc:
                label = "isolated" if not out and not inc else ("no-out" if not out else "no-in")
                orphans.append((fpath, label, len(inc), len(out)))
        else:
            # Strict: zero in AND zero out
            if not out and not inc:
                orphans.append((fpath, "isolated", 0, 0))

    mode = "loose (zero in OR zero out)" if loose else "strict (zero in AND zero out)"
    print(f"Total notes scanned: {len(all_files)}")
    print(f"Orphans [{mode}]: {len(orphans)}\n")
    for fpath, label, inc_n, out_n in orphans:
        rel = fpath.replace(VAULT + "/", "")
        print(f"  [{label}] {rel}  ({inc_n} in, {out_n} out)")

    return len(orphans)

if __name__ == "__main__":
    count = main()
    sys.exit(0 if count == 0 else 1)
