students = [
    {"Name": "Ravi", "Maths": 78, "Science": 88, "English": 80},
    {"Name": "Anu", "Maths": 85, "Science": 79, "English": 86},
    {"Name": "Kiran", "Maths": 90, "Science": 92, "English": 85},
    {"Name": "Meena", "Maths": 67, "Science": 70, "English": 72}
]

topper = None
highest_total = 0

print("Name\tMaths\tScience\tEnglish\tTotal\tAverage")

for s in students:
    total = s["Maths"] + s["Science"] + s["English"]
    average = total / 3

    print(s["Name"], "\t", s["Maths"], "\t", s["Science"],
          "\t", s["English"], "\t", total, "\t", round(average, 2))

    if total > highest_total:
        highest_total = total
        topper = s["Name"]

print("\nTopper:", topper)
print("Highest Total:", highest_total)
