import operator
import nltk
from os import listdir
from os.path import isfile, join
import params
from nltk import collections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import pandas as pd
import tweepy
import json
import tracker

# nltk.download('punkt')
# nltk.download('stopwords')

stemmer = SnowballStemmer('spanish')
f = open("stopwords.txt", "r", encoding="utf-8")
stoplist = f.read().splitlines()
stoplist += ['¡', '!', '¿', '?', '°', '.', ',', '\n', ';', ':', '»', '-', '«', '_', 'º','``',"''"]

files = [i for i in listdir("clean/") if isfile(join("clean/",i))]
def setFiles(files):
    files_stemmed = []
    for file in files:
        file_clean = json.dumps(file._json,indent=2)
        files_tokens = []
        file_stemmed = []
        text = file_clean["full_text"]
        files_tokens.append(nltk.word_tokenize(text.read().lower()))
        for token in text:
            if token in stoplist:
                text.remove(token)
        for token in files_tokens:
            file_stemmed.append(stemmer.stem(token))



tweet_text = []
'''
libros_dict = {i:libros_stemmed.count(i) for i in libros_stemmed}
sorted_x = sorted(libros_dict.items(), key=operator.itemgetter(1))
sorted_x.reverse()
libros_dict = collections.OrderedDict(sorted_x)

f = open("index.txt","a")
i = 0
for j,k in libros_dict.items():
    libros = ""
    if (i < 500):
        d = 0
        for s in stemmed_books:
            if j in s:
                libros = libros + str(stemmed_books.index(s)+1) + ", "
        libros = libros[:-2]
        f.write(j + ": " + libros + "\n")
        i+=1
f.close()'''
    print(tweet._json["full_text"])



