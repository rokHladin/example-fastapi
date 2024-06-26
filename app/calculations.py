def add(a: int, b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


def multiply(a: int, b: int):
    return a * b


def divide(a: int, b: int):
    return a / b

class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds in account")
        self.balance -= amount
        return self.balance

    def collect_interest(self):
        self.balance *= 1.1
