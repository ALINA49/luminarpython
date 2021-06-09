class Person:
    def detail(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name,self.age,self.gender)

class Employee(Person):
    def det(self,id,company):
        self.id=id
        self.company=company
    def prints(self):
        print(self.id,self.company)

p=Person()
p.detail("Krithika",23,"f")
p.printdet()
emp=Employee()
emp.det(7,"STSS.Ltd")
emp.prints()
emp.detail("Keerthan",24,"m")
emp.printdet()