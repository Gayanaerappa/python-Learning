students = [
    {"Name": "Ravi", "Marks": 78},
    {"Name": "Anu", "Marks": 85},
    {"Name": "Kiran", "Marks": 67},
    {"Name": "Meena", "Marks": 90},
    {"Name": "John", "Marks": 72}
]

# Sort by marks (ascending)
sorted_students = sorted(students, key=lambda s: s["Marks"])

second_lowest = sorted_students[1]

print("Second Lowest Scorer:")
print("Name:", second_lowest["Name"])
print("Marks:", second_lowest["Marks"])
