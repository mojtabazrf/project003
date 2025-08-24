from fastapi import APIRouter
from models.student import Student
from crud import student as crud

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/")
def list_students():
    return crud.get_students()

@router.post("/")
def create_student(student: Student):
    return {"id": crud.create_student(student.model_dump())}

@router.get("/{id}")
def get_student(id: str):
    return crud.get_student(id)

@router.put("/{id}")
def update_student(id: str, student: Student):
    crud.update_student(id, student.model_dump())
    return {"status": "updated"}

@router.delete("/{id}")
def delete_student(id: str):
    crud.delete_student(id)
    return {"status": "deleted"}
