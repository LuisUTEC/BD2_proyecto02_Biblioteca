import operator
import nltk
from os import listdir
from os.path import isfile, join
from nltk import collections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import json

# nltk.download('punkt')
# nltk.download('stopwords')

stemmer = SnowballStemmer('spanish')
f = open("stopwords.txt", "r", encoding="utf-8")
stoplist = f.read().splitlines()
stoplist += ['¡', '!', '¿', '?', '°', '.', ',', '\n', ';', ':', '»', '-', '«', '_', 'º','``',"''"]

files = [i for i in listdir("clean/") if isfile(join("clean/",i))]

def setFiles(files):
    file_stemmed = []
    for file in files:
        file_clean = json.dumps(file._json,indent=2)
        files_tokens = []
        text = file_clean["full_text"]
        files_tokens.append(nltk.word_tokenize(text.read().lower()))
        for token in text:
            if token in stoplist:
                text.remove(token)
        for token in files_tokens:
            file_stemmed.append(stemmer.stem(token))
    dict = {i: file_stemmed.count(i) for i in file_stemmed}
    sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    dict = collections.OrderedDict(sorted_x)
    return dict

tweet_text = setFiles(files)

