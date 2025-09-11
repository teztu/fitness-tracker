# Fitness Tracker API 🏋️

A simple FastAPI project for logging bodyweight.  
Built to demonstrate basic skills with **APIs, Python, SQLAlchemy, SQLite/Postgres, Docker, and CI/CD**.
Created by Nicolas Cook for own learning experience

---

## 🚀 Quickstart (SQLite – easiest)

Requires Python 3.12.

    git clone https://github.com/teztu/fitness-tracker.git
    cd fitness-tracker
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # Linux/Mac: source .venv/bin/activate
    pip install -r requirements.txt

    # Start the API
    uvicorn app.main:app --reload

Open in your browser:  
👉 http://127.0.0.1:8000/health

👉 It should look something like this:
<img width="2557" height="1227" alt="api_example" src="https://github.com/user-attachments/assets/88b96950-597d-4eb6-b560-9e6114680d29" />


---

## 🐘 Optional: Postgres with Docker

This repo also includes `docker-compose.yml` for running a Postgres database.  
Run it (if you have Docker installed):

    docker compose up -d

Configure your `.env` (see `env.example`):

    DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/fitness

Then start the API:

    uvicorn app.main:app --reload

---

## 🔗 API Endpoints

| Method | Endpoint         | Description                    |
|--------|------------------|--------------------------------|
| GET    | `/health`        | Health/status check            |
| POST   | `/weigh_in`      | Log a new weight entry         |
| GET    | `/weight/latest` | Fetch the most recent entry    |
| GET    | `/weights`       | List all entries (paginated)   |
| DELETE | `/weight/{id}`   | Delete a weight entry by ID    |

### Examples

    # Log weight (date optional, defaults to today)
    curl -X POST http://127.0.0.1:8000/weigh_in \
         -H "Content-Type: application/json" \
         -d '{"kg": 82.5}'

    # Get the latest logged weight
    curl http://127.0.0.1:8000/weight/latest

---

## 🧪 Tests

This project includes basic `pytest` tests.  
Run them with:

    pytest -q

---

## ⚙️ CI/CD

GitHub Actions is set up to run automatically on every push/PR:  
- **Lint:** ruff and black  
- **Tests:** pytest (using SQLite backend)  

---

## 📦 Tech stack

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **SQLite** (default) + **Postgres** (optional via Docker)
- **Docker Compose**
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

## 🚀 Possible future improvements/implimentations

- Alembic migrations for database schema changes  
- Authentication (JWT-based)  
- Frontend dashboard (React or Streamlit)  
- Extended test coverage  
- Deployment to cloud (Azure/AWS/GCP)  
- More endpoints
- Use API for visualization of weight progression
- Clean up code/syntax
- Add more descriptions of what code is doing

