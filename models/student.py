from pydantic import BaseModel, Field
from typing import Optional

class StudentCreate(BaseModel):
    name: str
    email: str

class Student(StudentCreate):
    id: Optional[str] = Field(alias="_id")

    class Config:
        populate_by_name = True