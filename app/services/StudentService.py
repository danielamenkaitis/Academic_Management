from sqlalchemy.orm import Session
from app.models.Student import Student
from app.schema.Student import StudentData
from app.util.util import NotFound, transactional

class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def getAll(self):
        students = self.db.query(Student).filter(Student.active=="S").all()
        if not students:
            NotFound()
        return students
   
    # GET by id------------------------------------------------------------------
    def getById(self, student_id: int):
        student = self.db.query(Student).filter(Student.id == student_id, Student.active=="S").first()
        if not student:
            NotFound()
        return student
    
    
    # POST------------------------------------------------------------------
    @transactional
    def post(self, student: StudentData):
        student_new = Student(**student.dict())
        self.db.add(student_new)
        self.db.commit()
        self.db.refresh(student_new)
        return student_new
    
    # PUT (update)------------------------------------------------------------------
    @transactional
    def put(self, student_id: int, student: StudentData):
        student_update = self.db.query(Student).filter(Student.id == student_id, Student.active=="S").first()
        
        if not student_update:
            NotFound()
            
        student_update.full_name             = student.full_name
        student_update.enrollment_number     = student.enrollment_number
        student_update.course                = student.course
        self.db.commit()
        self.db.refresh(student_update)
        return student_update

    # DELETE------------------------------------------------------------------
    @transactional
    def delete(self, student_id: int) -> dict:
        student_update = self.db.query(Student).filter(Student.id == student_id, Student.active=="S").first()
        if not student_update:
            NotFound()
        student_update.active  = "N"
        self.db.commit()
        return {"deleted": True}
      
