# Static Method

class BankAccount:
    MIN_BALANCE = 100 

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, ammount):
        pass
