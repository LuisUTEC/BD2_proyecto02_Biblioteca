import operator
import nltk
from os import listdir
from os.path import isfile, join
from nltk import collections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
import json

# nltk.download('punkt')
# nltk.download('stopwords')

stemmer = SnowballStemmer('spanish')
f = open("stopwords.txt", "r", encoding="utf-8")
stoplist = f.read().splitlines()
stoplist += ['¡', '!', '¿', '?', '°', '.', ',', '\n', ';', ':', '»', '-', '«', '_', 'º', '``', "''", '@', '#', '...']

files = [i for i in listdir("clean/") if isfile(join("clean/", i))]

def setFiles(files):
    tweets = {}
    n = 0
    for file in files:
        print(file)
        with open("clean/"+file, errors='ignore') as file_json:
            file_clean = json.load(file_json)
        for tweet in file_clean:
            text = tweet['text']
            file_stemmed = []
            text = text.lower()
            files_tokens = []
            tokenizer = nltk.RegexpTokenizer(r"\w+")
            files_tokens = tokenizer.tokenize(text)
            for token in files_tokens:
                if token in stoplist:
                    files_tokens.remove(token)
            for token in files_tokens:
                file_stemmed.append(stemmer.stem(token))
            tweets[tweet['id']] = file_stemmed
        n+=1
        if n == 2:
            break
    for tweet in tweets:
        print(tweet)
        print(tweets[tweet])
    return tweets

