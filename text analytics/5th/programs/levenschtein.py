__author__ = 'user'
from nltk.metrics import edit_distance
from random import *
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#  transposition flag allows transpositions edits (e.g., “ab” -> “ba”),
slist=[]
slist.append( 'Former Rangers defender David Bates eyed by Arsenal and Everton as well as other Premier League clubs')
slist.append('We will always be grateful to them for their courage. Today, I had the honour of meeting Lalti Ram Ji, an INA veteran. It was wonderful spending time with him.')

slist.append( 'Their success will inspire many other youngsters to shine on the playing field. Wishing these young stars the very best for their future endeavours.')
slist.append('Its amazing what a simple thermal paste change can do to an 11 month old laptop that was pretty clean. Sorry for it being a photo and not a screenshot.')

slist.append('Mobile Phones is one of the dominant sub-sector in the electronics industry. It witnessed a jump of 60 % as manufacturing of mobile phones reached 175 Mn units during 2016-17')
t=['']*20
slist2=slist[0].split()

for i in range(20):
    j=math.floor(random()*10)
    for k in range(7):
        t[i]=t[i]+(slist2[j])+' '
    t[i]=t[i]+slist[0]
    #print("t[",i,"]=",t[i])

mat=[' ']*20
b=np.array([1],dtype=int)
for j in range(20):
    for i in range(5):
        mat[j] = mat[j]+' '+str( edit_distance(t[j], slist[i], transpositions=False))
    np.insert(b,j,mat[j])
for i in range(20):
    print()
    for j in range(5):
        print(int(mat[0].split()[j]),end='     ')
        plt.plot(j,int(mat[i].split()[j]),'r')
plt.show()

