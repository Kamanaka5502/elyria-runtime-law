# Elyria Runtime Law v0.1 — Demo Script

## Purpose

This demo proves the core category:

```text
Most systems decide whether something may run.
Elyria determines whether continuation is lawful enough to become consequence.
```

The demo should not be presented as ordinary authorization, workflow approval, or AI governance.

The proof object is attempted becoming: a proposed transition pressing toward consequence.

---

## Start the runtime

```bash
uvicorn app.main:app --reload --port 8001
```

Health check:

```bash
curl -s http://127.0.0.1:8001/healthz
```

Expected:

```json
{"status":"ok"}
```

---

## Demo 1 — EXECUTE

### Claim

Lawful support holds. Consequence may bind.

### Command

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/cyber_execute.json | python -m json.tool
```

### What to point out

```text
decision = EXECUTE
consequence_binds = true
receipt_hash is present
replay_token is present
```

### Meaning

The action is not merely authenticated. It survives authority, evidence, state, capacity, continuity, and policy support.

---

## Demo 2 — REFUSE

### Claim

Authentication is not standing.

### Command

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/cyber_refuse_authority.json | python -m json.tool
```

### What to point out

```text
decision = REFUSE
consequence_binds = false
authority = FAIL
blocking_facts includes missing authority scope
```

### Meaning

The actor can be known and the request can be structured, but the attempted consequence lacks standing.

### Demo sentence

```text
Elyria does not ask only who you are. It asks whether this consequence has lawful standing now.
```

---

## Demo 3 — REDIRECT

### Claim

Non-execution is not one thing.

### Command

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/cyber_redirect.json | python -m json.tool
```

### What to point out

```text
decision = REDIRECT
consequence_binds = false for the original path
redirect_candidate is present
```

### Meaning

The original path fails, but intent may continue only through a different lawful corridor.

### Demo sentence

```text
A failed path does not automatically mean denial. If lawful transport exists, Elyria redirects instead of pretending the original path is safe.
```

---

## Demo 4 — HALT

### Claim

Hard guard failure prevents consequence from binding.

### Command

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/chemistry_halt_guard.json | python -m json.tool
```

### What to point out

```text
decision = HALT
consequence_binds = false
breach = FAIL
blocking_facts include energy_conserved
```

### Meaning

The chemistry corridor is not a separate product. It is a domain corridor under Elyria Runtime Law. Domain guards become admissibility conditions.

### Demo sentence

```text
A transformation cannot become admitted if the guard structure says the consequence would breach conservation or support.
```

---

## Demo 5 — ESCALATE

### Claim

Unresolved safety review fails closed.

### Command

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/bio_escalate_safety.json | python -m json.tool
```

### What to point out

```text
decision = ESCALATE
consequence_binds = false
blocking_facts include safety_review_required=true and safety_review_complete=false
```

### Meaning

Biomedical plans are admitted only as governed review outputs, not treatment authorization. Safety uncertainty does not silently execute.

### Demo sentence

```text
Elyria treats unresolved safety review as a runtime condition, not a note for later.
```

---

## Replay proof

### Claim

The boundary did not improvise.

Evaluate any request, copy the returned `receipt`, then call:

```text
POST /receipt/replay
```

Replay rule:

```text
same request + same state + same policy + same corridor = same decision receipt
```

### Meaning

Replay proves deterministic boundary behavior under the same field.

---

## Full demo arc

Run in this order:

```text
1. EXECUTE  — lawful consequence may bind
2. REFUSE   — authentication is not standing
3. REDIRECT — failed path may move through a lawful corridor
4. HALT     — hard guard breach stops continuation
5. ESCALATE — unresolved safety review fails closed
6. REPLAY   — same field returns same decision
```

---

## Closing line

```text
Most systems govern actors, actions, or outputs.
Elyria governs continuation.
```

Stronger close:

```text
Authority to enter is not authority to remain.
```
