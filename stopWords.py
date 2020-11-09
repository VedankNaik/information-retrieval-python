import os
import re

dir=r"C:\Users\VEDANK\Desktop\Files"
count=0
files = []
allwords = []
for r, d, f in os.walk(dir):
    for file in f:
        files.append(os.path.join(r, file))
        count += 1
print(count)

stopWords = ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
     "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to",
      "was", "were", "will", "with"]

index=dict()

for f in files:
    file = open(f, 'r')
    text = file.read().lower()
    words=text.split()
    for x in words:
        allwords.append(x)

allwords=list(dict.fromkeys(allwords))

for key in allwords:
    postList=[]
    for f in files:
        file = open(f, 'r')
        text = file.read().lower()
       # found = re.search(' ' + key + ' ', ' ' + text + ' ')       
        if(f' {key} ' in f' {text} '):
            postList.append(os.path.basename(f))
    index[key] = postList

for x, y in index.items():
  print(x, '  ', y) 

with open(r'C:\Users\VEDANK\Desktop\Output\invertedIndex.txt', 'w') as f:
    print(index, file=f)

length=len(index)

for k in stopWords:
    if k in index.keys():
        del index[k] 

print("------------After removal of stop words---------------------")

for x, y in index.items():
  print(x, '  ', y)  

with open(r'C:\Users\VEDANK\Desktop\Output\invertedIndex1.txt', 'w') as f:
    print(index, file=f)

query = input("Enter query: ") 
query = query.split()

docs=[]

for i in query:
    if i in index.keys():
        docs = docs + index[i]

docs=list(dict.fromkeys(docs))

print(docs)
