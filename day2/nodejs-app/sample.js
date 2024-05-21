// Import the MongoDB Node.js driver
const { MongoClient } = require('mongodb');

// MongoDB connection URI
const uri = "mongodb://localhost:27017/";

// Create a new MongoClient
const client = new MongoClient(uri);

// Define the database name and collection name
const dbName = 'mydatabase5';
const collectionName = 'mycollection';

async function main() {
    try {
        // Connect to MongoDB
        await client.connect();

        // Access a database
        const database = client.db(dbName);

        // Access a collection
        const collection = database.collection(collectionName);

        // Insert a document
        const result = await collection.insertOne({ name: "Alice", age: 30 });
        console.log("Inserted document with _id:", result.insertedId);

        // Find documents
        const query = { name: "Alice" };
        const foundDocument = await collection.findOne(query);
        console.log("Found document:", foundDocument);
    } catch (error) {
        console.error("Error:", error);
    } finally {
        // Close the connection
        await client.close();
    }
}

// Call the main function
main().catch(console.error);
