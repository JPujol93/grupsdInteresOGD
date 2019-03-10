from grupsDinteresExtractor import dbLoader
import os
import csv
from  utils import node, edge




db=dbLoader()


fileName="Registre_de_grups_d_inter_s_de_Catalunya.csv"
path= os.path.dirname(os.path.abspath(__file__))+"/"





with open(path+fileName, "r") as file:

    # First look at the .csv to extract person ma erelatet to interest groups

    source="IN"

    csv_reader = csv.reader(file)
    rows = list(csv_reader)
    headings=rows.pop(0)
    print(headings)

    for row in rows:

        # Adding of the persons listed as representants in the database
        type1 = "person"
        newNode1 = node([row[28]+ " " + row[29]+" "+row[30], type1, None ,source ])
        #db.addNode(newNode1)

        # Adding the private entities
        type2 = "priventity"
        newNode2=node([row[0], type2, row[10]+ "\n "+row[12], source])
        #db.addNode2(newNode2)

        # Adding the adges of the relation between the relpresentatives and ther represented entities
        #print("Initiate ADGES")
        re1=[newNode1.name, newNode2.name]
        #db.addEdge(re1)

        # Extraction of social reason
        type ="unknown"

        newNode4=node([row[27],type, None, source ])
        db.addNodeUnk(newNode4);

        # Adding edge betwen social reason and enterprise

        rel2=[newNode4.name, row[0]]
        db.addEdgeSoc(rel2)


