# Termux Runtime Note

This package was prepared on Termux where Python may default to 3.13.

FastAPI/Pydantic dependency installation may fail on Android/Termux because pydantic-core may require a Rust-backed build target not available through the local environment.

This is an environment limitation, not a Runtime Law logic failure.

Recommended validation environment:

- Python 3.11 or 3.12
- Linux/macOS/standard CI runner
- `pip install -e ".[dev]"`
- `pytest -q`

Core package purpose:

Elyria Runtime Law v0.1 implements consequence admissibility, corridor evaluation, morphology outcomes, deterministic receipts, and replay verification.
