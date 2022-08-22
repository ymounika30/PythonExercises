##create a banking application,to check current balance,to deposite,to withdraw.
##
##account class
##atributes-name,balance,min_balance
##methods-deposite,withdraw,printstatement
##
##currentaccount class.....currentaccount balance
##atributes-name,balance
##methods- __str__
##give min_balance
##
##
##saving account class.....currentaccount balance
##atributes-name,balance
##methods- __str__
##
##deposit rs.5000 in saving account
##withdraw rs.7000 from saving
##
##input:
##1.print current balance
##2.print current balance after deposit-5000
##3.print current balance after withdraw-10000
##4.withdraw 6000 rupees
##
##output:
##1.print current balance 10000
##2.print current balance after deposit-15000
##3.print current balance after withdraw-5000
##4.insufficient balance

class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print("Insufficient funds")
    def print_statement(self):
        print("Account Balance",self.balance)
class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-15000)
    def __str__(self):
        return "{} Current account with balance: {}".format(self.name,self.balance)
class Saving(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return "{} Savings account with balance: {}".format(self.name,self.balance)
s=Saving("Mounika",5000000)
s.deposit(100000)
s.print_statement()
s.withdraw(10000)
print(s)
