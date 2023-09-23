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

# New transaction entries
transactions = [
    {'date': '2023-09-23', 'description': 'Groceries', 'value': 50.00, 'main_category': 'Expenses', 'subcategory': 'Food'},
    {'date': '2023-09-24', 'description': 'Gasoline', 'value': 40.00, 'main_category': 'Expenses', 'subcategory': 'Transport'},
    {'date': '2023-09-25', 'description': 'Earnings', 'value': 1000.00, 'main_category': 'Income', 'subcategory': 'Salary'}
]

# SQL query to insert a new transaction
insert_transactions_query = '''
INSERT INTO transactions (date, description, value, main_category, subcategory)
VALUES (%(date)s, %(description)s, %(value)s, %(main_category)s, %(subcategory)s)
'''

try:
    # Execute the SQL query to insert transactions
    cursor.execute(insert_transactions_query)
    print("Transactions inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and the connection
    cursor.close()
    connection.close()