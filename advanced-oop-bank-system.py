class BankUser:
    
    def __init__(self, username, password, age, balance=0):
        self.username = username
        self.password = password
        self.age = age
        self.balance = balance
        self.transactions = []   # Store transaction history
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print("Deposit Successful ✅")
        print("Current Balance:", self.balance)
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal Successful ✅")
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance ❌")
    
    def check_balance(self):
        print("Current Balance:", self.balance)
    
    def mini_statement(self):
        print("\n--- Mini Statement ---")
        if len(self.transactions) == 0:
            print("No transactions yet.")
        else:
            for t in self.transactions[-5:]:  # show last 5 transactions
                print(t)
    
    def display_profile(self):
        print("\n--- Account Details ---")
        print("Username:", self.username)
        print("Age:", self.age)
        print("Balance:", self.balance)
