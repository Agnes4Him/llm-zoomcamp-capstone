import os
from pathlib import Path

import psycopg2

sql_file = Path(__file__).parent / "init_postgres_db.sql"

conn = psycopg2.connect(
    dbname=os.getenv('POSTGRES_DB', 'project_db'),
    user=os.getenv('POSTGRES_USER', 'project_user'),
    password=os.getenv('POSTGRES_PASSWORD', ''),
    host=os.getenv('POSTGRES_HOST', 'localhost'),
    port=os.getenv('POSTGRES_PORT', '5432'),
)

with conn.cursor() as cursor:
    with open(sql_file, "r") as f:
        cursor.execute(f.read())
    conn.commit()

conn.close()
print("PostgreSQL tables and sample data populated successfully!")