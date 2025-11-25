from dataclasses import dataclass
from typing import List
from app.schema.Professor import ProfessorData
from app.services.ProfessorService import ProfessorService

@dataclass
class ProfessorRouter(): 
    def __init__(self, service: ProfessorService):
        self.service = service
    
    def getAll(self) -> List[ProfessorData]:
        return self.service.getAll()
    
    def getById(self, professor_id: int) -> List[ProfessorData]:
        return self.service.getById(professor_id)
    
    def post(self, professor: ProfessorData) -> ProfessorData:  
        return self.service.post(professor)
    
    def put(self, professor_id: int, professor: ProfessorData) -> ProfessorData:
        return self.service.put(professor_id, professor)
    
    def delete(self, professor_id: int) -> dict:
        return self.service.delete(professor_id)
    
    
    
    