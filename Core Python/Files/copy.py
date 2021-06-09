f=open("new", "r")
f1 = open("copyfile", "w")
for word in f:
    f1.write(word)
