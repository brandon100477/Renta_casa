import mysql.connector

class registro():
    def __init__(self) -> None:
        self.conexion = mysql.connector.connect(user='root', password='', host = 'localhost',
                                        database='house', port='3306')
        def user(self, users):
            cur = self.conexion.cursor()
            sql = "SELECT * FROM usuario WHERE documento = {}".format(users)
            cur.execute(sql)
            usersx = cur.fetchall()
            cur.close()
            return usersx
        def password(self, password):
            cur = self.conexion.cursor()
            sql = "SELECT * FROM usuario WHERE password = {}".format(password)
            cur.execute(sql)
            passwordx = cur.fetchall()
            cur.close()
            return passwordx
    
