from typing import List
from fastapi import APIRouter, Depends
from app.database.DataBase import Session, get_db
from app.models.Assessment import Assessment
from app.schema.Assessment import AssessmentData
from app.services.AssessmentService import AssessmentService
from app.util.util import NotFound


class AssessmentRouter():
    def __init__(self):
        self.router = APIRouter(prefix="/assessment", tags=["Assessment"])
        self.router.add_api_route("/",                self.getAll,      methods=["GET"],    response_model=list[AssessmentData])
        self.router.add_api_route("/{assessment_id}", self.getById,     methods=["GET"],    response_model=AssessmentData)
        self.router.add_api_route("/",                self.post,        methods=["POST"],   response_model=AssessmentData)
        self.router.add_api_route("/{assessment_id}", self.put,         methods=["PUT"],    response_model=AssessmentData)
        self.router.add_api_route("/{assessment_id}", self.delete,      methods=["DELETE"], response_model=dict)
        
    def getAll(self, db: Session = Depends(get_db)) -> List[AssessmentData]:
        service = AssessmentService(db)
        return service.getAll()
    
    def getById(self, assessment_id: int, db: Session = Depends(get_db)) -> AssessmentData:
        service = AssessmentService(db)
        return service.getById(assessment_id)
    
    def post(self, assessment: AssessmentData, db: Session = Depends(get_db)) -> AssessmentData:
        service = AssessmentService(db)
        return service.post(assessment)
    
    def put(self, assessment_id: int ,assessment: AssessmentData, db: Session = Depends(get_db)) -> AssessmentData:
        service = AssessmentService(db)
        return service.put(assessment_id, assessment)
    
    def delete(self, assessment_id: int, db: Session = Depends(get_db)) -> dict: 
        service = AssessmentService(db)
        return service.delete(assessment_id)