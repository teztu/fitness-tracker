# Fitness Tracker API 🏋️

A simple FastAPI project for logging bodyweight.  
Built to demonstrate basic skills with **APIs, Python, SQLAlchemy, SQLite/Postgres, Docker, and CI/CD**.  
Created by **Nicolas Cook** for own learning experience.

---

## 🚀 Quickstart (SQLite – easiest)

Requires Python 3.12. The app uses SQLite by default and creates a local `app.db`.  
Tables are created automatically on startup.

Make sure you have latest git installed, 
then clone and run:

    git clone https://github.com/teztu/fitness-tracker.git
    cd fitness-tracker
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt

Start the API:

    uvicorn app.main:app --reload

Open in your browser:
- http://127.0.0.1:8000/health

It should look something like this:  
<img width="2557" height="1227" alt="api_example" src="https://github.com/user-attachments/assets/88b96950-597d-4eb6-b560-9e6114680d29" />

---

## 🔎 Smoke test (while server is running)

Health:

    curl http://127.0.0.1:8000/health

Log weight (date optional, defaults to today):

    curl -X POST http://127.0.0.1:8000/weigh_in -H "Content-Type: application/json" -d "{\"kg\": 82.5}"

Get latest:

    curl http://127.0.0.1:8000/weight/latest

List (if implemented in this version):

    curl "http://127.0.0.1:8000/weights?limit=5&offset=0"

Docs (Swagger UI):
- http://127.0.0.1:8000/docs

---

## 🐘 Optional: Postgres with Docker

This repo also includes `docker-compose.yml` for running a Postgres database.  
If you have Docker installed:

    docker compose up -d

Configure your `.env` (see `env.example`):

    DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/fitness

Then start the API:

    uvicorn app.main:app --reload

---

## 🔗 API Endpoints

| Method | Endpoint         | Description                    |
|--------|------------------|--------------------------------|
| GET    | /health          | Health/status check            |
| POST   | /weigh_in        | Log a new weight entry         |
| GET    | /weight/latest   | Fetch the most recent entry    |
| GET    | /weights         | List all entries (paginated)   |
| DELETE | /weight/{id}     | Delete a weight entry by ID    |

Example request body:
- POST `/weigh_in` → `{"kg": 82.5}`  
  (Optional: `{"kg": 82.5, "date": "2025-09-11"}`)

---

## 🧪 Tests

Run locally:

    pytest -q

Notes:
- Tests use SQLite by default. You can set a separate DB via `DATABASE_URL` if needed.
- If you change the model and want a fresh local DB, stop the server and delete `app.db`.

---

## ⚙️ CI/CD

GitHub Actions is set up to run automatically on every push/PR:  
- **Tests:** pytest (using SQLite by default, or Postgres job if enabled)  
- **Lint/format:** optional to add later (ruff/black)

Minimal example workflow (`.github/workflows/ci.yml`):

    name: CI
    on: [push, pull_request]
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.12"
          - run: pip install -r requirements.txt
          - run: pytest -q

---

## 🧱 Troubleshooting

- Run commands from the repo root (same level as the `app/` folder).
- Ensure `app/__init__.py` exists.
- Port in use? Start on a different port:
  
      uvicorn app.main:app --reload --port 8001

- Changed the schema and want a clean slate? Stop the server and delete `app.db`, then start again.

---

## 📦 Tech stack

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **SQLite** (default) + **Postgres** (optional via Docker)
- **Docker Compose** (optional)
- **pytest**
- **GitHub Actions**

---

## 💡 Why this repo?

This project was created to demonstrate practical experience with:
- Python backend development (FastAPI)
- Databases (SQLAlchemy + SQLite/Postgres)
- API design with validation and error handling
- Git / GitHub workflow
- Docker and environment-based configuration
- CI/CD pipelines with GitHub Actions

---

## 🚀 Possible future improvements / implementations

- Alembic migrations for database schema changes  
- Authentication (JWT-based)  
- Frontend dashboard (React or Streamlit)  
- Extended test coverage  
- Deployment to cloud (Azure/AWS/GCP)  
- More endpoints  
- Use API for visualization of weight progression  
- Clean up code/syntax  
- Add more descriptions of what code is doing

