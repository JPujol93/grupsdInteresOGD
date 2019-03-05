from grupsDinteresExtractor import dbLoader
import os
import csv



db=dbLoader()


fileName="Registre_de_grups_d_inter_s_de_Catalunya.csv"
path= os.path.dirname(os.path.abspath(__file__))+"/"


with open(path+fileName, "r") as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)
    headings=rows.pop(0)
  
