import psycopg2

with psycopg2.connect(database="postgres", user="postgres", 
                     password="password", host="127.0.0.1", 
                     port=5432,) as conn:
    
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS
            sandbox.pets ( name TEXT, weight_kg REAL, birthday DATE);
        """) 

        cursor.execute("""
            INSERT INTO sandbox.pets (name, weight_kg, birthday)
            VALUES (%s, %s, %s)
        """, ('Pit Bull', 24.3, '2022-10-18'))

        cursor.execute("SELECT * FROM sandbox.pets")
        print(cursor.fetchone()) 

        conn.commit()