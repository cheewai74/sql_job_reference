pip install --upgrade pip setuptools wheel</br>
pip install psycopg2</br>
pip install psycopg2-binary</br>

Notes:</br>
1. https://www.psycopg.org/docs/usage.html</br>
2. https://www.geeksforgeeks.org/python/python-psycopg2-getting-id-of-row-just-inserted/</br>
3. https://www.postgresql.org/docs/current/plpython.html</br>
4. https://www.psycopg.org/#home</br>
5. https://www.geeksforgeeks.org/python/postgresql-python-querying-data/</br>

Connetions:</BR>
```
import psycopg2
def get_connection():
    try:
        return psycopg2.connect(
            database="postgres",
            user="postgres",
            password="password",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False
conn = get_connection()
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered
```

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
