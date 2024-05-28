import pymongo
import random

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["my_database"]  # Choose your database

# Access the orders collection
orders_collection = db["orders"]

# Insert sample data into the orders collection
for i in range(1, 1001):
    order = {
        "_id": i,
        "customer_id": "customer_" + str(i),
        "total_amount": random.randint(1, 1000),  # Random integer between 1 and 1000
        "status": "completed" if random.random() > 0.5 else "pending"  # Randomly choose status
    }
    orders_collection.insert_one(order)

# Close the connection
client.close()
