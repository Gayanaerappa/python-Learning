students = [
    {"Name": "Ravi", "Maths": 78, "Science": 88, "English": 80},
    {"Name": "Anu", "Maths": 85, "Science": 79, "English": 86},
    {"Name": "Kiran", "Maths": 90, "Science": 92, "English": 85},
    {"Name": "Meena", "Maths": 67, "Science": 70, "English": 72}
]

# Function to calculate total
def get_total(student):
    return student["Maths"] + student["Science"] + student["English"]

# Sort by total marks (descending)
sorted_students = sorted(students, key=lambda s: get_total(s), reverse=True)

print("Students Sorted by Total Marks\n")

for s in sorted_students:
    total = get_total(s)
    print(s["Name"], "-> Total:", total)
