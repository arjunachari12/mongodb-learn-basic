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
