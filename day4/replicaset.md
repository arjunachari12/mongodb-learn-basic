```
mongod --replSet rs0 --port 27017 --dbpath ~/mongo/rs0 --bind_ip localhost --logpath ~/mongo/rs0/mongod.log
mongod --replSet rs0 --port 27018 --dbpath ~/mongo/rs1 --bind_ip localhost --logpath ~/mongo/rs1/mongod.log
mongod --replSet rs0 --port 27019 --dbpath ~/mongo/rs2 --bind_ip localhost --logpath ~/mongo/rs2/mongod.log
```
