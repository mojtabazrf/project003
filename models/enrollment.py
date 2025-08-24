from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timezone


class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: str
    timestamp: datetime = datetime.now(timezone.utc)

class Enrollment(EnrollmentCreate):
    id: Optional[str] = Field(alias="_id")

    class Config:
        populate_by_name = True