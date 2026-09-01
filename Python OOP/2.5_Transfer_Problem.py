class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount")

    def getBalance(self):
        return self.__balance


a1 = BankAccount("Sara", 5000)

a1.deposit(2000)
a1.withdraw(1000)

print("Name:", a1.name)
print("Balance:", a1.getBalance())