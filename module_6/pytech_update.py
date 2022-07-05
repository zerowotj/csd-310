from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zmalscx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

collection = db["students"]
collection.update_one({"student_id":1007, "first_name":"Fred", "last_name":"Freddy"})
result = db.collection.update_one({"student_id":1007}, {"$set": {"last_name": "Smith"}})