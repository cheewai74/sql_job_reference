
fetchall:</BR>
```
# How to query data using fetchall()

# The fetchall() method fetches all the records that 
# we got from our SQL query 
# (the SELECT query in this case) and 
# provides them in a list. 
# The list consists of tuples where each 
# tuple consists of all the column values 
# present in the particular record.

# GET THE CONNECTION OBJECT

from postgres_conn import get_connection


conn = get_connection()
# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()
# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM apress.customer;")
# FETCH ALL THE ROWS FROM THE CURSOR
data = curr.fetchall()
# PRINT THE RECORDS
for row in data:
    print(row)
# CLOSE THE CONNECTION
conn.close()
```

fetchmany:</br>
```
# How to query data using fetchmany()

# The fetchmany() method takes in the no. of records 
# that we want to fetch from the entire dump. 
# It also behaves like a queue as we saw in 
# the fetchone() method, 
# except for the fact that it can fetch 
# more than one record at a time. 
# However, using fetchmany(1) is equivalent 
# to using fetchone() method. In the above 
# code, we used the fetchmany(2) to query the 
# first two records and then used the fetchmany(3) 
# to query the next 3 records. 
# The same can be noticed in the below output.

from postgres_conn import get_connection


# GET THE CONNECTION OBJECT
conn = get_connection()
# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()
# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM apress.customer;")
print("First two records:")
# GET FIRST TWO RECORDS FROM DATABASE TABLE
data1 = curr.fetchmany(2)
for row in data1:
    print(row)
print("Next three records:")
# GET NEXT THREE RECORDS FROM DATABASE TABLE
data2 = curr.fetchmany(3)
for row in data2:
    print(row)
# CLOSE THE CONNECTION
conn.close()
```

fetchone</br>
```
# How to query data using fetchone()

# The fetchone() method is not to be confused
# with the idea that it queries the first row only. 
# The fetchone() method returns the first record 
# from the dump that we got from the SQL query 
# present in curr.execute() method. It behaves like 
# a queue where we query the first record and then it 
# gets deleted from the cursor object. Now, if we 
# try to use the fetchone() method again, it will 
# return the next record.

from postgres_conn import get_connection


# GET THE CONNECTION OBJECT
conn = get_connection()
# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()
# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM apress.customer;")
# FETCH THE FIRST ROW FROM THE CURSOR
data1 = curr.fetchone()
print(data1)
# FETCH THE SECOND ROW FROM THE CURSOR
data2 = curr.fetchone()
print(data2)
# CLOSE THE CONNECTION
conn.close()
```
