f=open("new", "r")
dic={}
for word in f:
    data=word.rstrip("\n").split(" ")
    print(data)
for char in data:
    if char not in dic:
        dic[char]=1
    else:
        dic[char]+=1
print(dic)
for k,v in dic.items():
    print(k,"",v)


