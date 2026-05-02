# Elyria Runtime Law v0.1

[![Elyria Runtime Law CI](https://github.com/Kamanaka5502/elyria-runtime-law/actions/workflows/ci.yml/badge.svg)](https://github.com/Kamanaka5502/elyria-runtime-law/actions/workflows/ci.yml)

**Runtime law for consequence-bearing systems.**

Most systems govern actors, actions, or outputs.  
**Elyria governs continuation.**

The core object is not an action.  
The core object is **attempted becoming**: a proposed transition pressing toward consequence.

A proposed action can be possible, requested, authenticated, predicted, or workflow-complete and still fail consequence admissibility.

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

## Runtime binding law

```text
Σ_C(x)=⟨Φ(x), A(x), U(x), V(x), B(x), R(x), H(x)⟩

Φ(x)=C(x)-M(x)

Bind ⇔ Φ≥0 ∧ A≥0 ∧ U=1 ∧ x∈Viab(R) ∧ B=0 ∧ H≥H_min
```

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

## Corridors included

```text
cyber_privileged_action_v0
chemistry_transformation_v0
bio_recovery_plan_v0
```

Chemistry and Bio are implemented as **domain corridors** under Elyria Runtime Law. They are not separate governing systems and not separate products in this scaffold.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload --port 8001
```

## Demo calls

### EXECUTE — lawful privileged action

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/cyber_execute.json | python -m json.tool
```

Expected:

```text
decision: EXECUTE
consequence_binds: true
```

### REFUSE — authenticated actor lacks standing

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/cyber_refuse_authority.json | python -m json.tool
```

Expected:

```text
decision: REFUSE
consequence_binds: false
```

### REDIRECT — original path fails but lawful corridor exists

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/cyber_redirect.json | python -m json.tool
```

Expected:

```text
decision: REDIRECT
redirect_candidate: present
```

### HALT — chemistry hard guard failure

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/chemistry_halt_guard.json | python -m json.tool
```

Expected:

```text
decision: HALT
consequence_binds: false
```

### ESCALATE — biomedical safety review required

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/bio_escalate_safety.json | python -m json.tool
```

Expected:

```text
decision: ESCALATE
consequence_binds: false
```

## Replay verification

Evaluate a request, copy the returned `receipt`, then call:

```text
POST /receipt/replay
```

Replay rule:

```text
same request + same state + same policy + same corridor = same decision receipt
```

## Test

```bash
pytest -q
```

The GitHub Actions workflow validates on Python 3.11 and 3.12.

## Termux note

Termux may default to Python 3.13. FastAPI/Pydantic dependency installation can fail on Android because `pydantic-core` may require a Rust-backed build target not available through the local Termux environment.

That is an environment limitation, not a Runtime Law logic failure. Validate with Python 3.11 or 3.12, or use the included GitHub Actions workflow.

## Core sentence

```text
Most systems decide whether something may run.
Elyria determines whether continuation is lawful enough to become consequence.
```
