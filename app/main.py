from fastapi import FastAPI, APIRouter
from app.database.DataBase import SessionLocal
from app.routers.CourseRouter import CourseRouter
from app.routers.ProfessorRouter import ProfessorRouter
from app.routers.StudentRouter import StudentRouter
from app.routers.AssessmentRouter import AssessmentRouter


#Base.metadata.create_all(bind=engine)

app = FastAPI()
db = SessionLocal()

student_router = StudentRouter()
app.include_router(student_router.router)

professor_router = ProfessorRouter()
app.include_router(professor_router.router)

course_router = CourseRouter()
app.include_router(course_router.router)

assessment_router = AssessmentRouter()
app.include_router(assessment_router.router)
