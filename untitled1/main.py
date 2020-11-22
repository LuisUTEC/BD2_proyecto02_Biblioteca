import operator
import nltk
from nltk import collections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# nltk.download('punkt')
# nltk.download('stopwords')

f = open("stopwords.txt", "r", encoding="utf-8")
stemmer = SnowballStemmer('spanish')
stoplist = f.read().splitlines()
stoplist += ['¡', '!', '¿', '?', '°', '.', ',', '\n', ';', ':', '»', '-', '«', '_', 'º','``',"''"]

libro1 = open("docs/libro1.txt", "r", encoding="utf-8")
libro1_tokens = nltk.word_tokenize(libro1.read().lower())
libro2 = open("docs/libro2.txt", "r", encoding="utf-8")
libro2_tokens = nltk.word_tokenize(libro2.read().lower())
libro3 = open("docs/libro3.txt", "r", encoding="utf-8")
libro3_tokens = nltk.word_tokenize(libro3.read().lower())
libro4 = open("docs/libro4.txt", "r", encoding="utf-8")
libro4_tokens = nltk.word_tokenize(libro4.read().lower())
libro5 = open("docs/libro5.txt", "r", encoding="utf-8")
libro5_tokens = nltk.word_tokenize(libro5.read().lower())
libro6 = open("docs/libro6.txt", "r", encoding="utf-8")
libro6_tokens = nltk.word_tokenize(libro6.read().lower())

libro1_clean = libro1_tokens.copy()
libro1_stemmed = []
libro2_clean = libro2_tokens.copy()
libro2_stemmed = []
libro3_clean = libro3_tokens.copy()
libro3_stemmed = []
libro4_clean = libro4_tokens.copy()
libro4_stemmed = []
libro5_clean = libro5_tokens.copy()
libro5_stemmed = []
libro6_clean = libro6_tokens.copy()
libro6_stemmed = []


for token in libro1_tokens:
    if token in stoplist:
        libro1_clean.remove(token)

for token in libro2_tokens:
    if token in stoplist:
        libro2_clean.remove(token)

for token in libro3_tokens:
    if token in stoplist:
        libro3_clean.remove(token)

for token in libro4_tokens:
    if token in stoplist:
        libro4_clean.remove(token)

for token in libro5_tokens:
    if token in stoplist:
        libro5_clean.remove(token)

for token in libro6_tokens:
    if token in stoplist:
        libro6_clean.remove(token)



for token in libro1_clean:
    libro1_stemmed.append(stemmer.stem(token))

for token in libro2_clean:
    libro2_stemmed.append(stemmer.stem(token))

for token in libro3_clean:
    libro3_stemmed.append(stemmer.stem(token))

for token in libro4_clean:
    libro4_stemmed.append(stemmer.stem(token))

for token in libro5_clean:
    libro5_stemmed.append(stemmer.stem(token))

for token in libro6_clean:
    libro6_stemmed.append(stemmer.stem(token))

stemmed_books = [libro1_stemmed, libro2_stemmed, libro3_stemmed, libro4_stemmed, libro5_stemmed, libro6_stemmed]
'''print(libro1_stemmed)
print(libro2_stemmed)
print(libro3_stemmed)
print(libro4_stemmed)
print(libro5_stemmed)
print(libro6_stemmed)'''

libros_stemmed = libro1_stemmed + libro2_stemmed + libro3_stemmed + libro4_stemmed + libro5_stemmed + libro6_stemmed
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
f.close()
