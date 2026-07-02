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

