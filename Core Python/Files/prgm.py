f=open("/Users/user/Downloads/customer","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    #print(lines)