import math
import json

def tf (num):
    return round(math.log10(1+num), 2)

def idf (num, N):
    return round(math.log10(N/num), 2)

def tf_idf (self):
	data = {}
	docs_length = {}
	for term in self:
		for word in self[term]:
			data[word] = {}
			data[word][term] = {}
			if 'f' in data[word][term].keys():
				data[word][term]['f'] += 1
			else:
				data[word][term]['f'] = 1
		docs_length[term] = len(self[term])

	for word in data:
		docs = data[word]
		size = len(docs)
		for doc in docs:
			_tf_idf = round(tf(docs[doc]['f'])*idf(size, len(self)), 2)
			data[word][doc]['tf-idf'] = _tf_idf
	with open('index.json', 'w') as file:
		json.dump(data, file)
	with open('doc_length.json', 'w') as file:
		json.dump(docs_length, file)

