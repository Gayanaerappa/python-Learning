print("===== Student Marks Management System =====")

num_students = int(input("Enter number of students: "))

marks_list = []

# Loop to get marks
for i in range(num_students):
    marks = float(input(f"Enter marks for student {i+1}: "))
    marks_list.append(marks)

# Calculate total
total = 0
for mark in marks_list:
    total += mark

# Calculate average
average = total / num_students

# Find highest and lowest
highest = max(marks_list)
lowest = min(marks_list)

# Display results
print("\n===== Result =====")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
