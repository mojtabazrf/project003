from fastapi import APIRouter
from models.course import Course
from crud import course as crud

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("/")
def list_courses():
    return crud.get_courses()

@router.post("/")
def create_course(course: Course):
    return {"id": crud.create_course(course.model_dump())}

@router.get("/{id}")
def get_course(id: str):
    return crud.get_course(id)

@router.put("/{id}")
def update_course(id: str, course: Course):
    crud.update_course(id, course.model_dump())
    return {"status": "updated"}

@router.delete("/{id}")
def delete_course(id: str):
    crud.delete_course(id)
    return {"status": "deleted"}

@router.get("/instructor/{id}")
def get_courses_by_instructor(id: str):
    return crud.get_courses_by_instructor(id)
