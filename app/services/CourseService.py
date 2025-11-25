from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Course


class CourseService: 
    def __init__(self, db: Session):
        self.db = db 
        
    def NotFound(self):
        raise HTTPException(status_code=404, detail="Not Found")  
    
    def getAll(self):
        courses = self.db.query(Course).filter(Course.active=="S").all()
        if not courses: 
            self.NotFound()
            return courses