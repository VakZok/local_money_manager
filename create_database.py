import mysql.connector
import credentials

# MySQL connection configuration
config = {
    'user': credentials.user,
    'password': credentials.password,
    'host': credentials.host,
    'database': credentials.database
}

# Establish a connection to the MySQL server
connection = mysql.connector.connect(**config)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# SQL query to create a table
create_table_query = '''
CREATE TABLE transactions (
    date DATE,
    description VARCHAR(100),
    value DOUBLE NOT NULL,
    main_category VARCHAR(100) NOT NULL,
    subcategory VARCHAR(100) NOT NULL,
    PRIMARY KEY (date, description)
)
'''

try:
    # Execute the SQL query to create the table
    cursor.execute(create_table_query)
    print("Table 'finances' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and the connection
    cursor.close()
    connection.close()