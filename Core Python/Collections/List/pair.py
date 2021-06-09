def pair()
    r=ele-2
    return r

lst=[2,4,6,8,5,7,9]
lst.sort()
low=0
upp=len(lst)-1
ele=int(input("enter the value"))
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(ele>lst[mid]):
        low=mid+1
    elif(ele<lst[mid]):
        upp=mid-1
    elif(ele==lst[mid]):
        flag=1
        break
if (flag>0):
    re=pair(ele)
    print(re)
else:
    print("not found")

