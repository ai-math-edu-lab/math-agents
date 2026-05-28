---
title: "Coset Enumeration (Todd-Coxeter Algorithm)"
author: maumayma
language: en
source: "Lyndon & Schupp, Combinatorial Group Theory (1977), §II.3; Todd & Coxeter (1936)"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/coset-enumeration
  - topic/word-problem
  - topic/finitely-presented-groups
  - status/validated
related:
  - "[[presentations]]"
  - "[[tietze-transformations]]"
  - "[[free-groups]]"
---

# Coset Enumeration (Todd-Coxeter Algorithm)

## Purpose

Given G = ⟨X | R⟩ and a subgroup H = ⟨h₁,...,hₖ⟩ specified by words in F(X), **coset enumeration** computes the index [G:H] and constructs a coset table — a finite table encoding the action of each generator on each coset.

If H = {e}, the algorithm computes |G| (when G is finite) and the Cayley table.

*Historical source: Todd & Coxeter, Proc. Edinburgh Math. Soc. (1936).*

## The coset table

Rows: cosets of H in G (numbered 1 = H, 2, ..., n = [G:H]).
Columns: one per generator x ∈ X ∪ X⁻¹.
Entry (i, x): the coset (Hgᵢ) · x.

The table is "complete" when every entry is filled; "closed" when every relator applied to any coset returns to the same coset (i.e., the relators act trivially on G/H as they should).

## Algorithm sketch

1. Start with coset 1 = H.
2. For each subgroup generator hⱼ: deduce that hⱼ acts trivially on coset 1 (since H · hⱼ = H).
3. For each relator r ∈ R and each coset i: apply r starting from coset i; if a new coset is encountered, add it; if the trace loops back, deduce table entries (coincidences).
4. Handle coincidences (two coset numbers that turn out to be the same coset): merge and propagate.
5. Repeat until the table is complete and closed.

## Termination

Todd-Coxeter terminates iff [G:H] < ∞. If G is infinite or [G:H] is infinite, the algorithm runs forever (or until a bound is exceeded).

For G = ⟨X | R⟩ and H = {e}:
- Terminates iff G is finite.
- Output: |G| and the complete multiplication table of G.

## In practice

- **GAP:** `CosetTable(G, H)` and `Index(G, H)`.
- **KBMAG (autgroup):** computes the automatic structure (a generalization that works for infinite groups too, when the group is automatic).

See `Tools/GAP/examples/02-coset-enumeration.md` for a runnable example.

## Complexity

- **Best case:** linear in the final coset table size.
- **Worst case:** exponential in |R| even when [G:H] is small (the table can grow enormously before collapsing).
- **In practice:** highly dependent on the strategy (HLT vs. Felsch; live vs. deferred coincidence handling). Various strategies implemented in GAP.

## Related concepts

- [[presentations]] — the input (G = ⟨X | R⟩, H specified by generators).
- [[tietze-transformations]] — Reidemeister-Schreier (which uses coset enumeration) produces a presentation for H, then Tietze simplifies.
- [[free-groups]] — the free group is the setting where the relator words live before quotienting.
