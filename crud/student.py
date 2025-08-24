from database import db
from bson import ObjectId

collection = db["students"]

def create_student(student: dict):
    result = collection.insert_one(student)
    return str(result.inserted_id)

def get_students():
    return [{**doc, "_id": str(doc["_id"])} for doc in collection.find()]

def get_student(id: str):
    return collection.find_one({"_id": ObjectId(id)})

def update_student(id: str, data: dict):
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return True

def delete_student(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return True
