#map=map(fn,iterable)
lst=[1,2,3,4,5,6,7,8,9,10]     #iterable
#def sq(num):                    #funtion
#    return num*num
#s=list(map(sq,lst))
#print(s)

s=list(map(lambda num:num*num,lst))
print(s)