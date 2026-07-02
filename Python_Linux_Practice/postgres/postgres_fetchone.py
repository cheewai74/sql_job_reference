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