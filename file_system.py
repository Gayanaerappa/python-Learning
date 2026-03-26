import os

def create_file():
    file_name = input("Enter file name: ")
    if os.path.exists(file_name):
        print("File already exists!")
    else:
        with open(file_name, 'w') as f:
            print("File created successfully!")

def write_file():
    file_name = input("Enter file name: ")
    data = input("Enter data to write: ")
    with open(file_name, 'w') as f:
        f.write(data)
    print("Data written successfully!")

def read_file():
    file_name = input("Enter file name: ")
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            print("\nFile Content:\n")
            print(f.read())
    else:
        print("File does not exist!")

def append_file():
    file_name = input("Enter file name: ")
    data = input("Enter data to append: ")
    with open(file_name, 'a') as f:
        f.write("\n" + data)
    print("Data appended successfully!")

def delete_file():
    file_name = input("Enter file name: ")
    if os.path.exists(file_name):
        os.remove(file_name)
        print("File deleted successfully!")
    else:
        print("File not found!")

def menu():
    while True:
        print("\n===== FILE HANDLING SYSTEM =====")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Append File")
        print("5. Delete File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_file()
        elif choice == '2':
            write_file()
        elif choice == '3':
            read_file()
        elif choice == '4':
            append_file()
        elif choice == '5':
            delete_file()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

# Run program
menu()
