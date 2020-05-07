import nltk
import pandas as pd


data=pd.read_excel
from nltk.tokenize import sent_tokenize ,word_tokenize
#nltk.download()

exemple_text="hello Mr. Smith  ,how are you doing today ? The weather is great and python is awsome"

print(sent_tokenize(exemple_text))
print(word_tokenize(exemple_text))