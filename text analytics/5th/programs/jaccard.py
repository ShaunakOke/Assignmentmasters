def JaccardIndex(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = 1-(float(len(set1 & set2)) / len(set1 | set2))
    return round(ans, 2)

target=[]
ans=[[]]
target.append("pills medicine amazon shop pasta")
target.append("medicine chips elephant panaroma")
target.append("medicine chips elephant demographic")
target.append("ice pizza eat amazon elephant shop")
target.append("pills medicine amazon trivia tango pasta")
target.append("ill panda camaro ships tango pasta")
target.append("ill panda camaro amazon tango pasta")

print("string 2->",end="")
for i in range (7):
    print("  ",i,end="      ")
print("\n")
for i in range (7):
    print(i,"       ", end="")
    for j in range(7):
        print (JaccardIndex(target[i], target[j]),"     ",end='')
    print("\n")



