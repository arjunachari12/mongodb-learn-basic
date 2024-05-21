from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["arjun-python-db"]

collection = db["mycollection"]

collection.insert_one({"name": "arjun", "age": 30})

result = collection.find_one({"name": "arjun"})

print(result)
