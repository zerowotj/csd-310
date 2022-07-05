from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zmalscx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
collection = db["students"]

print(1007)

db.students.find()
docs = db.collection.find()

for doc in docs:
    print(doc)

db.students.find_one
doc = db.collection.find_one({"student_id":1007})