class Account:

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def add_money(self, amount):
        self._balance += amount

    def withdraw_money(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self._balance