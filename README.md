# Fitness Tracker API

A FastAPI application for tracking bodyweight.  
Log daily weights, fetch the latest entry, and delete mistakes — perfect for simple fitness progress tracking.

---

## 📖 What can you use it for?
- Track your **daily bodyweight** over time
- Fetch the **latest logged weight**
- Remove mistakes with **delete**
- Connect it to a mobile app, web dashboard, or analytics tool

---

## 🚀 Tech Stack
- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Docker** (optional for DB)

---

## 🖥️ Install & run on your PC

1) **Clone repository**
```powershell
git clone https://github.com/<your-username>/fitness-tracker.git
cd fitness-tracker
```

2) **Create & activate virtual env**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3) **Install dependencies**
```powershell
pip install -r requirements.txt
```

4) **Start PostgreSQL (Docker)**
```powershell
docker compose up -d postgres
docker ps   # verify 'fitness_postgres' is running
```

5) **Create `.env` in project root**
```text
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/fitness
```

6) **Run API**
```powershell
python -m uvicorn app.main:app --reload
```

7) **Test health**
```powershell
curl http://127.0.0.1:8000/health
```
Expected:
```json
{"status": "everything stable"}
```

👉 Swagger UI: http://127.0.0.1:8000/docs

---

## 📌 API Endpoints

### Health check
```
GET /health
```

##
