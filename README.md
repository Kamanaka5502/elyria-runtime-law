# Elyria Runtime Law v0.1

Consequence admission before effect for AI and automated systems.

This repository is a proof surface for Elyria Runtime Law.

It demonstrates how a proposed action is evaluated at the moment of execution to determine whether it is allowed to become real.

If conditions do not resolve, the action does not occur.

---

## Category

This is not:

- AI governance
- authorization
- workflow control
- monitoring
- fraud detection
- compliance tooling

Those systems provide inputs.

They do not determine whether consequence binds.

---

## What Elyria Does

Elyria Runtime Law evaluates:

- authority
- evidence
- state
- capacity
- viability
- breach conditions
- continuation coherence

before allowing consequence to bind.

---

## Core Principle

A proposed action can be valid, approved, or complete
and still fail consequence admissibility.

If it fails, it does not become real.

---

## Runtime Binding

A consequence binds only when admissibility conditions resolve under live state.

If those conditions do not hold, the system returns:

- REFUSE   → action does not execute  
- HALT     → continuation stops  
- REDIRECT → alternate lawful corridor required  
- ESCALATE → authorized review required  

No downstream system receives committed effect unless binding is allowed.

---

## Enforcement

This system is not advisory.

- REFUSE = no execution  
- HALT = no continuation  
- REDIRECT = no forward motion without lawful path  

Execution is prevented, not observed.

---

## Proof Surface

This repository demonstrates:

- deterministic decision outcomes  
- receipt generation  
- replay verification  
- corridor-based evaluation  

Replay rule:

same request + same state + same policy + same corridor = same decision

---

## Architecture (High-Level)

Input → Runtime Law → Decision → Receipt → Replay

No internal decision logic, formulas, or policy structures are exposed.

---

## License

This repository is provided for evaluation only.

No rights to use, reproduce, modify, deploy, or derive commercial systems are granted without written authorization.

See LICENSE.txt for full restrictions.

---

## Core Sentence

Most systems decide whether something may run.

Elyria determines whether continuation is lawful enough to become consequence.
