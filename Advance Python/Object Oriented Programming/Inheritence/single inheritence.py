#single inheritence
#.....................
class Person:
    def detail(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name,self.age,self.gender)

class Student(Person):
    def det(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def prints(self):
        print(self.rollno,self.school)

p=Person()
p.detail("Ela",23,"f")
p.printdet()
st=Student()
st.det(7,"STSS")
st.prints()
st.detail("Elachi",24,"f")
st.printdet()