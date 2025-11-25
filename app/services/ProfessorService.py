from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.Professor import Professor
from app.schema.Professor import ProfessorData


class ProfessorService: 
    def __init__(self, db: Session):
        self.db = db 
        
    def NotFound(self):
        raise HTTPException(status_code=404, detail="Not Found")
    
    def getAll(self):
        professors = self.db.query(Professor).filter(Professor.active=="S").all()
        if not professors:
            self.NotFound()
        return professors
        
    def getById(self, professor_id: int):
        professor = self.db.query(Professor).filter(Professor.id == professor_id, Professor.active=="S").first()
        if not professor:
            self.NotFound()
        return professor   
    
    def post(self, professor: ProfessorData): 
        professor_new = Professor(**professor.dict())
        self.db.add(professor_new)
        self.db.commit()
        self.db.refresh(professor_new)
        return professor_new
    
    def put(self, professor_id: int, professor: ProfessorData): 
        professor_update = self.db.query(Professor).filter(Professor.id == professor_id, Professor.active == "S").first()
        if not professor_update: 
            self.NotFound()
        professor_update.full_name      = professor.full_name
        professor_update.department     = professor.department
        self.db.commit()
        self.db.refresh(professor_update)
        return professor_update
    
    def delete(self, professor_id: int): 
        professor_update = self.db.query(Professor).filter(Professor.id == professor_id, Professor.active == "S").first()
        if not professor_update: 
            self.NotFound()
        professor_update.active = "N"
        self.db.commit()
        return {"deleted": True}
        
       
    
    
   