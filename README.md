<div align="center">

# ELYRIA RUNTIME LAW

### Consequence admission before effect
### Runtime law for consequence-bearing systems

<br />

**ELYRIA SYSTEMS — VA**  
**Samantha Revita · Terry Snyder**

<br />

[![Elyria Runtime Law CI](https://github.com/Kamanaka5502/elyria-runtime-law/actions/workflows/ci.yml/badge.svg)](https://github.com/Kamanaka5502/elyria-runtime-law/actions/workflows/ci.yml)
![Status](https://img.shields.io/badge/status-public%20proof%20surface-gold)
![Runtime](https://img.shields.io/badge/runtime-protected%20commercial%20layer-black)
![License](https://img.shields.io/badge/license-proprietary-red)
![Category](https://img.shields.io/badge/category-consequence%20admission-blueviolet)

<br />

> **Most systems govern actors, actions, or outputs.**  
> **Elyria governs continuation.**

<br />

```text
possible ≠ admissible
authenticated ≠ standing
workflow-complete ≠ consequence-safe
EXECUTE is the only outcome that may bind effect
```

</div>

---

## What this is

**Elyria Runtime Law** is a public proof surface for a protected runtime category: **consequence admission before effect**.

It frames the boundary where a proposed transition is evaluated before it is allowed to become consequence.

The core object is not an action.

The core object is **attempted becoming**: a proposed transition pressing toward consequence.

A proposed action can be possible, requested, authenticated, predicted, or workflow-complete and still fail consequence admissibility.

> **Most systems decide whether something may run.**  
> **Elyria determines whether continuation is lawful enough to become consequence.**

---

## Authorship / stewardship

**Elyria Systems — VA**  
**Samantha Revita · Terry Snyder**

This repository is intentionally category-protected. It exposes the public proof framing, not the protected production substrate.

It is not a free implementation release.

---

## Category boundary

**Consequence admission before effect.**

Elyria Runtime Law evaluates whether a proposed consequence may enter, remain, redirect, halt, restart, or bind under live state.

This is not:

| Not this | Why |
|---|---|
| AI governance | governance may inform the boundary; it does not bind consequence |
| authorization | authorization is one condition, not the full admissibility field |
| workflow | workflow moves tasks; Elyria evaluates whether consequence may bind |
| audit | audit records what happened; Elyria prevents inadmissible effect |
| monitoring | monitoring observes; Elyria resolves consequence admission |
| compliance dashboard | dashboards surface status; they do not enforce runtime law |

Those layers may provide inputs.  
They do not decide whether continuation remains lawful enough to become consequence.

---

## Runtime binding law

Elyria evaluates consequence admissibility as a constrained state resolution:

```text
Σ_C(x) = ⟨Φ(x), A(x), U(x), V(x), B(x), R(x), H(x)⟩
```

Where:

| Term | Meaning |
|---|---|
| `Φ(x) = C(x) − M(x)` | capacity minus burden |
| `A(x)` | authority validity |
| `U(x)` | authorization state |
| `V(x) ∈ Viab(R)` | viability within regime constraints |
| `B(x)` | breach condition; must resolve to zero |
| `H(x)` | continuation / coherence threshold |

This expression is a public category marker and conceptual proof surface.  
Production policy structures, corridor logic, client-specific evaluation rules, replay internals, and protected runtime implementation are not exposed here.

---

## Binding condition

A consequence may bind only if:

```text
Φ ≥ 0 ∧ A ≥ 0 ∧ U = 1 ∧ x ∈ Viab(R) ∧ B = 0 ∧ H ≥ H_min
```

If any condition fails:

```text
consequence does not bind
runtime resolves to REFUSE, HALT, REDIRECT, or ESCALATE
```

---

## Governing invariant

> **No consequence persists without admissibility under current state.**

If admissibility fails at any point:

- continuation stops
- consequence does not bind
- prior state remains authoritative

---

## Interpretation

A system can be:

- correct
- authenticated
- policy-aligned
- workflow-complete

and still fail consequence admissibility.

Elyria enforces that distinction at the moment of execution.

---

## Execution boundary

```text
Proposed Action
      ↓
Admissibility Resolution
(Φ, A, U, V, B, H)
      ↓
┌───────────────┬───────────────┬───────────────┐
│   EXECUTE     │    REFUSE     │     HALT      │
│ binds         │ no bind       │ stops         │
└───────────────┴───────────────┴───────────────┘
      ↓
Decision Receipt
      ↓
Replay must reproduce decision
```

---

## Runtime outcomes

| Outcome | Meaning |
|---|---|
| **EXECUTE** | lawful support holds; consequence may bind |
| **REFUSE** | attempted consequence lacks standing |
| **HALT** | continuation stops because support, safety, viability, or breach condition failed |
| **REDIRECT** | intent may continue only through a different lawful corridor |
| **ESCALATE** | authorized review required before effect |
| **REBOUND** | unsupported pressure returns; motion cannot continue forward |
| **RESTART** | lawful re-entry after judged halt / recovery condition |

---

## Public proof surface

This repository shows:

- category framing
- public runtime-law vocabulary
- consequence-admission semantics
- runtime outcome morphology
- receipt / replay direction
- protected-scope boundaries

This repository does **not** include:

- production source code
- production protected-action adapters
- client corridors
- corridor evaluators
- private policy structures
- protected schemas
- receipt-generation internals
- replay-verification internals
- deployment substrate

---

## Proof claim

A valid request can still fail consequence admissibility.

```text
REFUSE = no execution
HALT   = no continuation
```

This system prevents effect.  
It does not merely observe it.

Replay principle:

```text
same request + same state + same policy + same corridor = same decision receipt
```

The protected implementation proving this behavior is retained outside the public proof surface.

---

## Production enforcement direction

The production target is consequence-binding enforcement:

```text
No protected action reaches effect unless the governed boundary resolves EXECUTE.
```

See [`docs/PRODUCTION_ENFORCEMENT_FABRIC.md`](./docs/PRODUCTION_ENFORCEMENT_FABRIC.md) for the production build direction.

---

## Protected scope

This repository is publicly visible for evaluation of the concept, category, and proof framing only.

It does not grant rights to reuse, reproduce, modify, deploy, or derive commercial systems.

No internal decision logic, production policy structures, client corridors, examples, tests, schemas, source code, replay internals, or protected runtime substrate are licensed through this repository.

See [`LICENSE`](./LICENSE) for full restrictions.

---

<div align="center">

## Core sentence

**Most systems decide whether something may run.**  
**Elyria determines whether continuation is lawful enough to become consequence.**

<br />

**Authority to enter is not authority to remain.**

<br />

**ELYRIA SYSTEMS — VA**  
**Samantha Revita · Terry Snyder**

</div>
