balance = 5000

try:
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful ✅")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance ❌")

except ValueError:
    print("Invalid input ❌ Please enter numbers only")
