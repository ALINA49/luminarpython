employee=[{"eid":1000,"name":"ajay","salary":25000,"design":"dev"},
    {"eid": 1001, "name": "vijay", "salary": 22000, "design": "dev"},
    {"eid": 1002, "name": "arun", "salary": 26000, "design": "qa"},
 {"eid": 1003, "name": "varun", "salary": 27000, "design": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "design": "arkt"}]

#emp_name=list(map(lambda emp:emp["name"],employee))
#print(emp_name)
desig=list(filter(lambda emp:emp["design"]=="dev" and emp["salary"]>24000,employee))
print(desig)