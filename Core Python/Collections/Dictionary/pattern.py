pattern="ABCDBC"

dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1

    else:

        print("1st recurssion char is", i)
        break
print(dic)