import io
import random

import psycopg2
from faker import Faker
from psycopg2 import sql

fake = Faker()

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="source_db", user="postgres", password="1", host="localhost", port="54323"
)
cur = conn.cursor()

# 10 schemas
schemas = [f"schema_{i}" for i in range(1, 11)]

# Total rows per table across all schemas (~50M total)
total_rows_per_table = {
    "users": 5_000_000,
    "products": 2_500_000,
    "orders": 10_000_000,
    "operations": 15_000_000,
    "payments": 17_500_000,
}

# Compute rows per table per schema
rows_per_schema_table = {
    table: total_rows // len(schemas)
    for table, total_rows in total_rows_per_table.items()
}

# Columns for each table (excluding SERIAL IDs)
columns_map = {
    "users": ["name", "email"],
    "products": ["name", "price", "stock"],
    "orders": ["user_id", "total", "status"],
    "operations": ["order_id", "operation_type"],
    "payments": ["order_id", "amount", "payment_method"],
}


# Row generator functions
def generate_user():
    return [fake.name(), fake.email()]


def generate_product():
    return [fake.word(), f"{random.uniform(1, 1000):.2f}", str(random.randint(0, 1000))]


def generate_order():
    return [
        str(random.randint(1, 500_000)),
        f"{random.uniform(10, 5000):.2f}",
        random.choice(["pending", "shipped", "completed", "cancelled"]),
    ]


def generate_operation():
    return [
        str(random.randint(1, 1_000_000)),
        random.choice(["create", "update", "delete", "ship"]),
    ]


def generate_payment():
    return [
        str(random.randint(1, 1_000_000)),
        f"{random.uniform(10, 5000):.2f}",
        random.choice(["cash", "card", "paypal"]),
    ]


generate_funcs = {
    "users": generate_user,
    "products": generate_product,
    "orders": generate_order,
    "operations": generate_operation,
    "payments": generate_payment,
}


# Batch insert function using COPY
def batch_copy(schema, table, rows, generator_fn, columns):
    batch_size = 100_000  # adjust depending on RAM
    for start in range(0, rows, batch_size):
        buffer = io.StringIO()
        for _ in range(min(batch_size, rows - start)):
            buffer.write("\t".join(generator_fn()) + "\n")
        buffer.seek(0)

        copy_sql = sql.SQL(
            "COPY {} ({}) FROM STDIN WITH (FORMAT text, DELIMITER E'\t')"
        ).format(
            sql.Identifier(schema, table),
            sql.SQL(", ").join(map(sql.Identifier, columns)),
        )
        cur.copy_expert(copy_sql, buffer)
        conn.commit()
        print(
            f"Inserted {min(start + batch_size, rows)}/{rows} rows into {schema}.{table}"
        )


# Create schemas if they don’t exist
for schema in schemas:
    cur.execute(
        sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(schema))
    )

# Insert data into all tables in all schemas
for schema in schemas:
    for table, rows in rows_per_schema_table.items():
        print(f"Starting insert for {schema}.{table} ({rows} rows)...")
        batch_copy(schema, table, rows, generate_funcs[table], columns_map[table])

cur.close()
conn.close()
print("Batch insert completed for all schemas and tables (~50M rows total)")
