from typing import List
from app.database.DataBase import get_db
from app.services.CourseService import CourseService
from fastapi import APIRouter, Depends
from app.schema.Course import CourseData
from sqlalchemy.orm import Session

#CourseRouter é molde
#__init__ método do construtor da classe,
# chamado automaticamente quando você cria um objeto dessa classe.
class CourseRouter():
    def __init__(self):
        self.router = APIRouter(prefix="/course",    tags=["Course"])
        self.router.add_api_route("/",               self.getAll,        methods=["GET"],       response_model=list[CourseData])
        self.router.add_api_route("/{course_id}",    self.getById,       methods=["GET"],       response_model=CourseData)
        self.router.add_api_route("/",               self.post,          methods=["POST"],      response_model=CourseData)
        self.router.add_api_route("/{course_id}",    self.put,           methods=["PUT"],       response_model=CourseData)
        self.router.add_api_route("/{course_id}",    self.delete,        methods=["DELETE"],    response_model=dict)
    
    def getAll(self, db: Session = Depends(get_db)) -> List[CourseData]:
        service = CourseService(db)
        return service.getAll()
    
    def getById(self, course_id: int, db: Session = Depends(get_db)) -> CourseData:  
        service = CourseService(db)
        return service.getById(course_id)
    
    def post(self, course: CourseData, db: Session = Depends(get_db)) -> CourseData:
        service = CourseService(db)
        return service.post(course)
    
    def put(self, course_id: int, course: CourseData ,db: Session = Depends(get_db)) -> CourseData:
        service = CourseService(db)
        return service.put(course_id, course)
    
    def delete(self, course_id: int, db: Session = Depends(get_db)) -> CourseData: 
        service = CourseService(db)
        return service.delete(course_id)
    
        

        