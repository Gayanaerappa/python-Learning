import os

FILE_NAME = "passwords.txt"

# Simple encryption (not very strong, just for learning)
def encrypt(text):
    return "".join(chr(ord(char) + 2) for char in text)

def decrypt(text):
    return "".join(chr(ord(char) - 2) for char in text)

def add_password():
    website = input("Enter website/app name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{website},{username},{encrypt(password)}\n")

    print("✅ Password saved successfully!")

def view_passwords():
    if not os.path.exists(FILE_NAME):
        print("No data found!")
        return

    with open(FILE_NAME, "r") as f:
        print("\n--- Saved Passwords ---")
        for line in f:
            website, username, password = line.strip().split(",")
            print(f"Website: {website}, Username: {username}, Password: {decrypt(password)}")

def search_password():
    site = input("Enter website to search: ")
    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                website, username, password = line.strip().split(",")
                if website.lower() == site.lower():
                    print(f"Found → Username: {username}, Password: {decrypt(password)}")
                    found = True
                    break

    if not found:
        print("❌ Not found!")

def menu():
    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            search_password()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

menu()
