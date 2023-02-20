class BankAccount:
    def __init__(self,acno,name,type,balance):
        self.acno=acno
        self.name=name
        self.type=type
        self.balance=balance
    def display(self):
        print()
        print("A/c no:",self.acno)
        print("Name of a/c holder:",self.name)
        print("A/c Type:",self.type," a/c")
        print("Total balance:",self.balance)
        print()
    def deposit(self,dpamount):
        print(dpamount,"RS/- Deposited to  a/c no ",self.acno)
        self.balance=self.balance+dpamount
        print("Total balance = ",self.balance)
    def withdrawal(self,wamount):
        print(wamount, "RS/- Withdraw from  a/c no ", self.acno)
        self.balance = self.balance - wamount
        print("Total balance = ", self.balance)
ac1=BankAccount(7476545444,"Anjana","savings",450000)
ac1.display()
ac1.deposit(5000)
ac1.withdrawal(2000)
