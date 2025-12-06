from datetime import date
from pydantic import BaseModel


class AssessmentData(BaseModel): 
    id: int | None = None 
    student_id: int
    course_id: int
    grade: float
    semester: str
    evaluation_date: date
    active: str
    
    class Config:
        orm_mode = True
    
    
   