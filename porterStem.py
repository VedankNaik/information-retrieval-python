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

index=dict()

def get_base(word, suf):
    suflen = word.rfind(suf)
    base = word[:suflen]
    return base

def replacer(word, suf1, suf2):
    base = get_base(word, suf1)
    base += suf2
    return base

def isvowel(l):
    letter = l.lower()
    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        return True
    else:
        return False

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

with open(r'C:\Users\VEDANK\Desktop\Output\index1.txt', 'w') as f:
    print(index, file=f)

newIndex=dict()


for word in allwords:    
    if word.endswith('sses'):
        new = replacer(word, 'sses', 'ss')  
        if new in newIndex:
            newList = newIndex[new]
            oldList = index[word]
            for i in oldList:
                newList.append(i)
            newList=list(dict.fromkeys(newList))
            newIndex[new] = newList
        else:            
            newIndex[new] = index[word] 
    elif word.endswith('ies'):
        new = replacer(word, 'ies', 'i')
        if new in newIndex:
            newList = newIndex[new]
            oldList = index[word]
            for i in oldList:
                newList.append(i)
            newList=list(dict.fromkeys(newList))
            newIndex[new] = newList
        else:            
            newIndex[new] = index[word] 
    elif word.endswith('ss'):
        new = word
        if new in newIndex:
            newList = newIndex[new]
            oldList = index[word]
            for i in oldList:
                newList.append(i)
            newList=list(dict.fromkeys(newList))
            newIndex[new] = newList
        else:            
            newIndex[new] = index[word]
    elif word.endswith('s'):
        new = replacer(word, 's', '')
        checkVowel = isvowel(new)
        if(checkVowel == False): 
            if new in newIndex:
                newList = newIndex[new]
                oldList = index[word]
                for i in oldList:
                    newList.append(i)
                newList=list(dict.fromkeys(newList))
                newIndex[new] = newList
            else:            
                newIndex[new] = index[word] 
        else:
            newIndex[word] = index[word]
    else:
        newIndex[word] = index[word]

print("===================After stemming===============")

for x, y in newIndex.items():
  print(x, '  ', y) 

with open(r'C:\Users\VEDANK\Desktop\Output\index2.txt', 'w') as f:
    print(newIndex, file=f)

query = input("Enter query: ") 
query = query.split()
newQuery=""
docs=[]

for word in query:
    if word.endswith('sses'):
        word = replacer(word, 'sses', 'ss')
        if word in newIndex.keys():
            docs = docs + newIndex[word]   
            print(word)       
    elif word.endswith('ies'):
        word = replacer(word, 'ies', 'i')
        if word in newIndex.keys():
            docs = docs + newIndex[word]   
            print(word)   
    elif word.endswith('ss'):
        new = word
        if word in newIndex.keys():
            docs = docs + newIndex[word] 
            print(word)     
    elif word.endswith('s'):
        word = replacer(word, 's', '')
        print(word) 
        checkVowel = isvowel(word)
        if(checkVowel == False): 
            if word in newIndex.keys():
                docs = docs + newIndex[word]  
                print(word) 
        else:
            word = word
    else:
        if word in newIndex:
            docs = docs + newIndex[word]  

docs=list(dict.fromkeys(docs))

print(docs)