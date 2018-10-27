from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
df=pd.read_csv("iris.csv")
x=df.iloc[:,1:4]
y=df.iloc[:,4]
accuracy=[]
mean=[]
neighbours=[19]
for k in neighbours:
    knn=KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(knn,x,y,cv=5,scoring='accuracy')
    accuracy.append(scores)
    mean.append(scores.mean())
print(accuracy)
print(mean)