class Account:
    def __init__(self, bal, acc):           # Dunder Function >>   ""  __init__ ""      # __init__  একে বলা হয়  initialize constructor method
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Taka", amount, "was dabit.")
        print('total balance =', self.get_balance())

    def creadit(self, amount):
        self.balance += amount
        print("taka", amount, "was creadit")
        print('total balance =', self.get_balance())

    def get_balance(self):
        return self.balance

account = Account(20000, 238)
print(account.balance)
print(account.account_no)
account.debit(600)
account.creadit(700)
account.debit(6000)
account.debit(14000)
account.creadit(50000)



