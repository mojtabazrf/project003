from fastapi import APIRouter
from models.instructor import Instructor
from crud import instructor as crud

router = APIRouter(prefix="/instructor", tags=["instructor"])

@router.get("/")
def list_instructors():
    return crud.get_instructors()

@router.post("/")
def create_instructor(instructor: Instructor):
    return {"id": crud.create_instructor(instructor.model_dump())}

@router.get("/{id}")
def get_instructor(id: str):
    return crud.get_instructor(id)

@router.put("/{id}")
def update_instructor(id: str, instructor: Instructor):
    crud.update_instructor(id, instructor.model_dump())
    return {"status": "updated"}

@router.delete("/{id}")
def delete_instructor(id: str):
    crud.delete_instructor(id)
    return {"status": "deleted"}
