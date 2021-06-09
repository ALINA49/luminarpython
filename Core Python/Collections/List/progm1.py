lst=[]
ev=[]
odd=[]
for i in range(1,101):
    lst.append(i)

for i in lst:
    if i%2==0:
        ev.append(i)

    else:
        odd.append(i)

print(lst)
print(ev)
print(odd)