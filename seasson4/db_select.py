# Import library mysql.connector
import mysql.connector

# A database instance is created
conn_db = mysql.connector.connect(
    user='root', password='r00t2023*!', host='127.0.0.1', port=3306, database='users')

# Create a cursos object
cursor = conn_db.cursor()

# Query execute
cursor.execute('select * from users.Users')

# Get the query results
# result_query = cursor.fetchall()
result_query2 = cursor.fetchone()

# Print the result
# print(result_query)
print(result_query2)

# Close connection
conn_db.close()
