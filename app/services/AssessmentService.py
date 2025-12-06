from app.database.DataBase import Session
from app.models.Assessment import Assessment
from app.schema.Assessment import AssessmentData
from app.util.util import NotFound, transactional


class AssessmentService: 
    def __init__(self, db: Session):
        self.db = db
        
    def getAll(self) -> list[AssessmentData]:
        assessments = self.db.query(Assessment).filter(Assessment.active=="S").all()
        if not assessments: 
            NotFound()
        return assessments
    
    def getById(self, assessment_id: int) -> AssessmentData:
        assessment = self.db.query(Assessment).filter(Assessment.id == assessment_id, Assessment.active=="S").first()
        if not assessment: 
            NotFound()
        return assessment
    
    @transactional
    def post(self, assessment: AssessmentData) -> AssessmentData:
        assessment_new = Assessment(**assessment.dict())
        self.db.add(assessment_new)
        self.db.commit()
        self.db.refresh(assessment_new)
        return assessment_new
    
    @transactional
    def put(self, assessment_id: int, assessment: AssessmentData)-> dict:
        assessment_update = self.db.query(Assessment).filter(Assessment.id == assessment_id, Assessment.active == "S").first()
        
        if not assessment_update: 
            NotFound()
        
        assessment_update.student_id      = assessment.student_id 
        assessment_update.course_id       = assessment.course_id
        assessment_update.grade           = assessment.grade
        assessment_update.semester        = assessment.semester
        assessment_update.evaluation_date = assessment.evaluation_date
        
        self.db.commit()
        self.db.refresh(assessment_update)
        return assessment_update
    
    @transactional
    def delete(self, assessment_id: int) -> dict:
        assessment_update = self.db.query(Assessment).filter(Assessment.id == assessment_id, Assessment.active == "S").first()
        
        if not assessment_update: 
            NotFound()
        
        assessment_update.active = "N"
        self.db.commit()
        self.db.refresh(assessment_update)
        return {"deleted": True}