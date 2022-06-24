import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zmalscx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)
collection = db["students"]
collection.insert_one({"_id":1, "student_id":23, "first_name":"Willy", "last_name":"Wonka"})


