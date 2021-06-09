class Student:
    school="KENDRIYA VIDYALAYA"
    def setval(self,id,name,age,gender):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender

    def printval(self):
        print(self.id,self.name,self.age,self.gender,Student.school)

stud1=Student()
stud1.setval(125677,"kiyara",5,"female")
stud1.printval()

stud2=Student()
stud2.setval(126777,"iyan",7,"male")
stud2.printval()