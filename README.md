# FastAPI Backend Sample

A small FastAPI application with no external service dependencies.

## Requirements

- Python 3.11 or later

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python main.py
```

The server listens on `PORT` when it is set and otherwise uses port `8080`.

Open `http://localhost:8080`.

## Verify

Install the development dependencies and run the tests:

```powershell
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python -m pytest
.\scripts\verify.ps1 -BaseUrl http://localhost:8080
```

## Builder Apps configuration

The root `builder.yaml` declares one public Python web component. It uses the
repository root, starts through `python main.py`, listens on port `8080`, and
reports readiness through `/health`.

## Routes

| Route | Purpose |
|---|---|
| `GET /` | Sample identity and deployment markers |
| `GET /products/widget-1` | Direct deep-link test |
| `GET /health` | Runtime health |
| `GET /api/status` | API reachability |
| `GET /api/version` | App, framework, runtime, and deployment identity |
| `GET /api/request` | Safe request metadata |
