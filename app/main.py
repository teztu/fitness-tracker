from fastapi import FastAPI, HTTPException
from schemas import EnterWeight, WeightOut
from datetime import datetime
from database import get_db

app = FastAPI()

db=get_db()


@app.get("/health")
def health():
    return {"status": "everything stable", "timestamp": datetime.now()}


@app.post("/weigh_in", response_model=schemas.WeightOut, status_code=status.HTTP_201_CREATED)
def entry_weight(payload: schemas.WeightCreate, db: Session = Depends(get_db)):
    try:
        row = models.Weight(date=payload.date, kg=payload.kg)
        db.add(row)
        db.flush()        # generer id
        db.refresh(row)   # sørger for oppdatert state
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to insert weight: {str(e)}")


@app.get("/weight/latest", response_model=schemas.WeightOut | None)
def get_latest_weight(db: Session = Depends(get_db)):
    try:
        row = db.query(models.Weight).order_by(models.Weight.id.desc()).first()
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch latest weight: {str(e)}")

@app.delete("/weight/{weight_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_weight(weight_id: int, db: Session = Depends(get_db)):
    try:
        row = db.get(models.Weight, weight_id)
        if not row:
            raise HTTPException(status_code=404, detail=f"Weight id={weight_id} not found")
        db.delete(row)
        # 204 -> ingen body
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete weight: {str(e)}")














"""  
@app.get("/weight/latest")
def get_latest_weight():
    try:

        """Get the most recent weight entry"""
        return latest_weight
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"generic error message: {str(e)}")
"""