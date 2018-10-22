# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:18:15 2018

@author: Admin
"""
import nltk
file=open("D:\code stuff\text\4r\tweets.txt","r+")
from nltk.corpus import stopwords
# ...
filtered_words = [word for word in word_list if word not in stopwords.words(file.read())]