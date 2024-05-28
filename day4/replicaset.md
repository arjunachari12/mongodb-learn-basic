```
mongod --replSet rs0 --port 27017 --dbpath ~/mongo/rs0 --bind_ip localhost --logpath ~/mongo/rs0/mongod.log
mongod --replSet rs0 --port 27018 --dbpath ~/mongo/rs1 --bind_ip localhost --logpath ~/mongo/rs1/mongod.log
mongod --replSet rs0 --port 27019 --dbpath ~/mongo/rs2 --bind_ip localhost --logpath ~/mongo/rs2/mongod.log

mongosh --port 27017

rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "localhost:27017" },
    { _id: 1, host: "localhost:27018" },
    { _id: 2, host: "localhost:27019" }
  ]
})

rs.status()




```
