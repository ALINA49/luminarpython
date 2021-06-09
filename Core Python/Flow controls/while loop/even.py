low_limit=int(input("enter the lower limit"))
upp_limit=int(input("enter the upper limit"))

while(low_limit<=upp_limit):
    if (low_limit % 2 == 0):
        print(low_limit)
    low_limit += 1