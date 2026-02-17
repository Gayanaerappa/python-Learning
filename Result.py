students = []

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("\nEnter student name: ")
    marks = []

    for i in range(3):
        mark = int(input(f"Enter subject {i+1} marks: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 3
    grade = calculate_grade(average)

    students.append({
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade
    })

print("\n--- Student Report ---")
print("Name\tTotal\tAverage\tGrade")

for s in students:
    print(s["Name"], "\t", s["Total"], "\t",
          round(s["Average"], 2), "\t", s["Grade"])

# Find Topper
topper = max(students, key=lambda s: s["Total"])

print("\n🏆 Topper:", topper["Name"])
print("Highest Marks:", topper["Total"])
