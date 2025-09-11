from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas
from .database import get_db, engine, Base



app = FastAPI(title="Fitness Tracker API", version="0.0.1")
Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "everything stable", "timestamp": datetime.now().isoformat()}


@app.post("/weigh_in", response_model=schemas.WeightOut, status_code=status.HTTP_201_CREATED)
def entry_weight(payload: schemas.EnterWeight, db: Session = Depends(get_db)):
    try:
        row = models.Weight(date=payload.date, kg=payload.kg)
        db.add(row)
        db.flush()
        db.refresh(row)
        return row
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=500, detail="Failed weight entry")


@app.get("/weight/latest", response_model=schemas.WeightOut | None)
def get_latest_weight(db: Session = Depends(get_db)):
    try:
        row = db.query(models.Weight).order_by(models.Weight.id.desc()).first()
        return row
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=500, detail="Failed to get weight")

@app.delete("/weight/{weight_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_weight(weight_id: int, db: Session = Depends(get_db)):
    try:
        row = db.get(models.Weight, weight_id)
        if not row:
            raise HTTPException(status_code=404, detail=f"Weight id={weight_id} not found")
        db.delete(row)
        return None
    except HTTPException:
        raise HTTPException(status_code=001, detail="handle fail")
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=500, detail="Delete failed")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)











