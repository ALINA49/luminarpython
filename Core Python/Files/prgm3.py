f=open("/Users/user/Downloads/customer","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    if data[4]=="Doctor":
        fname = data[1]
        lname = data[2]
        age = data[3]
        country = data[-1]
        print(fname,",",lname,",",age,",",country)