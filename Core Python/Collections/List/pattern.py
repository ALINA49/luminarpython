lst=[5,9,6]
newlst=[]
ele=0
val=0
for i in lst:
    ele=ele+i
print(ele)
for i in lst:
    val=ele-i
    newlst.append(val)
print(newlst)