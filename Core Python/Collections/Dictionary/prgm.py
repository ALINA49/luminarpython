emp={"id":1001,"name":"ahana","designation":"assit manager","salary":10000}
print(emp["name"])
print("cmpny" in emp)
emp["cmpny"]='SRDC'
print(emp)
emp["salary"]=emp["salary"]+(emp["salary"]*(5/100))
print (emp)
i=1
for i in emp:
    print(i,":",emp[i])