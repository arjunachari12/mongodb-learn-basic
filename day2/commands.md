```
db.products.insertOne({
    _id: 1,
    name: "Laptop",
    category: "Electronics",
    price: 999.99,
    stock: 50,
    details: {
        brand: "BrandName",
        model: "ModelX",
        specs: {
            cpu: "Intel i7",
            ram: "16GB",
            storage: "512GB SSD"
        }
    },
    tags: ["computing", "portable"]
})
===================
db.products.insertMany([
    {
        _id: 2,
        name: "Smartphone",
        category: "Electronics",
        price: 499.99,
        stock: 200,
        details: {
            brand: "BrandY",
            model: "ModelY",
            specs: {
                cpu: "Snapdragon 888",
                ram: "8GB",
                storage: "128GB"
            }
        },
        tags: ["mobile", "communication"]
    },
    {
        _id: 3,
        name: "Coffee Maker",
        category: "Home Appliances",
        price: 79.99,
        stock: 150,
        details: {
            brand: "BrandZ",
            model: "ModelC",
            features: ["auto shut-off", "programmable"]
        },
        tags: ["kitchen", "appliances"]
    }
])

=============================
db.products.updateMany({ category: "Electronics" },{ $set: { stock: 20 }})

================================
db.products.deleteMany({ category: "Electronics" })

========================

db.products.find({ price: { $gt: 100 } })

db.products.find({ stock: { $lte: 50 } }).pretty()

db.products.find({ price: { $gte: 50, $lte: 500 } }).pretty()

db.products.find({ $and: [{ category: "Electronics" }, { stock: { $gt: 100 } }] }).pretty()


================================

````
