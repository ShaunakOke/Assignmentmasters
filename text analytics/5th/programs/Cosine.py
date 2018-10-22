__author__ = 'user'
# bits from http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python
# load_docs, process_docs and compute_vector by MK
import math
from collections import Counter

vector_dict = {}

#Just loads in all the documents
def load_docs():
    print("Loading docs...")
    doc1=('d1', 'UCD is a good university to study computer science')
    doc2=('d2', 'UCD university can study computer ')
    doc3=('d3', ' decent university  to study campus science')
    doc4=('d4', 'UCD is a ok university for studying computer ')
    doc5=('d5', 'UCD is a cool university to study computer subjects')
    return [doc1,doc2,doc3,doc4,doc5]


#Computes TF for words in each doc, DF for all features in all docs; finally whole Tf-IDF matrix
def process_docs(all_dcs):
 stop_words = [ 'of', 'and', 'on','in' ,'is','be','at','&']
 all_words = []
 counts_dict = {}
 for doc in all_dcs:
    words = [x.lower() for x in doc[1].split() if x not in stop_words]
    words_counted = Counter(words)
    unique_words = list(words_counted.keys())
    counts_dict[doc[0]] = words_counted
    all_words = all_words + unique_words
 n = len(counts_dict)
 df_counts = Counter(all_words)
 compute_vector_len(counts_dict, n, df_counts)


#computes TF-IDF for all words in all docs
def compute_vector_len(doc_dict, no, df_counts):
  global vector_dict
  for doc_name in doc_dict:
    doc_words = doc_dict[doc_name].keys()
    wd_tfidf_scores = {}
    for wd in list(set(doc_words)):
        wds_cts = doc_dict[doc_name]
        wd_tf_idf = wds_cts[wd] * math.log(no / df_counts[wd], 10)
        wd_tfidf_scores[wd] = round(wd_tf_idf, 4)
    vector_dict[doc_name] = wd_tfidf_scores

def get_cosine(text1, text2):
     vec1 = vector_dict[text1]
     vec2 = vector_dict[text2]
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     if not denominator:
        return 0.0
     else:
        return round(float(numerator) / denominator, 3)

#RUN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
all_docs = load_docs()
process_docs(all_docs)
print()
list2=[]
coslist=[]
vector_dict['q1'] = {'UCD' : 1, 'good' : 1, 'university' : 1, 'study' : 1, 'computer' : 1, 'science' : 1}
vector_dict['q2'] ={'I':1,'UCD':1,'like':1,'campus':1}
vector_dict['q3']={'drink':1,'water':1,'healthy':1,'lifestyle':1}
vector_dict['q4'] = {'UCD' : 1,'university' : 1, 'important' : 1, 'nation' : 1, 'economy' : 1}
for keys,values in vector_dict.items(): print(keys, values)
for i in range(1,4):
    list2=[]
    for j in range(1,6):
       list2.append(get_cosine("d"+str(j),"q"+str(i)))
    coslist.append(list2)

df=pd.DataFrame(np.array(coslist),columns=['d1','d2','d3','d4','d5'],index=['q1','q2','q3'])
print(df)
plt.plot(['d1','d2','d3','d4','d5'],coslist[0],'r')
plt.plot(['d1','d2','d3','d4','d5'],coslist[1],'b')
plt.plot(['d1','d2','d3','d4','d5'],coslist[2],'g')
#print(plt.show())
print(get_cosine('q1','q4'))
print(get_cosine('q2','q4'))
print(get_cosine('q3','q4'))
