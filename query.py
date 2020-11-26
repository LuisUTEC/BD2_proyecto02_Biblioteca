import json
import nltk
from nltk import collections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from Files import stoplist, stemmer


def top(K, Scores):
    Result = {}
    Scores_items = Scores.items()
    Scores_sorted = sorted(Scores_items, key=lambda coche: coche[1])
    i = 0
    for doc in Scores_sorted:
        if i == K:
            break
        Result[doc[0]] = doc[1]
        i += 1
    return Scores

def parsing(content):
    files_tokens = nltk.word_tokenize(content)
    file_stemmed = []
    for token in files_tokens:
        if token in stoplist:
            files_tokens.remove(token)
    for token in files_tokens:
        file_stemmed.append(stemmer.stem(token))
    return file_stemmed

def query(content):
    Scores = {}
    Length = {}
    words = parsing(content)
    for t in words:
        with open('index.json') as file:
            data = json.load(file)
        for doc in data[t]:
            Scores.setdefault(doc, 0)
            Scores[doc] += data[t][doc]['tf-idf']
    with open('doc_length.json') as file:
        doc_length = json.load(file)
    for length in doc_length:
        Length[length] = doc_length[length]
    for d in Scores:
        Scores[d] = Scores[d]/Length[d]
    return top(5, Scores)
