import nltk
import re
file=open('D:/small.txt','r+')
words=file.read()
token=nltk.word_tokenize(words)
words=[w.lower() for w in token]
print (words)
print(nltk.pos_tag(words))
