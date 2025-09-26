# Static Method

class BankAccount:
    MIN_BALANCE = 100 

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, ammount):
        if self.is_valid_ammount(ammount):
            self._balance += ammount
            self.__log_transaction("deposit", ammount)
            print(f"{self.owner}'s new balance: {self._balance}.")
        else:
            print("Deposit ammount must be positive.")

    def is_valid_ammount(self, ammount):
        return ammount > 0

    def __log_transaction(self, transaction_type , ammount): # private method . Cant be accessed outside the class
        print(f"Logging {transaction_type} of ${ammount}. New balance: ${self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(200)

account = BankAccount("ali", 800)
account.deposit(700)

print(BankAccount.is_valid_interest_rate(3))  # True
print(BankAccount.is_valid_interest_rate(7))  # False