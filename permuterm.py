import os
import re

dir = r"C:\Users\VEDANK\Desktop\Files"
count = 0
files = []
allwords = []
for r, d, f in os.walk(dir):
    for file in f:
        files.append(os.path.join(r, file))
        count += 1
print(count)

index = dict()

for f in files:
    file = open(f, 'r')
    text = file.read().lower()
    words = text.split()
    for x in words:
        allwords.append(x)

allwords = list(dict.fromkeys(allwords))

for key in allwords:
    postList = []
    for f in files:
        file = open(f, 'r')
        text = file.read().lower()
       # found = re.search(' ' + key + ' ', ' ' + text + ' ')
        if(f' {key} ' in f' {text} '):
            postList.append(os.path.basename(f))
    index[key] = postList

for x, y in index.items():
  print(x, '  ', y)

with open(r'C:\Users\VEDANK\Desktop\Output\Index1.txt', 'w') as f:
    print(index, file=f)

permuterm = dict()


def rotate(lst, n):
    return lst[-n:] + lst[:-n]


for key in allwords:
    nkey = key + "$"
    for i in range(len(nkey), 0,-1):
        pkey = rotate(nkey, i)
        permuterm[pkey] = key
 
print("---------Permuterm-----------")
for x, y in permuterm.items():
  print(x, '  ', y) 

with open(r'C:\Users\VEDANK\Desktop\Output\PermuTerm.txt', 'w') as f:
    print(permuterm, file=f)

def rotatequery(lst, n):
    checkWord = lst[-n:] + lst[:-n]
    if checkWord.endswith('*'):
        return checkWord
    else:
        pass; 

docs = []

def matchPrefix(rotateWord,matchWord):
    permutermList = []
    for pk in permuterm:
        if pk.startswith(rotateWord):
            rex = re.compile("%s" %matchWord)
            match = permuterm[pk]
            if rex.findall(match):
                permutermList.append(permuterm[pk])
    return permutermList

def processQuery(rotateWord,matchWord):
    permutermList = matchPrefix(rotateWord,matchWord)
    print(permutermList)
    for term in permutermList:
        templist = index[term]
        for val in templist:
            docs.append(val)

query = input("Enter query: ") 
query = query.split()

for word in query:
    matchWord = word.replace("*", ".*")
    word = word.split('*')
    newWord = word[0] + '*' + word[len(word)-1]
    print(newWord) 
    newWord = newWord.split('*')
    rotateWord = newWord[1] + "$" + newWord[0]
    print(rotateWord + "*")
    processQuery(rotateWord,matchWord)

docs=list(dict.fromkeys(docs))
print("---------------")
print(docs)




