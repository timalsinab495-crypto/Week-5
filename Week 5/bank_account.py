# Question 1 - Bank Account Manager
# Cooperative Bank, Lalitpur

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        print(f"{self.name}: Rs. {self.balance}")


# --- Test ---

accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai",   "A003", 12000),
]

# Create objects
a1 = BankAccount(*accounts[0])
a2 = BankAccount(*accounts[1])
a3 = BankAccount(*accounts[2])

# Deposit 3000 into A002
a2.deposit(3000)

# Withdraw 15000 from A003 (should fail)
a3.withdraw(15000)

# Withdraw 2000 from A001
a1.withdraw(2000)

# Print final balances
print("\n--- Final Balances ---")
a1.get_balance()
a2.get_balance()
a3.get_balance()