---
title: OCR tooling — nuextract-cli
status: draft
domain: infra
project: mixer-core
author: <human>
tags:
  - agent/human
  - domain/infra
  - project/mixer-core
  - status/draft
  - convention
---

# OCR tooling — `nuextract-cli`

## Why we need it

Researcher occasionally encounters **image-only or scanned PDFs** — old group theory monographs, decades-old preprints, papers behind paywalls only available as scanned reproductions. `defuddle` can read text-extractable PDFs but produces nothing useful for pure-image PDFs.

Without an OCR step, those papers are unreadable by AI agents. With one, they enter the literature pass like any other source.

## What we chose

[**NuExtract-2.0-2B**](https://huggingface.co/numind/NuExtract-2.0-2B) — a 2B-parameter vision-language model from NuMind, based on Qwen2-VL-2B-Instruct.

- **License: MIT** (commercial-friendly, no restriction on research or production use).
- **Combines OCR + structured extraction** in one model — no separate Tesseract step required.
- **Image / PDF input** — takes the raw scan, outputs structured JSON per a schema.
- **Resource profile**: ~4–5 GB VRAM in bfloat16, runs on Apple Silicon via MPS (slower than GPU but workable).

The larger 8B variant exists if accuracy needs improvement, also MIT.

## What `nuextract-cli` should expose

A Python `uv`-managed tool (separate package or under `algo_mixing/tools/nuextract-cli/`) that wraps the model loading + invocation. Goals:

- **CLI invocation**: `nuextract-cli <pdf-path> <schema-file.json>` → emits extracted JSON to stdout.
- **Default schema** for academic papers (title, authors, abstract, sections, references) — Researcher can specify a richer schema for specific extraction needs.
- **One-time model load per invocation** is OK for the v0; if usage volume grows, daemonize.
- **Apple Silicon support**: don't require `flash_attention_2`; use MPS or CPU as fallback.

## What it should NOT do

- Don't ship a full GUI or web interface — it's a CLI.
- Don't bundle the model weights in the algo_mixing repo — they're large (~2 GB); use HuggingFace's cache.
- Don't try to be a general OCR system — NuExtract is specifically a *structured extraction* model. If you just need raw text, that's a degenerate schema (e.g. `{"text": "verbatim-string"}`).

## Status

`#status/draft` — not implemented. Researcher's role prompt references this stub; when Researcher needs OCR and `nuextract-cli` doesn't exist, it flags to Lead. Lead can file the implementation as a Developer ticket.

## When to file the Developer ticket

When the first real blocker happens: Researcher gets a B(2,5) old preprint that needs OCR, or a colleague brings a domain-specific paper that's image-only. Until then, the stub note exists and the intent is documented; building the tool before the need is premature.

## Related

- [[researcher]] — uses `nuextract-cli` for image-only PDFs.
- Model card: [NuExtract-2.0-2B on HuggingFace](https://huggingface.co/numind/NuExtract-2.0-2B).
