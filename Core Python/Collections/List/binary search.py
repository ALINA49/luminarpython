lst=[2,4,6,1,3,56,78,32,45,90,76,33,12,13,56,89,9,5]
lst.sort()
print(lst)
low=0
upp=len(lst)-1

flag=0
ele=int(input("enter the value to be searched"))
while(low<=upp):
    mid=(low+upp)//2
    if (ele>lst[mid]):
        low=mid+1
    elif(ele<lst[mid]):
         upp=mid-1
    elif(ele==lst[mid]):
        flag=1
        break

if(flag>0):
    print("element found")
else:
    print("not found")
