num1=int(input("enter 1st no."))
num2=int(input("enter 2nd no."))
num3=int(input("enter 3rd no."))
if(num1>num2)&(num1>num3):
    print(num1,"is the greatest among 3.")
elif(num2>num3)&(num3>num1):
    print(num2,"is the greatest among 3 ")
else:
    print(num3,"is the greatest among 3.")