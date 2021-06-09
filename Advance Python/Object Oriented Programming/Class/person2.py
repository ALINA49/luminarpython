class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age

    def printval(self,gender):
        self.gender=gender
        print(self.name,self.age,self.gender)

p=Person()
p.setval("laiya",22)
p.printval("female")