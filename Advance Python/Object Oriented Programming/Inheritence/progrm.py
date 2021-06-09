#constructor in inheritence
#...........................
class Person:
    def __init__(self,name,age):
        self.name=name
        self.ae=age
    def printval(self):
        print("name",self.name,"\n","age",self.ae)

class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super(). __init__(name,age)
        self.rollno=rollno
        self.mark=mark

    def print(self):
        print(self.rollno,"\n",self.mark,"\n",self.name,self.ae)

cr=Student(2,34,"anu",55)
cr.printval()
cr.print()