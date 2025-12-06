from sqlalchemy import Column, Date, Float, Integer, String
from app.database.DataBase import Base


class Assessment(Base): 
    __tablename__ = "assessments"
    
    id              = Column(Integer, primary_key=True, unique=True, index=True)
    student_id      = Column(Integer, nullable=False)
    course_id       = Column(Integer, nullable=False)
    grade           = Column(Float,   nullable=False)
    semester        = Column(String,  nullable=False)
    evaluation_date = Column(Date)
    active          = Column(String,  nullable=True, default="S")