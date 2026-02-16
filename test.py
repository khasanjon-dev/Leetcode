import psycopg2
from psycopg2 import sql

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="source_db",
    user="postgres",
    password="1",
    host="localhost",
    port="54323",
)
conn.autocommit = True
cur = conn.cursor()

# Define schemas
schemas = [f"schema_{i}" for i in range(1, 11)]
# schemas = ["public"]
# Define tables with their SQL structures
tables = {
    "users": """
             CREATE TABLE IF NOT EXISTS {table} (
                                                    id SERIAL PRIMARY KEY,
                                                    name VARCHAR(100) NOT NULL,
                 email VARCHAR(100) NOT NULL,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )
             """,
    "products": """
                CREATE TABLE IF NOT EXISTS {table} (
                                                       id SERIAL PRIMARY KEY,
                                                       name VARCHAR(100) NOT NULL,
                    price NUMERIC(10,2) NOT NULL,
                    stock INT DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """,
    "orders": """
              CREATE TABLE IF NOT EXISTS {table} (
                                                     id SERIAL PRIMARY KEY,
                                                     user_id INT NOT NULL,
                                                     total NUMERIC(10,2) NOT NULL,
                  status VARCHAR(50) DEFAULT 'pending',
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                  )
              """,
    "operations": """
                  CREATE TABLE IF NOT EXISTS {table} (
                                                         id SERIAL PRIMARY KEY,
                                                         order_id INT NOT NULL,
                                                         operation_type VARCHAR(50),
                      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                      )
                  """,
    "payments": """
                CREATE TABLE IF NOT EXISTS {table} (
                                                       id SERIAL PRIMARY KEY,
                                                       order_id INT NOT NULL,
                                                       amount NUMERIC(10,2) NOT NULL,
                    payment_method VARCHAR(50),
                    paid_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """,
}

# Loop through schemas and tables to create them
for schema in schemas:
    # Create schema
    cur.execute(
        sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(schema))
    )

    # Create tables in this schema
    for table_name, table_sql in tables.items():
        full_table_name = sql.Identifier(schema, table_name)
        cur.execute(sql.SQL(table_sql).format(table=full_table_name))

print("Schemas and tables created successfully!")

cur.close()
conn.close()
