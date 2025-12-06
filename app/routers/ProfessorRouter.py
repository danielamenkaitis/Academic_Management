from typing import List
from app.database.DataBase import get_db
from app.services.ProfessorService import ProfessorService
from fastapi import APIRouter, Depends
from app.schema.Professor import ProfessorData
from sqlalchemy.orm import Session


class ProfessorRouter(): 
    def __init__(self):
        self.router = APIRouter(prefix="/professor", tags=["Professor"])
        self.router.add_api_route("/",               self.getAll,        methods=["GET"],    response_model=list[ProfessorData])
        self.router.add_api_route("/{professor_id}", self.getById,       methods=["GET"],    response_model=ProfessorData)
        self.router.add_api_route("/",               self.post,          methods=["POST"],   response_model=ProfessorData)
        self.router.add_api_route("/{professor_id}", self.put,           methods=["PUT"],    response_model=ProfessorData)
        self.router.add_api_route("/{professor_id}", self.delete,        methods=["DELETE"], response_model=dict)
    
    
    def getAll(self, db: Session = Depends(get_db)) -> List[ProfessorData]:
        service = ProfessorService(db)
        return service.getAll()
    
    def getById(self, professor_id: int, db: Session = Depends(get_db)) -> ProfessorData:
        service = ProfessorService(db)
        return service.getById(professor_id)
    
    def post(self, professor: ProfessorData, db: Session = Depends(get_db)) -> ProfessorData:
        service = ProfessorService(db)
        return service.post(professor)
   
    def put(self, professor_id: int, student : ProfessorData, db: Session = Depends(get_db)) -> ProfessorData:
        service = ProfessorService(db)
        return service.put(professor_id, student)
    
    def delete(self, professor_id: int, db: Session = Depends(get_db)) -> dict:
        service = ProfessorService(db)
        return service.delete(professor_id) 


 
    
    
    
    