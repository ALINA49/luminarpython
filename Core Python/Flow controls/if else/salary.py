salary=int(input("Enter the salary"))   #10000    #678459
start_yr=int(input("Enter the year service started"))   #2015
current_yr=int(input("Enter the present year"))#2021
yr_of_exp=current_yr-start_yr  #2021-2015=6
if(yr_of_exp>5):        #6>5
    salary_Bonus=salary+(salary*(5/100))  #10000+(10000*(5/100))= 10500  #678459+(678459*(5/100))=712381.95
    print("salary along with bonus is",salary_Bonus) #true
else:
    print("not elligible for bonus as yr_of_exp is less than 5")