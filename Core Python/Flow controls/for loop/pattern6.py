n=int(input(":"))
for i in range(n+1,0,-1):
    for j in range(1,i):
        print(j,end="")
    for k in range(j-1,0,-1):
        print(k,end="")
    print()