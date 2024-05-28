```
use admin

db.createUser({
  user: "admin",
  pwd: "adminpassword",
  roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
})

mongod --auth --dbpath /path/to/your/db --bind_ip 127.0.0.1

mongosh -u "admin" -p "adminpassword" --authenticationDatabase "admin"

use yourdatabase

db.createUser({
  user: "appuser",
  pwd: "apppassword",
  roles: [{ role: "readWrite", db: "yourdatabase" }]
})

mongosh -u "appuser" -p "apppassword" --authenticationDatabase "yourdatabase"


```
