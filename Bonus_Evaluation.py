name = input("Enter Employee Name: ")
experience = int(input("Enter Years of Experience: "))
rating = float(input("Enter Performance Rating (1 to 5): "))
salary = float(input("Enter Current Salary: "))

if experience >= 2:
    print("\nEligible for Bonus Evaluation")
    
    if rating >= 4.5:
        bonus = salary * 0.20
        print("Congratulations! Promotion Granted 🎉")
        print("Bonus Amount:", bonus)
    
    elif rating >= 3:
        bonus = salary * 0.10
        print("Good Performance 👍")
        print("Bonus Amount:", bonus)
    
    else:
        print("No Bonus. Improve Performance.")
        
else:
    print("\nNot Eligible for Bonus (Minimum 2 Years Required)")
