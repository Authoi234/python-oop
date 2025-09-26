# Encapsulation

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

# account = BadBankAccount(0.0)
# account.balance = -1
# print(account.balance)  # -1

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, ammount):
        if ammount <= 0:
            raise ValueError("Deposit ammount must be positive.")
        self._balance += ammount

    def withdraw(self, ammount):
        if ammount <= 0:
            raise ValueError("Withdraw ammount must be positive.")
        if ammount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= ammount

account = BankAccount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1.00)
print(account.balance)