# Fitness Tracker API

A FastAPI application for tracking workouts and exercises.

---

## 🚀 Tech Stack

* **Python**
* **FastAPI**
* **PostgreSQL**
* **Docker**

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

3. **Start FastAPI server**

```powershell
python -m uvicorn app.main:app --reload
```

4. **Test if API is running**

```powershell
curl http://127.0.0.1:8000/health
```

**Expected output:**

```json
{
  "status": "everything stable"
}
```

---

## 📝 Notes

* `.env` must be saved as **UTF-8/ASCII**
* Always run `python -m uvicorn` (not just `uvicorn`)
* Docker Desktop must be running before starting Postgres
* Keep local `main` in sync with `origin/main` using `git pull` and `git push`

---

## 🔀 Git Workflow

1. **Create a new branch**

```powershell
git checkout -b feature/my-feature
```

2. **Make changes and commit**

```powershell
git add .
git commit -m "feat: add my new feature"
```

3. **Push branch to GitHub**

```powershell
git push -u origin feature/my-feature
```

4. **Create Pull Request (PR)** on GitHub → review → merge into `main`

5. **Update local main**

```powershell
git checkout main
git pull
```

