word=[2,5,4,7,8,9,0,5,7]
num=int(input("enter the value to be searched"))
if num not in word:
    print("not found")
else:
    print("found")

#linear search- increases the complexity of program
#.....................................................
#lst=[2,9,7,8,0,5,3]
element=int(input("enter the value to be searched"))
flag=0
for i in word:
    if i==element:
        flag=1
        break
    else:
        pass
if flag>0:
    print("element found")
else:
    print("not found")