import re


def postgres_to_clickhouse_type(postgres_type):
    type_mapping = {
        "SERIAL": "UInt32",
        "VARCHAR": "String",
        "CHAR": "String",
        "TEXT": "String",
        "INT": "Int32",
        "INTEGER": "Int32",
        "SMALLINT": "Int16",
        "BIGINT": "Int64",
        "NUMERIC": "Float64",  # Default mapping
        "DECIMAL": "Float64",   # Default mapping
        "REAL": "Float32",
        "DOUBLE PRECISION": "Float64",
        "DATE": "Date",
        "TIMESTAMP": "DateTime",
        "TIMESTAMPTZ": "DateTime",
        "BOOLEAN": "UInt8",
        "BOOL": "UInt8",
        "JSON": "String",
        "JSONB": "String",
        "UUID": "UUID",
    }

    # Check for type precision (e.g., VARCHAR(50), NUMERIC(10, 2))
    if '(' in postgres_type:
        base_type = postgres_type.split('(')[0].strip()
        if base_type in ["VARCHAR", "CHAR", "TEXT"]:
            return "String"  # ClickHouse always maps string types to String
        elif base_type in ["NUMERIC", "DECIMAL"]:
            return "Float64"  # ClickHouse defaults to Float64 for numeric types with precision
        else:
            # Return the base type if it's numeric with precision or something unsupported
            return type_mapping.get(base_type, "String")
    else:
        # No precision/size; simply return the mapped type
        return type_mapping.get(postgres_type, "String")


ddl_statement = """
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    hire_date DATE,
    salary NUMERIC(10, 2),
    status BOOLEAN,
    department_id INT,
    join_date TIMESTAMP,
    updated_at TIMESTAMPTZ,
    profile JSONB,
    unique_code UUID,
    age SMALLINT,
    bonus DOUBLE PRECISION
);
"""

def get_column_name_and_type(ddl):
    # Regex to capture column name and type
    column_pattern = re.compile(r"(\w+)\s+([\w\(\)\s]+(?: PRIMARY KEY)?)")
    columns_section = re.search(r"\((.*)\);", ddl, re.DOTALL).group(1)
    columns = column_pattern.findall(columns_section)
    return {column[0]: column[1] for column in columns}


columns = get_column_name_and_type(ddl_statement)

# Convert the column types to ClickHouse types
clickhouse_columns = {
    col: postgres_to_clickhouse_type(col_type) for col, col_type in columns.items()
}

print(clickhouse_columns)
