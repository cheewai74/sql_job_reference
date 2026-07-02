
Insert Record:</BR>
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
    
# GET THE CONNECTION OBJECT
conn = get_connection()

# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()

#  delete from apress.item where description ='Extension Plug'

# EXECUTE THE SQL QUERY
curr.execute('''
    INSERT INTO apress.item(description, cost_price, sell_price) 
             VALUES('Extension Plug', 15.40, 25.95)
             RETURNING item_id;
''')

# FETCH THE LATEST USER ID USING THE CURSOR
data = curr.fetchone()

# Check if data actually exists before printing
if data is not None:
    print("Item ID of latest entry:", data[0])
    conn.commit()
else:
    print("The database returned nothing! Check your table triggers or rules.")
    conn.rollback() # Undo the blank transaction

# CLOSE THE CONNECTION
conn.close()
```
