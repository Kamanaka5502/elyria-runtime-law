from __future__ import annotations

from app.corridors import evaluate_corridor
from app.models import BoundaryResult, RuntimeRequest, RuntimeResponse
from app.receipts import make_receipt


def boundary_result_from_signature(req: RuntimeRequest, draft) -> BoundaryResult:
    sig = draft.signature
    return BoundaryResult(
        authority="PASS" if sig.authority_U == 1 else "FAIL",
        evidence="PASS" if req.evidence.freshness_seconds <= req.evidence.max_age_seconds and req.evidence.custody_hash else "FAIL",
        state="PASS" if req.current_state.revocation_status == "clear" and req.current_state.drift_status in {"none", "minor"} else "FAIL",
        capacity="PASS" if sig.phi >= req.capacity.minimum_required_phi else "FAIL",
        viability="PASS" if sig.viability_V >= 0 else "FAIL",
        breach="PASS" if sig.breach_B == 0 else "FAIL",
        restart="PASS" if sig.restart_R == 1 else "ABSENT",
        coherence="PASS" if sig.coherence_H >= sig.h_min else "FAIL",
        policy_integrity="PASS" if req.current_state.policy_version else "FAIL",
    )


def evaluate(req: RuntimeRequest) -> RuntimeResponse:
    draft = evaluate_corridor(req)
    consequence_binds = draft.decision.value == "EXECUTE"

    receipt = make_receipt(
        req=req,
        decision=draft.decision,
        reason=draft.reason,
        rule_trace=draft.rule_trace,
        blocking_facts=draft.blocking_facts,
    )

    return RuntimeResponse(
        decision=draft.decision,
        morphology=draft.morphology,
        consequence_binds=consequence_binds,
        reason=draft.reason,
        corridor_id=req.continuity.corridor_id,
        signature=draft.signature,
        boundary_result=boundary_result_from_signature(req, draft),
        receipt=receipt,
        redirect_candidate=draft.redirect_candidate,
        missing_fields=draft.missing_fields,
    )
