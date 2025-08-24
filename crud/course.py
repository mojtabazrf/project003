from database import db
from bson import ObjectId

collection = db["courses"]

def create_course(course: dict):
    result = collection.insert_one(course)
    return str(result.inserted_id)

def get_courses():
    return [{**doc, "_id": str(doc["_id"])} for doc in collection.find()]

def get_course(id: str):
    return collection.find_one({"_id": ObjectId(id)})

def update_course(id: str, data: dict):
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return True

def delete_course(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return True

def get_courses_by_instructor(instructor_id: str):
    return [{**doc, "_id": str(doc["_id"])} for doc in collection.find({"instructor_id": instructor_id})]
