n=int(input("enter the no."))
i=0
for i in range((i+1),n):
    for j in range (i,0,-1):
        print(j,end="")
    for k in range((j+1),(i+1)):
        print(k,end="")
    print()