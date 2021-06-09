
age=int(input("enter the age"))
sex=input("enter the gender (f/m)")
marital_status=input("enter the status (y/n)")
if(sex== 'f'):
    print("work only in urban")
elif(sex=='m')&(20<=age<=40):
    print("work anywhere")
elif(sex=='m')&(40<=age<=60):
    print("work only in urban")
else:
    print("error")