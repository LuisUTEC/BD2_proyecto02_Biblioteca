from os import listdir
from os.path import isfile, join

from Database.Files import setFiles

files = [i for i in listdir("clean/") if isfile(join("clean/", i))]

if __name__ == '__main__':
    tweet_text = setFiles(files)