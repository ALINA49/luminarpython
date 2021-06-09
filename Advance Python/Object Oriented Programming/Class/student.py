class Student:
    def setval(self,id,name,age):
        self.name=name
        self.age=age
        self.id=id


    def printval(self,gender):
        self.gender=gender
        print(self.id,self.name,self.age,self.gender)

s=Student()
s.setval("liya",8)
s.printval("female")