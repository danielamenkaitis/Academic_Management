from typing import List
from app.schema.Course import CourseData
from app.services.CourseService import CourseService

#CourseRouter é molde
#__init__ método do construtor da classe,
# chamado automaticamente quando você cria um objeto dessa classe.
class CourseRouter():
    def __init__(self, service: CourseService):
        self.service = service
        
    def getAll(self) -> List[CourseData]:
        return self.service.getAll()
        

        

        