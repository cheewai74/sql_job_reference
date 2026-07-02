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
    DELETE FROM apress.item
    WHERE description ='Extension Plug' 
             RETURNING item_id;
''')


# 2. Now fetchone() will successfully grab the deleted ID
data = curr.fetchone()

if data is not None:
    print("Item ID of the deleted entry was:", data[0])
    conn.commit() # Save the deletion
else:
    print("No matching record was found to delete.")
    conn.commit()

# CLOSE THE CONNECTION
conn.close()