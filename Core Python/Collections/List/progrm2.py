lst=[10,20,21,22,25,26,27,28]
newlst=[]
j=1
for i in lst:
    if j<=len(lst):
        val=i**j
        newlst.append(val)
        j+=1
print(newlst)