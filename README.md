# Elyria Runtime Law v0.1

![Elyria Runtime Law CI](https://github.com/Kamanaka5502/elyria-runtime-law/actions/workflows/ci.yml/badge.svg)

**Runtime law for consequence-bearing systems.**

Most systems govern actors, actions, or outputs.  
**Elyria governs continuation.**

The core object is not an action.  
The core object is attempted becoming: a proposed transition pressing toward consequence.

A proposed action can be possible, requested, authenticated, predicted, or workflow-complete and still fail consequence admissibility.

---

## Category

Consequence admission before effect.

Elyria Runtime Law evaluates whether a proposed consequence may enter, remain, redirect, halt, restart, or bind under live state.

This is not:

- AI governance
- execution control
- authorization
- workflow
- audit
- compliance dashboard

Those layers may provide inputs.  
They do not decide whether continuation remains lawful enough to become consequence.

---

## Runtime outcomes

EXECUTE — lawful support holds; consequence may bind.  
REFUSE — attempted consequence lacks standing.  
HALT — continuation stops because support, safety, viability, or breach condition failed.  
REDIRECT — intent may continue only through a different lawful corridor.  
ESCALATE — authorized review required before effect.  
REBOUND — unsupported pressure returns; motion cannot continue forward.  
RESTART — lawful re-entry after judged halt/recovery condition.

---

## What this package contains

- FastAPI backend for Elyria Runtime Law v0.1
- Corridor evaluators (cyber / chemistry / bio)
- Deterministic receipt generation
- Replay verification endpoint
- Example JSON requests
- Unit tests

---

## Run

python -m venv .venv  
source .venv/bin/activate  
pip install -e ".[dev]"  
uvicorn app.main:app --reload --port 8001  

---

## Proof

A valid request can still fail consequence admissibility.

REFUSE = no execution  
HALT = no continuation  

This system prevents effect. It does not observe it.

---

## License

Evaluation only. No reuse or derivative rights.

---

## Core sentence

Most systems decide whether something may run.  
Elyria determines whether continuation is lawful enough to become consequence.

---

## Runtime binding law

Elyria evaluates consequence admissibility as a constrained state resolution:

Σ_C(x) = ⟨Φ(x), A(x), U(x), V(x), B(x), R(x), H(x)⟩

Where:

Φ(x) = C(x) − M(x)  
(capacity minus burden)

A(x) = authority validity  
U(x) = authorization state (binary)  
V(x) ∈ Viab(R) (viability within regime constraints)  
B(x) = breach condition (must be 0)  
H(x) = continuity / coherence threshold  

---

## Binding condition

A consequence may bind only if:

Φ ≥ 0 ∧ A ≥ 0 ∧ U = 1 ∧ x ∈ Viab(R) ∧ B = 0 ∧ H ≥ H_min

If any condition fails:

→ consequence does not bind  
→ runtime resolves to REFUSE, HALT, REDIRECT, or ESCALATE  

---

## Interpretation

A system can be:

- correct  
- authenticated  
- policy-aligned  

and still fail consequence admissibility.

Elyria enforces that distinction at the moment of execution.


---

## Governing invariant

No consequence persists without admissibility under current state.

If admissibility fails at any point:

→ continuation stops  
→ consequence does not bind  
→ prior state remains authoritative  


---

## Execution boundary (conceptual)

Proposed Action  
      ↓  
Admissibility Resolution (Φ, A, U, V, B, H)  
      ↓  
┌───────────────┬───────────────┬───────────────┐  
│   EXECUTE     │    REFUSE     │     HALT      │  
│ binds         │ no bind       │ stops         │  
└───────────────┴───────────────┴───────────────┘  
      ↓  
Receipt  
      ↓  
Replay (must reproduce decision)

