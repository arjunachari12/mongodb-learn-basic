from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Select the retail database and products collection
db = client.retail3
products_collection = db.products

# Create (Insert) documents
def insert_products():
    products = [
        {
            "_id": 1,
            "name": "Laptop",
            "category": "Electronics",
            "price": 999.99,
            "stock": 50,
            "details": {
                "brand": "BrandName",
                "model": "ModelX",
                "specs": {
                    "cpu": "Intel i7",
                    "ram": "16GB",
                    "storage": "512GB SSD"
                }
            },
            "tags": ["computing", "portable"]
        },
        {
            "_id": 2,
            "name": "Smartphone",
            "category": "Electronics",
            "price": 499.99,
            "stock": 200,
            "details": {
                "brand": "BrandY",
                "model": "ModelY",
                "specs": {
                    "cpu": "Snapdragon 888",
                    "ram": "8GB",
                    "storage": "128GB"
                }
            },
            "tags": ["mobile", "communication"]
        },
        {
            "_id": 3,
            "name": "Coffee Maker",
            "category": "Home Appliances",
            "price": 79.99,
            "stock": 150,
            "details": {
                "brand": "BrandZ",
                "model": "ModelC",
                "features": ["auto shut-off", "programmable"]
            },
            "tags": ["kitchen", "appliances"]
        }
    ]
    products_collection.insert_many(products)
    print("Documents inserted")

# Read (Query) documents
def read_products():
    # Find all products
    all_products = products_collection.find()
    print("All products:")
    for product in all_products:
        print(product)

    # Find products where category is "Electronics"
    electronics = products_collection.find({"category": "Electronics"})
    print("\nElectronics:")
    for product in electronics:
        print(product)

    # Find products where price is greater than $100
    expensive_products = products_collection.find({"price": {"$gt": 100}})
    print("\nExpensive products:")
    for product in expensive_products:
        print(product)

# Update documents
def update_products():
    # Update stock to 20 for all products in the "Electronics" category
    result = products_collection.update_many(
        {"category": "Electronics"},
        {"$set": {"stock": 20}}
    )
    print(f"{result.modified_count} documents updated")

# Delete documents
def delete_products():
    # Delete all products in the "Electronics" category
    result = products_collection.delete_many({"category": "Electronics"})
    print(f"{result.deleted_count} documents deleted")

# Perform CRUD operations
insert_products()
read_products()
update_products()
read_products()
delete_products()
read_products()

# Close the connection
client.close()
