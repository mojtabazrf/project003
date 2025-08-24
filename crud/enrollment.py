from database import db
from bson import ObjectId

collection = db["enrollments"]

def create_enrollment(enrollment: dict):
    result = collection.insert_one(enrollment)
    return str(result.inserted_id)

def get_enrollments():
    return [{**doc, "_id": str(doc["_id"])} for doc in collection.find()]

def delete_enrollment(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return True

def get_courses_by_student(student_id: str):
    return [{**doc, "_id": str(doc["_id"])} for doc in collection.find({"student_id": student_id})]

def get_students_by_course(course_id: str):
    return [{**doc, "_id": str(doc["_id"])} for doc in collection.find({"course_id": course_id})]
