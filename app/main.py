from fastapi import FastAPI, APIRouter
from app.database.DataBase import SessionLocal
from app.routers.CourseRouter import CourseRouter
from app.routers.ProfessorRouter import ProfessorRouter
from app.routers.StudentRouter import StudentRouter
from app.schema.Course import CourseData
from app.schema.Professor import ProfessorData
from app.schema.Student import StudentData
from app.services.CourseService import CourseService
from app.services.ProfessorService import ProfessorService
from app.services.StudentService import StudentService

#Base.metadata.create_all(bind=engine)
app = FastAPI()
db = SessionLocal()

student_service = StudentService(db)
student_router = StudentRouter(student_service)
router_student = APIRouter(prefix="/student", tags=["Student"])
router_student.add_api_route("/", student_router.getAll, methods=["GET"], response_model=list[StudentData])
router_student.add_api_route("/{student_id}", student_router.getById, methods=["GET"], response_model=StudentData)
router_student.add_api_route("/", student_router.create, methods=["POST"], response_model=StudentData)
router_student.add_api_route("/{student_id}", student_router.put, methods=["PUT"], response_model=StudentData)
router_student.add_api_route("/{student_id}", student_router.delete, methods=["DELETE"], response_model=dict)
app.include_router(router_student)

professor_service = ProfessorService(db)
professor_router = ProfessorRouter(professor_service)
router_professor = APIRouter(prefix="/professor", tags=["Professor"])
router_professor.add_api_route("/", professor_router.getAll, methods=["GET"], response_model=list[ProfessorData])
router_professor.add_api_route("/{professor_id}", professor_router.getById, methods=["GET"], response_model=ProfessorData)
router_professor.add_api_route("/", professor_router.post, methods=["POST"], response_model=ProfessorData)
router_professor.add_api_route("/{professor_id}", professor_router.put, methods=["PUT"], response_model=ProfessorData)
router_professor.add_api_route("/{professor_id}", professor_router.delete, methods=["DELETE"], response_model=dict)
app.include_router(router_professor)

course_service = CourseService(db)
course_router = CourseRouter(professor_service)
router_course = APIRouter(prefix="/course", tags=["Course"])
router_course.add_api_route("/", course_router.getAll, methods=["GET"], response_model=list[CourseData])
app.include_router(router_course)
