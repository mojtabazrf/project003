from pydantic import BaseModel, Field
from typing import Optional

class InstructorCreate(BaseModel):
    name: str
    expertise: str

class Instructor(InstructorCreate):
    id: Optional[str] = Field(alias="_id")

    class Config:
        populate_by_name = True