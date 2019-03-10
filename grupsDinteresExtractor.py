

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


    def addNodeUnk(self, node):

        queryExists = ("SELECT name, type  FROM nodes WHERE name=%s OR name =%s")
        self.cursor.execute(queryExists, (node.name, "Hello"))

        if len(self.cursor._rows) != 1:

            queryAddNode = ("insert into nodes (name, type, extra, source) values(%s, %s, null, %s)")
            self.cursor.execute(queryAddNode, (node.name, node.type, node.source))
            self.connector.commit()

        else:

            print("This node already exists")




    def addNode(self, node):


        queryExists = ("SELECT name, type  FROM nodes WHERE name=%s AND type =%s")
        self.cursor.execute(queryExists, (node.name, node.type))

        if len(self.cursor._rows) != 1:

            queryAddNode = ("insert into nodes (name, type, extra, source) values(%s, %s, null, %s)")
            self.cursor.execute(queryAddNode, (node.name, node.type, node.source))
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



    def addEdge(self, edge):

        queryGetID=("select id from nodes where name=%s or name =%s")
        print(edge[0])
        self.cursor.execute(queryGetID, (edge[0], edge[1]))
        result =self.cursor.fetchall()
        try:
            for row in result:
                print(row)

            id1=result[0][0]
            print(id1)
            id2=result[1][0]
            print(id2)
            queryExists = ("SELECT origin, target, charge FROM edges WHERE origin=%s AND target =%s AND charge=%s")
            self.cursor.execute(queryExists, (id1, id2, "respresentant"))
            if len(self.cursor._rows) != 1 :
                queryAddEdge=("insert into edges (origin, target, charge, source) values(%s, %s, %s, %s)")
                self.cursor.execute(queryAddEdge, (id1, id2, "respresentant", "IN"))

            self.connector.commit()
        except Error as err:
            print("DB ERROR ")
        except IndexError as error:
            print("INDEX ERROR")

    def addEdgeSoc(self, edge):

        queryGetID=("select id from nodes where name=%s or name =%s")
        print(edge[0])
        self.cursor.execute(queryGetID, (edge[0], edge[1]))
        result =self.cursor.fetchall()
        try:
            if len(result)==1:
                id1=result[0][0]
                id2=id1
            else:

                for row in result:
                    print(row)

                id1=result[0][0]
                print(id1)
                id2=result[1][0]
                print(id2)
            queryExists = ("SELECT origin, target, charge FROM edges WHERE origin=%s AND target =%s AND charge=%s")
            self.cursor.execute(queryExists, (id1, id2, "respresentant"))
            if len(self.cursor._rows) != 1 :
                queryAddEdge=("insert into edges (origin, target, charge, source) values(%s, %s, %s, %s)")
                self.cursor.execute(queryAddEdge, (id1, id2, "respresentant", "IN"))

            self.connector.commit()
        except Error as err:
            print("DB ERROR ")
        except IndexError as error:
            print("INDEX ERROR")

    def isPerson(self, name ):

        queryExists = ("SELECT name, type  FROM nodes WHERE name=%s AND type =%s")
        self.cursor.execute(queryExists, (name, "person"))

        if len(self.cursor._rows) == 0:
            return False
        else :
            return True
