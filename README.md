# Elyria Runtime Law v0.1

[![Elyria Runtime Law CI](https://github.com/Kamanaka5502/elyria-runtime-law/actions/workflows/ci.yml/badge.svg)](https://github.com/Kamanaka5502/elyria-runtime-law/actions/workflows/ci.yml)

**Consequence admission before effect for AI and automated systems.**

Elyria Runtime Law evaluates whether a proposed consequence is admissible under live state, and determines whether it is allowed to bind.

If conditions do not resolve, the consequence does not occur.

This system does not govern actors, workflows, or outputs.

It governs whether continuation is lawful enough to become consequence.

---

## Core Invariant

```text
No consequence is allowed to bind unless admissibility resolves at the moment of execution under current state.

What is not admissible does not become consequence.
```

---

## Category

```text
Consequence admission before effect.
```

Elyria Runtime Law evaluates whether a proposed consequence may enter, remain, redirect, halt, restart, or bind under live state.

This is not:

```text
AI governance
execution control
authorization
workflow
audit
compliance dashboard
```

Those layers may provide inputs. They do not decide whether continuation remains lawful enough to become consequence.

---

## Runtime binding law

```text
Σ_C(x)=⟨Φ(x), A(x), U(x), V(x), B(x), R(x), H(x)⟩

Φ(x)=C(x)-M(x)

Bind ⇔ Φ≥0 ∧ A≥0 ∧ U=1 ∧ x∈Viab(R) ∧ B=0 ∧ H≥H_min
```

---

## Runtime outcomes

```text
EXECUTE  — lawful support holds; consequence may bind.
REFUSE   — attempted consequence lacks standing.
HALT     — continuation stops because support, safety, viability, or breach condition failed.
REDIRECT — intent may continue only through a different lawful corridor.
ESCALATE — authorized review required before effect.
REBOUND  — unsupported pressure returns / reseats; motion cannot continue forward.
RESTART  — lawful re-entry after judged halt/recovery condition.
```

---

## What this package contains

- FastAPI backend for Elyria Runtime Law v0.1
- Cyber, Chemistry, and Bio corridor evaluators
- Consequence-signature evaluation
- Morphology outcomes beyond allow/deny
- Deterministic receipt generation
- Replay verification endpoint
- Example JSON requests
- Unit tests
- Chemistry/Bio corridor map

---

## Corridors included

```text
cyber_privileged_action_v0
chemistry_transformation_v0
bio_recovery_plan_v0
```

Chemistry and Bio are implemented as **domain corridors** under Elyria Runtime Law. They are not separate governing systems and not separate products in this scaffold.

---

## Replay verification

```text
same request + same state + same policy + same corridor = same decision receipt
```

---

## Commercial Expression

**One-Corridor Governed Execution Pilot**

A controlled deployment of Elyria Runtime Law over a single high-risk action class, where consequence is admitted or refused at the execution boundary with deterministic proof and replay.

Contact required for evaluation, deployment, or licensing.

---

## Core sentence

```text
Most systems decide whether something may run.
Elyria determines whether continuation is lawful enough to become consequence.
```
