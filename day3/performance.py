import time
from pymongo import MongoClient

client = MongoClient("mongodb+srv://arjun:m23tUZaaXqrSRF9N@sample-db.csprbsn.mongodb.net/?retryWrites=true&w=majority&appName=sample-db")

db = client.retailDB5
products_collection = db.products

def insert_sample_data():
    data = [
        {"name": "Laptop", "category": "Electronics", "price": 999.99, "stock": 50},
        {"name": "Smartphone", "category": "Electronics", "price": 499.99, "stock": 200},
        {"name": "Coffee Maker", "category": "Home Appliances", "price": 79.99, "stock": 150}
    ]
    products_collection.insert_many(data)
    print("Sample data inserted.")

# Function to execute sample queries
def execute_queries():
    # Query 1: Find all products
    start_time = time.time()
    all_products = products_collection.find()
    end_time = time.time()
    print(f"Query 'Find all products' executed in {(end_time - start_time) * 1000} milliseconds.")
    for product in all_products:
        print(product)

    # Query 2: Find products with category "Electronics" (Using Index)
    start_time = time.time()
    electronics_products = products_collection.find({"category": "Electronics"})
    end_time = time.time()
    print(f"\nQuery 'Find electronics products' executed in {(end_time - start_time) * 1000} milliseconds.")
    for product in electronics_products:
        print(product)

    # Query 3: Find products with category "Electronics" with only name and price fields (Query Projection)
    start_time = time.time()
    electronics_products_projection = products_collection.find({"category": "Electronics"}, {"name": 1, "price": 1, "_id": 0})
    end_time = time.time()
    print(f"\nQuery 'Find electronics products with projection' executed in {(end_time - start_time) * 1000} milliseconds.")
    for product in electronics_products_projection:
        print(product)

# Insert sample data
insert_sample_data()

# Execute sample queries
execute_queries()

# Close the connection
client.close()
