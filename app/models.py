from sqlalchemy import Column, Integer, Date, Float
from .database import Base

class Weight(Base):
    __tablename__ = "bodyweight"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    kg = Column(Float, nullable=False) #not realistic weighing 0 kg



