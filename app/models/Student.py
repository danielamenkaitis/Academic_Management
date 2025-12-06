from sqlalchemy import Column, Date, Integer, String
from app.database.DataBase import Base


class Student(Base): 
    __tablename__ = "students"
    
    id                = Column (Integer, primary_key=True, unique=True, index=True)
    full_name         = Column (String, nullable=False)
    enrollment_number = Column (String, nullable=False)
    birth_date        = Column(Date)
    course            = Column (String, nullable=False)
    active            = Column (String, nullable=True, default="S")
    
    
    