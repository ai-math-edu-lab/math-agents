# /// script
# requires-python = ">=3.10"
# dependencies = ["pypdf>=4"]
# ///
"""Throwaway extractor: print plain text per page for one PDF path."""
import sys
from pypdf import PdfReader

path = sys.argv[1]
reader = PdfReader(path)
print(f"=== {path} ===")
print(f"pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages, 1):
    text = page.extract_text() or ""
    print(f"\n--- page {i} ---")
    print(text)
