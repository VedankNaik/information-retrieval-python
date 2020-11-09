import os
import re
import math
import operator
from collections import OrderedDict
from collections import defaultdict

dir = r"C:\Users\VEDANK\Desktop\scoeff"
docCount = 0
files = []
allwords = []
for r, d, f in os.walk(dir):
    for file in f:
        files.append(os.path.join(r, file))
        docCount += 1
print(docCount)

docs = list()

for f in files:
    file = open(f, 'r')
    text = file.read().lower().split()
    text.sort()
    docs.append(text)

print(docs)

wordfreq = dict()

for sentence in docs:
    for token in sentence:
        if token not in wordfreq.keys():
            wordfreq[token] = 1
        else:
            wordfreq[token] += 1

print(wordfreq)

word_idf_values = {}
for token in wordfreq:
    doc_containing_word = 0
    for document in docs:
        if token in document:
            doc_containing_word += 1
    word_idf_values[token] = round(
        math.log(docCount/doc_containing_word, 10), 2)

print("---IDF---")
print(word_idf_values)

word_tf_values = {}


def tdfidf(docs):
    for token in wordfreq:
        sent_tf_vector = []
        for document in docs:
            doc_freq = 0
            for word in document:
                if token == word:
                    doc_freq += 1
            word_tf = word_idf_values[token]*doc_freq
            sent_tf_vector.append(word_tf)
        word_tf_values[token] = sent_tf_vector


query_tf_values = {}


def querytdfidf(query):
    for token in wordfreq:
        sent_tf_vector = []
        doc_freq = 0
        for word in query:
            if token == word:
                doc_freq += 1
        word_tf = word_idf_values[token]*doc_freq
        sent_tf_vector.append(word_tf)
        query_tf_values[token] = sent_tf_vector


print("-----TF-IDF--------")
tdfidf(docs)

for x, y in word_tf_values.items():
    print(x, '  ', y)

query = "equity fund investment market"
#query = input("Enter query: ") 
query = query.split()

print(query)

querytdfidf(query)

print("-----QueryIDF--------")
for x, y in query_tf_values.items():
    print(x, '  ', y)

similarity=dict()
i = 0
while (i < docCount):
    tempVal = 0
    for word in word_tf_values:
        wordList = word_tf_values[word]
        queryList = query_tf_values[word]
        tempVal = tempVal + wordList[i] * queryList[0]
    similarity["D"+str(i+1)+"Q"]=tempVal
    i = i+1

print("-----Similarity--------")
sort_similarity = sorted(similarity.items(), key=lambda x: x[1], reverse=True)

print(sort_similarity)