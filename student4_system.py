import os

FILE_NAME = "students.txt"

def add_student():
    with open(FILE_NAME, "a") as f:
        name = input("Enter student name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")
        f.write(f"{name},{age},{course}\n")
    print("✅ Student added successfully!")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found!")
        return
    
    with open(FILE_NAME, "r") as f:
        data = f.readlines()
        if not data:
            print("No records available!")
        else:
            print("\n--- Student Records ---")
            for line in data:
                name, age, course = line.strip().split(",")
                print(f"Name: {name}, Age: {age}, Course: {course}")

def search_student():
    name_to_search = input("Enter student name to search: ")
    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, age, course = line.strip().split(",")
                if name.lower() == name_to_search.lower():
                    print(f"Found → Name: {name}, Age: {age}, Course: {course}")
                    found = True
                    break

    if not found:
        print("❌ Student not found!")

def delete_student():
    name_to_delete = input("Enter student name to delete: ")
    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            for line in lines:
                name, age, course = line.strip().split(",")
                if name.lower() != name_to_delete.lower():
                    f.write(line)
                else:
                    found = True

    if found:
        print("🗑️ Student deleted successfully!")
    else:
        print("❌ Student not found!")

def menu():
    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

menu()
