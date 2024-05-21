from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase3-new"]
collection = db["users"]

# Sample data
sample_users = [
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 35, "email": "bob@example.com"},
    {"name": "Charlie", "age": 25, "email": "charlie@example.com"}
]

# Insert many
def insert_many_users(users):
    result = collection.insert_many(users)
    print("Inserted", len(result.inserted_ids), "users")

# Update many
def update_users_age():
    result = collection.update_many({}, {"$inc": {"age": 1}})
    print("Updated", result.modified_count, "users")

# Delete many
def delete_users_age_gt(age):
    result = collection.delete_many({"age": {"$gt": age}})
    print("Deleted", result.deleted_count, "users")

# Test insert_many, update_many, delete_many operations
if __name__ == "__main__":
    # Insert many
    insert_many_users(sample_users)

    # Display all users
    print("All users:")
    for user in collection.find():
        print(user)

    # Update many
    update_users_age()

    # Display all users after update
    print("All users after age update:")
    for user in collection.find():
        print(user)

    # Delete many
    delete_users_age_gt(30)

    # Display all users after delete
    print("All users after deletion:")
    for user in collection.find():
        print(user)
