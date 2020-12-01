import csv 

filename = r"C:\Users\VEDANK\Desktop\Dataset\Records3.csv"
  
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

ColNo = 0
mean = []

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

while ColNo < ColumnNo:
    sum = 0
    for row in rows:
        if(row[ColNo].isdigit() or isfloat(row[ColNo])):
            print(row[ColNo])
            sum = sum + float(row[ColNo])
    mean.append(round(sum/RowNo,1))
    ColNo = ColNo + 1

print(mean)

ColNo = 0

while ColNo < ColumnNo:
    for row in rows:
        if row[ColNo] == '':
            row[ColNo] = mean[ColNo]
    ColNo += 1


with open('NewData2.csv', 'w',newline='') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)

