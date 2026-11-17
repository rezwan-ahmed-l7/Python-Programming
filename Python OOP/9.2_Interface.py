from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class Cash(Payment):

    def pay(self, amount):
        print("Cash:", amount)


class Card(Payment):

    def pay(self, amount):
        print("Card:", amount)


class Bkash(Payment):

    def pay(self, amount):
        print("Bkash:", amount)


cash = Cash()
card = Card()
bkash = Bkash()

cash.pay(500)
card.pay(1000)
bkash.pay(1500)