def Remove(dup):
    list=[]
    for i in dup:
        if i not in list:
            list.append(i)
    return list
dup=[3,7,8,7,9,1,8,0,5,4,3,5,4,7]
print(Remove(dup))