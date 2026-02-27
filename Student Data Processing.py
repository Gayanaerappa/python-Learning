print("===== Student Data Processing System =====")

students = [
    {"name": "Ravi", "marks": 85},
    {"name": "Anu", "marks": 72},
    {"name": "Kiran", "marks": 90},
    {"name": "Meena", "marks": 60},
    {"name": "Arjun", "marks": 78}
]

# 1️⃣ Display all students
print("\nAll Students:")
for s in students:
    print(s)

# 2️⃣ Add 5 grace marks using map + lambda
grace_marks = list(map(lambda x: {"name": x["name"], 
                                  "marks": x["marks"] + 5}, students))

print("\nAfter Adding Grace Marks:")
for s in grace_marks:
    print(s)

# 3️⃣ Filter students who scored above 80
top_students = list(filter(lambda x: x["marks"] > 80, grace_marks))

print("\nTop Students (Marks > 80):")
for s in top_students:
    print(s)

# 4️⃣ Sort students by marks (Descending)
sorted_students = sorted(grace_marks, key=lambda x: x["marks"], reverse=True)

print("\nSorted Students (High to Low):")
for s in sorted_students:
    print(s)

# 5️⃣ Find highest marks using lambda
highest = max(grace_marks, key=lambda x: x["marks"])
print("\nHighest Scorer:", highest)
