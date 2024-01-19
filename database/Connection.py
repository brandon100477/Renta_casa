import mysql.connector

class registro():
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host = 'localhost',
                                        database='house', port='3306')
    
