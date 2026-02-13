students = [
    {"Name": "Ravi", "Maths": 78, "Science": 88, "English": 80},
    {"Name": "Anu", "Maths": 85, "Science": 79, "English": 86},
    {"Name": "Kiran", "Maths": 90, "Science": 92, "English": 85},
    {"Name": "Meena", "Maths": 67, "Science": 70, "English": 72}
]

# Function to calculate average
def get_average(student):
    total = student["Maths"] + student["Science"] + student["English"]
    return total / 3

# Sort by average (descending)
sorted_students = sorted(students, key=lambda s: get_average(s), reverse=True)

print("Students Sorted by Average Marks\n")

for s in sorted_students:
    avg = get_average(s)
    print(s["Name"], "-> Average:", round(avg, 2))
