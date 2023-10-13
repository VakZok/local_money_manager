import mysql.connector
import credentials
import transactions

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

# SQL query to insert a new transaction
insert_transactions_query = '''
INSERT INTO transactions (date, description, value, type, main_category, subcategory)
VALUES (%(date)s, %(description)s, %(value)s, %(type)s, %(main_category)s, %(subcategory)s)
ON DUPLICATE KEY UPDATE value = %(value)s;
'''

try:
    # Execute the SQL query to insert transactions
    for transaction in transactions.transactions:
        cursor.execute(insert_transactions_query, transaction)
    print("Transactions inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and the connection
    cursor.close()
    connection.commit()
    connection.close()