import csv 
from collections import defaultdict

filename = r"C:\Users\VEDANK\Desktop\Dataset\Iris3.csv"
  
fields = [] 
rows = [] 

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
    fields = next(csvreader) 
    for row in csvreader: 
        rows.append(row) 

    print("Total no. of rows: %d"%(csvreader.line_num)) 
  

ColumnNo = len(fields)
RowNo = len(rows)

print(ColumnNo)
print(RowNo)

ColNo = 0
mean = []

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

ClassList = []

for row in rows:
    if row[ColumnNo-1] not in ClassList: 
        ClassList.append(row[ColumnNo-1])

print(ClassList)
count = 0
MeanDict = defaultdict(list)

while ColNo < ColumnNo - 1:
    for ClassType in ClassList:  
        sum = 0
        count = 0
        for row in rows:
            if((row[ColNo].isdigit() or isfloat(row[ColNo])) and row[ColumnNo-1] == ClassType):
                # print(row[ColNo])
                sum = sum + float(row[ColNo])
                count = count + 1
        MeanDict[ClassType].append(round(sum/count,1))
    ColNo = ColNo + 1
        
print(MeanDict)

ColNo = 0

while ColNo < ColumnNo - 1:
    for ClassType in ClassList: 
        for row in rows:
            if row[ColNo] == '' and row[ColumnNo-1] == ClassType:
                MeanList = MeanDict[ClassType]
                row[ColNo] = MeanList[ColNo]
    ColNo += 1

with open('IrisCleaned.csv', 'w',newline='') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)
