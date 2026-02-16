balance = 0

def check_balance():
    print("💰 Current Balance:", balance)

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("✅ Amount Deposited")

def withdraw():
    global balance
    amount = float(input("Enter withdraw amount: "))

    if amount <= balance:
        balance -= amount
        print("✅ Withdrawal Successful")
    else:
        print("❌ Insufficient Balance")

# ===== MAIN MENU =====

while True:
    print("\n===== Simple Bank System =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("👋 Thank you for using the bank system")
        break

    else:
        print("❌ Invalid Choice")
