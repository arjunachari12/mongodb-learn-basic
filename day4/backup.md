```
#Backup command
#create a directory to store backups
mongodump --db yourDatabaseName --out /path/to/backup/directory

mongodump --out /path/to/backup/directory

#restore command
mongorestore --db yourDatabaseName /path/to/backup/directory/yourDatabaseName
```
