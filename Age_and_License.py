age = int(input("Enter your age: "))
has_license = input("Do you have license? (yes/no): ")

if age >= 18:
    if has_license == "yes":
        print("You can drive")
    else:
        print("You need a driving license")
else:
    print("You are underage")
