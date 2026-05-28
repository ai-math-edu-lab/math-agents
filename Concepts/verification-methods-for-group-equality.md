---
title: "Verification Methods for Group Equality"
domain: methodology
status: draft
author: maumayma
language: en
introduced_in: []
appears_in:
  - "[[Research/Group theory/Burnside groups/B25/havas-robertson]]"
  - "[[Research/Group theory/Burnside groups/B25/havas-wall-wamsley-1974]]"
  - "[[Research/Group theory/Open problems/Free groups/2-relator-word-problem-9.29-merzlyakov]]"
related_concepts:
  - "[[kb-mixing-stagnation]]"
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/word-problem
  - topic/knuth-bendix
  - topic/finitely-presented-groups
  - concept
  - status/draft
invariants:
  - id: V1
    summary: "KB with proven confluence is the only general method that is both necessary and sufficient for equality in a finitely presented group."
    why: "A confluent + terminating system gives unique normal forms; equal normal form ⟺ equal group element. Without confluence, reduction is not a decision procedure."
  - id: V2
    summary: "Abelianization is a necessary condition for inequality, never a sufficient condition for equality."
    why: "The abelianization is a quotient; equal in the quotient means equal modulo commutators, not equal in G. The braid_reduce_fast bug is the canonical project failure case."
  - id: V3
    summary: "Individual rule applications from valid rules are always sound, regardless of whether the rule set is confluent."
    why: "Each rule l→r derives from group relators: l =_G r is a theorem about the group, not about the rule set. Applying it preserves group equality by transitivity."
  - id: V4
    summary: "Critical pair checking proves confluence of a specific rule set; it does not prove any group-equality claim directly."
    why: "A non-confluent system can be checked, found non-confluent, and corrected. The check is about the system's internal consistency, not about the underlying group."
  - id: V5
    summary: "A reduction chain proves w =_G w' only if every step applies a valid rule. It does NOT prove w =_G 1 unless the chain ends at the empty word."
    why: "Chains certify specific paths through the Cayley graph. Reaching a dead end or a non-identity word at chain terminus proves nothing about identity."
related:
  - "[[havas-wall-wamsley-1974]]"
  - "[[havas-newman-1980]]"
  - "[[havas-robertson]]"
  - "[[grobner]]"
  - "[[kb-mixing-stagnation]]"
  - "[[algo-mixing-burnside-slides]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
tags: [agent/research, user/maumayma, domain/methodology, project/none, status/draft, concept]
---

# Verification Methods for Group Equality

## What this note is

A decision reference for Validator. Given a claim about element equality in a finitely presented group — specifically in the B(2,5), B(4,3), B(5,3) context — this note answers: which verification methods are available, what each one actually proves, and what it cannot prove. **The load-bearing fact for every method is what its positive verdict entails.** Weak methods produce weaker verdicts. Combining methods narrows a claim from `#status/conjectured` toward `#status/replicated`, but only a complete KB system or a closed GAP coset enumeration achieves `#status/proven` for an arbitrary equality claim.

---

## The question shapes

Not all equality claims are the same shape. Conflating them is the primary source of verification errors in this project.

**Shape 1 — Element equality** (w₁ =_G w₂): are two words the same group element?
Reduces to Shape 2 by considering w = w₁ · w₂⁻¹.

**Shape 2 — Trivial-element check** (w =_G 1): is a word equal to the identity?
The hardest shape. For a finitely presented group with unsolvable word problem, no algorithm can decide this in general. For B(2,5) specifically, it is decidable in principle (the restricted group has order 5^34, so membership in the kernel of the regular representation is decidable), but no efficient method is currently available without a complete rewriting system.

**Shape 3 — Reduction-chain soundness**: does a sequence of rule applications w → w₁ → ... → wₙ preserve group equality?
Each step is a separate sub-question of the form "does applying rule lᵢ → rᵢ here preserve equality?" This is decidable step-by-step; the chain is sound iff every step is sound.

**Shape 4 — Confluence of a rewriting system**: given a rule set R, is every word reducible to a unique normal form?
Answered by exhaustive critical pair checking. Independent of any particular group claim.

**Shape 5 — Order of a group or element**: |G| = ? or ord(g) = ?
Usually handled via coset enumeration (group order) or iterated multiplication + reduction (element order in a group where you have a complete system).

---

## The methods

### 1. Knuth-Bendix completion + normal-form comparison

**What it does:** Given a group presentation ⟨X | R⟩ and a term ordering ≻, KB attempts to produce a complete (confluent + terminating) rewriting system R* such that w ↠ R* nf(w) and w₁ =_G w₂ iff nf(w₁) = nf(w₂).

**What it proves:**
- If KB terminates with confluent R*: normal-form equality is **necessary and sufficient** for group equality. Every positive verdict (nf(w) = ε) proves w =_G 1; every negative verdict (nf(w) ≠ ε) proves w ≠_G 1.
- If KB is still running or diverges: no verdict on any specific word. The partial rule set is not a decision procedure.

**Soundness assumptions:** The ordering ≻ must be a well-founded reduction ordering (no infinite descending chains). Shortlex and RPO both satisfy this. **The rule derivation must be from the group's actual relators** — rules that aren't derived from relators are unsound.

**Cost:** Doubly exponential in the number of relators in the worst case. For B(4,3), the Mixer approach found a 2,333-rule complete system in 33 minutes. For B(2,5), KB has not completed in 40+ years of attempts. For B(5,3), completion is an active open problem.

**When to use:** When a complete system is available (B(4,3): yes; B(2,5): no). Validity of the complete system requires a separate confluence check (see Method 4).

**Project instance:** B(4,3) complete system (2,333 rules, confluence verified on 1,702,360 critical pairs). See [[algo-mixing-burnside-slides]].

---

### 2. Todd-Coxeter coset enumeration

**What it does:** Given G = ⟨X | R⟩ and a subgroup H (possibly trivial), enumerates cosets of H in G. If it terminates, it outputs |G:H| and a coset table.

**What it proves:**
- If H = ⟨1⟩ and enumeration terminates: |G| = output count. The coset table gives a faithful permutation representation of G.
- Given a specific word w and the coset table: w acts as identity on cosets iff w =_G 1.
- Does **not** terminate for infinite groups or very large finite groups (B(2,5) has |B(2,5)_restricted| = 5^34 ≈ 10^23 — enumeration over trivial subgroup is infeasible).

**Soundness assumptions:** The relator list must be complete and correct.

**Cost:** Exponential space in the worst case; polynomial for many practical cases. In GAP: `CosetEnumeration(G, [])` or via the kbmag package.

**When to use:** Verifying group order for small groups (B(2,4) = 4096, B(3,3) = 2187: both feasible). Not feasible for B(2,5) restricted (5^34) or the unrestricted group.

**Project instance:** The deck's B(2,4) and B(3,3) validation used group-order verification consistent with Todd-Coxeter/BFS methods. See [[algo-mixing-burnside-slides]].

---

### 3. Tietze transformations

**What it does:** A sequence of four elementary moves on a group presentation that provably preserve the group:
1. Add a relator that follows from existing relators.
2. Remove a relator that follows from the remaining ones.
3. Add a new generator defined as a word in existing generators.
4. Remove a generator by substituting its definition everywhere.

**What it proves:**
- Each step preserves the presented group (the group before and after each move is isomorphic).
- A chain of Tietze moves proves that the initial and final presentations define the same group.
- Does **not** prove element equality directly — it proves presentation equivalence.

**Soundness assumptions:** Each step must be validated individually. Step 1 requires showing the added relator follows from existing relators (itself a Shape-2 question!). Step 3 requires the definition to be consistent with existing relators.

**Cost:** Polynomial per step if the presentation is small. Programs exist (Havas-Kenne-Richardson-Robertson, cited in [[havas-robertson]]); hand-verifiable for chains of ≤ ~5 steps.

**When to use:** Simplifying unwieldy presentations (e.g., Reidemeister-Schreier output), verifying that a simpler and a more complex presentation define the same group. Not for direct equality checking on specific words.

---

### 4. Abelianization check

**What it does:** Maps G → G^ab = G/[G,G] (the abelianization). For a finitely presented group ⟨X | R⟩, G^ab is a finitely generated abelian group computable by Smith normal form of the relator matrix. For B(2,5) specifically, G^ab ≅ ℤ₅ × ℤ₅, with each generator mapping to its exponent pair (e₁, e₂) mod 5.

**What it proves:**
- If φ(w₁) ≠ φ(w₂) in G^ab: then w₁ ≠_G w₂. (Necessary condition for inequality; equivalently: if w₁ = w₂ in G, then φ(w₁) = φ(w₂) in G^ab — contrapositive.)
- If φ(w₁) = φ(w₂) in G^ab: **nothing** about G-equality. The abelianization is a strict quotient; equal images are compatible with both w₁ =_G w₂ and w₁ ≠_G w₂.

**Soundness assumptions:** The abelianization map must be computed correctly. For B(2,5): φ(a) = (1,0), φ(b) = (0,1), φ(A) = (4,0) ≡ (-1,0), φ(B) = (0,4) mod 5. Each letter contributes additively.

**Cost:** O(|w|) per word — just sum generator exponents modulo the group's abelian invariants.

**When to use:** As a fast pre-filter before any expensive method. If the abelianization disagrees, the words are unequal — done. If the abelianization agrees, proceed to stronger methods.

**The canonical failure case in this project:** The `braid_reduce_fast` bug. The reduction chain for comm_12_9 produced words with abelianization (4,4) mod 5 rather than (0,0). Each individual step passed the per-step abelianization check because both GH and HG have the same commutative exponents — but the *cumulative* abelianization diverged. The fix required tracking the full running abelianization, not just checking each step locally. See memory entry "CRITICAL BUG FIXED: braid_reduce_fast."

---

### 5. Individual rule application in a non-confluent system

**What it does:** Applies a single rewrite rule l → r to a word w = u·l·v to produce w' = u·r·v, where the rule l → r is known to be a valid group equality (l =_G r derived from relators).

**What it proves:**
- w =_G w' (the specific rewrite step preserves group equality).
- A chain of valid steps w → w₁ → ... → wₙ proves w =_G wₙ.
- If wₙ = ε: proves w =_G 1.
- If wₙ ≠ ε: proves w =_G wₙ. **Does not prove w ≠ 1** — the chain may simply have run out of applicable rules before reaching identity.

**Soundness assumptions:** Every rule l → r applied must derive from the group's relators. Rules from a lifted KB run (where KB was run on the full presentation, not a quotient) are valid group equalities regardless of whether the system is confluent. Rules from other sources (heuristics, incomplete derivations, wrong presentations) may be unsound.

**"Bounded soundness":** The term used in this project for what this method achieves. It certifies specific reduction paths, not global decidability. A word that doesn't reduce to identity via available rules may still equal identity via a different path.

**When to use:** When a complete system is unavailable (B(2,5)) and we want to certify partial progress. E.g., the b25_reduce_core pipeline: the 28,652→544→...→7,245 chain certifies that the starting word equals 7,245 chars in B(2,5), but does not certify that either equals identity.

**Critical guard:** Before reporting a chain as sound, verify the abelianization is preserved end-to-end (not step-by-step — cumulative), and verify a sample of rules against the group presentation.

---

### 6. GAP symbolic computation

**What it does:** GAP (Groups, Algorithms, Programming) is a computer algebra system with built-in finitely presented group machinery. Relevant functions:
- `F := FreeGroup("a","b"); G := F / [relators]` — creates the fp group.
- `IsOne(g)` — tests if element g equals identity in G. Internally runs coset enumeration or KB (via kbmag package).
- `Order(g)` — element order (may not terminate).
- `Size(G)` — group order via Todd-Coxeter (may not terminate for large groups).
- `IsIdenticalObj(g,h)` — **object identity** (same GAP memory object), NOT group equality. A common confusion; this is not a mathematical check.

**What it proves:**
- `IsOne(g)` returning `true`: if the underlying algorithm (KB or TC) terminated and is correct, then g =_G 1. The verdict is as strong as the underlying method.
- `IsOne(g)` returning `false`: g ≠_G 1 (if terminated).
- `IsOne(g)` not returning: algorithm diverged; no verdict.

**Soundness assumptions:** GAP's implementations of TC and KB are well-tested. The kbmag package (Holt) implements KB for string rewriting; its output is sound if the ordering and relator list are correct.

**B(2,5) specifics:** GAP's kbmag does not complete KB for B(2,5) — it diverges. `IsOne` for B(2,5) words that aren't provably identity will loop. The 5^34 order means even `Size(G)` via TC over the trivial subgroup is infeasible. GAP is useful for B(2,5) quotients (nilpotent quotients, abelianization) but not for the full group word problem.

**B(4,3) specifics:** After the 2,333-rule complete system, one can in principle input those rules directly as a GAP rewriting system for instant word-problem decisions.

**Installation requirement:** GAP not installed in the current project environment (as of 2026-05-22). See escalation section below.

---

### 7. Sage / Gröbner-based methods

**What it does:** Sage wraps GAP for group theory. Additionally, via Gröbner bases (see [[grobner]]): for a finitely presented group G = ⟨X|R⟩, construct the variety of SL(n,K) representations V_R. A word w represents the identity in G only if it acts as the identity matrix in every representation. The Gröbner-based quotient test (Kreuzer-Myasnikov-Rosenberger) checks whether φ(w) = I in the universal linear representation G → SL(n, Q_R).

**What it proves:**
- If φ(w) ≠ I in the universal representation: w ≠_G 1. (Sufficient for inequality; "No" verdict.)
- If φ(w) = I: "Don't know" — the representation may not be faithful. (Never proves w = 1 unless faithfulness is established.)
- This is a semi-decision procedure for the "No" side only.

**Soundness assumptions:** The Gröbner basis computation is correct; the representation is correctly constructed.

**Cost:** Gröbner basis computation is doubly exponential in the worst case. For small n (n=2) and short relators, often practical. For B(2,5) with relators of length up to 20: untested (Section 7.5 of grobner.pdf is labeled "TODO: Continue!").

**When to use:** As a "No" filter before attempting KB — if the Gröbner test can certify w ≠ 1, the expensive KB search is unnecessary. If the test returns "Don't know," fall back to other methods.

**Installation requirement:** Sage not installed in current environment. See escalation section.

---

### 8. Hand proofs

**What it does:** A human (or AI-written, human-reviewed) proof that explicitly cites group relators or derived rules at each step.

**What it proves:** Whatever the proof demonstrates — only as strong as the cited justifications. A hand proof citing valid relators at each step is fully rigorous. A hand proof that cites "by inspection" or "clearly" is not.

**Soundness assumptions:** The proof is complete (no gaps), every cited rule is valid, and the reviewer is competent to catch errors.

**When to use:**
- Short reduction chains (≤ ~10 steps) where each step can be displayed and checked.
- Structural arguments: "this word has weight > 12 in the Hall basis of B(2,5), so it's trivial by nilpotency class" — this is a valid hand argument for the restricted group.
- Presentation-equivalence claims that are small enough to verify.

**Limitations:** Hand proofs do not scale. A 28,652-character word reduction chain cannot be hand-verified step by step. For those, use automated methods.

---

## Decision tree

```
Claim type?
│
├─ Shape 3 (reduction-chain soundness): is step-by-step valid?
│   └─ For each step l→r: is the rule a valid group equality?
│       ├─ YES → step is sound. Check all steps; chain is sound if all are.
│       │         Then check: does chain end at ε? → proves w =_G 1.
│       │         Ends at wₙ ≠ ε? → proves w =_G wₙ only.
│       └─ NO  → step is unsound; flag to Lead. Stop.
│
├─ Shape 4 (confluence): is rule set R complete?
│   └─ Run critical pair check on all pairs in R.
│       ├─ All pairs joinable → R is confluent. Verdict: PROVEN confluent.
│       └─ Some pair fails → R is not confluent. Tidy and repeat.
│
├─ Shape 5 (group/element order):
│   ├─ Complete rule set available? → BFS from identity; count reachable elements.
│   ├─ GAP installed? → Size(G) via Todd-Coxeter (may not terminate).
│   └─ Neither → ESCALATE for tool install (see below).
│
└─ Shape 1 or 2 (element equality or trivial check):
    Reduce Shape 1 to Shape 2: check w₁ · w₂⁻¹ =_G 1.
    │
    ├─ FAST FILTER: abelianization check (always available, O(|w|))
    │   └─ φ(w) ≠ 0 in G^ab → w ≠_G 1. PROVEN NOT EQUAL. Done.
    │       φ(w) = 0 → inconclusive. Continue.
    │
    ├─ Complete rewriting system available (e.g., B(4,3) 2333 rules)?
    │   └─ YES → reduce w. nf(w) = ε ↔ w =_G 1. PROVEN (either way). Done.
    │
    ├─ GAP installed + KB or TC terminates for this group?
    │   └─ YES → run IsOne(w). PROVEN if terminates.
    │
    ├─ Gröbner/Sage available?
    │   └─ YES → run quotient test.
    │       nf(φ(w)) ≠ I → PROVEN w ≠ 1. Done.
    │       nf(φ(w)) = I → "Don't know". Continue.
    │
    ├─ Partial rule set (non-confluent, e.g. lifted-KB banks for B(2,5)):
    │   └─ Apply rules; reduce to w'.
    │       w' = ε → PROVEN w =_G 1 (chain soundness applies). Done.
    │       w' ≠ ε → know w =_G w' (bounded soundness). Report w' as current form.
    │                 Mark claim #status/replicated if multiple independent rule banks agree.
    │
    └─ Hand proof (short chain or structural argument):
        └─ Write proof; route to Validator for review.
            Accepted → PROVEN (by whatever the proof establishes).
            Rejected → back to top; try different method.
```

### Current toolkit for B(2,5) (GAP not installed, KB not complete)

Available:
1. Abelianization (necessary, instant, catches sign/inverse errors).
2. Individual rule applications from valid rule banks (bounded soundness: certifies reduction path, not identity).
3. Structural weight arguments (for the restricted group: elements at class > 12 are trivially equal to 1).
4. Hand proofs for specific short chains.

**What none of these can prove:** An arbitrary element equality w =_G 1 in B(2,5) where w is long and the abelianization check passes. For such claims, the achievable verdict is `#status/replicated` at best (multiple independent methods consistent with equality), not `#status/proven`.

**To reach `#status/proven` for B(2,5) word equalities:** Either (a) a complete KB system (none exists), or (b) a closed GAP coset enumeration on a quotient large enough to resolve the specific claim (possible for finite quotients, impossible for the full group without KB).

---

## When to escalate for missing tools

**Rule:** If a claim requires GAP or Sage and neither is installed, Validator files an install request via Lead within **10 minutes** of beginning triage on that claim. Do not attempt to reimplement GAP functionality by hand — the reimplementation will be slower, less tested, and more error-prone than the package.

**Escalation message to Lead:**
```
TYPE: BLOCKER
TOPIC: Tool needed for verdict on <claim>
CONTEXT: [[verification-methods-for-group-equality]] § GAP/Sage
ASK: Install GAP (with kbmag package) / Sage to support Shape-2 verification on <claim>.
     Claim currently routed to #status/conjectured pending tool availability.
DEADLINE: none (blocks verdict, not project)
```

**What Validator should do while waiting:** Apply all available methods (abelianization, partial rule banks, structural arguments). Document results and bounds. Mark with `#status/replicated` if multiple methods agree. Do not mark `#status/proven`.

**For nuextract-cli (OCR of scanned PDFs):** Same pattern — flag BLOCKED to Lead, note as "unread" in the paper summary. Do not fabricate content from the file name.

---

## References

Papers in `docs/papers/` (all are text-extracted and summarized in Research/):

- **Havas, Wall, Wamsley (1974)** — [[havas-wall-wamsley-1974]] — defines the consistent commutator power presentation for B(2,5) and the generator numbering convention used in B(2,5) reduction chains. The verification foundation for all comm_X_Y work.
- **Havas & Newman (1980)** — [[havas-newman-1980]] — describes the p-quotient algorithm and nilpotent group computation methods; background for KB's relationship to nilpotent quotients.
- **Havas & Robertson (1994)** — [[havas-robertson]] — surveys coset enumeration, Reidemeister-Schreier, Tietze, and KB as a toolkit. The best available survey of methods 1–3 above in one place.
- **Kreuzer, Myasnikov, Rosenberger (2025 draft)** — [[grobner]] — the Gröbner-based quotient test; method 7 above. Section 7.5 proposes applying this to B(2,5) but is incomplete.

Papers not in `docs/papers/` (cited in [[algo-mixing-burnside-slides]] and/or standard references):
- **Knuth & Bendix (1970)** — "Simple word problems in universal algebras." The original KB paper; method 1 above. Not in our folder; cite as Knuth & Bendix (1970).
- **Sims — *Computation with Finitely Presented Groups*** (1994, Cambridge University Press) — the standard textbook covering methods 1–3 and 6 in full depth. Not available in `docs/papers/`; flag to Lead to add if Validator needs the specific theorem statements.
- **Holt — KBMag documentation** — the manual for the Knuth-Bendix for MAGs package (GAP). Online; not in our folder.

---

## Caveats / limitations of this note

- This note covers the methods as used **in this project's context** (finitely presented groups, primarily Burnside groups). It is not a general survey of all group-equality methods (e.g., it omits Magnus-Karrass-Solitar methods for one-relator groups, HNN extensions, Bass-Serre theory).
- Status: `#status/draft`. Validator should note corrections or additions; Researcher will update.
- The "Decision tree" section uses the current tool availability (2026-05-22). Update if GAP or Sage becomes available.
