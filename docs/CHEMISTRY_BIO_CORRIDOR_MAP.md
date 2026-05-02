# Chemistry / Bio Kernels → Elyria Corridors

This map keeps the Chemistry and Bio kernels cleanly inside Elyria Runtime Law.

They are **not** the whole Elyria system.  
They are **domain corridors**: constrained application surfaces where attempted becoming is evaluated before effect.

---

## Governing hierarchy

```text
Elyria Systems
  ↓
Elyria Continuum
  ↓
Elyria Runtime Law
  ↓
Runtime signature resolver
  ↓
Domain corridors
      - Cyber privileged action corridor
      - Chemistry transformation corridor
      - Bio recovery / biomedical plan corridor
  ↓
Receipts + replay witness
```

---

## Core rule

Every domain corridor must reduce its proposed action into the same runtime signature:

```text
Σ_C(x)=⟨Φ(x), A(x), U(x), V(x), B(x), R(x), H(x)⟩
```

Where:

| Term | Meaning | Domain mapping |
|---|---|---|
| Φ(x) | capacity minus burden | available margin minus projected load/risk |
| A(x) | admissibility | domain guard satisfaction |
| U(x) | authority | live scope, actor authority, permitted use |
| V(x) | viability | whether continuation can remain lawful |
| B(x) | breach pressure | unsafe / invalid / forbidden condition pressure |
| R(x) | restart path | rollback, containment, alternative route |
| H(x) | coherence | cross-field alignment and minimum support |

---

# Chemistry Kernel Corridor

## Domain purpose

Evaluate proposed chemical, quantum, or environmental transformations before treating them as allowable continuation.

## Chemistry kernel assets

The Chemistry Kernel contributes:

```text
Obligation lattice
Witnesses
Atoms
Edges
FIV metrics
Monotone closure
Guard registry
Energy conservation guard
Causality guard
Stoichiometry guard
Thermodynamic stability guard
Pauli exclusion guard
Ledger append behavior
```

## Corridor name

```text
chemistry_transformation_v0
```

## Attempted becoming

```text
proposed chemical/quantum composition, reaction, transformation, or closure
```

## Runtime mapping

| Chemistry object | Elyria runtime term |
|---|---|
| Atom | state component |
| Edge | relation / transition support |
| Obligation lattice | proof obligation level |
| Witness | authority / certification support |
| Guard | admissibility check |
| FIV.MonotoneOK | monotone continuation condition |
| FIV.EntropyBudget | burden / thermodynamic margin |
| FIV.CausalityMet | breach prevention |
| FIV.CurvatureRisk | instability / boundary pressure |
| monotoneClosure | guarded continuation attempt |
| Ledger | receipt substrate |

## Chemistry outcome rules

```text
IF authority scope is not chemistry_transform
→ REFUSE

IF energy conservation fails
→ HALT

IF causality fails
→ HALT

IF stoichiometry fails
→ HALT or ESCALATE

IF thermodynamic stability fails
→ REDIRECT if alternative_path exists, else HALT

IF Pauli exclusion fails
→ HALT

IF monotonicity fails or curvature risk exceeds threshold
→ HALT

IF all guards pass and Φ≥0 and coherence holds
→ EXECUTE
```

## Chemistry public-safe product language

```text
Elyria can evaluate proposed chemical or quantum transformations as consequence-bearing transitions, requiring energy, causality, stoichiometry, thermodynamic, quantum, authority, and viability support before the transformation is admitted.
```

## Protected internal language

Do not publicly expose the full guard structure, advanced thermo mappings, or proprietary proof/closure logic.

---

# Bio Kernel Corridor

## Domain purpose

Evaluate biomedical diagnostic/recovery plans before treating them as consequence-bearing recommendations or actions.

## Bio kernel assets

The Bio-K2 kernel contributes:

```text
BioProfile
Genome/anomaly analysis
Recovery goals
RegenerativePrint blueprint
InstructionEngine protocol compilation
BioRepairLoop
Aging/rejuvenation module
NeuroBridge
Simulation output
```

## Corridor name

```text
bio_recovery_plan_v0
```

## Attempted becoming

```text
proposed biomedical recovery, regenerative, diagnostic, neuro, aging, or repair-loop plan
```

## Runtime mapping

| Bio object | Elyria runtime term |
|---|---|
| BioProfile | patient state |
| condition_tags | risk / domain context |
| anomalies | evidence field |
| recovery_goals | intended consequence |
| RegenerativePrint | proposed consequence blueprint |
| InstructionEngine | protocol compiler |
| BioRepairLoop | consequence simulation |
| success_score | projected viability signal |
| goals_met | limited simulated outcome |
| clinician / researcher role | authority |
| safety_review | escalation condition |
| restart_protocol | rollback / restart path |

## Bio outcome rules

```text
IF authority scope is not biomedical_review
→ REFUSE

IF patient/evidence freshness fails
→ HALT

IF safety review is required and missing
→ ESCALATE

IF burden/risk exceeds capacity
→ HALT

IF viability score is below threshold
→ REDIRECT if alternative_plan exists, else HALT

IF domain is experimental and no controlled corridor exists
→ ESCALATE

IF all required support holds
→ EXECUTE as plan_review_approved, not treatment authorization
```

## Important boundary

Bio-K2 v0.1 must not present itself as medical advice, diagnosis, or treatment.  
It is a **simulation and admissibility-review corridor** for biomedical plan governance.

Public-safe wording:

```text
Elyria can evaluate whether a biomedical recommendation, recovery plan, or research protocol has sufficient authority, evidence freshness, safety review, viability, and restart support before it is allowed to proceed as a governed recommendation.
```

---

# Why this is not messy

Chemistry and Bio are not separate products yet.

They are:

```text
domain corridors under Elyria Runtime Law
```

Each corridor must:

1. Convert domain payload into the shared consequence signature.
2. Evaluate authority, evidence, capacity, viability, breach, restart, and coherence.
3. Return a morphology outcome.
4. Issue a deterministic receipt.
5. Replay under the same state and law.

The product remains Elyria Continuum / Elyria Runtime Law.  
Chemistry and Bio are proof-bearing corridors.
