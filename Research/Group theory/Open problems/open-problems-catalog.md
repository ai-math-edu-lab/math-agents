---
title: "Open Problems in Group Theory — Mixer/AI Feasibility Catalog"
domain: group-theory
status: draft
author: maumayma
related:
  - "[[problems-people]]"
  - "[[kourovka-2022]]"
  - "[[algo-mixing-burnside-slides]]"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/word-problem
  - topic/braid-groups
  - topic/finitely-presented-groups
  - synthesis
  - status/draft
---

# Open Problems in Group Theory — Mixer/AI Feasibility Catalog

**Purpose:** Canonical reference for Lead when deciding which Mixer cross-domain applications to spawn. Each entry is scored on AI/Mixer feasibility (score/1–3) against a consistent rubric. Scope is intentionally narrow: only problems with at least one canonical reference, direct relevance to group theory, and a plausible algorithmic angle.

Last updated: 2026-05-22 by Researcher.

---

## Scope

**Included:**
- Open problems in group theory with a verifiable canonical source (Kourovka Notebook problem number, published paper, or named internal document from the project).
- Problems where the AI/Mixer feasibility score is non-trivial to assign (i.e., not obviously score/3 or obviously score/1 without analysis).
- Problems already in scope for the algo_mixing project (from [[problems-people]]) plus Kourovka-sourced problems adjacent to our experimental domains.

**Excluded:**
- Resolved problems (marked ∗ in Kourovka 2022 or confirmed solved in the body text).
- Problems where I could not verify the canonical source (no invented problems, no invented references).
- Problems outside group theory: combinatorics without a group-theoretic frame, topology-only problems, representation theory of specific finite groups (e.g., sporadic group character tables).
- Problems requiring purely algebraic structural arguments with no search or verification component (typically score/1 and not worth cataloging unless they define a boundary condition).

**Selection criteria for Kourovka-sourced problems:**
1. Directly involves a group family or algorithmic question relevant to the Mixer: word problem, Burnside groups, braid groups, group rings, free groups.
2. Appears in a Kourovka issue where the problem is clearly still open in 2022 (no asterisk).
3. Has a plausible — even if indirect — computational angle worth assessing.

---

## Scoring Rubric

| Score | Label | Meaning |
|-------|-------|---------|
| 3 | High | Mixer's specific machinery (KB interleaving, rule injection, beam search) directly attacks. Concrete computational instance with existing infrastructure. Output is a verifiable mathematical artifact. |
| 2 | Medium | Partial computational evidence, verification tooling helps, or Mixer-style cooperation could contribute a *step*. Mixer might not resolve the problem but could contribute meaningfully. |
| 1 | Low | Requires deep structural insight, classification arguments, or undecidability arguments that KB/search/verification cannot reach. Mixer is irrelevant or marginal. |

---

## Score Distribution (2026-05-22)

| Score | Count | Problems |
|-------|-------|---------|
| score/3 | 1 | B(2,5) finiteness (11.48) |
| score/2 | 4 | Exponent-5 infinite groups (4.2b), Burau₄ faithfulness, B₄ membership (6.24), Andrews-Curtis |
| score/1 | 2 | Kaplansky zero-divisors, 2-relator word problem (9.29) |
| **Total** | **7** | |

Most open problems in group theory are score/1 or score/2. The score/3 entry (B(2,5)) is exceptional because the Mixer is already deployed against it with active experiments and existing infrastructure.

---

## Catalog by Family

### Burnside groups/

| Note | Problem | Score | Source |
|------|---------|-------|--------|
| [[b25-finiteness-11.48-kostrikin]] | Is B(2,5) finite or infinite? | 3 | Kourovka 11.48 (Kostrikin, 1990) |
| [[b-exponent-5-adian-4.2b]] | Do infinite finitely generated groups of exponent 5 exist? | 2 | Kourovka 4.2b (Adian, 1973) |

### Braid groups/

| Note | Problem | Score | Source |
|------|---------|-------|--------|
| [[burau4-faithfulness]] | Is the Burau representation of B₄ faithful? | 2 | Well-known open problem; [[problems-people]] |
| [[braid-b4-membership-6.24-makanin]] | Is the membership problem for B₄ decidable? | 2 | Kourovka 6.24 (Makanin, 1980) |

### Group rings/

| Note | Problem | Score | Source |
|------|---------|-------|--------|
| [[kaplansky-zero-divisors]] | Kaplansky zero-divisors conjecture | 1 | Well-known (Kaplansky, ~1956); [[problems-people]] |

### Free groups/

| Note | Problem | Score | Source |
|------|---------|-------|--------|
| [[andrews-curtis-conjecture]] | Do all balanced presentations of the trivial group AC-reduce? | 2 | Andrews-Curtis 1965; [[problems-people]] |
| [[2-relator-word-problem-9.29-merzlyakov]] | Do 2-relator groups with insoluble word problem exist? | 1 | Kourovka 9.29 (Merzlyakov, 1984) |

---

## Hand-off Notes

### Problems needing paper acquisition

The following catalog entries have `source_path: ""` — no paper exists in `docs/papers/`. Before extending these notes or building experiments, acquire the canonical sources:

- **Burau₄ faithfulness**: Bigelow 1999 (n≥5 unfaithful, J. AMS), Long-Paton 1993 (n≥6); Birman textbook for status.
- **Kaplansky zero-divisors**: Kaplansky 1956 (original); Linnell survey "Zero divisors and group von Neumann algebras"; Gräter et al. for constructive approaches.
- **Andrews-Curtis conjecture**: Andrews-Curtis 1965 (Proc. Amer. Math. Soc. 16, 192–195); Akbulut-Kirby (candidate counterexamples); Bridson examples.

### Problems needing Kourovka verification

- **Burau₄ faithfulness**: no Kourovka problem number identified. May not appear in the Kourovka Notebook.
- **Andrews-Curtis (classical)**: no Kourovka problem number identified. Kourovka 18.89 is a related meta-question (ACₙ finitely presented?), not the classical conjecture.
- **Kaplansky zero-divisors**: Kourovka 12.29 (Zalesski) and 18.80 (Passman) are related ring-theoretic questions; the classical zero-divisors conjecture does not appear to have its own Kourovka entry.

### Problems needing Validator input

- **B(2,5) finiteness (11.48)**: The "~50 witness words" claim in [[algo-mixing-burnside-slides]] (if wᵢ = e for all i, B(2,5) finite) lacks a source citation. Validator should verify the witness word count and originating paper before relying on this as a proof strategy.

### Catalog extension guidance (for future Researcher)

The current catalog covers: Burnside groups (2), Braid groups (2), Group rings (1), Free groups (2). Domains NOT yet covered with explicit notes despite being mentioned in [[problems-people]]:

- **Cayley graph approximation algorithms** (Ushakov's approach for search word problem): no catalog entry; no Research/ paper note.
- **Automated theorem proving for B(2,5)** (Lisitsa): no catalog entry; no paper.
- **Todd-Coxeter / coset enumeration** (Ginzburg): no dedicated problem note, though [[verification-methods-for-group-equality]] covers Todd-Coxeter as a method.

These should be added when Lead routes a specific research question or when a canonical source is available.

---

## Relationship to Other Vault Regions

- **[[problems-people]]** — the internal project planning document that seeded this catalog. The catalog extends it with Kourovka sourcing and scoring.
- **[[kourovka-2022]]** — the Kourovka Notebook summary note; the catalog draws selectively from it.
- **[[algo-mixing-burnside-slides]]** — the slide deck that established the Mixer methodology and set B(2,5) as the primary target. Score/3 for 11.48 directly reflects the existing project infrastructure described there.
- **[[verification-methods-for-group-equality]]** — complements this catalog: given a problem instance, which verification method applies? This catalog tells Lead WHICH problems to attack; the verification-methods note tells Validator HOW to verify outputs.
