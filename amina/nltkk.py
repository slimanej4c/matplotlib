





import xlrd
import django
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize ,word_tokenize

header_list = ["id", "sentiment", "statement"]
data=pd.read_csv('train.csv',encoding = "ISO-8859-1",sep=',',names=header_list)
data=data['statement'][0:10]


stop_words=set(stopwords.words("english"))

ps=PorterStemmer()
for i in data:
    print("i",i)
    print("sent tokensize",sent_tokenize(i))
    print("word toknize",word_tokenize(i))
    a=word_tokenize(i)
    l=[]
    for y in a :

        l.append(ps.stem(y))
    print("stemmer",l)

    print("#################################""")