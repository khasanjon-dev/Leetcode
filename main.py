import re

def get_column_name_and_type(ddl):
    # Regular expression to match column name and type
    column_pattern = re.compile(r'(\w+)\s+([\w\(\)]+(?: PRIMARY KEY)?)')

    # Extract the part of DDL inside the parentheses
    columns_section = re.search(r'\((.*)\);', ddl, re.DOTALL).group(1)

    # Find all matches in the columns section
    columns = column_pattern.findall(columns_section)

    # Create a dictionary with column names as keys and types as values
    column_dict = {column[0]: column[1].split('(')[0] for column in columns}

    return column_dict

# Example DDL statement
ddl_statement = """
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    hire_date DATE,
    salary NUMERIC(10, 2)
);
"""

# Get column names and types as a dictionary
d = get_column_name_and_type(ddl_statement)

# Print the result
print(d)