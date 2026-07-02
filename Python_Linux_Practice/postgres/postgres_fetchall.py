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