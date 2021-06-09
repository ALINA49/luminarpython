def print_employee(**kwargs):
    for k,v in kwargs.item():
        print(k,"=>",v)
print_employee(id=100,nat_place="thrissur",wrk_place="kakkanad",salaray=15000)