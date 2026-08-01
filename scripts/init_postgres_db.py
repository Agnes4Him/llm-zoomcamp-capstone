import psycopg2

conn = psycopg2.connect(
    dbname="healthsecure",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432",
)

with conn.cursor() as cursor:
    with open("init_postgres_db.sql", "r") as f:
        cursor.execute(f.read())
    conn.commit()

conn.close()
print("PostgreSQL tables and sample data populated successfully!")