from fastapi import APIRouter
from models.enrollment import Enrollment
from crud import enrollment as crud

router = APIRouter(prefix="/enrollments", tags=["enrollments"])

@router.get("/")
def list_enrollments():
    return crud.get_enrollments()

@router.post("/")
def create_enrollment(enrollment: Enrollment):
    return {"id": crud.create_enrollment(enrollment.model_dump())}

@router.delete("/{id}")
def delete_enrollment(id: str):
    crud.delete_enrollment(id)
    return {"status": "deleted"}

@router.get("/student/{id}")
def get_courses_by_student(id: str):
    return crud.get_courses_by_student(id)

@router.get("/course/{id}")
def get_students_by_course(id: str):
    return crud.get_students_by_course(id)
