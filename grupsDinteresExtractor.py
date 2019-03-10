

import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error


class dbLoader:


    def __init__(self):

        try:

            self.connector = mysql.connector.connect(host='localhost',user='root', password='olaola.',database='dacdb')
            self.cursor = self.connector.cursor(buffered=True)

        except errorcode as err:

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:

                print("Hi ha hagut algun problema amb laccés a la base de dades")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:

                print("Base de dades errònia")

            else:

                print(err)



    def addNode(self, node):


        queryExists = ("SELECT name, type  FROM nodes WHERE name=%s AND type =%s")
        self.cursor.execute(queryExists, (node.name, node.type))

        if len(self.cursor._rows) != 1:

            queryAddNode = ("insert into nodes (name, type, extra, source) values(%s, %s, null, %s)")
            self.cursor.execute(queryAddNode, (node.name, node.type, node.extra, node.source))
            self.connector.commit()

        else:

            print("This node already exists")


    def addNode2(self, node):

        queryExists = ("SELECT name, type  FROM nodes WHERE name=%s AND type =%s")
        self.cursor.execute(queryExists, (node.name, node.type))

        if len(self.cursor._rows) != 1:
            queryAddNode = ("insert into nodes (name, type, extra, source) values(%s, %s, %s, %s)")
            try:

                self.cursor.execute(queryAddNode, (node.name, node.type, node.extra, node.source))
                self.connector.commit()

            except Error as err:

                print(err)
        else:

            print("This node already exists")

