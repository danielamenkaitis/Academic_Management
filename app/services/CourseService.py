from sqlalchemy.orm import Session
from app.models.Course import Course
from app.schema.Course import CourseData
from app.util.util import NotFound, transactional


class CourseService: 
    def __init__(self, db: Session):
        self.db = db 
        
    def getAll(self):
        course = self.db.query(Course).filter(Course.active=="S").all()
        if not course: 
            NotFound()
        return course
    
    def getById(self, course_id: int):
        course = self.db.query(Course).filter(Course.id == course_id, Course.active=="S").first()
        if not course: 
            NotFound()
        return course
    
    @transactional
    def post(self, course: CourseData): 
        course_new = Course(**course.dict())
        self.db.add(course_new)
        self.db.commit()
        self.db.refresh(course_new)
        return course_new
    
    @transactional
    def put(self, course_id, course: CourseData):
        course_update = self.db.query(Course).filter(Course.id == course_id, Course.active == "S" ).first()
        if not course_update:
            NotFound()
        course_update.course_name  = course_update.course_name
        course_update.course_code  = course_update.course_code
        course_update.credit_hours = course_update.credit_hours
        course_update.professor_id = course_update.professor_id
        self.db.commit()
        self.db.refresh(course_update)
        return course_update    
    
    @transactional
    def delete(self, course_id: int) -> dict:
        course_update = self.db.query(Course).filter(Course.id == course_id, Course.active == "S" ).first() 
        
        if not course_update: 
            NotFound()
            
        course_update.active = "N"
        self.db.commit()
        return {"deleted": True}
        
    
    
        