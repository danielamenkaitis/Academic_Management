from sqlalchemy import Column, Integer, String
from app.database.DataBase import Base


class Course(Base): 
    __tablename__ = "courses"
    
    id           = Column(Integer, primary_key=True, unique=True, index=True)
    course_name  = Column(String, nullable=False)
    course_code  = Column(String, nullable=False)
    credit_hours = Column(Integer, nullable=True)
    professor_id = Column(Integer, nullable=True)
    active       = Column(String, nullable=True, default="S")
    
