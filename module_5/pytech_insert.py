from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.zmalscx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

collection = db["students"]
collection.insert_one({"student_id":1007, "first_name":"Fred", "last_name":"Freddy"})

print(1007)

db.students.find()
docs = db.collection.find()

for doc in docs:
    print(doc)

db.students.find_one
doc = db.collection.find_one({"student_id":1007})

collection = db["students"]
collection.insert_one({"student_id":1008, "first_name":"Willy", "last_name":"Wonka"})

print(1008)

db.students.find()
docs = db.collection.find()

for doc in docs:
    print(doc)

db.students.find_one
doc = db.collection.find_one({"student_id":1008})

collection = db["students"]
collection.insert_one({"student_id":1009, "first_name":"Bill", "last_name":"Ted"})

print(1009)

db.students.find()
docs = db.collection.find()

for doc in docs:
    print(doc)

db.students.find_one
doc = db.collection.find_one({"student_id":1009})

