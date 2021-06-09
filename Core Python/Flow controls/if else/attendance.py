tot_cls=int(input("enter total classes held"))
att_cls=int(input("enter attended classes"))
percentage=(att_cls/tot_cls)*100

if(percentage>=75):
    print(percentage,"student is allowed to sit in class")
else:
    print(percentage,"student is not allowed sit in exam")