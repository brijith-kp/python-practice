# Python Encapsulation

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    # Display balance
    def get_balance(self):
        return self.__balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance or invalid amount")


# Creating object
account = BankAccount("Brijith", 5000)

print("Owner:", account.owner)
print("Balance:", account.get_balance())

account.deposit(1000)
account.withdraw(2000)

print("Final Balance:", account.get_balance())
