import nltk
import math 
from decimal import Decimal
from nltk import collections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

class startcount:
	def __init__(self):
		self.df=set()
		self.tfd={}
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
def tf_idf(N, df, tfd):
  a = math.log((1+tfd), 10)
  b = math.log((N/df), 10)
  return round((a * b), 6)
def invert_index(self,query):
	KScores=dict()
	tokens=Tokensclean()
	terms=tokens.edit_query(query)
	weights=dict(collections.Counter(terms).items())
	for query in weights:
		Ids=self.L(query)
		for doc in Ids:
			if doc[0] not in KScores:
				KScores[doc[0]]=tf_idf(terms,tokens,Ids)*tf_idf(terms,tokens,Ids)
			else:
				KScores[doc[0]]=KScores[doc[0]]+tf_idf(terms,tokens,Ids)*tf_idf(terms,tokens,Ids)
				
	KScores=sorted(KScores.items(),key=lambda kv: kv[1], reverse=True)
	return KScores
