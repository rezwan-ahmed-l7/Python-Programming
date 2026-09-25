class Account:

    def __init__(self, balance):
        self.balance = balance

    def show(self):
        print("Balance:", self.balance)

class SavingsAccount(Account):

    def show(self):
        super().show()
        print("Account Type: Savings")

class CurrentAccount(Account):

    def show(self):
        super().show()
        print("Account Type: Current")

s1 = SavingsAccount(5000)
c1 = CurrentAccount(10000)

s1.show()

print()

c1.show()