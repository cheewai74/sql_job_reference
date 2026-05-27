
Create database:</br>
```
createdb -h localhost -p <port> -U <user> <database name>

createdb -h localhost -p 5432 -U postgres two_trees

```

List the database:</BR>
```
psql -h localhost -p 5432 -U postgres -l
```


Connect to the database:</BR>
```
psql -h localhost -d <database> -U <user>

psql -h localhost -d two_trees -U postgres
```
