from pydantic import BaseModel


class ProfessorData(BaseModel):
    id: int | None = None
    full_name: str 
    department: str 
    active: str 
    
    class Config:
        orm_mode = True