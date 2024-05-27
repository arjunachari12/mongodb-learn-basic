from pymongo import MongoClient, ASCENDING, DESCENDING
from pprint import pprint

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://arjun:m23tUZaaXqrSRF9N@sample-db.csprbsn.mongodb.net/?retryWrites=true&w=majority&appName=sample-db")

# Select the database and collection
db = client.retailDB1
products = db.products

# Sample retail data
data = [
    {
        "name": "Smartphone",
        "category": "Electronics",
        "price": 699.99,
        "stock": 150,
        "attributes": {
            "brand": "Samsung",
            "model": "Galaxy S21",
            "color": "Black",
            "screen_size": 6.2,
            "camera_resolution": "64 MP",
            "storage": "128 GB",
            "RAM": "8 GB"
        },
        "reviews": [
            {
                "username": "user123",
                "rating": 4.5,
                "comment": "Great phone, excellent camera!"
            },
            {
                "username": "user456",
                "rating": 3.0,
                "comment": "Battery life could be better."
            }
        ]
    },
    {
        "name": "Laptop",
        "category": "Electronics",
        "price": 1299.99,
        "stock": 80,
        "attributes": {
            "brand": "Apple",
            "model": "MacBook Pro",
            "color": "Silver",
            "screen_size": 13.3,
            "storage": "256 GB",
            "RAM": "8 GB"
        },
        "reviews": [
            {
                "username": "user789",
                "rating": 5.0,
                "comment": "Absolutely love it!"
            }
        ]
    },
    {
        "name": "Headphones",
        "category": "Accessories",
        "price": 199.99,
        "stock": 300,
        "attributes": {
            "brand": "Bose",
            "model": "QuietComfort 35",
            "color": "Black",
            "type": "Over-Ear",
            "wireless": True
        },
        "reviews": [
            {
                "username": "user321",
                "rating": 4.8,
                "comment": "Great noise cancellation!"
            },
            {
                "username": "user654",
                "rating": 4.2,
                "comment": "Comfortable and good sound quality."
            }
        ]
    }
]

products.insert_many(data)

products.create_index([("category", ASCENDING)])

def query_and_explain(filter_query, sort_query=None):
    explain_options = {"verbosity": "executionStats"}  # Specify options as a dictionary
    cursor = products.find(filter_query)
    if sort_query:
        cursor = cursor.sort(sort_query)
    result = cursor.explain()
    pprint(result)
