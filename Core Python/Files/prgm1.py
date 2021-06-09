f=open("/Users/user/Downloads/customer","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
    fname=data[1]
    age=data[3]
    country=data[-1]
    print(fname,",",age,",",country)