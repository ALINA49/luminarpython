f=open("/Users/user/Downloads/customer","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    if data[3]>"50":
        fname = data[1]
        lname = data[2]
        age = data[3]
        prof = data[4]
        country = data[-1]
        print(fname,",",lname,",",age,",",prof,",",country)