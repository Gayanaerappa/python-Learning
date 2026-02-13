students = [
    {"Name": "Ravi", "Maths": 78, "Science": 88, "English": 80},
    {"Name": "Anu", "Maths": 85, "Science": 79, "English": 86},
    {"Name": "Kiran", "Maths": 90, "Science": 92, "English": 85},
    {"Name": "Meena", "Maths": 35, "Science": 40, "English": 50}
]

# Helper functions
def get_total(s):
    return s["Maths"] + s["Science"] + s["English"]

def get_average(s):
    return get_total(s) / 3

def get_grade(avg):
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

# Sort for ranking
ranked_students = sorted(students, key=lambda s: get_total(s), reverse=True)

print("Rank\tName\tTotal\tAverage\tGrade\tResult")

rank = 1
for s in ranked_students:
    total = get_total(s)
    avg = get_average(s)
    grade = get_grade(avg)
    result = "Pass" if grade != "Fail" else "Fail"

    print(rank, "\t", s["Name"], "\t", total, "\t",
          round(avg, 2), "\t", grade, "\t", result)

    rank += 1
