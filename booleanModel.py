import os
import re

dir=r"C:\Users\VEDANK\Desktop\Files2"
count=0
files = []
allwords = []
for r, d, f in os.walk(dir):
    for file in f:
        files.append(os.path.join(r, file))
        count += 1
print(count)

table=dict()

for f in files:
    file = open(f, 'r')
    text = file.read().lower()
    words=text.split()
    for x in words:
        allwords.append(x)

allwords=list(dict.fromkeys(allwords))

for key in allwords:
    valueList=[]
    for f in files:
        file = open(f, 'r')
        text = file.read().lower()
       # found = re.search(' ' + key + ' ', ' ' + text + ' ')       
        if(f' {key} ' in f' {text} '):
            valueList.append(1)
        else:
            valueList.append(0)
    table[key] = valueList

print("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} ".format('Key','D1','D2','D3','D4','D5'))

for k, v in table.items():
    d1, d2, d3, d4, d5 = v
    print("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} ".format(k, d1, d2, d3, d4, d5))

print("============================================================")

i=0
result=[]
operators=[ '(', ')', 'OR', 'AND', 'NOT']
ops=[]
values=[]
operator=None
precedence =	{
  "NOT": 3,
  "AND": 2,
  "OR": 1,
  "(": 0,
  ")": 0
}

query = input("Enter query: ") 
query = query.split()

for i in range(len(query)):
    print(i,query[i])

def performOp(v1,v2,op):
    print("function")


for i in range(len(query)):
    if (query[i] == '('): 
        ops.append(query[i])
    elif (query[i] in allwords):
        values.append(query[i])
    elif (query[i] == ')'):
        while len(ops) != 0 and ops[-1] != '(':
            val2 = values.pop()
            if (len(values) !=0):
                val1 = values.pop()
                if type(val1) == str:
                    vector1 = table[val1]
                else:
                    vector1 = val1 
            operator = ops.pop()
            if type(val2) == str:
                vector2 = table[val2]
            else:
                vector2 = val2
            print("v1")
            print(vector1)
            print("v2")
            print(vector2)

            if(operator == 'OR'):
                currentVector = [vector1 or vector2 for vector1, vector2 in zip(vector1, vector2)]
                values.append(currentVector)
                print(currentVector)
            if(operator == 'AND'):
                currentVector = [vector1 and vector2 for vector1, vector2 in zip(vector1, vector2)]
                values.append(currentVector)
                print(currentVector)
            if(operator == 'NOT'):
                n=[]
                for j in vector2:
                    if j == 1:
                        n.append(0)
                    else:
                        n.append(1)
                values.append(n)
        
        ops.pop()
    # operator
    else:
        while (len(ops) != 0 and precedence[ops[-1]] >= precedence[query[i]]):
            val2 = values.pop()
            if (len(values) !=0):
                val1 = values.pop()
                if type(val1) == str:
                    vector1 = table[val1]
                else:
                    vector1 = val1 
            operator = ops.pop()
            if type(val2) == str:
                vector2 = table[val2]
            else:
                vector2 = val2 
            print("v1")
           # print(vector1)
            print("v2")
            print(vector2)

            if(operator == 'OR'):
                currentVector = [vector1 or vector2 for vector1, vector2 in zip(vector1, vector2)]
                values.append(currentVector)
                print(currentVector)
            if(operator == 'AND'):
                currentVector = [vector1 and vector2 for vector1, vector2 in zip(vector1, vector2)]
                values.append(currentVector)
                print(currentVector)
            if(operator == 'NOT'):
                n=[]
                for j in vector2:
                    if j == 1:
                        n.append(0)
                    else:
                        n.append(1)
                values.append(n)
        
        ops.append(query[i])

    i += 1

while (len(ops) != 0):
    val2 = values.pop()
    if (len(values) !=0):
        val1 = values.pop()
        if type(val1) == str:
            vector1 = table[val1]
        else:
            vector1 = val1 
    operator = ops.pop()
    if type(val2) == str:
        vector2 = table[val2]
    else:
        vector2 = val2
    print("v1")
    print(vector1)
    print("v2")
    print(vector2)

    if(operator == 'OR'):
        currentVector = [vector1 or vector2 for vector1, vector2 in zip(vector1, vector2)]
        values.append(currentVector)
        print(currentVector)
    if(operator == 'AND'):
        currentVector = [vector1 and vector2 for vector1, vector2 in zip(vector1, vector2)]
        values.append(currentVector)
        print(currentVector)
    if(operator == 'NOT'):
        n=[]
        for j in vector2:
            if j == 1:
                n.append(0)
            else:
                n.append(1)
        values.append(n)

print("Result")
print(values) 