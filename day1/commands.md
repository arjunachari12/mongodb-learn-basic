```
show bds

use admin

show collections

db.my_collection.insertOne({ "name": "arjun" })

db.mycollection.findOne()

db.mycollection.find()

db.mycollection.insertOne({ "name": "arjun1" })

db.employee.insertOne({"id":1,"name":"arjun","age":30,"isStudent":true,"address":{"street":"2nd","city":"bangalore","country":"india"},"hobbies":["football","program"]})

db.student.insertOne({"_id":1,"name":"arjun","age":30,"isStudent":true,"address":{"street":"2nd","city":"bangalore","country":"india"},"hobbies":["football","program"]})

db.mycollection2.insertOne({ name: "arjun", age: 30 })

db.mycollection2.updateOne({ name: "arjun" },{ $set: { age: 35 }})

db.mycollection2.find()

db.employee.updateOne({_id: 1}, {$set: {"address.street": "3rd", hobbies: ["football", "cricket"]}})
```
