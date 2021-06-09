class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
obj=Calc(2,5)
n=int(input("choose the operation"))
if n ==1:
    print(obj.add())
elif n == 2:
    print(obj.sub())
elif n == 3:
    print(obj.mul())
elif n == 4:
    print(obj.div())
else:
    print("error")