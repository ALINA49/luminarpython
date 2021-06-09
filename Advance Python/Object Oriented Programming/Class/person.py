class Person:
    def print(self,name,age,gender):
        self.name=name
        self.gender=gender
        self.age=age
        print("inside print",self.name,self.age,self.gender)

p=Person()
p=print("ahana",22,"female")
