# AGENTS.md

## Cursor Cloud specific instructions

This repo is a minimal Flask demo API (`app.py`) with two endpoints: `/` (welcome JSON) and `/health` (status JSON).

- Python dependencies are installed into a local virtualenv at `.venv` (created by the update script). Activate with `source .venv/bin/activate` or call binaries directly via `.venv/bin/...`.
- Run the app in development mode (debug + hot reload):
  `.venv/bin/flask --app app run --debug --host 127.0.0.1 --port 5000`
  It serves on `http://127.0.0.1:5000`.
- There are no automated tests or lint config in the repo; CI (`.github/workflows/build.yml`) only runs a SonarQube Cloud scan, which requires the `SONAR_TOKEN` secret and is not needed for local development.
- Quick smoke check: `curl http://127.0.0.1:5000/` and `curl http://127.0.0.1:5000/health`.
