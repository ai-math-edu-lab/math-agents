#!/usr/bin/env python3
"""
verify-bidirectional-links.py
Checks that for every paper note in Research/ that lists paper X in cites:,
paper X has the citing note listed in its cited_by:.

Run from anywhere:
    python3 /Users/maumayma/Documents/Obsidian/Math/_meta/scripts/verify-bidirectional-links.py

Exit 0 = clean. Exit 1 = gaps found (printed to stdout).

Last promoted from Agents/maumayma/Researcher/scratch/ on 2026-05-28 (F8.4).
"""
import os, re, glob, sys

VAULT = "/Users/maumayma/Documents/Obsidian/Math/Research"

def parse_wikilink_stems(fm_block):
    """Extract filename stems from [[...]] wikilinks in a YAML block."""
    links = re.findall(r'\[\[([^\]|#]+?)(?:\|[^\]]+)?\]\]', fm_block)
    return [link.split('/')[-1] for link in links]

def main():
    paper_files = glob.glob(f"{VAULT}/**/*.md", recursive=True)

    cites_map = {}
    cited_by_map = {}

    for fpath in paper_files:
        stem = os.path.splitext(os.path.basename(fpath))[0]
        with open(fpath, 'r', errors='replace') as f:
            content = f.read()

        fm_match = re.match(r'^---\n(.*?\n)---', content, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)

        cites_section = re.search(r'^cites:\s*\n((?:\s*-\s*.+\n)*)', fm, re.MULTILINE)
        cites_map[stem] = parse_wikilink_stems(cites_section.group(1)) if cites_section else []

        cited_by_section = re.search(r'^cited_by:\s*\n((?:\s*-\s*.+\n)*)', fm, re.MULTILINE)
        cited_by_map[stem] = parse_wikilink_stems(cited_by_section.group(1)) if cited_by_section else []

    # Build expected cited_by from cites_map
    expected = {}
    for citing, cited_list in cites_map.items():
        for cited in cited_list:
            expected.setdefault(cited, []).append(citing)

    gaps = []
    for cited_stem, expected_citers in expected.items():
        actual_citers = cited_by_map.get(cited_stem, [])
        missing = [c for c in expected_citers if c not in actual_citers]
        if missing:
            gaps.append((cited_stem, missing))

    if gaps:
        print("Missing cited_by entries:")
        for cited_stem, missing in gaps:
            print(f"  {cited_stem}: missing <- {missing}")
        sys.exit(1)
    else:
        print("All bidirectional cited_by links verified clean.")
        sys.exit(0)

if __name__ == "__main__":
    main()
