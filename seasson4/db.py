import mysql.connector


conn_db = mysql.connector.connect(user='root', password='r00t2023*!',
                                  host='127.0.0.1', port=3306,
                                  database='users')

conn_db.close()
# print(type(conn_db))
