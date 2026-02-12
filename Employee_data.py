def employee_info(name, salary, department="General", location="India"):
    print("\n--- Employee Info ---")
    print("Name       :", name)
    print("Salary     :", salary)
    print("Department :", department)
    print("Location   :", location)


employee_info(name="Gayana", salary=50000)
employee_info(name="Gayana", salary=50000, location="Bangalore")
employee_info(salary=60000, name="Rahul", department="IT")
