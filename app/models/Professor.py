from sqlalchemy import Column, Integer, String
from app.database.DataBase import Base


class Professor(Base): 
    __tablename__ = "professors"
    
    id          = Column(Integer, primary_key=True, unique=True, index=True)
    full_name   = Column(String, nullable=False)
    department  = Column(String, nullable=False)
    active      = Column(String, nullable=True, default="S")
    
  