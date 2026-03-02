import tkinter as tk
from tkinter import messagebox

# ------------------ Bank User Class ------------------

class BankUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            return True
        return False


# ------------------ Bank System ------------------

class BankSystem:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = BankUser(username, password)
        return True

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.current_user = self.users[username]
            return True
        return False


# ------------------ GUI Application ------------------

bank = BankSystem()
root = tk.Tk()
root.title("Banking Management System")
root.geometry("400x400")


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


# ------------------ Main Menu ------------------

def main_menu():
    clear_screen()

    tk.Label(root, text="Banking System", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Register", width=20, command=register_screen).pack(pady=10)
    tk.Button(root, text="Login", width=20, command=login_screen).pack(pady=10)


# ------------------ Register ------------------

def register_screen():
    clear_screen()

    tk.Label(root, text="Register").pack(pady=10)

    username_entry = tk.Entry(root)
    username_entry.pack()

    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def register_user():
        username = username_entry.get()
        password = password_entry.get()

        if bank.register(username, password):
            messagebox.showinfo("Success", "Account Created Successfully")
            main_menu()
        else:
            messagebox.showerror("Error", "Username already exists")

    tk.Button(root, text="Submit", command=register_user).pack(pady=10)
    tk.Button(root, text="Back", command=main_menu).pack()


# ------------------ Login ------------------

def login_screen():
    clear_screen()

    tk.Label(root, text="Login").pack(pady=10)

    username_entry = tk.Entry(root)
    username_entry.pack()

    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def login_user():
        username = username_entry.get()
        password = password_entry.get()

        if bank.login(username, password):
            messagebox.showinfo("Success", "Login Successful")
            user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    tk.Button(root, text="Login", command=login_user).pack(pady=10)
    tk.Button(root, text="Back", command=main_menu).pack()


# ------------------ User Dashboard ------------------

def user_dashboard():
    clear_screen()

    tk.Label(root, text=f"Welcome {bank.current_user.username}").pack(pady=10)

    tk.Button(root, text="Deposit", width=20, command=deposit_screen).pack(pady=5)
    tk.Button(root, text="Withdraw", width=20, command=withdraw_screen).pack(pady=5)
    tk.Button(root, text="Check Balance", width=20, command=check_balance).pack(pady=5)
    tk.Button(root, text="Mini Statement", width=20, command=mini_statement).pack(pady=5)
    tk.Button(root, text="Logout", width=20, command=main_menu).pack(pady=5)


def deposit_screen():
    amount = tk.simpledialog.askfloat("Deposit", "Enter Amount:")
    if amount:
        bank.current_user.deposit(amount)
        messagebox.showinfo("Success", "Amount Deposited")


def withdraw_screen():
    amount = tk.simpledialog.askfloat("Withdraw", "Enter Amount:")
    if amount:
        if bank.current_user.withdraw(amount):
            messagebox.showinfo("Success", "Withdrawal Successful")
        else:
            messagebox.showerror("Error", "Insufficient Balance")


def check_balance():
    balance = bank.current_user.balance
    messagebox.showinfo("Balance", f"Current Balance: {balance}")


def mini_statement():
    transactions = bank.current_user.transactions
    if not transactions:
        messagebox.showinfo("Mini Statement", "No Transactions Yet")
    else:
        statement = "\n".join(transactions[-5:])
        messagebox.showinfo("Mini Statement", statement)


# Start App
main_menu()
root.mainloop()
