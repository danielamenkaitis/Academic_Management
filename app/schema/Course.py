from pydantic import BaseModel


class CourseData(BaseModel): 
    id: int | None = None 
    course_name: str
    course_code: int
    credit_hours: int
    professor_id: int
    active: str
    
    class Config: 
        from_attributes = True
    
    