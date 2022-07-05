from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zmalscx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

collection = db["students"]
collection.insert_one({"student_id":1010, "first_name":"John", "last_name":"Doe"})

print(1010)

db.students.find()
docs = db.collection.find()

for doc in docs:
    print(doc)

db.students.find_one
doc = db.collection.find_one({"student_id":1010})

collection = db["students"]
collection.delete_one({"student_id":1010, "first_name":"John", "last_name":"Doe"})

print(1010)

db.students.find()
docs = db.collection.find()

for doc in docs:
    print(doc)

db.students.find_one
doc = db.collection.find_one({"student_id":1010})