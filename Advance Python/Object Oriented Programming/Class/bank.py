class Bank:
    bname="sbi"
    def acCreate(self,acno,name):
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal

    def deposit(self,amt):
        self.amt=amt
        self.balance+=self.amt
        print("your",Bank.bname,"account has been created",self.amt)
        print("your current balance",self.balance)

    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amnt)
            self.balance-=self.amnt
            print("available balance",self.balance)

obj=Bank()
obj.acCreate(345178,"sathyasheelan")
obj.deposit(4555)
obj.withdraw(6345)