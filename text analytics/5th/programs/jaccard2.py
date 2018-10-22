def JaccardIndex(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = 1-(2*float(len(set1 & set2)) / (len(set1)+len(set2)))
    return round(ans, 3)

target=[]
ans=[[]]
target.append("pills medicine amazon shop pasta trivia")
target.append("medicine chips elephant panaroma tango pasta")
target.append("medicine chips elephant demographic tango pasta")
target.append("ice pizza eat amazon elephant shop")
target.append("pills medicine amazon trivia tango pasta")
target.append("ill panda camaro ships tango pasta")
target.append("ill panda camaro amazon tango pasta")
print("string 2->",end="")
import pandas as pd
mat={}
for i in range (7):
    for j in range(7):
        mat["string"+str(i)].append(JaccardIndex(target[i], target[j]))

df=pd.DataFrame(mat)
print (df)


'''for i in range (7):
    print("  ",i,end="      ")
print("\n")
for i in range (7):
    print(i,"       ", end="")
    for j in range(7):
        print (JaccardIndex(target[i], target[j]),"     ",end='')
    print("\n")


'''
