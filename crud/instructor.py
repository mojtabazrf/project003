from database import db
from bson import ObjectId

collection = db["instructors"]

def create_instructor(instructor: dict):
    result = collection.insert_one(instructor)
    return str(result.inserted_id)

def get_instructors():
    return [{**doc, "_id": str(doc["_id"])} for doc in collection.find()]

def get_instructor(id: str):
    return collection.find_one({"_id": ObjectId(id)})

def update_instructor(id: str, data: dict):
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return True

def delete_instructor(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return True
