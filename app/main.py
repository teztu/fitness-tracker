from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#from .schemas import WeightInput
from datetime import datetime

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "everything stable", "timestamp": datetime.now()}


@app.post("/weigh_in")
def entry_weight():
    try:
        """Enter todays weight"""
        return weight_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"generic error message: {str(e)}")


@app.get("/weight/latest")
def get_latest_weight():
    try:

        """Get the most recent weight entry"""
        return latest_weight
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"generic error message: {str(e)}")

@app.delete("/weight/{weight_id}")
def delete_weight():
    try:

        """Delete a weight entry"""
        return deleted_weight
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"generic error message: {str(e)}")