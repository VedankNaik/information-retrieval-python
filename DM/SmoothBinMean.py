import csv 
from collections import defaultdict

filename = r"E:\py\IrisCleaned.csv"
  
fields = [] 
rows = [] 

# with open(filename, 'r') as csvfile: 
#     csvreader = csv.reader(csvfile) 
#     fields = next(csvreader) 
#     for row in csvreader: 
#         rows.append(row) 

#     print("Total no. of rows: %d"%(csvreader.line_num)) 
  

# ColumnNo = len(fields)
# RowNo = len(rows)

# print(ColumnNo)
# print(RowNo)
# print(rows)
# for row in rows:
#     print(row['Id'])

with open(filename, newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID")
 print("---------------------------------")
 for row in data:
   print(row)