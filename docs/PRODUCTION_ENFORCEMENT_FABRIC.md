# Production Consequence-Binding Enforcement Fabric

## Build Sheet for Sam v1

This document upgrades the current Elyria Runtime Law scaffold from a controlled proof slice into the production enforcement target.

The current repository proves:

```text
evaluate → decision → receipt → replay
```

The production fabric must enforce:

```text
protected action → boundary resolution → physical consequence prevention unless EXECUTE
```

The proof corridor is not the architecture. The proof corridor is the inspection slice cut out of the production enforcement fabric.

---

## 1. Non-negotiable runtime law

```text
EXECUTE is the only decision that allows consequence to bind.
REFUSE physically prevents the protected action from reaching effect.
ESCALATE prevents consequence until ambiguity is resolved.
HALT stops corridor continuation when enforcement integrity, visibility, or carryability collapses.
Every boundary decision emits a receipt and supports deterministic replay.
No local layer can bypass the boundary and still bind consequence.
```

If `REFUSE` can be bypassed, if receipt cannot replay, or if a local layer can bind consequence without the boundary, the build fails.

---

## 2. Production architecture

The production fabric is an on-path boundary that resolves whether a protected action may bind consequence.

| Module | Production function |
|---|---|
| Boundary | Deterministic `EXECUTE / REFUSE / ESCALATE / HALT` resolution |
| Corridor | Registers action class, protected route, state, context, and proof rules |
| Authority | Validates standing, delegation, revocation, and current right-to-bind |
| Evidence | Checks freshness, custody, trace, and admissibility basis |
| Carryability | Determines whether the state remains supportable under live burden |
| Enforcement | Physically prevents effect unless outcome is `EXECUTE` |
| Receipt | Emits proof-bearing receipt for every boundary decision |
| Replay | Reproduces outcome under same canonical input and governing basis |
| Ledger | Append-only receipt chain with tamper detection |

Primary outcome set:

```text
EXECUTE | REFUSE | ESCALATE | HALT
```

Optional expansion:

```text
REDIRECT | REBOUND | REVOKE
```

Keep v1 strict unless a corridor requires the broader grammar.

---

## 3. Canonical execution envelope

Every protected action enters through a single canonical envelope. No ad hoc execution path, callback, queue, worker, agent, or local layer may bind consequence outside the boundary.

Required envelope fields:

```text
execution_intent_id
corridor_id
protected_action
effect_class
actor identity
actor type
authority reference
delegation status
revocation status
policy id
policy hash
policy version lock
evidence id
evidence hash
freshness
custody status
state id
state hash
environment
visibility
admissibility scope
standing
context
capacity
burden
phi
continuation viability
request time
nonce
canonical input hash
```

---

## 4. Decision precedence

```text
1. Enforcement integrity failure → HALT
2. Corridor halted → HALT
3. Missing required state visibility → ESCALATE or HALT
4. Invalid / revoked authority → REFUSE
5. Policy mismatch → REFUSE
6. Stale evidence or broken custody → REFUSE
7. Standing / admissibility failure → REFUSE
8. Carryability failure → HALT or REFUSE
9. Replay / nonce integrity failure → REFUSE
10. All conditions resolved → EXECUTE
```

---

## 5. Production corridors

Each product corridor is a bounded commercial surface of the same production enforcement fabric. Corridors differ by protected action and evidence class, not by runtime law.

| Corridor | Protected consequence |
|---|---|
| Cloudflare / Saudi Placement | Production-impacting API/action request before effect |
| Financial Action Guard | Payment, transfer, approval, drawdown, limit, release |
| SafeChange | Production or operational change before apply/revert boundary |
| StandingGrid | Standing basis across authority, evidence, custody, scope, continuity |
| Ad Fraud Protect | Ad spend, campaign action, attribution, invoice, payout |

Shared proof pattern:

```text
valid state → EXECUTE → consequence binds → receipt → replay
invalid state → REFUSE → physical prevention → receipt → replay
degraded / ambiguous state → ESCALATE or HALT → no consequence bind → receipt → replay
tamper attempt → replay mismatch → HALT_REVIEW_REQUIRED
bypass attempt → blocked → no effect
```

---

## 6. Ad Fraud Protect corridor

Buyer-readable rule:

```text
No valid standing = no ad spend execution.
```

Ad Fraud Protect prevents ad spend or downstream payout from binding unless the traffic, placement, attribution, budget authority, and fraud evidence still have standing at the moment of execution.

Protected actions:

```text
campaign launch
budget increase or spend release
bid change or audience expansion
creative approval
publisher / placement approval
conversion attribution acceptance
invoice approval
payout to traffic source or affiliate
```

Boundary question:

```text
Does this ad-spend action still have standing under live fraud, authority, evidence, placement, attribution, and budget conditions?
```

Failure model:

Traditional fraud systems often detect after spend. This corridor prevents invalid spend from becoming consequence before money, inventory, attribution, invoice, or payout binds.

Proof cases:

| Case | Expected result |
|---|---|
| Valid campaign spend | `EXECUTE` — spend/action proceeds — receipt — replay |
| Bot / fraud traffic source | `REFUSE` — no spend release — receipt — replay |
| Invalid attribution claim | `REFUSE` or `ESCALATE` — payout does not bind |
| Brand-unsafe placement | `REFUSE` — placement/action blocked before spend |
| Uncertain evidence | `ESCALATE` — no consequence bind pending review |
| Fraud / carryability collapse | `HALT` — corridor stopped — receipt — replay |

Ad Fraud Protect receipt additions:

```text
traffic_source_id
placement_id
campaign_id
budget_authority_id
fraud_signal_hash
attribution_evidence_hash
placement_safety_hash
spend_amount_requested
spend_amount_bound
invoice_or_payout_reference
standing_result
fraud_result
attribution_result
budget_result
physical_prevention_confirmed for REFUSE / ESCALATE / HALT
```

Commercial line:

```text
Detection after fraud is not protection. Protection means invalid spend never binds.
```

---

## 7. Production hardening requirements

```text
Atomic enforcement
Boundary decision, receipt emission, ledger append, and action dispatch must be transactionally bound or fail closed.

Bypass guard
Protected actions cannot be invoked directly by local services, workers, agents, queues, or callbacks.

No async leakage
Queued or delayed downstream actions must carry EXECUTE receipt reference or be refused.

Partial visibility discipline
Missing required state/evidence produces ESCALATE or HALT, never assumed continuity.

Concurrency discipline
Competing transitions over the same state must re-resolve; stale validity cannot carry forward.

Tamper evidence
Receipt, policy, evidence, state, and carryability hashes must break replay on modification.

Corridor halt semantics
Enforcement integrity failure or carryability collapse stops the corridor, not just the action.

Commercial proof slice
Show one narrow corridor, but only after production enforcement is in place.
```

---

## 8. Delivery package requirements

Finished package must include:

```text
production enforcement code
schemas and canonicalization rules
corridor registry and corridor configs
policy and evidence fixtures
protected action adapters
receipt examples and receipt-chain verification
replay examples and replay verifier
tamper tests
bypass tests
concurrency tests
partial-visibility tests
Cloudflare / Saudi proof slice
Financial Action Guard proof slice
Ad Fraud Protect proof slice
deployment instructions
review checklist
```

---

## 9. Internal statement

```text
We are building the full production enforcement fabric. The proof corridor is only the inspection slice.
```

## 10. External statement after build

```text
This is not a demo. It is production consequence-binding enforcement with controlled proof corridors showing EXECUTE, REFUSE, ESCALATE/HALT, physical prevention, receipt, and replay.
```

---

## 11. v0.2 implementation path

The current repo remains the v0.1 proof scaffold. Production fabric work should proceed as v0.2.

Build order:

```text
1. canonical envelope
2. corridor registry
3. protected action adapter interface
4. enforcement dispatcher
5. bypass guard
6. append-only receipt ledger
7. Ad Fraud Protect corridor
8. tamper / replay / bypass tests
9. concurrency and partial-visibility tests
10. production review checklist
```

---

## 12. Category protection

Do not describe this as:

```text
a demo
an authorization layer
an approval workflow
an audit tool
a control dashboard
policy monitoring
```

Correct description:

```text
Production consequence-binding enforcement: protected actions cannot reach effect unless the governed boundary resolves EXECUTE.
```
