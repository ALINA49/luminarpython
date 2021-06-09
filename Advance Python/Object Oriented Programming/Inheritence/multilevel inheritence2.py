#person child parent student
# child& parent inherit person
# student class inherit child
class Person:
    def parsement(self,age,name,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name,self.age,self.gender)

class Parent(Person):
    def parement(self,job,place,salary):
        self.job=job
        self.place=place
        self.salary=salary
        print(self.job,self.place,self.salary)
class Child(Person):
    def childment(self,school):
        self.school=school
        print(self.school)

class Student(Child):
    def studment(self,rollno):
        self.rollno=rollno
        print(self.rollno)

m1=Parent()
m1.parsement("reena",45,"f")
m1.parement("housewife","adoor",78977)
m2=Child()
m2.parsement("ansa",17,"f")
m2.childment("kv")
m3=Student()
m3.studment(7)

