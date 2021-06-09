class Parent:
    def m1(self,pname,addr,job):
        self.pname=pname
        self.addr=addr
        self.job=job
        print(self.pname,self.addr,self.job)

class Child:
    def m2(self,cname,age):
        self.cname=cname
        self.age=age
        print(self.cname,self.age)

class Subchild(Child,Parent):
    def m3(self,community):
        self.community=community
        print(self.community)

obj=Subchild()
obj.m1("Abraham","Thundil Kripa","Bank Employee")
obj.m2("Alina",22,)
obj.m3("Christian")
