from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["exampleMany"]
collection = db["users"]

sample_users = [
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 35, "email": "bob@example.com"},
    {"name": "Charlie", "age": 25, "email": "charlie@example.com"}
]

def insert_many_users(users):
    result = collection.insert_many(users)

if __name__ == "__main__":
    # Insert many
    insert_many_users(sample_users)
