class Person:
    def __init__(self, name,age,gender):  #intialization
        self.name=name
        self.age=age
        self.gender=gender
    def print(self):
        print(self.name,self.age,self.gender)
p=Person(u",23,"f")
p.print()