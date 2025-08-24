from pydantic import BaseModel, Field
from typing import Optional

class CourseCreate(BaseModel):
    title: str
    description: str
    instructor_id: str

class Course(CourseCreate):
    id: Optional[str] = Field(alias="_id")

    class Config:
        populate_by_name = True