from pydantic import BaseModel


class CourseData(BaseModel): 
    id: int | None = None 
    course_name: str
    course_code: str
    credit_hours: int
    professor_id: int
    active: str
    
    class Config:
        orm_mode = True
    