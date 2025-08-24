from fastapi import FastAPI
from routers import instructor, student, course, enrollment

app = FastAPI(title="Course Selling API")

# اضافه کردن روترها
app.include_router(instructor.router)
app.include_router(student.router)
app.include_router(course.router)
app.include_router(enrollment.router)

@app.get("/")
def home():
    return {"message": "Course Selling API is running 🚀"}
