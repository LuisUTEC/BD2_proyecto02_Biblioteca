from os import listdir
from os.path import isfile, join

from Files import setFiles
from invertindex import tf_idf
from query import query

files = [i for i in listdir("clean/") if isfile(join("clean/", i))]

if __name__ == '__main__':
    #tweet_text = setFiles(files)
    #tf_idf(tweet_text)
    Result = query("Comer es sano")
    print(Result)