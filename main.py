from fastapi import FastAPI,HTTPException, status, APIRouter
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, timezone
from pymongo import MongoClient
from bson import ObjectId

# --------------------------
# Database Connection
# --------------------------
client = MongoClient("mongodb://localhost:27017")
db = client["course_api_db"]
Instructor_col = db["instructor"]
Student_col = db["student"]
Course_col = db["course"]
Enrollment_col = db["enrollment"]

# --------------------------
# Models
# --------------------------
class InstructorCreate(BaseModel):
    name: str
    expertise: str

class Instructor(InstructorCreate):
    id: Optional[str] = Field(alias="_id")

    class Config:
        populate_by_name = True



class StudentCreate(BaseModel):
    name: str
    email: str

class Student(StudentCreate):
    id: Optional[str] = Field(alias="_id")

    class Config:
        populate_by_name = True



class CourseCreate(BaseModel):
    title: str
    description: str
    instructor_id: str

class Course(CourseCreate):
    id: Optional[str] = Field(alias="_id")

    class Config:
        populate_by_name = True



class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: str
    timestamp: datetime = datetime.now(timezone.utc)

class Enrollment(EnrollmentCreate):
    id: Optional[str] = Field(alias="_id")

    class Config:
        populate_by_name = True


# --------------------------
# FastAPI App
# --------------------------
app = FastAPI(title="Course Selling API")

# --------------------------
# Instructor Endpoints
# --------------------------
instructor_router = APIRouter(prefix="/instructor", tags=["instructor"])

@instructor_router.post("/instructors/")
def create_instructor(instructor: InstructorCreate):
    result = Instructor_col.insert_one(instructor.model_dump())
    return Instructor(id=str(result.inserted_id), **instructor.model_dump())





























# --------------------------
# Include Routers
# --------------------------
app.include_router(instructor_router)