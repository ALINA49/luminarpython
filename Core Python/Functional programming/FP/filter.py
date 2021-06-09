#filter=filter(fn,iterable)
lst=[1,2,3,4,5,6,7,8,9,10]
#def ev(num):
#   return num%2==0
#s=list(filter(ev,lst))
#print(s)

s=list(filter(lambda num:num%2==0,lst))
print(s)