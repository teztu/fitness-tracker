# Fitness Tracker API

A FastAPI application for tracking bodyweight.  
Log daily weights, fetch the latest entry, and delete mistakes — perfect for simple fitness progress tracking.

<img width="2557" height="1227" alt="image" src="https://github.com/user-attachments/assets/19983c6f-8f37-4bc0-8733-b70bd4eda685" />



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

### Log bodyweight
```
POST /weigh_in
```
Body:
```json
{ "date": "2025-09-07", "kg": 82.5 }
```

### Fetch latest weight
```
GET /weight/latest
```

### Delete weight
```
DELETE /weight/{weight_id}
```

---

## 🧪 Quick usage (PowerShell)

**Add a new weight**
```powershell
curl -X POST http://127.0.0.1:8000/weigh_in -H "Content-Type: application/json" -d "{ \"date\": \"2025-09-07\", \"kg\": 82.5 }"
```

**Fetch latest**
```powershell
curl http://127.0.0.1:8000/weight/latest
```

**Delete weight with ID 1**
```powershell
curl -X DELETE http://127.0.0.1:8000/weight/1
```

---

## 📝 Notes
- Save `.env` as **UTF-8/ASCII**  
- Prefer `python -m uvicorn app.main:app --reload` over bare `uvicorn`  
- Docker Desktop must be running before Postgres  
- Hard refresh Swagger with **Ctrl+F5** if the docs look stale  

---

## 🔀 Git Workflow
```powershell
# create a new branch
git checkout -b feature/my-feature

# make changes and commit
git add .
git commit -m "feat: add my new feature"

# push branch to GitHub
git push -u origin feature/my-feature

# open PR on GitHub → review → merge into main

# update local main
git checkout main
git pull
```

---

## ✅ Next Steps
- Authentication (users)  
- Progress charts / visualization  
- Extend schema with workouts & nutrition  
- Dockerize FastAPI app (not just Postgres)  
- CI/CD with GitHub Actions  

