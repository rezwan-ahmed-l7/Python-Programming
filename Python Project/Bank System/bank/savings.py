from .account import Account


class SavingsAccount(Account):

    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest

    def add_money(self, amount):
        self._balance += amount

    def withdraw_money(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient Balance")

    def calculate_interest(self):
        return self._balance * self.interest / 100

    def calculate_total_balance(self):
        return self._balance + self.calculate_interest()