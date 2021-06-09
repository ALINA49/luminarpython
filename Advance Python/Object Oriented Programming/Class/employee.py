class Employee:
    cmpny="STGHU.Ltd"
    def setval(self,id,name,age,gender):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender

    def printval(self,salary,desig):
        self.salary=salary
        self.desig=desig
        print(self.id,"\n",self.name,"\n",self.age,"\n",self.gender,"\n",self.desig,"\n",Employee.cmpny,"\n\n")

emp1=Employee()
emp1.setval(125677,"kiyara",45,"female")
emp1.printval(97657,"assist_manager")

emp2=Employee()
emp2.setval(567787,"iyan",27,"male")
emp2.printval(34566,"clerk")