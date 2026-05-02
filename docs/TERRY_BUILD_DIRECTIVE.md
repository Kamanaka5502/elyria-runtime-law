# Terry Build Directive — Elyria Runtime Law v0.1

## Product

```text
Elyria Continuum
Powered by Elyria Runtime Law
```

## First implementation

Build the runtime substrate with three corridors:

```text
cyber_privileged_action_v0
chemistry_transformation_v0
bio_recovery_plan_v0
```

## Rule

Boundary gates are not the product.  
They are local enforcement surfaces inside Runtime Law.

## Required proof

Every evaluation must produce:

```text
decision
morphology
consequence_binds
signature vector
blocking facts
receipt hash
replay token
replay verification
```

## Acceptance

The package is acceptable if:

```text
pytest -q passes
uvicorn app.main:app --reload --port 8001 starts
POST /runtime/evaluate returns deterministic decisions
POST /receipt/replay verifies prior receipt
Chemistry and Bio are corridorized, not treated as separate governing systems
```
