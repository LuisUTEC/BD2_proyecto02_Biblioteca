import nltk
from nltk import collections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def get_tf(query):
    return 1

def get_idf(query):
    return 1

def top(K, Scores):
    return Scores

def query(content):
    Scores = []
    Length = []
    for t in content.split():
        w_tq = get_tf(t)*get_idf(t)
        for d in data:
            w_td = get_tf(d)
            Scores[d] += w_td*w_tq
    for d in Scores:
        Scores[d] = Scores/Length[d]
    return top(5, Scores)


if __name__ == '__main__':
    consulta('PyCharm')

