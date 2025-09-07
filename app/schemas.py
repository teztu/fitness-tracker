from datetime import date
from pydantic import BaseModel, Field, ConfigDict

class EnterWeight(BaseModel):
    """expected of user to type"""
    date: date
    kg: float = Field(gt=0, description="BW in kilograms")


class WeightOut(BaseModel):
    """when requesting weight"""
    id: int
    date: date
    kg: float

    # access object directly
    model_config = ConfigDict(from_attributes=True)


class WeightLatestOut(WeightOut):

    pass



