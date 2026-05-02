# Elyria Runtime Law v0.1

**Runtime law for consequence-bearing systems.**

Elyria does not govern actors, actions, or outputs as the primary object.  
Elyria governs continuation.

The core object is **attempted becoming**: a proposed transition pressing toward consequence.

A proposed action can be possible, requested, authenticated, predicted, or workflow-complete and still fail consequence admissibility.

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
- Receipt generation and replay verification
- Example JSON requests
- Unit tests
- Chemistry/Bio corridor map

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload --port 8001
```

## Example

```bash
curl -s -X POST http://127.0.0.1:8001/runtime/evaluate \
  -H "Content-Type: application/json" \
  -d @examples/cyber_execute.json | python -m json.tool
```

## Test

```bash
pytest -q
```
