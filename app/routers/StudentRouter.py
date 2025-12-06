from typing import List
from app.database.DataBase import get_db
from app.schema.Student import StudentData
from app.services.StudentService import StudentService
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

class StudentRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/student", tags=["Student"])
        self.router.add_api_route("/",               self.getAll,        methods=["GET"],    response_model=list[StudentData])
        self.router.add_api_route("/{student_id}",   self.getById,       methods=["GET"],    response_model=StudentData)
        self.router.add_api_route("/",               self.post,          methods=["POST"],   response_model=StudentData)
        self.router.add_api_route("/{student_id}",   self.put,           methods=["PUT"],    response_model=StudentData)
        self.router.add_api_route("/{student_id}",   self.delete,        methods=["DELETE"], response_model=dict)

    def getAll(self, db: Session = Depends(get_db)) -> List[StudentData]:
        service = StudentService(db)
        return service.getAll()
    
    def getById(self, student_id: int, db: Session = Depends(get_db)) -> StudentData:
        service = StudentService(db)
        return service.getById(student_id)

    def post(self, student: StudentData, db: Session = Depends(get_db)) -> StudentData:
        service = StudentService(db)
        return service.post(student)
   
    def put(self, student_id: int, student : StudentData, db: Session = Depends(get_db)) -> StudentData:
        service = StudentService(db)
        return service.put(student_id, student)
    
    def delete(self, student_id: int, db: Session = Depends(get_db)) -> dict:
        service = StudentService(db)
        return service.delete(student_id) 
