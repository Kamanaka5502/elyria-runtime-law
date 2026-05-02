from __future__ import annotations

import hashlib
import json
from typing import Any, Dict, Optional

from app.models import Receipt, RuntimeRequest, RuntimeDecision


def canonical_json(obj: Any) -> str:
    if hasattr(obj, "model_dump"):
        obj = obj.model_dump(mode="json")
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def request_hash(req: RuntimeRequest) -> str:
    return sha256_text(canonical_json(req))


def stable_state_hash(req: RuntimeRequest) -> str:
    if req.current_state.state_hash:
        return req.current_state.state_hash
    state_obj = {
        "current_state": req.current_state.model_dump(mode="json"),
        "capacity": req.capacity.model_dump(mode="json"),
        "continuity": req.continuity.model_dump(mode="json"),
    }
    return sha256_text(canonical_json(state_obj))


def make_receipt(
    req: RuntimeRequest,
    decision: RuntimeDecision,
    reason: str,
    rule_trace: list[str],
    blocking_facts: list[str],
) -> Receipt:
    req_hash = request_hash(req)
    state_hash = stable_state_hash(req)
    prior = req.continuity.prior_receipt_hash
    policy_version = req.current_state.policy_version

    replay_material = {
        "request_hash": req_hash,
        "state_hash": state_hash,
        "policy_version": policy_version,
        "corridor_id": req.continuity.corridor_id.value,
        "decision": decision.value,
        "reason": reason,
        "rule_trace": rule_trace,
        "blocking_facts": blocking_facts,
        "prior_receipt_hash": prior,
    }
    replay_token = sha256_text(canonical_json(replay_material))

    receipt_material = {
        **replay_material,
        "replay_token": replay_token,
    }
    receipt_hash = sha256_text(canonical_json(receipt_material))

    return Receipt(
        receipt_hash=receipt_hash,
        prior_receipt_hash=prior,
        state_hash=state_hash,
        request_hash=req_hash,
        policy_version=policy_version,
        rule_trace=rule_trace,
        blocking_facts=blocking_facts,
        replay_token=replay_token,
    )
