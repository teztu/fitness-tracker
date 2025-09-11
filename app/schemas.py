import datetime as dt
from pydantic import BaseModel, Field, ConfigDict

class EnterWeight(BaseModel):
    """expected of user to type"""
    date: dt.date = Field(default_factory=dt.date.today, description="date today)")
    kg: float = Field(gt=10, le=400, description="Bodyweight in KG") #want positive number


class WeightOut(BaseModel):
    """when requesting weight"""
    id: int
    date: dt.date
    kg: float

    # access object directly
    model_config = ConfigDict(from_attributes=True)





class DeleteWeight(BaseModel):
    """when requesting weight"""
    #id: int
    #date: date
    #kg: float
    pass




class WeightLatestOut(WeightOut):

    pass



