# Import library mysql.connector
import mysql.connector

# A database instance is created
conn_db = mysql.connector.connect(
    user='root', password='r00t2023*!', host='127.0.0.1', port=3306, database='users')

# Create a cursos object
cursor = conn_db.cursor()

# # cursor.execute('show create table Users')

# # result = cursor.fetchall()
# # print(result)
# sql_insert = 'insert into Users (email, name, lastname, phone) values (%s, %s, %s, %s)'
# values = ('johanluna7777@gmail.com', 'Ederlien', 'Bermeo', 3105405342)

# # Recibe dos argumentos, consulta SQL + values
# cursor.execute(sql_insert, values)

cursor.execute('select * from Users')



# conn_db.commit()

result_query = cursor.fetchall()

# Print the result
# print(result_query)
print(result_query)

# Close connection
conn_db.close()
