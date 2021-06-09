sub1=int(input("enter mark1"))
sub2=int(input("enter mark2"))
sub3=int(input("enter mark3"))
sub4=int(input("enter mark4"))
tot=sub1+sub2+sub3+sub4
print("total mark=",tot)
if(180<=tot<=200):
    print("a+")
elif(160<=tot<=179):
    print("a")
elif(140<=tot<=159):
    print("b+")
elif(120<=tot<=139):
    print("b")
elif(100<=tot<=199):
    print("c+")
elif(80<=tot<=99):
    print("c")
elif(60<=tot<=79):
    print("d+")
else:

    print("fail")