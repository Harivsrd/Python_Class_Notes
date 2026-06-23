class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_name}: Deposited {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.account_name}: Withdrawn {amount}, Balance: {self.balance}")
        else:
            print(f"{self.account_name}: Insufficient funds!")

    def __add__(self, other):
        return BankAccount(f"{self.account_name}+{other.account_name}", self.balance + other.balance)

    def __sub__(self, other):
        return BankAccount(f"{self.account_name}-{other.account_name}", self.balance - other.balance)

    def __mul__(self, other):
        return BankAccount(f"{self.account_name}*{other.account_name}", self.balance * other.balance)

    def __truediv__(self, other):
        if other.balance != 0:
            return BankAccount(f"{self.account_name}/{other.account_name}", self.balance / other.balance)
        else:
            raise ZeroDivisionError("Cannot divide by zero balance!")

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __str__(self):
        return f"{self.account_name} Balance: {self.balance}"


savings = BankAccount("Savings", 5000)
current = BankAccount("Current", 3000)

savings.deposit(1000)    
current.withdraw(500)     
print(savings + current)  
print(savings - current)   
print(savings * current)   
print(savings / current)   
print(savings == current)  
print(savings > current)  
print(savings < current)   
