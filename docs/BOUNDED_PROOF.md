# Elyria Runtime Law v0.1 — Bounded Proof Statement

## Purpose

This document states the bounded proof carried by the public Elyria Runtime Law v0.1 surface.

It does not claim universal production completeness.
It does not claim unrestricted runtime enforcement.
It does not expose protected substrate logic.

It states the bounded proof that this repository establishes:

```text
A proposed action can be authenticated, structured, and technically executable while still failing consequence admissibility.

Within the v0.1 proof surface, Elyria resolves that distinction before bind, emits a receipt, and supports deterministic replay.
```

---

## Category proven

Most systems prove one of the following:

```text
actor authenticated
action authorized
workflow completed
output generated
policy checked
audit recorded
```

Elyria v0.1 proves a different category:

```text
consequence admission before effect
```

The controlled proof object is not an action.

The controlled proof object is:

```text
attempted becoming — a proposed transition pressing toward consequence
```

---

## Bounded proof claim

Within the scoped v0.1 runtime surface, Elyria proves:

```text
Given the same request, same state, same corridor, and same governing policy,
the runtime resolves the same consequence decision and produces the same replay-verifiable receipt.
```

And:

```text
Only EXECUTE may bind consequence.
REFUSE, HALT, REDIRECT, and ESCALATE do not bind the original consequence.
```

This is the bounded proof.

---

## Formal resolution structure

The runtime evaluates a public consequence signature:

```text
Σ_C(x) = ⟨Φ(x), A(x), U(x), V(x), B(x), R(x), H(x)⟩
```

Where:

| Term | Runtime role |
|---|---|
| `Φ(x)` | capacity minus burden |
| `A(x)` | admissibility / authority basis |
| `U(x)` | standing / authorization state |
| `V(x)` | viability of continuation |
| `B(x)` | breach pressure / breach condition |
| `R(x)` | restart or lawful recovery path |
| `H(x)` | coherence / support threshold |

The public binding condition is:

```text
Bind ⇔ Φ ≥ 0 ∧ A ≥ 0 ∧ U = 1 ∧ x ∈ Viab(R) ∧ B = 0 ∧ H ≥ H_min
```

If the binding condition does not hold, the original consequence does not bind.

---

## What the proof demonstrates

### 1. Authentication is not standing

A known actor can still fail consequence admissibility.

Proof class:

```text
cyber_refuse_authority.json → REFUSE
```

Meaning:

```text
identity and request structure are insufficient if authority / standing does not resolve.
```

---

### 2. Non-execution is not one thing

A failed path does not collapse into a flat deny.

Proof class:

```text
cyber_redirect.json → REDIRECT
```

Meaning:

```text
The original path does not bind, but a lawful corridor may be offered.
```

This proves boundary morphology beyond binary allow/deny.

---

### 3. Domain guards can become admissibility conditions

A chemistry transformation may be structurally proposed but halted when a hard guard fails.

Proof class:

```text
chemistry_halt_guard.json → HALT
```

Meaning:

```text
domain validity is not commentary; it can become a runtime condition for consequence admission.
```

---

### 4. Safety uncertainty fails closed

A biomedical review path with unresolved safety review does not silently proceed.

Proof class:

```text
bio_escalate_safety.json → ESCALATE
```

Meaning:

```text
uncertainty is not treated as permission.
```

---

### 5. Lawful support can bind

When authority, evidence, state, capacity, continuity, and policy support hold, the runtime can resolve EXECUTE.

Proof class:

```text
cyber_execute.json → EXECUTE
```

Meaning:

```text
EXECUTE is not default permission; it is an admitted outcome.
```

---

### 6. Replay verifies the boundary did not improvise

Proof class:

```text
same request + same state + same policy + same corridor = same receipt-verifiable decision
```

Meaning:

```text
The runtime decision is replayable under the same canonical input and governing basis.
```

---

## What most systems do not prove

Most execution-control systems can show:

```text
who requested
what was requested
which policy was checked
whether the action was allowed
what happened afterward
```

Elyria v0.1 proves the more specific boundary distinction:

```text
whether the proposed consequence is admitted to bind before effect
```

That is not the same as authorization.
That is not the same as audit.
That is not the same as governance review.

---

## Proof boundary

This v0.1 public proof surface proves the decision-resolution and replay structure.

It does not yet claim public production enforcement of:

```text
physical prevention
protected action adapters
atomic dispatch
bypass guard
queued-action enforcement
append-only production ledger
concurrency lockout
partial-visibility halt semantics
client-specific corridor policy
```

Those are v0.2 production enforcement requirements documented in:

```text
docs/PRODUCTION_ENFORCEMENT_FABRIC.md
```

This distinction matters.

The v0.1 proof shows consequence-admission resolution.
The v0.2 production target adds physical consequence-binding enforcement.

---

## Why the proof is bounded and strong

A weak proof overclaims.

A strong proof states its boundary.

Elyria v0.1 proves:

```text
1. proposed consequence is evaluated before bind
2. EXECUTE is not default
3. REFUSE / HALT / REDIRECT / ESCALATE are distinct morphologies
4. every decision emits receipt material
5. replay verifies deterministic boundary behavior under the same field
6. corridor-specific logic maps domain conditions into consequence admissibility
```

This is enough to demonstrate the category break.

---

## Undeniable sentence

```text
Most systems prove an action was allowed or recorded.

Elyria proves whether the consequence was admitted to bind.
```

Stronger:

```text
Authority to enter is not authority to remain.
```

Strongest:

```text
Execution is not assumed.
It is admitted.
```

---

## Acceptance condition

The proof fails if any of the following occur:

```text
REFUSE binds consequence
HALT continues consequence
REDIRECT binds the original failed path
ESCALATE proceeds without resolution
receipt cannot replay under the same field
same request/state/policy/corridor produces inconsistent decision
binary allow/deny collapses morphology
```

The proof holds only where those failure modes are prevented inside the bounded v0.1 surface.

---

## Closing

This repository does not ask a buyer to believe a slogan.

It shows a bounded category proof:

```text
proposed consequence
→ admissibility resolution
→ morphology outcome
→ receipt
→ replay
```

That is the proof surface.

The production enforcement fabric extends this into:

```text
protected action
→ governed boundary
→ physical prevention unless EXECUTE
→ receipt
→ replay
```

The distinction is the product path.
