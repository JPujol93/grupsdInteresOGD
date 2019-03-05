

import mysql.connector
from mysql.connector import errorcode

class dbLoader:
    def __init__(self):
    
        try:
            self.cnx = mysql.connector.connect(host='localhost',user='root', password='olaola.',database='dacdb')
            self.cur = self.cnx.cursor(buffered=True)

        except errorcode as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Hi ha hagut algun problema amb laccés a la base de dades")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de dades errònia")
            else:
                print(err)



