employee={1000:{"eid":1000,"name":"ajay","salary":25000,"design":"dev"},
    1001: {"eid": 1001, "name": "vijay", "salary": 22000, "design": "dev"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "design": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "design": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "design": "arkt"}}

def print_employee(**kwargs):  #kwargs={id:1003,prop:"salary"}
    eid=kwargs["id"] #1003
    prop=kwargs["prop"] #salary
    if eid in employee:
        print(employee[id]["name"])
        print(employee[id][prop])
    else:
        print("invalid")
print_employee(id=1003,prop="salary")