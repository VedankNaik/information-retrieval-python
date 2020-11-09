import os
import re
from collections import defaultdict

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

soundex = defaultdict(list)
letters = 'abcdefghijklmnopqrstuvwxyz.'
codes   = '012301200224550126230102020'
codeDict = dict(zip(letters, codes))

def soundexCode(word):
    result = word[0]
    word = word[1:]
    word = re.sub(r'[0-9]+', '', word)
    prev_code=""
    for char in word:
        code = codeDict[char]
        if code != '0' and code != prev_code:
            result += code
        prev_code = code
    return (result + "0000")[:4]

for term in allwords:
    word = soundexCode(term)
    soundex[word].append(term)

for x, y in soundex.items():
  print(x, '  ', y)

with open(r'C:\Users\VEDANK\Desktop\Output\Soundex.txt', 'w') as f:
    print(index, file=f)

query = input("Enter query: ") 
query = query.split()

docs=[]

for term in query:
    word = soundexCode(term)
    print(word)
    if word in soundex:
        wordList = soundex[word]
    print(wordList)  
    for i in wordList:
        if i in index:
            tempList = index[i]
            for j in tempList:
                docs.append(j)

docs=list(dict.fromkeys(docs))
print("---------------")
print(docs)









'''
for term in allwords:
    replaceWord = term[0]
    for i in range(1,len(term)):
        if term[i] in ['a','e','i','o','u']:
            replaceWord = replaceWord + '0'
        if term[i] in ['b','f','p','v']:
            replaceWord = replaceWord + '1'
        if term[i] in ['c','g','j','k','q','s','x','z']:
            replaceWord = replaceWord + '2'
        if term[i] in ['d','t']:
            replaceWord = replaceWord + '3'
        if term[i] in ['l']:
            replaceWord = replaceWord + '4'
        if term[i] in ['m', 'n']:
            replaceWord = replaceWord + '5'
        if term[i] in ['r']:
            replaceWord = replaceWord + '6' 
    stripSpace=replaceWord[0]
    for i in range(1,len(replaceWord)):
        try:      
            if replaceWord[i]==replaceWord[i-1]:
                pass
            else:
                stripSpace = stripSpace + replaceWord[i]
        except:
            pass
    stripZeros=stripSpace[0]
    for i in range(1,len(stripSpace)):
        if stripSpace[i]!='0':
            stripZeros = stripZeros + stripSpace[i]
    print(stripZeros)
'''           