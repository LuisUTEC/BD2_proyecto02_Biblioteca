import nltk
import math 
from decimal import Decimal
from nltk import collections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def tf(num):
    return round(math.log10(1+num),2)

def idf(num,N):
    return round(math.log10(N/num),2)


def tf_idf(term,tokens,Ids):
	st=SnowballStemmer('spanish')
	for token in tokens:
		token=st.stem(token)
		if token not in terms:
			term[token]=startcount()
			term[token].df.add(Ids)
			if id in term[token].tfd:
				term[token].tfd[Ids]=term[token].tfd[Ids]+1
			else:
				term[token].tfd[Ids]=1
		else:
			term[token].df.add(Ids)
			if id in term[token].tfd:
				tmp.tfd[doc_id] = term[token].tfd[id] + 1
			else:
				tmp.tfd[doc_id] = 1

			terms[token] = term[token]

def invert_index_rc(self,query):
	KScores=dict()
	tokens=Tokensclean()	
	terms=tokens.edit_query(query)
	weights=dict(collections.Counter(terms).items())
	for query in weights:
		Ids=self.L(query)
		for doc in Ids:
			if doc[0] not in scores:
                    scores[doc[0]] = tf(doc[1])*tf(weights[terms])
                else:
                    scores[doc[0]] = scores[doc[0]] + tf(doc[1])*tf(weights[terms])
				
	KScores=sorted(KScores.items(),key=lambda kv: kv[1], reverse=True)
	return KScores
