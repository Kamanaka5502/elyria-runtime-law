from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from app.models import Corridor, RuntimeDecision, RuntimeRequest, SignatureVector


@dataclass
class EvalDraft:
    decision: RuntimeDecision
    morphology: str
    reason: str
    signature: SignatureVector
    rule_trace: List[str] = field(default_factory=list)
    blocking_facts: List[str] = field(default_factory=list)
    redirect_candidate: Optional[Dict[str, Any]] = None
    missing_fields: List[str] = field(default_factory=list)


def authority_ok(req: RuntimeRequest, required_scope: str) -> bool:
    return required_scope in req.actor.authority_scope


def evidence_fresh(req: RuntimeRequest) -> bool:
    return req.evidence.freshness_seconds <= req.evidence.max_age_seconds and bool(req.evidence.custody_hash)


def phi(req: RuntimeRequest) -> float:
    return req.capacity.C - req.capacity.M


def state_ok(req: RuntimeRequest) -> bool:
    return req.current_state.system_health.lower() in {"green", "yellow"} and req.current_state.revocation_status == "clear"


def base_signature(req: RuntimeRequest, authority: bool, admissible: bool, viable: bool, breach: bool, coherence: float) -> SignatureVector:
    computed_phi = phi(req)
    return SignatureVector(
        phi=computed_phi,
        admissibility_A=1.0 if admissible else -1.0,
        authority_U=1 if authority else 0,
        viability_V=1.0 if viable else -1.0,
        breach_B=1.0 if breach else 0.0,
        restart_R=1 if req.continuity.restart_available else 0,
        coherence_H=coherence,
    )


def eval_common_first(req: RuntimeRequest, required_scope: str) -> Optional[EvalDraft]:
    trace = ["authority_scope_check", "evidence_freshness_and_custody_check", "state_revocation_drift_check", "capacity_phi_check", "continuity_corridor_check"]

    if req.continuity.corridor_status != "open":
        sig = base_signature(req, True, False, False, True, 0.2)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="closed_corridor_halt",
            reason="Corridor is not open; continuation cannot bind.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=[f"corridor_status={req.continuity.corridor_status}"],
        )

    auth = authority_ok(req, required_scope)
    if not auth:
        sig = base_signature(req, False, False, True, False, 0.75)
        return EvalDraft(
            decision=RuntimeDecision.REFUSE,
            morphology="hard_lawful_boundary",
            reason=f"Actor authority does not include required scope: {required_scope}.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=[f"missing_authority_scope={required_scope}"],
        )

    if not evidence_fresh(req):
        sig = base_signature(req, True, False, False, True, 0.45)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="stale_or_uncustodied_evidence_halt",
            reason="Evidence is stale or lacks custody hash; consequence cannot bind.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=["evidence_stale_or_missing_custody_hash"],
        )

    if not state_ok(req) or req.current_state.drift_status not in {"none", "minor"}:
        sig = base_signature(req, True, False, False, True, 0.5)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="state_drift_halt",
            reason="Live state, revocation, or drift status does not support continuation.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=[
                f"system_health={req.current_state.system_health}",
                f"revocation_status={req.current_state.revocation_status}",
                f"drift_status={req.current_state.drift_status}",
            ],
        )

    if phi(req) < req.capacity.minimum_required_phi:
        sig = base_signature(req, True, False, False, True, 0.4)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="capacity_burden_halt",
            reason="Capacity minus burden is below required threshold.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=[f"phi={phi(req)} < required={req.capacity.minimum_required_phi}"],
        )

    return None


def eval_cyber(req: RuntimeRequest) -> EvalDraft:
    common = eval_common_first(req, "privileged_action")
    if common:
        return common

    payload = req.proposed_action.payload
    destructive = bool(payload.get("destructive", False))
    blast_radius = str(payload.get("blast_radius", "low")).lower()

    trace = [
        "authority_scope_check",
        "evidence_freshness_and_custody_check",
        "state_revocation_drift_check",
        "capacity_phi_check",
        "cyber_blast_radius_check",
        "cyber_restart_path_check",
    ]

    if destructive and not req.continuity.restart_available:
        sig = base_signature(req, True, False, False, True, 0.35)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="destructive_action_without_restart_halt",
            reason="Destructive privileged action lacks lawful restart or rollback path.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=["destructive=true", "restart_available=false"],
        )

    if blast_radius == "high" and req.continuity.alternative_path_available:
        sig = base_signature(req, True, False, True, False, 0.68)
        return EvalDraft(
            decision=RuntimeDecision.REDIRECT,
            morphology="reduced_blast_radius_redirect",
            reason="Original path exceeds corridor; reduced lawful path is available.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=["blast_radius=high"],
            redirect_candidate={"action_type": req.proposed_action.action_type, "blast_radius": "low", "requires_restart": req.continuity.restart_available},
        )

    sig = base_signature(req, True, True, True, False, 0.92)
    return EvalDraft(
        decision=RuntimeDecision.EXECUTE,
        morphology="lawful_continuation",
        reason="Privileged action satisfies authority, evidence, state, capacity, continuity, and policy support.",
        signature=sig,
        rule_trace=trace,
    )


def eval_chemistry(req: RuntimeRequest) -> EvalDraft:
    common = eval_common_first(req, "chemistry_transform")
    if common:
        return common

    p = req.proposed_action.payload
    required = ["energy_conserved", "causality_met", "stoichiometry_balanced", "thermodynamically_stable", "pauli_ok", "monotone_ok"]
    missing = [k for k in required if k not in p]
    trace = [
        "chem_energy_conservation_guard",
        "chem_causality_guard",
        "chem_stoichiometry_guard",
        "chem_thermodynamic_stability_guard",
        "quantum_pauli_exclusion_guard",
        "chem_monotone_closure_guard",
    ]

    if missing:
        sig = base_signature(req, True, False, False, False, 0.55)
        return EvalDraft(
            decision=RuntimeDecision.ESCALATE,
            morphology="missing_chemistry_guard_evidence",
            reason="Chemistry corridor lacks required guard evidence.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=[f"missing={','.join(missing)}"],
            missing_fields=missing,
        )

    hard_failures = []
    for k in ["energy_conserved", "causality_met", "pauli_ok", "monotone_ok"]:
        if not bool(p.get(k)):
            hard_failures.append(k)

    if hard_failures:
        sig = base_signature(req, True, False, False, True, 0.25)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="chemistry_hard_guard_halt",
            reason="Chemistry transformation violates hard guard conditions.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=hard_failures,
        )

    if not bool(p.get("stoichiometry_balanced")):
        sig = base_signature(req, True, False, False, False, 0.62)
        return EvalDraft(
            decision=RuntimeDecision.ESCALATE,
            morphology="stoichiometry_review_required",
            reason="Stoichiometry evidence is insufficient; review required before effect.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=["stoichiometry_balanced=false"],
        )

    if not bool(p.get("thermodynamically_stable")):
        if req.continuity.alternative_path_available:
            sig = base_signature(req, True, False, True, False, 0.66)
            return EvalDraft(
                decision=RuntimeDecision.REDIRECT,
                morphology="thermodynamic_redirect",
                reason="Original transformation is not thermodynamically stable; alternative lawful path available.",
                signature=sig,
                rule_trace=trace,
                blocking_facts=["thermodynamically_stable=false"],
                redirect_candidate={"corridor": "chemistry_transformation_v0", "constraint": "lower_delta_g_path"},
            )
        sig = base_signature(req, True, False, False, True, 0.3)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="thermodynamic_halt",
            reason="Transformation is not thermodynamically stable and no alternative lawful path is available.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=["thermodynamically_stable=false"],
        )

    curvature_risk = float(p.get("curvature_risk", 0.0))
    if curvature_risk > 5.0:
        sig = base_signature(req, True, False, False, True, 0.4)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="curvature_risk_halt",
            reason="FIV curvature risk exceeds admissible threshold.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=[f"curvature_risk={curvature_risk}"],
        )

    sig = base_signature(req, True, True, True, False, 0.91)
    return EvalDraft(
        decision=RuntimeDecision.EXECUTE,
        morphology="chemistry_lawful_transformation",
        reason="Chemistry transformation satisfies guards, capacity, authority, viability, and coherence.",
        signature=sig,
        rule_trace=trace,
    )


def eval_bio(req: RuntimeRequest) -> EvalDraft:
    common = eval_common_first(req, "biomedical_review")
    if common:
        return common

    p = req.proposed_action.payload
    trace = [
        "bio_patient_evidence_check",
        "bio_safety_review_check",
        "bio_viability_score_check",
        "bio_experimental_corridor_check",
        "bio_restart_or_alternative_plan_check",
    ]

    if not p.get("patient_state_current", False):
        sig = base_signature(req, True, False, False, True, 0.35)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="patient_state_stale_halt",
            reason="Patient or biomedical evidence state is not current.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=["patient_state_current=false"],
        )

    if p.get("safety_review_required", True) and not p.get("safety_review_complete", False):
        sig = base_signature(req, True, False, False, False, 0.61)
        return EvalDraft(
            decision=RuntimeDecision.ESCALATE,
            morphology="biomedical_safety_review_required",
            reason="Safety review is required before the biomedical plan may proceed.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=["safety_review_required=true", "safety_review_complete=false"],
        )

    if p.get("experimental", False) and not p.get("controlled_corridor", False):
        sig = base_signature(req, True, False, False, False, 0.58)
        return EvalDraft(
            decision=RuntimeDecision.ESCALATE,
            morphology="experimental_plan_controlled_corridor_required",
            reason="Experimental biomedical plan requires a controlled corridor.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=["experimental=true", "controlled_corridor=false"],
        )

    viability_score = float(p.get("viability_score", 0.0))
    min_viability = float(p.get("min_viability_score", 0.75))
    if viability_score < min_viability:
        if req.continuity.alternative_path_available:
            sig = base_signature(req, True, False, True, False, 0.64)
            return EvalDraft(
                decision=RuntimeDecision.REDIRECT,
                morphology="biomedical_alternative_plan_redirect",
                reason="Biomedical plan viability is below threshold; alternative plan available.",
                signature=sig,
                rule_trace=trace,
                blocking_facts=[f"viability_score={viability_score} < min={min_viability}"],
                redirect_candidate={"corridor": "bio_recovery_plan_v0", "constraint": "lower_risk_alternative_plan"},
            )
        sig = base_signature(req, True, False, False, True, 0.32)
        return EvalDraft(
            decision=RuntimeDecision.HALT,
            morphology="biomedical_viability_halt",
            reason="Biomedical plan viability is below threshold and no alternative lawful path is available.",
            signature=sig,
            rule_trace=trace,
            blocking_facts=[f"viability_score={viability_score} < min={min_viability}"],
        )

    sig = base_signature(req, True, True, True, False, 0.89)
    return EvalDraft(
        decision=RuntimeDecision.EXECUTE,
        morphology="biomedical_review_admitted",
        reason="Biomedical plan is admitted as governed review output, not as treatment authorization.",
        signature=sig,
        rule_trace=trace,
    )


def evaluate_corridor(req: RuntimeRequest) -> EvalDraft:
    if req.continuity.corridor_id == Corridor.CYBER_PRIVILEGED_ACTION:
        return eval_cyber(req)
    if req.continuity.corridor_id == Corridor.CHEMISTRY_TRANSFORMATION:
        return eval_chemistry(req)
    if req.continuity.corridor_id == Corridor.BIO_RECOVERY_PLAN:
        return eval_bio(req)
    raise ValueError(f"Unsupported corridor: {req.continuity.corridor_id}")
