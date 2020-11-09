import os
import re
import math
from collections import defaultdict

dir = r"C:\Users\VEDANK\Desktop\coscoff"
docCount = 0
files = []
allwords = []
for r, d, f in os.walk(dir):
    for file in f:
        files.append(os.path.join(r, file))
        docCount += 1
print(docCount)

docs = list()
allwords = list()

for f in files:
    file = open(f, 'r')
    text = file.read().lower().split()
    for x in text:
        allwords.append(x)
    text.sort()
    docs.append(text)

allwords = list(dict.fromkeys(allwords))
allwords.sort()

query = "gold silver truck"
query = query.split()
docs.append(query)
docCount = docCount + 1
print("----Documents----")
print(docs)

#Frequency
termfreq = defaultdict(list)

for token in allwords:
    for sentence in docs:
        termfreq[token].append(sentence.count(token))

print("----Frequency----")
for x, y in termfreq.items():
    print(x, '  ', y) 

#Log Frquency
logfreq = defaultdict(list)
i=0
for token in termfreq:
    tlist = termfreq[token]
    logList = list()
    for i in tlist:
        if i > 0:
            logList.append(1 + round(math.log(i, 10), 2))
        else:
            logList.append(0)
    logfreq[token] = logList

print("----Log Frequency----")
for x, y in logfreq.items():
    print(x, '  ', y) 

#Normalisation
normalList = defaultdict(list)
i=0

while (i < docCount):
    normal = 0
    for token in logfreq:
        tlist = logfreq[token]
        normal = normal + pow(tlist[i],2)
    normal = round(normal ** 0.5, 2)
    for token in logfreq:
        tlist = logfreq[token]
        normalList[token].append(round(tlist[i]/normal,2) )
    i = i + 1

print("----Normalisation----")
for x, y in normalList.items():
    print(x, '  ', y)    

#Cosine
cosine = dict()
i = 0
while (i < docCount-1):
    angle = 0
    for token in normalList:
        tlist = normalList[token]
        angle = angle + round(tlist[i] * tlist[docCount-1], 2) 
    cosine["D"+str(i+1)+"Q"]=round(math.degrees(math.acos(angle)) , 2) 
    i = i + 1

print("-----Cosine--------")
sort_cosine = sorted(cosine.items(), key=lambda x: x[1], reverse=False)
print(sort_cosine)
