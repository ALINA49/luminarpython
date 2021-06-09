b_date=int(input("enter the birth date"))
b_month=int(input("enter the birth month"))
b_year=int(input("enter the birth year"))
c_date=int(input("enter the current date"))
c_month=int(input("enter the current month"))
c_year=int(input("enter the current year"))

if(b_date==c_date)&(b_month==c_month):
    age=c_year-b_year
    print("he/she is",age,"years old.")
else:
    c_year-=1
    age=c_year-b_year
    print (age)