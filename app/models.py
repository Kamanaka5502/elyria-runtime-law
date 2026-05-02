from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class RuntimeDecision(str, Enum):
    EXECUTE = "EXECUTE"
    REFUSE = "REFUSE"
    HALT = "HALT"
    REDIRECT = "REDIRECT"
    ESCALATE = "ESCALATE"
    REBOUND = "REBOUND"
    RESTART = "RESTART"


class Corridor(str, Enum):
    CYBER_PRIVILEGED_ACTION = "cyber_privileged_action_v0"
    CHEMISTRY_TRANSFORMATION = "chemistry_transformation_v0"
    BIO_RECOVERY_PLAN = "bio_recovery_plan_v0"


class Actor(BaseModel):
    actor_id: str
    role: str = "operator"
    authority_scope: List[str] = Field(default_factory=list)


class Evidence(BaseModel):
    evidence_id: str = "ev_001"
    source: str = "unspecified"
    freshness_seconds: int = 0
    max_age_seconds: int = 300
    custody_hash: Optional[str] = None
    confidence: float = 1.0


class Capacity(BaseModel):
    C: float = 100.0
    M: float = 0.0
    minimum_required_phi: float = 0.0


class Continuity(BaseModel):
    prior_receipt_hash: Optional[str] = None
    corridor_id: Corridor
    corridor_status: str = "open"
    restart_available: bool = False
    alternative_path_available: bool = False


class ProposedAction(BaseModel):
    action_id: str
    action_type: str
    target_system: str = "unspecified"
    intended_effect: str = "unspecified"
    risk_level: str = "medium"
    payload: Dict[str, Any] = Field(default_factory=dict)


class CurrentState(BaseModel):
    state_hash: Optional[str] = None
    system_health: str = "green"
    policy_version: str = "elyria_runtime_law_v0.1"
    revocation_status: str = "clear"
    drift_status: str = "none"


class RuntimeRequest(BaseModel):
    actor: Actor
    proposed_action: ProposedAction
    evidence: Evidence
    current_state: CurrentState
    capacity: Capacity
    continuity: Continuity


class SignatureVector(BaseModel):
    phi: float
    admissibility_A: float
    authority_U: int
    viability_V: float
    breach_B: float
    restart_R: int
    coherence_H: float
    h_min: float = 0.70


class BoundaryResult(BaseModel):
    authority: str
    evidence: str
    state: str
    capacity: str
    viability: str
    breach: str
    restart: str
    coherence: str
    policy_integrity: str


class Receipt(BaseModel):
    receipt_hash: str
    prior_receipt_hash: Optional[str] = None
    state_hash: str
    request_hash: str
    policy_version: str
    rule_trace: List[str]
    blocking_facts: List[str]
    replay_token: str


class RuntimeResponse(BaseModel):
    decision: RuntimeDecision
    morphology: str
    consequence_binds: bool
    reason: str
    corridor_id: Corridor
    signature: SignatureVector
    boundary_result: BoundaryResult
    receipt: Receipt
    redirect_candidate: Optional[Dict[str, Any]] = None
    missing_fields: List[str] = Field(default_factory=list)


class ReplayRequest(BaseModel):
    original_request: RuntimeRequest
    receipt: Receipt


class ReplayResponse(BaseModel):
    replay_passed: bool
    expected_receipt_hash: str
    observed_receipt_hash: str
    expected_replay_token: str
    observed_replay_token: str
    decision: RuntimeDecision
