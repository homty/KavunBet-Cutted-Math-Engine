# KavunBet Math Engine

KavunBet Math Engine evaluates reel configurations for a five-reel ways game with base-game and free-spin modes. This repository contains the deterministic math runtime; optimization orchestration belongs to the separate Optimizer service.

## Current scope

- Ways-pay evaluation.
- Base-game and free-spin execution.
- Reel-strip input from CSV files.
- Bounded local simulations of up to 5,000 spins per mode.
- Unit tests for ways wins and multiplier strategies.


## Local setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
```

Run the current local simulation with:

```powershell
python -m games.ways.run
```

Generated books, lookup tables, and configuration output are ignored by Git.

## Service boundary

The future gRPC layer will accept an evaluation request containing a validated configuration, candidate reel CSV content, spin count, and seed. It will return calculated metrics and artifact metadata. The Math Engine will not own optimization jobs, candidate generation, user-facing REST endpoints, or permanent artifact storage.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and [`docs/ROADMAP.md`](docs/ROADMAP.md).
