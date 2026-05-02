import json
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
EX = Path(__file__).resolve().parents[1] / "examples"


def load(name: str):
    return json.loads((EX / name).read_text())


def test_cyber_execute():
    r = client.post("/runtime/evaluate", json=load("cyber_execute.json"))
    assert r.status_code == 200
    data = r.json()
    assert data["decision"] == "EXECUTE"
    assert data["consequence_binds"] is True
    assert data["receipt"]["receipt_hash"]


def test_cyber_refuse_authority():
    r = client.post("/runtime/evaluate", json=load("cyber_refuse_authority.json"))
    assert r.status_code == 200
    data = r.json()
    assert data["decision"] == "REFUSE"
    assert data["consequence_binds"] is False


def test_cyber_redirect():
    r = client.post("/runtime/evaluate", json=load("cyber_redirect.json"))
    assert r.status_code == 200
    data = r.json()
    assert data["decision"] == "REDIRECT"
    assert data["redirect_candidate"] is not None


def test_chemistry_guard_halt():
    r = client.post("/runtime/evaluate", json=load("chemistry_halt_guard.json"))
    assert r.status_code == 200
    data = r.json()
    assert data["decision"] == "HALT"
    assert "energy_conserved" in data["receipt"]["blocking_facts"]


def test_bio_escalate_safety():
    r = client.post("/runtime/evaluate", json=load("bio_escalate_safety.json"))
    assert r.status_code == 200
    data = r.json()
    assert data["decision"] == "ESCALATE"


def test_replay_passes():
    payload = load("cyber_execute.json")
    r = client.post("/runtime/evaluate", json=payload)
    assert r.status_code == 200
    receipt = r.json()["receipt"]

    replay = client.post("/receipt/replay", json={"original_request": payload, "receipt": receipt})
    assert replay.status_code == 200
    assert replay.json()["replay_passed"] is True
