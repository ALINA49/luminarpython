class Employee:
    def __init__(self, name,id,salary):  #intialization
        self.name=name
        self.id=id
        self.salary=salary
    def printval(self):
        print(self.name,self.id,self.salary)
emp=Employee("inayath",25789,66789)
emp.printval()