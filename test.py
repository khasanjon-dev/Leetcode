import re
# from clickhouse_driver import Client

# Mapping of PostgreSQL data types to ClickHouse data types
TYPE_MAPPING = {
    "smallint": "Int16",
    "integer": "Int32",
    "bigint": "Int64",
    "serial": "UInt32",
    "bigserial": "UInt64",
    "real": "Float32",
    "double precision": "Float64",
    "numeric": "Decimal",
    "decimal": "Decimal",
    "boolean": "UInt8",
    "varchar": "String",
    "char": "String",
    "text": "String",
    "date": "Date",
    "timestamp": "DateTime",
    "timestamptz": "DateTime",
    "json": "String",
    "jsonb": "String",
    "uuid": "UUID",
    "bytea": "String",
}

# Function to parse PostgreSQL CREATE TABLE statement
def parse_postgres_create_table(psql_statement):
    # Extract table name
    table_name_match = re.search(r"CREATE TABLE (\w+)", psql_statement, re.IGNORECASE)
    if not table_name_match:
        raise ValueError("Table name not found in the CREATE TABLE statement.")
    table_name = table_name_match.group(1)

    # Extract column definitions
    column_definitions = re.findall(r"(\w+)\s+([\w\(\)\s,]+)(?:,|\))", psql_statement)

    # Extract constraints (if any)
    constraints = re.findall(r"CONSTRAINT\s+(\w+)\s+(.*?)(?:,|\))", psql_statement)

    return table_name, column_definitions, constraints

# Function to convert PostgreSQL column definitions to ClickHouse
def convert_column_definitions(column_definitions):
    clickhouse_columns = []
    for col_name, col_type in column_definitions:
        # Extract base type (e.g., "numeric(10, 2)" -> "numeric")
        base_type = re.sub(r"\(.*\)", "", col_type).lower()

        # Map PostgreSQL type to ClickHouse type
        if base_type in TYPE_MAPPING:
            clickhouse_type = TYPE_MAPPING[base_type]
            # Handle precision/scale for numeric/decimal
            if base_type in ["numeric", "decimal"]:
                precision_scale = re.search(r"\((\d+),\s*(\d+)\)", col_type)
                if precision_scale:
                    clickhouse_type = f"Decimal({precision_scale.group(1)}, {precision_scale.group(2)})"
            clickhouse_columns.append(f"{col_name} {clickhouse_type}")
        else:
            raise ValueError(f"Unsupported PostgreSQL data type: {base_type}")

    return clickhouse_columns

# Function to generate ClickHouse CREATE TABLE statement
def generate_clickhouse_create_table(table_name, clickhouse_columns):
    columns_str = ",\n    ".join(clickhouse_columns)
    return f"CREATE TABLE {table_name} (\n    {columns_str}\n) ENGINE = MergeTree() ORDER BY tuple()"

# Function to dynamically convert and execute
def convert_and_execute(psql_statement):
    # Parse PostgreSQL statement
    table_name, column_definitions, constraints = parse_postgres_create_table(psql_statement)

    # Convert column definitions
    clickhouse_columns = convert_column_definitions(column_definitions)

    # Generate ClickHouse CREATE TABLE statement
    clickhouse_statement = generate_clickhouse_create_table(table_name, clickhouse_columns)
    print("Generated ClickHouse CREATE TABLE Statement:")
    print(clickhouse_statement)

    # Execute in ClickHouse
    # client = Client(host='localhost')
    # client.execute(clickhouse_statement)
    # print(f"Table '{table_name}' created successfully in ClickHouse!")

# Example PostgreSQL CREATE TABLE statement
psql_create_table = """
CREATE TABLE example_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    price NUMERIC(10, 2),
    is_active BOOLEAN DEFAULT TRUE,
    metadata JSONB
);
"""

# Convert and execute
convert_and_execute(psql_create_table)