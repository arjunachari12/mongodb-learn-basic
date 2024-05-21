from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase-new"]
collection = db["users"]

# Create
def create_user(user_data):
    result = collection.insert_one(user_data)
    print("User created with id:", result.inserted_id)

# Read
def find_user_by_name(name):
    user = collection.find_one({"name": name})
    if user:
        print("User found:", user)
    else:
        print("User not found")

def find_users_by_age_range(min_age, max_age):
    users = collection.find({"age": {"$gte": min_age, "$lte": max_age}})
    print("Users found:")
    for user in users:
        print(user)

# Update
def update_user(user_name, new_data):
    result = collection.update_one({"name": user_name}, {"$set": new_data})
    if result.modified_count > 0:
        print("User updated successfully")
    else:
        print("User not found")

# Delete
def delete_user(user_name):
    result = collection.delete_one({"name": user_name})
    if result.deleted_count > 0:
        print("User deleted successfully")
    else:
        print("User not found")

# Test CRUD operations
if __name__ == "__main__":
    # Create
    create_user({"name": "Alice", "age": 30, "email": "alice@example.com"})

    # Read
    find_user_by_name("Alice")
    find_users_by_age_range(25, 35)

    # Update
    update_user("Alice", {"age": 31})

    # Delete
    delete_user("Alice")
