# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 22:26:05 2018

@author: Admin
"""
import matplotlib.pyplot as plt
import math
list1=[]
list1.append([1,20,80,2,98])
list1.append([5,50,50,5,95])
list1.append([10,60,40,10,90])
list1.append([15
,80
,20
,20
,80])
list1.append(
[20,
88,
12,
30,
70])
list1.append(
[25,
90,
10,
40,
60])
list1.append(
[30,
95,
5,
50,
50])
list1.append(
[35,
96,
4,
60,
40])
list1.append(
[40,
97,
3,
70,
30])
list1.append(
[50,
98,
2,
80,
20])
temp=0
Xaxis=[]
Xaxis2=[]
Yaxis=[]
Yaxis2=[]
#print(list[0][1])
print(list1[4][3]/(list1[4][3]+list1[4][4]))
print(list1[4][2]/(list1[4][1]+list1[4][2]))
for var in list1:
    print (var)
    print("For threshold",var[0],"precision=",round(var[1]/(var[1]+var[3]),4)," Recall=",round((var[1]/(var[1]+var[2])),4))
    pr=var[1]/(var[1]+var[3])
    re=var[1]/(var[1]+var[2])
    Xaxis.append(var[3]/(var[3]+var[4]))
 
    misr=((var[3]/(var[3]+var[4])))
   
    fpr=(var[2]/(var[1]+var[2]))
    if (misr<0.5 and misr>0.1 and fpr>0.05 and fpr <0.40):
        Xaxis2.append(((var[3]/(var[3]+var[4]))))
        Yaxis2.append((var[2]/(var[1]+var[2])))
    Yaxis.append(re)
    
    f1=2*pr*re/(pr+re)
 
    if(f1>temp):
        temp=f1
        bestthreshold=var[0]
print(Xaxis2)
print(Yaxis2)
     
plt.figure(1)        
plt.plot(Xaxis,Yaxis)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")        


plt.figure(2)
plt.xlabel("False Positive Rate")
plt.ylabel("Missed Detection Rate") 
plt.yscale('log')
plt.xscale('log')

#plt.xticks([0,1/2,1/4,1/8,1/16,1/32],['0','1/2','1/4','1/8','1/16','1/32'])#(np.arange(0, 1, step=0.03))/
#plt.yticks([0,1/2,1/4,1/8,1/16,1/32],['0','1/2','1/4','1/8','1/16','1/32'])

plt.plot(Xaxis2,Yaxis2)

print ("best f1 measure value is  =",temp," threshold for this f1 is=",bestthreshold)
    