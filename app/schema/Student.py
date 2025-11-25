from pydantic import BaseModel
from datetime import date

class StudentData(BaseModel):
    id: int | None = None   # opcional na entrada
    full_name: str
    enrollment_number: str
    birth_date: date
    course: str
    active: str
    
    class Config:
        orm_mode = True
        
 