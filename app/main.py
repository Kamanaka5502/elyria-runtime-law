from __future__ import annotations

from fastapi import FastAPI, HTTPException

from app.evaluator import evaluate
from app.models import ReplayRequest, ReplayResponse, RuntimeRequest, RuntimeResponse
from app.receipts import make_receipt

app = FastAPI(
    title="Elyria Runtime Law",
    version="0.1.0",
    description="Runtime law for consequence-bearing systems. Consequence admission before effect.",
)


@app.get("/")
def root():
    return {
        "name": "Elyria Runtime Law",
        "version": "0.1.0",
        "category": "Runtime law for consequence-bearing systems",
        "core_object": "attempted becoming",
        "principle": "Most systems govern actors, actions, or outputs. Elyria governs continuation.",
    }


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    return {"status": "ready"}


@app.post("/runtime/evaluate", response_model=RuntimeResponse)
def runtime_evaluate(req: RuntimeRequest):
    try:
        return evaluate(req)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/receipt/replay", response_model=ReplayResponse)
def receipt_replay(req: ReplayRequest):
    observed = evaluate(req.original_request)
    expected = req.receipt

    return ReplayResponse(
        replay_passed=(
            observed.receipt.receipt_hash == expected.receipt_hash
            and observed.receipt.replay_token == expected.replay_token
        ),
        expected_receipt_hash=expected.receipt_hash,
        observed_receipt_hash=observed.receipt.receipt_hash,
        expected_replay_token=expected.replay_token,
        observed_replay_token=observed.receipt.replay_token,
        decision=observed.decision,
    )
