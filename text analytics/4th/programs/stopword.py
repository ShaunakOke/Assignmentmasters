# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:18:15 2018

@author: Admin
"""
import nltk
import math
from textblob import TextBlob as tb
from nltk.corpus import stopwords
file=open("D:/code stuff/text/4th/tweets.txt","r+")
words=file.read();
token=nltk.word_tokenize(words)
words2=[w.lower() for w in token]
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
doc=[]
doc.append(("Never underestimate what its like in someone elses head. In this job we see people at breaking point everyday and that affects us too. Please remember that you are loved and important. Pick up the phone, talk and put the kettle on...you are not alone.WorldMentalHealthDay"))
doc.append(("As it's #WorldMentalHealthDay I encourage everyone who is struggling to try and book an appointment with a GP - get on that road! I know it can be scary, intimidating, embarrassing and/or cause anxiety - I cancelled two appointments before finally plucking up the courage...") )

doc.append(("On #WorldMentalHealthDay, let us not forget the conscious cruelty the Tories have inflicted on mental health sufferers: £105 million less funding now than in 2012. 30% fewer beds for mental health patients  40% of mental health trusts have experienced cuts"))

doc.append(("Today is #WorldMentalHealthDay. Around 70% of autistic children and young people have mental health problems - and many autistic adults do too. It’s vital that they can get the support they need, from professionals who understand autism"))

doc.append(("Its #WorldMentalHealthDay today. Remember that even the happiest, smiliest and most confident people you know have days where they lose faith in themselves and don't feel comfortable in their own skin. Everyone is fighting their own battle, lets help each other out" ))

doc.append(("Please dont be afraid to speak to someone if your struggling no matter what the reason is. You're family & friends will want you in their lives not just a memory of you. Its Ok not to be Ok. Stay strong & ask for help its a sign of great strength to do so. #WorldMentalHealthDay"))

doc.append(("In Peacehaven the Joff Youth Centre are working towards Takeover Day in November — a national initiative which will give young people a voice on issues and policies around mental health and emotional wellbeing #WorldMentalHealthDay"))
doc.append(("It’s #WorldMentalHealthDay and 1 in 4 people suffer from mental health problems. Were proud to say we help hundreds of learners combat their personal barriers by motivating them to improve their skills and get back into work with our free training courses. DM us for more info!"))

doc.append(("You cannot recover from anxiety by staying calm. You can not recover from depression by just being positive. You cannot recover from anorexia nervosa by eating more. If mental illness were that simple we wouldn’t be struggling in the first place. #WorldMentalHealthDay"))

doc.append(("Struggling with mental health was always a journey I kept to myself until recently, but opening up and seeking help got me to the good place Im in today. Its hard to talk about it but its even harder to go through it by yourself, lets break the stigma  #WorldMentalHealthDay."))


for i in range(0,10):
    doc[i]=[word for word in doc[i].split() if word not in stopwords.words('english')]
    strtemp=tb(" ".join(doc[i])).lower()
    doc[i]=strtemp
  
'''wordfreq = []
for w in filtered_words:
    wordfreq.append(filtered_words.count(w))
print(len(filtered_words))
for word in words:
    strin=" ".join(filtered_words)
strin=tb(words)
#print("Pairs\n" ,list(zip(filtered_words, wordfreq)))
'''
bloblist=[]
for i in range(0,10):
    bloblist.append(doc[i])
    
doctfidf=[]
docttf=[]
stri=""
for i, blob in enumerate(bloblist):
    #print(" Doc {}".format(i))
    tfs={word: tf(word, blob) for word in blob.words}
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    sorted_wordtf = sorted(tfs.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:10]:
       
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
    doctfidf.append(stri+"\n")
    print (doctfidf[i])
    stri=""
    #print (doctfidf[i])
    #for word,score in sorted_wordtf[:40]:
      #print("\tWord: {}, TF: {}".format(word, round(score, 5)))
      
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(token)
#for i in finder.score_ngrams(bigram_measures.pmi):
    #print (i)
file2=open("tweets2.txt",'r+')
file3=open("adverts.txt","r+")

f2=file2.read()
f3=file3.read()
print(entropy(f2))
print(entropy(f3))
abcd=f2+f3
print(entropy(abcd))
def entropy(labels):
    freqdist=nltk.FreqDist(labels)
    probs=[freqdist.freq(l) for l in freqdist]
    return -sum(p*math.log(p,2) for p in probs)