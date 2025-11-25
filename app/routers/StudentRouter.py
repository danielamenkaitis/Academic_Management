from typing import List
from app.schema.Student import StudentData
from app.services.StudentService import StudentService

class StudentRouter:
    def __init__(self, service: StudentService):
        self.service = service

    def getAll(self) -> List[StudentData]:
        return self.service.getAll()
    
    def getById(self, student_id: int) -> List[StudentData]:
        return self.service.getById(student_id)

    def create(self, student: StudentData) -> StudentData:
        return self.service.post(student)
   
    def put(self, student_id: int, student : StudentData) -> StudentData:
        return self.service.put(student_id, student)
    
    def delete(self, student_id: int) -> dict:
        return self.service.delete(student_id) 
