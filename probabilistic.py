import os
import re
import math
from collections import defaultdict

dir = r"C:\Users\VEDANK\Desktop\coscoff2"
docCount = 0
files = []
allwords = []
for r, d, f in os.walk(dir):
    for file in f:
        files.append(os.path.join(r, file))
        docCount += 1
print(docCount)

doctable = dict()

for f in files:
    file = open(f, 'r')
    text = file.read().lower()
    doctable[os.path.basename(f)] = text

print(doctable)

table = dict()

query = "gold silver truck"
query = query.split()

R = 2
releventDocs = "d2.txt d3.txt"
#R = input("Enter number of relevent docs")
#releventDocs = input(f'Enter {R} relevent docs: ')

print(releventDocs)

for word in query:
    newList = list()
    newList.append(docCount)
    n=0
    r=0
    for doc in doctable:
        docList = doctable[doc]
        if(f' {word} ' in f' {docList} '):
            n = n + 1
            if(f' {doc} ' in f' {releventDocs} '):
                r = r + 1
    newList.append(n)
    newList.append(R)
    newList.append(r)
    table[word] = newList

print("\n------------")
print("{:<15} {:<8} {:<8} {:<8} {:<8}".format(' ','N','n','R','r'))

for k, v in table.items():
    d1, d2, d3, d4 = v
    print("{:<15} {:<8} {:<8} {:<8} {:<8} ".format(k, d1, d2, d3, d4))


#termWeights
termWeights = dict()

for term in table:
    v = table[term]
    weightList = []
    # v3=r v2=R v1=n v0=N
    w1 = round(math.log(((v[3]+0.5)/(v[2]+1)/((v[1]+1)/(v[0]+2))), 10), 3)
    weightList.append(w1)
    w2 = round(math.log(((v[3]+0.5)/(v[2]+1)/((v[1]-v[3]+0.5)/(v[0]-v[2]+1))), 10), 3)
    weightList.append(w2)
    w3 = round(math.log(((v[3]+0.5)/(v[2]-v[3]+0.5)/((v[1]+1)/(v[0]-v[1]+1))), 10), 3)
    weightList.append(w3)
    w4 = round(math.log(((v[3]+0.5)/(v[2]-v[3]+0.5)/((v[1]-v[3]+0.5)/(v[0]-v[1]-(v[2]-v[3])+0.5))), 10), 3)
    weightList.append(w4)
    
    termWeights[term] = weightList

print("\n------Term Weights------")
print("{:<15} {:<8} {:<8} {:<8} {:<8}".format(' ','W1','W2','W3','W4'))

for k, v in termWeights.items():
    d1, d2, d3, d4 = v
    print("{:<15} {:<8} {:<8} {:<8} {:<8} ".format(k, d1, d2, d3, d4))


#documentWeights
docWeights = dict()

for doc in doctable:
    sentence = doctable[doc]
    for term in query:
        if(f' {term} ' in f' {sentence} '):
            if doc in docWeights:
                tlist = docWeights[doc]
                addVal = termWeights[term]
                i=0
                for i in range(len(tlist)):
                    newList[i] =  round(tlist[i] + addVal[i], 3) 
                docWeights[doc] = newList
            else:
                docWeights[doc] = termWeights[term]

sort_docWeights = sorted(docWeights.items(), key=lambda x: x[1], reverse=True)
print("\n------Document Weights------")
for i in sort_docWeights:
    print(i)



    

