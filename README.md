<div align="center">

# Elyria Runtime Law v0.1

### Consequence admission before effect for AI and automated systems

![Elyria Runtime Law CI](https://github.com/Kamanaka5502/elyria-runtime-law/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
![License](https://img.shields.io/badge/license-proprietary-red)
![Status](https://img.shields.io/badge/status-proof%20surface-gold)

**Runtime law for consequence-bearing systems.**

Most systems govern actors, actions, or outputs.  
**Elyria governs continuation.**

</div>

---

## Core premise

The core object is not an action.

The core object is **attempted becoming**: a proposed transition pressing toward consequence.

A proposed action can be possible, requested, authenticated, predicted, or workflow-complete and still fail consequence admissibility.

> **Most systems decide whether something may run.**  
> **Elyria determines whether continuation is lawful enough to become consequence.**

---

## Category

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

## What this package contains

- FastAPI backend for Elyria Runtime Law v0.1
- Corridor evaluators for cyber, chemistry, and bio examples
- Deterministic receipt generation
- Replay verification endpoint
- Example JSON requests
- Unit tests
- CI validation for Python 3.11 and 3.12

---

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload --port 8001
```

---

## Proof

A valid request can still fail consequence admissibility.

```text
REFUSE = no execution
HALT   = no continuation
```

This system prevents effect.  
It does not merely observe it.

Replay rule:

```text
same request + same state + same policy + same corridor = same decision receipt
```

---

## Protected scope

This repository is a public proof surface.

It does not grant rights to reuse, reproduce, modify, deploy, or derive commercial systems.

No internal decision logic, production policy structures, client corridors, or protected runtime substrate are licensed through this repository.

See [`LICENSE.txt`](./LICENSE.txt) for full restrictions.

---

<div align="center">

## Core sentence

**Most systems decide whether something may run.**  
**Elyria determines whether continuation is lawful enough to become consequence.**

</div>
