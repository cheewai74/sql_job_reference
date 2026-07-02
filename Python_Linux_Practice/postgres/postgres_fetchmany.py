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