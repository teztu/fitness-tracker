# Fitness Tracker API

A FastAPI application for tracking workouts and exercises (currently focused on bodyweight logging).

---

## 🚀 Tech Stack
- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Docker**

---

## ▶️ How to start program

1. **Activate local environment**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Start Postgres container**
   ```powershell
   docker compose up -d postgres
   docker ps   # check if fitness_postgres is running
   ```

3. **Create `.env` in project root**
   ```text
   DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/fitness
   ```

4. **Start FastAPI server**
   ```powershell
   python -m uvicorn app.main:app --reload
   ```

5. **Test if API is running**
   ```powershell
   curl http://127.0.0.1:8000/health
   ```
   **Expected output:**
   ```json
   { "status": "everything stable" }
   ```

👉 Swagger UI is available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 API Endpoints

- `GET /health` → health check  
- `POST /weigh_in` → log new weight  
  Example body:
  ```json
  { "date": "2025-09-07", "kg": 82.5 }
  ```
- `GET /weight/latest` → fetch latest logged weight  
- `DELETE /weight/{weight_id}` → delete a weight entry  

---

## 📝 Notes
- `.env` must be saved as **UTF-8/ASCII**  
- Always run `python -m uvicorn` (not just `uvicorn`)  
- Docker Desktop must be running before starting Postgres  
- Hard refresh Swagger with **Ctrl+F5** if docs cache old state  
- Keep local `main` in sync with `origin/main` using `git pull` and `git push`  

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

# create Pull Request (PR) on GitHub → review → merge into main

# update local main
git checkout main
git pull
```

---

## ✅ Next Steps
- Add authentication (users)  
- Extend schema with more metrics (workouts, nutrition, etc.)  
- Dockerize FastAPI app (not just Postgres)  
- Add CI/CD pipeline with GitHub Actions  
