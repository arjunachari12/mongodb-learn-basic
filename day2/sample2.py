from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["arjun-python-db"]

collection = db["mycollection"]

collection.insert_one({"name": "arjun", "age": 30})

documents = collection.find()

for document in documents:
    print(document)
