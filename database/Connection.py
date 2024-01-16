import mysql.connector

conect = mysql.connector.connect(user='root', password='', host = 'localhost',
                                database='house', port='3306')

print(conect)
