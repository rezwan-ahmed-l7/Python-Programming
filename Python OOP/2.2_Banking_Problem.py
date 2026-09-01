class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def debit(self, amount):
        self.balance = self.balance - amount

    def credit(self, amount):
        self.balance = self.balance + amount

    def display(self):
        print("Name: ", self.name)
        print("Balance: ", self.balance)

a = Account("Sara", 9000)
a.debit(500)
a.display()
a.credit(1500)
a.display()